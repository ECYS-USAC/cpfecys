# coding: utf8
# intente algo como
@auth.requires_login()
@auth.requires_membership('Student')
def index():
    import datetime
    current_date = datetime.datetime.now().date()
    assignations = db((db.user_project.assigned_user == auth.user.id)&
                      (db.user_project.assigned_user == db.auth_user.id)&
                      (db.user_project.project == db.project.id)&
                      (db.project.area_level == db.area_level.id)&
                      (db.user_project.period == db.period_year.id)).select()
    cyear_period = cpfecys.current_year_period()
    def available_reports(assignation_period):
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
        if assignation_period.period == cpfecys.first_period.id:
            date_min = datetime.datetime(assignation_period.yearp, 1, 1)
            date_max = datetime.datetime(assignation_period.yearp, 7, 1)
        else:
            date_min = datetime.datetime(assignation_period.yearp, 7, 1)
            date_max = datetime.datetime(assignation_period.yearp, 1, 1)
        return db((db.report_restriction.start_date <= current_date)&
                  (db.report_restriction.end_date >= current_date)&
                  (db.report_restriction.start_date >= date_min)&
                  (db.report_restriction.end_date >= date_min)&
                  (db.report_restriction.start_date < date_max)&
                  (db.report_restriction.end_date < date_max)&
                  (db.report_restriction.is_enabled == True))

    def available_item_restriction(period_year, user_project):
        return db(((db.item_restriction.period==period_year) |
                    (db.item_restriction.permanent==True))&
                (db.item_restriction.is_enabled==True)&
                (db.item_restriction_area.item_restriction==\
                    db.item_restriction.id)&
                (db.item_restriction_area.area_level==\
                    user_project.project.area_level.id)&
                (db.item_restriction.item_type!=2))

    def restriction_project_exception(item_restriction_id, assignation_id):
        return db((db.item_restriction_exception.project== \
                    assignation_id)&
                    (db.item_restriction_exception.item_restriction \
                        ==item_restriction_id))

    def items_instance(item_restriction, assignation):
        return db((db.item.item_restriction==item_restriction.id)&
                    (db.item.assignation==assignation.user_project.id)&
                    (db.item.is_active==True))

    def is_indate_range(report):
        import datetime
        current_date = datetime.datetime.now().date()
        next_date = report.score_date + datetime.timedelta(
                        days=cpfecys.get_custom_parameters().rescore_max_days)
        return current_date < next_date


    return dict(assignations = assignations,
                available_reports = available_reports,
                current_date = current_date,
                cyear_period = cyear_period,
                available_item_restriction = available_item_restriction,
                items_instance = items_instance,
                restriction_project_exception=restriction_project_exception,
                is_indate_range=is_indate_range)

@auth.requires_login()
@auth.requires_membership('Student')
def update_data():
    update_data_form = False
    if auth.user != None:
        cuser = db(db.auth_user.id==auth.user.id).select().first()
        form = FORM(
                        DIV(LABEL(T('First Name')),
                                    INPUT(_name="first_name",
                                        _type="text", _id="first_name",
                                        _value=cuser.first_name,
                                        requires=IS_NOT_EMPTY())),

                        DIV(LABEL(T('Last Name')),
                                       INPUT(_name="last_name",
                                        _type="text", _id="last_name",
                                         _value=cuser.last_name, 
                                         requires=IS_NOT_EMPTY())),

                        DIV(LABEL(T('Email')),
                                       INPUT(_name="email",
                                        _type="text", _id="email",
                                        _value=cuser.email,
                                        requires=IS_NOT_EMPTY())),

                        DIV(LABEL(T('Password (Leave the same for no \
                            change)')),
                                      INPUT(_name="password",
                                        _type="password", _id="password",
                                        _value=cuser.password,
                                        requires=IS_NOT_EMPTY())),

                        DIV(LABEL(T('Repeat password (Leave the blank for \
                            no change)')),
                                      INPUT(_name="repass",
                                        _type="password", _id="repass")),

                        DIV(LABEL(T('Phone')),
                                      INPUT(_name="phone", _type="text",
                                        _id="phone", _value=cuser.phone,
                                        requires=IS_LENGTH(minsize=8,
                                                        maxsize=12))),

                        DIV(LABEL(T('Working')),
                                      INPUT(_name="working",
                                        _type="checkbox", _id="working",
                                        _value=cuser.working)),

                        DIV(LABEL(T('Work Address')),
                                      INPUT(_name="work_address",
                                        _type="text", _id="work_address",
                                        _value=cuser.work_address)),
                        BR(),
                        DIV(INPUT(_type='submit',
                            _value=T('Update Profile'),
                            _class="btn-primary")),
                            _class="form-horizontal",)
        if form.process().accepted:
            first_name = request.vars['first_name']
            last_name = request.vars['last_name']
            email = request.vars['email']
            password = request.vars['password']
            repass = request.vars['repass']
            phone = request.vars['phone']
            working = request.vars['working']
            work_address = request.vars['work_address']

            #TODO analyze for aditional security steps
            cuser=db(db.auth_user.id==auth.user.id).select().first()
            if cuser != None:
                cuser.first_name = first_name
                cuser.last_name = last_name
                cuser.email = email
                cuser.phone = phone
                cuser.data_updated = True
                if password == repass and len(repass) > 0:
                    #TODO Fix password update
                    cuser.password = db.auth_user.password.validate(password)[0]
                if working:
                    cuser.working = working
                    cuser.work_address = work_address

                cuser.update_record()
                response.flash = 'User data updated!'
                redirect(URL('default', 'index'))
            else:
                response.flash = 'Error!'

        elif form.errors:
            response.flash = 'form has errors'
        else:
            response.flash = 'please fill the form'
    return dict(form=form, update_data_form=True)

