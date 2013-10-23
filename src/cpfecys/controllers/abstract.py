# coding: utf8
# intente algo como
def index(): return dict(message="hello from abstract.py")

def user_active():
    uid = request.vars['uid']
    if uid is None:
        success = False
    else:
        success = True
    return dict(success=success)
