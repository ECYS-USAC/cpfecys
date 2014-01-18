# coding: utf8
# intente algo como
@auth.requires_login()
@auth.requires_membership('Student')
def index():
    assignations = db((db.user_project.assigned_user == auth.user.id)&
                      (db.user_project.assigned_user == db.auth_user.id)&
                      (db.user_project.project == db.project.id)&
                      (db.project.area_level == db.area_level.id)&
                      (db.user_project.period == db.period_year.id)).select()
    cyear_period = get_current_year_period()
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
        if assignation_period.period == first_period.id:
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
        return db(  (
                        (db.item_restriction.period==period_year) |
                        (db.item_restriction.permanent==True)
                    )&
                (db.item_restriction.is_enabled==True)&
                (db.item_restriction_area.item_restriction==\
                    db.item_restriction.id)&
                (db.item_restriction_area.area_level==\
                    user_project.project.area_level.id))
    def items_instance(item_restriction, assignation):
        return db((db.item.item_restriction==item_restriction.id)&
                    (db.item.assignation==assignation.user_project.id)&
                    (db.item.is_active==True))

    import datetime
    current_date = datetime.datetime.now().date()
    return dict(assignations = assignations,
                available_reports = available_reports,
                current_date = current_date,
                cyear_period = cyear_period,
                available_item_restriction = available_item_restriction,
                items_instance = items_instance)

## Validate that the report date restriction and is_enabled restriction apply to current date
def val_rep_restr(report_restriction):
    import datetime
    current_date = datetime.datetime.now()
    rep_restr = db((db.report_restriction.id == report_restriction)&
        (db.report_restriction.start_date <= current_date)&
        (db.report_restriction.end_date >= current_date)&
        (db.report_restriction.is_enabled == True)).select().first()
    return rep_restr != None

## Validate that the report status is editable (it is either 'Draft' or 'Recheck')
def valid_status(report):
    return (report.status == db.report_status(db.report_status.name == 'Draft').id) or \
            (report.status == db.report_status(db.report_status.name == 'Recheck'))

def get_current_year_period():
    import datetime
    cdate = datetime.datetime.now()
    cyear = cdate.year
    cmonth = cdate.month
    period = second_period
    #current period depends if we are in dates between jan-jun and jul-dec
    if cmonth < 7 :
        period = first_period
    return db.period_year((db.period_year.yearp == cyear)&
                          (db.period_year.period == period))

def val_rep_owner(report):
    usr_rep = db((db.report.id == report)&
            (db.report.assignation == db.user_project.id)&
            (db.user_project.assigned_user == auth.user.id)).select().first()
    return usr_rep != None

