#***************************************************************
#***************************************************************
#***************************************************************
#***************************************************************
@auth.requires_login()
@auth.requires(auth.has_membership('Student') or auth.has_membership('Teacher') or auth.has_membership('Academic'))
def inbox():
    import cpfecys
    cperiod = cpfecys.current_year_period()
    period_list = []
    period_list2 = []
    assignations = []
    coursesAdmin = []

    academic_var = db.academic(db.academic.id_auth_user==auth.user.id)        
    if auth.has_membership('Academic'):
        if academic_var is None:
            session.flash = T('Not valid Action.')
            redirect(URL('default', 'index'))
        else:
            period_list = db(db.academic_course_assignation.carnet==academic_var.id).select(db.academic_course_assignation.semester,distinct=True)
    
    select_form = FORM(INPUT(_name='semester_id',_type='text'))

    
    if select_form.accepts(request.vars,formname='select_form'):
        if auth.has_membership('Academic'):
            assignations = db((db.academic_course_assignation.semester==str(select_form.vars.semester_id)) & (db.academic_course_assignation.carnet==academic_var.id)).select()
        period_id = str(select_form.vars.semester_id)
    else:
        if auth.has_membership('Academic'):
            assignations = db((db.academic_course_assignation.semester==cperiod.id) & (db.academic_course_assignation.carnet==academic_var.id)).select()
        period_id = str(cperiod.id)

    if (auth.has_membership('Student') or auth.has_membership('Teacher')):
        coursesAdmin = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == period_id) & (db.user_project.project==db.project.id) ).select()
        temp = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.project==db.project.id) ).select(db.user_project.period ,distinct=True)
        for t in temp:
            exists = False
            for t2 in period_list:
                if str(T(t.period.period.name) + t.period.yearp) == str(T(t2.semester.period.name) + t2.semester.yearp):
                    exists = True
                pass
            pass
            if exists == False:
                period_list2.append(t)
            pass
        pass
    pass


        
    return dict(assignations=assignations,email=auth.user.email,period_id=period_id,period_list=period_list,cperiod=cperiod.id,coursesAdmin=coursesAdmin, period_list2=period_list2)

@auth.requires_login()
@auth.requires(auth.has_membership('Student') or auth.has_membership('Teacher') or auth.has_membership('Academic'))
def inbox_mails_load():
    import cpfecys
    #request.vars['email']
    #If emisor username change... error of reload
    try:
        if request.vars['operation'] == "mails_list":
            year_var = db.period_year(db.period_year.id==request.vars['period_id'])
            period_var = db.period(db.period.id==year_var.period)
            project_var = db.project(db.project.id==request.vars['project_id'])
                        
            mails = db((db.notification_general_log4.yearp==year_var.yearp) & (db.notification_general_log4.period==period_var.name) & (db.notification_general_log4.course==project_var.name)).select()
            
            return dict(mails = mails, auth_user = auth.user.id)    

        if request.vars['operation'] == "view_mail":
            if db((db.read_mail.id_auth_user == auth.user.id) & (db.read_mail.id_mail == request.vars['mail_id']) ).select().first() == None:
                db.read_mail.insert(id_auth_user = auth.user.id,
                                id_mail  = request.vars['mail_id'])
            mail_var = db.notification_general_log4(db.notification_general_log4.id==request.vars['mail_id'])
            user_var = db.auth_user(db.auth_user.username==mail_var.emisor)
        return dict(mail = mail_var, emisor = user_var)
    except:
        return dict(mail = "", emisor = "")

