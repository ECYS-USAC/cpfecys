# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################
@auth.requires_login()
@auth.requires(auth.has_membership('Student') or auth.has_membership('Teacher'))
def academic_assignation():
    #requires parameter year_period if no one is provided then it is 
    #automatically detected
    #and shows the current period
    assignation = request.vars['assignation']
    year_period = request.vars['year_period']
    max_display = 1
    import cpfecys
    currentyear_period = db.period_year(db.period_year.id == year_period)
    check = db.user_project(id=assignation, assigned_user = auth.user.id)

    if not currentyear_period:
        currentyear_period = cpfecys.current_year_period()
        changid = currentyear_period.id
    if (check is None):
        #check if there is no assignation or if it is locked (shouldn't be touched)
        if (session.last_assignation is None):
            redirect(URL('default','index'))
            return
        else:
            check = db.user_project(id = session.last_assignation)
            if cpfecys.assignation_is_locked(check):
                redirect(URL('default','index'))
                return
    else:
        session.last_assignation = check.id
    cyearperiod = cpfecys.current_year_period()

    if request.vars['search_var'] is None:
        query = ((db.academic_course_assignation.semester == currentyear_period.id) & (db.academic_course_assignation.assignation==check.project))
    else:
        query2 = db((db.academic_course_assignation.carnet == db.academic.id) & (db.academic_course_assignation.semester == currentyear_period.id) & (db.academic_course_assignation.assignation==check.project) & (db.academic.carnet.like('%'+request.vars['search_var']+'%')) ).select()
        dest = []
        query = None
        for q in query2:
            dest.append(q.academic.id)
            #consultar a la base de datos para obtener a los usuarios a los que enviaremos
        query = (db.academic_course_assignation.carnet.belongs(dest) & (db.academic_course_assignation.semester == currentyear_period.id) & (db.academic_course_assignation.assignation==check.project))
        

    fields = (db.academic_course_assignation.carnet, db.academic_course_assignation.laboratorio)

    #db.academic.id.readable = False
    #db.academic.id.writable = False
    #db.academic.carnet.readable = False    
    #db.academic.carnet.writable = False
    #db.academic.email.writable = False
    #db.academic.email.readable = False


    db.academic_course_assignation.assignation.default = check.project
    db.academic_course_assignation.assignation.writable = False
    db.academic_course_assignation.assignation.readable = False
    db.academic_course_assignation.semester.default = currentyear_period.id
    db.academic_course_assignation.semester.writable = False
    db.academic_course_assignation.semester.readable = False

    if (currentyear_period.id == cpfecys.current_year_period().id):
        grid = SQLFORM.grid(query, fields=fields, oncreate=oncreate_academic_assignation, onupdate=onupdate_academic_assignation, ondelete=ondelete_academic_assignation,csv=False)
    else:
        checkProject = db((db.user_project.project == check.project) & (db.user_project.assigned_user==check.assigned_user) & (db.user_project.period==currentyear_period.id)).select()
        b=0
        for a in checkProject:
            b=b+1
        if b!=0:
            grid = SQLFORM.grid(query, fields=fields, deletable=False, editable=False, create=False,csv=False)
        else:
            session.flash  =T('Not authorized')
            redirect(URL('default','index'))

    current_period_name = T(cpfecys.second_period.name)
    if currentyear_period.period == cpfecys.first_period.id:
        current_period_name = T(cpfecys.first_period.name)
    start_index = currentyear_period.id - max_display - 1
    if start_index < 1:
        start_index = 0
    end_index = currentyear_period.id + max_display
    periods_before = db(db.period_year).select(limitby=(start_index,  \
        currentyear_period.id - 1))
    periods_after = db(db.period_year).select(limitby=(currentyear_period.id, \
     end_index))
    other_periods = db(db.period_year).select()
    return dict(grid = grid,
                currentyear_period = currentyear_period,
                current_period_name = current_period_name,
                periods_before = periods_before,
                periods_after = periods_after,
                other_periods = other_periods,
                name = check.project.name,
                assignation = check.id)