@cache.action()
@auth.requires_login()
@auth.requires_membership('Student')
def download():
    item = db(db.item.uploaded_file==request.args[0]).select().first()
    if item != None and item.assignation.assigned_user == auth.user.id:
        return response.download(request, db)
    else:
        session.flash = T('Access Forbidden')
        redirect(URL('default', 'index'))

@auth.requires_login()
@auth.requires_membership('Student')
def report_hours():
    if (request.args(0) == 'create'):
        report = request.vars['report']
        hours = request.vars['report-hours']
        ## Get the report id
        report = db.report(db.report.id == report)
        valid = not(report is None) and not(hours is None)
        ## Validate report TIMING restriction
        if valid: valid = cpfecys.student_validation_report_restrictions(report.report_restriction.id)
        ## Validate that the report belongs to user
        if valid: valid = cpfecys.student_validation_report_owner(report.id)
        ## Validate that the report status is editable (it is either 'Draft' or 'Recheck')
        if valid: valid = cpfecys.student_validation_report_status(report)
        if valid:
            report.hours = hours
            report.update_record()
            session.flash = T('Report updated.')
            redirect(URL('student','report/edit', vars = dict(report = report.id)))
        else:
            session.flash = T('Selected report can\'t be edited. Select a valid report.')
            redirect(URL('student','index'))
    elif (request.args(0) == 'update'):
        report = request.vars['report']
        hours = request.vars['report-hours']
        report = db.report(db.report.id == report)
        valid = not(report is None) and not(hours is None)
        ## Validate report TIMING restriction
        if valid: valid = cpfecys.student_validation_report_restrictions(report.report_restriction.id)
        ## Validate that the report belongs to user
        if valid: valid = cpfecys.student_validation_report_owner(report.id)
        ## Validate that the report status is editable (it is either 'Draft' or 'Recheck')
        if valid: valid = cpfecys.student_validation_report_status(report)
        if valid:
            report.hours = hours
            report.update_record()
            session.flash = T('Report updated.')
            redirect(URL('student','report/edit', vars = dict(report = report.id)))
        else:
            session.flash = T('Selected report can\'t be edited. Select a valid report.')
            redirect(URL('student','index'))
    elif (request.args(0) == 'delete'):
        report = request.vars['report']
        report = db.report(db.report.id == report)
        valid = not(report is None)
        ## Validate report TIMING restriction
        if valid: valid = cpfecys.student_validation_report_restrictions(report.report_restriction.id)
        ## Validate that the report belongs to user
        if valid: valid = cpfecys.student_validation_report_owner(report.id)
        ## Validate that the report status is editable (it is either 'Draft' or 'Recheck')
        if valid: valid = cpfecys.student_validation_report_status(report)
        if valid:
            report.hours = None
            report.update_record()
            session.flash = T('Report updated.')
            redirect(URL('student','report/edit', vars = dict(report = report.id)))
        else:
            session.flash = T('Selected report can\'t be edited. Select a valid report.')
            redirect(URL('student','index'))
    raise HTTP(404)

