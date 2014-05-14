# coding: utf8
# intente algo como
@auth.requires_login()
@auth.requires_membership('Teacher')
def index():
    return dict()

@auth.requires_login()
@auth.requires_membership('Teacher')
def todo_reports():
    #show the reports that haven't already been checked based on current assignations of the teacher
    data = db((db.report.status == db.report_status.id)&
       ((db.report_status.name == 'Grading')|(db.report_status.name == 'EnabledForTeacher'))&
       (db.report.assignation == db.user_project.id)&
       (db.user_project.assigned_user == auth.user.id)).select()
    return dict(my_projects = db((db.user_project.assigned_user == auth.user.id)&
                                 (db.project.id == db.user_project.project)).select())

@auth.requires_login()
@auth.requires_membership('Teacher')
def final_practice():
    def assignation_range(assignation):
        cperiod = cpfecys.current_year_period()
        ends = assignation.period.id + assignation.periods
        period_range = db((db.period_year.id >= assignation.period.id)&
            (db.period_year.id < ends)&
            (db.period_year.id <= cperiod.id)).select()
        return period_range

    def available_item_restriction(period_year, user_project):
        return db(((db.item_restriction.period==period_year) |
                    (db.item_restriction.permanent==True))&
                (db.item_restriction.is_enabled==True)&
                (db.item_restriction.hidden_from_teacher!=True)&
                (db.item_restriction_area.item_restriction==\
                    db.item_restriction.id)&
                (db.item_restriction_area.area_level==\
                    user_project.project.area_level.id))

    def restriction_project_exception(item_restriction_id, project_id):
        return db((db.item_restriction_exception.project== \
                    project_id)&
                    (db.item_restriction_exception.item_restriction \
                        ==item_restriction_id))

    def items_instance(item_restriction, assignation):
        return db((db.item.item_restriction==item_restriction.id)&
                    (db.item.assignation==assignation.id)&
                    (db.item.is_active==True))

    def get_items(period, assignation):
        restrictions = db((db.item_restriction.id== \
            db.item_restriction_exception.item_restriction)& \
            (db.item_restriction_exception.project==final_practice.project.id) \
            ).select(db.item_restriction.ALL)
        items = db((db.item.created==period.id)&
            (db.item.assignation==assignation.id)&
            (~db.item.item_restriction.belongs(restrictions)))
        return items.select(db.item.ALL)

    assignation = request.vars['assignation']
    if not assignation: redirect(URL('courses'))
    assignation = db(db.user_project.id==assignation).select().first()
    final_practice = db((db.user_project.id == assignation)&
                        (db.user_project.assigned_user == db.auth_user.id)&
                        (db.user_project.project == db.project.id)&
                        (db.project.area_level == db.area_level.id)&
                        (db.user_project.period == db.period_year.id)).select()
    if not final_practice: redirect(URL('courses'))
    final_practice = final_practice.first()
    #TODO evaluate if available_periods is really necessary
    available_periods = db((db.period_year.id >= \
                            final_practice.user_project.period)&
                        (db.period_year.id < \
                            (final_practice.user_project.period + \
                            final_practice.user_project.periods))).select()

    items = db((db.item.created==cpfecys.current_year_period())& \
                        (db.item.assignation==final_practice.user_project.id) \
                        ).select()
    total_items = db((db.item.created==cpfecys.current_year_period())).select()
    def get_current_reports(period):
        from datetime import datetime
        import cpfecys
        cperiod = cpfecys.current_year_period()
        year = str(cperiod.yearp)
        if period.period == 1:
            start = datetime.strptime(year + '-01-01', "%Y-%m-%d")
            end = datetime.strptime(year + '-07-01', "%Y-%m-%d")
        else:
            start = datetime.strptime(year + '-07-01', "%Y-%m-%d")
            end = datetime.strptime(year + '-12-31', "%Y-%m-%d")

        reports = db((db.report.assignation == final_practice.user_project.id)&
                        (db.report.status.name!='Grading')&
                        (db.report.created >= start)&
                        (db.report.created <= end))
        avg = reports.select((db.report.score.sum()/db.report.score.count()).\
                        with_alias('avg')).first()['avg'] or 0
        reports = reports.select(), avg
        return reports
    return dict(final_practice=final_practice,
                available_periods=available_periods,
                items=items,
                total_items=total_items,
                get_items=get_items,
                assignation_range=assignation_range,
                available_item_restriction=available_item_restriction,
                assignation=assignation,
                restriction_project_exception=restriction_project_exception,
                items_instance=items_instance,
                get_current_reports=get_current_reports)

