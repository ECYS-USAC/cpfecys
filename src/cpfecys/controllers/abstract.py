# coding: utf8
# intente algo como
import string, random
def index(): return dict(message="hello from abstract.py")

def user_active():
    uid = request.vars['uid']
    carnet = None
    nombre = None
    if uid is None:
        success = False
    else:
        success = True
        carnet = db2(db2.user_user.id == uid).select().first().username
        usuario = db(db.auth_user.username == carnet).select().first()
        token = usuario.uv_token = ''.join(random.choice(string.ascii_uppercase\
                                    + string.ascii_lowercase + string.digits)\
                                    for x in range(63))
        usuario.update_record()
        if usuario is None:
            success = False
        else:
            nombre = usuario.first_name

    return dict(success=success, carnet = carnet, name = nombre, token=usuario.uv_token)
