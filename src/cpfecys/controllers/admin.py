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

def tabs_test():
    # if no parameter is specified returns the current period_year
    # and the two before it
    # if a parameter is specified returns the specified period_year
    # and the two before it
    return dict()

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def assignation():
    year_period = request.vars['year_period']
    if year_period:
        yp = db.period_year(db.period_year.id == year_period)
        cyear = yp.yearp
        periodcurrent = db.period(db.period.id == yp.period)
    else:
        cyear, periodcurrent = current_year_period()
    import csv
    newUsrs, errUsrs, existUsers = {}, {}, {}
    exisIndex, UsrIndx, errIndx = 0, 0 ,0
    success = False
    periods = getPeriods(cyear = cyear, period = periodcurrent)
    periods_years = db(db.period_year).select()
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
                    periods = periods,
                    periods_years = periods_years)
    return dict(success = False,
                file = False,
                periods = periods,
                periods_years = periods_years)

def current_year_period():
    import datetime
    cdate = datetime.datetime.now()
    cyear = cdate.year
    cmonth = cdate.month
    period = second_period
    #current period depends if we are in dates between jan-jun and jul-dec
    if cmonth < 7 :
        period = first_period
    return cyear, period

def getPeriods(cyear = None, period = None, periods_ammount = 3):
    #if cyear and period not provided provide the current ones
    if (not cyear) or (not period):
        cyear, period = current_year_period()
    #need the period_year id that belongs the current year and period
    is_first_period = (first_period == period)
    periods = []
    for x in range(0, periods_ammount):
        a = {}
        #get the current period
        if is_first_period:
            a['grid'] = SQLFORM.grid((db.user_project.period == first_period))
            a['name'] = str(cyear) + '-' + T(first_period_name)
            #if the period_name is the first period change year-1
            cyear = cyear - 1
        else:
            a['grid'] = SQLFORM.grid((db.user_project.period == second_period))
            a['name'] = str(cyear) + '-' + T(second_period_name)
        periods.insert(0, a)
        #alternate the current period
        is_first_period = not is_first_period
    return periods

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
