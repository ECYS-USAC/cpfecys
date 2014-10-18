@auth.requires_login()
@auth.requires(auth.has_membership('Student') or auth.has_membership('Teacher') or auth.has_membership('Super-Administrator') or auth.has_membership('Academic') or auth.has_membership('Ecys-Administrator'))
def courses_list():
    area = db(db.area_level.name=='DTT Tutor Académico').select().first()
    coursesAdmin = None
    countcoursesAdmin = db.user_project.id.count()
    countcoursesAdminT = 0
    coursesStudent = None
    countcoursesStudent = db.academic_course_assignation.id.count()
    coursesStudentT = 0
    

    import cpfecys
    #Obtain the current period of the system and all the register periods
    period = cpfecys.current_year_period()
    periods = db(db.period_year).select()

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

    #Check if the period is change
    if request.vars['period'] is None:
        period = cpfecys.current_year_period()
        periods = db(db.period_year).select()
    else:
        if request.vars['period']!='':
            period = request.vars['period']
            period = db(db.period_year.id==period).select().first()
        else:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

    response.view='activity_control/courses_list.html'
    if auth.has_membership('Super-Administrator'):
        coursesAdmin = db(db.project.area_level==area.id).select()
    elif auth.has_membership('Teacher'):
        coursesAdmin = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == period.id) & (db.user_project.project==db.project.id) & (db.project.area_level==area.id)).select()
    elif auth.has_membership('Student'):
        coursesAdmin = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == period.id) & (db.user_project.project==db.project.id) & (db.project.area_level==area.id)).select(countcoursesAdmin).first()
        countcoursesAdminT = coursesAdmin[countcoursesAdmin]
        coursesAdmin = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == period.id) & (db.user_project.project==db.project.id) & (db.project.area_level==area.id)).select()        

        academicCourse = db(db.academic.carnet==auth.user.username).select().first()
        if academicCourse is not None:
            coursesStudent = db((db.academic_course_assignation.carnet == academicCourse.id) & (db.academic_course_assignation.semester == period.id) & (db.academic_course_assignation.assignation==db.project.id) & (db.project.area_level==area.id)).select(countcoursesStudent).first()
            coursesStudentT = coursesStudent[countcoursesStudent]
            coursesStudent = db((db.academic_course_assignation.carnet == academicCourse.id) & (db.academic_course_assignation.semester == period.id) & (db.academic_course_assignation.assignation==db.project.id) & (db.project.area_level==area.id)).select()
    elif auth.has_membership('Academic'):
        academicCourse = db(db.academic.carnet==auth.user.username).select().first()
        if academicCourse is not None:
            coursesStudent = db((db.academic_course_assignation.carnet == academicCourse.id) & (db.academic_course_assignation.semester == period.id) & (db.academic_course_assignation.assignation==db.project.id) & (db.project.area_level==area.id)).select(countcoursesStudent).first()
            coursesStudentT = coursesStudent[countcoursesStudent]
            coursesStudent = db((db.academic_course_assignation.carnet == academicCourse.id) & (db.academic_course_assignation.semester == period.id) & (db.academic_course_assignation.assignation==db.project.id) & (db.project.area_level==area.id)).select()
    else:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))



    return dict(coursesAdmin = coursesAdmin, countcoursesAdminT=countcoursesAdminT, coursesStudent=coursesStudent, coursesStudentT=coursesStudentT, split_name=split_name, split_section=split_section, periods=periods,period=period,periodo=period)


@auth.requires_login()
@auth.requires(auth.has_membership('Student') or auth.has_membership('Teacher') or auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
def students_control():
    #vars
    year = None
    project_var = None
    #Check if the period is correct
    if request.vars['period'] is None or request.vars['period']=='':
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    else:
        year = request.vars['period']
        year = db(db.period_year.id==year).select().first()
        if year is None:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))


    project_var = request.vars['project']
    
    project_select = db(db.project.id==project_var).select().first()

    if auth.has_membership('Super-Administrator') == False and auth.has_membership('Ecys-Administrator') == False :
        assigantion = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == year.id) & (db.user_project.project == project_var)).select().first()
        
        if assigantion is None:
            academic_var = db(db.academic.carnet==auth.user.username).select().first()
            try:
                academic_assig = db((db.academic_course_assignation.carnet == academic_var.id) & (db.academic_course_assignation.semester == year.id) & (db.academic_course_assignation.assignation==project_var) ).select().first()
                
                if academic_assig is None:
                    session.flash=T('Not valid Action.')
                    redirect(URL('default','index'))
                
                    
            except:
                session.flash=T('Not valid Action.')
                redirect(URL('default','index'))
        
    return dict(project = project_var, year = year.id , name = project_select.name, nameP=(T(year.period.name)+" "+str(year.yearp)))



#**************************************************************************************************************************************************************************
#**************************************************************************************************************************************************************************
#************************************************************************************************************************************************************************
#*******************grades********************************************************************************************************************************************

@auth.requires_login()
@auth.requires(auth.has_membership('Student') or auth.has_membership('Teacher') or auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
def control_students_grades():
    id_activity = role = request.vars['activity']
    id_project = role = request.vars['project']
    id_year = role = request.vars['year']

    var_period = db(db.period_year.id==id_year).select().first()
    if not var_period:
        session.flash = T('Not valid Action.')
        redirect(URL('default', 'index'))

    var_activity = db(db.course_activity.id==id_activity).select().first()
    if not var_activity:
        session.flash = T('Not valid Action.')
        redirect(URL('default', 'index'))

    var_project = db(db.project.id==id_project).select().first()
    if not var_project:
        session.flash = T('Not valid Action.')
        redirect(URL('default', 'index'))

    course_ended_var = db((db.course_ended.project==var_project.id) & (db.course_ended.period==var_period.id) ).select().first()

    if course_ended_var != None:
        if course_ended_var.finish == True:
            session.flash = T('Not valid Action.')
            redirect(URL('default', 'index'))
    

    if auth.has_membership('Super-Administrator') == False and auth.has_membership('Ecys-Administrator') == False :
        assigantion = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == var_period.id) & (db.user_project.project == var_project.id)).select().first()
        #exception_query = db(db.course_laboratory_exception.project == id_project).select().first()
        #if exception_query is None:
        #    exception_s_var = False
        #    exception_t_var = False
        #else:
        #    exception_t_var = exception_query.t_edit_lab
        #    exception_s_var = exception_query.s_edit_course
        #if (assigantion is None): #or (auth.has_membership('Teacher') and var_activity.laboratory == True and exception_t_var == False) or (auth.has_membership('Student') and var_activity.laboratory == False and exception_s_var == False):
        #    session.flash=T('You do not have permission to view course requests')
        #    redirect(URL('default','index'))
        
    if var_activity.laboratory == True:
        academic_assig =  db((db.academic_course_assignation.assignation==id_project) & (db.academic_course_assignation.semester==id_year) &  (db.academic_course_assignation.laboratorio==True)).select()
    else:
        academic_assig =  db((db.academic_course_assignation.assignation==id_project) & (db.academic_course_assignation.semester==id_year)).select()

    #Permition to add grades
    exception_query = db(db.course_laboratory_exception.project == id_project).select().first()
    exception_s_var = False
    exception_t_var = False
    no_menu=True
    request_change_var=False

    if exception_query is not None:
        exception_t_var = exception_query.t_edit_lab
        exception_s_var = exception_query.s_edit_course

    if auth.has_membership('Student')==True:
        if var_activity.laboratory == True or exception_s_var == True or var_activity.teacher_permition==True or var_activity.course_activity_category.teacher_permition==True:
            if var_activity.laboratory == True:
                from datetime import datetime
                comparacion = T(var_period.period.name)+" "+str(var_period.yearp)
                controlP = db((db.student_control_period.period_name==comparacion)).select().first()

                maximTimeGrade = db.executesql('SELECT DATE_ADD(\''+str(var_activity.date_finish)+'\', INTERVAL '+str(controlP.timeout_income_notes)+' Day) as fechaMaxGrade;',as_dict=True)
                dateGrade0=''
                for d0 in maximTimeGrade:
                    dateGrade0=d0['fechaMaxGrade']

                if str(datetime.now()) <= str(dateGrade0):
                    request_change_var=True
            else:
                request_change_var=True
    elif auth.has_membership('Teacher')==True:
        if var_activity.laboratory == True:
            if exception_t_var == True:
                request_change_var=True
        else:
            request_change_var=True
    elif auth.has_membership('Ecys-Administrator')==True:
        request_change_var=True
    elif auth.has_membership('Super-Administrator')==True:
        request_change_var=True
    
    if request_change_var == False:
        request_change_var = True
    else:
        request_change_var = False


    return dict(academic_assig=academic_assig, var_period=var_period, var_activity=var_activity, var_project=var_project, request_change_var =request_change_var)


