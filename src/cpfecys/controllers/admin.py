# coding: utf8
# intente algo como

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def scheduler_activity():
    auto_daily()
    return dict(data = db3(db3.scheduler_run.id>0).select())

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def dtt_general_approval():
    from datetime import datetime
    cperiod = cpfecys.current_year_period()
    year = str(cperiod.yearp)
    if cperiod.period == 1:
        start = datetime.strptime(year + '-01-01', "%Y-%m-%d")
        end = datetime.strptime(year + '-06-01', "%Y-%m-%d")
    else:
        start = datetime.strptime(year + '-06-01', "%Y-%m-%d")
        end = datetime.strptime(year + '-12-31', "%Y-%m-%d")
    status = request.vars['status']
    period = request.vars['period']
    approve = request.vars['approve']
    # Get the coincident reports
    if status == 'None':
        reports = db((db.report.created>start)&
                     (db.report.created<end)).select()
        for report in reports:
            entries = count_log_entries(report.id)[0]['COUNT(log_entry.id)']
            metrics = count_metrics_report(report.id)[0]['COUNT(log_metrics.id)']
            anomalies = count_anomalies(report)[0]['COUNT(log_entry.id)']
            if entries != 0 or metrics!= 0 or anomalies != 0:
                report.update_record(dtt_approval = approve)
    elif int(status) == -1:
        reports = db((db.report.created>start)&
            (db.report.created<end)&
            (db.report.score>=db.report.min_score)&
            (db.report.min_score!=None)&
            (db.report.min_score!=0)).select()
        for report in reports:
            entries = count_log_entries(report.id)[0]['COUNT(log_entry.id)']
            metrics = count_metrics_report(report.id)[0]['COUNT(log_metrics.id)']
            anomalies = count_anomalies(report)[0]['COUNT(log_entry.id)']
            if entries != 0 or metrics!= 0 or anomalies != 0:
                report.update_record(dtt_approval = approve)
    else:
        reports = db((db.report.created>start)&
            (db.report.created<end)&
            (db.report.status==status)).select()
        for report in reports:
            entries = count_log_entries(report.id)[0]['COUNT(log_entry.id)']
            metrics = count_metrics_report(report.id)[0]['COUNT(log_metrics.id)']
            anomalies = count_anomalies(report)[0]['COUNT(log_entry.id)']
            if entries != 0 or metrics!= 0 or anomalies != 0:
                report.update_record(dtt_approval = approve)
    if request.env.http_referer is None:
        redirect(URL('admin','report_filter'))
    else:
        redirect(request.env.http_referer)
    return

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def roles():
    grid = SQLFORM.smartgrid(
        db.auth_group, linked_tables=['auth_membership'])
    return dict(grid=grid)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def general_report():
    period = cpfecys.current_year_period()
    if request.vars['period'] != None:
        period = request.vars['period']
        period = db(db.period_year.id==period).select().first()
        if not period:
            session.flash = T('Not valid Action.')
            redirect(URL('default', 'index'))
    periods = db(db.period_year).select()
    areas = db(db.area_level).select()
    def get_projects(area):
        projects = db(db.project.area_level==area).select()
        return projects
    def get_teacher(project):
        assignations = get_assignations(project, period, 'Teacher' \
                ).select(db.user_project.ALL)
        return assignations
    def get_final_report(project_id):
        from datetime import datetime
        log_final = None
        parcial_1 = None
        parcial_2 = None
        parcial_3 = None
        cperiod = cpfecys.current_year_period()
        year = str(cperiod.yearp)
        start = datetime.strptime(year + '-06-01', "%Y-%m-%d")
        end = datetime.strptime(year + '-12-31', "%Y-%m-%d")
        if cperiod.period == 1:
            start = datetime.strptime(year + '-01-01', "%Y-%m-%d")
            end = datetime.strptime(year + '-06-01', "%Y-%m-%d")

        final_report = db((db.report.created>start)&
                     (db.report.created<end)&
                     ((db.report_restriction.is_enabled!=None) &
                        (db.report_restriction.is_enabled!=False))&
                     (db.report.assignation==db.user_project.id)&
                     (db.user_project.project==project_id)&
                     (db.report.report_restriction==db.report_restriction.id)&
                     ((db.report_restriction.is_final!=None)&
                        (db.report_restriction.is_final!=False))
                      ).select(db.report.ALL).first()

        project_reports = db((db.report.created>start)&
                     (db.report.created<end)&
                     ((db.report_restriction.is_enabled!=None) &
                        (db.report_restriction.is_enabled!=False))&
                     (db.report.assignation==db.user_project.id)&
                     (db.user_project.project==project_id)
                      )._select(db.report.id)
        parcial_1 = db((db.log_metrics.metrics_type== \
                        db.metrics_type(name='PRIMER PARCIAL'))&
                        (db.log_metrics.report.belongs(project_reports))
                        ).select(db.log_metrics.ALL).first()
        parcial_2 = db((db.log_metrics.metrics_type== \
                        db.metrics_type(name='SEGUNDO PARCIAL'))&
                        (db.log_metrics.report.belongs(project_reports))
                        ).select(db.log_metrics.ALL).first()
        parcial_3 = db((db.log_metrics.metrics_type== \
                        db.metrics_type(name='TERCER PARCIAL'))&
                        (db.log_metrics.report.belongs(project_reports))
                        ).select(db.log_metrics.ALL).first()
        final = db((db.log_metrics.metrics_type== \
                        db.metrics_type(name='EXAMEN FINAL'))&
                        (db.log_metrics.report.belongs(project_reports))
                        ).select(db.log_metrics.ALL).first()
        primera_r = db((db.log_metrics.metrics_type== \
                        db.metrics_type(name='PRIMERA RETRASADA'))&
                        (db.log_metrics.report.belongs(project_reports))
                        ).select(db.log_metrics.ALL).first()
        segunda_r = db((db.log_metrics.metrics_type== \
                        db.metrics_type(name='SEGUNDA RETRASADA'))&
                        (db.log_metrics.report.belongs(project_reports))
                        ).select(db.log_metrics.ALL).first()
        if final_report != None:
            log_final = db(db.log_final.report== \
                final_report.id).select().first()
        return final_report, log_final, parcial_1, parcial_2, parcial_3, \
                final, primera_r, segunda_r
    periods = db(db.period_year).select()
    return dict(areas=areas, get_projects=get_projects, 
        get_teacher=get_teacher,get_final_report=get_final_report,
        actual_period=period, periods=periods)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def count_log_entries(report):
    log_entries = db((db.log_entry.report== \
        report)).select(db.log_entry.id.count())
    return log_entries

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def count_metrics_report(report):
    log_metrics = db((db.log_metrics.report== \
        report)).select(db.log_metrics.id.count())
    return log_metrics

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def count_anomalies(report):
    log_entries = db((db.log_entry.report== \
        report)&
    (db.log_entry.log_type==db.log_type(name='Anomaly')) \
    ).select(db.log_entry.id.count())
    return log_entries

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def delivered():
    periods = db(db.period_year).select()
    period = cpfecys.current_year_period()
    area_list = []
    if request.vars['period'] != None:
        period = request.vars['period']
        period = db.period_year(db.period_year.id==period)
    admin = False
    restrictions = db(
       (db.item_restriction.item_type==db.item_type(name='Activity'))& \
       ((db.item_restriction.period==period.id) |
        ((db.item_restriction.permanent==True)&
            (db.item_restriction.period <= period.id)))&
        (db.item_restriction.is_enabled==True)).select()| \
    db((db.item_restriction.item_type==db.item_type(name='Grade Activity'))& \
       ((db.item_restriction.period==period.id) |
        ((db.item_restriction.permanent==True)&
            (db.item_restriction.period <= period.id)))&
        (db.item_restriction.is_enabled==True)).select()
    def calculate_by_restriction(restriction):
        pending = 0
        graded = 0
        total = 0
        approved = 0
        failed = 0
        restriction_instance = db(
           (db.item_restriction.item_type==db.item_type(name='Activity'))& \
           (db.item_restriction.id==restriction)&
           (db.item_restriction.is_enabled==True)).select() | \
            db((db.item_restriction.item_type==db.item_type( \
                name='Grade Activity'))& \
           (db.item_restriction.id==restriction)&
           (db.item_restriction.is_enabled==True)
                ).select(db.item_restriction.ALL)

        areas = db((db.item_restriction_area.item_restriction== \
            restriction_instance[0].id)&
            (db.area_level.id==db.item_restriction_area.area_level)
                ).select(db.area_level.ALL)
        for area in areas:
            area_list.append(area.id)
        projects = db((db.project.area_level==db.area_level.id)&
         (db.item_restriction.id==restriction)&
         (db.item_restriction_area.area_level.belongs(area_list))&
         (db.item_restriction_area.item_restriction==restriction)&
         (db.item_restriction_area.item_restriction==db.item_restriction.id)&
         (db.item_restriction_area.area_level==db.area_level.id)&
         (db.item_restriction_area.is_enabled==True)).select(db.project.ALL)

        for project in projects:
            exception = db((db.item_restriction_exception.project== \
                project.id)&
                (db.item_restriction_exception.item_restriction== \
                restriction))
            if exception.count() == 0:
                assignations = db(
                    (db.auth_user.id==db.user_project.assigned_user)&
                    (db.auth_user.id==db.auth_membership.user_id)&
                    (db.auth_membership.group_id==db.auth_group.id)&
                    (db.auth_group.role=='Student')&
                    (db.user_project.project==project.id)&
                    (db.user_project.period == db.period_year.id)&
                    ((db.user_project.period <= period.id)&
                 ((db.user_project.period + db.user_project.periods) > \
                  period.id))
                    ).select(db.user_project.ALL)
                for assignation in assignations:
                    item = db((db.item.assignation==assignation.id)&
                     (db.item.item_restriction==restriction)&
                     (db.item.item_restriction==db.item_restriction.id)&
                     (db.item_restriction.is_enabled==True)&
                     (db.item.is_active==True)&
                     (db.item.created==period.id)).select(db.item.ALL).first()
                    if item == None:
                        pending += 1
                        total += 1
                    elif item.item_restriction.item_type.name=='Grade Activity':
                        if item.min_score == None:
                            pending += 1
                            total += 1
                        elif item.score >= item.min_score:
                            graded += 1
                            approved += 1
                            total += 1
                    elif item.item_restriction.item_type.name=='Activity':
                        if item.done_activity == None:
                            pending += 1
                            total += 1
                        elif item.done_activity == True:
                            graded += 1
                            approved += 1
                            total += 1
                        elif item.done_activity == False:
                            graded += 1
                            failed += 1
                            total += 1
        return pending, graded, total, approved, failed
    return dict(restrictions=restrictions, periods=periods,
        calculate_by_restriction=calculate_by_restriction,
        period=period)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def dtt_approval():
    # get report id
    report = request.vars['report']
    # get the approval value
    approve = request.vars['approve']
    # get the report
    report = db.report(id = report)
    # toggle report dtt_approval flag
    report.dtt_approval = approve
    report.update_record()
    if request.env.http_referer is None:
        redirect(URL('admin','report_filter'))
    else:
        redirect(request.env.http_referer)
    return

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
    if request.env.http_referer:
        redirect(request.env.http_referer)
    else:
        redirect(URL('admin','assignations'))
    return

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def force_assignation_active():
    # get assignation id
    assignation = request.vars['id']
    # get assignation comment
    comment = request.vars['comment']
    # get the assignation
    assignation = db.user_project(id = assignation)
    # set the assignation as active
    assignation.assignation_status = None
    assignation.assignation_status_comment = comment
    assignation.update_record()
    if request.env.http_referer:
        redirect(request.env.http_referer)
    else:
        redirect(URL('admin','assignations'))
    return

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def force_assignation_failed():
    # get assignation id
    assignation = request.vars['id']
    # get assignation comment
    comment = request.vars['comment']
    # get the assignation
    assignation = db.user_project(id = assignation)
    # set the assignation as failed
    assignation.assignation_status = db.assignation_status(name="Failed")
    assignation.assignation_status_comment = comment
    assignation.update_record()
    if request.env.http_referer:
        redirect(request.env.http_referer)
    else:
        redirect(URL('admin','assignations'))
    return

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def force_assignation_successful():
    # get assignation id
    assignation = request.vars['id']
    # get assignation comment
    comment = request.vars['comment']
    # get the assignation
    assignation = db.user_project(id = assignation)
    # set the assignation as successful
    assignation.assignation_status = db.assignation_status(name="Successful")
    assignation.assignation_status_comment = comment
    assignation.update_record()
    if request.env.http_referer:
        redirect(request.env.http_referer)
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
    q5 = (db.project.area_level == db.area_level.id)
    q6 = (db.auth_user.id==db.user_project.assigned_user)
    q7 = (db.auth_user.id==db.auth_membership.user_id)
    q8 = (db.auth_membership.group_id==db.auth_group.id)
    q9 = (db.auth_group.role!='Teacher')
    orderby =  db.area_level.name
    orderby2 = db.project.name
    orderby3 = db.auth_user.username
    orderby4 = db.auth_user.first_name
    data = db(q_selected_period_assignations&q2&q3&q4&q5&q6&q7&q8&q9\
        ).select(orderby=orderby|orderby2|orderby3|orderby4)
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

    if request.args(0) == 'toggle':
        enabled = ''
        user = request.vars['user']
        user = db(db.auth_user.id==user).select().first()
        if user == None:
            session.flash = T("No existing user")
            redirect(URL('admin', 'assignations', \
            vars=dict(year_period = currentyear_period)))
        if user.registration_key != 'blocked':
            enabled = 'blocked'
        user.update_record(
                registration_key=enabled)
        redirect(URL('admin', 'assignations', \
            vars=dict(year_period = currentyear_period)))

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
    import cpfecys
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
            semester = cpfecys.first_period.id
            if report.created.month > 7:
                semester = cpfecys.second_period.id

            period = db((db.period_year.yearp==int(report.created.year))&
                (db.period_year.period==semester)).select().first()
            teacher = db(
                        (db.auth_user.id==db.user_project.assigned_user)&
                        (db.auth_user.id==db.auth_membership.user_id)&
                        (db.auth_membership.group_id==db.auth_group.id)&
                        (db.auth_group.role=='Teacher')&
                        (db.user_project.project==report.assignation.project)&
                        (db.user_project.period==db.period_year.id)&
                        ((db.user_project.period <= period.id)&
                       ((db.user_project.period + db.user_project.periods) > \
                        period.id))
                        ).select(db.auth_user.ALL).first()
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
                final_r = db(db.log_final.report == report.id).select(),
                anomalies=db((db.log_type.name == 'Anomaly')&
                           (db.log_entry.log_type == db.log_type.id)&
                           (db.log_entry.report == report.id)).count(),
                markmin_settings=cpfecys.get_markmin,
                report=report,
                next_date=next_date,
                status_list=db(db.report_status).select(),
                add_timing=add_timing,
                teacher=teacher)
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
    elif (request.args(0) == 'pending'):
        report.update_record(dtt_approval=None)
        session.flash = T('The report has been set to pending')
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
                    dtt_approval=True,
                    never_delivered=False)
            elif score >= 0  and score <= 100:
                report.update_record(
                    admin_score=score,
                    min_score=cpfecys.get_custom_parameters().min_score,
                    admin_comment=comment,
                    score_date=cdate,
                    status=db.report_status(name='Acceptance'),
                    dtt_approval=True,
                    never_delivered=False)

            if sendmail:
                user = report.assignation.assigned_user
                subject = T('[DTT]Automatic Notification - Report graded ') \
                +T('BY ADMIN USER')
                signat = cpfecys.get_custom_parameters().email_signature or ''
                cstatus = db(db.report_status.id==report.status).select().first()
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
                + XML(T(cstatus.name)) +'<br/>' \
                + T('DTT-ECYS') \
                + ' ' + cpfecys.get_domain() + '<br />' + signat + '</html>'
                was_sent = mail.send(to=user.email,
                  subject=subject,
                  message=message)
                #MAILER LOG
                db.mailer_log.insert(sent_message = message,
                             destination = str(user.email),
                             result_log = str(mail.error or '') + ':' + str(mail.result),
                             success = was_sent)
            session.flash = T('The report has been scored \
                successfully')
            redirect(URL('admin', 'report/view', \
                vars=dict(report=report.id)))

        session.flash = T('Not valid Action.')
        redirect(URL('admin', 'report/view', \
                    vars=dict(report=report.id)))

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def courses_report():
    period = cpfecys.current_year_period()
    periods = db(db.period_year).select()
    area = None
    if request.vars['period'] != None:
        period = request.vars['period']
        period = db(db.period_year.id==period).select().first()
        if not period:
            session.flash = T('Not valid Action.')
            redirect(URL('default', 'index'))
    if request.args(0) == 'areas':
        areas = db(db.area_level).select()
        return dict(areas=areas)
    elif request.args(0) == 'list':
        area = request.vars['area']
        response.view = 'admin/courses_list.html'
        projects = db(db.project.area_level==area).select()
        def count_assigned(project):
            assignations = get_assignations(project, period, 'Student' \
                ).count()
            return assignations

        def count_assigned_students(project):
            assigned = []
            desertion = []
            assignations = get_assignations(project, period, 'Student' \
                ).select(db.user_project.ALL)
            for assignation in assignations:
                reports = db(db.report.assignation==assignation.id
                    ).select()
                for report in reports:
                    assigned.append(report.desertion_started)
            if assignations.first() != None:
                desertion_assignation = assignations.first()
                desertion_reports = db(
                    db.report.assignation==desertion_assignation.id).select()
                for report in desertion_reports:
                    if report.desertion_gone != None:
                        if report.desertion_gone:
                            desertion.append(report.desertion_gone)
            if len(assigned) > 0:
                assigned = max(assigned)
            else:
                assigned = T('Pending')
            if len(desertion) > 0:
                desertion = sum(desertion)
            else:
                desertion = T('Pending')
            return desertion, assigned
        def count_student_hours(project):
            resp = []
            assignations = get_assignations(project, period, 'Student' \
                ).select(db.user_project.ALL)
            for assignation in assignations:
                hours = 0
                reports = db(db.report.assignation==assignation.id
                    ).select()
                for report in reports:
                    hours += report.hours
                sub_response = [assignation.assigned_user.first_name +\
                    ' ' + assignation.assigned_user.last_name + \
                    ', ' + assignation.assigned_user.username, hours]
                resp.append(sub_response)
            return resp

        def current_teacher(project):
            teacher = get_assignations(project, period, 'Teacher'
                ).select(db.auth_user.ALL).first()
            name = T('Pending')
            if teacher != None:
                name = teacher.first_name + ' ' + teacher.last_name
            return name

        return dict(projects=projects, count_assigned=count_assigned,
            current_teacher=current_teacher, 
            count_assigned_students=count_assigned_students,
            count_student_hours=count_student_hours,
            periods=periods,
            area=area, period=period)
    else:
        session.flash = "Action not allowed"
        redirect(URL('default','index'))

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def active_teachers():
    period = cpfecys.current_year_period()
    if request.vars['period'] != None:
            period = request.vars['period']
            period = db(db.period_year.id==period).select().first()
            if not period:
                session.flash = T('Not valid Action.')
                redirect(URL('default', 'index'))
    if (request.args(0) == 'toggle'):
        enabled = ''
        user = request.vars['user']
        user = db(db.auth_user.id==user).select().first()
        if user == None:
            session.flash = T("No existing user")
            redirect(URL('admin','active_teachers'))
        if user.registration_key != 'blocked':
            enabled = 'blocked'
        user.update_record(
                registration_key=enabled)
        redirect(URL('admin','active_teachers'))
    elif request.args(0) == 'mail':
        user = request.vars['user']
        if user == None:
            session.flash = T("No existing user")
            redirect(URL('admin','active_teachers'))
        user = db(db.auth_user.id==user).select().first()
        if user == None:
            session.flash = T("No existing user")
            redirect(URL('admin','active_teachers'))
        recovery = cpfecys.get_domain() + \
            'default/user/retrieve_username?_next=/cpfecys/default/index'
        message = "Bienvenido a CPFECYS, su usuario es " + user.username + \
        ' para generar su contraseña puede visitar el siguiente enlace e ' +\
        'ingresar su usuario ' + recovery
        subject = 'DTT-ECYS Bienvenido'
        send_mail_to_users([user], message, None, None, subject)
        user.update_record(load_alerted=True)
    elif request.args(0) == 'notifyall':
        users = get_assignations(False, period, 'Teacher'
                ).select(db.auth_user.ALL, distinct=True)
        recovery = cpfecys.get_domain() + \
            'default/user/retrieve_username?_next=/cpfecys/default/index'
        for user in users:
            message = "Bienvenido a CPFECYS, su usuario es " + user.username + \
            ' para generar su contraseña puede visitar el siguiente enlace e ' +\
            'ingresar su usuario ' + recovery
            subject = 'DTT-ECYS Bienvenido'
            send_mail_to_users([user], message, None, None, subject)
            user.update_record(load_alerted=True)
    elif request.args(0) == 'notifypending':
        project = False
        users = db(
            (db.auth_user.id==db.user_project.assigned_user)&
            (db.auth_user.id==db.auth_membership.user_id)&
            (db.auth_user.load_alerted==None)&
            (db.auth_membership.group_id==db.auth_group.id)&
            (db.auth_group.role=='Teacher')&
            (project==False or (db.user_project.project==project))&
            (db.project.area_level==db.area_level.id)&
            (db.user_project.project==db.project.id)&
            (db.user_project.period == db.period_year.id)&
            ((db.user_project.period <= period.id)&
         ((db.user_project.period + db.user_project.periods) > \
          period.id))
            ).select(db.auth_user.ALL, distinct=True)
        recovery = cpfecys.get_domain() + \
            'default/user/retrieve_username?_next=/cpfecys/default/index'
        for user in users:
            message = "Bienvenido a CPFECYS, su usuario es " + user.username + \
            ' para generar su contraseña puede visitar el siguiente enlace e ' +\
            'ingresar su usuario ' + recovery
            subject = 'DTT-ECYS Bienvenido'
            send_mail_to_users([user], message, None, None, subject)
            user.update_record(load_alerted=True)

    assignations = get_assignations(False, period, 'Teacher' \
                ).select(db.user_project.ALL,
                orderby=db.area_level.name|\
                db.project.name|\
                db.auth_user.last_name|\
                db.auth_user.first_name)
    periods = db(db.period_year).select()
    return dict(periods=periods, assignations=assignations,
        actual_period=period)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def get_assignations(project, period, role):
    assignations = db(
                    (db.auth_user.id==db.user_project.assigned_user)&
                    (db.auth_user.id==db.auth_membership.user_id)&
                    (db.auth_membership.group_id==db.auth_group.id)&
                    (db.auth_group.role==role)&
                    (project==False or (db.user_project.project==project))&
                    (db.project.area_level==db.area_level.id)&
                    (db.user_project.project==db.project.id)&
                    (db.user_project.period == db.period_year.id)&
                    ((db.user_project.period <= period.id)&
                 ((db.user_project.period + db.user_project.periods) > \
                  period.id))
                    )
    return assignations

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def courses_report_detail():
    period = cpfecys.current_year_period()
    periods = db(db.period_year).select()
    if request.vars['period'] != None:
        period = request.vars['period']
        period = db(db.year_period.id==period).select().first()
    if request.vars['project'] == None:
        session.flash = "Action not allowed"
        redirect(URL('admin','courses_report/areas'))
    project = request.vars['project']
    assignations = db(
                    (db.auth_user.id==db.user_project.assigned_user)&
                    (db.auth_user.id==db.auth_membership.user_id)&
                    (db.auth_membership.group_id==db.auth_group.id)&
                    (db.auth_group.role=='Student')&
                    (db.user_project.project==project)&
                    (db.user_project.period == db.period_year.id)&
                    ((db.user_project.period <= period)&
                 ((db.user_project.period + db.user_project.periods) > \
                  period))
                    )._select()
    return assignations
    return dict(periods=periods, project=project,
        period=period)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def mail_notifications():
    period = cpfecys.current_year_period()
    if (request.args(0) == 'send'):
        roles = request.vars['role']
        projects = request.vars['project']
        message = request.vars['message']
        subject = request.vars['subject']

        if isinstance(roles, str):
            roles = [roles]

        if projects != None and isinstance(projects, str):
            projects = [projects]

        if projects  != None  and roles != None:
            for role in request.vars['role']:
                role = db(db.auth_group.id==role).select().first()

                if role.role == 'DSI':
                    users = db(
                        (db.auth_user.id==db.auth_membership.user_id)&
                        (db.auth_membership.group_id==db.auth_group.id)&
                        (db.auth_group.role=='DSI'))
                    group_id = users.select().first().auth_group.id
                    dsi_role = [group_id]
                    send_mail_to_users(users.select(db.auth_user.ALL), 
                        message, dsi_role, projects,
                        subject)

                users = db(
                    (db.auth_user.id==db.auth_membership.user_id)&
                    (db.auth_membership.group_id==db.auth_group.id)&
                    (db.auth_group.id.belongs(roles))&
                    #Until here we get users from role
                    (db.user_project.project.belongs(projects))&
                    (db.auth_user.id==db.user_project.assigned_user)&
                    #Until here we get users from role assigned to projects
                    (db.user_project.period==db.period_year.id)&
                    ((db.user_project.period <= period.id)&
                    ((db.user_project.period + db.user_project.periods) > \
                     period.id))
                    )
                #return users._select(db.auth_user.ALL, distinct=True)
                users = users.select(db.auth_user.ALL, distinct=True)
                #return users
                send_mail_to_users(users, message, \
                    roles, projects, subject, True)

            session.flash = T('Mail successfully sent')
            redirect(URL('admin', 'mail_notifications'))
        elif (roles != None) and (len(roles) == 1):
            for role in roles:
                role = db(db.auth_group.id==role).select().first()
                if role.role == 'DSI':
                    users = db(
                        (db.auth_user.id==db.auth_membership.user_id)&
                        (db.auth_membership.group_id==db.auth_group.id)&
                        (db.auth_group.role=='DSI'))
                    group_id = users.select().first().auth_group.id
                    dsi_role = [group_id]
                    send_mail_to_users(users.select(db.auth_user.ALL), 
                        message, dsi_role, projects,
                        subject)
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
        prepare_name=prepare_name,
        markmin_settings = cpfecys.get_markmin)

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
            projects_text = projects_text + ', ' + project.name
            pass
        db.mail_log.insert(sent_message=message,
            roles=roles_text[1:],
            projects=projects_text[1:],
            sent=cdate)
        import cpfecys
        message = '<html>' + message + \
            (cpfecys.get_custom_parameters().email_signature or '') + '</html>'
    emails = []
    for user in users:
        #print user.email
        if user.email != None and user.email != '':
            emails.append(user.email)
    was_sent = mail.send(to='dtt.ecys@gmail.com',
                         bcc=emails,
                         subject=T(subject),
                         message=message)
    #MAILER LOG
    db.mailer_log.insert(sent_message = message,
                         destination = str(user.email),
                         result_log = str(mail.error or '') + ':' + \
                         str(mail.result),
                         success = was_sent)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def anomalies_list():
    from datetime import datetime
    cperiod = cpfecys.current_year_period()
    year = str(cperiod.yearp)
    if cperiod.period == 1:
        start = datetime.strptime(year + '-01-01', "%Y-%m-%d")
        end = datetime.strptime(year + '-06-01', "%Y-%m-%d")
    else:
        start = datetime.strptime(year + '-06-01', "%Y-%m-%d")
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
        cperiod = db(db.period_year.id==period).select().first()
        if cperiod.period == 1:
            start = datetime.strptime(year + '-01-01', "%Y-%m-%d")
            end = datetime.strptime(year + '-06-01', "%Y-%m-%d")
        else:
            start = datetime.strptime(year + '-06-01', "%Y-%m-%d")
            end = datetime.strptime(year + '-12-31', "%Y-%m-%d")
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
            cperiod = db(db.period_year.id==period).select().first()
            if cperiod.period == 1:
                start = datetime.strptime(year + '-01-01', "%Y-%m-%d")
                end = datetime.strptime(year + '-06-01', "%Y-%m-%d")
            else:
                start = datetime.strptime(year + '-06-01', "%Y-%m-%d")
                end = datetime.strptime(year + '-12-31', "%Y-%m-%d")
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
            end = datetime.strptime(year + '-06-01', "%Y-%m-%d")
        else:
            start = datetime.strptime(year + '-06-01', "%Y-%m-%d")
            end = datetime.strptime(year + '-12-31', "%Y-%m-%d")
        reports = db((db.report.created>start)&
            (db.report.created<end)&
            (db.report.score < db.report.min_score)&
            (db.report.never_delivered==None 
                or db.report.never_delivered==False))
        return reports.count()

    def count_approved(pyear):
        from datetime import datetime
        year = str(pyear.yearp)
        if pyear.period == 1:
            start = datetime.strptime(year + '-01-01', "%Y-%m-%d")
            end = datetime.strptime(year + '-06-01', "%Y-%m-%d")
        else:
            start = datetime.strptime(year + '-06-01', "%Y-%m-%d")
            end = datetime.strptime(year + '-12-31', "%Y-%m-%d")
        reports = db((db.report.created<end)&
            (db.report.created>start)&
            ((db.report.score>=db.report.min_score) |
                (db.report.admin_score>=db.report.min_score))&
            (db.report.min_score!=None)&
            (db.report.min_score!=0))
        return reports.count()

    def count_no_created(pyear):
        from datetime import datetime
        year = str(pyear.yearp)
        if pyear.period == 1:
            start = datetime.strptime(year + '-01-01', "%Y-%m-%d")
            end = datetime.strptime(year + '-06-01', "%Y-%m-%d")
        else:
            start = datetime.strptime(year + '-06-01', "%Y-%m-%d")
            end = datetime.strptime(year + '-12-31', "%Y-%m-%d")
        cperiod = cpfecys.current_year_period()
        restrictions = db((db.report_restriction.start_date>=start)&
            (db.report_restriction.end_date<=end)&
            (db.report_restriction.is_enabled==True)).select()
        pending = 0
        assignations = get_assignations(False, cperiod, 'Student').select()
        for assignation in assignations:
            for restriction in restrictions:
                report = db(
                    (db.report.assignation==assignation.user_project.id)&
                    (db.report.report_restriction==restriction.id)&
                    (db.report.report_restriction==db.report_restriction.id)
                    ).select(db.report.ALL).first()
                if report == None:
                    pending += 1
                #esto es para no ver drafts en no_created del report_filter
                #else:
                #    hours = report.hours
                #    entries = count_log_entries(\
                #        report.id)[0]['COUNT(log_entry.id)']
                #    metrics = count_metrics_report(\
                #        report.id)[0]['COUNT(log_metrics.id)']
                #    anomalies = count_anomalies(\
                #        report)[0]['COUNT(log_entry.id)']
                #    if assignation.user_project.project.area_level.name == \
                #            'DTT Tutor Académico':
                #        if entries == 0 and metrics == 0 and anomalies == 0:
                #            pending += 1
                #    else:
                #        if hours == None and hours == 0:
                #            pending += 1

        return pending

    def count_acceptance(pyear):
        from datetime import datetime
        year = str(pyear.yearp)
        total = 0
        string = ''
        if pyear.period == 1:
            start = datetime.strptime(year + '-01-01', "%Y-%m-%d")
            end = datetime.strptime(year + '-06-01', "%Y-%m-%d")
        else:
            start = datetime.strptime(year + '-06-01', "%Y-%m-%d")
            end = datetime.strptime(year + '-12-31', "%Y-%m-%d")
        reports = db((db.report.created>= start)&
            (db.report.created<=end)&
            (db.report.status==db.report_status(name='Acceptance'))).select()
        array = []
        for report in reports:
            hours = report.hours
            entries = count_log_entries(\
                report)[0]['COUNT(log_entry.id)']
            metrics = count_metrics_report(\
                report)[0]['COUNT(log_metrics.id)']
            anomalies = count_anomalies(\
                report)[0]['COUNT(log_entry.id)']
            string = string + str(entries) + ' ' + str(metrics) + ' ' +str(anomalies) + '<br/>'
            if report.assignation.project.area_level.name == \
                    'DTT Tutor Académico':
                if entries != 0 or metrics != 0 or anomalies != 0:
                    total += 1
            else:
                if hours != None:
                    total += 1
        return total

    def count_draft(pyear):
        from datetime import datetime
        year = str(pyear.yearp)
        total = 0
        string = ''
        if pyear.period == 1:
            start = datetime.strptime(year + '-01-01', "%Y-%m-%d")
            end = datetime.strptime(year + '-06-01', "%Y-%m-%d")
        else:
            start = datetime.strptime(year + '-06-01', "%Y-%m-%d")
            end = datetime.strptime(year + '-12-31', "%Y-%m-%d")
        reports = db((db.report.created>= start)&
            (db.report.created<=end)&
            (db.report.status==db.report_status(name='Draft'))).select()
        for report in reports:
            hours = report.hours
            entries = count_log_entries(\
                report)[0]['COUNT(log_entry.id)']
            metrics = count_metrics_report(\
                report)[0]['COUNT(log_metrics.id)']
            anomalies = count_anomalies(\
                report)[0]['COUNT(log_entry.id)']
            string = string + str(entries) + ' ' + str(metrics) + ' ' +str(anomalies) + '<br/>'
            if report.assignation.project.area_level.name == \
                    'DTT Tutor Académico':
                if entries != 0 or metrics != 0 or anomalies != 0:
                            total += 1
            else:
                if hours != None and hours != 0:
                    total += 1
        return total

    def count_no_delivered(pyear):
        from datetime import datetime
        year = str(pyear.yearp)
        if pyear.period == 1:
            start = datetime.strptime(year + '-01-01', "%Y-%m-%d")
            end = datetime.strptime(year + '-06-01', "%Y-%m-%d")
        else:
            start = datetime.strptime(year + '-06-01', "%Y-%m-%d")
            end = datetime.strptime(year + '-12-31', "%Y-%m-%d")
        reports = db((db.report_restriction.start_date>=start)&
            (db.report_restriction.end_date<=end)&
            (db.report.report_restriction==db.report_restriction.id)&
            (db.report.never_delivered == True))
        return reports.count()
    def count_reports(pyear, status, exclude):
        from datetime import datetime
        year = str(pyear.yearp)
        if pyear.period == 1:
            start = datetime.strptime(year + '-01-01', "%Y-%m-%d")
            end = datetime.strptime(year + '-06-01', "%Y-%m-%d")
        else:
            start = datetime.strptime(year + '-06-01', "%Y-%m-%d")
            end = datetime.strptime(year + '-12-31', "%Y-%m-%d")
        count = db.report.id.count()
        report_total = db().select(
            db.report_status.ALL, count, 
            left=db.report.on((db.report.status==db.report_status.id)&
                (db.report.created < end)&
                (db.report.created > start)&
                ((status==False) or (db.report_status.name==status))), 
            groupby=db.report_status.name,
            orderby=db.report_status.order_number)
        return report_total

    count = db.report.id.count()
    report_total = db().select(
        db.report_status.ALL, count, 
        left=db.report.on((db.report.status==db.report_status.id)), 
        groupby=db.report_status.name,
        orderby=db.report_status.order_number)
    return dict(period_year=period_year,
        report_total=report_total,
        count_reproved=count_reproved,
        count_approved=count_approved,
        count_no_created=count_no_created,
        count_reports=count_reports,
        count_draft=count_draft,
        count_no_delivered=count_no_delivered,
        count_acceptance=count_acceptance)
                

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def report_filter():
    from datetime import datetime
    cperiod = cpfecys.current_year_period()
    if request.vars['period'] != None:
        cperiod = db(db.period_year.id==\
            request.vars['period']).select().first()
    year = str(cperiod.yearp)
    if cperiod.period == 1:
        start = datetime.strptime(year + '-01-01', "%Y-%m-%d")
        end = datetime.strptime(year + '-06-01', "%Y-%m-%d")
    else:
        start = datetime.strptime(year + '-06-01', "%Y-%m-%d")
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
        status_instance = False
    elif int(status) == -1:
        reports = db((db.report.created>start)&
            (db.report.created<end)&
            ((db.report.admin_score>=db.report.min_score) |\
             (db.report.score>=db.report.min_score))&
            (db.report.min_score!=None)&
            (db.report.min_score!=0)).select()
        status_instance = db(db.report_status.id==status).select().first()
    elif int(status) == -2:
        reports = db((db.report.created>start)&
            (db.report.created<end)&
            (db.report.score<=db.report.min_score)&
            (db.report.min_score!=None)&
            (db.report.min_score!=0)&
            (db.report.never_delivered==None or
                db.report.never_delivered==False)).select()
        status_instance = db(db.report_status.id==status).select().first()
    elif int(status) == -3:
        result = []
        existing = []
        restrictions = db((db.report_restriction.start_date>=start)&
            (db.report_restriction.end_date<=end)&
            (db.report_restriction.is_enabled==True)).select()
        pending = 0
        assignations = get_assignations(False, cperiod, 'Student').select()
        for assignation in assignations:
            for restriction in restrictions:
                report = db(
                    (db.report.assignation==assignation.user_project.id)&
                    (db.report.report_restriction==restriction.id)&
                    (db.report.report_restriction==db.report_restriction.id)
                    ).select(db.report.ALL).first()
                if report == None:
                    temp = dict(assignation=assignation, 
                        restriction=restriction)
                    result.append(temp)
                else:
                    hours = report.hours
                    entries = count_log_entries(\
                        report)[0]['COUNT(log_entry.id)']
                    metrics = count_metrics_report(\
                        report)[0]['COUNT(log_metrics.id)']
                    anomalies = count_anomalies(\
                        report)[0]['COUNT(log_entry.id)']
                    temp = dict(assignation=assignation, 
                            restriction=restriction,
                            report=report)
                    if assignation.user_project.project.area_level.name == \
                            'DTT Tutor Académico':
                        if entries == 0 and metrics == 0 and anomalies == 0:
                            existing.append(temp)
                    else:
                        if hours == None:
                            existing.append(temp)
              
        response.view = 'admin/report_filter_pending.html'      
        return dict(result=result, existing=existing,
            count_log_entries=count_log_entries,
            count_metrics_report=count_metrics_report,
            count_anomalies=count_anomalies,)
    elif int(status) == -4:
        reports = db((db.report_restriction.start_date>=start)&
            (db.report_restriction.end_date<=end)&
            (db.report.report_restriction==db.report_restriction.id)&
            (db.user_project.id==db.report.assignation)&
            (db.auth_user.id==db.user_project.assigned_user)&
            (db.project.id==db.user_project.project)&
            (db.report.never_delivered == True))
        status_instance = reports.select()
        response.view = 'admin/report_filter_never_delivered.html'
        return dict(status_instance=status_instance,
            count_log_entries=count_log_entries,
            count_metrics_report=count_metrics_report,
            count_anomalies=count_anomalies,
            status=status,
            period=period)
    else:
        reports = db((db.report.created>start)&
            (db.report.created<end)&
            (db.report.status==status)).select(db.report.ALL)
        status_instance = db(db.report_status.id==status).select().first()
    return dict(reports=reports,
        count_log_entries=count_log_entries,
        count_metrics_report=count_metrics_report,
        count_anomalies=count_anomalies,
        calculate_ending_date=calculate_ending_date,
        status = status,
        status_instance = status_instance,
        period = period)

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
    from datetime import datetime
    cperiod = cpfecys.current_year_period()
    year = str(cperiod.yearp)
        
    if request.function == 'new':
        db.item.created.writable=db.item.created.readable=False
    grid = SQLFORM.smartgrid(db.item_restriction,  \
        linked_tables=['item_restriction_area', 'item_restriction_exception'])
    return dict(grid=grid, year=year)

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
def delivered_download():
    if request.args(0) == 'type':
        period = request.vars['period']
        restrictions = db((db.item_restriction.period==period)&
            (db.item_restriction.is_enabled==True)&
            (db.item_restriction.item_type==db.item_type(name='File')))
        restrictions = restrictions.select(db.item_restriction.ALL)
        response.view = 'admin/delivered_download_restrictions.html'
        return dict(restrictions=restrictions)

    elif request.args(0) == 'zip':
        import datetime
        period = request.vars['period']
        cdate = datetime.datetime.now().date()
        restriction = request.vars['restriction']
        r_instance = db(db.item_restriction.id==1
            ).select(db.item_restriction.ALL)
        file_name = cdate + T('Deliverable Items')
        items = db((db.item.item_restriction==restriction)&
            (db.item.uploaded_file!=None)&
            (db.item.uploaded_file!='')).select()
        files = []
        for item in items:
            files.append(item.uploaded_file)
        if len(files) > 0:
            return response.zip(request, files, db)
        session.flash = T('No files to download.')
        redirect(URL('admin', 'delivered_download/type', 
            vars=dict(period=period)))

    periods = db(db.period_year).select()
    return dict(periods=periods)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def send_item_mail():
    user = request.vars['user']
    item = request.vars['item']
    success = False
    if not (not item and not user):
        user = db(db.auth_user.id==user).select().first()
        item = db(db.item.id==item).select().first()
        comment = item.admin_comment or T('No comment')
        subject = T('Item rejected by admin, please take action.')
        message = T('An item you created has been rejected by admin,') \
            + T('the reason is ') + comment \
            + T('please proceed to replace the item, if you don\'t take\
                any action the item will remain disabled.')
        import cpfecys
        message += (cpfecys.get_custom_parameters().email_signature or '')
        was_sent = mail.send(to=user.email,
                  subject=subject,
                  message=message)
        #MAILER LOG
        db.mailer_log.insert(sent_message = message,
                             destination = str(user.email),
                             result_log = str(mail.error or '') + ':' + str(mail.result),
                             success = was_sent)
        item.update_record(
            notified_mail = True)
        success = True
    return success
