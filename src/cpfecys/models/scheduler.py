# coding: utf8
if not request.env.web2py_runtime_gae:
    ## if NOT running on Google App Engine use SQLite or other DB
    db3 = DAL('mysql://root@localhost/cpfecys_scheduler',pool_size=1,check_reserved=['all'])
else:
    ## connect to Google BigTable (optional 'google:datastore://namespace')
    db3 = DAL('google:datastore://cpfecys_scheduler')
    ## store sessions and tickets there
    session.connect(request, response, db=db2)
    ## or store session in Memcache, Redis, etc.
    ## from gluon.contrib.memdb import MEMDB
    ## from google.appengine.api.memcache import Client
    ## session.connect(request, response, db = MEMDB(Client()))

def assignation_done_succesful(assignation):
    ## Validate Reports
    # Get all report restrictions that apply up to now
    # Start date to get them depends on assignation start
    # End date that apply to reports is current date
    # import cpfecys
    # import datetime
    #current_date = datetime.datetime.now()
    #start_date = datetime.date(assignation.period.yearp, 1, 1)
    #if assignation.period.period == cpfecys.second_period:
    #    start_date = datetime.date(assignation.period.yearp, 7, 1)
    #r_restrictions = db((db.report_restriction.start_date >= start_date)&
    #                    (db.report_restriction.end_date < current_date)&
    #                    (db.report_restriction.is_enabled == True)).select()
    # Check if they where delivered
    # Get all the reports of this assignation
    average_report = 0
    status = True
    message = ''
    total_reports = assignation.report.count()
    for report in assignation.report.select():
        # Check DTT Approval
        if report.dtt_approval is None:
            # I don't think status has to change since by average the student can win
            # status = False
            message += T('A report was not checked by DTT Admin. Contact Admin.')
            message += ' '
        elif report.dtt_approval is False:
            # I don't think status has to change since by average the student can win
            # status = False
            message += T('A report was not approved by DTT Admin. Thus considered failed.')
            message += ' '
        else:
            # Save for average grading
            average_report += (float(report.score)/float(total_reports))
    # Check the grade (average) to be beyond the expected minimal grade in current settings
    min_score = db(db.custom_parameters.id>0).select().first().min_score
    if average_report < min_score:
        #he lost the practice due to reports
        status = False
        message += T('To consider assignation to be valid, report grades should be above: ') + min_score
        message += ' '
        message += T('Reports Grade is below minimun note; that sets this assignation as lost.')
    ## Validate Items
    # Get all item restrictions that apply up to now
    # Ok, ive the assignation, it has my starting period of final practice and the length
    # assignation.period Holds the starting period, assignation.periods holds the ammount of them
    period = assignation.period
    import cpfecys
    for x in range (0, assignation.periods):
        # Get the item_restrictions for this period, for the area of the assignation,
        # removing the ones that don't belong to this assignation since are exceptions
        # and not allowing optionals
        rows = db((db.item_restriction.period == period)&
                  (db.item_restriction_area.area_level == assignation.project.area_level)&
                  (db.item_restriction_area.item_restriction == db.item_restriction.id)&
                  (db.item_restriction_exception.project == assignation.project.id)&
                  (db.item_restriction_exception.item_restriction != db.item_restriction.id)&
                  (db.item_restriction.optional == False)).select()
        for row in rows:
            items = row.item_restriction.item(db.item.is_active != False).select()
            if not items:
                status = False
                message += T('There is a missing deliverable item: ') + row.item_restriction.name + '.'
            elif len(items) == 0:
                status = False
                message += T('There is a missing deliverable item: ') + row.item_restriction.name + '.'
            elif (row.item_restriction.item_type.name == 'File'):
                #check there is an uploaded file
                if not items.first().uploaded_file:
                    status = False
                    message += T('There is not an uploaded file for: ') + row.item_restriction.name + ' item.'
            elif (row.item_restriction.item_type.name == 'Activity'):
                #check there is an activity
                if not items.first().done_activity:
                    status = False
                    message += T('Activity not completed: ') + row.item_restriction.name + '.'
            elif (row.item_restriction.item_type.name == 'Grade Activity'):
                #check there is an activity with minimun grade
                if items.first().score < items.first().min_score:
                    status = False
                    message += T('Activity: ') + row.item_restriction.name + ' ' + T('has not met minimal score of: ') + str(items.first().min_score) + '.'
            elif (row.item_restriction.item_type.name == 'Schedule'):
                #check there is an activity
                if not items.first().item_schedule.count():
                    status = False
                    message += T('Schedule is missing: ') + row.item_restriction.name + '.'
        if (period.period == cpfecys.first_period):
            #this means the next one is second period of the same year
            period = db.period_year(yearp = period.yearp, period = cpfecys.second_period)
        else:
            #this means the next one is first period of the next year
            period = db.period_year(yearp = period.yearp + 1, period = cpfecys.first_period)
        if period == None:
            break
    # Check if they where delivered
    return {'status':status, 'message':message}