def oncreate_academic_assignation(form):
    import datetime
    import cpfecys

    cdate = datetime.datetime.now()
    assignation = request.vars['assignation']
    
    
    currentyear_period = cpfecys.current_year_period()

    check = db.user_project(id=assignation, assigned_user = auth.user.id)
    if (check is None):
        #check if there is no assignation or if it is locked (shouldn't be touched)
        if (session.last_assignation is None):
            redirect(URL('default','index'))
            return
        else:
            check = db.user_project(id = session.last_assignation)
            if cpfecys.assignation_is_locked(check):
                redirect(URL('default','index'))
                return
    else:
        session.last_assignation = check.id
    #Search for user roles
    result = db(db.auth_membership.user_id==auth.user.id).select()
    roll_var = ''
    i = 0;
    for a in result:
        if i == 0:
            roll_var = a.group_id.role
            i = i+1
        else:
           roll_var = roll_var + ',' + a.group_id.role

    
    student_var = db(db.academic.id == form.vars.carnet).select()
    carnet_var = ''
    for a in student_var:
        carnet_var = a.carnet

    #Check that there is not an assignation
    usr2 = db((db.academic_course_assignation.id != form.vars.id) & (db.academic_course_assignation.semester == currentyear_period.id) & (db.academic_course_assignation.assignation == check.project) & (db.academic_course_assignation.carnet == form.vars.carnet)).select()
    i = 0;
    for a in usr2:
        i = i+1

    if i == 0: 
        #If there is not an assignation update the log
        session.flash = T('Se realizó la asignación')
        db.academic_course_assignation_log.insert(user_name = auth.user.username, 
                                                roll =  roll_var, 
                                                operation_log = 'insert', 
                                                after_carnet = carnet_var, 
                                                after_course = check.project.name,
                                                after_year = str(currentyear_period.yearp) ,
                                                after_semester = str(currentyear_period.period),
                                                after_laboratory = form.vars.laboratorio,
                                                id_academic_course_assignation = form.vars.id,
                                                id_period = str(currentyear_period.id),
                                                description = 'Se creo el registro desde la pagina Asignar Estudiantes')
    else:
        #If there is an assignation delete the last record
        db(db.academic_course_assignation.id==form.vars.id).delete()
        session.flash = T('Error: Ya existe la asignacion')


def onupdate_academic_assignation(form):
    import datetime
    import cpfecys

    cdate = datetime.datetime.now()
    assignation = request.vars['assignation']
    
    
    currentyear_period = cpfecys.current_year_period()

    check = db.user_project(id=assignation, assigned_user = auth.user.id)
    if (check is None):
        #check if there is no assignation or if it is locked (shouldn't be touched)
        if (session.last_assignation is None):
            redirect(URL('default','index'))
            return
        else:
            check = db.user_project(id = session.last_assignation)
            if cpfecys.assignation_is_locked(check):
                redirect(URL('default','index'))
                return
    else:
        session.last_assignation = check.id

    #Search for user roles
    result = db(db.auth_membership.user_id==auth.user.id).select()
    roll_var = ''
    i = 0;
    for a in result:
        if i == 0:
            roll_var = a.group_id.role
            i = i+1
        else:
            roll_var = roll_var + ',' + a.group_id.role

    #Search for carnet
    student_var = db(db.academic.id == form.vars.carnet).select()
    carnet_var = ''
    for a in student_var:
        carnet_var = a.carnet

    #Search for before values
    student_var2 = db(db.academic_course_assignation_log.id_academic_course_assignation == form.vars.id).select(orderby=db.academic_course_assignation_log.id)
    bef_carnet_var = ''
    course_var = ''
    year_var = ''
    semester_var = ''
    laboratory_var = ''
    for a in student_var2:
        bef_carnet_var = a.after_carnet
        course_var = a.after_course
        year_var = a.after_year
        semester_var = a.after_semester
        laboratory_var = a.after_laboratory
    if form.vars.delete_this_record != None:
        db.academic_course_assignation_log.insert(user_name = auth.user.username, 
                                                roll =  roll_var, 
                                                operation_log = 'delete', 
                                                before_carnet = bef_carnet_var, 
                                                before_course = course_var,
                                                before_year = year_var,
                                                before_semester = semester_var,
                                                before_laboratory = laboratory_var,
                                                id_period = str(currentyear_period.id),
                                                description = 'Se elimino el registro desde la pagina Asignar Estudiantes')
    else:
        #Check that there is not an assignation
        usr2 = db((db.academic_course_assignation.id != form.vars.id) & (db.academic_course_assignation.semester == currentyear_period.id) & (db.academic_course_assignation.assignation == check.project) & (db.academic_course_assignation.carnet == form.vars.carnet)).select()
        i = 0;
        for a in usr2:
            i = i+1

        if i == 0: 
            #If there is not an assignation update the log
            session.flash = T('Se realizó la modificacion')
            db.academic_course_assignation_log.insert(user_name = auth.user.username, 
                                                roll =  roll_var, 
                                                operation_log = 'update', 
                                                before_carnet = bef_carnet_var, 
                                                before_course = course_var,
                                                before_year = year_var,
                                                before_semester = semester_var,
                                                before_laboratory = laboratory_var,
                                                after_carnet = carnet_var, 
                                                after_course = check.project.name,
                                                after_year = str(currentyear_period.yearp) ,
                                                after_semester = str(currentyear_period.period),
                                                after_laboratory = form.vars.laboratorio,
                                                id_academic_course_assignation = form.vars.id,
                                                id_period = str(currentyear_period.id),
                                                description = 'Se modifico el registro desde la pagina Asignar Estudiantes')
        else:
            #If there is an assignation delete the last record
            #db(db.academic_course_assignation.id==form.vars.id).delete()
            temp_academic = db(db.academic.carnet==bef_carnet_var).select()
            id_academic = ''
            for a in temp_academic:
                id_academic = a.id
            db(db.academic_course_assignation.id==form.vars.id).update(carnet=id_academic,laboratorio=laboratory_var)
            session.flash = T('Error: Ya existe la asignacion, no se modifico el estudiante')
        




