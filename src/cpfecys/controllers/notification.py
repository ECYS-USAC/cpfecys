#***************************************************************
#*******************NOTIFICATIONS OF STUDENT********************
#***************************************************************
#***************************************************************
#*******************REGISTER OF NOTIFICATIONS*******************
#***************************************************************
@auth.requires_login()
@auth.requires_membership('Teacher')
def teacher_register_mail_notifications_detail():
    if request.vars['notification'] ==None:
        if session.notification_var == None:
            session.flash = T('Not valid Action.')
            redirect(URL('default', 'index'))
        else:
            notice = session.notification_var
    else:
        notice = request.vars['notification']
        session.notification_var = notice

    #show the page resiter_mail_notifications.html
    response.view='notification/teacher_register_mail_notifications_detail.html'

    #obtain the projects where the student is register and is of the select semester
    asunto = db(db.notification_general_log4.id==notice).select()
    db.notification_log4.register.readable = False
    db.notification_log4.id.readable = False
    db.notification_general_log4.id.readable = False
    db.notification_general_log4.subject.readable = False
    db.notification_general_log4.sent_message.readable = False
    db.notification_general_log4.emisor.readable = False
    db.notification_general_log4.course.readable = False
    db.notification_general_log4.yearp.readable = False
    db.notification_general_log4.period.readable = False
    
    if request.vars['search_var'] is None:
        query = ((db.notification_log4.register==notice)&(db.notification_general_log4.id==db.notification_log4.register))
    else:
        query = ((db.notification_log4.register==notice)&(db.notification_general_log4.id==db.notification_log4.register) & (db.notification_log4.destination.like('%'+request.vars['search_var']+'%')) )


    grid = SQLFORM.grid(query, deletable=False, editable=False, create=False, paginate=10, details=False, maxtextlength={'notification_log4.result_log' : 256},csv=False)
    
    return dict(subject=asunto, grid=grid, notice=notice)


@auth.requires_login()
@auth.requires_membership('Teacher')
def teacher_register_mail_notifications():
#db.user_project.assigned_user == auth.user.id
    #Obtain the current period of the system and all the register periods
    period = cpfecys.current_year_period()
    periods = db(db.period_year).select()

    #Check if the period is change
    if request.vars['period'] !=None:
        period = request.vars['period']
        period = db(db.period_year.id==period).select().first()

    #show the page resiter_mail_notifications.html
    response.view='notification/teacher_register_mail_notifications.html'

    #obtain the projects where the student is register and is of the select semester
    projects = db((db.user_project.period==period) & (db.user_project.assigned_user == auth.user.id)).select()
#    dest=[]
 #   for student in allProject:
  #      dest.append(student.project)
   # projects = db(db.project.id.belongs(dest)).select()

    #obtain the names of the projects that thas register the user
    def obtain_nameProjects(userP):
        p = db(db.project.id==userP).select()
        nameP = ''
        for p2 in p:
            nameP=p2.name
        return nameP

    def obtain_period(periodo):
        semester = db(db.period.id==periodo).select()
        nameS = ''
        for s in semester:
            nameS=s.name
        return nameS

    #obtain all the registers of the send notices of the student
    def obtain_notices(project):
        #name project
        n=obtain_nameProjects(project.project)

        #name of the year
        anio = db(db.period_year.id==project.period).select()
        nameY = ''
        idP = ''
        for a in anio:
            nameY=a.yearp
            idP = a.period

        #name of period
        nameS=obtain_period(idP)
        #obtain all the notices that has the user has register
        notices  = db((db.notification_general_log4.emisor==project.assigned_user.username) & (db.notification_general_log4.course==n)&(db.notification_general_log4.period==nameS)&(db.notification_general_log4.yearp==nameY)).select()
        return notices

    def obtain_Persons(project):
        persons = db((db.user_project.assigned_user!=auth.user.id)&(db.user_project.project == project.project)&(db.user_project.period==project.period)&(db.auth_membership.user_id==db.user_project.assigned_user)&(db.auth_membership.group_id==2)).select()
        return persons

    def obtain_PersonsA(project):
        persons = db((db.user_project.assigned_user==auth.user.id) & (db.user_project.project == project.project)&(db.user_project.period==project.period)).select()
        return persons

    return dict(obtain_PersonsA=obtain_PersonsA,obtain_Persons=obtain_Persons, obtain_nameProjects=obtain_nameProjects,periods=periods, projects=projects, obtain_notices=obtain_notices)

#obtain all the registers of the send notices of the student
def teacher_register_mail():
    notices=None
    tipoD=0
    if request.vars['userN'] != None and request.vars['project']!=None:
        usuario = db(db.auth_user.id==request.vars['userN']).select().first()
        project = request.vars['project']
        userproject = db(db.user_project.id==project).select().first()
        notices  = db((db.notification_general_log4.emisor==usuario.username) & (db.notification_general_log4.course==userproject.project.name)&(db.notification_general_log4.period==userproject.period.period.name)&(db.notification_general_log4.yearp==userproject.period.yearp)).select()
        tipoD=1
    else:
        if request.vars['project']!=None:
            project = request.vars['project']
            userproject = db(db.user_project.id==project).select().first()
            notices  = db((db.notification_general_log4.emisor==auth.user.username) & (db.notification_general_log4.course==userproject.project.name)&(db.notification_general_log4.period==userproject.period.period.name)&(db.notification_general_log4.yearp==userproject.period.yearp)).select()
            tipoD=2
    return dict(notices=notices, tipoD=tipoD)