# Auto Freeze happens automatically, it FREEZES the assignation when it ends.
# Successful means all needed reports and items where delivered
# Failed means something was not good :( too bad
def auto_freeze():
    # Get the current month and year
    import datetime
    current_date = datetime.datetime.now()
    current_month = T(current_date.strftime("%B"))
    current_year = current_date.year
    # Get every period that has to be autoasigned within current month
    periods_to_work = db(db.assignation_freeze.pmonth == current_month).select()
    # For each assignation_freeze
    for period in periods_to_work:
        current_period_year = db.period_year((db.period_year.period == period)&
                                             (db.period_year.yearp == current_year))
        # this period means that we should check the ones that end in first_semester for example
        # or the ones that end in second_semester; it always applies to current year
        # Get all the assignations still active
        assignations = db(db.user_project.assignation_status == None).select()
        # Validate each assignation
        for assignation in assignations:
            # Obtengo el inicio de la asignacion
            ass_id = assignation.period.id
            # Obtengo la duracion
            length = assignation.periods
            # finaliza en (id de cuando finaliza en period_year)
            finish = ass_id + length
            final = db.period_year(id = finish)
            if final and current_period_year:
                if final.id == current_period_year.id:
                    validation = assignation_done_succesful(assignation)
                    if validation['status']:
                        assignation.assignation_comment = validation['message']
                        assignation.assignation_status = db.assignation_status(name = 'Successful')
                    else:
                        assignation.assignation_comment = validation['message']
                        assignation.assignation_status = db.assignation_status(name = 'Failed')
                    assignation.update_record()
    db.commit()


def check_exception_semester_repeat():
    import datetime
    import cpfecys
    cperiod = cpfecys.current_year_period()
    year = str(cperiod.yearp)
    cdate = datetime.datetime.now()
    compareDate = datetime.datetime(cdate.year, cdate.month, cdate.day)
    #compareDate = datetime.strptime( + '-'+cdate.month+'-'+cdate.day, "%Y-%m-%d")
    if cperiod.period == 1:
        #Period
        initSemester = datetime.datetime(cdate.year, 1, 1)
        #Time exception for the courses
        extraTime = datetime.datetime(cdate.year, 3, 1)

        if compareDate==initSemester:
            db(db.course_limit_exception.semester_repet==False).delete()
            db(db.course_limit_exception.semester_repet==True).update(date_finish=extraTime)
        else:			
            exceptions = db((db.course_limit_exception.date_finish<initSemester)).select()
            if exceptions.first() is not None:
                for exception in exceptions:
                    if exception.semester_repet==True:
                        db(db.course_limit_exception.id==exception.id).update(date_finish=extraTime)
                    else:
                        db(db.course_limit_exception.id==exception.id).delete()
    else:
        #Period
        #initSemester = datetime.strptime(year + '-06-01', "%Y-%m-%d")
        initSemester = datetime.datetime(cdate.year, 6, 1)
        #Time exception for the courses
        #extraTime = datetime.strptime(year + '-09-01', "%Y-%m-%d")
        extraTime = datetime.datetime(cdate.year, 9, 1)

        if compareDate==initSemester:
            db(db.course_limit_exception.semester_repet==False).delete()
            db(db.course_limit_exception.semester_repet==True).update(date_finish=extraTime)
        else:
            exceptions = db((db.course_limit_exception.date_finish<initSemester)).select()
            if exceptions.first() is not None:
                for exception in exceptions:
                    if exception.semester_repet==True:
                        db(db.course_limit_exception.id==exception.id).update(date_finish=extraTime)
                    else:
                        db(db.course_limit_exception.id==exception.id).delete()	
    db.commit()