@auth.requires_login()
@auth.requires_membership('Student')
def report_header():
    if (request.args(0) == 'create'):
        report = request.vars['report']
        content = request.vars['report-content']
        ## Get the report id
        report = db.report(db.report.id == report)
        valid = not(report is None) and not(content is None)
        ## Validate report TIMING restriction
        if valid: valid = cpfecys.student_validation_report_restrictions(report.report_restriction.id)
        ## Validate that the report belongs to user
        if valid: valid = cpfecys.student_validation_report_owner(report.id)
        ## Validate that the report status is editable (it is either 'Draft' or 'Recheck')
        if valid: valid = cpfecys.student_validation_report_status(report)
        if valid:
            report.heading = content
            report.update_record()
            session.flash = T('Report updated.')
            redirect(URL('student','report/edit', vars = dict(report = report.id)))
        else:
            session.flash = T('Selected report can\'t be edited. Select a valid report.')
            redirect(URL('student','index'))
    elif (request.args(0) == 'update'):
        report = request.vars['report']
        content = request.vars['report-content']
        report = db.report(db.report.id == report)
        valid = not(report is None) and not(content is None)
        ## Validate report TIMING restriction
        if valid: valid = cpfecys.student_validation_report_restrictions(report.report_restriction.id)
        ## Validate that the report belongs to user
        if valid: valid = cpfecys.student_validation_report_owner(report.id)
        ## Validate that the report status is editable (it is either 'Draft' or 'Recheck')
        if valid: valid = cpfecys.student_validation_report_status(report)
        if valid:
            report.heading = content
            report.update_record()
            session.flash = T('Report updated.')
            redirect(URL('student','report/edit', vars = dict(report = report.id)))
        else:
            session.flash = T('Selected report can\'t be edited. Select a valid report.')
            redirect(URL('student','index'))
    elif (request.args(0) == 'delete'):
        report = request.vars['report']
        report = db.report(db.report.id == report)
        valid = not(report is None)
        ## Validate report TIMING restriction
        if valid: valid = cpfecys.student_validation_report_restrictions(report.report_restriction.id)
        ## Validate that the report belongs to user
        if valid: valid = cpfecys.student_validation_report_owner(report.id)
        ## Validate that the report status is editable (it is either 'Draft' or 'Recheck')
        if valid: valid = cpfecys.student_validation_report_status(report)
        if valid:
            report.heading = None
            report.update_record()
            session.flash = T('Report updated.')
            redirect(URL('student','report/edit', vars = dict(report = report.id)))
        else:
            session.flash = T('Selected report can\'t be edited. Select a valid report.')
            redirect(URL('student','index'))
    raise HTTP(404)

@auth.requires_login()
@auth.requires_membership('Student')
def report_footer():
    if (request.args(0) == 'create'):
        report = request.vars['report']
        content = request.vars['report-content']
        ## Get the report id
        report = db.report(db.report.id == report)
        valid = not(report is None) and not(content is None)
        ## Validate report TIMING restriction
        if valid: valid = cpfecys.student_validation_report_restrictions(report.report_restriction.id)
        ## Validate that the report belongs to user
        if valid: valid = cpfecys.student_validation_report_owner(report.id)
        ## Validate that the report status is editable (it is either 'Draft' or 'Recheck')
        if valid: valid = cpfecys.student_validation_report_status(report)
        if valid:
            report.footer = content
            report.update_record()
            session.flash = T('Report updated.')
            redirect(URL('student','report/edit', vars = dict(report = report.id)))
        else:
            session.flash = T('Selected report can\'t be edited. Select a valid report.')
            redirect(URL('student','index'))
    elif (request.args(0) == 'update'):
        report = request.vars['report']
        content = request.vars['report-content']
        report = db.report(db.report.id == report)
        valid = not(report is None) and not(content is None)
        ## Validate report TIMING restriction
        if valid: valid = cpfecys.student_validation_report_restrictions(report.report_restriction.id)
        ## Validate that the report belongs to user
        if valid: valid = cpfecys.student_validation_report_owner(report.id)
        ## Validate that the report status is editable (it is either 'Draft' or 'Recheck')
        if valid: valid = cpfecys.student_validation_report_status(report)
        if valid:
            report.footer = content
            report.update_record()
            session.flash = T('Report updated.')
            redirect(URL('student','report/edit', vars = dict(report = report.id)))
        else:
            session.flash = T('Selected report can\'t be edited. Select a valid report.')
            redirect(URL('student','index'))
    elif (request.args(0) == 'delete'):
        report = request.vars['report']
        report = db.report(db.report.id == report)
        valid = not(report is None)
        ## Validate report TIMING restriction
        if valid: valid = cpfecys.student_validation_report_restrictions(report.report_restriction.id)
        ## Validate that the report belongs to user
        if valid: valid = cpfecys.student_validation_report_owner(report.id)
        ## Validate that the report status is editable (it is either 'Draft' or 'Recheck')
        if valid: valid = cpfecys.student_validation_report_status(report)
        if valid:
            report.footer = None
            report.update_record()
            session.flash = T('Report updated.')
            redirect(URL('student','report/edit', vars = dict(report = report.id)))
        else:
            session.flash = T('Selected report can\'t be edited. Select a valid report.')
            redirect(URL('student','index'))
    raise HTTP(404)

