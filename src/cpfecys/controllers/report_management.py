@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def student_management():
    #Todos los periodos registrados en el sistema
    def obtenerSemestres():
        return db(db.period_year).select()

    #Obtener el total de accionnes realizadas por tipo del nivel 1
    def obtenerTotalNivel(tipo, periodo):
        total=0
        count = db.academic_log.id.count()
        if tipo=='i':
            acciones = db((db.academic_log.id_period == periodo) & (db.academic_log.operation_log=='insert')).select(count).first()
            total=acciones[count]
        elif tipo=='u':
            acciones = db((db.academic_log.id_period == periodo) & (db.academic_log.operation_log=='update')).select(count).first()
            total=acciones[count]
        elif tipo=='d':
            acciones = db((db.academic_log.id_period == periodo) & (db.academic_log.operation_log=='delete')).select(count).first()
            total=acciones[count]
        return total
    return dict(obtenerSemestres=obtenerSemestres, obtenerTotalNivel=obtenerTotalNivel)



def student_management_n2():
    operaciones = []
    tipo1=''
    periodo=None
    if request.vars['semestre'] != None and request.vars['tipo']!=None:
        periodo=request.vars['semestre']
        tipo=request.vars['tipo']
        count = db.academic_log.id.count()
        varRoles = db(db.auth_group).select()
        for rol in varRoles:
            u = []
            u.append(rol.id)
            u.append(rol.role)
            if tipo=='all':
                acciones = db((db.academic_log.id_period == periodo) & (db.academic_log.operation_log=='insert')&(db.academic_log.roll.like('%'+rol.role+'%'))).select(count).first()
                u.append(acciones[count])
                acciones = db((db.academic_log.id_period == periodo) & (db.academic_log.operation_log=='update')&(db.academic_log.roll.like('%'+rol.role+'%'))).select(count).first()
                u.append(acciones[count])
                acciones = db((db.academic_log.id_period == periodo) & (db.academic_log.operation_log=='delete')&(db.academic_log.roll.like('%'+rol.role+'%'))).select(count).first()
                u.append(acciones[count])
                operaciones.append(u)
                tipo1='all'
            elif tipo=='i':
                acciones = db((db.academic_log.id_period == periodo) & (db.academic_log.operation_log=='insert')&(db.academic_log.roll.like('%'+rol.role+'%'))).select(count).first()
                u.append(acciones[count])
                operaciones.append(u)
                tipo1='i'
            elif tipo=='u':
                acciones = db((db.academic_log.id_period == periodo) & (db.academic_log.operation_log=='update')&(db.academic_log.roll.like('%'+rol.role+'%'))).select(count).first()
                u.append(acciones[count])
                operaciones.append(u)
                tipo1='u'
            elif tipo=='d':
                acciones = db((db.academic_log.id_period == periodo) & (db.academic_log.operation_log=='delete')&(db.academic_log.roll.like('%'+rol.role+'%'))).select(count).first()
                u.append(acciones[count])
                operaciones.append(u)
                tipo1='d'
    return dict(operaciones=operaciones, tipo1=tipo1, periodo=periodo)



