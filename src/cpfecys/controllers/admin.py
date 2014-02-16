# coding: utf8
# intente algo como
@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def periods():
    grid = SQLFORM.grid(db.period_year)
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
def reports():
    response.view = 'admin/report_list.html'
    period_year = db(db.period_year).select()
    report_status = db(db.report_status).select()

    count = db.report.id.count()
    report_total = db().select(
        db.report_status.ALL, count, 
        left=db.report.on(db.report.status==db.report_status.id), 
        groupby=db.report_status.name)
    return dict(period_year=period_year, report_status=report_status, 
        report_total=report_total)
                

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def reports_view():
    status = request.vars['status']
    period = request.vars['period']
    grid = SQLFORM.grid((db.report.period==period)&(db.report.status==status))
    return dict(grid=grid)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def links():
    user = db(db.auth_membership.user_id == auth.user.id).select(db.auth_group.ALL)
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
    user = db(db.auth_membership.user_id == auth.user.id).select(db.auth_group.ALL)
    grid = SQLFORM.smartgrid(db.uploaded_file, linked_tables=['file_access'])
    return locals()

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def notifications_manager():
    user = db(db.auth_membership.user_id == auth.user.id).select(db.auth_group.ALL)
    grid = SQLFORM.smartgrid(db.front_notification, linked_tables=['notification_access'])
    return locals()

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def items_manager():
    if request.function == 'new':
        db.item.created.writable=db.item.created.readable=False
    grid = SQLFORM.smartgrid(db.item_restriction, linked_tables=['item_restriction_area', 'item_restriction_exception'])
    return dict(grid=grid)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def manage_items():
    return dict()

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
                        row.append(T('Error: ') + T('User is not valid. User doesn\'t exist in UV.'))
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
                    assignation = db.user_project((db.user_project.assigned_user == usr.id)&
                                                  (db.user_project.project == project)&
                                                  (db.user_project.period == current_period))
                    if assignation != None:
                        row.append(T('Warning: ') + T('User was already assigned, Updating Data.'))
                        warning_users.append(row)
                        assignation.update_record(periods = rassignation_length, pro_bono = rpro_bono)
                        continue
                if project != None:
                    db.user_project.insert(assigned_user = usr,
                                            project = project,
                                            period = current_period,
                                            periods = rassignation_length,
                                            pro_bono = rpro_bono)
                else:
                    # project_id is not valid
                    row.append('Error: ' + T('Project code is not valid. Check please.'))
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

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def assignation():
    #requires parameter year_period if no one is provided then it is automatically detected
    #and shows the current period
    year_period = request.vars['year_period']
    max_display = 1
    import cpfecys
    currentyear_period = db.period_year(db.period_year.id == year_period)
    if not currentyear_period:
        currentyear_period = cpfecys.current_year_period()
        changid = currentyear_period.id
    grid = SQLFORM.grid((db.user_project.period <= currentyear_period.id)&
              ((db.user_project.period + db.user_project.periods) > currentyear_period.id))
    current_period_name = T(cpfecys.second_period.name)
    if currentyear_period.period == cpfecys.first_period.id:
        current_period_name = T(cpfecys.first_period.name)
    start_index = currentyear_period.id - max_display - 1
    if start_index < 1:
        start_index = 0
    end_index = currentyear_period.id + max_display
    periods_before = db(db.period_year).select(limitby=(start_index, currentyear_period.id - 1))
    periods_after = db(db.period_year).select(limitby=(currentyear_period.id, end_index))
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
    grid = SQLFORM.smartgrid(db.auth_user)
    return dict(grid = grid)