@auth.requires_login()
@auth.requires_membership('Student')
def item():
    cyear_period = cpfecys.current_year_period()
    item_restriction = request.vars['restriction']
    user_project = request.vars['assignation']
    item_query = db((db.item.created==cyear_period)&
                (db.item.item_restriction==item_restriction)&
                (db.item.assignation==user_project))
    item_restriction = db(db.item_restriction.id==\
            item_restriction).select().first()

    if(request.args(0) == 'create'):
        if item_query.select().first() == None:
            if item_restriction.item_type.name == 'File' and \
                item_restriction.teacher_only != True:

                form = FORM(
                            DIV(LABEL(T('Upload '+item_restriction.name+' \
                            File:')),
                            INPUT(_name="upload", 
                                _type="file", _id="first_name", 
                                requires=[IS_NOT_EMPTY(), \
                                            IS_UPLOAD_FILENAME( \
                                            extension='^(pdf|doc|docx)$',\
                                            error_message=T('Invalid Format, \
                                            Please upload only PDF, DOC or \
                                            DOCX files files'))])),
                            BR(),
                            DIV(INPUT(_type='submit',
                                            _value=T('Upload File'),
                                            _class="btn-primary")),
                                            _class="form-horizontal",)
                if form.process().accepted:
                    if request.vars.upload != None:
                        item = db.item.uploaded_file.store( \
                            request.vars.upload.file,  \
                            request.vars.upload.filename)
                        db.item.insert(uploaded_file=item,
                            is_active=True,
                            created=cyear_period,
                            item_restriction=item_restriction.id,
                            assignation=user_project)
                        db.commit()
                        session.flash = T('Item created!')
                        redirect(URL('student', 'index'))
                    else:
                        session.flash = T('Error')
                        redirect(URL('student', 'index'))
                elif form.errors:
                    session.flash = T('Errors')
                    redirect(URL('student', 'index'))
                else:
                    session.flash = T('please fill the form')
                return  dict(form=form, action='create')
        else:
            session.flash = T('Action not allowed')
            redirect(URL('student', 'index'))

    elif(request.args(0) == 'view'):
        item_upload = request.vars['file']
        item = db((db.item.item_restriction==item_restriction)&
            (db.item.assignation==user_project)&
            (db.item.uploaded_file==item_upload)).select().first()
        if item != None and item_restriction.teacher_only != True \
                and item.is_active == True \
                and item.assignation.assigned_user == auth.user.id:
            return dict(item=item, name=item_restriction.name, action='view')
        else:
            session.flash = T('Access Forbidden')
            redirect(URL('student', 'index'))

    elif(request.args(0) == 'edit'):
        item = db((db.item.created==cyear_period)&
            (db.item.item_restriction==item_restriction)&
            (db.item.assignation==user_project)).select().first()
        if item == None or item_restriction.teacher_only == True \
                or item.is_active != True:
            redirect(URL('student', 'index'))
        form = FORM(
                    DIV(LABEL(T('Upload '+item_restriction.name+' \
                        File:')),
                                INPUT(_name="upload", 
                                    _type="file", _id="first_name", 
                                    requires=[IS_NOT_EMPTY(), \
                                            IS_UPLOAD_FILENAME( \
                                            extension='^(pdf|doc|docx)$',\
                                            error_message=T('Invalid Format, \
                                            Please upload only PDF, DOC or \
                                            DOCX files files'))])),
                    BR(),
                    DIV(INPUT(_type='submit',
                        _value=T('Upload File'),
                        _class="btn-primary")),
                        _class="form-horizontal",)
        if form.process().accepted:
            if request.vars.upload != None:
                uploaded = db.item.uploaded_file.store(request.vars.upload.file, request.vars.upload.filename)
                item = db((db.item.created==cyear_period)&
                    (db.item.item_restriction==item_restriction)&
                    (db.item.assignation==user_project)).select().first()
                if item != None:
                    item.update_record(uploaded_file = uploaded)
                    db.commit()
                    redirect(URL('student', 'index'))
                elif form.errors:
                    response.flash = "Errors"
                else:
                    response.flash = "please fill the form"
        return  dict(form=form, action='edit')