def teacher_register_mail_detail():
    if request.vars['notice'] != None:
        listadoC = db(db.notification_log4.register==request.vars['notice']).select().first()
        l=listadoC.destination[1:-1].replace("'","").split(",")
        a=0
        for i in l:
            if a>0:
                l[a]=i[1:]
            a=a+1

        noticia = db(db.notification_general_log4.id==request.vars['notice']).select().first()
        a=0
        tutores = db((db.auth_user.id==db.user_project.assigned_user)&(db.user_project.project==db.project.id)&(db.project.name==noticia.course)&(db.user_project.period==db.period_year.id)&(db.period_year.yearp==noticia.yearp)&(db.period_year.period==db.period.id)&(db.period.name==noticia.period)).select()
        tempT = []
        for t in tutores:
            if t.auth_user.email in l:
                tempT.append(t.auth_user.id)
        tutores = db(db.auth_user.id.belongs(tempT)).select()
        estudiantes = db(db.academic.email.belongs(l)).select()
    return dict(tutores=tutores, estudiantes=estudiantes, noticia=noticia, log=listadoC)

def teacher_search_destination():
    if request.vars['notice'] != None:
        listadoC = db(db.notification_log4.register==request.vars['notice']).select().first()
        l=listadoC.destination[1:-1].replace("'","").split(",")
        a=0
        for i in l:
            if a>0:
                l[a]=i[1:]
            a=a+1

        noticia = db(db.notification_general_log4.id==request.vars['notice']).select().first()
        tutores = db((db.auth_user.id==db.user_project.assigned_user)&(db.user_project.project==db.project.id)&(db.project.name==noticia.course)&(db.user_project.period==db.period_year.id)&(db.period_year.yearp==noticia.yearp)&(db.period_year.period==db.period.id)&(db.period.name==noticia.period)).select()
        tempT = []
        for t in tutores:
            if t.auth_user.email in l:
                tempT.append(t.auth_user.id)
        if request.vars['search_input'] != None:
            tutores = db((db.auth_user.id.belongs(tempT))&(db.auth_user.username.like('%'+request.vars['search_input']+'%'))).select()
            estudiantes = db((db.academic.email.belongs(l))&(db.academic.carnet.like('%'+request.vars['search_input']+'%'))).select()
        else:
            tutores = db(db.auth_user.id.belongs(tempT)).select()
            estudiantes = db(db.academic.email.belongs(l)).select()
    return dict(tutores=tutores, estudiantes=estudiantes, noticia=noticia, log=listadoC)

#*********************************************************
#**********************ENVIAR AVISOS**********************
#*********************************************************
@auth.requires_login()
@auth.requires_membership('Teacher')
def teacher_send_mail_to_students(users1, users2, message, subject, check, semester, year):
    #Obtener valores reales (no ids)
    nameS2 = check.assigned_user.first_name+" "+check.assigned_user.last_name
    nameU = check.assigned_user.username
    nameP = check.project.name

    attachment_m = '<br><br><b>' + T('Attachments') +":</b><br>"

    if session.attachment_list != []:
        for attachment_list_var in session.attachment_list:
            for attachment_var in attachment_list_var:
                attachment_m = attachment_m + '<a href="' + cpfecys.get_domain() + URL('default/download', attachment_var.file_data) +'" target="blank"> '+ attachment_var.name + '</a> <br>'
    else:        
        attachment_m = ''

    try:
        (nameP, projectSection) = str(nameP).split('(')
        (nameS,garbage) = str(projectSection).split(')')
        nameP=nameP+' - '+nameS
    except:
        None
    period = T(semester)+' '+str(year)
    message = message.replace("\n","<br>")
    messageC = '<html>' + message + attachment_m + '<br><br>Catedrático:'+str(nameS2)+'<br>'+str(period)+'<br>'+str(nameP)+'<br>Sistema de Seguimiento de La Escuela de Ciencias y Sistemas<br> Facultad de Ingeniería - Universidad de San Carlos de Guatemala</html>'
    #variable de control
    control = 0
    #Log General del Envio
    row = db.notification_general_log4.insert(subject=subject,
                                        sent_message=message + attachment_m,
                                        emisor=check.assigned_user.username,
                                        course=check.project.name,
                                        yearp=year,
                                        period=semester)
    #Ciclo para el envio de correos para estudiantes
    ListadoCorreos = None
    if users1 != None:
        for user in users1:
            if user.email != None and user.email != '':
                if ListadoCorreos == None:
                    ListadoCorreos = []
                    ListadoCorreos.append(user.email)
                else:
                    ListadoCorreos.append(user.email)

    if users2 != None:
        for user in users2:
            if user.email != None and user.email != '':
                if ListadoCorreos == None:
                    ListadoCorreos = []
                    ListadoCorreos.append(user.email)
                else:
                    ListadoCorreos.append(user.email)


    was_sent = mail.send(to='dtt.ecys@dtt-ecys.org',subject=subject,message=messageC, bcc=ListadoCorreos)
    ##Notification LOG GENERAL
    db.mailer_log.insert(sent_message = messageC, destination = str(ListadoCorreos), result_log = str(mail.error or '') + ':' + str(mail.result), success = was_sent, emisor=str(check.assigned_user.username))
    ##Notification LOG
    db.notification_log4.insert(destination = str(ListadoCorreos), result_log = str(mail.error or '') + ':' + str(mail.result), success = was_sent, register=row.id)
    if was_sent==False:
        control=control+1
                
    

    session.attachment_list = []
    session.attachment_list_temp = []
    session.attachment_list_temp2 = []
    session.notification_subject = ''
    session.notification_message = ''
    return control

    
