# coding: utf8
# intente algo como
def index(): return dict(message="hello from abstract.py")

def user_active():
    uid = request.vars['uid']
    carnet = None
    if uid is None:
        success = False
    else:
        #success = True
        carnet = db2(db2.user_user.id ==uid).select().first().username
        cpfCarnet = db(db.auth_user.carnet == carnet).select().first().carnet()
        
    return dict(success=success, carnet = carnet)