def ondelete_academic_assignation(table_involved, id_of_the_deleted_record):
    import datetime
    cdate = datetime.datetime.now()
    student_assignation_var = db.academic_course_assignation(id_of_the_deleted_record)  
    import cpfecys  
    currentyear_period = cpfecys.current_year_period()

    #Search for user roles
    result = db(db.auth_membership.user_id==auth.user.id).select()
    roll_var = ''
    i = 0;
    for a in result:
        if i == 0:
            roll_var = a.group_id.role
            i = i+1
        else:
            roll_var = roll_var + ',' + a.group_id.role

    project_name_var = ''
    project_var = db(db.project.id == student_assignation_var.assignation).select()
    for a in project_var:
        project_name_var = a.name

    db.academic_course_assignation_log.insert(user_name = auth.user.username, 
                                                roll =  roll_var, 
                                                operation_log = 'delete', 
                                                before_carnet = student_assignation_var.carnet.carnet, 
                                                before_course = student_assignation_var.assignation.name,
                                                before_year = str(student_assignation_var.semester.yearp) ,
                                                before_semester = str(student_assignation_var.semester.period),
                                                before_laboratory = student_assignation_var.laboratorio,
                                                id_period = str(currentyear_period.id),
                                                description = 'Se elimino el registro desde la pagina Asignar Estudiantes')


@auth.requires_login()
@auth.requires(auth.has_membership('Student') or auth.has_membership('Teacher'))
def periods():
    grid = SQLFORM.grid(db.period_year)
    return locals()

