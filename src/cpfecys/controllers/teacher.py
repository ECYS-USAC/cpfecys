# coding: utf8
# intente algo como
@auth.requires_login()
@auth.requires_membership('Teacher')
def index():
    return dict()

@auth.requires_login()
@auth.requires_membership('Teacher')
def final_practice():
    def get_items():
        restrictions = db((db.item_restriction.id== \
            db.item_restriction_exception.item_restriction)& \
            (db.item_restriction_exception.project==final_practice.project.id) \
            ).select(db.item_restriction.ALL)
    assignation = request.vars['assignation']
    if not assignation: redirect(URL('courses'))
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
    reports = db((db.report.assignation == final_practice.user_project.id)&
                        (db.report.status.name!='Grading'))
    avg = reports.select((db.report.score.sum()/db.report.score.count()).\
                        with_alias('avg')).first()['avg'] or 0
    reports = reports.select()
    return dict(final_practice=final_practice,
                available_periods=available_periods,
                reports=reports,
                reports_avg=avg,
                items=items,
                total_items=total_items,
                get_items=get_items)

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
    parameters = cpfecys.get_custom_parameters()
    valid = not(report is None)
    next_date = None

    if (request.args(0) == 'view'):
        report = request.vars['report']
        report = db.report(db.report.id == report)
        valid = not(report is None)
        if valid: valid = cpfecys.teacher_validation_report_access(report.id)
        if valid:
            if report.score_date:
                next_date = report.score_date + datetime.timedelta(
                    days=parameters.rescore_max_days)
            response.view = 'teacher/report_view.html'
            assignation_reports = db(db.report.assignation== \
                report.assignation).select()
            return dict(
                log_types=db(db.log_type.id > 0).select(),
                assignation_reports = assignation_reports,
                logs=db((db.log_entry.report == report.id)).select(),
                parameters=parameters,
                metrics=db((db.log_metrics.report == report.id)).select(),
                anomalies=db((db.log_type.name == 'Anomaly')&
                           (db.log_entry.log_type == db.log_type.id)&
                           (db.log_entry.report == report.id)).count(),
                markmin_settings=cpfecys.get_markmin,
                report=report,
                next_date=next_date)
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
                        + T('Fix the report on:') \
                        + ' http://omnomyumi.com/dtt/' + '</html>'
                        # send mail to teacher and student notifying change.
                        mails = []
                        # retrieve teacher's email
                        teacher = me_the_user.email
                        mails.append(teacher)
                        # retrieve student's email
                        student_mail = row.assigned_user['email']
                        mails.append(student_mail)
                        mail.send(to=mails,
                                  subject=T('[DTT]Automatic Notification - Report ready to be checked.'),
                                  # If reply_to is omitted, then mail.settings.sender is used
                                  reply_to = teacher,
                                  message=message)
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
                        redirect(URL('teacher', 'report/view', \
                            vars=dict(report=report.id)))

        session.flash = T('Selected report can\'t be viewed. \
                            Select a valid report.')
        redirect(URL('teacher', 'index'))

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
    if currentyear_period.period == cpfecys.first_period.id:
        current_period_name = T(cpfecys.first_period_name)
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