@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def items_grid():
    import datetime
    cdate = datetime.datetime.now().date()
    period = request.vars['period']
    area = request.vars['area']
    context_string = T('All')
    period_entity = db(db.period_year.id==period).select().first()
    if period_entity:
        period_name = period_entity.period.name
        period_year = period_entity.yearp
        context_string = T(str(period_name)) + ' ' + str(period_entity.yearp)
    school_id = request.vars['school_id']
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
        ((period=='' or period==None) or (db.item.created==period))
        ).select(orderby=db.item.item_restriction.name)
    if request.args(0) == 'zip':
        files = []
        for item in items:
            files.append(item.uploaded_file)
        if len(files) > 0:
            return response.zip(request, files, db)
        response.flash = T('No files to download.')
    return dict(items=items,
        area=area,
        period=period,
        context_string=context_string,
        cdate=str(cdate))

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def toggle_active_item():
    item = request.vars['item']
    comment = request.vars['comment'] or None
    if item != None:
        item = db(db.item.id==item).select().first()
    if item != None:
        item.update_record(
            is_active = not item.is_active,
            admin_comment=comment)
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
def teacher_assignation_upload():
    import csv
    error_users = []
    warning_users = []
    uv_off = request.vars['uv_off'] or False
    success = False
    import cpfecys
    current_period = cpfecys.current_year_period()
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
                rusername = row[2] or ''
                rproject = row[0]
                rassignation_length = row[7]
                rpro_bono = (row[8] == 'Si') or (row[8] == 'si')
                rhours = row[9]
                remail = row[5]
                rphone = row[6] or ''
                rlast_name = row[3]
                rfirst_name = row[4]
                ## check if user exists
                usr = db.auth_user(db.auth_user.username == rusername)
                project = db.project(db.project.project_id == rproject)
                if usr is None:
                    ## find it on chamilo (db2)
                    if not uv_off:
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
                                                    first_name = usr.firstname,
                                                    email = usr.email)
                            #add user to role 'Teacher'
                            auth.add_membership('Teacher', usr)
                    else:
                        #insert a new user with csv data
                        usr = db.auth_user.insert(username = rusername,
                                                  email = remail,
                                                  first_name=rfirst_name,
                                                  last_name=rlast_name,
                                                  phone=rphone)
                        #add user to role 'Teacher'
                        auth.add_membership('Teacher', usr)
                else:
                    assignation = db.user_project(
                        (db.user_project.assigned_user == usr.id)&
                        (db.user_project.project == project)&
                        (db.user_project.period == current_period)&
                        (db.user_project.assignation_status == None))
                    if assignation != None:
                        row.append(T('Error: ') + T('User \
                         was already assigned, Please Manually Assign Him.'))
                        error_users.append(row)
                        continue
                if project != None:
                    db.user_project.insert(assigned_user = usr,
                                            project = project,
                                            period = current_period,
                                            periods = rassignation_length,
                                            pro_bono = rpro_bono,
                                            hours = rhours)
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
                periods = periods,
                current_period = current_period)
        response.flash = T('Data uploaded')
        return dict(success = success,
                    errors = error_users,
                    warnings = warning_users,
                    periods = periods,
                    current_period = current_period)
    return dict(success = False,
                file = False,
                periods = periods,
                current_period = current_period)