def student_management_n3():
    operaciones = []
    tipo1=''
    periodo=None
    rol=None
    if request.vars['semestre'] != None and request.vars['tipo']!=None  and request.vars['rol']!=None:
        periodo=request.vars['semestre']
        tipo=request.vars['tipo']
        count = db.academic_log.id.count()
        #usuarios = db(db.auth_user.id.belongs(usuarioRol)).select(db.auth_user.username)
        rol = db(db.auth_group.id==request.vars['rol']).select().first()
        #session.flash=str(rol)
        #redirect(URL('default','index'))

        u = []
        if tipo=='all':
            acciones = db((db.academic_log.id_period == periodo) & (db.academic_log.roll.like('%'+rol.role+'%'))).select(groupby=db.academic_log.user_name)
            for accion in acciones:
                usuario = db(db.auth_user.username==accion.user_name).select().first()
                if usuario != None:
                    u=[]
                    u.append(usuario.id)
                    u.append(usuario.username)
                    acciones = db((db.academic_log.id_period == periodo) & (db.academic_log.operation_log=='insert')&(db.academic_log.roll.like('%'+rol.role+'%')) & (db.academic_log.user_name==usuario.username)).select(count).first()
                    u.append(acciones[count])
                    acciones = db((db.academic_log.id_period == periodo) & (db.academic_log.operation_log=='update')&(db.academic_log.roll.like('%'+rol.role+'%')) & (db.academic_log.user_name==usuario.username)).select(count).first()
                    u.append(acciones[count])
                    acciones = db((db.academic_log.id_period == periodo) & (db.academic_log.operation_log=='delete')&(db.academic_log.roll.like('%'+rol.role+'%')) & (db.academic_log.user_name==usuario.username)).select(count).first()
                    u.append(acciones[count])
                    operaciones.append(u)
            tipo1='all'
        elif tipo=='i':
            acciones = db((db.academic_log.id_period == periodo) & (db.academic_log.operation_log=='insert') & (db.academic_log.roll.like('%'+rol.role+'%'))).select(groupby=db.academic_log.user_name)
            for accion in acciones:
                usuario = db(db.auth_user.username==accion.user_name).select().first()
                if usuario != None:
                    u=[]
                    u.append(usuario.id)
                    u.append(usuario.username)
                    acciones = db((db.academic_log.id_period == periodo) & (db.academic_log.operation_log=='insert')&(db.academic_log.roll.like('%'+rol.role+'%')) & (db.academic_log.user_name==usuario.username)).select(count).first()
                    u.append(acciones[count])
                    operaciones.append(u)
            tipo1='i'
        elif tipo=='u':
            acciones = db((db.academic_log.id_period == periodo) & (db.academic_log.operation_log=='update') & (db.academic_log.roll.like('%'+rol.role+'%'))).select(groupby=db.academic_log.user_name)
            for accion in acciones:
                usuario = db(db.auth_user.username==accion.user_name).select().first()
                if usuario != None:
                    u=[]
                    u.append(usuario.id)
                    u.append(usuario.username)
                    acciones = db((db.academic_log.id_period == periodo) & (db.academic_log.operation_log=='update')&(db.academic_log.roll.like('%'+rol.role+'%')) & (db.academic_log.user_name==usuario.username)).select(count).first()
                    u.append(acciones[count])
                    operaciones.append(u)
            tipo1='u'
        elif tipo=='d':
            acciones = db((db.academic_log.id_period == periodo) & (db.academic_log.operation_log=='delete') & (db.academic_log.roll.like('%'+rol.role+'%'))).select(groupby=db.academic_log.user_name)
            for accion in acciones:
                usuario = db(db.auth_user.username==accion.user_name).select().first()
                if usuario != None:
                    u=[]
                    u.append(usuario.id)
                    u.append(usuario.username)
                    acciones = db((db.academic_log.id_period == periodo) & (db.academic_log.operation_log=='delete')&(db.academic_log.roll.like('%'+rol.role+'%')) & (db.academic_log.user_name==usuario.username)).select(count).first()
                    u.append(acciones[count])
                    operaciones.append(u)
            tipo1='d'
    return dict(operaciones=operaciones, tipo1=tipo1, periodo=periodo, rol=rol.id)



def student_management_n4():
    periodo=None
    rol=None
    user = None
    operaciones = None
    if request.vars['semestre'] != None and request.vars['tipo']!=None  and request.vars['rol']!=None and request.vars['user']!=None:
        if request.vars['consulta'] != None:
            None
        else:
            periodo=request.vars['semestre']
            tipo=request.vars['tipo']
            rol = db(db.auth_group.id==request.vars['rol']).select().first()
            user = db(db.auth_user.id==request.vars['user']).select().first()
            if tipo=='all':
                tipo='all'
                operaciones = db((db.academic_log.id_period == periodo) & (db.academic_log.roll.like('%'+rol.role+'%')) & (db.academic_log.user_name==user.username)).select()
            elif tipo=='i':
                tipo='i'
                operaciones = db((db.academic_log.id_period == periodo) & (db.academic_log.operation_log=='insert') & (db.academic_log.roll.like('%'+rol.role+'%')) & (db.academic_log.user_name==user.username)).select()
            elif tipo=='u':
                tipo='u'
                operaciones = db((db.academic_log.id_period == periodo) & (db.academic_log.operation_log=='update') & (db.academic_log.roll.like('%'+rol.role+'%')) & (db.academic_log.user_name==user.username)).select()
            elif tipo=='d':
                tipo='d'
                operaciones = db((db.academic_log.id_period == periodo) & (db.academic_log.operation_log=='delete') & (db.academic_log.roll.like('%'+rol.role+'%')) & (db.academic_log.user_name==user.username)).select()

    def obtenerSemestre(id):
        return db(db.period_year.id==id).select().first()
    return dict(operaciones=operaciones, obtenerSemestre=obtenerSemestre, periodo=periodo, tipo=tipo, rol=rol.id, user=user.id)