@auth.requires_login()
@auth.requires_membership('Teacher')
def teacher_mail_notifications():
    import cpfecys
    #Obtener la asignacion del estudiante
    assignation = request.vars['assignation']
    #Obtener al tutor del proyecto
    check = db.user_project(id = assignation, assigned_user = auth.user.id)
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


    year = db.period_year(id=check.period)
    year_semester = db.period(id=year.period)
    var=""
    if (request.args(0) == 'send'):
        #Tipo estudiante al que se le enviara el correo
        tipoes = request.vars['tipoe']
        #Obtener listado alumnos a enviar mensaje
        listado = request.vars['listado']
        listado2 = request.vars['listado2']
        #Mensaje que se enviara
        message = request.vars['message']
        #Asunto del mensaje que se enviara
        subject = request.vars['subject']
        #Check that the user select only one group of students
        if not tipoes or count_selectItems(tipoes)!=1:
            session.flash = T('You must select only one group of students')
            redirect(URL('notification', 'teacher_mail_notifications'))
            return
        #Obtener la lista de destinatarios en base a los usuarios presionados
        if ((tipoes=='specific' and (listado!= None or listado2!= None)) or (tipoes!='specific')) and message != '' and subject != '':
            users1 = None
            users2 = None
            count1 = db.academic_course_assignation.id.count()
            count2 = db.auth_user.id.count()
            user1 = None
            user2 = None
            totalC1 = 0
            totalC2 = 0
            if tipoes =='all' or tipoes=='cl' or tipoes =='sl' or tipoes =='fp':
                if tipoes =='cl':
                    users1 = db((db.academic.id==db.academic_course_assignation.carnet)&(db.academic_course_assignation.semester == period) & (db.academic_course_assignation.assignation==check.project) & (db.academic_course_assignation.laboratorio=='True')).select(count1)
                    totalC1 = count_Items(users1,count1)
                elif tipoes =='sl':
                    users1 = db((db.academic.id==db.academic_course_assignation.carnet)&(db.academic_course_assignation.semester == period) & (db.academic_course_assignation.assignation==check.project) & (db.academic_course_assignation.laboratorio=='False')).select(count1)
                    totalC1 = count_Items(users1,count1)
                elif tipoes =='fp':
                    users2 = db((db.auth_user.id==db.user_project.assigned_user)&(db.user_project.period == period) & (db.user_project.project==check.project)&(db.auth_membership.user_id==db.user_project.assigned_user)&(db.auth_membership.group_id==2)).select(count2)
                    totalC2 = count_Items(users2,count2)
                else:
                    users1 = db((db.academic.id==db.academic_course_assignation.carnet)&(db.academic_course_assignation.semester == period) & (db.academic_course_assignation.assignation==check.project)).select(count1)
                    users2 = db((db.auth_user.id==db.user_project.assigned_user)&(db.user_project.period == period) & (db.user_project.project==check.project)&(db.auth_membership.user_id==db.user_project.assigned_user)&(db.auth_membership.group_id==2)).select(count2)
                    totalC1 = count_Items(users1,count1)
                    totalC2 = count_Items(users2,count2)
                if tipoes=='all' and (totalC1>0 or totalC2>0):
                    if totalC1>0:
                        user1 = []
                        users1 = db((db.academic.id==db.academic_course_assignation.carnet)&(db.academic_course_assignation.semester == period) & (db.academic_course_assignation.assignation==check.project)).select()
                        for user in users1:
                            user1.append(user.academic)
                    if totalC2 >0:
                        user2 = []
                        users2 = db((db.auth_user.id==db.user_project.assigned_user)&(db.user_project.period == period) & (db.user_project.project==check.project)&(db.auth_membership.user_id==db.user_project.assigned_user)&(db.auth_membership.group_id==2)).select()
                        for user in users2:
                            user2.append(user.auth_user)
                elif tipoes =='cl' and totalC1 > 0:
                    user1 = []
                    users1 = db((db.academic.id==db.academic_course_assignation.carnet)&(db.academic.id==db.academic_course_assignation.carnet)&(db.academic_course_assignation.semester == period) & (db.academic_course_assignation.assignation==check.project) & (db.academic_course_assignation.laboratorio=='True')).select()
                    for user in users1:
                        user1.append(user.academic)
                elif tipoes =='sl' and totalC1 > 0:
                    user1 = []
                    users1 = db((db.academic.id==db.academic_course_assignation.carnet)&(db.academic.id==db.academic_course_assignation.carnet)&(db.academic_course_assignation.semester == period) & (db.academic_course_assignation.assignation==check.project) & (db.academic_course_assignation.laboratorio=='False')).select()
                    for user in users1:
                        user1.append(user.academic)
                elif tipoes =='fp' and totalC2 > 0:
                    user2 = []
                    users2 = db((db.auth_user.id==db.user_project.assigned_user)&(db.user_project.period == period) & (db.user_project.project==check.project)&(db.auth_membership.user_id==db.user_project.assigned_user)&(db.auth_membership.group_id==2)).select()
                    for user in users2:
                        user2.append(user.auth_user)
            else:
                #Obtain the list of destination for the students
                if listado != None:
                    dest=[]
                    students = request.vars['listado']
                    try:
                        students.append(-1)
                        students.remove(-1)
                        for student in students:
                            dest.append(student)
                        #consultar a la base de datos para obtener a los usuarios a los que enviaremos
                        user1 = db(db.academic.id.belongs(dest)).select()
                    except:
                        #consultar a la base de datos para obtener a los usuarios a los que enviaremos
                        user1 = db(db.academic.id==request.vars['listado']).select()
                #obtain the list of destination for the final practices students
                if listado2 != None:
                    dest=[]
                    students = request.vars['listado2']
                    try:
                        students.append(-1)
                        students.remove(-1)
                        for student in students:
                            dest.append(student)
                        #consultar a la base de datos para obtener a los usuarios a los que enviaremos
                        user2 = db(db.auth_user.id.belongs(dest)).select()
                    except:
                        #consultar a la base de datos para obtener a los usuarios a los que enviaremos
                        user2 = db(db.auth_user.id==request.vars['listado2']).select()

            if user1 != None or user2 != None:
                #Realizar el envio de mensajes
                fail = teacher_send_mail_to_students(user1,user2,message,subject,check,year_semester.name,year.yearp)
                if fail > 0:
                    session.flash = T('Avisos enviados - Existen '+str(fail) + ' avisos fallidos, revise el registro de avisos')
                else:
                    session.flash = T('Notices Sent')
                redirect(URL('notification', 'teacher_mail_notifications'))
            else:
                session.flash = T('No recipient who sent the message')
            redirect(URL('notification', 'teacher_mail_notifications'))
        else:
            session.flash = T('Fill all fields of notification')
            redirect(URL('notification', 'teacher_mail_notifications'))

    def get_projects(grupo):
        #Obtener la asignacion del estudiante
        assignation = request.vars['assignation']
        #Obtener al tutor
        check = db.user_project(id = assignation, assigned_user = auth.user.id)
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
        if grupo == 1:
            #Obtener los estudiantes del tutor y asignados al proyecto
            students = db((db.academic_course_assignation.semester == period) & (db.academic_course_assignation.assignation==check.project) & (db.academic_course_assignation.laboratorio=='True')).select()
            return students
        else:
            if grupo==2:
                #Obtener los estudiantes del tutor y asignados al proyecto
                students = db((db.academic_course_assignation.semester == period) & (db.academic_course_assignation.assignation==check.project) & (db.academic_course_assignation.laboratorio=='False')).select()
                return students
            else:
                #obtain the final practice students assigned in the course where the user is the manager
                students = db((db.user_project.project==check.project)&(db.user_project.period==check.period)&(db.user_project.assigned_user!=check.assigned_user)&(db.auth_membership.user_id==db.user_project.assigned_user)&(db.auth_membership.group_id==2)).select()
                return students

    if session.notification_subject == None:
        session.notification_subject = ''
    if session.notification_message == None:
        session.notification_message = ''    

    upload_form = FORM(INPUT(_name='file_name',_type='text'),
                        INPUT(_name='file_upload',_type='file',requires=[IS_UPLOAD_FILENAME(extension = '(pdf|zip)',error_message='Solo se aceptan archivos con extension zip|pdf'),IS_LENGTH(2097152,error_message='El tamaño máximo del archivo es 2MB')]),
                        INPUT(_name='file_description',_type='text'),
                        INPUT(_name='file_visible',_type='checkbox'))

    if upload_form.accepts(request.vars,formname='upload_form'):
        try:
            if ( upload_form.vars.file_name is "" ) or ( upload_form.vars.file_upload is "") or ( upload_form.vars.file_description is ""):
                response.flash = T('You must enter all fields.')
            else:
                exists = db.library((db.library.name == upload_form.vars.file_name) & (db.library.project == check.project.id) & (db.library.owner_file==auth.user.id) )
                if exists is None:                    
                    file_var = db.library.file_data.store(upload_form.vars.file_upload.file, upload_form.vars.file_upload.filename)
                    
                    var_visible = 'False'
                    if upload_form.vars.file_visible:
                        var_visible = 'True'

                    id = db.library.insert(file_data=file_var,
                                            name=upload_form.vars.file_name,
                                            description=upload_form.vars.file_description,
                                            visible=var_visible,
                                            period=cpfecys.current_year_period(),
                                            project=check.project.id,
                                            owner_file=auth.user.id)

                    session.attachment_list.append( db(db.library.id==id).select() )
                    response.flash = T('File loaded successfully.')
                else:
                    response.flash = T('File already exists.')
        except:
            response.flash = T('Error loading file.')

    attach_form = FORM()

    if attach_form.accepts(request.vars,formname='attach_form'):
        if session.attachment_list_temp != None:
            for var in session.attachment_list_temp:
                session.attachment_list.append(var)
                session.attachment_list_temp = []
        else:
            session.attachment_list_temp = []        
    
    remove_form = FORM()

    if remove_form.accepts(request.vars,formname='remove_form'):
        list_tempo = []
        if session.attachment_list_temp2 != None and len(session.attachment_list_temp2) > 0:
            for var_list in session.attachment_list:                
                for tempo1 in var_list:                    
                    cambiar = 'false'
                    for var_list_2 in session.attachment_list_temp2:
                        for tempo2 in var_list_2:
                            
                            if (tempo1.id == tempo2.id):
                                cambiar = 'true'

                if(cambiar == 'false'):
                    list_tempo.append(var_list)

            session.attachment_list = list_tempo
            session.attachment_list_temp2 = []
        else:
            session.attachment_list_temp2 = []

    
    session.project_id = check.project.id
    return dict(get_projects=get_projects,
        markmin_settings = cpfecys.get_markmin,
        name = check.project.name,
        semester = year_semester.name,
        year = year.yearp,
        assignation=assignation,
        attachment_list=session.attachment_list)