def automation_evaluations():
    import datetime
    import cpfecys
    cperiod = cpfecys.current_year_period()
    year = str(cperiod.yearp)
    cdate = datetime.datetime.now()

    #First Semester date start
    initSemester = datetime.date(cdate.year, 1, 1)
    #Second Semester date start
    initSemester2 = datetime.date(cdate.year, 6, 1)

    #First Semester
    if cperiod.period == 1:
    
            
        evaluations = db((db.evaluation.date_finish<initSemester)).select()
        if evaluations.first() is not None:
            for evaluation in evaluations:
                if evaluation.semester_repeat==True:
                    db(db.evaluation.id==evaluation.id).update(semester_repeat=False)
                    
                    if (evaluation.date_start.month == 12 or evaluation.date_start.month == 11):
                        sum_month_1 = 5
                    else:
                        sum_month_1 = 6

                    if evaluation.date_finish.month == 12:
                        sum_month_2 = 5
                    else:
                        sum_month_2 = 6

                                
                    
                    date_start_temp = evaluation.date_start + relativedelta.relativedelta(months=sum_month_1)
                    date_finish_temp = evaluation.date_finish + relativedelta.relativedelta(months=sum_month_2)
                    
                    db.evaluation.insert(date_start=date_start_temp,
                                            date_finish=date_finish_temp,
                                            semester_repeat=True,                                                
                                            description=evaluation.description,
                                            repository_evaluation=evaluation.repository_evaluation)
                    
    #Second Semester
    else:            
        evaluations = db((db.evaluation.date_finish<initSemester2)).select()
        if evaluations.first() is not None:
            for evaluation in evaluations:
                if evaluation.semester_repeat==True:
                    db(db.evaluation.id==evaluation.id).update(semester_repeat=False)
                    
                    sum_month_1 = 6

                    if evaluation.date_finish.month == 5:
                        sum_month_2 = 7
                    else:
                        sum_month_2 = 6
                    
                    from dateutil import relativedelta
                    
                    date_start_temp = evaluation.date_start + relativedelta.relativedelta(months=sum_month_1)
                    date_finish_temp = evaluation.date_finish + relativedelta.relativedelta(months=sum_month_2)
                    
                    db.evaluation.insert(date_start=evaluation.date_start + datetime.timedelta(date_start_temp),
                                            date_finish=evaluation.date_finish + datetime.timedelta(date_finish_temp),
                                            semester_repeat=True,                                                
                                            description=evaluation.description,
                                            repository_evaluation=evaluation.repository_evaluation)
    db.commit()