@auth.requires_login()
@auth.requires_membership('Student')
def report():
    if (request.args(0) == 'create'):
        #get the data & save the report
        assignation = request.vars['assignation']
        report_restriction = request.vars['report_restriction']
        # Validate DB report_restriction to obey TIMING rules
        valid_rep_restr = cpfecys.student_validation_report_restrictions(report_restriction)
        # Validate report_restriction
        report_restrict = db.report_restriction(db.report_restriction.id == report_restriction)
        valid_report = report_restrict != None
        # Validate assignation belongs to this user
        assign = db.user_project((db.user_project.id == assignation)&
                                (db.user_project.assigned_user == auth.user.id))
        valid_assignation = assign != None
        # Validate there is not an already inserted report
        valid = db.report((db.report.assignation == assignation)&
                  (db.report.report_restriction == report_restriction)) is None
        if not(assignation and report_restriction and valid and valid_assignation and valid_report
           and valid_rep_restr):
            session.flash = T('Invalid selected assignation and report. Select a valid one.')
            redirect(URL('student','index'))
        import datetime
        current_date = datetime.datetime.now()
        report = db.report.insert(created = current_date,
                             assignation = assignation,
                             report_restriction = report_restriction,
                             status = db.report_status(name = 'Draft'),
                             period = cpfecys.current_year_period())
        session.flash = T('Report is now a draft.')
        redirect(URL('student','report/edit', vars = dict(report = report.id)))
    elif (request.args(0) == 'edit'):
        ## Get the report id
        report = request.vars['report']
        ## Retrieve report data
        report = db.report(db.report.id == report)
        if not(report):
            session.flash = T('Selected report can\'t be edited. Select a valid report.')
            redirect(URL('student','index'))
        ## Validate report TIMING restriction
        valid_rep_restr = cpfecys.student_validation_report_restrictions(report.report_restriction.id)
        if not(valid_rep_restr):
            session.flash = T('Selected report can\'t be edited. Select a valid report.')
            redirect(URL('student','index'))
        ## Validate that the report belongs to user
        valid_report_owner = cpfecys.student_validation_report_owner(report.id)
        if not(valid_report_owner):
            session.flash = T('Selected report can\'t be edited. Select a valid report.')
            redirect(URL('student','index'))
        ## Validate that the report status is editable (it is either 'Draft' or 'Recheck')
        if not(cpfecys.student_validation_report_status(report)):
            session.flash = T('Selected report can\'t be edited. Select a valid report.')
            redirect(URL('student','index'))
        ## Markmin formatting of reports
        response.view = 'student/report_edit.html'
        assignation_reports = db(db.report.assignation == report.assignation).select()
        # check minimun requirements
        reqs = db(db.area_report_requirement.area_level == report.assignation.project.area_level).select()
        minimal_requirements = True
        activities_count = db(db.log_entry.report == report.id).count()
        metrics_count = db(db.log_metrics.report == report.id).count()
        for req in reqs:
            if (req.report_requirement.name == 'Encabezado') and (report.heading is None):
                minimal_requirements = False
                break
            if (req.report_requirement.name == 'Pie de Reporte') and (report.footer is None):
                minimal_requirements = False
                break
            if (req.report_requirement.name == 'Registrar Actividad') and (activities_count == 0):
                minimal_requirements = False
                break
            if (req.report_requirement.name == 'Registrar Actividad con Metricas') and (metrics_count == 0):
                minimal_requirements = False
                break
            if (req.report_requirement.name == 'Registrar Deserciones') and (report.desertion_started is None):
                minimal_requirements = False
                break
            if (req.report_requirement.name == 'Registrar Horas Completadas') and (report.hours is None):
                minimal_requirements = False
                break
        mandatory_requirements = ''
        for req in reqs:
            mandatory_requirements += req.report_requirement.name  + ', '
        return dict(log_types = db(db.log_type.id > 0).select(),
                    mandatory_requirements = mandatory_requirements,
                    minimal_requirements = minimal_requirements,
                    assignation_reports = assignation_reports,
                    logs = db((db.log_entry.report == report.id)).select(),
                    metrics = db((db.log_metrics.report == report.id)).select(),
                    metrics_type = db(db.metrics_type).select(),
                    anomalies = db((db.log_type.name == 'Anomaly')&
                                   (db.log_entry.log_type == db.log_type.id)&
                                   (db.log_entry.report == report.id)).count(),
                    markmin_settings = cpfecys.get_markmin,
                    report = report)
    elif (request.args(0) == 'acceptance'):
        #get the data & save the report
        report = request.vars['report']
        report = db.report(db.report.id == report)
        # Check minimun requirements
        reqs = db(db.area_report_requirement.area_level == report.assignation.project.area_level).select()
        minimal_requirements = True
        activities_count = db(db.log_entry.report == report.id).count()
        metrics_count = db(db.log_metrics.report == report.id).count()
        for req in reqs:
            if (req.report_requirement.name == 'Encabezado') and (report.heading is None):
                minimal_requirements = False
                break
            if (req.report_requirement.name == 'Pie de Reporte') and (report.footer is None):
                minimal_requirements = False
                break
            if (req.report_requirement.name == 'Registrar Actividad') and (activities_count == 0):
                minimal_requirements = False
                break
            if (req.report_requirement.name == 'Registrar Actividad con Metricas') and (metrics_count == 0):
                minimal_requirements = False
                break
            if (req.report_requirement.name == 'Registrar Deserciones') and (report.desertion_started is None):
                minimal_requirements = False
                break
            if (req.report_requirement.name == 'Registrar Horas Completadas') and (report.hours is None):
                minimal_requirements = False
                break
        if not minimal_requirements:
            session.flash = T('Selected report can\'t be accepted, it lacks mandatory blocks.')
            redirect(URL('student','index'))
        # Validate DB report_restriction to obey TIMING rules
        valid_rep_restr = cpfecys.student_validation_report_restrictions(report.report_restriction.id)
        ## Validate that the report status is editable (it is either 'Draft' or 'Recheck')
        if not(cpfecys.student_validation_report_status(report)):
            session.flash = T('Invalid selected assignation and report. Select a valid one.')
            redirect(URL('student','index'))
        # Validate assignation belongs to this user
        assign = db.user_project((db.user_project.id == report.assignation)&
                                (db.user_project.assigned_user == auth.user.id))
        valid_assignation = assign != None
        if not(report and valid_assignation and valid_rep_restr):
            session.flash = T('Invalid selected assignation and report. Select a valid one.')
            redirect(URL('student','index'))
        import datetime
        current_date = datetime.datetime.now()
        if(report.status.name=='Recheck'):
            import datetime
            dated = datetime.datetime.now().date()
            next_date = report.score_date + datetime.timedelta(
                            days=cpfecys.get_custom_parameters().rescore_max_days)
            if not(dated < next_date):
                session.flash = T('Selected report can\'t be edited. Select a valid report.')
                redirect(URL('student','index'))
        report.update_record(created = current_date,
                      status = db.report_status(name = 'Grading'))
        session.flash = T('Report sent to Grading.')
        # Notification Message
        me_the_user = db.auth_user(db.auth_user.id == auth.user.id)
        message = '<html>' + T('The report') + ' ' \
        + '<b>' + XML(report.report_restriction['name']) + '</b><br/>' \
        + T('sent by student: ') + XML(me_the_user.username) + ' ' \
        + XML(me_the_user.first_name) + ' ' + XML(me_the_user.last_name) \
        + '<br/>' \
        + T('was sent to be checked.') + '<br/>' + T('Checking can be done in:') \
        + ' http://omnomyumi.com/dtt/' + '</html>'
        # send mail to teacher and student notifying change.
        mails = []
        # retrieve teacher's email
        teachers = db((db.project.id == assign.project)&
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
        redirect(URL('student','index'))
    elif (request.args(0) == 'view'):
        #Get the report id
        report = request.vars['report']
        # Validate that the report exists
        report = db.report(db.report.id == report)
        valid = not(report is None)
        # Validate that the report belongs to user
        if valid: valid = cpfecys.student_validation_report_owner(report.id)
        if valid:
            ## Markmin formatting of reports
            response.view = 'student/report_view.html'
            assignation_reports = db(db.report.assignation == report.assignation).select()
            return dict(log_types = db(db.log_type.id > 0).select(),
                        assignation_reports = assignation_reports,
                        logs = db((db.log_entry.report == report.id)).select(),
                        metrics = db((db.log_metrics.report == report.id)).select(),
                        anomalies = db((db.log_type.name == 'Anomaly')&
                                   (db.log_entry.log_type == db.log_type.id)&
                                   (db.log_entry.report == report.id)).count(),
                        markmin_settings = cpfecys.get_markmin,
                        report = report)
        else:
            session.flash = T('Selected report can\'t be viewed. Select a valid report.')
            redirect(URL('student', 'index'))
    else:
        redirect(URL('student', 'index'))
    raise HTTP(404)

@auth.requires_login()
@auth.requires_membership('Student')
def log():
    if (request.args(0) == 'save'):
        # validate the user owns this report
        report = request.vars['report']
        report = db.report(db.report.id == report)
        valid_report = report != None
        if valid_report: valid_report = cpfecys.student_validation_report_owner(report.id)
        # validate report is editable
        if valid_report: valid_report = cpfecys.student_validation_report_restrictions \
            (report.report_restriction)
        # validate report is 'Draft' or 'Recheck'
        if valid_report: valid_report = cpfecys.student_validation_report_status(report)
        # validate we receive log-date, log-type, log-content
        log_type = request.vars['log-type']
        log_date = request.vars['log-date']
        log_content = request.vars['log-content']
        if valid_report: valid_report = (log_type and log_date and log_content)
        if valid_report:
            db.log_entry.insert(log_type = log_type,
                                entry_date = log_date,
                                description = log_content,
                                report = report.id,
                                period=cpfecys.current_year_period())
            session.flash = T('Log added')
            redirect(URL('student', 'report/edit', vars=dict(report=report.id)))
        else:
            session.flash = T('Operation not allowed.')
            redirect(URL('student', 'index'))
    elif (request.args(0) == 'update'):
        # validate the requested log
        log = request.vars['log']
        log = db.log_entry(db.log_entry.id == log)
        valid_log = log != None
        # validate log report owner is valid
        if valid_log: valid_log = cpfecys.student_validation_report_owner(log.report)
        # validate report is editable
        if valid_log: valid_log = cpfecys.student_validation_report_restrictions \
            (log.report['report_restriction'])
        # validate report is 'Draft' or 'Recheck'
        if valid_log: valid_log = cpfecys.student_validation_report_status \
            (db.report(db.report.id == log.report))
        # validate we receive log-date, log-type, log-content
        log_type = request.vars['log-type']
        log_date = request.vars['log-date']
        log_content = request.vars['log-content']
        if valid_log: valid_log = (log_type and log_date and log_content)
        if valid_log:
            log.update_record(log_type = log_type,
                              entry_date = log_date,
                              description = log_content)
            session.flash = T('Log Updated')
            redirect(URL('student', 'report/edit', vars=dict(report=log.report)))
        else:
            session.flash = T('Operation not allowed.')
            redirect(URL('student', 'index'))
    elif (request.args(0) == 'delete'):
        # validate the requested log
        log = request.vars['log']
        log = db.log_entry(db.log_entry.id == log)
        valid_log = log != None
        # validate log report owner is valid
        if valid_log: valid_log = cpfecys.student_validation_report_owner(log.report)
        # validate report is editable
        if valid_log: valid_log = cpfecys.student_validation_report_restrictions \
            (log.report['report_restriction'])
        # validate report is 'Draft' or 'Recheck'
        if valid_log: valid_log = cpfecys.student_validation_report_status \
            (db.report(db.report.id == log.report))
        if valid_log:
            log.delete_record()
            session.flash = T('Log Deleted')
            redirect(URL('student', 'report/edit', vars=dict(report=log.report)))
        else:
            session.flash = T('Operation not allowed.')
            redirect(URL('student', 'index'))
    raise HTTP(404)


@auth.requires_login()
@auth.requires_membership('Student')
def metrics():
    import datetime
    cdate = datetime.datetime.now()
    if (request.args(0) == 'save'):
        # validate the user owns this report
        report = request.vars['report']
        report = db.report(db.report.id == report)
        valid_report = report != None
        if valid_report: valid_report = cpfecys.student_validation_report_owner(report.id)
        # validate report is editable
        if valid_report: valid_report = cpfecys.student_validation_report_restrictions \
            (report.report_restriction)
        # validate report is 'Draft' or 'Recheck'
        if valid_report: valid_report = cpfecys.student_validation_report_status(report)
        # validate we receive log-date, log-type, log-content

        media = request.vars['media-metrics']
        error_tipico = request.vars['error-tipico-metrics']
        mediana = request.vars['mediana-metrics']
        moda = request.vars['moda-metrics']
        desviacion_estandar = request.vars['desviacion-estandar-metrics']
        varianza = request.vars['varianza-metrics']
        curtosis = request.vars['curtosis-metrics']
        coeficiente = request.vars['coeficiente-metrics']
        rango = request.vars['rango-metrics']
        minimo = request.vars['minimo-metrics']
        maximo = request.vars['maximo-metrics']
        total = request.vars['total-metrics']
        reprobados = request.vars['reprobados-metrics']
        aprobados = request.vars['aprobados-metrics']
        metric_type = request.vars['metric-type']
        log_date = request.vars['log-date']

        if valid_report: valid_report = (media and error_tipico and mediana \
                                         and moda and desviacion_estandar  
                                         and varianza and curtosis \
                                         and coeficiente and rango \
                                         and minimo and maximo and total \
                                         and reprobados and aprobados \
                                         and metric_type and log_date)

        if valid_report:
            db.log_metrics.insert(report = report.id,
                                media = media,
                                error = error_tipico,
                                mediana = mediana,
                                moda = moda,
                                desviacion = desviacion_estandar,
                                varianza = varianza,
                                curtosis = curtosis,
                                coeficiente = coeficiente,
                                rango = rango,
                                minimo = minimo,
                                maximo = maximo,
                                total = total,
                                reprobados = reprobados,
                                aprobados = aprobados,
                                created = log_date,
                                metrics_type = metric_type)
            session.flash = T('Log added')
            redirect(URL('student', 'report/edit', vars=dict(report=report.id)))
        else:
            session.flash = T('Operation not allowed.')
            redirect(URL('student', 'index'))
    elif (request.args(0) == 'update'):
        # validate the requested metric
        metric = request.vars['metric']
        metric = db.log_metrics(db.log_metrics.id == metric)
        valid_metric = metric != None
        # validate metric report owner is valid
        if valid_metric: valid_metric = cpfecys.student_validation_report_owner(metric.report)
        # validate report is editable
        if valid_metric: valid_metric = cpfecys.student_validation_report_restrictions \
            (metric.report['report_restriction'])
        # validate report is 'Draft' or 'Recheck'
        if valid_metric: valid_metric = cpfecys.student_validation_report_status \
            (db.report(db.report.id == metric.report))
        # validate we receive log-date, log-type, log-content
        
        media = request.vars['media-metrics']
        error_tipico = request.vars['error-tipico-metrics']
        mediana = request.vars['mediana-metrics']
        moda = request.vars['moda-metrics']
        desviacion_estandar = request.vars['desviacion-estandar-metrics']
        varianza = request.vars['varianza-metrics']
        curtosis = request.vars['curtosis-metrics']
        coeficiente = request.vars['coeficiente-metrics']
        rango = request.vars['rango-metrics']
        minimo = request.vars['minimo-metrics']
        maximo = request.vars['maximo-metrics']
        total = request.vars['total-metrics']
        reprobados = request.vars['reprobados-metrics']
        aprobados = request.vars['aprobados-metrics']
        metric_type = request.vars['metric-type']
        log_date = request.vars['log-date']
        if valid_metric: valid_metric = (media and error_tipico and mediana \
                                         and moda and desviacion_estandar  
                                         and varianza and curtosis \
                                         and coeficiente and rango \
                                         and minimo and maximo and total \
                                         and reprobados and aprobados \
                                         and metric_type and log_date)
        if valid_metric:
            metric.update_record(report = metric.report.id,
                                media = media,
                                error = error_tipico,
                                mediana = mediana,
                                moda = moda,
                                desviacion = desviacion_estandar,
                                varianza = varianza,
                                curtosis = curtosis,
                                coeficiente = coeficiente,
                                rango = rango,
                                minimo = minimo,
                                maximo = maximo,
                                total = total,
                                reprobados = reprobados,
                                aprobados = aprobados,
                                created = log_date,
                                metrics_type = metric_type)
            session.flash = T('Metric Updated')
            redirect(URL('student', 'report/edit', vars=dict(report=metric.report)))
        else:
            session.flash = T('Operation not allowed.')
            redirect(URL('student', 'index'))
    elif (request.args(0) == 'delete'):
        # validate the requested metric
        metric = request.vars['metric']
        metric = db.log_metrics(db.log_metrics.id == metric)
        valid_metric = metric != None
        # validate metric report owner is valid
        if valid_metric: valid_metric = cpfecys.student_validation_report_owner(metric.report)
        # validate report is editable
        if valid_metric: valid_metric = cpfecys.student_validation_report_restrictions \
            (metric.report['report_restriction'])
        # validate report is 'Draft' or 'Recheck'
        if valid_metric: valid_metric = cpfecys.student_validation_report_status \
            (db.report(db.report.id == metric.report))
        if valid_metric:
            metric.delete_record()
            session.flash = T('Log Deleted')
            redirect(URL('student', 'report/edit', vars=dict(report=metric.report)))
        else:
            session.flash = T('Operation not allowed.')
            redirect(URL('student', 'index'))
    raise HTTP(404)

@auth.requires_login()
@auth.requires_membership('Student')
def desertions():
    if (request.args(0) == 'save'):
        # validate the user owns this report
        report = request.vars['report']
        report = db.report(db.report.id == report)
        valid_report = report != None
        if valid_report: valid_report = cpfecys.student_validation_report_owner(report.id)
        # validate report is editable
        if valid_report: valid_report = cpfecys.student_validation_report_restrictions \
            (report.report_restriction)
        # validate report is 'Draft' or 'Recheck'
        if valid_report: valid_report = cpfecys.student_validation_report_status(report)
        # validate we receive log-date, log-type, log-content
        desertion_started = request.vars['desertion-started']
        desertion_gone = request.vars['desertion-gone']
        desertion_continued = request.vars['desertion-continued']
        if valid_report: valid_report = (desertion_started and desertion_gone
                                         and desertion_continued)
        if valid_report:
            report.desertion_started = desertion_started
            report.desertion_gone = desertion_gone
            report.desertion_continued = desertion_continued
            report.update_record()
            session.flash = T('Desertion log added')
            redirect(URL('student', 'report/edit', vars=dict(report=report.id)))
        else:
            session.flash = T('Operation not allowed.')
            redirect(URL('student', 'index'))
    elif (request.args(0) == 'update'):
        # validate the user owns this report
        report = request.vars['report']
        report = db.report(db.report.id == report)
        valid_report = report != None
        if valid_report: valid_report = cpfecys.student_validation_report_owner(report.id)
        # validate report is editable
        if valid_report: valid_report = cpfecys.student_validation_report_restrictions \
            (report.report_restriction)
        # validate report is 'Draft' or 'Recheck'
        if valid_report: valid_report = cpfecys.student_validation_report_status(report)
        # validate we receive log-date, log-type, log-content
        desertion_started = request.vars['desertion-started']
        desertion_gone = request.vars['desertion-gone']
        desertion_continued = request.vars['desertion-continued']
        if valid_report: valid_report = (desertion_started and desertion_gone
                                         and desertion_continued)
        if valid_report:
            report.desertion_started = desertion_started
            report.desertion_gone = desertion_gone
            report.desertion_continued = desertion_continued
            report.update_record()
            session.flash = T('Desertion log updated')
            redirect(URL('student', 'report/edit', vars=dict(report=report.id)))
        else:
            session.flash = T('Operation not allowed.')
            redirect(URL('student', 'index'))
    elif (request.args(0) == 'delete'):
        # validate the user owns this report
        report = request.vars['report']
        report = db.report(db.report.id == report)
        valid_report = report != None
        if valid_report: valid_report = cpfecys.student_validation_report_owner(report.id)
        # validate report is editable
        if valid_report: valid_report = cpfecys.student_validation_report_restrictions \
            (report.report_restriction)
        # validate report is 'Draft' or 'Recheck'
        if valid_report: valid_report = cpfecys.student_validation_report_status(report)
        # validate we receive log-date, log-type, log-content
        desertion_started = request.vars['desertion-started']
        desertion_gone = request.vars['desertion-gone']
        desertion_continued = request.vars['desertion-continued']
        if valid_report: valid_report = (desertion_started and desertion_gone
                                         and desertion_continued)
        if valid_report:
            report.desertion_started = None
            report.desertion_gone = None
            report.desertion_continued = None
            report.update_record()
            session.flash = T('Desertion log removed')
            redirect(URL('student', 'report/edit', vars=dict(report=report.id)))
        else:
            session.flash = T('Operation not allowed.')
            redirect(URL('student', 'index'))
    raise HTTP(404)