#Show all the courses that the teacher has register in the current period
@auth.requires_login()
@auth.requires_membership('Teacher')
def teacher_courses_mail_notifications():
    #show all assignations of current user
    import cpfecys
    session.attachment_list = []
    session.attachment_list_temp = []
    session.attachment_list_temp2 = []
    session.notification_subject = ''
    session.notification_message = ''
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




#***************************************************************
#*******************NOTIFICATIONS OF STUDENT********************
#***************************************************************
#***************************************************************
#*******************REGISTER OF NOTIFICATIONS*******************
#***************************************************************
@auth.requires_login()
@auth.requires_membership('Student')
def register_mail_notifications_detail():
    if request.vars['notification'] ==None:
        if session.notification_var == None:
            session.flash = T('Not valid Action.')
            redirect(URL('default', 'index'))
        else:
            notice = session.notification_var
    else:
        notice = request.vars['notification']
        session.notification_var = notice

    #show the page resiter_mail_notifications.html
    response.view='notification/register_mail_notifications_detail.html'

    #obtain the projects where the student is register and is of the select semester
    asunto = db(db.notification_general_log4.id==notice).select()
    db.notification_log4.register.readable = False
    db.notification_log4.id.readable = False
    db.notification_general_log4.id.readable = False
    db.notification_general_log4.subject.readable = False
    db.notification_general_log4.sent_message.readable = False
    db.notification_general_log4.emisor.readable = False
    db.notification_general_log4.course.readable = False
    db.notification_general_log4.yearp.readable = False
    db.notification_general_log4.period.readable = False
    
    if request.vars['search_var'] is None:
        query = ((db.notification_log4.register==notice)&(db.notification_general_log4.id==db.notification_log4.register))
    else:
        query = ((db.notification_log4.register==notice)&(db.notification_general_log4.id==db.notification_log4.register) & (db.notification_log4.destination.like('%'+request.vars['search_var']+'%')) )
    
    grid = SQLFORM.grid(query, deletable=False, editable=False, create=False, paginate=10, details=False, maxtextlength={'notification_log4.result_log' : 256},csv=False)
    
    return dict(subject=asunto, grid=grid, notice=notice)

