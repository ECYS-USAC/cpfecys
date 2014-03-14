# coding: utf8
# intente algo como

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def assignation_freeze():
    grid = SQLFORM.grid(db.assignation_freeze)
    return dict(grid = grid)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def assignation_ignore_toggle():
    # get assignation id
    assignation = request.vars['id']
    # get the assignation
    assignation = db.user_project(id = assignation)
    # toggle assignation_ignored flag
    assignation.assignation_ignored = not assignation.assignation_ignored
    assignation.update_record()
    if request.env.http_referrer:
        redirect(request.env.http_referrer)
    else:
        redirect(URL('admin','assignations'))
    return

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def force_assignation_active():
    # get assignation id
    assignation = request.vars['id']
    # get the assignation
    assignation = db.user_project(id = assignation)
    # set the assignation as active
    assignation.assignation_status = None
    assignation.update_record()
    if request.env.http_referrer:
        redirect(request.env.http_referrer)
    else:
        redirect(URL('admin','assignations'))
    return

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def force_assignation_failed():
    # get assignation id
    assignation = request.vars['id']
    # get the assignation
    assignation = db.user_project(id = assignation)
    # set the assignation as failed
    assignation.assignation_status = db.assignation_status(name="Failed")
    assignation.update_record()
    if request.env.http_referrer:
        redirect(request.env.http_referrer)
    else:
        redirect(URL('admin','assignations'))
    return

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def force_assignation_successful():
    # get assignation id
    assignation = request.vars['id']
    # get the assignation
    assignation = db.user_project(id = assignation)
    # set the assignation as successful
    assignation.assignation_status = db.assignation_status(name="Successful")
    assignation.update_record()
    if request.env.http_referrer:
        redirect(request.env.http_referrer)
    else:
        redirect(URL('admin','assignations'))
    return

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def assignations():
    #requires parameter year_period if no one is provided then it is automatically detected
    #and shows the current period
    year_period = request.vars['year_period']
    max_display = 1
    import cpfecys
    currentyear_period = db.period_year(db.period_year.id == year_period)
    if not currentyear_period:
        currentyear_period = cpfecys.current_year_period()
        changid = currentyear_period.id
    q_selected_period_assignations = ((db.user_project.period <= \
        currentyear_period.id)&
              ((db.user_project.period + db.user_project.periods) > \
                currentyear_period.id))
    q2 = (db.user_project.assigned_user == db.auth_user.id)
    q3 = (db.user_project.project == db.project.id)
    q4 = (db.user_project.period == db.period_year.id)
    orderby = db.auth_user.last_name
    orderby2 = db.auth_user.first_name
    orderby3 = db.auth_user.username
    data = db(q_selected_period_assignations&q2&q3&q4\
        ).select(orderby=orderby|orderby2|orderby3)
    current_period_name = T(cpfecys.second_period.name)
    if currentyear_period.period == cpfecys.first_period.id:
        current_period_name = T(cpfecys.first_period.name)
    start_index = currentyear_period.id - max_display - 1
    if start_index < 1:
        start_index = 0
    end_index = currentyear_period.id + max_display
    periods_before = db(db.period_year \
        ).select(limitby=(start_index, currentyear_period.id - 1))
    periods_after = db(db.period_year \
        ).select(limitby=(currentyear_period.id, end_index))
    other_periods = db(db.period_year).select()
    return dict(data = data,
                currentyear_period = currentyear_period,
                current_period_name = current_period_name,
                periods_before = periods_before,
                periods_after = periods_after,
                other_periods = other_periods)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def periods():
    grid = SQLFORM.grid(db.period_year)
    return locals()

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def report_requirements():
    grid = SQLFORM.grid(db.area_report_requirement)
    return locals()

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def report_restrictions():
    grid = SQLFORM.grid(db.report_restriction)
    return locals()

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def projects():
    grid = SQLFORM.grid(db.project)
    return locals()

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def parameters():
    grid = SQLFORM.grid(db.custom_parameters)
    return dict(grid=grid)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
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
        if valid:
            def add_timing(status):
                if status == 'Acceptance':
                    return status
                elif status == 'Recheck':
                    return status + ' (' + str(parameters.rescore_max_days) + \
                        ' days)'
                else:
                    return status + ' (24 hours)'
            if report.score_date:
                next_date = report.score_date + datetime.timedelta(
                    days=parameters.rescore_max_days)
            response.view = 'admin/report_view.html'
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
                next_date=next_date,
                status_list=db(db.report_status).select(),
                add_timing=add_timing)
        else:
            session.flash = T('Selected report can\'t be viewed. \
                                Select a valid report.')
            redirect(URL('admin', 'index'))
    elif (request.args(0) == 'approve'):
        report.update_record(dtt_approval=True)
        session.flash = T('The report has been approved')
        redirect(URL('admin', 'report/view', \
            vars=dict(report=report.id)))
    elif (request.args(0) == 'fail'):
        report.update_record(dtt_approval=False)
        session.flash = T('The report has been failed')
        redirect(URL('admin', 'report/view', \
            vars=dict(report=report.id)))
    elif (request.args(0) == 'grade'):
        if valid:
            score = request.vars['score']
            comment = request.vars['comment']
            status = request.vars['status']
            sendmail = request.vars['send_mail']
            if sendmail != None: sendmail = True
            else: sendmail = False
            if score != '': score = int(score)
            else: score = report.score
            if comment == '': comment = report.teacher_comment
            status =db.report_status(id=status)
            if status.id != report.status:
                report.update_record(
                    admin_score=score,
                    min_score=cpfecys.get_custom_parameters().min_score,
                    admin_comment=comment,
                    score_date=cdate,
                    status=status.id,
                    dtt_approval=True)
            elif score >= 0  and score <= 100:
                report.update_record(
                    admin_score=score,
                    min_score=cpfecys.get_custom_parameters().min_score,
                    admin_comment=comment,
                    score_date=cdate,
                    status=db.report_status(name='Acceptance'),
                    dtt_approval=True)

            if sendmail:
                user = report.assignation.assigned_user
                subject = T('[DTT]Automatic Notification - Report graded ') \
                +T('BY ADMIN USER')
                message = '<html>' + T('The report') + ' ' \
                + '<b>' + XML(report.report_restriction.name) + '</b><br/>' \
                + T('sent by student: ') + XML(user.username) + ' ' \
                + XML(user.first_name) + ' ' \
                + XML(user.last_name) \
                + '<br/>' \
                + T('Score: ') + XML(report.admin_score) + ' ' \
                + '<br/>' \
                + T('Scored by: ') + XML('Admin User') + ' ' \
                + '<br/>' \
                + T('Comment: ') + XML(comment) + ' ' \
                + '<br/>' \
                + T('Current status is: ') \
                + XML(T(report.status.name)) +'<br/>' \
                + T('DTT-ECYS') \
                + ' http://omnomyumi.com/dtt/' + '</html>'
                mail.send(to=user.email,
                  subject=subject,
                  message=message)
                session.flash = T('The report has been scored \
                    successfully')
                redirect(URL('admin', 'report/view', \
                    vars=dict(report=report.id)))

        session.flash = T('Invalid Action.')
        redirect(URL('admin', 'report/view', \
                    vars=dict(report=report.id)))

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def mail_notifications():
    period = cpfecys.current_year_period()
    if (request.args(0) == 'send'):
        roles = request.vars['role']
        projects = request.vars['project']
        message = request.vars['message']
        subject = request.vars['subject']
        if projects  != None  and roles != None:
            assignations = None
            for role in request.vars['role']:
                role = db(db.auth_group.id==role).select().first()
                if role.role == 'DSI':
                    users = db(
                        (db.auth_user.id==db.auth_membership.user_id)&
                        (db.auth_membership.group_id==db.auth_group.id)&
                        (db.auth_group.role=='DSI'))
                    dsi_role = [users.select().first().auth_group.id]
                    send_mail_to_users(users.select(db.auth_user.ALL), 
                        message, dsi_role, projects,
                        subject)
            users = db(
                    (db.auth_user.id==db.user_project.assigned_user)&
                    (db.auth_user.id==db.auth_membership.user_id)&
                    (db.auth_membership.group_id==db.auth_group.id)&
                    (db.auth_group.id.belongs(roles))&
                    (db.user_project.project.belongs(projects))&
                    (db.user_project.period==db.period_year.id)&
                    ((db.user_project.period <= period.id)&
                    ((db.user_project.period + db.user_project.periods) > \
                     period.id))
                    ).select(db.auth_user.ALL, distinct=True)

            send_mail_to_users(users, message, roles, projects, subject, True)
            session.flash = T('Mail successfully sent')
            redirect(URL('admin', 'mail_notifications'))
        else:
            session.flash = T('At least a project and a role must be selected')
            redirect(URL('admin', 'mail_notifications'))

    groups = db(db.auth_group.role!='Super-Administrator').select()
    areas = db(db.area_level).select()
    def get_projects(area):
        courses = db(db.project.area_level==area.id)
        return courses
    def prepare_name(name):
        name = name.lower()
        name = name.replace(' ', '-')
        return name
    return dict(groups=groups,
        areas=areas,
        get_projects=get_projects,
        prepare_name=prepare_name)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def mail_log():
    logs = db(db.mail_log).select()
    return dict(logs=logs)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def send_mail_to_users(users, message, roles, projects, subject, log=False):
    if log:
        import datetime
        cdate = datetime.datetime.now()
        roles = db(db.auth_group.id.belongs(roles)).select()
        projects = db(db.project.id.belongs(projects)).select()
        roles_text = ''
        projects_text = ''
        for role in roles:
            roles_text = roles_text + ',' + role.role
            pass
        for project in projects:
            projects_text = projects_text + '|' + project.name + '|'
            pass
        db.mail_log.insert(sent_message=message,
            roles=roles_text[1:],
            projects=projects_text[1:],
            sent=cdate)
    for user in users:
        print user.email
        if user.email != None and user.email != '':
            mail.send(to=user.email,
              subject=T(subject),
              message=message)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def anomalies_list():
    from datetime import datetime
    cperiod = cpfecys.current_year_period()
    year = str(cperiod.yearp)
    if cperiod.period == 1:
        start = datetime.strptime(year + '-01-01', "%Y-%m-%d")
        end = datetime.strptime(year + '-07-01', "%Y-%m-%d")
    else:
        start = datetime.strptime(year + '-07-01', "%Y-%m-%d")
        end = datetime.strptime(year + '-12-31', "%Y-%m-%d")
    def get_month_name(date):
        import datetime
        return date.strftime("%B")
    count = db.log_entry.id.count()
    if (request.args(0) == 'view'):
        period = request.vars['period']
        valid = period != None
        if not valid:
            session.flash = T('Incomplete Information')
            redirect(URL('default', 'index'))
        anomalies = db((db.log_entry.report==db.report.id)&
            (db.log_entry.log_type==db.log_type(name='Anomaly'))&
            (db.report.created>start)&
            (db.report.created<end)&
            (db.report.assignation==db.user_project.id)&
            (db.user_project.project==db.project.id) \
            ).select(db.log_entry.entry_date, \
            count, db.log_entry.log_type, \
            db.project.ALL, groupby=db.project.name)
        return dict(anomalies=anomalies,
            get_month_name=get_month_name,
            period=period)

    elif (request.args(0) == 'periods'):
        response.view = 'admin/anomaly_periods.html'
        periods = db(db.period_year).select()
        def count_by_period(period):
            anomalies_total = db((db.log_entry.report==db.report.id)&
            (db.log_entry.log_type==db.log_type(name='Anomaly'))&
            (db.report.created>start)&
            (db.report.created<end)&
            (db.report.assignation==db.user_project.id)&
            (db.user_project.project==db.project.id) \
            ).count()
            return anomalies_total
        return dict(periods=periods,
            count_by_period=count_by_period)

    elif (request.args(0) == 'show'):
        project = request.vars['project']
        period = request.vars['period']
        valid = project != None
        if not valid:
            session.flash = T('Incomplete Information')
            redirect(URL('default', 'index'))
        project = db(db.project.id==project).select().first()
        anomalies = db((db.log_entry.report==db.report.id)&
            (db.log_entry.log_type==db.log_type(name='Anomaly'))&
            (db.report.created>start)&
            (db.report.created<end)&
            (db.report.assignation==db.user_project.id)&
            (db.user_project.project==db.project.id)&
            (db.project.id==project) \
            ).select(db.log_entry.ALL, \
            db.user_project.ALL,
            db.project.ALL)
        response.view = 'admin/anomaly_show.html'
        return dict(anomalies=anomalies)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def report_list():
    response.view = 'admin/report_list.html'
    period_year = db(db.period_year).select(orderby=~db.period_year.id)
    def count_reproved(pyear):
        from datetime import datetime
        year = str(pyear.yearp)
        if pyear.period == 1:
            start = datetime.strptime(year + '-01-01', "%Y-%m-%d")
            end = datetime.strptime(year + '-07-01', "%Y-%m-%d")
        else:
            start = datetime.strptime(year + '-07-01', "%Y-%m-%d")
            end = datetime.strptime(year + '-12-31', "%Y-%m-%d")
        reports = db((db.report.created>start)&
            (db.report.created<end)&
            (db.report.score < db.report.min_score))
        return reports.count()
    def count_approved(pyear):
        from datetime import datetime
        year = str(pyear.yearp)
        if pyear.period == 1:
            start = datetime.strptime(year + '-01-01', "%Y-%m-%d")
            end = datetime.strptime(year + '-07-01', "%Y-%m-%d")
        else:
            start = datetime.strptime(year + '-07-01', "%Y-%m-%d")
            end = datetime.strptime(year + '-12-31', "%Y-%m-%d")
        reports = db((db.report.created<end)&
            (db.report.created>start)&
            (db.report.score>=db.report.min_score)&
            (db.report.min_score!=None)&
            (db.report.min_score!=0))
        return reports.count()
    def count_no_created(pyear):
        return -1
        from datetime import datetime
        year = str(pyear.yearp)
        if pyear.period == 1:
            start = datetime.strptime(year + '-01-01', "%Y-%m-%d")
            end = datetime.strptime(year + '-07-01', "%Y-%m-%d")
            restrictions = db((db.report_restriction.start_date>=start)&
                (db.report_restriction.end_date<=end))
            return restrictions
        else:
            start = datetime.strptime(year + '-07-01', "%Y-%m-%d")
            end = datetime.strptime(year + '-12-31', "%Y-%m-%d")
            restrictions = db((db.report_restriction.start_date>=start)&
                (db.report_restriction.end_date<=end))
            return restrictions

    def count_reports(pyear):
        from datetime import datetime
        year = str(pyear.yearp)
        if pyear.period == 1:
            start = datetime.strptime(year + '-01-01', "%Y-%m-%d")
            end = datetime.strptime(year + '-07-01', "%Y-%m-%d")
        else:
            start = datetime.strptime(year + '-07-01', "%Y-%m-%d")
            end = datetime.strptime(year + '-12-31', "%Y-%m-%d")
        count = db.report.id.count()
        report_total = db().select(
            db.report_status.ALL, count, 
            left=db.report.on((db.report.status==db.report_status.id)&
                (db.report.created < end)&
                (db.report.created > start)), 
            groupby=db.report_status.name)
        return report_total

    count = db.report.id.count()
    report_total = db().select(
        db.report_status.ALL, count, 
        left=db.report.on((db.report.status==db.report_status.id)), 
        groupby=db.report_status.name)
    return dict(period_year=period_year,
        report_total=report_total,
        count_reproved=count_reproved,
        count_approved=count_approved,
        count_no_created=count_no_created,
        count_reports=count_reports)
                

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def report_filter():
    from datetime import datetime
    cperiod = cpfecys.current_year_period()
    year = str(cperiod.yearp)
    if cperiod.period == 1:
        start = datetime.strptime(year + '-01-01', "%Y-%m-%d")
        end = datetime.strptime(year + '-07-01', "%Y-%m-%d")
    else:
        start = datetime.strptime(year + '-07-01', "%Y-%m-%d")
        end = datetime.strptime(year + '-12-31', "%Y-%m-%d")
    status = request.vars['status']
    period = request.vars['period']
    valid = period != None
    def count_log_entries(report):
        log_entries = db((db.log_entry.report== \
            report.id)).select(db.log_entry.id.count())
        return log_entries
    def count_metrics_report(report):
        log_metrics = db((db.log_metrics.report== \
            report.id)).select(db.log_metrics.id.count())
        return log_metrics
    def count_anomalies(report):
        log_entries = db((db.log_entry.report== \
            report.id)&
        (db.log_entry.log_type==db.log_type(name='Anomaly')) \
        ).select(db.log_entry.id.count())
        return log_entries
    def calculate_ending_date(report):
        from datetime import date, datetime, timedelta
        someday = date.today()
        otherday = someday + timedelta(days=8)
        date = datetime.strptime(str(report.assignation.period.yearp) + \
                '-01-01', "%Y-%m-%d")
        date += timedelta(days=(30*6)*report.assignation.periods)
        semester =''
        if report.assignation.period.period.id == 1:

            if report.assignation.periods % 2 == 0:
                semester = T('Second Semester')
            else:
                semester = T('First Semester')
        else:
            if report.assignation.periods % 2 == 0:
                semester = T('First Semester')
            else:
                semester = T('Second Semester')
        return str(date.year) + '-' + str(semester)
    if not valid:
        session.flash = T('Incomplete Information')
        redirect(URL('default', 'index'))
    if not status:
        reports = db((db.report.created>start)&
            (db.report.created<end)).select(db.report.ALL)
    elif int(status) == -1:
        reports = db((db.report.created>start)&
            (db.report.created<end)&
            (db.report.score>=db.report.min_score)&
            (db.report.min_score!=None)&
            (db.report.min_score!=0)).select()
    else:
        reports = db((db.report.created>start)&
            (db.report.created<end)&
            (db.report.status==status)).select(db.report.ALL)
    return dict(reports=reports,
        count_log_entries=count_log_entries,
        count_metrics_report=count_metrics_report,
        count_anomalies=count_anomalies,
        calculate_ending_date=calculate_ending_date)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def links():
    user = db(db.auth_membership.user_id== \
        auth.user.id).select(db.auth_group.ALL)
    grid = SQLFORM.smartgrid(db.link, linked_tables=['link_access'])
    return locals()

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def areas():
    grid = SQLFORM.grid(db.area_level)
    return locals()

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def files_manager():
    user = db(db.auth_membership.user_id==auth.user.id \
        ).select(db.auth_group.ALL)
    grid = SQLFORM.smartgrid(db.uploaded_file, linked_tables=['file_access'])
    return locals()

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def notifications_manager():
    user = db(db.auth_membership.user_id == auth.user.id \
        ).select(db.auth_group.ALL)
    grid = SQLFORM.smartgrid(db.front_notification,  \
        linked_tables=['notification_access'])
    return locals()

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def items_manager():
    if request.function == 'new':
        db.item.created.writable=db.item.created.readable=False
    grid = SQLFORM.smartgrid(db.item_restriction,  \
        linked_tables=['item_restriction_area', 'item_restriction_exception'])
    return dict(grid=grid)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def manage_items():
    if (request.args(0) == 'periods'):
        response.view = 'admin/manage_items_periods.html'
        periods = db(db.period_year).select()
        return dict(periods=periods)
    elif (request.args(0) == 'area'):
        def count_items(area, period, disabled=False, enabled=False):
            if not(area and period):
                assignations = db(
                    (db.auth_user.id==db.user_project.assigned_user)&
                    (db.auth_user.id==db.auth_membership.user_id)&
                    (db.auth_membership.group_id==db.auth_group.id)&
                    (db.auth_group.role!='Teacher')).select(db.user_project.ALL)
                items = db((db.item.assignation.belongs(assignations))&
                    ((disabled==False)or(db.item.is_active==False))&
                    ((enabled==False)or(db.item.is_active==True)))
                return items
            else:
                projects = db(db.project.area_level==area).select()
                assignations = db((db.user_project.project.belongs(projects))&
                    (db.auth_user.id==db.user_project.assigned_user)&
                    (db.auth_user.id==db.auth_membership.user_id)&
                    (db.auth_membership.group_id==db.auth_group.id)&
                    (db.auth_group.role!='Teacher')).select(db.user_project.ALL)
                items = db((db.item.assignation.belongs(assignations))&
                    (db.item.created==period)&
                    ((disabled==False)or(db.item.is_active==False))&
                    ((enabled==False)or(db.item.is_active==True)))
                return items
        period = request.vars['period']
        areas = db(db.area_level).select()
        response.view = 'admin/manage_items_areas.html'
        return dict(areas=areas,
            period=period,
            count_items=count_items)        

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def items_grid():
    period = request.vars['period']
    area = request.vars['area']
    context_string = T('All')
    period_entity = db(db.period_year.id==period).select().first()
    if period_entity:
        context_string = T(str(period_entity.period.name)) + \
        ' ' + str(period_entity.yearp)
    school_id = request.vars['school-id']
    if not(area=='' or area==None):
        projects = db(db.project.area_level==area).select()    
    else:
        projects = db(db.project).select()
    assignations = db((db.user_project.project.belongs(projects))&
            (db.auth_user.id==db.user_project.assigned_user)&
            (db.auth_user.id==db.auth_membership.user_id)&
            ((school_id=='' or school_id==None) or \
                (db.auth_user.username==school_id))&
            (db.auth_membership.group_id==db.auth_group.id)&
            (db.auth_group.role!='Teacher')).select(db.user_project.ALL)
    items = db((db.item.assignation.belongs(assignations))&
        ((period=='' or period==None) or (db.item.created==period))).select()
    response.view = 'admin/manage_items_detail.html'
    return dict(items=items,
        area=area,
        period=period,
        context_string=context_string)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def toggle_active_item():
    item = request.vars['item']    
    if item != None:
        item = db(db.item.id==item).select().first()
    if item != None:
        item.update_record(
            is_active = not item.is_active)
    return True

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def assign_items():
    filter = 1
    if request.vars['filter'] != None:
        filter = int(request.vars['filter'])
    if filter == 1:
        pass
    dct = {}
    items = db((db.item.is_active==True)).select()
    rows=db().select(db.item.ALL, db.item_project.ALL,
         left=db.item_project.on(db.item.id==db.item_project.item))
    for item in items:
        dct.update({item.name:[]})
    for row in rows:
        dct[row.item.name].append(row)
    return locals()

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def assignation_upload():
    import csv
    error_users = []
    warning_users = []
    success = False
    if request.vars.csvfile != None:
        try:
            file = request.vars.csvfile.file
        except AttributeError:
            response.flash = T('Please upload a file.')
            return dict(success = False,
                file = False,
                periods = periods)
        try:
            cr = csv.reader(file, delimiter=',', quotechar='"')
            success = True
            header = next(cr)
            for row in cr:
                ## parameters
                rusername = row[1]
                rproject = row[3]
                rassignation_length = row[4]
                rpro_bono = (row[5] == 'Si') or (row[5] == 'si')
                ## check if user exists
                usr = db.auth_user(db.auth_user.username == rusername)
                project = db.project(db.project.project_id == rproject)
                import cpfecys
                current_period = cpfecys.current_year_period()
                if usr is None:
                    ## find it on chamilo (db2)
                    usr = db2.user_user(db2.user_user.username == rusername)
                    if usr is None:
                        # report error and get on to next row
                        row.append(T('Error: ') + T('User is not valid. \
                            User doesn\'t exist in UV.'))
                        error_users.append(row)
                        continue
                    else:
                        # insert the new user
                        usr = db.auth_user.insert(username = usr.username,
                                            password = usr.password,
                                            phone = usr.phone,
                                            last_name = usr.lastname,
                                            first_name = usr.firstname)
                        #add user to role 'student'
                        auth.add_membership('Student', usr)
                else:
                    assignation = db.user_project(
                        (db.user_project.assigned_user == usr.id)&
                        (db.user_project.project == project)&
                        (db.user_project.period == current_period))
                    if assignation != None:
                        row.append(T('Warning: ') + T('User \
                         was already assigned, Updating Data.'))
                        warning_users.append(row)
                        assignation.update_record(periods = \
                            rassignation_length, pro_bono = \
                            rpro_bono)
                        continue
                if project != None:
                    db.user_project.insert(assigned_user = usr,
                                            project = project,
                                            period = current_period,
                                            periods = rassignation_length,
                                            pro_bono = rpro_bono)
                else:
                    # project_id is not valid
                    row.append('Error: ' + T('Project code is not valid. \
                     Check please.'))
                    error_users.append(row)
                    continue
        except csv.Error:
            response.flash = T('File doesn\'t seem properly encoded.')
            return dict(success = False,
                file = False,
                periods = periods)
        response.flash = T('Data uploaded')
        return dict(success = success,
                    errors = error_users,
                    warnings = warning_users,
                    periods = periods)
    return dict(success = False,
                file = False,
                periods = periods)