@cache.action()
@auth.requires_login()
@auth.requires_membership('Teacher')
def download():
    item = db(db.item.uploaded_file==request.args[0]).select().first()
    project =  item.assignation.project
    t_assignation = db((db.user_project.project==project.id)&
        (db.user_project.assigned_user==auth.user.id))
    if item != None and t_assignation != None:
        return response.download(request, db)
    else:
        session.flash = T('Access Forbidden')
        redirect(URL('default', 'index'))

@auth.requires_login()
@auth.requires_membership('Teacher')
def report():
    import datetime
    cdate = datetime.datetime.now()
    report = request.vars['report']
    report = db.report(db.report.id == report)
    import cpfecys
    parameters = cpfecys.get_custom_parameters()
    valid = not(report is None)
    next_date = None
    if valid:
        valid = cpfecys.teacher_validation_report_access(report.id)

    if (request.args(0) == 'view'):
        report = request.vars['report']
        report = db.report(db.report.id == report)
        valid = not(report is None)
        if valid:
            if report.score_date:
                next_date = report.score_date + datetime.timedelta(
                    days=parameters.rescore_max_days)
            response.view = 'teacher/report_view.html'
            assignation_reports = db(db.report.assignation== \
                report.assignation).select()
            teacher = db(db.auth_user.id==auth.user.id).select().first()
            return dict(
                log_types=db(db.log_type.id > 0).select(),
                assignation_reports = assignation_reports,
                logs=db((db.log_entry.report == report.id)).select(),
                parameters=parameters,
                metrics=db((db.log_metrics.report == report.id)).select(),
                final_r = db(db.log_final.report == report.id).select(),
                anomalies=db((db.log_type.name == 'Anomaly')&
                           (db.log_entry.log_type == db.log_type.id)&
                           (db.log_entry.report == report.id)).count(),
                markmin_settings=cpfecys.get_markmin,
                report=report,
                next_date=next_date,
                teacher=teacher)
        else:
            session.flash = T('Selected report can\'t be viewed. \
                                Select a valid report.')
            redirect(URL('teacher', 'index'))
    elif (request.args(0) == 'grade'):
        if valid:
            score = request.vars['score']
            comment = request.vars['comment']
            if score != None:
                score = int(score)
                if request.vars['improve'] != None:
                    if report.times_graded >= parameters.rescore_max_count and \
                            report.status.name!='EnabledForTeacher':
                        session.flash = T('This report can\'t be sent to \
                            rechecked anymore')
                        redirect(URL('teacher', 'report/view', \
                            vars=dict(report=report.id)))

                    if comment != None:
                        report.update_record(
                            score=score,
                            min_score=cpfecys.get_custom_parameters().min_score,
                            teacher_comment=comment,
                            status=db.report_status(name='Recheck'),
                            score_date=cdate,
                            times_graded=(report.times_graded or 0)+1)
                        session.flash = T('The report has been sent to recheck \
                            you will be notified via email when rechecked')
                        # Notification Message
                        import cpfecys
                        signature = (cpfecys.get_custom_parameters().email_signature or '')
                        me_the_user = db.auth_user(db.auth_user.id == auth.user.id)
                        row = db.user_project(db.user_project.id == report.assignation)
                        message = '<html>' + T('The report') + ' ' \
                        + '<b>' + XML(report.report_restriction['name']) + '</b><br/>' \
                        + T('sent by student: ') + XML(row.assigned_user['username']) + ' ' \
                        + XML(row.assigned_user['first_name']) + ' ' + XML(row.assigned_user['last_name']) \
                        + '<br/>' \
                        + T('Score: ') + XML(report.score) + ' ' \
                        + '<br/>' \
                        + T('Scored by: ') + XML(me_the_user.username) + ' ' \
                        + XML(me_the_user.first_name) + ' ' + XML(me_the_user.last_name) \
                        + '<br/>' \
                        + T('Comment: ') + XML(comment) + ' ' \
                        + '<br/>' \
                        + T('Was checked, but sent back to be fixed.') + '<br/>' \
                        + T('You have:') + ' ' + str(db(db.custom_parameters.id > 0).select().first().rescore_max_days) + ' '  + T('days to fix the report.') + '<br/>' \
                        + T('If report is not fixed within given time, then last valid score is taken.') + '<br/>' \
                        + T('Fix the report on:') \
                        + ' ' + cpfecys.get_domain() + '<br />' + signature + '</html>'
                        # send mail to teacher and student notifying change.
                        mails = []
                        # retrieve teacher's email
                        teacher = me_the_user.email
                        mails.append(teacher)
                        # retrieve student's email
                        student_mail = row.assigned_user['email']
                        mails.append(student_mail)
                        was_sent = mail.send(to=mails,
                                  subject=T('[DTT]Automatic Notification - Report needs improvement.'),
                                  # If reply_to is omitted, then mail.settings.sender is used
                                  reply_to = teacher,
                                  message=message)
                        #MAILER LOG
                        db.mailer_log.insert(sent_message = message,
                             destination = ','.join(mails),
                             result_log = str(mail.error or '') + ':' + str(mail.result),
                             success = was_sent)
                        redirect(URL('teacher', 'report/view', \
                            vars=dict(report=report.id)))
                else:
                    if score >= 0  and score <= 100:
                        report.update_record(
                            score=score,
                            min_score=cpfecys.get_custom_parameters().min_score,
                            teacher_comment=comment,
                            status=db.report_status(name='Acceptance'),
                            score_date=cdate,
                            times_graded=(report.times_graded or 0)+1)
                        session.flash = T('The report has been scored \
                            successfully')
                        # Notification Message
                        import cpfecys
                        signature = (cpfecys.get_custom_parameters().email_signature or '')
                        me_the_user = db.auth_user(db.auth_user.id == auth.user.id)
                        row = db.user_project(db.user_project.id == report.assignation)
                        message = '<html>' + T('The report') + ' ' \
                        + '<b>' + XML(report.report_restriction['name']) + '</b><br/>' \
                        + T('sent by student: ') + XML(row.assigned_user['username']) + ' ' \
                        + XML(row.assigned_user['first_name']) + ' ' + XML(row.assigned_user['last_name']) \
                        + '<br/>' \
                        + T('Score: ') + XML(report.score) + ' ' \
                        + '<br/>' \
                        + T('Scored by: ') + XML(me_the_user.username) + ' ' \
                        + XML(me_the_user.first_name) + ' ' + XML(me_the_user.last_name) \
                        + '<br/>' \
                        + T('Comment: ') + XML(comment) + ' ' \
                        + '<br/>' \
                        + T('Was checked. No further actions are needed.') + '<br/>' \
                        + T('DTT-ECYS') \
                        + ' ' + cpfecys.get_domain() + '<br />' + signature + '</html>'
                        # send mail to teacher and student notifying change.
                        mails = []
                        # retrieve teacher's email
                        teacher = me_the_user.email
                        mails.append(teacher)
                        # retrieve student's email
                        student_mail = row.assigned_user['email']
                        mails.append(student_mail)
                        was_sent = mail.send(to=mails,
                                  subject=T('[DTT]Automatic Notification - Report Done.'),
                                  # If reply_to is omitted, then mail.settings.sender is used
                                  reply_to = teacher,
                                  message=message)
                        #MAILER LOG
                        db.mailer_log.insert(sent_message = message,
                             destination = ','.join(mails),
                             result_log = str(mail.error or '') + ':' + str(mail.result),
                             success = was_sent)
                        redirect(URL('teacher', 'report/view', \
                            vars=dict(report=report.id)))

        session.flash = T('Selected report can\'t be viewed. \
                            Select a valid report.')
        redirect(URL('teacher', 'index'))