@auth.requires_login()
@auth.requires(auth.has_membership('Student') or auth.has_membership('Teacher') or auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
def grades():
    id_activity = request.vars['activity']
    id_project = request.vars['project']
    id_year = request.vars['year']

    var_period = db(db.period_year.id==id_year).select().first()
    if not var_period:
        session.flash = T('Not valid Action.')
        redirect(URL('default', 'index'))

    var_activity = db(db.course_activity.id==id_activity).select().first()
    if not var_activity:
        session.flash = T('Not valid Action.')
        redirect(URL('default', 'index'))

    var_project = db(db.project.id==id_project).select().first()
    if not var_project:
        session.flash = T('Not valid Action.')
        redirect(URL('default', 'index'))

    if var_activity.laboratory == True:
        academic_assig =  db((db.academic_course_assignation.assignation==id_project) & (db.academic_course_assignation.semester==id_year) &  (db.academic_course_assignation.laboratorio==True)).select()
    else:
        academic_assig =  db((db.academic_course_assignation.assignation==id_project) & (db.academic_course_assignation.semester==id_year)).select()

    rol_log=''
    if auth.has_membership('Ecys-Administrator')==True:
        rol_log='Ecys-Administrator'
    elif auth.has_membership('Super-Administrator')==True:
        rol_log='Super-Administrator'
    elif auth.has_membership('Teacher')==True:
        rol_log='Teacher'
    elif auth.has_membership('Student')==True:
        rol_log='Student'
    pass

    #Request change
    exist_request_change = False
    if db((db.request_change_grades.activity==var_activity.id)&(db.request_change_grades.status=='pending')).select().first() != None:
        exist_request_change = True


    #Permition to add grades
    exception_query = db(db.course_laboratory_exception.project == id_project).select().first()
    exception_s_var = False
    exception_t_var = False
    no_menu=True
    request_change_var=False

    if exception_query is not None:
        exception_t_var = exception_query.t_edit_lab
        exception_s_var = exception_query.s_edit_course

    if auth.has_membership('Student')==True:
        if var_activity.laboratory == True or exception_s_var == True or var_activity.teacher_permition==True or var_activity.course_activity_category.teacher_permition==True:
            if var_activity.laboratory == True:
                from datetime import datetime
                comparacion = T(var_period.period.name)+" "+str(var_period.yearp)
                controlP = db((db.student_control_period.period_name==comparacion)).select().first()

                maximTimeGrade = db.executesql('SELECT DATE_ADD(\''+str(var_activity.date_finish)+'\', INTERVAL '+str(controlP.timeout_income_notes)+' Day) as fechaMaxGrade;',as_dict=True)
                dateGrade0=''
                for d0 in maximTimeGrade:
                    dateGrade0=d0['fechaMaxGrade']

                if str(datetime.now()) <= str(dateGrade0):
                    request_change_var=True
            else:
                request_change_var=True
    elif auth.has_membership('Teacher')==True:
        if var_activity.laboratory == True:
            if exception_t_var == True:
                request_change_var=True
        else:
            request_change_var=True
    elif auth.has_membership('Ecys-Administrator')==True:
        request_change_var=True
    elif auth.has_membership('Super-Administrator')==True:
        request_change_var=True
    
    if request_change_var == False:
        request_change_var = True
    else:
        request_change_var = False

    add_grade_flash = False
    add_grade_error = False
    message_var = ""
    message_var2 = ""
    alert_message = False

    carnet_list = str(request.vars['carnet']).split(',')
    grade_list = str(request.vars['grade']).split(',')
    cont_temp = 0
    #<!---------------------------INSERT---------------------------->
    if (request.vars['op'] == "add_grade") | (request.vars['op'] == "add_grade_list"):
        for carnet_id in carnet_list: 
            if (request.vars['op'] == "add_grade"):
                carnet_list = request.vars['carnet']
                grade_list = request.vars['grade']
                request.vars['grade'] = grade_list
            else:
                request.vars['grade'] = grade_list[cont_temp]
                cont_temp = cont_temp+1
            request.vars['carnet'] = carnet_id
        
        
            try:
                academic_var =  db(db.academic.carnet==request.vars['carnet']).select().first()

                assig_var =  db((db.academic_course_assignation.assignation==var_project.id) & (db.academic_course_assignation.semester==var_period.id) & (db.academic_course_assignation.carnet == academic_var.id)).select().first()
                  #--------------------------------------------INSERT GRADE-------------------------------------
                if request_change_var == False:
                    if exist_request_change == True:
                        add_grade_error = True
                        message_var = T('Can not make operation because there is a pending request change. Please resolve it before proceeding.')
                    else:
                        grade_before = db((db.grades.academic_assignation==assig_var.id) & (db.grades.activity==var_activity.id) ).select().first() 
                        if grade_before is None:
                            if (var_activity.laboratory == False) | (assig_var.laboratorio == var_activity.laboratory):
                                grade = db.grades.insert(academic_assignation = assig_var.id,
                                                activity = var_activity.id,
                                                grade =  request.vars['grade'])

                                if grade != None:
                                    #--------------------------------------------log-------------------------------------
                                    db.grades_log.insert(user_name = auth.user.username,
                                                    roll = rol_log,
                                                    operation_log = 'insert',
                                                    academic_assignation_id = assig_var.id,
                                                    academic = assig_var.carnet.carnet,
                                                    project = assig_var.assignation.name,
                                                    activity = var_activity.name,
                                                    activity_id = var_activity.id,
                                                    category = var_activity.course_activity_category.category.category,
                                                    period = T(assig_var.semester.period.name),
                                                    yearp = assig_var.semester.yearp,
                                                    after_grade = request.vars['grade'],
                                                    description = T('Inserted from Grades page')
                                                     )
                                    if request.vars['op'] == "add_grade":
                                        add_grade_flash = True
                                        message_var = T('Grade added') + " | Carnet: "+ str(academic_var.carnet) +" "+ T('Grade')+ ": " + str(grade.grade)
                                    pass
                                else:
                                    add_grade_error = True
                                    message_var = T('Failed to add grade') + " | Carnet: "+ str(academic_var.carnet)+" " + T('Grade')+": " + str(grade.grade)
                                pass  #----grade!=None---
                            else:
                                add_grade_error = True
                                message_var = T('Failed to add grade') + " | Carnet: "+ str(academic_var.carnet)+" " + T('Grade')+": " + str(grade.grade)
                            pass  #----grade!=None---
                        else:
                            add_grade_error = True
                            message_var = T('Failed to add grade') + " | Carnet: "+ request.vars['carnet']+" " + T('Already have an associated grade')
                        pass #-------grade_before-is-None---  
                    pass  #------exist_request_change-==-True----
                  #--------------------------------------------INSERT REQUEST-------------------------------------
                else:
                    grade_before = db((db.grades.academic_assignation==assig_var.id) & (db.grades.activity==var_activity.id) ).select().first() 
                    
                    var_grade_before = None
                    var_operation = 'insert'
                    if grade_before != None:
                        var_grade_before = grade_before.grade
                        var_operation = 'update'
                    pass
                    
                    request_change = db((db.request_change_grades.activity== var_activity.id) & (db.request_change_grades.status=='pending') ).select().first() 
                    if request_change is None:
                        grade = db.request_change_grades.insert(user_id = auth.user.id,
                                                              activity = var_activity.id,
                                                              status =  'pending',
                                                              roll = rol_log,
                                                              period = assig_var.semester.id,
                                                              project = assig_var.assignation.id,
                                                              description = request.vars['description_var'])
                    
                        #-------------------------------------LOG-----------------------------------------------
                        log_id = db.request_change_g_log.insert(r_c_g_id = grade,
                                                      username = auth.user.username,
                                                      roll = rol_log,
                                                      after_status = 'pending',
                                                      description = request.vars['description_var'],
                                                      description_log = T('Inserted from Grades page'),
                                                      semester = T(assig_var.semester.period.name),
                                                      yearp = assig_var.semester.yearp,
                                                      activity = var_activity.name,
                                                      category = var_activity.course_activity_category.category.category,
                                                      project = assig_var.assignation.name
                                                    )
                    pass #--------request_change-is-None----
                    request_change = db((db.request_change_grades.activity== var_activity.id) & (db.request_change_grades.status=='pending') ).select().first() 
                    rq_grade = db.request_change_grades_detail.insert(request_change_grades = request_change.id,
                                                                          academic_assignation = assig_var.id,
                                                                          before_grade = var_grade_before,
                                                                          operation_request = var_operation,
                                                                          after_grade = request.vars['grade'])

                    log_id = db((db.request_change_g_log.r_c_g_id== request_change.id) & (db.request_change_g_log.after_status=='pending') ).select().first() 

                    db.request_change_grade_d_log.insert(request_change_g_log = log_id.id,
                                                      operation_request = var_operation,
                                                      academic = academic_var.carnet,
                                                      before_grade = var_grade_before,
                                                      after_grade = request.vars['grade']
                                                      )
                                    
                    #send mail
                    project_name = var_project.name
                    project_id = id_project
                    check = db.user_project(project = project_id, period = var_period.id, assigned_user = auth.user.id)
                    #Message
                    users2 = db((db.auth_user.id==db.user_project.assigned_user)&(db.user_project.period == check.period) & (db.user_project.project==check.project)&(db.auth_membership.user_id==db.user_project.assigned_user)&(db.auth_membership.group_id==3)).select().first()
                    subject="Solicitud de cambio de ponderación - "+project_name
                    message2="<br>Por este medio se le informa que el(la) practicante "+check.assigned_user.first_name+" "+check.assigned_user.last_name+" ha creado una solicitud de cambio en las notas del laboratorio del Curso de \""+project_name+"\"."
                    message2=message2+"<br>Para aceptar o rechazar dicha solicitud dirigirse al control de solicitudes o al siguiente link: " +cpfecys.get_domain()+ "cpfecys/activity_control/solve_request_change_grades?course="+str(project_id)
                    message2=message2+"<br>Saludos.<br><br>Sistema de Seguimiento de La Escuela de Ciencias y Sistemas<br>Facultad de Ingeniería - Universidad de San Carlos de Guatemala</html>"
                    #Send Mail to the Teacher
                    message="<html>catedratico(a) "+users2.auth_user.first_name+" "+users2.auth_user.last_name+" reciba un cordial saludo.<br>"
                    message3=message+message2

                    fail1 = send_mail_to_students(message3,subject,users2.auth_user.email,check,var_period.period.name,var_period.yearp) 
                    if fail1==1:
                        alert_message = True
                        message_var2 = T("Request has been sent") + ". " + T("Sent email to teacher")
                    
                    else:
                        alert_message = True
                        message_var2 = T("Request has been sent") + ". " + T("Failed to send email to teacher")
                        

                pass #-------request_change_var-==-False---
                
                  
            except:
                if academic_var is None:
                    add_grade_error = True
                    message_var = T('Failed to add grade') + " | Carnet: "+ request.vars['carnet'] +" " + T('not exist')
                else:
                    add_grade_error = True
                    message_var = T('Failed to add grade')
                pass
            pass

        pass
    pass
    return dict(academic_assig=academic_assig, 
        var_period=var_period, 
        var_activity=var_activity, 
        var_project=var_project, 
        rol_log=rol_log, 
        request_change_var = request_change_var, 
        exist_request_change = exist_request_change,
        message_var = message_var,
        message_var2 = message_var2,
        alert_message = alert_message,
        add_grade_error = add_grade_error,
        add_grade_flash = add_grade_flash
        )





@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def activity_category():
    query = db.activity_category
    grid = SQLFORM.grid(query, maxtextlength=100,csv=False)
    return dict(grid=grid)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def course_laboratory_exception():
    query = db.course_laboratory_exception
    grid = SQLFORM.grid(query, maxtextlength=100,csv=False)
    return dict(grid=grid)


@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def course_limit_exception():
    query = db.course_limit_exception
    grid = SQLFORM.grid(query, maxtextlength=100,csv=False)
    return dict(grid=grid)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def student_control_period():
    import cpfecys
    year = cpfecys.current_year_period()
    year_semester = db.period(id=year.period)
    grid = SQLFORM.grid(db.student_control_period, maxtextlength=100,csv=False,create=False,deletable=False,)
    return dict(grid=grid)


@auth.requires_login()
def semaphore():
    period = db(db.period_year.id==request.vars['period']).select().first()
    return dict(period=period)

@auth.requires_login()
@auth.requires(auth.has_membership('Student'))
def request_change_weighting():
    import cpfecys
    year = db(db.period_year.id == request.vars['year']).select().first() 
    year_semester = year.period

    assignation = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == year.id) & (db.user_project.project == request.vars['project'])).select().first()
    if assignation is None:
        session.flash = T("Action not allowed")
        redirect(URL('default','index'))    
    check = db(db.project.id == request.vars['project']).select().first()
    
    
    try:
        
        if request.vars['operation'] == "cancel":
            db((db.request_change_weighting.period == year.id) & (db.request_change_weighting.project == request.vars['project']) & ((db.request_change_weighting.status != 'accepted') & (db.request_change_weighting.status != 'rejected'))).delete()
            response.flash = T("Request has been canceled")
        if (request.args(0) == 'request'):
            if str(request.vars['description']) == "":
                response.flash = "Error. "+ T("Please enter a description")
            else:
                
                if session.total_var != 100:
                    if session.total_var != None:
                        response.flash = "Error. "+ T("The sum of the weighting is incorrect") + ": " + str(session.total_var)
                else:
                    
                    temp = db((db.request_change_weighting.period == year.id) & (db.request_change_weighting.project == request.vars['project']) & ((db.request_change_weighting.status != 'accepted') & (db.request_change_weighting.status != 'rejected')) ).select().first()
                    db((db.request_change_weighting.id == temp.id) ).update(status = 'pending',
                                            description = str(request.vars['description']),
                                            date_request = datetime.datetime.now())
                    #LOG
                    temp2 = db.request_change_w_log.insert(r_c_w_id=temp.id,
                                                    username=auth.user.username,
                                                    roll='Student',
                                                    before_status='edit',
                                                    after_status='pending',
                                                    description=str(request.vars['description']),
                                                    semester=year_semester.name,
                                                    yearp=str(year.yearp),
                                                    project=str(check.name))
                    #LOG_DETAIL
                    r_c_w_d_var = db((db.request_change_weighting_detail.request_change_weighting==temp)).select()
                    for var_temp in r_c_w_d_var:
                        if var_temp.operation_request == 'insert':
                            cat_temp = db(db.activity_category.id==var_temp.category).select().first()
                            db.request_change_w_detail_log.insert(request_change_w_log=temp2,
                                                                operation_request=var_temp.operation_request,
                                                                category=cat_temp.category,
                                                                after_grade=var_temp.grade,
                                                                after_specific_grade=var_temp.specific_grade)
                        if var_temp.operation_request == 'delete':
                            cat_temp = db(db.course_activity_category.id==var_temp.course_category).select().first()
                            
                            db.request_change_w_detail_log.insert(request_change_w_log=temp2,
                                                                operation_request=var_temp.operation_request,
                                                                course_category=cat_temp.category.category,
                                                                before_grade=cat_temp.grade,
                                                                before_specific_grade=cat_temp.specific_grade)
                        if var_temp.operation_request == 'update':
                            cat_temp = db(db.course_activity_category.id==var_temp.course_category).select().first()
                            cat_temp2 = db(db.activity_category.id==var_temp.category).select().first()
                            db.request_change_w_detail_log.insert(request_change_w_log=temp2,
                                                                operation_request=var_temp.operation_request,
                                                                course_category=cat_temp.category.category,
                                                                category=cat_temp2.category,
                                                                before_grade=cat_temp.grade,                                                                
                                                                after_specific_grade=var_temp.specific_grade,
                                                                after_grade=var_temp.grade,
                                                                before_specific_grade=cat_temp.specific_grade)

                    project_name = check.name
                    project_id = check.id
                    check = db.user_project(project = check.id, period = year.id, assigned_user = auth.user.id)
                    #Message
                    users2 = db((db.auth_user.id==db.user_project.assigned_user)&(db.user_project.period == check.period) & (db.user_project.project==check.project)&(db.auth_membership.user_id==db.user_project.assigned_user)&(db.auth_membership.group_id==3)).select().first()
                    subject="Solicitud de cambio de ponderación - "+project_name
                    message2="<br>Por este medio se le informa que el(la) practicante "+check.assigned_user.first_name+" "+check.assigned_user.last_name+" ha creado una solicitud de cambio en la ponderación del laboratorio del Curso de \""+project_name+"\"."
                    message2=message2+"<br>Para aceptar o rechazar dicha solicitud dirigirse al control de solicitudes o al siguiente link: " +cpfecys.get_domain()+ "cpfecys/activity_control/solve_request_change_weighting?course="+str(project_id)
                    message2=message2+"<br>Saludos.<br><br>Sistema de Seguimiento de La Escuela de Ciencias y Sistemas<br>Facultad de Ingeniería - Universidad de San Carlos de Guatemala</html>"
                    #Send Mail to the Teacher
                    message="<html>catedratico(a) "+users2.auth_user.first_name+" "+users2.auth_user.last_name+" reciba un cordial saludo.<br>"
                    message3=message+message2
                    fail1 = send_mail_to_students(message3,subject,users2.auth_user.email,check,year_semester.name,year.yearp) 
                    if fail1==1:
                        response.flash = T("Request has been sent") + " - " + T("Sent email to teacher")
                    else:
                        response.flash = T("Request has been sent") + " - " + T("Failed to send email to teacher")
                    return dict(name = project_name,
                        semester = year_semester.name,
                        year = year.yearp,
                        semestre2 = year,
                        project = request.vars['project'],
                        assignation=assignation)

    except:
        None

    session.total_var = None
    return dict(name = check.name,
        semester = year_semester.name,
        year = year.yearp,
        semestre2 = year,
        project = request.vars['project'],
        assignation=assignation)

