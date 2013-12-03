# coding: utf8
# intente algo como
@auth.requires_login()
@auth.requires_membership('Teacher')
def index():
    return dict()