@auth.requires_login()
@auth.requires_membership('Student')
def update_data():
    update_data_form = False
    if auth.user != None:
        cuser = db(db.auth_user.id==auth.user.id).select().first()
        form = FORM(
                        DIV(LABEL(T('First Name:')),
                                    INPUT(_name="first_name", 
                                        _type="text", _id="first_name", 
                                        _value=cuser.first_name,
                                        requires=IS_NOT_EMPTY())),

                        DIV(LABEL(T('Last Name:')),
                                       INPUT(_name="last_name", 
                                        _type="text", _id="last_name", 
                                         _value=cuser.last_name, 
                                         requires=IS_NOT_EMPTY())),

                        DIV(LABEL(T('Email:')),
                                       INPUT(_name="email", 
                                        _type="text", _id="email", 
                                        _value=cuser.email, 
                                        requires=IS_NOT_EMPTY())),

                        DIV(LABEL(T('Password: (Leave the same for no \
                            change)')),
                                      INPUT(_name="password", 
                                        _type="password", _id="password", 
                                        _value=cuser.password, 
                                        requires=IS_NOT_EMPTY())),

                        DIV(LABEL(T('Repeat password: (Leave the blank for \
                            no change)')),
                                      INPUT(_name="repass", 
                                        _type="password", _id="repass")),

                        DIV(LABEL(T('Phone:')),
                                      INPUT(_name="phone", _type="text", 
                                        _id="phone", _value=cuser.phone, 
                                        requires=IS_LENGTH(minsize=8, 
                                                        maxsize=12))),

                        DIV(LABEL(T('Working:')),
                                      INPUT(_name="working", 
                                        _type="checkbox", _id="working", 
                                        _value=cuser.working)),

                        DIV(LABEL(T('Work Address:')),
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
                    cuser.password = db.auth_user.password.validate(password)
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

@auth.requires_login()
@auth.requires_membership('Student')
def item():
    cyear_period = get_current_year_period()
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
                                            requires=IS_NOT_EMPTY())),
                            BR(),
                            DIV(INPUT(_type='submit', 
                                _value=T('Upload File'), 
                                _class="btn-primary")),
                                _class="form-horizontal",)
                if form.process().accepted:
                    if request.vars.upload != None:
                        item = db.item.uploaded_file.store(request.vars.upload.file, request.vars.upload.filename)
                        db.item.insert(uploaded_file=item,
                            is_active=True,
                            created=cyear_period,
                            item_restriction=item_restriction.id,
                            assignation=user_project)
                        db.commit()
                        response.flash = T('Item created!')
                        redirect(URL('student', 'index'))
                    else:
                        response.flash = T('Error')
                        redirect(URL('student', 'index'))
                elif form.errors:
                    response.flash = T('Errors')
                    redirect(URL('student', 'index'))
                else:
                    response.flash = T('please fill the form')
                return  dict(form=form, action='create')
        else:
            response.flash = T('Action not allowed')
            redirect(URL('student', 'index'))

    elif(request.args(0) == 'view'):
        item = db((db.item.item_restriction==item_restriction)&
            (db.item.assignation==user_project)).select().first()
        if item == None or item_restriction.teacher_only == True \
                or item.is_active != True:
            redirect(URL('student', 'index'))
        return dict(item=item, action='view')

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
                                    requires=IS_NOT_EMPTY())),
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
        valid_rep_restr = val_rep_restr(report_restriction)
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
                             status = db.report_status(name = 'Draft'))
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
        valid_rep_restr = val_rep_restr(report.report_restriction.id)
        ## Validate that the report belongs to user
        valid_report_owner = val_rep_owner(report.id)
        if not(valid_report_owner):
            session.flash = T('Selected report can\'t be edited. Select a valid report.')
            redirect(URL('student','index'))
        ## Validate that the report status is editable (it is either 'Draft' or 'Recheck')
        if not(valid_status(report)):
            session.flash = T('Selected report can\'t be edited. Select a valid report.')
            redirect(URL('student','index'))
        ## Markmin formatting of reports
        LATEX = '<img src="http://chart.apis.google.com/chart?cht=tx&chl=%s" align="center"/>'
        markmin_settings = {
            'latex':lambda code: LATEX % code.replace('"','"'),
            'code_cpp':lambda text: CODE(text,language='cpp').xml(),
            'code_java':lambda text: CODE(text,language='java').xml(),
            'code_python':lambda text: CODE(text,language='python').xml(),
            'code_html':lambda text: CODE(text,language='html').xml()}
        return dict(state = 'edit',
                    log_types = db(db.log_type.id > 0).select(),
                    logs = db((db.log_entry.id > 0)&
                              (db.log_entry.report == report.id)).select(),
                    anomalies = db((db.log_type.name == 'Anomaly')&
                                   (db.log_entry.log_type == db.log_type.id)&
                                   (db.log_entry.report == report.id)).count(),
                    markmin_settings = markmin_settings,
                    report = report)
    elif (request.args(0) == 'save'):
        #get the data & save the report
        report = request.vars['report']
        report = db.report(db.report.id == report)
        # Validate DB report_restriction to obey TIMING rules
        valid_rep_restr = val_rep_restr(report.report_restriction.id)
        ## Validate that the report status is editable (it is either 'Draft' or 'Recheck')
        if not(valid_status(report)):
            session.flash = T('Selected report can\'t be saved. Select a valid report.')
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
        report.update(created = current_date,
                      status = db.report_status(name = 'Draft'))
        session.flash = T('Draft Updated.')
        redirect(URL('student','index'))
    elif (request.args(0) == 'acceptance'):
        #get the data & save the report
        report = request.vars['report']
        report = db.report(db.report.id == report)
        # Validate DB report_restriction to obey TIMING rules
        valid_rep_restr = val_rep_restr(report.report_restriction.id)
        # Validate assignation belongs to this user
        assign = db.user_project((db.user_project.id == report.assignation)&
                                (db.user_project.assigned_user == auth.user.id))
        valid_assignation = assign != None
        if not(report and valid_assignation and valid_rep_restr):
            session.flash = T('Invalid selected assignation and report. Select a valid one.')
            redirect(URL('student','index'))
        import datetime
        current_date = datetime.datetime.now()
        report.update_record(created = current_date,
                      status = db.report_status(name = 'Grading'))
        session.flash = T('Report sent to Grading.')
        redirect(URL('student','index'))
    elif (request.args(0) == 'view'):
        #Get the report id
        report = request.vars['report']
        # Validate that the report belongs to user
        report = db.report(db.report.id == report)
        if not(report):
            session.flash = T('Selected report can\'t be edited. Select a valid report.')
            redirect(URL('student'))
        valid_report_owner = val_rep_owner(report.id)
        if not(valid_report_owner):
            session.flash = T('Selected report can\'t be edited. Select a valid report.')
            redirect(URL('student'))
        #TODO: retrieve report data
        #TODO: Display report data as read_only
        return dict(state='view')
    else:
        redirect(URL('student', 'index'))
    return dict()