@auth.requires_login()
@auth.requires(auth.has_membership('Student') or auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator') or auth.has_membership('Teacher'))
def request_change_weighting_load():
    session.total_var = None
    import cpfecys
    year = db(db.period_year.id == request.vars['year']).select().first() 
    year_semester = year.period
    project_id = request.vars['project']
    change_id = request.vars['change_id']
    op = request.vars['op']
    change = None
    if op != "select_change":
        if change_id is None:
            change_activity = db((db.requestchange_activity.semester == year.id) & (db.requestchange_activity.course == project_id) & (db.requestchange_activity.status == 'Pending')).select().first()
            change = db((db.request_change_weighting.period == year.id) & (db.request_change_weighting.project == project_id) & ((db.request_change_weighting.status != 'accepted') & (db.request_change_weighting.status != 'rejected'))).select().first()
            if change is None:
                if change_activity is None:
                    change = db.request_change_weighting.insert(user_id=auth.user.id,
                                                            roll='Student',
                                                            status='edit',
                                                            period=year.id,
                                                            project=project_id)
                else:
                    response.flash = T("Unable to send the request as long as other pending requests")
                    return '<script type="text/javascript">$("#div_request_detail").css("display", "none");</script>'
                
            else:
                if change_activity != None:
                    response.flash = T("Unable to send the request as long as other pending requests")
                    db(db.request_change_weighting.id == change.id).delete()
                    return '<script type="text/javascript">$("#div_request_detail").css("display", "none");</script>'
                
                
        else:
            change = db((db.request_change_weighting.id == change_id)).select().first()
    
    assignation = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == year.id) & (db.user_project.project == project_id)).select().first()
    if assignation is None:
        session.flash = T("Action not allowed")
        redirect(URL('default','index'))    
    check = db(db.project.id == request.vars['project']).select().first()

    return dict(name = check.name,
        semester = year_semester.name,
        year = year.yearp,
        semestre2 = year,
        project = request.vars['project'],
        assignation = assignation,
        op = op,
        change = change)

@auth.requires_login()
@auth.requires(auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator') or auth.has_membership('Teacher'))
def solve_request_change_weighting():
    import cpfecys
    #Obtain the course that want to view the request
    courseCheck = request.vars['course']

    #Check that the request vars contain something
    if (courseCheck is None):
        redirect(URL('default','index'))
    else:
        #Check if teacher or other role
        course=None
        if auth.has_membership('Teacher'):
            course = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == cpfecys.current_year_period().id) & (db.user_project.project==courseCheck)).select().first()
            if (course is None):
                session.flash=T('You do not have permission to view course requests')
                redirect(URL('default','index'))
        else:
            course=db.project(id=courseCheck)

        #Check that the course exist
        name=None
        if (course is None):
            redirect(URL('default','index'))
        else:
            if auth.has_membership('Teacher'):
                name=course.project.name
            else:
                name=course.name

        currentyear_period = cpfecys.current_year_period()
        return dict(name = name,
                    semester = currentyear_period.period.name,
                    semestre2 = currentyear_period,
                    year = currentyear_period.yearp,
                    course=courseCheck)

@auth.requires_login()
@auth.requires(auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator') or auth.has_membership('Teacher'))
def solve_request_change_grades():
    import cpfecys
    #Obtain the course that want to view the request
    courseCheck = request.vars['course']

    #Check that the request vars contain something
    if (courseCheck is None):
        redirect(URL('default','index'))
    else:
        #Check if teacher or other role
        course=None
        if auth.has_membership('Teacher'):
            course = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == cpfecys.current_year_period().id) & (db.user_project.project==courseCheck)).select().first()
            if (course is None):
                session.flash=T('You do not have permission to view course requests')
                redirect(URL('default','index'))
        else:
            course=db.project(id=courseCheck)

        #Check that the course exist
        name=None
        if (course is None):
            redirect(URL('default','index'))
        else:
            if auth.has_membership('Teacher'):
                name=course.project.name
            else:
                name=course.name

        currentyear_period = cpfecys.current_year_period()
        return dict(name = name,
                    semester = currentyear_period.period.name,
                    semestre2 = currentyear_period,
                    year = currentyear_period.yearp,
                    course=courseCheck)



@auth.requires_login()
def control_weighting():
    import cpfecys
    year = db(db.period_year.id == request.vars['year']).select().first() 
    year_semester = year.period

    assigantion = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == year.id) & (db.user_project.project == request.vars['project'])).select().first()
    if assigantion is None:
        assigned_to_project = False
    else:
        assigned_to_project = True

    check = db(db.project.id == request.vars['project']).select().first()
    return dict(name = check.name,
        semester = year_semester.name,
        year = year.yearp,
        semestre2 = year,
        project = request.vars['project'],
        assigned_to_project = assigned_to_project)
    
@auth.requires_login()
def students_control_full():
    import cpfecys
    project = request.vars['project']
    assigantion =None
    year = db(db.period_year.id == request.vars['year']).select().first() 

    project_var = request.vars['project']
    if auth.has_membership('Super-Administrator') == False and auth.has_membership('Ecys-Administrator') == False :
        assigantion = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == year.id) & (db.user_project.project == project_var)).select().first()
        
        if assigantion is None:
            academic_var = db(db.academic.carnet==auth.user.username).select().first()
            try:
                academic_assig = db((db.academic_course_assignation.carnet == academic_var.id) & (db.academic_course_assignation.semester == year.id) & (db.academic_course_assignation.assignation==project_var) ).select().first()
            
                if academic_assig is None:
                    session.flash=T('Not valid Action.')
                    redirect(URL('default','index'))
            except:
                session.flash=T('Not valid Action.')
                redirect(URL('default','index'))
    

    return dict(name = '',
                semester = year.period.name,
                year = year.yearp,
                assigantion=assigantion)

@auth.requires_login()
def control_students_modals():
    import cpfecys
    project = request.vars['project']
    
    year = db(db.period_year.id == request.vars['year']).select().first() 
    
    project_var = db(db.project.id == request.vars['project']).select().first() 
    return dict(semestre2 = year, name=project_var.name)

@auth.requires_login()
def weighting():
    import cpfecys
    project = request.vars['project']
    rol_log=''
    if auth.has_membership('Ecys-Administrator')==True:
        rol_log='Ecys-Administrator'
    elif auth.has_membership('Super-Administrator')==True:
        rol_log='Super-Administrator'
    elif auth.has_membership('Teacher')==True:
        rol_log='Teacher'
    elif auth.has_membership('Student')==True:
        rol_log='Student'
    pass
    project_var = db(db.project.id == project).select().first() 
    year = db(db.period_year.id == request.vars['year']).select().first() 
    assigantion = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == year.id) & (db.user_project.project == project)).select().first()
    return dict(semestre2 = year, project = project, project_variable= project_var,assigantion=assigantion, rol_log = rol_log)



#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
@auth.requires_login()
def control_activity():
    year = db(db.period_year.id == request.vars['year']).select().first() 
    year_semester = year.period
    project = db(db.project.id==request.vars['project']).select().first()

    assigantion = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == year.id) & (db.user_project.project == project.id)).select().first()
    if assigantion is None:
        assigned_to_project = False
    else:
        assigned_to_project = True

    return dict(semester = year_semester.name,
            year = year.yearp,
            semestre2 = year,
            project = project,
            type=request.vars['type'],
            assigned_to_project = assigned_to_project)
@auth.requires_login()
def activity():
    import cpfecys
    #Obteners la asignacion del estudiante
    project = request.vars['project']
    typ = request.vars['type']
    
    year = db(db.period_year.id == request.vars['year']).select().first() 
    assigantion = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == year.id) & (db.user_project.project == project)).select().first()
    if assigantion is None:
        assigned_to_project = False
    else:
        assigned_to_project = True
    
    return dict(semestre2 = year, project = project, type=typ, assigned_to_project = assigned_to_project)

@auth.requires_login()
def control_students_modals2():
    #Obtener la asignacion del estudiante
    project = request.vars['project']
    year = db(db.period_year.id == request.vars['year']).select().first() 
    project_var = db(db.project.id == request.vars['project']).select().first() 
    return dict(semestre2 = year, name=project_var.name, project_var=project_var)

@auth.requires_login()
@auth.requires(auth.has_membership('Student'))
def request_change_activity():
    #Obtener al tutor del proyecto
    check = db.user_project(project = request.vars['project'], period = request.vars['year'], assigned_user = auth.user.id)
    if (check is None):
        redirect(URL('default','index'))

    year = db.period_year(id=check.period)
    year_semester = db.period(id=year.period)

    return dict(name = check.project.name,
                semester = year_semester.name,
                semestre2 = year,
                year = year.yearp,
                assignation=check.id)

@auth.requires_login()
@auth.requires_membership('Student')
def send_mail_to_students(message, subject, user, check, semester, year):
    control = 0
    was_sent = mail.send(to='dtt.ecys@dtt-ecys.org',subject=subject,message=message, bcc=user)
    #MAILER LOG
    db.mailer_log.insert(sent_message = message,
                     destination = user,
                     result_log = str(mail.error or '') + ':' + \
                     str(mail.result),
                     success = was_sent, emisor=str(check.assigned_user.username))
    if was_sent==False:
        control=control+1
    return control


@auth.requires_login()
def requestchangeactivity():
    import datetime
    stateRequest=0
    #Cancel the request made
    if request.args(0) == 'reject':
        Pending = db((db.requestchange_activity.id==int(request.vars['requestID']))&(db.requestchange_activity.status=='Pending')&(db.requestchange_activity.semester==int(request.vars['year']))&(db.requestchange_activity.course==int(request.vars['project']))).select().first()
        if Pending is None:
            session.flash=T('The plan change request has been answered by another user or is there a problem with the request')
        else:
            db(db.requestchange_activity.id==int(request.vars['requestID'])).update(status = 'Rejected', user_resolve = auth.user.id, roll_resolve =  'Student', date_request_resolve =  datetime.datetime.now())
            #Log of request change activity
            Rejected = db(db.requestchange_activity.id==int(request.vars['requestID'])).select().first()
            if Rejected is not None:
                idR = db.requestchange_activity_log.insert(user_request=Rejected.user_id.username, roll_request=Rejected.roll, status='Rejected', user_resolve=Rejected.user_resolve.username, roll_resolve=Rejected.roll_resolve, description=Rejected.description, date_request=Rejected.date_request, date_request_resolve=Rejected.date_request_resolve, category_request=Rejected.course_activity_category.category.category, semester=Rejected.semester.period.name, yearp=Rejected.semester.yearp, course=Rejected.course.name)
                activitiesChange = db(db.requestchange_course_activity.requestchange_activity==Rejected.id).select()
                for actChange in activitiesChange:
                    db.requestchange_course_activity_log.insert(requestchange_activity=idR, operation_request=actChange.operation_request, activity=actChange.activity, name=actChange.name, description=actChange.description, grade=actChange.grade, date_start=actChange.date_start, date_finish=actChange.date_finish)
            session.flash=T('The plan change request has been canceled')
        redirect(URL('activity_control','request_change_activity',vars=dict(project=request.vars['project'], year=request.vars['year'])))


    #Cancel the request without having done
    if request.args(0)=='cancelR':
        if request.vars['year']=='' or request.vars['year'] is None or request.vars['project']=='' or request.vars['project'] is None:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))
        else:
            deleteR = db((db.requestchange_activity.status=='Draft')&(db.requestchange_activity.semester==int(request.vars['year']))&(db.requestchange_activity.course==int(request.vars['project']))).select().first()
            if deleteR is not None:
                db(db.requestchange_activity.id==deleteR.id).delete()
            session.flash=T('The change activities request has been canceled')
            redirect(URL('activity_control','request_change_activity',vars=dict(project=request.vars['project'], year=request.vars['year'])))


    cat = None
    if request.vars['category'] is None or request.vars['category']=='':
        cat=-1
    else:
        cat=db(db.course_activity_category.id==request.vars['category']).select().first()

    year = db.period_year(id=request.vars['year'])
    project = db.project(id=request.vars['project'])
    
    Draft = db((db.requestchange_activity.status=='Draft')&(db.requestchange_activity.semester==year.id)&(db.requestchange_activity.course==project.id)).select().first()

    if request.vars['op'] == "createRequestChangeL":
        if Draft==None:
            stateRequest=-1
        else:
            if Draft.course_activity_category!=int(request.vars['category']):
                stateRequest=-1
            else:
                #Update the request change activity
                db(db.requestchange_activity.id==Draft.id).update(description=request.vars['activity_description_request_var'],status='Pending', date_request = datetime.datetime.now())
                Draft = db((db.requestchange_activity.status=='Pending')&(db.requestchange_activity.semester==year.id)&(db.requestchange_activity.course==project.id)).select().first()
                #Log of request change activity
                idR = db.requestchange_activity_log.insert(user_request=Draft.user_id.username, roll_request='Student', status='Pending', description=request.vars['activity_description_request_var'], date_request=Draft.date_request, category_request=Draft.course_activity_category.category.category, semester=year.period.name, yearp=year.yearp, course=project.name)
                activitiesChange = db(db.requestchange_course_activity.requestchange_activity==Draft.id).select()
                for actChange in activitiesChange:
                    db.requestchange_course_activity_log.insert(requestchange_activity=idR, operation_request=actChange.operation_request, activity=actChange.activity, name=actChange.name, description=actChange.description, grade=actChange.grade, date_start=actChange.date_start, date_finish=actChange.date_finish)
                #Check the user project
                check = db.user_project(project = request.vars['project'], period = request.vars['year'], assigned_user = auth.user.id)
                #Message
                users2 = db((db.auth_user.id==db.user_project.assigned_user)&(db.user_project.period == check.period) & (db.user_project.project==check.project)&(db.auth_membership.user_id==db.user_project.assigned_user)&(db.auth_membership.group_id==3)).select().first()
                try:
                    subject="Solicitud de cambio de actividades - "+project.name
                    
                    message2="<br>Por este medio se le informa que el(la) practicante "+check.assigned_user.first_name+" "+check.assigned_user.last_name+" ha creado una solicitud de cambio de actividades en la categoría \""+Draft.course_activity_category.category.category+"\" dentro de la ponderación de laboratorio del Curso de \""+project.name+"\"."
                    message2=message2+"<br>Para aceptar o rechazar dicha solicitud dirigirse al control de solicitudes o al siguiente link: "
                    message2=message2+"<br>Saludos.<br><br>Sistema de Seguimiento de La Escuela de Ciencias y Sistemas<br>Facultad de Ingeniería - Universidad de San Carlos de Guatemala</html>"

                    #Send Mail to the Teacher
                    message="<html>catedratico(a) "+users2.auth_user.first_name+" "+users2.auth_user.last_name+" reciba un cordial saludo.<br>"
                    message3=message+message2
                    fail1 = send_mail_to_students(message3,subject,users2.auth_user.email,check,year.period.name,year.yearp)
                    #Refresh the var Draft
                    Draft=None
                    if fail1==1:
                        stateRequest=2
                    else:
                        stateRequest=4
                except:
                    stateRequest=2


    requestC=db((db.requestchange_activity.course==project.id)&(db.requestchange_activity.semester==year.id)&(db.requestchange_activity.status=='Pending')).select()
    tempCategories=[]
    tempCategories.append(-1)
    for r in requestC:
        tempCategories.append(int(r.course_activity_category))
    categories = db((db.course_activity_category.assignation==project.id)&(db.course_activity_category.semester==year.id)&(db.course_activity_category.laboratory=='T')&(~db.course_activity_category.id.belongs(tempCategories))).select()
    totalCategories=0
    if categories is not None:
        for c in categories:
            totalCategories=totalCategories+1
    return dict(period=year,
                project=project,
                requestC=requestC,
                categories=categories,
                totalCategories=totalCategories,
                cat=cat,
                Draft=Draft,
                stateRequest=stateRequest)