@auth.requires_login()
@auth.requires(auth.has_membership('Student') or auth.has_membership('Teacher'))
def academic_assignation_upload():
    def files():
        f = db(db.uploaded_file.name=='CargaEstudiantes_TutoresAcademicos').select()
        nameP = ''
        for p2 in f:
            nameP=p2.file_data
        return nameP
        return dict(nameP=nameP)

    assignation = request.vars['assignation']
    check = db.user_project(id=assignation, assigned_user = auth.user.id)
    name = check.project.name
    import csv
    error_users = []
    aviso_users = []
    success = False
    import cpfecys
    import datetime
    cdate = datetime.datetime.now()
    current_period = cpfecys.current_year_period()
    if request.vars.csvfile != None:
        try:
            file = request.vars.csvfile.file
        except AttributeError:
            response.flash = T('Please upload a file.')
            return dict(success = False,
                file = False,
                periods = periods,
                current_period = current_period,
                name=name, files=files)
        try:
            cr = csv.reader(file, delimiter=',', quotechar='"')
            success = True
            header = next(cr)
            for row in cr:
                ## parameters
                rcarnet = row[0]
                remail = row[1]
                rlaboratorio = row[2]
                ## check if user exists                
                check = db.user_project(id =assignation, assigned_user = auth.user.id)                      
                usr = db.academic(db.academic.carnet == rcarnet)        
                if usr is None:
                    #Email validation        
                    if rcarnet == '':
                        row.append(T('Error: ') + T('El carnet es un campo obligatorio.'))
                        error_users.append(row)
                    else:            
                        if IS_EMAIL()(remail)[1]:
                            row.append(T('Error: ') + T('El correo ingresado no es correcto.'))
                            error_users.append(row)
                        else:
                            #T o F validation
                            if rlaboratorio != 'T' and rlaboratorio != 'F':
                                row.append(T('Error: ') + T('El tipo de laboratorio ingresado no es correcto. Este debe ser T o F.'))
                                error_users.append(row)
                            else:
                                #insert a new user with csv data
                                usr = db.academic.insert(carnet = rcarnet,
                                                              email = remail)
                                #Add log
                                db.academic_log.insert(user_name = auth.user.username, 
                                                        roll =  'Student', 
                                                        operation_log = 'insert', 
                                                        after_carnet = rcarnet, 
                                                        after_email = remail, 
                                                        id_academic = usr.id,
                                                        id_period = current_period.id,
                                                        description = 'Se inserto desde archivo CSV.')
                                #add user to the course
                                ingresado = db.academic_course_assignation.insert(carnet = usr.id, semester = current_period, assignation = check.project, laboratorio = rlaboratorio)
                                #Add to log
                                lab_var = ''
                                if rlaboratorio == 'T':
                                    lab_var = 'True'
                                else:
                                    lab_var = 'False'

                                #Search for user roles
                                result = db(db.auth_membership.user_id==auth.user.id).select()
                                roll_var = ''
                                i = 0;
                                for a in result:
                                    if i == 0:
                                        roll_var = a.group_id.role
                                        i = i+1
                                    else:
                                        roll_var = roll_var + ',' + a.group_id.role

                                db.academic_course_assignation_log.insert(user_name = auth.user.username, roll =  roll_var, 
                                                        operation_log = 'insert', 
                                                        after_carnet = rcarnet, 
                                                        after_course = str(check.project.name), 
                                                        after_year = str(current_period.yearp) ,
                                                        after_semester = str(current_period.period),
                                                        after_laboratory = lab_var,
                                                        id_academic_course_assignation = str(ingresado.id),
                                                        id_period = current_period.id,
                                                        description = 'Se inserto desde archivo CSV.')
                else:
                    #Agregar la advertencia que el usuario ya se encuentra registrado en el sistema
                    row.append(T('Aviso: ') + T('El estudiante ya se encuentra registrado en el sistema'))
                    usr2 = db.academic_course_assignation((db.academic_course_assignation.semester == current_period) & (db.academic_course_assignation.assignation == check.project) & (db.academic_course_assignation.carnet == usr.id))
                    if usr2 is None:
                        #T o F validation
                        if rlaboratorio != 'T' and rlaboratorio != 'F':
                            row.append(T('Error: ') + T('El tipo de laboratorio ingresado no es correcto. Este debe ser T o F.'))
                            error_users.append(row)
                        else:
                            lab_var = ''
                            if rlaboratorio == 'T':
                                lab_var = 'True'
                            else:
                                lab_var = 'False'

                            #Search for user roles
                            result = db(db.auth_membership.user_id==auth.user.id).select()
                            roll_var = ''
                            i = 0;
                            for a in result:
                                if i == 0:
                                    roll_var = a.group_id.role
                                    i = i+1
                                else:
                                    roll_var = roll_var + ',' + a.group_id.role

                            ingresado = db.academic_course_assignation.insert(carnet = usr.id, semester = current_period, assignation = check.project, laboratorio = rlaboratorio)
                            db.academic_course_assignation_log.insert(user_name = auth.user.username, roll =  roll_var, 
                                                        operation_log = 'insert', 
                                                        after_carnet = rcarnet, 
                                                        after_course = str(check.project.name), 
                                                        after_year = str(current_period.yearp) ,
                                                        after_semester = str(current_period.period),
                                                        after_laboratory = lab_var,
                                                        id_academic_course_assignation = str(ingresado.id),
                                                        id_period = current_period.id,
                                                        description = 'Se inserto desde archivo CSV.')
                            aviso_users.append(row)
                    else:
                        row.remove(T('Aviso: ') + T('El estudiante ya se encuentra registrado en el sistema'))
                        row.append(T('Error: ') + T('El estudiante ya se encuentra registrado en el sistema y asignado al curso'))
                        error_users.append(row)
                    continue
        except:
            response.flash = T('File doesn\'t seem properly encoded.')
            return dict(success = False,
                file = False,
                periods = periods,
                current_period = current_period,
                name=name, files=files)
        response.flash = T('Data uploaded')
        return dict(success = success,
                    errors = error_users,
                    avisos = aviso_users,
                    periods = periods,
                    current_period = current_period,
                    name=name, files=files)
    return dict(success = False,
                file = False,
                periods = periods,
                current_period = current_period,
                name=name, files=files)