@cache.action()
@auth.requires_login()
@auth.requires_membership('Super-Administrator')
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
@auth.requires_membership('Super-Administrator')
def assignation():
    #requires parameter year_period if no one is provided then it is 
    #automatically detected
    #and shows the current period
    year_period = request.vars['year_period']
    max_display = 1
    import cpfecys
    currentyear_period = db.period_year(db.period_year.id == year_period)
    if not currentyear_period:
        currentyear_period = cpfecys.current_year_period()
        changid = currentyear_period.id
    grid = SQLFORM.grid((db.user_project.period <= currentyear_period.id)&
              ((db.user_project.period + db.user_project.periods) >  \
                currentyear_period.id))
    current_period_name = T(cpfecys.second_period.name)
    if currentyear_period.period == cpfecys.first_period.id:
        current_period_name = T(cpfecys.first_period.name)
    start_index = currentyear_period.id - max_display - 1
    if start_index < 1:
        start_index = 0
    end_index = currentyear_period.id + max_display
    periods_before = db(db.period_year).select(limitby=(start_index,  \
        currentyear_period.id - 1))
    periods_after = db(db.period_year).select(limitby=(currentyear_period.id, \
     end_index))
    other_periods = db(db.period_year).select()
    return dict(grid = grid,
                currentyear_period = currentyear_period,
                current_period_name = current_period_name,
                periods_before = periods_before,
                periods_after = periods_after,
                other_periods = other_periods)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def users():
    orderby = dict(auth_user=[db.auth_user.first_name, \
                db.auth_user.username])
    grid = SQLFORM.smartgrid(db.auth_user, orderby=orderby)
    return dict(grid = grid)