@auth.requires_login()
@auth.requires_membership('Student')
def register_mail_notifications():
    #Obtain the current period of the system and all the register periods
    period = cpfecys.current_year_period()
    periods = db(db.period_year).select()

    #Check if the period is change
    if request.vars['period'] !=None:
        period = request.vars['period']
        period = db(db.period_year.id==period).select().first()

    #show the page resiter_mail_notifications.html
    response.view='notification/register_mail_notifications.html'

    #obtain the projects where the student is register and is of the select semester
    projects = db((db.user_project.period==period) & (db.user_project.assigned_user == auth.user.id)).select()

    def obtain_nameProjects(userP):
        p = db(db.project.id==userP).select()
        nameP = ''
        for p2 in p:
            nameP=p2.name
        return nameP

    return dict(obtain_nameProjects=obtain_nameProjects,periods=periods, projects=projects)

#obtain all the registers of the send notices of the student
def register_mail():
    notices=None    
    if request.vars['project'] != None:
        project = request.vars['project']
        userproject = db(db.user_project.id==project).select().first()
        notices  = db((db.notification_general_log4.emisor==auth.user.username) & (db.notification_general_log4.course==userproject.project.name)&(db.notification_general_log4.period==userproject.period.period.name)&(db.notification_general_log4.yearp==userproject.period.yearp)).select()
    return dict(notices=notices)


def register_mail_detail():
    all_n=None
    if request.vars['notice'] != None:
        count = db.notification_log4.id.count()
        total = db(db.notification_log4.register==request.vars['notice']).select(count).first()

        if total[count]==1:
            listadoC = db(db.notification_log4.register==request.vars['notice']).select().first()
            d = listadoC.destination[0:1]
            if d =="|":
                d=listadoC.destination[1:-1]
                d=d.replace("|",",")
                listadoC.destination=str(d).split(",")
                listadoC.destination = db(db.academic.email.belongs(listadoC.destination)).select()
            else:
                listado=[]
                listado.append(listadoC.destination)
                listadoC.destination = db(db.academic.carnet.belongs(listado)).select()
        else:
            if total[count]>1:
                    listadoC = db(db.notification_log4.register==request.vars['notice']).select()
                    listado=[]
                    for l in listadoC:
                        listado.append(l.destination)
                    listadoC = db(db.notification_log4.register==request.vars['notice']).select().first()
                    listadoC.destination = db(db.academic.carnet.belongs(listado)).select()
    return dict(all_n=listadoC)