#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------



@auth.requires_login()
@auth.requires(auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator') or auth.has_membership('Teacher'))
def courses_list_request():
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

    area = db(db.area_level.name=='DTT Tutor Académico').select().first()
    courses_request=None
    if auth.has_membership('Teacher'):
        courses_request = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == cpfecys.current_year_period().id) & (db.user_project.project==db.project.id) & (db.project.area_level==area.id)).select()
    if auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'):
        courses_request = db(db.project.area_level==area.id).select()

    return dict(courses_request = courses_request, 
                split_name=split_name, 
                split_section=split_section,
                semester_id=cpfecys.current_year_period())


@auth.requires_login()
@auth.requires(auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator') or auth.has_membership('Teacher'))
def solve_request_change_activity():
    import cpfecys
    
    import datetime
    #Cancel the request made
    if request.args(0) == 'reject':
        Pending = db((db.requestchange_activity.id==int(request.vars['requestID']))&(db.requestchange_activity.status=='Pending')&(db.requestchange_activity.semester==cpfecys.current_year_period().id)&(db.requestchange_activity.course==int(request.vars['course']))).select().first()
        if Pending is None:
            session.flash=T('The plan change request has been answered by another user or is there a problem with the request')
        else:
            rol_temp=''
            if auth.has_membership('Super-Administrator'):
                rol_temp='Super-Administrator'
            elif auth.has_membership('Ecys-Administrator'):
                rol_temp='Ecys-Administrator'
            else:
                rol_temp='Teacher'

            db(db.requestchange_activity.id==int(request.vars['requestID'])).update(status = 'Rejected', user_resolve = auth.user.id, roll_resolve =  rol_temp, date_request_resolve =  datetime.datetime.now())
            #Log of request change activity
            Rejected = db(db.requestchange_activity.id==int(request.vars['requestID'])).select().first()
            if Rejected is not None:
                idR = db.requestchange_activity_log.insert(user_request=Rejected.user_id.username, roll_request=Rejected.roll, status='Rejected', user_resolve=Rejected.user_resolve.username, roll_resolve=Rejected.roll_resolve, description=Rejected.description, date_request=Rejected.date_request, date_request_resolve=Rejected.date_request_resolve, category_request=Rejected.course_activity_category.category.category, semester=Rejected.semester.period.name, yearp=Rejected.semester.yearp, course=Rejected.course.name)
                activitiesChange = db(db.requestchange_course_activity.requestchange_activity==Rejected.id).select()
                for actChange in activitiesChange:
                    db.requestchange_course_activity_log.insert(requestchange_activity=idR, operation_request=actChange.operation_request, activity=actChange.activity, name=actChange.name, description=actChange.description, grade=actChange.grade, date_start=actChange.date_start, date_finish=actChange.date_finish)
            session.flash=T('The plan change request has been canceled')
        redirect(URL('activity_control','solve_request_change_activity',vars=dict(course=request.vars['course'])))

    #Solve the request made
    if request.args(0) == 'solve':
        Pending = db((db.requestchange_activity.id==int(request.vars['requestID']))&(db.requestchange_activity.status=='Pending')&(db.requestchange_activity.semester==cpfecys.current_year_period().id)&(db.requestchange_activity.course==int(request.vars['course']))).select().first()
        if Pending is None:
            session.flash=T('The plan change request has been answered by another user or is there a problem with the request')
        else:
            rol_temp=''
            if auth.has_membership('Super-Administrator'):
                rol_temp='Super-Administrator'
            elif auth.has_membership('Ecys-Administrator'):
                rol_temp='Ecys-Administrator'
            else:
                rol_temp='Teacher'

            db(db.requestchange_activity.id==int(request.vars['requestID'])).update(status = 'Accepted', user_resolve = auth.user.id, roll_resolve =  rol_temp, date_request_resolve =  datetime.datetime.now())
            #Log of request change activity
            Accepted = db(db.requestchange_activity.id==int(request.vars['requestID'])).select().first()
            if Accepted is not None:
                idR = db.requestchange_activity_log.insert(user_request=Accepted.user_id.username, roll_request=Accepted.roll, status='Accepted', user_resolve=Accepted.user_resolve.username, roll_resolve=Accepted.roll_resolve, description=Accepted.description, date_request=Accepted.date_request, date_request_resolve=Accepted.date_request_resolve, category_request=Accepted.course_activity_category.category.category, semester=Accepted.semester.period.name, yearp=Accepted.semester.yearp, course=Accepted.course.name)
                activitiesChange = db(db.requestchange_course_activity.requestchange_activity==Accepted.id).select()
                for actChange in activitiesChange:
                    #Log request change activity
                    db.requestchange_course_activity_log.insert(requestchange_activity=idR, operation_request=actChange.operation_request, activity=actChange.activity, name=actChange.name, description=actChange.description, grade=actChange.grade, date_start=actChange.date_start, date_finish=actChange.date_finish)
                    #Log and changes in activities
                    if actChange.operation_request=='insert':
                        #Change in activities
                        db.course_activity_log.insert(user_name=auth.user.username, roll=rol_temp, operation_log='insert', course= Accepted.course.name, yearp=cpfecys.current_year_period().yearp, period=cpfecys.current_year_period().period.name, metric='T', after_course_activity_category=Accepted.course_activity_category.category.category, after_name=actChange.name, after_description=actChange.description, after_grade =  actChange.grade, after_laboratory = 'T', after_teacher_permition = 'F', after_date_start = actChange.date_start, after_date_finish = actChange.date_finish)
                        db.course_activity.insert(course_activity_category = Accepted.course_activity_category, name=actChange.name, description=actChange.description, grade =  actChange.grade, semester = cpfecys.current_year_period().id,  assignation = Accepted.course,  laboratory = 'T', teacher_permition = 'F', date_start = actChange.date_start, date_finish = actChange.date_finish)
                    elif actChange.operation_request=='delete':
                        db.course_activity_log.insert(user_name=auth.user.username, roll=rol_temp, operation_log='delete', course= Accepted.course.name, yearp=cpfecys.current_year_period().yearp, period=cpfecys.current_year_period().period.name, metric='T', before_course_activity_category=Accepted.course_activity_category.category.category, before_name=actChange.name, before_description=actChange.description, before_grade =  actChange.grade, before_laboratory = 'T', before_teacher_permition = 'F', before_date_start = actChange.date_start, before_date_finish = actChange.date_finish)
                        db(db.course_activity.id==actChange.activity).delete()
                    elif actChange.operation_request=='update':
                        activityOldR=db(db.course_activity.id==actChange.activity).select().first()
                        db.course_activity_log.insert(user_name=auth.user.username, roll=rol_temp, operation_log='update', course= Accepted.course.name, yearp=cpfecys.current_year_period().yearp, period=cpfecys.current_year_period().period.name, metric='T', before_course_activity_category=activityOldR.course_activity_category.category.category, before_name=activityOldR.name, before_description=activityOldR.description, before_grade =  activityOldR.grade, before_laboratory = activityOldR.laboratory, before_teacher_permition = activityOldR.teacher_permition, before_date_start = activityOldR.date_start, before_date_finish = activityOldR.date_finish, after_course_activity_category=Accepted.course_activity_category.category.category, after_name=actChange.name, after_description=actChange.description, after_grade =  actChange.grade, after_laboratory = 'T', after_teacher_permition = 'F', after_date_start = actChange.date_start, after_date_finish = actChange.date_finish)
                        db(db.course_activity.id==actChange.activity).update(name=actChange.name, description=actChange.description, grade =  actChange.grade, date_start = actChange.date_start, date_finish = actChange.date_finish)
            session.flash=T('The plan change request has been accepted')
        redirect(URL('activity_control','solve_request_change_activity',vars=dict(course=request.vars['course'])))



    #Obtain the course that want to view the request
    courseCheck = request.vars['course']

    #Check that the request vars contain something
    if (courseCheck is None):
        redirect(URL('default','index'))
    else:
        #Check if teacher or other role
        course=None
        if auth.has_membership('Teacher'):
            course = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == cpfecys.current_year_period().id) & (db.user_project.project==courseCheck)).select().first()
            if (course is None):
                session.flash=T('You do not have permission to view course requests')
                redirect(URL('default','index'))
        else:
            course=db.project(id=courseCheck)

        #Check that the course exist
        name=None
        if (course is None):
            redirect(URL('default','index'))
        else:
            if auth.has_membership('Teacher'):
                name=course.project.name
            else:
                name=course.name

        currentyear_period = cpfecys.current_year_period()
        return dict(name = name,
                    semester = currentyear_period.period.name,
                    semestre2 = currentyear_period,
                    year = currentyear_period.yearp,
                    course=courseCheck)


@auth.requires_login()
@auth.requires(auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator') or auth.has_membership('Teacher'))
def activityRequest():
    import cpfecys
    currentyear_period = cpfecys.current_year_period()
    return dict(semestre2 = currentyear_period)

@auth.requires_login()
@auth.requires(auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator') or auth.has_membership('Teacher'))
def weighting_request():
    import cpfecys
    currentyear_period = cpfecys.current_year_period()
    rol_log=''
    if auth.has_membership('Ecys-Administrator')==True:
        rol_log='Ecys-Administrator'
    elif auth.has_membership('Super-Administrator')==True:
        rol_log='Super-Administrator'
    elif auth.has_membership('Teacher')==True:
        rol_log='Teacher'
    elif auth.has_membership('Student')==True:
        rol_log='Student'
    pass
    return dict(semestre2 = currentyear_period,rol_log = rol_log)

@auth.requires_login()
@auth.requires(auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator') or auth.has_membership('Teacher'))
def grades_request():
    import cpfecys
    currentyear_period = cpfecys.current_year_period()
    rol_log=''
    if auth.has_membership('Ecys-Administrator')==True:
        rol_log='Ecys-Administrator'
    elif auth.has_membership('Super-Administrator')==True:
        rol_log='Super-Administrator'
    elif auth.has_membership('Teacher')==True:
        rol_log='Teacher'
    elif auth.has_membership('Student')==True:
        rol_log='Student'
    pass


    return dict(semestre2 = currentyear_period,rol_log = rol_log)



#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
@auth.requires_login()
def control_activity_without_metric():
    year = db(db.period_year.id == request.vars['year']).select().first() 
    year_semester = year.period
    project = db(db.project.id==request.vars['project']).select().first()

    assigantion = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == year.id) & (db.user_project.project == project.id)).select().first()
    if assigantion is None:
        assigned_to_project = False
    else:
        assigned_to_project = True

    return dict(semester = year_semester.name,
            year = year.yearp,
            semestre2 = year,
            project = project,
            assigned_to_project = assigned_to_project)


@auth.requires_login()
def management_activity_without_metric():
    #Check if the period is correct
    if request.vars['year'] is None or request.vars['year']=='':
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    else:
        year = request.vars['year']
        year = db(db.period_year.id==year).select().first()
        if year is None:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))
        else:
            if cpfecys.current_year_period().id != year.id:
                session.flash = T('Not valid Action.')
                redirect(URL('default','index'))

    #Check if the project is correct
    if request.vars['project'] is None or request.vars['project']=='':
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    else:
        project = request.vars['project']
        project = db(db.project.id==project).select().first()
        if project is None:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

    #Time limit of semester
    from datetime import datetime
    date1=None
    tiempo=str(datetime.now())
    dateInicialP = db.executesql('SELECT date(\''+tiempo+'\');',as_dict=True)
    for d0 in dateInicialP:
        date1=d0['date(\''+tiempo+'\')']
    date_var = db((db.student_control_period.period_name==(T(year.period.name)+" "+str(year.yearp)))).select().first()
    if date1 >= date_var.date_start_semester and date1 <= date_var.date_finish_semester:
        #Exception of permition
        exception_query = db(db.course_laboratory_exception.project == project.id).select().first()
        exception_s_var = False
        exception_t_var = False
        if exception_query is not None:
            exception_t_var = exception_query.t_edit_lab
            exception_s_var = exception_query.s_edit_course

        #Grid
        grid=None
        db.course_activity_without_metric.assignation.readable = False
        db.course_activity_without_metric.assignation.writable = False
        db.course_activity_without_metric.assignation.default = project.id
        db.course_activity_without_metric.semester.readable = False
        db.course_activity_without_metric.semester.writable = False
        db.course_activity_without_metric.semester.default = year.id
        if auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'):
            query = ((db.course_activity_without_metric.semester==year.id) & (db.course_activity_without_metric.assignation==project.id))
            grid = SQLFORM.grid(query, csv=False, paginate=5)
        elif auth.has_membership('Teacher'):
            assigantion = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == year.id) & (db.user_project.project == project)).select().first()
            if assigantion is None:
                session.flash = T('Not valid Action.')
                redirect(URL('default','index'))
            else:
                if exception_t_var==True:
                    query = ((db.course_activity_without_metric.semester==year.id) & (db.course_activity_without_metric.assignation==project.id))
                    grid = SQLFORM.grid(query, csv=False, paginate=10)
                else:
                    db.course_activity_without_metric.laboratory.writable = False
                    db.course_activity_without_metric.laboratory.default = False
                    query = ((db.course_activity_without_metric.semester==year.id) & (db.course_activity_without_metric.assignation==project.id)&(db.course_activity_without_metric.laboratory==False))
                    grid = SQLFORM.grid(query, csv=False, paginate=10)
        elif auth.has_membership('Student'):
            assigantion = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == year.id) & (db.user_project.project == project)).select().first()
            if assigantion is None:
                session.flash = T('Not valid Action.')
                redirect(URL('default','index'))
            else:
                db.course_activity_without_metric.teacher_permition.writable = False
                if exception_s_var==True:
                    query = ((db.course_activity_without_metric.semester==year.id) & (db.course_activity_without_metric.assignation==project.id))
                    grid = SQLFORM.grid(query, csv=False, paginate=10)
                else:
                    db.course_activity_without_metric.laboratory.writable = False
                    db.course_activity_without_metric.laboratory.default = True
                    query = ((db.course_activity_without_metric.semester==year.id) & (db.course_activity_without_metric.assignation==project.id)& ((db.course_activity_without_metric.laboratory==True) | ((db.course_activity_without_metric.laboratory== False)&(db.course_activity_without_metric.teacher_permition==True))))
                    grid = SQLFORM.grid(query, csv=False, paginate=10)
        else:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))
        return dict(year = year, project = project, grid=grid)
    else:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))