@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def assignation_upload():
    import csv
    error_users = []
    warning_users = []
    uv_off = request.vars['uv_off'] or False
    success = False
    import cpfecys
    current_period = cpfecys.current_year_period()
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
                rhours = row[6]
                remail = row[7]
                ## check if user exists
                usr = db.auth_user(db.auth_user.username == rusername)
                project = db.project(db.project.project_id == rproject)
                if usr is None:
                    ## find it on chamilo (db2)
                    if not uv_off:
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
                                                    first_name = usr.firstname,
                                                    email = usr.email)
                            #add user to role 'student'
                            auth.add_membership('Student', usr)
                    else:
                        #insert a new user with csv data
                        usr = db.auth_user.insert(username = rusername,
                                                  email = remail)
                        #add user to role 'student'
                        auth.add_membership('Student', usr)
                else:
                    assignation = db.user_project(
                        (db.user_project.assigned_user == usr.id)&
                        (db.user_project.project == project)&
                        (db.user_project.assignation_status == None))
                    if assignation != None:
                        row.append(T('Error: ') + T('User \
                         was already assigned, Please Manually Assign Him.'))
                        error_users.append(row)
                        #assignation.update_record(periods = \
                            #rassignation_length, pro_bono = \
                            #rpro_bono)
                        continue
                if project != None:
                    db.user_project.insert(assigned_user = usr,
                                            project = project,
                                            period = current_period,
                                            periods = rassignation_length,
                                            pro_bono = rpro_bono,
                                            hours = rhours)
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
                periods = periods,
                current_period = current_period)
        response.flash = T('Data uploaded')
        return dict(success = success,
                    errors = error_users,
                    warnings = warning_users,
                    periods = periods,
                    current_period = current_period)
    return dict(success = False,
                file = False,
                periods = periods,
                current_period = current_period)

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
def final_practice():
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