def search_destination():
    all_n=None
    if request.vars['notice'] != None:
        count = db.notification_log4.id.count()
        total = db(db.notification_log4.register==request.vars['notice']).select(count).first()

        if total[count]==1:
            listadoC = db(db.notification_log4.register==request.vars['notice']).select().first()
            d = listadoC.destination[0:1]
            if d =="|":
                d=listadoC.destination[1:-1]
                d=d.replace("|",",")
                listadoC.destination=str(d).split(",")
                if request.vars['search_input'] != None:
                    listadoC.destination = db(db.academic.email.belongs(listadoC.destination) & (db.academic.carnet.like('%'+request.vars['search_input']+'%'))).select()
                else:
                    listadoC.destination = db(db.academic.email.belongs(listadoC.destination)).select()
            else:
                listado=[]
                listado.append(listadoC.destination)
                listadoC.destination = db(db.academic.carnet.belongs(listado)).select()
                if request.vars['search_input'] != None:
                    listadoC.destination = db((db.academic.carnet.belongs(listado)) & (db.academic.carnet.like('%'+request.vars['search_input']+'%'))).select()
                else:
                    listadoC.destination = db(db.academic.carnet.belongs(listado)).select()
        else:
            if total[count]>1:
                    listadoC = db(db.notification_log4.register==request.vars['notice']).select()
                    listado=[]
                    for l in listadoC:
                        listado.append(l.destination)
                    listadoC = db(db.notification_log4.register==request.vars['notice']).select().first()
                    if request.vars['search_input'] != None:
                        listadoC.destination = db((db.academic.carnet.belongs(listado)) & (db.academic.carnet.like('%'+request.vars['search_input']+'%'))).select()
                    else:
                        listadoC.destination = db(db.academic.carnet.belongs(listado)).select()

    #if request.vars['notice'] is None:
     #   all_list = db((db.library.owner_file==auth.user.id) or ((db.library.project == session.project_id) & (db.library.visible==True)) ).select()
    #else:
    all_n=None
    tipoD = 0
    if request.vars['notice'] != None:
        #all_n = db(db.notification_log4.register==request.vars['notice']).select().first()
        count = db.notification_log4.id.count()
        total = db(db.notification_log4.register==request.vars['notice']).select(count)
        totalR = 0
        for t in total:
            totalR=t[count]
        if totalR>1:
            listadoC = db(db.notification_log4.register==request.vars['notice']).select().first()
            d = listadoC.destination[0:1]
            if d !='|':
                listadoC = db(db.notification_log4.register==request.vars['notice']).select()
                listado=[]
                for l in listadoC:
                    listado.append(int(l.destination))
                listadoC = db(db.notification_log4.register==request.vars['notice']).select().first()
                #session.flash=str(listado)
                #redirect(URL('default','index'))
                if request.vars['search_input'] != None:
                    carnets = db((db.academic.carnet.belongs(listado)) & (db.academic.carnet.like('%'+request.vars['search_input']+'%'))).select()
                else:
                    carnets = db(db.academic.carnet.belongs(listado)).select()
                listadoC.destination=carnets
            else:
                listadoC = db(db.notification_log4.register==request.vars['notice']).select()
                listado=''
                for l in listadoC:
                    if listado=='':
                        listado=l.destination[1:-1]
                    else:
                        listado+=","+l.destination[1:-1]
                listadoC = db(db.notification_log4.register==request.vars['notice']).select().first()
                listadoC.destination=str(listado).split(",")
                
                listadoC.destination=carnets
        else:
            listadoC = db(db.notification_log4.register==request.vars['notice']).select().first()
            d = listadoC.destination[0:1]
            if d =='|':
                d=listadoC.destination[1:-1]
                d=d.replace("|",",")
                listadoC.destination=str(d).split(",")
                if request.vars['search_input'] != None:
                    carnets = db(db.academic.email.belongs(listadoC.destination) & (db.academic.carnet.like('%'+request.vars['search_input']+'%'))).select()
                else:
                    carnets = db(db.academic.email.belongs(listadoC.destination)).select()
                listadoC.destination=carnets
            else:
                if d=='[':
                    l=listadoC.destination[1:-1].replace("'","").split(",")
                    l = list(set(l))
                    listado = db((db.academic.email.belongs(l))&(db.academic.carnet.like('%'+request.vars['search_input']+'%'))).select()
                    listadoC.destination=listado
                else:
                    listado=[]
                    listado.append(int(listadoC.destination))
                    if request.vars['search_input'] != None:
                        carnets = db((db.academic.carnet.belongs(listado)) & (db.academic.carnet.like('%'+request.vars['search_input']+'%'))).select()
                    else:
                        carnets = db(db.academic.carnet.belongs(listado)).select()
                    listadoC.destination=carnets
    return dict(all_n=listadoC, tipoD=tipoD)
#*********************************************************
#**********************ENVIAR AVISOS**********************
#*********************************************************
@auth.requires_login()
@auth.requires_membership('Student')
def send_mail_to_students(users, message, subject, check, semester, year):
    #Obtener valores reales (no ids)
    nameS2 = check.assigned_user.first_name+" "+check.assigned_user.last_name
    nameU = check.assigned_user.username
    nameP = check.project.name

    attachment_m = '<br><br><b>' + T('Attachments') +":</b><br>"
    attachments_list = []
    if session.attachment_list != []:
        for attachment_list_var in session.attachment_list:
            for attachment_var in attachment_list_var:
                try:
                    attachments_list.append(mail.Attachment(cpfecys.get_domain() + URL('default/download', attachment_var.file_data)))
                except:
                    None
                attachment_m = attachment_m + '<a href="'+ cpfecys.get_domain() + URL('default/download', attachment_var.file_data) +'" target="blank"> '+ attachment_var.name + '</a> <br>'
    else:        
        attachment_m = ''
        
    
    try:
        (nameP, projectSection) = str(nameP).split('(')
        (nameS,garbage) = str(projectSection).split(')')
        nameP=nameP+' - '+nameS
    except:
        None
    period = T(semester)+' '+str(year)
    message = message.replace("\n","<br>")
    messageC = '<html>' + message + attachment_m + '<br><br>Tutor Academico: '+str(nameS2)+'<br>'+str(period)+'<br>'+str(nameP)+'<br>Sistema de Seguimiento de La Escuela de Ciencias y Sistemas<br> Facultad de Ingeniería - Universidad de San Carlos de Guatemala</html>'
    #variable de control
    control = 0
    #Log General del Envio
    row = db.notification_general_log4.insert(subject=subject,
                                        sent_message=message + attachment_m,
                                        emisor=check.assigned_user.username,
                                        course=check.project.name,
                                        yearp=year,
                                        period=semester)
    #Ciclo para el envio de correos
    ListadoCorreos = None
    for user in users:
        if user.email != None and user.email != '':
            if ListadoCorreos == None:
                ListadoCorreos = []
                ListadoCorreos.append(user.email)
            else:
                ListadoCorreos.append(user.email)

    was_sent = mail.send(to='dtt.ecys@dtt-ecys.org',subject=subject,message=messageC, bcc=ListadoCorreos)
    #MAILER LOG
    db.mailer_log.insert(sent_message = messageC,
                     destination = str(ListadoCorreos),
                     result_log = str(mail.error or '') + ':' + \
                     str(mail.result),
                     success = was_sent, emisor=str(check.assigned_user.username))
    ##Notification LOG
    db.notification_log4.insert(destination = ListadoCorreos,
                     result_log = str(mail.error or '') + ':' + \
                     str(mail.result),
                     success = was_sent,
                     register=row.id)
    if was_sent==False:
        control=control+1
    session.attachment_list = []
    session.attachment_list_temp = []
    session.attachment_list_temp2 = []
    session.notification_message = ''
    session.notification_subject = ''
    return control