def automation_activities_assigned():
    #ACTUAL AND FUTURE TIME
    import time
    from datetime import date, datetime, timedelta
    officialTime = date.today()
    futureTime = officialTime + timedelta(days=1)
    #CURRENT PERIOD
    import cpfecys
    year = cpfecys.current_year_period()
    #ALL ACTIVITIES OF THE CURRENT PERIOD
    for activity in db(db.course_assigned_activity.semester==year.id).select():
        if activity.status==T('Pending') and activity.date_start==futureTime:
            #REMINDER
            subject = T('[DTT]Automatic Notification - Reminder activity assigned by the professor')
            message = '<html>' +T('You are reminded that tomorrow should develop the following activity:')+'<br>'
            message += T('Activity data:')+'<br>'
            message += T('Name')+': '+activity.name+'<br>'
            message += T('Description')+': '+activity.description+'<br>'
            message += T('Date')+': '+str(activity.date_start)+'<br>'
            if activity.report_required == True:
                message += T('Report Required')+': '+T('You need to enter a report of the activity to be taken as valid.')+'<br>'
            message += activity.assignation.name+'<br>'+T(activity.semester.period.name)+' '+str(activity.semester.yearp)+'<br>Sistema de Seguimiento de La Escuela de Ciencias y Sistemas<br> Facultad de Ingeniería - Universidad de San Carlos de Guatemala</html>'
            #Log General del Envio
            row = db.notification_general_log4.insert(subject=subject,
                                                sent_message=message,
                                                emisor='DTT-ECYS',
                                                course=activity.assignation.name,
                                                yearp=activity.semester.yearp,
                                                period=T(activity.semester.period.name))
            ListadoCorreos=None
            email_list_log=None
            students = db((db.user_project.project == activity.assignation)&
                      ((db.user_project.period <= activity.semester) & ((db.user_project.period + db.user_project.periods) > activity.semester))&
                      (db.user_project.assigned_user == db.auth_user.id)&
                      (db.auth_membership.user_id == db.auth_user.id)&
                      (db.auth_membership.group_id == db.auth_group.id)&
                      (db.auth_group.role == 'student')).select()

            for usersT in students:
                if ListadoCorreos is None:
                    ListadoCorreos=[]
                    email_list_log=usersT.auth_user.email
                else:
                    email_list_log+=','+usersT.auth_user.email
                ListadoCorreos.append(usersT.auth_user.email)

            if ListadoCorreos is not None:
                was_sent = mail.send(to='dtt.ecys@dtt-ecys.org',subject=subject,message=message, bcc=ListadoCorreos)
                db.mailer_log.insert(sent_message = message, destination = email_list_log, result_log = str(mail.error or '') + ':' + str(mail.result), success = was_sent, emisor='DTT-ECYS')
                #Notification LOG
                email_list =str(email_list_log).split(",")
                for email_temp in email_list:
                    user_var = db((db.auth_user.email == email_temp)).select().first()
                    if user_var is not None:
                        username_var = user_var.username
                    else:
                        user_var = db((db.academic.email == email_temp)).select().first()
                        if user_var is not None:
                            username_var = user_var.carnet
                        else:
                            username_var = 'None'
                    db.notification_log4.insert(destination = email_temp, 
                                                username = username_var,
                                                result_log = str(mail.error or '') + ':' + str(mail.result), 
                                                success = was_sent, 
                                                register=row.id)
        elif activity.status==T('Pending') and activity.date_start==officialTime:
            db(db.course_assigned_activity.id == activity.id).update(status = T('Active'))
        elif (activity.status==T('Active') and activity.date_start<officialTime) or (activity.status==T('Pending') and activity.date_start<officialTime):
            status = T('Completed')
            #Activity requires report
            if activity.report_required==True:
                if activity.fileReport is None:
                    status = T('Pending') +' '+T('Item Delivery')
                else:
                    if activity.automatic_approval==False:
                        status = T('Grade pending')
            else:
                if activity.automatic_approval==False:
                    status = T('Grade pending')
            db(db.course_assigned_activity.id == activity.id).update(status = status)
    db.commit()





