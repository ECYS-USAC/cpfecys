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
                print db.report.insert(assignation = assignation.id,
                                 report_restriction = restriction.id,
                                 created = current_date,
                                 score = 0,
                                 status = status_acceptance,
                                 teacher_comment =  T('The period of time to create the report finished and it was never completed; so automatically it is considered as failed.'))
    ## This makes all 'Draft' reports that expired get to 'Grading'
    drafties = db((db.report.status == db.report_status(name = 'Draft'))&
               (db.report_restriction.end_date < current_date)&
               (db.report.report_restriction == db.report_restriction.id)).select()
    total_drafties = len(drafties)
    for d in drafties:
        d.report.status = db.report_status(name = 'Grading')
        d.update_record()
        ## TODO: Send Email according to assignation
        # Notification Message
        me_the_user = d.report.assignation.assigned_user
        message = '<html>' + T('The report') + ' ' \
        + '<b>' + XML(d.report_restriction['name']) + '</b><br/>' \
        + T('sent by student: ') + XML(me_the_user.username) + ' ' \
        + XML(me_the_user.first_name) + ' ' + XML(me_the_user.last_name) \
        + '<br/>' \
        + T('was sent to be checked.') + '<br/>' + T('Checking can be done in:') \
        + ' http://omnomyumi.com/dtt/' + '</html>'
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
        mail.send(to=mails,
                  subject=T('[DTT]Automatic Notification - Report ready to be checked.'),
                  # If reply_to is omitted, then mail.settings.sender is used
                  reply_to = student_mail,
                  message=message)
    ## This makes all 'Recheck' reports that expired to 'Grading'
    import datetime
    recheckies = db((db.report_restriction.id == db.report.report_restriction)&
                    (db.report.status == db.report_status(name='Recheck'))&
                    (db.report.score_date <= (current_date - datetime.timedelta(days = cpfecys.get_custom_parameters().rescore_max_days)))).select()
    total_recheckies = len(recheckies)
    for rech in recheckies:
        rech.report.status = db.report_status(name = 'Grading')
        rech.update_record()
        ## TODO: Send Email according to assignation
        me_the_user = rech.report.assignation.assigned_user
        message = '<html>' + T('The report') + ' ' \
        + '<b>' + XML(rech.report_restriction['name']) + '</b><br/>' \
        + T('sent by student: ') + XML(me_the_user.username) + ' ' \
        + XML(me_the_user.first_name) + ' ' + XML(me_the_user.last_name) \
        + '<br/>' \
        + T('was sent to be checked.') + '<br/>' + T('Checking can be done in:') \
        + ' http://omnomyumi.com/dtt/' + '</html>'
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
        mail.send(to=mails,
                  subject=T('[DTT]Automatic Notification - Report ready to be checked.'),
                  # If reply_to is omitted, then mail.settings.sender is used
                  reply_to = student_mail,
                  message = message)
    db.commit()
    return T('Total Updated Reports: ') + str(total_recheckies + total_drafties + missed_reports) + ' ' + \
            T('Automatically Updated Draft Reports: ') + str(total_drafties) + ' ' + \
            T('Automatically Updated Recheck Reports: ') + str(total_recheckies) + ' ' + \
            T('Reports Never Delivered: ') + str(missed_reports)

from gluon.scheduler import Scheduler
scheduler = Scheduler(db3, dict(auto_daily = auto_daily), heartbeat = 60)

import cpfecys
cpfecys.setup(db, auth, scheduler, auto_daily)
cpfecys.force_student_data_update(request.env.path_info,
                                  ['/student/update_data',
                                   '/default/user/logout'])