@auth.requires_login()
@auth.requires(auth.has_membership('Student') or auth.has_membership('Teacher'))
def student_courses():
    #show all assignations of current user
    import cpfecys
    def split_name(project):
        try:
            (nameP, projectSection) = str(project).split('(')
        except:
            nameP = project
        return nameP

    def split_section(project):
        try:
            projectSection = None
            nameS = None
            (nameP, projectSection) = str(project).split('(')
            (nameS,garbage) = str(projectSection).split(')')
        except:
            nameS = '--------'
        return nameS
    return dict(assignations = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == cpfecys.current_year_period().id)).select(), split_name=split_name, split_section=split_section)

#Mostrar el listado de estudiantes que han sido registrados en el sistema
@auth.requires_login()
@auth.requires(auth.has_membership('Student') or auth.has_membership('Teacher'))
def academic():       
    if request.vars['search_var'] is None:
        query = db.academic
    else:
        query = db.academic.carnet.like('%'+request.vars['search_var']+'%')

    db.academic.id.writable = False
    db.academic.id.readable = False

    grid = SQLFORM.grid(
        query, oncreate=oncreate_academic, onupdate=onupdate_academic, ondelete=ondelete_academic,  maxtextlength=100,csv=False)
    return dict(grid=grid)

def oncreate_academic(form):
    import datetime
    cdate = datetime.datetime.now()
    import cpfecys  
    currentyear_period = cpfecys.current_year_period()

    #Search for user roles
    result = db(db.auth_membership.user_id==auth.user.id).select()
    roll_var = ''
    i = 0;
    for a in result:
        if i == 0:
            roll_var = a.group_id.role
            i = i+1
        else:
            roll_var = roll_var + ',' + a.group_id.role  

    db.academic_log.insert(user_name = auth.user.username, 
                                roll =  roll_var, 
                                operation_log = 'insert', 
                                after_carnet = form.vars.carnet, 
                                after_email = form.vars.email, 
                                id_academic = form.vars.id, 
                                id_period = str(currentyear_period.id),
                                description = 'Se agrego registro desde la pagina agregar estudiantes.')

def onupdate_academic(form):
    import datetime
    import cpfecys  
    currentyear_period = cpfecys.current_year_period()
    cdate = datetime.datetime.now()
    #session.flash = T('hola-'+str(form.vars))
    #Search for user roles
    result = db(db.auth_membership.user_id==auth.user.id).select()
    roll_var = ''
    i = 0;
    for a in result:
        if i == 0:
            roll_var = a.group_id.role
            i = i+1
        else:
            roll_var = roll_var + ',' + a.group_id.role    

    student_var = db(db.academic_log.id_academic == form.vars.id).select(orderby=db.academic_log.id)
    carnet_var = ''
    email_var = ''
    for a in student_var:
        carnet_var = a.after_carnet
        email_var = a.after_email
    if form.vars.delete_this_record == None:
        db.academic_log.insert(user_name = auth.user.username, 
                                roll =  roll_var, 
                                operation_log = 'update', 
                                before_carnet = carnet_var, 
                                before_email = email_var, 
                                after_carnet = form.vars.carnet, 
                                after_email = form.vars.email, 
                                id_academic = form.vars.id, 
                                id_period = str(currentyear_period.id),
                                description = 'Se modifico registro desde la pagina estudiantes.')
    else:
        db.academic_log.insert(user_name = auth.user.username, 
                                roll =  str(roll_var), 
                                operation_log = 'delete', 
                                before_carnet = carnet_var, 
                                before_email = email_var, 
                                id_period = str(currentyear_period.id),
                                description = 'Se elimino el registro desde la pagina estudiantes.')


def ondelete_academic(table_involved, id_of_the_deleted_record):
    import datetime
    import cpfecys  
    currentyear_period = cpfecys.current_year_period()

    cdate = datetime.datetime.now()
    student_var = db.academic(id_of_the_deleted_record)    

    #Search for user roles
    result = db(db.auth_membership.user_id==auth.user.id).select()
    roll_var = ''
    i = 0;
    for a in result:
        if i == 0:
            roll_var = a.group_id.role
            i = i+1
        else:
            roll_var = roll_var + ',' + a.group_id.role        

    db.academic_log.insert(user_name = auth.user.username, 
                                roll =  str(roll_var), 
                                operation_log = 'delete', 
                                before_carnet = student_var.carnet, 
                                before_email = student_var.email, 
                                id_period = str(currentyear_period.id),
                                description = 'Se elimino el registro desde la pagina estudiantes.')




