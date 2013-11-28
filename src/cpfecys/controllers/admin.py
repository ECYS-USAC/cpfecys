# coding: utf8
# intente algo como
@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def periods():
    grid = SQLFORM.grid(db.period_year)
    return locals()

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def projects():
    grid = SQLFORM.grid(db.project)
    return locals()

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def links():
    grid = SQLFORM.grid(db.link)
    return locals()

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def areas():
    grid = SQLFORM.grid(db.area_level)
    return locals()

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def upload_file():
    grid = SQLFORM.grid(db.uploaded_file)
    return locals()

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def assignation():
    import csv
    import datetime
    cdate = datetime.datetime.now()
    cyear = cdate.year
    newUsrs, errUsrs, existUsers = {}, {}, {}
    exisIndex, UsrIndx, errIndx = 0, 0 ,0
    success = False
    periods, periodname = getPeriods()
    if request.vars.csvfile != None:
        file = request.vars.csvfile.file
        cr = csv.reader(file, delimiter=',', quotechar='|')
        success = True
        header = next(cr)
        for row in cr:
            project, currentUser = None, None
            currentUser = db(db.auth_user.username==row[1]).select().first()
            project = db(db.project.id==row[10]).select().first()
            if currentUser is None:
                phone, first_name, username = '', '', ''
                phone = row[3]
                email = row[4]
                cycles = row[9]
                pro_bono = row[8]
                username = row[1]
                first_name = row[2]
                currentUser = db.auth_user.insert(username=username, \
                                                   first_name=first_name, \
                                                   email=email, pro_bono=pro_bono,\
                                                   phone=phone)
            if project:
                    periodcurrent = db.period(db.period.name == periodname)
                    period_year = db.period_year((db.period_year.yearp == cyear)&
                                 (db.period_year.period == periodcurrent))
                    db.user_project.insert(student=currentUser, project=project, period=period_year)
                    existUsers[exisIndex] = currentUser.first_name + ' - ' + project.name
                    exisIndex = exisIndex + 1

        response.flash = T('Data uploaded')
        return dict(success = success,
                    data = newUsrs,
                    errors = errUsrs,
                    existUsers = existUsers,
                    periods = periods)
    else:
        return dict(success = False,
                    file = False,
                    periods = periods)
    return locals()

def getPeriods():
    #need the period_year id that belongs the current year and period
    import datetime
    cdate = datetime.datetime.now()
    cyear = cdate.year
    cyear_before = cdate.year
    cyear_before2 = cdate.year
    cmonth = cdate.month
    periodname = second_period_name
    #current period depends if we are in dates between jan-jun and jul-dec
    if cmonth < 7 :
        periodname = first_period_name
        period_before_name = second_period_name
        period_before2_name = first_period_name
        cyear_before = cyear - 1
        cyear_before2 = cyear - 1
    else:
        period_before_name = first_period_name
        period_before2_name = second_period_name
        cyear_before = cyear
        cyear_before2 = cyear - 1

    periodcurrent = db.period(db.period.name == periodname)
    period_year = db.period_year((db.period_year.yearp == cyear)&
                                 (db.period_year.period == periodcurrent))
    grid_current_period = SQLFORM.grid((db.user_project.period == period_year))

    periodcurrent = db.period(db.period.name == period_before_name)
    period_year = db.period_year((db.period_year.yearp == cyear_before)&
                                 (db.period_year.period == periodcurrent))
    grid_before_period = SQLFORM.grid((db.user_project.period == period_year))

    periodcurrent = db.period(db.period.name == period_before2_name)
    period_year = db.period_year((db.period_year.yearp == cyear_before2)&
                                 (db.period_year.period == periodcurrent))
    grid_before2_period = SQLFORM.grid((db.user_project.period == period_year))
    periods = []
    name = T(period_before2_name) + '-' + str(cyear_before2)
    a = {}
    a['grid'] = grid_before2_period
    a['name'] = name
    periods.append(a)
    name = T(period_before_name) + '-' + str(cyear_before)
    a = {}
    a['grid'] = grid_before_period
    a['name'] = name
    periods.append(a)
    name = T(periodname) + '-' + str(cyear)
    a = {}
    a['grid'] = grid_current_period
    a['name'] = name
    periods.append(a)
    return periods, periodname

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def users():
    grid = SQLFORM.grid(db.auth_membership)
    return dict(grid = grid)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def add_student():
    #get the username
    #other data is fetched from db2
    #if that data exists then the user is created here
    #teacher role is assigned
    return dict()

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def add_teacher():
    #get the username
    #other data is fetched from db2
    #if that data exists then the user is created here
    #teacher role is assigned
    return dict()

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def add_administrator():
    #get the username
    #administrator role is assigned
    return dict()