#This thing kills reports that where never done to an empty report with score 0
def auto_daily():
    ## Get current year period
    import cpfecys
    currentyear_period = cpfecys.current_year_period()
    ## Get all report_restriction of this period_year that end_date is beyond today
    import datetime
    current_date = datetime.datetime.now()
    #if it is the first semester then the restriction should be:
    #start date >= January 1 year 00:00:00
    #end date >= January 1 year 00:00:00
    #start date < July 1 year 00:00:00
    #end date < July 1 year 00:00:00
    #if it is the second semester then the restriction should be:
    #start date >= July 1 year 00:00:00
    #end date >= July 1 year 00:00:00
    #start date < Jan 1 year 00:00:00
    #end date < Jan 1 year 00:00:00
    if currentyear_period.period == cpfecys.first_period.id:
        date_min = datetime.datetime(currentyear_period.yearp, 1, 1)
        date_max = datetime.datetime(currentyear_period.yearp, 7, 1)
    else:
        date_min = datetime.datetime(currentyear_period.yearp, 7, 1)
        date_max = datetime.datetime(currentyear_period.yearp, 1, 1)
    expired_restrictions = db((db.report_restriction.end_date < current_date)&
                              (db.report_restriction.start_date >= date_min)&
                              (db.report_restriction.end_date >= date_min)&
                              (db.report_restriction.start_date < date_max)&
                              (db.report_restriction.end_date < date_max)&
                              (db.report_restriction.is_enabled == True)).select()
    ## Get all assignations for this period_year
    semester_assignations = db((db.user_project.period <= currentyear_period.id)&
                     ((db.user_project.period + db.user_project.periods) > currentyear_period.id)).select()
    # For every assignation and restriction
    ## This makes all missed assignations automatically not sent and set to failed reports :(
    missed_reports = 0
    status_acceptance = db.report_status(db.report_status.name == 'Acceptance')
    for assignation in semester_assignations:
        for restriction in expired_restrictions:
            reports = db((db.report.assignation == assignation.id)&
                         (db.report.report_restriction == restriction.id)).count()
            if not(reports > 0):
                missed_reports += 1
                db.report.insert(assignation = assignation.id,
                                 min_score = cpfecys.get_custom_parameters().min_score,
                                 report_restriction = restriction.id,
                                 created = current_date,
                                 score = 0,
                                 status = status_acceptance,
                                 never_delivered = True,
                                 teacher_comment =  T('The period of time to create the report finished and it was never completed; so automatically it is considered as failed.'))
    ## This makes all 'Draft' reports that have no delivered anything to be set to failed!
    drafties = db((db.report.status == db.report_status(name = 'Draft'))&
               (db.report_restriction.end_date < current_date)&
               (db.report.report_restriction == db.report_restriction.id)&
               (db.report.heading == None)&
               (db.report.footer == None)&
               (db.report.desertion_started == None)&
               (db.report.desertion_gone == None)&
               (db.report.desertion_continued == None)&
               (db.report.hours == None)).select()
    total_drafties_empty = len(drafties)
    for d in drafties:
        d.report.score = 0
        d.report.status = db.report_status(name = 'Acceptance')
        d.report.teacher_comment =  T('The period of time to create the report finished and it was never completed; so automatically it is considered as failed.')
        d.report.never_delivered = True
        d.report.min_score = cpfecys.get_custom_parameters().min_score
        d.report.update_record()