@auth.requires_login()
@auth.requires(auth.has_membership('Student') or auth.has_membership('Teacher') or auth.has_membership('Academic'))
def inbox_student_mails_load():
    import cpfecys
    #request.vars['email']
    #If emisor username change... error of reload
    try:
        if request.vars['operation'] == "mails_list":
            year_var = db.period_year(db.period_year.id==request.vars['period_id'])
            period_var = db.period(db.period.id==year_var.period)
            project_var = db.project(db.project.id==request.vars['project_id'])
                        
            mails = db((db.academic_send_mail_log.yearp==year_var.yearp) & (db.academic_send_mail_log.period==period_var.name) & (db.academic_send_mail_log.course==project_var.name)).select()
            mails2 = db((db.notification_general_log4.yearp==year_var.yearp) & (db.notification_general_log4.period==period_var.name) & (db.notification_general_log4.course==project_var.name)).select()

            return dict(mails = mails,  mails2 = mails2, auth_user = auth.user.id)    

        if request.vars['operation'] == "view_mail":
            if db((db.read_mail_student.id_auth_user == auth.user.id) & (db.read_mail_student.id_mail == request.vars['mail_id']) ).select().first() == None:
                db.read_mail_student.insert(id_auth_user = auth.user.id,
                                id_mail  = request.vars['mail_id'])
            mail_var = db.academic_send_mail_log(db.academic_send_mail_log.id==request.vars['mail_id'])
            user_var = db.auth_user(db.auth_user.username==mail_var.emisor)
        return dict(mail = mail_var, emisor = user_var)
    except:
        return dict(mail = "", emisor = "")

@auth.requires_login()
@auth.requires(auth.has_membership('Student') or auth.has_membership('Teacher') or auth.has_membership('Academic'))
def send_mail():        
    import cpfecys
    cperiod = cpfecys.current_year_period()
    period_id = cperiod.id
    period_list = []
    if (request.args(0) == 'send'):
        email = request.vars['mail']
        if email != None:
            name = request.vars['name']
            message = request.vars['message']
            subject = request.vars['subject']
            remessage = request.vars['remessage']
            resub = request.vars['resub']
            retime = request.vars['retime']
            var_project_name = request.vars['var_project_name']
            if message != '' and subject != '':
                fail = reply_mail_with_email(email,message, remessage, retime, resub, subject, cperiod, var_project_name)
                if fail > 0:
                    response.flash = T('Sent Error')
                else:
                    response.flash = T('Mail Sent')                
            else:
                response.flash = T('Fill all fields of the mail')
            return dict(email=email,name=name,remessage=remessage,retime=retime,resub=resub,var_project_name=var_project_name)
        else:
            list_users = request.vars['list_users']
            message = request.vars['message']
            subject = request.vars['subject']
            var_course = request.vars['var_course']
            
            if list_users!= None and var_course != '' and message != '' and subject != '':
                fail = send_mail_to_users(list_users, message, subject, cperiod.period.name, cperiod.yearp, var_course)
                if fail > 0:
                    response.flash = T('Sent Error')
                else:
                    response.flash = T('Mail Sent')                
            else:
                response.flash = T('Fill all fields of the mail')
            academic_var = db.academic(db.academic.id_auth_user==auth.user.id) 
            
            assignations = []
             
            assignations = db((db.academic_course_assignation.semester==period_id) & (db.academic_course_assignation.carnet==academic_var.id)).select()
            period_list = db(db.academic_course_assignation.carnet==academic_var.id).select(db.academic_course_assignation.semester,distinct=True)
            return dict(email=None,assignations=assignations,cperiod=cperiod,period_list = period_list, period_id = period_id)
        
    else:
        if (request.args(0) == 'period'):
            period_id = subject = request.vars['semester_id']
        if request.vars['mail'] != None:
            email = request.vars['mail']          
            name = request.vars['name']       
            remessage = request.vars['remessage']
            retime = request.vars['retime']
            resub = request.vars['resub']
            project_var = db.project(db.project.id==request.vars['var_project_id'])
            var_project_name = project_var.name
            return dict(email=email,name=name,remessage=remessage,retime=retime,resub=resub,var_project_name=var_project_name)
        else:
            academic_var = db.academic(db.academic.id_auth_user==auth.user.id)        
            assignations = db((db.academic_course_assignation.semester==period_id) & (db.academic_course_assignation.carnet==academic_var.id)).select()
            period_list = db(db.academic_course_assignation.carnet==academic_var.id).select(db.academic_course_assignation.semester,distinct=True)
            return dict(email=None,assignations=assignations,cperiod=cperiod,period_list = period_list, period_id = period_id)
            