@auth.requires_login()
@auth.requires_membership('Teacher')
def graphs():
    #requires parameter of project if none is provided then redirected to courses
    project_id = request.vars['project']
    #This also validates the current user is assigned in the project
    if not project_id: redirect(URL('courses'))
    current_project = db((db.user_project.assigned_user == auth.user.id)&
                         (db.project.id == project_id)).select().first()
    if not current_project: redirect(URL('courses'))
    #requires parameter year_period if no one is provided then it is automatically detected
    #and shows the current period
    year_period = request.vars['year_period']
    max_display = 1
    currentyear_period = db.period_year(db.period_year.id == year_period)
    if not currentyear_period:
        currentyear_period = current_year_period()
    current_data = db((db.user_project.period <= currentyear_period.id)&
              ((db.user_project.period + db.user_project.periods) > currentyear_period.id)&
              (db.user_project.project == current_project.project.id)&
              (db.auth_group.role == 'Student')&
              (db.auth_membership.group_id == db.auth_group.id)&
              (db.user_project.assigned_user == db.auth_membership.user_id)).select()
    current_period_name = T(cpfecys.second_period_name)
    #if we are second semester then start is 1st july
    import datetime
    start_date = datetime.date(currentyear_period.yearp, 7, 7)
    end_date = datetime.date(currentyear_period.yearp, 12, 31)
    if currentyear_period.period == cpfecys.first_period.id:
        current_period_name = T(cpfecys.first_period_name)
        #else we are on first semester, start jan 1st
        start_date = datetime.date(currentyear_period.yearp, 1, 1)
        end_date = datetime.date(currentyear_period.yearp, 6, 30)
    # i need all reports delivered by students for this semester
    reports = db((db.user_project.period <= currentyear_period.id)&
              ((db.user_project.period + db.user_project.periods) > currentyear_period.id)&
              (db.user_project.project == current_project.project.id)&
              (db.auth_group.role == 'Student')&
              (db.auth_membership.group_id == db.auth_group.id)&
              (db.user_project.assigned_user == db.auth_membership.user_id)&
              (db.report_restriction.start_date >= start_date)&
              (db.report_restriction.start_date <= end_date)).select(db.report.ALL, db.report_restriction.ALL, db.user_project.ALL, db.auth_group.ALL, db.auth_membership.ALL, orderby=db.user_project.assigned_user|db.report_restriction.start_date|db.report_restriction.name, left=[db.report.on(db.user_project.id == db.report.assignation), db.report_restriction.on(db.report.report_restriction == db.report_restriction.id)])
    report_activities = db((db.user_project.period <= currentyear_period.id)&
              ((db.user_project.period + db.user_project.periods) > currentyear_period.id)&
              (db.user_project.project == current_project.project.id)&
              (db.auth_group.role == 'Student')&
              (db.auth_membership.group_id == db.auth_group.id)&
              (db.user_project.assigned_user == db.auth_membership.user_id)&
              (db.report_restriction.start_date >= start_date)&
              (db.report_restriction.start_date <= end_date)&
              (db.report.id == db.log_metrics.report)).select(db.log_metrics.ALL, db.report.ALL, db.report_restriction.ALL, db.user_project.ALL, db.auth_group.ALL, db.auth_membership.ALL, orderby=db.user_project.assigned_user|db.report_restriction.start_date|db.report_restriction.name|db.log_metrics.created, left=[db.report.on(db.user_project.id == db.report.assignation), db.report_restriction.on(db.report.report_restriction == db.report_restriction.id)])
    # A helper to display this code within js stuff
    def values_display(values):
        result = "["
        old_user = None
        for item in values:
            if old_user != item.user_project.assigned_user.username:
                if old_user is not None:
                    result += "]},"
                old_user = item.user_project.assigned_user.username
                result += "{ name: '" + item.user_project.assigned_user.username + " - " + item.user_project.assigned_user.first_name +"',"
                result += "data: ["
            #categories.add(item.report.report_restriction)
            result += str(item.report.desertion_continued or 0) + ','
        result += "]}]"
        return XML(result)
    # A helper to display this code within js stuff
    def values_display_activities(values):
        result = "["
        old_user = None
        for item in values:
            if old_user != item.user_project.assigned_user.username:
                if old_user is not None:
                    result += "]},"
                old_user = item.user_project.assigned_user.username
                result += "{ name: '" + item.user_project.assigned_user.username + " - " + item.user_project.assigned_user.first_name +"',"
                result += "data: ["
            #categories.add(item.report.report_restriction)
            result += str(item.log_metrics.mediana or 0) + ','
        result += "]}]"
        return XML(result)
    start_index = currentyear_period.id - max_display - 1
    if start_index < 1:
        start_index = 0
    end_index = currentyear_period.id + max_display
    periods_before = db(db.period_year).select(limitby=(start_index, currentyear_period.id - 1))
    periods_after = db(db.period_year).select(limitby=(currentyear_period.id, end_index))
    other_periods = db(db.period_year).select()
    return dict(current_project = current_project,
                current_data = current_data,
                currentyear_period = currentyear_period,
                current_period_name = current_period_name,
                current_reports = reports,
                values_display = values_display,
                values_display_activities = values_display_activities,
                report_activities = report_activities,
                periods_before = periods_before,
                periods_after = periods_after,
                other_periods = other_periods)