#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------


@auth.requires_login()
@auth.requires(auth.has_membership('Student') or auth.has_membership('Teacher') or auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
def validate_laboratory():
    #Check if the period is correct
    if request.vars['year'] is None or request.vars['year']=='':
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    else:
        year = request.vars['year']
        year = db(db.period_year.id==year).select().first()
        if year is None:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))
        else:
            if cpfecys.current_year_period().id != year.id:
                session.flash = T('Not valid Action.')
                redirect(URL('default','index'))

    #Check if the project is correct
    if request.vars['project'] is None or request.vars['project']=='':
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    else:
        project = request.vars['project']
        project = db(db.project.id==project).select().first()
        if project is None:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

    #Time limit of semester
    from datetime import datetime
    date1=None
    tiempo=str(datetime.now())
    dateInicialP = db.executesql('SELECT date(\''+tiempo+'\');',as_dict=True)
    for d0 in dateInicialP:
        date1=d0['date(\''+tiempo+'\')']
    date_var = db((db.student_control_period.period_name==(T(year.period.name)+" "+str(year.yearp)))).select().first()
    if date1 >= date_var.date_start_semester and date1 <= date_var.date_finish_semester:
        #Exception of permition
        exception_query = db(db.course_laboratory_exception.project == project.id).select().first()
        exception_s_var = False
        exception_t_var = False
        if exception_query is not None:
            exception_t_var = exception_query.t_edit_lab
            exception_s_var = exception_query.s_edit_course

        #Check if the course has endend
        no_actionsAll=False
        course_ended_var = db((db.course_ended.project==project.id) & (db.course_ended.period==year.id) ).select().first()
        if course_ended_var != None:
            if course_ended_var.finish == True:
                no_actionsAll=True

        #Grid
        grid=None
        db.validate_laboratory.id.readable = False
        db.validate_laboratory.id.writable = False
        db.validate_laboratory.project.readable = False
        db.validate_laboratory.project.writable = False
        db.validate_laboratory.project.default = project.id
        db.validate_laboratory.semester.readable = False
        db.validate_laboratory.semester.writable = False
        db.validate_laboratory.semester.default = year.id
        if auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'):
            query = ((db.validate_laboratory.semester==year.id)&(db.validate_laboratory.project==project.id))
            if no_actionsAll==False:
                if 'edit' in request.args:
                    db.validate_laboratory.carnet.writable = False
                    grid = SQLFORM.grid(query, csv=False, paginate=10, oncreate=oncreate_validate_laboratory, onupdate=onupdate_validate_laboratory, ondelete=ondelete_validate_laboratory, searchable=False)
                else:
                    grid = SQLFORM.grid(query, csv=False, paginate=10, oncreate=oncreate_validate_laboratory, onupdate=onupdate_validate_laboratory, ondelete=ondelete_validate_laboratory, searchable=False)
            else:
                grid = SQLFORM.grid(query, csv=False, create=False, editable=False, deletable=False, paginate=10, searchable=False)
        elif auth.has_membership('Teacher'):
            assigantion = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == year.id) & (db.user_project.project == project)).select().first()
            if assigantion is None:
                session.flash = T('Not valid Action.')
                redirect(URL('default','index'))
            else:
                if exception_t_var==True and no_actionsAll==False:
                    query = ((db.validate_laboratory.semester==year.id)&(db.validate_laboratory.project==project.id))
                    if 'edit' in request.args:
                        db.validate_laboratory.carnet.writable = False
                        grid = SQLFORM.grid(query, csv=False, paginate=10, oncreate=oncreate_validate_laboratory, onupdate=onupdate_validate_laboratory, ondelete=ondelete_validate_laboratory, searchable=False)
                    else:
                        grid = SQLFORM.grid(query, csv=False, paginate=10, oncreate=oncreate_validate_laboratory, onupdate=onupdate_validate_laboratory, ondelete=ondelete_validate_laboratory, searchable=False)
                else:
                    query = ((db.validate_laboratory.semester==year.id)&(db.validate_laboratory.project==project.id))
                    grid = SQLFORM.grid(query, csv=False, create=False, editable=False, deletable=False, paginate=10, searchable=False)
        elif auth.has_membership('Student'):
            assigantion = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == year.id) & (db.user_project.project == project)).select().first()
            if assigantion is None:
                session.flash = T('Not valid Action.')
                redirect(URL('default','index'))
            else:
                if no_actionsAll==False:
                    query = ((db.validate_laboratory.semester==year.id)&(db.validate_laboratory.project==project.id))
                    if 'edit' in request.args:
                        db.validate_laboratory.carnet.writable = False
                        grid = SQLFORM.grid(query, csv=False, paginate=10, oncreate=oncreate_validate_laboratory, onupdate=onupdate_validate_laboratory, ondelete=ondelete_validate_laboratory, searchable=False)
                    else:
                        grid = SQLFORM.grid(query, csv=False, paginate=10, oncreate=oncreate_validate_laboratory, onupdate=onupdate_validate_laboratory, ondelete=ondelete_validate_laboratory, searchable=False)
                else:
                    query = ((db.validate_laboratory.semester==year.id)&(db.validate_laboratory.project==project.id))
                    grid = SQLFORM.grid(query, csv=False, create=False, editable=False, deletable=False, paginate=10, searchable=False)
        else:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))
        return dict(year = year, project = project, grid=grid)
    else:
        #Grid
        grid=None
        db.validate_laboratory.id.readable = False
        db.validate_laboratory.id.writable = False
        db.validate_laboratory.project.readable = False
        db.validate_laboratory.project.writable = False
        db.validate_laboratory.project.default = project.id
        db.validate_laboratory.semester.readable = False
        db.validate_laboratory.semester.writable = False
        db.validate_laboratory.semester.default = year.id
        if auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'):
            query = ((db.validate_laboratory.semester==year.id)&(db.validate_laboratory.project==project.id))
            grid = SQLFORM.grid(query, csv=False, create=False, editable=False, deletable=False, paginate=10, searchable=False)
        elif auth.has_membership('Teacher'):
            assigantion = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == year.id) & (db.user_project.project == project)).select().first()
            if assigantion is None:
                session.flash = T('Not valid Action.')
                redirect(URL('default','index'))
            else:
                query = ((db.validate_laboratory.semester==year.id)&(db.validate_laboratory.project==project.id))
                grid = SQLFORM.grid(query, csv=False, create=False, editable=False, deletable=False, paginate=10, searchable=False)
        elif auth.has_membership('Student'):
            assigantion = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == year.id) & (db.user_project.project == project)).select().first()
            if assigantion is None:
                session.flash = T('Not valid Action.')
                redirect(URL('default','index'))
            else:
                query = ((db.validate_laboratory.semester==year.id)&(db.validate_laboratory.project==project.id))
                grid = SQLFORM.grid(query, csv=False, create=False, editable=False, deletable=False, paginate=10, searchable=False)
        else:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))
        return dict(year = year, project = project, grid=grid)



def oncreate_validate_laboratory(form):
    import cpfecys

    #Check if the period is correct
    if request.vars['year'] is None or request.vars['year']=='':
        db(db.validate_laboratory.id==form.vars.id).delete()
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    else:
        year = request.vars['year']
        year = db(db.period_year.id==year).select().first()
        if year is None:
            db(db.validate_laboratory.id==form.vars.id).delete()
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))
        else:
            if cpfecys.current_year_period().id != year.id:
                db(db.validate_laboratory.id==form.vars.id).delete()
                session.flash = T('Not valid Action.')
                redirect(URL('default','index'))

    #Check if the project is correct
    if request.vars['project'] is None or request.vars['project']=='':
        db(db.validate_laboratory.id==form.vars.id).delete()
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    else:
        project = request.vars['project']
        project = db(db.project.id==project).select().first()
        if project is None:
            db(db.validate_laboratory.id==form.vars.id).delete()
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))


    roll_var=''
    if auth.has_membership('Super-Administrator'):
        roll_var='Super-Administrator'
    elif auth.has_membership('Ecys-Administrator'):
        roll_var='Ecys-Administrator'
    elif auth.has_membership('Teacher'):
        assigantion = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == year.id) & (db.user_project.project == project)).select().first()
        if assigantion is None:
            db(db.validate_laboratory.id==form.vars.id).delete()
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))
        else:
            if exception_t_var==True:
                roll_var='Teacher'
            else:
                db(db.validate_laboratory.id==form.vars.id).delete()
                session.flash = T('Not valid Action.')
                redirect(URL('default','index'))
    elif auth.has_membership('Student'):
        assigantion = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == year.id) & (db.user_project.project == project)).select().first()
        if assigantion is None:
            db(db.validate_laboratory.id==form.vars.id).delete()
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))
        else:
            roll_var='Student'
    else:
        db(db.validate_laboratory.id==form.vars.id).delete()
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))

    usr2 = db((db.validate_laboratory.id != form.vars.id) & (db.validate_laboratory.semester == request.vars['year']) & (db.validate_laboratory.project == request.vars['project']) & (db.validate_laboratory.carnet == form.vars.carnet)).select().first()
    if usr2 is not None:
        db(db.validate_laboratory.id==form.vars.id).delete()
        session.flash = T('Error. Exist a register of validation of the student in the course.')
    else:
        academic_s = db(db.academic.id==form.vars.carnet).select().first()
        db.validate_laboratory_log.insert(user_name = auth.user.username,
                                roll = roll_var,
                                operation_log = 'insert',
                                academic_id = academic_s.id,
                                academic = academic_s.carnet,
                                project = project.name,
                                period = T(year.period.name),
                                yearp = year.yearp,
                                after_grade = form.vars.grade,
                                id_validate_laboratory = form.vars.id,
                                description = T('Inserted from validation page')
                                 )

def ondelete_validate_laboratory(table_involved, id_of_the_deleted_record):
    import cpfecys

    #Check if the period is correct
    if request.vars['year'] is None or request.vars['year']=='':
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    else:
        year = request.vars['year']
        year = db(db.period_year.id==year).select().first()
        if year is None:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))
        else:
            if cpfecys.current_year_period().id != year.id:
                session.flash = T('Not valid Action.')
                redirect(URL('default','index'))

    #Check if the project is correct
    if request.vars['project'] is None or request.vars['project']=='':
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    else:
        project = request.vars['project']
        project = db(db.project.id==project).select().first()
        if project is None:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

    roll_var=''
    if auth.has_membership('Super-Administrator'):
        roll_var='Super-Administrator'
    elif auth.has_membership('Ecys-Administrator'):
        roll_var='Ecys-Administrator'
    elif auth.has_membership('Teacher'):
        assigantion = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == year.id) & (db.user_project.project == project)).select().first()
        if assigantion is None:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))
        else:
            if exception_t_var==True:
                roll_var='Teacher'
            else:
                session.flash = T('Not valid Action.')
                redirect(URL('default','index'))
    elif auth.has_membership('Student'):
        assigantion = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == year.id) & (db.user_project.project == project)).select().first()
        if assigantion is None:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))
        else:
            roll_var='Student'
    else:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))


    validate_laboratory_var = db.validate_laboratory(id_of_the_deleted_record)
    if validate_laboratory_var is not None:        
        academic_s = db(db.academic.id==validate_laboratory_var.carnet).select().first()
        db.validate_laboratory_log.insert(user_name = auth.user.username,
                                roll = roll_var,
                                operation_log = 'delete',
                                academic_id = academic_s.id,
                                academic = academic_s.carnet,
                                project = project.name,
                                period = T(year.period.name),
                                yearp = year.yearp,
                                before_grade = validate_laboratory_var.grade,
                                description = T('Delete from validation page')
                                 )

