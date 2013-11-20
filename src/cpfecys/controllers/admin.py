# coding: utf8
# intente algo como
@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def projects():
    grid = SQLFORM.grid(db.project)
    return locals()

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def areas():
    grid = SQLFORM.grid(db.area_level)
    return locals()

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def assignation():
    import csv
    newUsrs = {}
    errUsrs = {}
    existUsers ={}
    exisIndex = 0
    UsrIndx = 0
    errIndx = 0
    success = False
    grid = SQLFORM.grid(db.user_project.student != auth.user.id)
    if request.vars.csvfile:
        cr = csv.reader(file, delimiter=',', quotechar='|')
        success = True
        header = next(cr)
        for row in cr:
            user = None
            user = db2(db2.user_user.username==row[1]).select().first()
            if not user:
                errUsrs[errIndx] = row[1]
                errIndx = errIndx + 1
            else:
                currentUser = None
                currentUser = db(db.auth_user.username==user.username).select().first()
                if not currentUser:
                    phone = ''
                    area = None
                    first_name = ''
                    first_name = row[2]
                    phone = row[3]
                    email = row[4]
                    areacode = row[10]
                    pro_bono = row[8]
                    cycles = row[9]
                    project = db(db.project.id==row[10]).select().first()

                    if project:
                        tempUser = db.auth_user.insert(username=user.username, \
                        first_name=first_name, email=email, pro_bono=pro_bono, \
                        phone=phone)
                        db.user_project.insert(student=tempUser, project=project)

                    newUsrs[UsrIndx] = first_name + ' :' + project.name
                    UsrIndx = UsrIndx + 1
                else:
                    existUsers[exisIndex] = row[1]
                    exisIndex = exisIndex + 1

        response.flash = T('Data uploaded')
        return dict(grid = grid,
                    success = success,
                    data = newUsrs,
                    errors = errUsrs,
                    existUsers = existUsers)
    else:
        return dict(grid = grid,
                    success = False,
                    file = False)
    return locals()

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