@auth.requires_login()
@auth.requires_membership('Teacher')
def students():
    #requires parameter of project if none is provided then redirected to courses
    project_id = request.vars['project']
    #This also validates the current user is assigned in the project
    if not project_id: redirect(URL('courses'))
    current_project = db((db.user_project.assigned_user == auth.user.id)&
                         (db.project.id == project_id)).select().first()
    if not current_project: redirect(URL('courses'))
    #requires parameter year_period if no one is provided then it is automatically detected
    #and shows the current period
    year_period = request.vars['year_period']
    max_display = 1
    currentyear_period = db.period_year(db.period_year.id == year_period)
    if not currentyear_period:
        currentyear_period = current_year_period()
    current_data = db((db.user_project.period <= currentyear_period.id)&
              ((db.user_project.period + db.user_project.periods) > currentyear_period.id)&
              (db.user_project.project == current_project.project.id)&
              (db.auth_group.role == 'Student')&
              (db.auth_membership.group_id == db.auth_group.id)&
              (db.user_project.assigned_user == db.auth_membership.user_id)).select()
    current_period_name = T(cpfecys.second_period_name)
    #if we are second semester then start is 1st july
    import datetime
    start_date = datetime.date(currentyear_period.yearp, 7, 7)
    end_date = datetime.date(currentyear_period.yearp, 12, 31)
    if currentyear_period.period == cpfecys.first_period.id:
        current_period_name = T(cpfecys.first_period_name)
        #else we are on first semester, start jan 1st
        start_date = datetime.date(currentyear_period.yearp, 1, 1)
        end_date = datetime.date(currentyear_period.yearp, 6, 30)
    # i need all reports delivered by students for this semester
    reports = db((db.user_project.period <= currentyear_period.id)&
              ((db.user_project.period + db.user_project.periods) > currentyear_period.id)&
              (db.user_project.project == current_project.project.id)&
              (db.auth_group.role == 'Student')&
              (db.auth_membership.group_id == db.auth_group.id)&
              (db.user_project.assigned_user == db.auth_membership.user_id)&
              (db.report_restriction.start_date >= start_date)&
              (db.report_restriction.start_date <= end_date)).select(db.report.ALL, db.report_restriction.ALL, db.user_project.ALL, db.auth_group.ALL, db.auth_membership.ALL, orderby=db.user_project.assigned_user|db.report_restriction.start_date|db.report_restriction.name, left=[db.report.on(db.user_project.id == db.report.assignation), db.report_restriction.on(db.report.report_restriction == db.report_restriction.id)])
    report_activities = db((db.user_project.period <= currentyear_period.id)&
              ((db.user_project.period + db.user_project.periods) > currentyear_period.id)&
              (db.user_project.project == current_project.project.id)&
              (db.auth_group.role == 'Student')&
              (db.auth_membership.group_id == db.auth_group.id)&
              (db.user_project.assigned_user == db.auth_membership.user_id)&
              (db.report_restriction.start_date >= start_date)&
              (db.report_restriction.start_date <= end_date)&
              (db.report.id == db.log_metrics.report)).select(db.log_metrics.ALL, db.report.ALL, db.report_restriction.ALL, db.user_project.ALL, db.auth_group.ALL, db.auth_membership.ALL, orderby=db.user_project.assigned_user|db.report_restriction.start_date|db.report_restriction.name, left=[db.report.on(db.user_project.id == db.report.assignation), db.report_restriction.on(db.report.report_restriction == db.report_restriction.id)])
    # A helper to display this code within js stuff
    start_index = currentyear_period.id - max_display - 1
    if start_index < 1:
        start_index = 0
    end_index = currentyear_period.id + max_display
    periods_before = db(db.period_year).select(limitby=(start_index, currentyear_period.id - 1))
    periods_after = db(db.period_year).select(limitby=(currentyear_period.id, end_index))
    other_periods = db(db.period_year).select()
    return dict(current_project = current_project,
                current_data = current_data,
                currentyear_period = currentyear_period,
                current_period_name = current_period_name,
                current_reports = reports,
                report_activities = report_activities,
                periods_before = periods_before,
                periods_after = periods_after,
                other_periods = other_periods)