def onupdate_validate_laboratory(form):
    import cpfecys

    #Check if the period is correct
    if request.vars['year'] is None or request.vars['year']=='':
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    else:
        year = request.vars['year']
        year = db(db.period_year.id==year).select().first()
        if year is None:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))
        else:
            if cpfecys.current_year_period().id != year.id:
                session.flash = T('Not valid Action.')
                redirect(URL('default','index'))

    #Check if the project is correct
    if request.vars['project'] is None or request.vars['project']=='':
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    else:
        project = request.vars['project']
        project = db(db.project.id==project).select().first()
        if project is None:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

    roll_var=''
    if auth.has_membership('Super-Administrator'):
        roll_var='Super-Administrator'
    elif auth.has_membership('Ecys-Administrator'):
        roll_var='Ecys-Administrator'
    elif auth.has_membership('Teacher'):
        assigantion = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == year.id) & (db.user_project.project == project)).select().first()
        if assigantion is None:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))
        else:
            if exception_t_var==True:
                roll_var='Teacher'
            else:
                session.flash = T('Not valid Action.')
                redirect(URL('default','index'))
    elif auth.has_membership('Student'):
        assigantion = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == year.id) & (db.user_project.project == project)).select().first()
        if assigantion is None:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))
        else:
            roll_var='Student'
    else:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))

    usr2 = db(db.validate_laboratory_log.id_validate_laboratory == form.vars.id).select(orderby=db.validate_laboratory_log.id)
    academic_log=''
    academic_id_log=''
    before_grade_log=''
    for u in usr2:
        academic_log=u.academic
        academic_id_log=u.academic_id
        before_grade_log=u.after_grade

    if form.vars.delete_this_record != None:
        db.validate_laboratory_log.insert(user_name = auth.user.username,
                                roll = roll_var,
                                operation_log = 'delete',
                                academic_id = academic_id_log,
                                academic = academic_log,
                                project = project.name,
                                period = T(year.period.name),
                                yearp = year.yearp,
                                before_grade = before_grade_log,
                                description = T('Delete from validation page')
                                 )
    else:
        if before_grade_log != form.vars.grade:
            db.validate_laboratory_log.insert(user_name = auth.user.username,
                                    roll = roll_var,
                                    operation_log = 'update',
                                    academic_id = academic_id_log,
                                    academic = academic_log,
                                    project = project.name,
                                    period = T(year.period.name),
                                    yearp = year.yearp,
                                    before_grade = before_grade_log,
                                    after_grade = form.vars.grade,
                                    id_validate_laboratory = form.vars.id,
                                    description = T('Update from validation page')
                                     )


#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
@auth.requires_login()
@auth.requires(auth.has_membership('Student') or auth.has_membership('Teacher') or auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
def general_report_activities_export():
    #vars
    year = None
    project_var = None
    #Check if the period is correct
    if request.vars['period'] is None or request.vars['period']=='':
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    else:
        year = request.vars['period']
        year = db(db.period_year.id==year).select().first()
        if year is None:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))


    #Check if the period is correct
    if request.vars['project'] is None or request.vars['project']=='':
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    else:
        project_var = request.vars['project']
        project_var = db(db.project.id==project_var).select().first()
        if project_var is None:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

    if auth.has_membership('Super-Administrator') == False and auth.has_membership('Ecys-Administrator')==False:
        assigantion = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == year.id) & (db.user_project.project == project_var.id)).select().first()
        if assigantion is None:
            try:
                academic_var = db(db.academic.carnet==auth.user.username).select().first()
                academic_assig = db((db.academic_course_assignation.carnet == academic_var.id) & (db.academic_course_assignation.semester == year.id) & (db.academic_course_assignation.assignation==project_var.id)).select().first()
                if academic_assig is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))
            except:
                session.flash = T('Not valid Action.')
                redirect(URL('default','index'))

    #Check the correct parameters
    if (request.vars['type'] != 'class' and request.vars['type']!='lab'):
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))

    teacher = db((db.user_project.period == year.id) & (db.user_project.project == project_var.id) & (db.user_project.assigned_user==db.auth_user.id)&(db.auth_user.id==db.auth_membership.user_id)&(db.auth_membership.group_id==3)).select().first()
    practice = db((db.user_project.period == year.id) & (db.user_project.project == project_var.id) & (db.user_project.assigned_user==db.auth_user.id)&(db.auth_user.id==db.auth_membership.user_id)&(db.auth_membership.group_id==2)).select()
    if request.vars['type'] == 'class':
        students = db((db.academic_course_assignation.semester == year.id) & (db.academic_course_assignation.assignation==project_var.id)).select()
    else:
        students = db((db.academic_course_assignation.semester == year.id) & (db.academic_course_assignation.assignation==project_var.id) & (db.academic_course_assignation.laboratorio==True)).select()


    existLab=False
    totalLab=float(0)
    totalW=float(0)
    CourseCategory = db((db.course_activity_category.semester==year.id)&(db.course_activity_category.assignation==project_var.id)&(db.course_activity_category.laboratory==False)).select()
    catCourseTemp=None
    catVecCourseTemp=[]
    CourseActivities = []
    for categoryC in CourseCategory:
        totalW=totalW+float(categoryC.grade)
        if categoryC.category.category=="Laboratorio":
            existLab=True
            totalLab=float(categoryC.grade)
            catVecCourseTemp.append(categoryC)
        elif categoryC.category.category=="Examen Final":
            catCourseTemp=categoryC
        else:
            catVecCourseTemp.append(categoryC)
            CourseActivities.append(db((db.course_activity.semester==year.id)&(db.course_activity.assignation==project_var.id)&(db.course_activity.laboratory==False)&(db.course_activity.course_activity_category==categoryC.id)).select())
    if catCourseTemp != None:
        catVecCourseTemp.append(catCourseTemp)
        CourseActivities.append(db((db.course_activity.semester==year.id)&(db.course_activity.assignation==project_var.id)&(db.course_activity.laboratory==False)&(db.course_activity.course_activity_category==catCourseTemp.id)).select())
    CourseCategory=catVecCourseTemp

    if request.vars['type'] == 'class':
        if totalW!=float(100):
            session.flash= T('Can not find the correct weighting defined in the course. You can not use this function')
            redirect(URL('default','index'))

    totalW=float(0)
    LabCategory=None
    catLabTemp=None
    catVecLabTemp=[]
    LabActivities = None
    validateLaboratory=None
    if existLab == True or request.vars['type'] == 'lab':
        validateLaboratory = db((db.validate_laboratory.semester==year.id)&(db.validate_laboratory.project==project_var.id)).select()
        LabCategory = db((db.course_activity_category.semester==year.id)&(db.course_activity_category.assignation==project_var.id)&(db.course_activity_category.laboratory==True)).select()
        LabActivities = []
        for categoryL in LabCategory:
            if categoryL.category.category=="Examen Final":
                totalW=totalW+float(categoryL.grade)
                catLabTemp=categoryL
            else:
                catVecLabTemp.append(categoryL)
                totalW=totalW+float(categoryL.grade)
                LabActivities.append(db((db.course_activity.semester==year.id)&(db.course_activity.assignation==project_var.id)&(db.course_activity.laboratory==True)&(db.course_activity.course_activity_category==categoryL.id)).select())
        if catLabTemp != None:
            catVecLabTemp.append(catLabTemp)
            LabActivities.append(db((db.course_activity.semester==year.id)&(db.course_activity.assignation==project_var.id)&(db.course_activity.laboratory==True)&(db.course_activity.course_activity_category==catLabTemp.id)).select())
        LabCategory=catVecLabTemp

        if totalW!=float(100):
            session.flash= T('Can not find the correct weighting defined in the laboratory. You can not use this function')
            redirect(URL('default','index'))

    requirement = db((db.course_requirement.semester==year.id)&(db.course_requirement.project==project_var.id)).select().first()

    l=[]
    t=[]
    tempCont=T('General Report of Activities')
    if request.vars['type'] == 'class':
        tempCont += ' - '+T('Course')
    else:
        tempCont += ' - '+T('Laboratory')
    t.append(tempCont)
    l.append(t)

    t=[]
    tempCont=T('General Course Data')
    t.append(tempCont)
    l.append(t)

    t=[]
    tempCont=T('Course')
    t.append(tempCont)
    tempCont=project_var.name
    t.append(tempCont)
    tempCont=T('Semester')
    t.append(tempCont)
    tempCont=T(year.period.name)+' '+str(year.yearp)
    t.append(tempCont)
    l.append(t)

    t=[]
    tempCont=T('Teacher')
    t.append(tempCont)
    if teacher is not None:
        tempCont=teacher.auth_user.first_name+' '+teacher.auth_user.last_name
    else:
        tempCont=T('Not Assigned')
    t.append(tempCont)
    tempCont=T('Rol Student')
    t.append(tempCont)
    tempCont=None
    for t1 in practice:
        if tempCont is None:
            tempCont=t1.auth_user.first_name+' '+t1.auth_user.last_name
        else:
            tempCont=tempCont+'\n'+t1.auth_user.first_name+' '+t1.auth_user.last_name
    t.append(tempCont)
    l.append(t)

    t=[]
    t.append(T('Carnet'))
    posVCC=0
    if request.vars['type'] == 'class':
        for category in CourseCategory:
            if category.category.category!="Laboratorio":
                for c in CourseActivities[posVCC]:
                    t.append(c.name)
                t.append(category.category.category +'\n('+str(category.grade)+'pts)')
                posVCC=posVCC+1
    else:
        for category in LabCategory:
            if category.category.category!="Laboratorio":
                for c in LabActivities[posVCC]:
                    t.append(c.name)
                t.append(category.category.category +'\n('+str(category.grade)+'pts)')
                posVCC=posVCC+1
    if request.vars['type'] == 'class' and existLab==True:
        t.append(T('Laboratory') +'\n('+str(totalLab)+'pts)')
    if request.vars['type'] == 'class' and requirement is not None:
        t.append(T('Course Requeriment') +'\n('+requirement.name+'pts)')
    t.append(T('Final Grade') +'\n(100 pts)')
    l.append(t) 


    t=[]
    for t1 in students:
        t=[]
        if request.vars['type'] == 'class':
            t.append(str(t1.carnet.carnet))
            #Position in the vector of activities-
            posVCC=0
            #Vars to the control of grade of the student
            totalCategory=float(0)
            totalActivities=0
            totalCarry=float(0)
            #<!--****************************************FILL THE GRADES OF THE STUDENT****************************************-->
            #<!--COURSE ACTIVITIES-->
            for category in CourseCategory:
                if category.category.category!="Laboratorio":
                    totalCategory=float(0)
                    totalActivities=0
                    for c in CourseActivities[posVCC]:
                        studentGrade = db((db.grades.activity==c.id)&(db.grades.academic_assignation==t1.id)).select().first()
                        if studentGrade is None:
                            totalCategory=totalCategory+float(0)
                            t.append('')
                        else:
                            if category.specific_grade==True:
                                t.append(str(studentGrade.grade))
                                totalCategory=totalCategory+float((studentGrade.grade*c.grade)/100)
                            else:
                                t.append(str(studentGrade.grade))
                                totalCategory=totalCategory+float(studentGrade.grade)
                        totalActivities=totalActivities+1

                    if category.specific_grade==True:
                        t.append(str(totalCategory))
                    else:
                        if totalActivities==0:
                            totalActivities=1
                        totalActivities=totalActivities*100
                        totalCategory=float((totalCategory*float(category.grade))/float(totalActivities))
                        t.append(str(totalCategory))
                    totalCarry=totalCarry+totalCategory
                    posVCC=posVCC+1

            if request.vars['type'] == 'class' and existLab==True:
                totalCategory=float(0)
                isValidate=False
                #<!--Revalidation of laboratory-->
                for validate in validateLaboratory:
                    if validate.carnet==t1.carnet:
                        isValidate=True
                        totalCategory=float((validate.grade*totalLab)/100)


                #<!--Doesnt has a revalidation-->
                if isValidate==False:
                    #<!--Position in the vector of activities-->
                    posVCC_Lab=0
                    #<!--Vars to the control of grade of the student-->
                    totalCategory_Lab=float(0)
                    totalActivities_Lab=0
                    totalCarry_Lab=float(0)

                    #<!--****************************************FILL THE GRADES OF THE STUDENT****************************************-->
                    #<!--LAB ACTIVITIES-->
                    for category_Lab in LabCategory:
                        totalCategory_Lab=float(0)
                        totalActivities_Lab=0
                        for c_Lab in LabActivities[posVCC_Lab]:
                            studentGrade = db((db.grades.activity==c_Lab.id)&(db.grades.academic_assignation==t1.id)).select().first()
                            if studentGrade is None:
                                totalCategory_Lab=totalCategory_Lab+float(0)
                            else:
                                if category_Lab.specific_grade==True:
                                    totalCategory_Lab=totalCategory_Lab+float((studentGrade.grade*c_Lab.grade)/100)
                                else:
                                    totalCategory_Lab=totalCategory_Lab+float(studentGrade.grade)
                            totalActivities_Lab=totalActivities_Lab+1
                        

                        if category_Lab.specific_grade==False:
                            if totalActivities_Lab==0:
                                totalActivities_Lab=1
                            totalActivities_Lab=totalActivities_Lab*100
                            totalCategory_Lab=float((totalCategory_Lab*float(category_Lab.grade))/float(totalActivities_Lab))
                        totalCarry_Lab=totalCarry_Lab+totalCategory_Lab
                        posVCC_Lab=posVCC_Lab+1
                    totalCategory=float((totalCarry_Lab*totalLab)/100)


                #<!--Show grade of laboratory-->
                t.append(str(totalCategory))
                #<!--Plus the laboratory to the carry-->
                totalCarry=totalCarry+totalCategory

            if request.vars['type'] == 'class' and requirement is not None:
                if db((db.course_requirement_student.carnet==t1.carnet)&(db.course_requirement_student.requirement==requirement.id)).select().first() is not None:
                    t.append(T('True'))
                else:
                    t.append(T('False'))
            if request.vars['type'] == 'class' and requirement is not None:
                if db((db.course_requirement_student.carnet==t1.carnet)&(db.course_requirement_student.requirement==requirement.id)).select().first() is not None:
                    if request.vars['type'] == 'class' and existLab==True:
                        if totalCategory>=float((61*totalLab)/100):
                            t.append(str(totalCarry))
                        else:
                            t.append('0')
                    else:
                        t.append(str(totalCarry))
                else:
                    t.append('0')
            else:
                if request.vars['type'] == 'class' and existLab==True:
                    if totalCategory>=float((61*totalLab)/100):
                        t.append(str(totalCarry))
                    else:
                        t.append('0')
                else:
                    t.append(str(totalCarry))
            posVCC=0
            totalCategory=float(0)
            totalActivities=0
            totalCarry=float(0)
            l.append(t)
            t=[]
        else:
            t.append(str(t1.carnet.carnet))

            #<!--Position in the vector of activities-->
            posVCC=0
            #<!--Vars to the control of grade of the student-->
            totalCategory=float(0)
            totalActivities=0
            totalCarry=float(0)
            #<!--****************************************FILL THE GRADES OF THE STUDENT****************************************-->
            #<!--COURSE ACTIVITIES-->
            for category in LabCategory:
                totalCategory=float(0)
                totalActivities=0
                for c in LabActivities[posVCC]:
                    studentGrade = db((db.grades.activity==c.id)&(db.grades.academic_assignation==t1.id)).select().first()
                    if studentGrade is None:
                        totalCategory=totalCategory+float(0)
                        t.append('')
                    else:
                        if category.specific_grade==True:
                            t.append(str(studentGrade.grade))
                            totalCategory=totalCategory+float((studentGrade.grade*c.grade)/100)
                        else:
                            t.append(str(studentGrade.grade))
                            totalCategory=totalCategory+float(studentGrade.grade)
                    totalActivities=totalActivities+1

                if category.specific_grade==True:
                    t.append(str(totalCategory))
                else:
                    if totalActivities==0:
                        totalActivities=1
                    pass
                    totalActivities=totalActivities*100
                    totalCategory=float((totalCategory*float(category.grade))/float(totalActivities))
                    t.append(str(totalCategory))
                totalCarry=totalCarry+totalCategory
                posVCC=posVCC+1

            t.append(str(totalCarry))
            l.append(t)
            t=[]
            posVCC=0
            totalCategory=float(0)
            totalActivities=0
            totalCarry=float(0)


    nombre='ReporteGeneralActividades '+project_var.name
    return dict(filename=nombre, csvdata=l)