@auth.requires_login()
@auth.requires_membership('Student')
def log():
    if (request.args(0) == 'save'):
        # validate the user owns this report
        report = request.vars['report']
        report = db.report(db.report.id == report)
        valid_report = report != None
        if valid_report: valid_report = val_rep_owner(report.id)
        # validate report is editable
        if valid_report: valid_report = val_rep_restr(report.report_restriction)
        # validate we receive log-date, log-type, log-content
        log_type = request.vars['log-type']
        log_date = request.vars['log-date']
        log_content = request.vars['log-content']
        if valid_report: valid_report = (log_type and log_date and log_content)
        if valid_report:
            db.log_entry.insert(log_type = log_type,
                                entry_date = log_date,
                                description = log_content,
                                report = report.id)
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
        if valid_log: valid_log = val_rep_owner(log.report)
        # validate report is editable
        if valid_log: valid_log = val_rep_restr(log.report['report_restriction'])
        # validate we receive log-date, log-type, log-content
        log_type = request.vars['log-type']
        log_date = request.vars['log-date']
        log_content = request.vars['log-content']
        if valid_log: valid_log = (log_type and log_date and log_content)
        if valid_log:
            log.update_record(log_type = log_type,
                              entry_date = log_date,
                              description = log_content)
            session.flash = T('Log Aupdated')
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
        if valid_log: valid_log = val_rep_owner(log.report)
        # validate report is editable
        if valid_log: valid_log = val_rep_restr(log.report['report_restriction'])
        if valid_log:
            log.delete_record()
            session.flash = T('Log Deleted')
            redirect(URL('student', 'report/edit', vars=dict(report=log.report)))
        else:
            session.flash = T('Operation not allowed.')
            redirect(URL('student', 'index'))
    return dict()

@auth.requires_login()
@auth.requires_membership('Student')
def project_items():
    import datetime
    cdate = datetime.datetime.now()
    user_project = request.vars['assignation']
    create_current, c_enab_date, creport = False, False, False

    project = db((db.user_project.id==user_project)&
                (db.project.id==db.user_project.project)).select(db.project.ALL).first()

    c_enab_date = db((db.enabled_date.start_date <= cdate)&
             (db.enabled_date.end_date >= cdate)).select().first()

    if c_enab_date:
        creport = db((db.report_head.repor_user==auth.user.id)&
              (db.report_head.enabled_date == c_enab_date.id)&
              (db.report_head.project == project.id)).select(db.report_head.ALL)
        if len(creport) == 0 and c_enab_date:
          create_current = True
          usr_reports = db((db.report_head.repor_user==auth.user.id)&
                 (db.report_head.enabled_date != c_enab_date.id)&
                 (db.report_head.project == project.id)).select()
        else:
          usr_reports = db((db.report_head.repor_user==auth.user.id)&
                 (db.report_head.project == project.id)).select()
    else:
        usr_reports = db((db.report_head.repor_user==auth.user.id)&
                 (db.report_head.project == project.id)).select()
    return locals()

@auth.requires_login()
@auth.requires_membership('Student')
def report_detail():
    import datetime
    report = request.vars['report']
    cdate = datetime.datetime.now()
    creport_head, report_head, c_enab_date, project, go_create = False, False\
                                                        ,False, False, False
    user_project = request.vars['assignation']
    project = db((db.user_project.id==user_project)&
                (db.project.id==db.user_project.project)).select(db.project.ALL).first()
    c_enab_date = db((db.enabled_date.start_date <= cdate)&
             (db.enabled_date.end_date >= cdate)).select().first()

    if c_enab_date and project:
        creport_head = db((db.report_head.repor_user==auth.user.id)&
              (db.report_head.enabled_date == c_enab_date.id)&
              (db.report_head.project == project.id)).select(db.report_head.ALL)
        if not creport_head:
            report_head = db.report_head.insert(created=cdate, project=project.id,
                     repor_user=auth.user.id, enabled_date=c_enab_date.id)
            db.commit()
            go_create = True
    return locals()

def get_report_head(user_project):
    import datetime
    cdate = datetime.datetime.now()
    creport_head, report_head, c_enab_date, project, go_create = False, False\
                                                        ,False, False, False
    user_project = user_project
    project = db((db.user_project.id==user_project)&
                (db.project.id==db.user_project.project)).select(db.project.ALL).first()
    if project:
        c_enab_date = db((db.enabled_date.start_date <= cdate)&
                 (db.enabled_date.end_date >= cdate)).select().first()

    if c_enab_date and project:
        creport_head = db((db.report_head.repor_user==auth.user.id)&
              (db.report_head.enabled_date == c_enab_date.id)&
              (db.report_head.project == project.id)).select(db.report_head.ALL).first()

    return creport_head, c_enab_date