@auth.requires_login()
@auth.requires_membership('Teacher')
def courses():
    #requires parameter year_period if no one is provided then it is automatically detected
    #and shows the current period
    year_period = request.vars['year_period']
    max_display = 1
    currentyear_period = db.period_year(db.period_year.id == year_period)
    if not currentyear_period:
        currentyear_period = current_year_period()
    current_data = db((db.user_project.period <= currentyear_period.id)&
              ((db.user_project.period + db.user_project.periods) > currentyear_period.id)&
              (db.user_project.assigned_user == auth.user.id)).select()
    current_period_name = T(cpfecys.second_period_name)
    if currentyear_period.period == cpfecys.first_period.id:
        current_period_name = T(cpfecys.first_period_name)
    start_index = currentyear_period.id - max_display - 1
    if start_index < 1:
        start_index = 0
    end_index = currentyear_period.id + max_display
    periods_before = db(db.period_year).select(limitby=(start_index, currentyear_period.id - 1))
    periods_after = db(db.period_year).select(limitby=(currentyear_period.id, end_index))
    other_periods = db(db.period_year).select()
    return dict(current_data = current_data,
                currentyear_period = currentyear_period,
                current_period_name = current_period_name,
                periods_before = periods_before,
                periods_after = periods_after,
                other_periods = other_periods)

def find_max_cycles(user_projects):
    cycles = [0]
    for item in user_projects:
        cycles.extend([item.periods])
    return max(cycles)

def get_current_year():
    from datetime import datetime
    return datetime.now().year

def current_year_period():
    #this should be a module's method
    import datetime
    cdate = datetime.datetime.now()
    cyear = cdate.year
    cmonth = cdate.month
    period = cpfecys.second_period
    #current period depends if we are in dates between jan-jun and jul-dec
    if cmonth < 7 :
        period = cpfecys.first_period
    return db.period_year((db.period_year.yearp == cyear)&
                          (db.period_year.period == period))

def grading():
    return locals()
