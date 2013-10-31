# coding: utf8
# listing all projects
@auth.requires_login()
def index():
    grid = SQLFORM.grid(db.project)
    return locals()

#def create():
    #form = SQLFORM(db.project).process(next=URL('index'))
    #return dict(form = form)
