# coding: utf8
# intente algo como
import string, random
def index():
    #import datetime
    #tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    #tomorrow = datetime.datetime(tomorrow.year, tomorrow.month, tomorrow.day)
    #print tomorrow
    #print request.now
    #scheduler.queue_task(auto_daily,start_time=request.now)
    return dict(message="hello from abstract.py")

def oauth_login():
    token = request.vars['token']
    if not (token):
        #no token provided
        session.flash = T('No token was provided.')
        redirect(URL('cpfecys','default','user/login'))
    user = db(db.auth_user.uv_token==token).select()
    if not user:
        #bad token
        session.flash = T('The provided token is not valid.')
        redirect(URL('cpfecys','default','user/login'))
    auth.login_user(user.first())
    #sucessfull login :D
    redirect(URL('cpfecys', 'default', 'index'))
    return dict()

def user_active():
    uid = request.vars['uid']
    #carnet = None
    #nombre = None
    if uid is None:
        success = False
    else:
        success = True
        chamilo_user = db2.user_user(uid)
        if not chamilo_user:
            success = False
        usuario = db(db.auth_user.username == chamilo_user.username).select()
        #token = usuario.uv_token = ''.join(random.choice(string.ascii_uppercase\
        #                            + string.ascii_lowercase + string.digits)\
        #                            for x in range(63))
        #usuario.update_record()
        if usuario is None:
            success = False
        elif not (usuario.first()):
            success = False
        #else:
        #    nombre = usuario.first_name
    return dict(success=success)
