# coding: utf8
# intente algo como
@auth.requires_login()
def projects():
    grid = SQLFORM.grid(db.project)
    return locals()

@auth.requires_login()
def user_project():
    grid = SQLFORM.grid(db.user_project)
    return locals()