@auth.requires_login()
@auth.requires_membership('Student')
def mail_notifications():
    import cpfecys
    #Obtener la asignacion del estudiante
    assignation = request.vars['assignation']
    #Obtener al tutor del proyecto
    check = db.user_project(id = assignation, assigned_user = auth.user.id)
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


    year = db.period_year(id=check.period)
    year_semester = db.period(id=year.period)
    var=""
    if (request.args(0) == 'send'):
        #Tipo estudiante al que se le enviara el correo
        tipoes = request.vars['tipoe']
        #Obtener listado alumnos a enviar mensaje
        listado = request.vars['listado']
        #Mensaje que se enviara
        message = request.vars['message']
        #Asunto del mensaje que se enviara
        subject = request.vars['subject']
        #Check that the user select only one group of students
        if not tipoes or count_selectItems(tipoes)!=1:
            session.flash = T('You must select only one group of students')
            redirect(URL('notification', 'mail_notifications'))
            return
        #Obtener la lista de destinatarios en base a los usuarios presionados
        if ((tipoes=='specific' and listado!= None) or (tipoes!='specific')) and message != '' and subject != '':
            #Check that the user select only one group of students
            users = None
            dest=[]
            count = db.academic_course_assignation.id.count()
            if tipoes =='all' or tipoes=='cl' or tipoes =='sl':
                if tipoes=='all':
                    users2 = db((db.academic_course_assignation.semester == period) & (db.academic_course_assignation.assignation==check.project)).select(count)
                elif tipoes =='cl':
                    users2 = db((db.academic.id==db.academic_course_assignation.carnet)&(db.academic_course_assignation.semester == period) & (db.academic_course_assignation.assignation==check.project) & (db.academic_course_assignation.laboratorio=='True')).select(count)
                else:
                    users2 = db((db.academic.id==db.academic_course_assignation.carnet)&(db.academic_course_assignation.semester == period) & (db.academic_course_assignation.assignation==check.project) & (db.academic_course_assignation.laboratorio=='False')).select(count)
                totalC = count_Items(users2,count)
                if totalC > 0:
                    if tipoes=='all':
                        users2 = db((db.academic.id==db.academic_course_assignation.carnet)&(db.academic_course_assignation.semester == period) & (db.academic_course_assignation.assignation==check.project)).select()
                    elif tipoes =='cl':
                        users2 = db((db.academic.id==db.academic_course_assignation.carnet)&(db.academic.id==db.academic_course_assignation.carnet)&(db.academic_course_assignation.semester == period) & (db.academic_course_assignation.assignation==check.project) & (db.academic_course_assignation.laboratorio=='True')).select()
                    else:
                        users2 = db((db.academic.id==db.academic_course_assignation.carnet)&(db.academic.id==db.academic_course_assignation.carnet)&(db.academic_course_assignation.semester == period) & (db.academic_course_assignation.assignation==check.project) & (db.academic_course_assignation.laboratorio=='False')).select()
                    users = []
                    for user in users2:
                        users.append(user.academic)
            else:
                students = request.vars['listado']
                try:
                    students.append(-1)
                    students.remove(-1)
                    for student in students:
                        dest.append(student)
                    users = db(db.academic.id.belongs(dest)).select()
                except:
                    users = db(db.academic.id==request.vars['listado']).select()

            if users != None:
                #Realizar el envio de mensajes
                fail = send_mail_to_students(users,message,subject,check,year_semester.name,year.yearp)
                if fail > 0:
                    session.flash = T('Avisos enviados - Existen '+str(fail) + ' avisos fallidos, revise el registro de avisos')
                else:
                    session.flash = T('Notices Sent')
                dest=None
                students=None
            else:
                session.flash = T('No recipient who sent the message')
            redirect(URL('notification', 'mail_notifications'))
        else:
            session.flash = T('Fill all fields of notification')
            redirect(URL('notification', 'mail_notifications'))

    def get_projects(grupo):
        import cpfecys
        
        if grupo == 1:       
            #Obtener la asignacion del estudiante
            assignation = request.vars['assignation']
            #Obtener al tutor
            check = db.user_project(id = assignation, assigned_user = auth.user.id)

            import cpfecys
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


            #Obtener los estudiantes del tutor y asignados al proyecto
            students = db((db.academic_course_assignation.semester == period) & (db.academic_course_assignation.assignation==check.project) & (db.academic_course_assignation.laboratorio=='True')).select()
            return students
        else:
            #Obtener la asignacion del estudiante
            assignation = request.vars['assignation']
            #Obtener al tutor
            check = db.user_project(id = assignation, assigned_user = auth.user.id)


            import cpfecys
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
            #Obtener los estudiantes del tutor y asignados al proyecto
            students = db((db.academic_course_assignation.semester == period) & (db.academic_course_assignation.assignation==check.project) & (db.academic_course_assignation.laboratorio=='False')).select()
            return students

    #db.library.period.default = check.project
    db.library.period.writable = False
    db.library.period.readable = False

    #db.library.project.default = check.project
    db.library.project.writable = False
    db.library.project.readable = False

    #db.library.owner_file.default = check.project
    db.library.owner_file.writable = False
    db.library.owner_file.readable = False

    if session.notification_subject == None:
        session.notification_subject = ''
    if session.notification_message == None:
        session.notification_message = ''    

    upload_form = FORM(INPUT(_name='file_name',_type='text'),
                        INPUT(_name='file_upload',_type='file',requires=[IS_UPLOAD_FILENAME(extension = '(pdf|zip)',error_message='Solo se aceptan archivos con extension zip|pdf'),IS_LENGTH(2097152,error_message='El tamaño máximo del archivo es 2MB')]),
                        INPUT(_name='file_description',_type='text'),
                        INPUT(_name='file_visible',_type='checkbox'))

    if upload_form.accepts(request.vars,formname='upload_form'):
        try:

            if ( upload_form.vars.file_name is "" ) or ( upload_form.vars.file_upload is "") or ( upload_form.vars.file_description is ""):
                response.flash = T('You must enter all fields.')
            else:
                exists = db.library((db.library.name == upload_form.vars.file_name) & (db.library.project == check.project.id) & (db.library.owner_file==auth.user.id) )
                if exists is None:                    
                    file_var = db.library.file_data.store(upload_form.vars.file_upload.file, upload_form.vars.file_upload.filename)
                    
                    var_visible = 'False'
                    if upload_form.vars.file_visible:
                        var_visible = 'True'

                    id = db.library.insert(file_data=file_var,
                                            name=upload_form.vars.file_name,
                                            description=upload_form.vars.file_description,
                                            visible=var_visible,
                                            period=cpfecys.current_year_period(),
                                            project=check.project.id,
                                            owner_file=auth.user.id)

                    session.attachment_list.append( db(db.library.id==id).select() )
                    response.flash = T('File loaded successfully.')
                else:
                    response.flash = T('File already exists.')
        except:
            response.flash = T('Error loading file.')

    attach_form = FORM()

    if attach_form.accepts(request.vars,formname='attach_form'):
        if session.attachment_list_temp != None:
            for var in session.attachment_list_temp:
                session.attachment_list.append(var)
                session.attachment_list_temp = []
        else:
            session.attachment_list_temp = []        
    
    remove_form = FORM()

    if remove_form.accepts(request.vars,formname='remove_form'):
        list_tempo = []
        if session.attachment_list_temp2 != None and len(session.attachment_list_temp2) > 0:
            for var_list in session.attachment_list:                
                for tempo1 in var_list:                    
                    cambiar = 'false'
                    for var_list_2 in session.attachment_list_temp2:
                        for tempo2 in var_list_2:
                            
                            if (tempo1.id == tempo2.id):
                                cambiar = 'true'

                if(cambiar == 'false'):
                    list_tempo.append(var_list)

            session.attachment_list = list_tempo
            session.attachment_list_temp2 = []
        else:
            session.attachment_list_temp2 = []

    session.project_id = check.project.id

    return dict(get_projects=get_projects,
        markmin_settings = cpfecys.get_markmin,
        name = check.project.name,
        semester = year_semester.name,
        year = year.yearp,
        assignation=assignation,
        attachment_list=session.attachment_list
        )

