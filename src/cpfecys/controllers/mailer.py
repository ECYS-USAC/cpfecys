# coding: utf8
# intente algo como
@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def index():
    grid = SQLFORM.smartgrid(db.mailer_log)
    return dict(grid = grid)