@auth.requires_login()
@auth.requires_membership('Academic')
def sent_mails():        
    import cpfecys
    cperiod = cpfecys.current_year_period()

    academic_var = db.academic(db.academic.id_auth_user==auth.user.id)        
    period_list = db(db.academic_course_assignation.carnet==academic_var.id).select(db.academic_course_assignation.semester,distinct=True)

    select_form = FORM(INPUT(_name='semester_id',_type='text'))

    if select_form.accepts(request.vars,formname='select_form'):
        assignations = db((db.academic_course_assignation.semester==str(select_form.vars.semester_id)) & (db.academic_course_assignation.carnet==academic_var.id)).select()
        period_id = str(select_form.vars.semester_id)
    else:
        assignations = db((db.academic_course_assignation.semester==cperiod.id) & (db.academic_course_assignation.carnet==academic_var.id)).select()
        period_id = str(cperiod.id)

    return dict(assignations=assignations,email=auth.user.email,period_id=period_id,period_list=period_list,cperiod=cperiod.id)


@auth.requires_login()
def register_mail():
    notices=None    
    if request.vars['project'] != None:
        project = request.vars['project']
        semester = request.vars['period_id']        
        yearp_var = db(db.period_year.id==semester).select().first()
        project_name = db(db.project.id==project).select().first()
        notices  = db((db.academic_send_mail_log.emisor==auth.user.username) & (db.academic_send_mail_log.course==project_name.name)&(db.academic_send_mail_log.period==yearp_var.period.name)&(db.academic_send_mail_log.yearp==yearp_var.yearp)).select()
    return dict(notices=notices)

@auth.requires_login()
def register_mail_detail():
    if request.vars['notice'] != None:
        mail_var = db(db.academic_send_mail_log.id==request.vars['notice']).select().first()         
        listadoC=db((db.academic_send_mail_detail.academic_send_mail_log==mail_var.id)).select()
    
    return dict(mail_var=mail_var,listadoC=listadoC)
            
            
@auth.requires_login()
def reply_mail_with_email(email, message, remessage, retime, resub ,subject, semester, project_name):  
    
    message = message.replace("\n","<br>")
    period = T(semester.period.name)+' '+str(semester.yearp) 
    coursesAdmin = None
    if (auth.has_membership('Student') or auth.has_membership('Teacher')):
        project = db(db.project.name==project_name).select().first()
        if project == None:
            session.flash = T('Not valid Action.')
            redirect(URL('default', 'index'))
        else:
            coursesAdmin = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == semester.id) & (db.user_project.project==db.project.id) ).select()
    
    

    messageC = '<html>' + message 
    if ((coursesAdmin is None) and auth.has_membership('Academic')):
        messageC = messageC +'<br><br>Estudiante: '+ auth.user.first_name +' '+ auth.user.last_name +'<br>Carnet: '+auth.user.username+'<br>Correo: '+auth.user.email+'<br>'
    elif (auth.has_membership('Student') or auth.has_membership('Teacher')) and coursesAdmin != None:
        messageC = messageC +'<br><br>'+ auth.user.first_name +' '+ auth.user.last_name + '<br>'
    else:
        session.flash = T('Not valid Action.')
        redirect(URL('default', 'index'))
    messageC = messageC + project_name+"<br>"+str(period)+'<br>Sistema de Seguimiento de La Escuela de Ciencias y Sistemas<br> Facultad de Ingeniería - Universidad de San Carlos de Guatemala'
    messageC = messageC + '<br><br><hr style="width:100%;"><b><i>Respuesta al mensaje enviado el '+ retime +':</i></b><br><table><tr><td><i><b>Asunto:</b></td><td>'+resub+ '</td></tr></table></i></html>'
    control = 0
    was_sent = mail.send(to='dtt.ecys@dtt-ecys.org',subject=subject,message=messageC, bcc=email)

    if ((coursesAdmin is None) and auth.has_membership('Academic')):        
        row = db.academic_send_mail_log.insert(subject=subject,
                                    sent_message=message,
                                    emisor=auth.user.username,
                                    course=project_name,
                                    yearp=semester.yearp,
                                    period=semester.period.name,
                                    mail_state=str(was_sent))

        email_list =str(email).split(",")
        for email_temp in email_list:
            user_var = db((db.auth_user.email == email_temp)).select().first()

            if user_var != None:
                username_var = user_var.username
            else:
                username_var = 'None'
            db.academic_send_mail_detail.insert(academic_send_mail_log=row,
                                                username = username_var,
                                                email = email_temp)
    elif (auth.has_membership('Student') or auth.has_membership('Teacher')) and coursesAdmin != None:
        row = db.notification_general_log4.insert(subject=subject,
                                        sent_message=message,
                                        emisor=auth.user.username,
                                        course=project_name,
                                        yearp=semester.yearp,
                                        period=semester.period.name)
        
        user_var = db((db.auth_user.email == email)).select().first()

        if user_var != None:
            username_var = user_var.username
        else:
            user_var = db((db.academic.email == email)).select().first()
            if user_var != None:
                username_var = user_var.carnet
            else:
                username_var = 'None'
        db.notification_log4.insert(destination = email, 
                                    result_log =str(was_sent), 
                                    username = username_var,
                                    success = str(was_sent), 
                                    register=row)    
    
    if was_sent==False:
        control=control+1
    
    return control