@auth.requires_login()
@auth.requires(auth.has_membership('Student') or auth.has_membership('Teacher') or auth.has_membership('Super-Administrator') or auth.has_membership('Academic') or auth.has_membership('Ecys-Administrator'))
def General_report_activities():
    #vars
    year = None
    project_var = None
    #Check if the period is correct
    if request.vars['period'] is None or request.vars['period']=='':
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    else:
        year = request.vars['period']
        year = db(db.period_year.id==year).select().first()
        if year is None:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))


    #Check if the period is correct
    if request.vars['project'] is None or request.vars['project']=='':
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    else:
        project_var = request.vars['project']
        project_var = db(db.project.id==project_var).select().first()
        if project_var is None:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

    if auth.has_membership('Super-Administrator') == False and auth.has_membership('Ecys-Administrator')==False:
        assigantion = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == year.id) & (db.user_project.project == project_var.id)).select().first()
        if assigantion is None:
            try:
                academic_var = db(db.academic.carnet==auth.user.username).select().first()
                academic_assig = db((db.academic_course_assignation.carnet == academic_var.id) & (db.academic_course_assignation.semester == year.id) & (db.academic_course_assignation.assignation==project_var.id)).select().first()
                if academic_assig is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))
            except:
                session.flash = T('Not valid Action.')
                redirect(URL('default','index'))

    #Check the correct parameters
    if (request.vars['type'] != 'class' and request.vars['type']!='lab'):
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))

    teacher = db((db.user_project.period == year.id) & (db.user_project.project == project_var.id) & (db.user_project.assigned_user==db.auth_user.id)&(db.auth_user.id==db.auth_membership.user_id)&(db.auth_membership.group_id==3)).select().first()
    practice = db((db.user_project.period == year.id) & (db.user_project.project == project_var.id) & (db.user_project.assigned_user==db.auth_user.id)&(db.auth_user.id==db.auth_membership.user_id)&(db.auth_membership.group_id==2)).select()
    if request.vars['type'] == 'class':
        students = db((db.academic_course_assignation.semester == year.id) & (db.academic_course_assignation.assignation==project_var.id)).select()
    else:
        students = db((db.academic_course_assignation.semester == year.id) & (db.academic_course_assignation.assignation==project_var.id) & (db.academic_course_assignation.laboratorio==True)).select()


    existLab=False
    totalLab=float(0)
    totalW=float(0)
    CourseCategory = db((db.course_activity_category.semester==year.id)&(db.course_activity_category.assignation==project_var.id)&(db.course_activity_category.laboratory==False)).select()
    catCourseTemp=None
    catVecCourseTemp=[]
    CourseActivities = []
    for categoryC in CourseCategory:
        totalW=totalW+float(categoryC.grade)
        if categoryC.category.category=="Laboratorio":
            existLab=True
            totalLab=float(categoryC.grade)
            catVecCourseTemp.append(categoryC)
        elif categoryC.category.category=="Examen Final":
            catCourseTemp=categoryC
        else:
            catVecCourseTemp.append(categoryC)
            CourseActivities.append(db((db.course_activity.semester==year.id)&(db.course_activity.assignation==project_var.id)&(db.course_activity.laboratory==False)&(db.course_activity.course_activity_category==categoryC.id)).select())
    if catCourseTemp != None:
        catVecCourseTemp.append(catCourseTemp)
        CourseActivities.append(db((db.course_activity.semester==year.id)&(db.course_activity.assignation==project_var.id)&(db.course_activity.laboratory==False)&(db.course_activity.course_activity_category==catCourseTemp.id)).select())
    CourseCategory=catVecCourseTemp


    if request.vars['type'] == 'class':
        if totalW!=float(100):
            session.flash= T('Can not find the correct weighting defined in the course. You can not use this function')
            redirect(URL('default','index'))

    totalW=float(0)
    LabCategory=None
    catLabTemp=None
    catVecLabTemp=[]
    LabActivities = None
    validateLaboratory=None
    if existLab == True or request.vars['type'] == 'lab':
        validateLaboratory = db((db.validate_laboratory.semester==year.id)&(db.validate_laboratory.project==project_var.id)).select()
        LabCategory = db((db.course_activity_category.semester==year.id)&(db.course_activity_category.assignation==project_var.id)&(db.course_activity_category.laboratory==True)).select()
        LabActivities = []
        for categoryL in LabCategory:
            if categoryL.category.category=="Examen Final":
                totalW=totalW+float(categoryL.grade)
                catLabTemp=categoryL
            else:
                catVecLabTemp.append(categoryL)
                totalW=totalW+float(categoryL.grade)
                LabActivities.append(db((db.course_activity.semester==year.id)&(db.course_activity.assignation==project_var.id)&(db.course_activity.laboratory==True)&(db.course_activity.course_activity_category==categoryL.id)).select())
        if catLabTemp != None:
            catVecLabTemp.append(catLabTemp)
            LabActivities.append(db((db.course_activity.semester==year.id)&(db.course_activity.assignation==project_var.id)&(db.course_activity.laboratory==True)&(db.course_activity.course_activity_category==catLabTemp.id)).select())
        LabCategory=catVecLabTemp

        if totalW!=float(100):
            session.flash= T('Can not find the correct weighting defined in the laboratory. You can not use this function')
            redirect(URL('default','index'))


    if request.vars['list'] =='True':
        redirect(URL('activity_control','general_report_activities_export',vars=dict(project = project_var.id, period = year.id, type=request.vars['type'])))
    
    if request.vars['list'] =='False':
        course_ended_var = db((db.course_ended.project==project_var.id) & (db.course_ended.period==year.id) ).select().first() 
        if course_ended_var is None:
            
            #ROL FOR LOG
            nombreRol=''
            if auth.has_membership('Ecys-Administrator')==True:
                nombreRol='Ecys-Administrator'
            elif auth.has_membership('Super-Administrator')==True:
                nombreRol='Super-Administrator'
            elif auth.has_membership('Teacher')==True:
                nombreRol='Teacher'
            elif auth.has_membership('Student')==True:
                nombreRol='Student'
            pass
            
            #GRADES CHANGE REQUEST
            request_change = db((db.request_change_grades.status=='pending')&(db.request_change_grades.period==int(year.id))&(db.request_change_grades.project==int(project_var.id))).select()
            for change in request_change:
                from datetime import datetime
                
                db(db.request_change_grades.id==change.id).update(status = 'rejected', 
                                                                    resolve_user = auth.user.id, 
                                                                    roll_resolve =  nombreRol, 
                                                                    date_request_resolve = str(datetime.now())
                                                                )

                #---------------------------------LOG-----------------------------------------------
                                                                                    
                temp2 = db(db.request_change_g_log.r_c_g_id == change.id).select().first()
                
                temp3 = db.request_change_g_log.insert(r_c_g_id=change.id,
                                                    username=temp2.username,
                                                    roll=temp2.roll,
                                                    before_status='pending',
                                                    after_status='rejected',
                                                    description=temp2.description,
                                                    semester=temp2.semester,
                                                    yearp=temp2.yearp,
                                                    project=temp2.project,
                                                    category=temp2.activity,
                                                    activity=temp2.category,
                                                    resolve_user=auth.user.username,
                                                    roll_resolve=nombreRol,
                                                    date_request=temp2.date_request,
                                                    date_request_resolve=str(datetime.now())
                                                ) 
                for var_chang_ins in db((db.request_change_grades_detail.request_change_grades ==  change.id)).select():
                    db.request_change_grade_d_log.insert(request_change_g_log=temp3,
                                                            operation_request=var_chang_ins.operation_request,
                                                            academic=var_chang_ins.academic_assignation.carnet.carnet,
                                                            after_grade=var_chang_ins.after_grade,
                                                            before_grade=var_chang_ins.before_grade
                                                           )
                pass
            pass

            #Weighting CHANGE REQUEST
            request_change = db((db.request_change_weighting.status=='pending')&(db.request_change_weighting.period==int(year.id))&(db.request_change_weighting.project==int(project_var.id))).select()
            for change in request_change:
                from datetime import datetime
                db(db.request_change_weighting.id==change.id).update(status = 'rejected', 
                                                                    resolve_user = auth.user.id, 
                                                                    roll_resolve =  nombreRol, 
                                                                    date_request_resolve = str(datetime.now())
                                                                )
                temp2 = db(db.request_change_w_log.r_c_w_id == change.id).select().first()
                temp3 = db.request_change_w_log.insert(r_c_w_id=change.id,
                                                    username=temp2.username,
                                                    roll=temp2.roll,
                                                    before_status='pending',
                                                    after_status='rejected',
                                                    description=temp2.description,
                                                    semester=temp2.semester,
                                                    yearp=temp2.yearp,
                                                    project=temp2.project,
                                                    resolve_user=auth.user.username,
                                                    roll_resolve=nombreRol,
                                                    date_request=temp2.date_request,
                                                    date_request_resolve=str(datetime.now())
                                                ) 
                temp4 = db(db.request_change_weighting.id == change.id).select().first() 
                
                for var_chang_ins in db((db.request_change_weighting_detail.request_change_weighting ==  temp4.id) & (db.request_change_weighting_detail.operation_request == 'insert')).select():
                    if var_chang_ins.operation_request == 'insert':
                        db.request_change_w_detail_log.insert(request_change_w_log=temp3,
                                                                operation_request=var_chang_ins.operation_request,
                                                                category=var_chang_ins.category.category,
                                                                after_grade=var_chang_ins.grade,
                                                                after_specific_grade=var_chang_ins.specific_grade)
                    pass

                pass

                for categories in db((db.course_activity_category.semester==int(temp4.period)) & (db.course_activity_category.assignation==temp4.project) & (db.course_activity_category.laboratory==True)).select():
                    var_chang = db(db.request_change_weighting_detail.course_category ==  str(categories.id)).select().first()
                    if var_chang != None:
                        if var_chang.operation_request == 'delete':
                            
                            cat_temp = db(db.course_activity_category.id == var_chang.course_category).select().first()

                            temp44 = db(db.request_change_w_log.id == str(temp3) ).select().first() 
                            db.request_change_w_detail_log.insert(request_change_w_log = str(temp3),
                                                                    operation_request = str(var_chang.operation_request),
                                                                    course_category = str(cat_temp.category.category),
                                                                    before_grade = str(cat_temp.grade),
                                                                    before_specific_grade = str(cat_temp.specific_grade) )

                        pass
                        if var_chang.operation_request == 'update':
                            cat_temp = db(db.course_activity_category.id==var_chang.course_category).select().first()
                            cat_temp2 = db(db.activity_category.id==var_chang.category).select().first()

                            db.request_change_w_detail_log.insert(request_change_w_log=temp3,
                                                                    operation_request=var_chang.operation_request,
                                                                    course_category=cat_temp.category.category,
                                                                    category=cat_temp2.category,
                                                                    before_grade=cat_temp.grade,                                                                
                                                                    after_specific_grade=var_chang.specific_grade,
                                                                    after_grade=var_chang.grade,
                                                                    before_specific_grade=cat_temp.specific_grade)

                        pass
                        db(db.request_change_weighting_detail.id==var_chang.id).update(course_category = None)
                    else:
                        add_to_log = True
                        for req_c_w_d_l in db(db.request_change_w_detail_log.request_change_w_log==temp3).select():
                            if categories.category.category == req_c_w_d_l.category:
                                add_to_log = False
                            pass
                        pass
                        if add_to_log == True:
                            db.request_change_w_detail_log.insert(request_change_w_log=temp3,
                                                                    operation_request='none',
                                                                    category=categories.category.category,
                                                                    after_grade=categories.grade,
                                                                    after_specific_grade=categories.specific_grade)
                        pass                                                        
                    pass
                pass
            pass

            #Weighting CHANGE REQUEST
            request_change = db((db.requestchange_activity.status=='Pending')&(db.requestchange_activity.semester==int(year.id))&(db.requestchange_activity.course==int(project_var.id))).select()
            for change in request_change:
                from datetime import datetime
                Pending = change
                rol_temp = nombreRol
                
                db(db.requestchange_activity.id==int(change.id)).update(status = 'Rejected', user_resolve = auth.user.id, roll_resolve =  rol_temp, date_request_resolve =  datetime.now())
                #Log of request change activity
                Rejected = db(db.requestchange_activity.id==int(change.id)).select().first()
                if Rejected is not None:
                    idR = db.requestchange_activity_log.insert(user_request=Rejected.user_id.username, 
                                                                roll_request=Rejected.roll, status='Rejected', 
                                                                user_resolve=Rejected.user_resolve.username, 
                                                                roll_resolve=Rejected.roll_resolve,
                                                                description=Rejected.description,
                                                                date_request=Rejected.date_request, 
                                                                date_request_resolve=Rejected.date_request_resolve, 
                                                                category_request=Rejected.course_activity_category.category.category, 
                                                                semester=Rejected.semester.period.name, 
                                                                yearp=Rejected.semester.yearp, 
                                                                course=Rejected.course.name)
                    activitiesChange = db(db.requestchange_course_activity.requestchange_activity==Rejected.id).select()
                    for actChange in activitiesChange:
                        db.requestchange_course_activity_log.insert(requestchange_activity=idR, 
                                                                    operation_request=actChange.operation_request, 
                                                                    activity=actChange.activity, 
                                                                    name=actChange.name, 
                                                                    description=actChange.description, 
                                                                    grade=actChange.grade, 
                                                                    date_start=actChange.date_start, 
                                                                    date_finish=actChange.date_finish)
            pass#hola

            #Insert to course_ended           
            db.course_ended.insert(project = project_var.id,
                            period = year.id,
                            finish =  True)

    controlP = db((db.student_control_period.period_name==(T(year.period.name)+" "+str(year.yearp)))).select().first()
    requirement = db((db.course_requirement.semester==year.id)&(db.course_requirement.project==project_var.id)).select().first()

    return dict(project = project_var, year = year, teacher=teacher, practice=practice, students=students, CourseCategory=CourseCategory, CourseActivities=CourseActivities, existLab=existLab, LabCategory=LabCategory, LabActivities=LabActivities, validateLaboratory=validateLaboratory, totalLab=totalLab, controlP=controlP, requirement=requirement)


