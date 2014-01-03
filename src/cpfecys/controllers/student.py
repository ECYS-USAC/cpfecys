# coding: utf8
# intente algo como
@auth.requires_login()
@auth.requires_membership('Student')
def index():
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