def files_check():
    return dict(var='');

def notification_functions():
    return dict(var='');

def attachment_files():
    return dict(attachment_list=session.attachment_list)



def search_files(): 
    if request.vars['search_input'] is None:
        #projects = db((db.project.id==db.user_project.project)&(db.period.id==db.user_project.period)&(db.user_project.assigned_user==auth.user.id)).select()
        #all_list = db((db.library.owner_file==auth.user.id) or ((db.library.project == session.project_id) & (db.library.visible==True)) ).select()
        all_list = db(((db.library.visible==True)&(db.library.owner_file!=auth.user.id)&(db.library.project==db.project.id)&(db.period.id==db.user_project.period)&(db.project.id==db.user_project.project)&(db.user_project.assigned_user==auth.user.id))).select()
        p=[]
        for a in all_list:
            p.append(a.library)
        all_list = db((db.library.owner_file==auth.user.id)).select()
        for a in all_list:
            p.append(a)
    else:
        #all_list = db((db.library.visible==True)&(db.library.project==db.project.id)&(db.period.id==db.user_project.period)&(db.project.id==db.user_project.project)&(db.user_project.assigned_user==auth.user.id)).select()
        #all_list = db((db.library.owner_file==auth.user.id) or ((db.library.project == session.project_id) & (db.library.visible==True)) ).select()
        #all_list = db( ((db.library.owner_file==auth.user.id) or ((db.library.project == session.project_id) & (db.library.visible==True) & (db.library.owner_file!=auth.user.id)) ) & (db.library.name.like('%'+request.vars['search_input']+'%'))).select()

        all_list = db(((db.library.name.like('%'+request.vars['search_input']+'%'))&(db.library.visible==True)&(db.library.owner_file!=auth.user.id)&(db.library.project==db.project.id)&(db.period.id==db.user_project.period)&(db.project.id==db.user_project.project)&(db.user_project.assigned_user==auth.user.id))).select()
        p=[]
        for a in all_list:
            p.append(a.library)
        all_list = db((db.library.name.like('%'+request.vars['search_input']+'%'))&(db.library.owner_file==auth.user.id)).select()
        for a in all_list:
            p.append(a)
    return dict(all_list=p)


#Mostrar los cursos a los cuales esta asignado el tutor academico para enviar mensajes
@auth.requires_login()
@auth.requires_membership('Student')
def courses_mail_notifications():
    #show all assignations of current user
    import cpfecys
    session.attachment_list = []
    session.attachment_list_temp = []
    session.attachment_list_temp2 = []
    session.notification_subject = ''
    session.notification_message = ''
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


#Function use to obtain the count of the items
def count_selectItems(items):
    count = 0
    try:
        items.append(-1)
        items.remove(-1)
        for item in items:
            count = count + 1
    except:
        if items==None:
            count = 0
        else:
            count = 1
    return count

def count_Items(notices,count):
    total = 0
    for s in notices:
        total = s[count]
    return total