##

    ## This makes all 'Draft' reports that expired get to 'Grading'
    drafties = db((db.report.status == db.report_status(name = 'Draft'))&
               (db.report_restriction.end_date < current_date)&
               (db.report.report_restriction == db.report_restriction.id)).select()
    total_drafties = len(drafties)
    import cpfecys
    signature = (cpfecys.get_custom_parameters().email_signature or '')
    for d in drafties:
        d.report.status = db.report_status(name = 'Grading')
        d.report.min_score = cpfecys.get_custom_parameters().min_score
        d.report.update_record()
        ## TODO: Send Email according to assignation
        # Notification Message
        me_the_user = d.report.assignation.assigned_user
        message = '<html>' + T('The report') + ' ' \
        + '<b>' + XML(d.report_restriction['name']) + '</b><br/>' \
        + T('sent by student: ') + XML(me_the_user.username) + ' ' \
        + XML(me_the_user.first_name) + ' ' + XML(me_the_user.last_name) \
        + '<br/>' \
        + T('was sent to be checked.') + '<br/>' + T('Checking can be done in:') \
        + ' ' + cpfecys.get_domain() + '<br />' + signature + '</html>'
        # send mail to teacher and student notifying change.
        mails = []
        # retrieve teacher's email
        teachers = db((db.project.id == d.report.assignation.project)&
                      (db.user_project.project == db.project.id)&
                      (db.user_project.assigned_user == db.auth_user.id)&
                      (db.auth_membership.user_id == db.auth_user.id)&
                      (db.auth_membership.group_id == db.auth_group.id)&
                      (db.auth_group.role == 'Teacher')).select()
        for teacher in teachers:
            mails.append(teacher.auth_user.email)
        # retrieve student's email
        student_mail = me_the_user.email
        mails.append(student_mail)
        was_sent = mail.send(to=mails,
                  subject=T('[DTT]Automatic Notification - Report ready to be checked.'),
                  # If reply_to is omitted, then mail.settings.sender is used
                  reply_to = student_mail,
                  message=message)
        #MAILER LOG
        db.mailer_log.insert(sent_message = message,
                             destination = ','.join(mails),
                             result_log = str(mail.error or '') + ':' + str(mail.result),
                             success = was_sent)
    ## This makes all 'Recheck' reports that expired to 'Grading'
    import datetime
    recheckies = db((db.report_restriction.id == db.report.report_restriction)&
                    (db.report.status == db.report_status(name='Recheck'))&
                    (db.report.score_date <= (current_date - datetime.timedelta(days = cpfecys.get_custom_parameters().rescore_max_days)))).select()
    total_recheckies = len(recheckies)
    import cpfecys
    signature = cpfecys.get_custom_parameters().email_signature
    for rech in recheckies:
        rech.report.status = db.report_status(name = 'Grading')
        rech.report.update_record()
        ## TODO: Send Email according to assignation
        me_the_user = rech.report.assignation.assigned_user
        message = '<html>' + T('The report') + ' ' \
        + '<b>' + XML(rech.report_restriction['name']) + '</b><br/>' \
        + T('sent by student: ') + XML(me_the_user.username) + ' ' \
        + XML(me_the_user.first_name) + ' ' + XML(me_the_user.last_name) \
        + '<br/>' \
        + T('was sent to be checked.') + '<br/>' + T('Checking can be done in:') \
        + ' ' + cpfecys.get_domain() + '<br />' + signature + '</html>'
        # send mail to teacher and student notifying change.
        mails = []
        # retrieve teacher's email
        teachers = db((db.project.id == rech.report.assignation.project)&
                      (db.user_project.project == db.project.id)&
                      (db.user_project.assigned_user == db.auth_user.id)&
                      (db.auth_membership.user_id == db.auth_user.id)&
                      (db.auth_membership.group_id == db.auth_group.id)&
                      (db.auth_group.role == 'Teacher')).select()
        for teacher in teachers:
            mails.append(teacher.auth_user.email)
        # retrieve student's email
        student_mail = me_the_user.email
        mails.append(student_mail)
        was_sent = mail.send(to=mails,
                  subject=T('[DTT]Automatic Notification - Report ready to be checked.'),
                  # If reply_to is omitted, then mail.settings.sender is used
                  reply_to = student_mail,
                  message = message)
        #MAILER LOG
        db.mailer_log.insert(sent_message = message,
                             destination = ','.join(mails),
                             result_log = str(mail.error or '') + ':' + str(mail.result),
                             success = was_sent)
    db.commit()
    auto_freeze()
    check_exception_semester_repeat()
    automation_activities_assigned()
    automation_evaluations()
    return T('Total Updated Reports: ') + str(total_recheckies + total_drafties + missed_reports) + ' ' + \
            T('Automatically Updated Draft Reports: ') + str(total_drafties) + ' ' + \
            T('Automatically Updated Recheck Reports: ') + str(total_recheckies) + ' ' + \
            T('Reports Never Delivered: ') + str(missed_reports + total_drafties_empty)

from gluon.scheduler import Scheduler
scheduler = Scheduler(db3, dict(auto_daily = auto_daily), heartbeat = 60)

import cpfecys
cpfecys.setup(db, auth, scheduler, auto_daily)
cpfecys.force_student_data_update(request.env.path_info,
                                  ['/student/update_data',
                                   '/default/user/logout'])

#resources menu
#import cpfecys
period = cpfecys.current_year_period()
data = db((db.item_restriction.is_public == True)&
          (db.item_restriction.period == period)).select()
mnu = []
for d in data:
    mnu.append((T(d.name), False, URL('default', 'resources', vars=dict(r=d.id))))
response.menu.extend([(T('Resources & Schedules'), False, URL(), mnu)])

#any user should be able to see this menu
#resources menu
response.menu.extend([
(T('Help'), False, URL(), [
   (T('Links'), False, URL('default', 'links'), []),
   (T('Files'), False, URL('default', 'files'), []),
])])