@auth.requires_login()
@auth.requires(auth.has_membership('Student') or auth.has_membership('Teacher') or auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
def course_requirement():
    #vars
    year = None
    project_var = None
    #Check if the period is correct
    if request.vars['period'] is None or request.vars['period']=='':
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    else:
        year = request.vars['period']
        year = db(db.period_year.id==year).select().first()
        if year is None:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))
        else:
            if cpfecys.current_year_period().id != year.id:
                session.flash = T('Not valid Action.')
                redirect(URL('default','index'))

    #Check if the period is correct
    if request.vars['project'] is None or request.vars['project']=='':
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    else:
        project_var = request.vars['project']
        project_var = db(db.project.id==project_var).select().first()
        if project_var is None:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

    if auth.has_membership('Super-Administrator') == False and auth.has_membership('Ecys-Administrator')==False:
        assigantion = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == year.id) & (db.user_project.project == project_var.id)).select().first()
        if assigantion is None:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

    #Exception of permition
    exception_query = db(db.course_laboratory_exception.project == project_var.id).select().first()
    exception_s_var = False
    if exception_query is not None:
        exception_s_var = exception_query.s_edit_course
    #Check if the course has endend
    no_actionsAll=False
    course_ended_var = db((db.course_ended.project==project_var.id) & (db.course_ended.period==year.id) ).select().first()
    if course_ended_var != None:
        if course_ended_var.finish == True:
            no_actionsAll=True
    #Grid
    activityPermition=db((db.course_requirement.semester==year.id)&(db.course_requirement.project==project_var.id)).select().first()
    grid=None
    db.course_requirement.id.readable = False
    db.course_requirement.id.writable = False
    db.course_requirement.project.readable = False
    db.course_requirement.project.writable = False
    db.course_requirement.project.default = project_var.id
    db.course_requirement.semester.readable = False
    db.course_requirement.semester.writable = False
    db.course_requirement.semester.default = year.id
    #
    links = [lambda row: A(T('Management approval of students'),
        _role='button',
        _class='btn btn-success',
        _href=URL('activity_control', 'management_approval_students_requirement', vars=dict(project = project_var.id, period = year.id, requirement=row.id)),
        _title=T('Edit academic information'))]
    #
    if auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'):
        query = ((db.course_requirement.semester==year.id)&(db.course_requirement.project==project_var.id))
        if no_actionsAll==False:
            if activityPermition is None:
                grid = SQLFORM.grid(query, csv=False, paginate=1, searchable=False, links=links)
            else:
                grid = SQLFORM.grid(query, csv=False, paginate=1, create=False, searchable=False, links=links)
        else:
            grid = SQLFORM.grid(query, csv=False, create=False, editable=False, deletable=False, searchable=False, links=links)
    elif auth.has_membership('Teacher'):
        query = ((db.course_requirement.semester==year.id)&(db.course_requirement.project==project_var.id))
        if no_actionsAll==False:
            if activityPermition is None:
                grid = SQLFORM.grid(query, csv=False, paginate=1, searchable=False, links=links)
            else:
                grid = SQLFORM.grid(query, csv=False, paginate=1, create=False, searchable=False, links=links)
        else:
            grid = SQLFORM.grid(query, csv=False, create=False, editable=False, deletable=False, searchable=False, links=links)
    elif auth.has_membership('Student'):
        query = ((db.course_requirement.semester==year.id)&(db.course_requirement.project==project_var.id))
        if no_actionsAll==False:
            if exception_s_var==True or activityPermition.teacher_permition==True:
                db.course_requirement.teacher_permition.default = False
                db.course_requirement.teacher_permition.writable = False
                if activityPermition is None:
                    grid = SQLFORM.grid(query, csv=False, paginate=1, searchable=False, links=links)
                else:
                    grid = SQLFORM.grid(query, csv=False, paginate=1, create=False, searchable=False, links=links)
            else:
                grid = SQLFORM.grid(query, csv=False, create=False, editable=False, deletable=False, searchable=False, links=links)
        else:
            grid = SQLFORM.grid(query, csv=False, create=False, editable=False, deletable=False, searchable=False, links=links)
    else:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    return dict(project = project_var, year = year, grid=grid)


@auth.requires_login()
@auth.requires(auth.has_membership('Student') or auth.has_membership('Teacher') or auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
def management_approval_students_requirement():
    #vars
    year = None
    project_var = None
    requirement = None
    #Check if the period is correct
    if request.vars['period'] is None or request.vars['period']=='':
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    else:
        year = request.vars['period']
        year = db(db.period_year.id==year).select().first()
        if year is None:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))
        else:
            if cpfecys.current_year_period().id != year.id:
                session.flash = T('Not valid Action.')
                redirect(URL('default','index'))

    #Check if the period is correct
    if request.vars['project'] is None or request.vars['project']=='':
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    else:
        project_var = request.vars['project']
        project_var = db(db.project.id==project_var).select().first()
        if project_var is None:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

    #Check if the requirement is correct
    if request.vars['requirement'] is None or request.vars['requirement']=='':
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    else:
        requirement = request.vars['requirement']
        requirement = db(db.course_requirement.id==requirement).select().first()
        if requirement is None:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))
        else:
            if requirement.project!=project_var.id or requirement.semester!=year.id:
                session.flash = T('Not valid Action.')
                redirect(URL('default','index'))


    if auth.has_membership('Super-Administrator') == False and auth.has_membership('Ecys-Administrator')==False:
        assigantion = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == year.id) & (db.user_project.project == project_var.id)).select().first()
        if assigantion is None:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

    #Exception of permition
    exception_query = db(db.course_laboratory_exception.project == project_var.id).select().first()
    exception_s_var = False
    if exception_query is not None:
        exception_s_var = exception_query.s_edit_course
    #Check if the course has endend
    no_actionsAll=False
    course_ended_var = db((db.course_ended.project==project_var.id) & (db.course_ended.period==year.id) ).select().first()
    if course_ended_var != None:
        if course_ended_var.finish == True:
            no_actionsAll=True
    #Grid
    grid=None
    db.course_requirement_student.id.readable = False
    db.course_requirement_student.id.writable = False
    db.course_requirement_student.requirement.readable = False
    db.course_requirement_student.requirement.writable = False
    db.course_requirement_student.requirement.default = requirement.id
    if auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'):
        query = (db.course_requirement_student.requirement==requirement.id)
        if no_actionsAll==False:
            grid = SQLFORM.grid(query, csv=False, paginate=10, editable=False, searchable=False)
        else:
            grid = SQLFORM.grid(query, csv=False, create=False, editable=False, deletable=False, searchable=False)
    elif auth.has_membership('Teacher'):
        query = (db.course_requirement_student.requirement==requirement.id)
        if no_actionsAll==False:
            grid = SQLFORM.grid(query, csv=False, paginate=10, editable=False, searchable=False)
        else:
            grid = SQLFORM.grid(query, csv=False, create=False, editable=False, deletable=False, searchable=False)
    elif auth.has_membership('Student'):
        query = (db.course_requirement_student.requirement==requirement.id)
        if no_actionsAll==False:
            if exception_s_var==True or requirement.teacher_permition==True:
                grid = SQLFORM.grid(query, csv=False, paginate=10, editable=False, details=False, searchable=False)
            else:
                grid = SQLFORM.grid(query, csv=False, create=False, editable=False, deletable=False, searchable=False)
        else:
            grid = SQLFORM.grid(query, csv=False, create=False, editable=False, deletable=False, searchable=False)
    else:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    return dict(project = project_var, year = year, requirement=requirement, grid=grid)


#********************************************************************************************************************************************************************************************************
#********************************************************************************************************************************************************************************************************
#********************************************************************************************************************************************************************************************************
#********************************************************************************************************************************************************************************************************
@auth.requires_login()
def grades_management():
    #vars
    year = None
    project = None
    #Check if the period is correct
    if request.vars['period'] is None or request.vars['period']=='':
        session.flash = T('Not valid Action.')
        redirect(URL('sdefault','index'))
    else:
        year = request.vars['period']
        year = db(db.period_year.id==year).select().first()
        if year is None:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

    #Check if the period is correct
    if request.vars['project'] is None or request.vars['project']=='':
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    else:
        project = request.vars['project']
        project = db(db.project.id==project).select().first()
        if project is None:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

    #Check if the user is assigned to the course
    assigantion = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == year.id) & (db.user_project.project == project.id)).select().first()
    if assigantion is None:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))

    vecMonth=[]
    tmpMonth=[]
    if year.period == 1:
        tmpMonth=[]
        tmpMonth.append(1)
        tmpMonth.append('Enero')
        tmpMonth.append(2)
        vecMonth.append(tmpMonth)

        tmpMonth=[]
        tmpMonth.append(2)
        tmpMonth.append('Febrero')
        tmpMonth.append(3)
        vecMonth.append(tmpMonth)

        tmpMonth=[]
        tmpMonth.append(3)
        tmpMonth.append('Marzo')
        tmpMonth.append(4)
        vecMonth.append(tmpMonth)

        tmpMonth=[]
        tmpMonth.append(4)
        tmpMonth.append('Abril')
        tmpMonth.append(5)
        vecMonth.append(tmpMonth)

        tmpMonth=[]
        tmpMonth.append(5)
        tmpMonth.append('Mayo')
        tmpMonth.append(6)
        vecMonth.append(tmpMonth)
    else:
        tmpMonth=[]
        tmpMonth.append(6)
        tmpMonth.append('Junio')
        tmpMonth.append(7)
        vecMonth.append(tmpMonth)

        tmpMonth=[]
        tmpMonth.append(7)
        tmpMonth.append('Julio')
        tmpMonth.append(8)
        vecMonth.append(tmpMonth)

        tmpMonth=[]
        tmpMonth.append(8)
        tmpMonth.append('Agosto')
        tmpMonth.append(9)
        vecMonth.append(tmpMonth)

        tmpMonth=[]
        tmpMonth.append(9)
        tmpMonth.append('Septiembre')
        tmpMonth.append(10)
        vecMonth.append(tmpMonth)

        tmpMonth=[]
        tmpMonth.append(10)
        tmpMonth.append('Octubre')
        tmpMonth.append(11)
        vecMonth.append(tmpMonth)

        tmpMonth=[]
        tmpMonth.append(11)
        tmpMonth.append('Noviembre')
        tmpMonth.append(12)
        vecMonth.append(tmpMonth)

        tmpMonth=[]
        tmpMonth.append(12)
        tmpMonth.append('Diciembre')
        tmpMonth.append(1)
        vecMonth.append(tmpMonth)

    return dict(project = project, year = year, vecMonth=vecMonth)