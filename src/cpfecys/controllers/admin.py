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
    grid = SQLFORM.grid(db.project_area)
    return locals()

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def user_area():
    grid = SQLFORM.grid(db.user_area.student != auth.user.id)
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