@auth.requires_login()
@auth.requires_membership('Student')
def logs_list():
    report = False
    report = request.vars['report']
    user_project = request.vars['assignation']
    creport_head, c_enab_date = get_report_head(user_project)
    entries = []
    if creport_head:
        entries = db((db.log_entry.entry_user==auth.user.id)&
        (db.log_entry.head==creport_head.id)).select()
    elif report:
        entries = db((db.log_entry.entry_user==auth.user.id)&
        (db.log_entry.head==report)).select()
    entries_size = len(entries)
    return locals()

@auth.requires_login()
@auth.requires_membership('Student')
def logs_area():
    log_types = db(db.log_type).select()
    log_count = len(log_types)
    user_project = request.vars['assignation']
    form = FORM(
              T('Entry Date:'),
              INPUT(_name="event_date", _type="text", _id="my_calendar",
               requires=IS_NOT_EMPTY()),
              T('Type:'),
              SELECT(_name="type_select", *[OPTION(log_types[i].name,
                                  _value=str(log_types[i].id))
                                  for i in range(log_count)]),
              T('Description:'),
              TEXTAREA(_label=T('Description'), _name="description",
                   requires=IS_NOT_EMPTY()),

              INPUT(_type='submit', _value=T('Save activity')))
    if form.process().accepted:
        date = request.vars['event_date']
        log_type = request.vars['type_select']
        description = request.vars['description']
        user_project = request.vars['assignation']
        creport_head, c_enab_date = get_report_head(user_project)

        if creport_head and c_enab_date:
            db.log_entry.insert(entry_date=date, log_type=log_type,
                    description=description, entry_user=auth.user.id,
                    project = 1, head=creport_head)
            session.flash = T('Log Inserted')
        else:
            if creport_head:
                session.flash = T('Activity Logs creation not longer available')
                redirect(URL('student', 'courses'))
            elif c_enab_date:
                session.flash = T('No report set created')
                redirect(URL('logs_list', vars=dict(date=c_enab_date.id, assignation=user_project)))
            else:
                session.flash = T('Activity Logs creation not longer available,\
                                and no report set created')
                redirect(URL('student', 'courses'))
        redirect(URL('logs_list', vars=dict(date=c_enab_date.id, assignation=user_project)))

    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill the form'
    return locals()

@auth.requires_login()
@auth.requires_membership('Student')
def courses():
    year_period = request.vars['year_period']
    max_display = 1
    currentyear_period = db.period_year(db.period_year.id == year_period)
    if not currentyear_period:
        currentyear_period = current_year_period()
    current_data = db((db.user_project.period <= currentyear_period.id)&
              ((db.user_project.period + db.user_project.periods) > currentyear_period.id)&
              (db.user_project.assigned_user == auth.user.id)).select()
    current_period_name = T(second_period_name)
    if currentyear_period.period == first_period.id:
        current_period_name = T(first_period_name)
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


def current_year_period():
    #this should be a module's method
    import datetime
    cdate = datetime.datetime.now()
    cyear = cdate.year
    cmonth = cdate.month
    period = second_period
    #current period depends if we are in dates between jan-jun and jul-dec
    if cmonth < 7 :
        period = first_period
    return db.period_year((db.period_year.yearp == cyear)&
                          (db.period_year.period == period))
    assignations = db((db.user_project.assigned_user == auth.user.id)&
                      (db.user_project.assigned_user == db.auth_user.id)&
                      (db.user_project.project == db.project.id)&
                      (db.project.area_level == db.area_level.id)&
                      (db.user_project.period == db.period_year.id)).select()
    return dict(assignations = assignations)

def report_list():
    assignation = request.vars['assignation']
    #TODO: security statement goes here
    if not assignation: redirect(URL('index'))
    final_practice = db((db.user_project.id == assignation)&
                        (db.user_project.assigned_user == db.auth_user.id)&
                        (db.user_project.project == db.project.id)&
                        (db.project.area_level == db.area_level.id)&
                        (db.user_project.period == db.period_year.id)).select()
    if not final_practice: redirect(URL('index'))
    final_practice = final_practice.first()
    available_periods = db((db.period_year.id >= final_practice.user_project.period)&
                           (db.period_year.id < (final_practice.user_project.period + final_practice.user_project.periods))).select()
    return dict(final_practice = final_practice,
                available_periods = available_periods)