@auth.requires_login()
def send_mail_to_users(users, message, subject, semester,year, project_name):  
    
    message = message.replace("\n","<br>")
    period = T(semester)+' '+str(year)
    
    academic_var = db.academic(db.academic.id_auth_user==auth.user.id)

    messageC = '<html>' + message  +'<br><br>Estudiante: '+ auth.user.first_name +' '+ auth.user.last_name +'<br>Carnet: '+auth.user.username +'<br>Correo: '+auth.user.email+'<br>'+auth.user.username+"<br>"+str(period)+'<br>Sistema de Seguimiento de La Escuela de Ciencias y Sistemas<br> Facultad de Ingeniería - Universidad de San Carlos de Guatemala </html>'    
    control = 0

    
    
    dest=[]
    students = users
    try:
        students.append(-1)
        students.remove(-1)
        for student in students:
            dest.append(student)
        #consultar a la base de datos para obtener a los usuarios a los que enviaremos
        user1 = db(db.auth_user.id.belongs(dest)).select()
    except:
        #consultar a la base de datos para obtener a los usuarios a los que enviaremos
        user1 = db(db.auth_user.id==users).select()
    
    email_list = None
    email_list_log = ""

    if user1 != None:
        for user in user1:
            if user.email != None and user.email != '':
                if email_list == None:
                    email_list = []
                    email_list.append(user.email)
                    email_list_log = str(user.email)

                else:
                    email_list.append(user.email)
                    email_list_log = email_list_log + "," + str(user.email)

    was_sent = mail.send(to='dtt.ecys@dtt-ecys.org',subject=subject,message=messageC, bcc=email_list)
    row = db.academic_send_mail_log.insert(subject=subject,
                                    sent_message=message,
                                    emisor=auth.user.username,
                                    course=project_name,
                                    yearp=year,
                                    period=semester,
                                    mail_state=str(was_sent))

    email_list =str(email_list_log).split(",")
    for email_temp in email_list:
        user_var = db((db.auth_user.email == email_temp)).select().first()

        if user_var != None:
            username_var = user_var.username
        else:
            username_var = 'None'
        db.academic_send_mail_detail.insert(academic_send_mail_log=row,
                                            username = username_var,
                                            email = email_temp)
    
    #if was_sent==False:
    #    control=control+1
    
    return control

