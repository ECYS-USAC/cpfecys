@auth.requires_login()
@auth.requires(auth.has_membership('Student') or auth.has_membership('Teacher') or auth.has_membership('Super-Administrator') or auth.has_membership('Academic') or auth.has_membership('Ecys-Administrator'))
def courses_list():
    session.attachment_list = []
    session.attachment_list_temp = []
    session.attachment_list_temp2 = []
    session.notification_subject = ''
    session.notification_message = ''

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
    
    if auth.has_membership('Academic'):
        academic_var = db.academic(db.academic.id_auth_user==auth.user.id)
    pass

    if(auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator')):
        periods = db(db.period_year).select()

    else:
        periods_temp = db(db.period_year).select()
        periods = []
        for period_temp in periods_temp:
            added = False
            if auth.has_membership('Student') or auth.has_membership('Teacher'):
                try:
                    if db((db.user_project.assigned_user==auth.user.id)&\
                        (db.user_project.period == db.period_year.id)&\
                        ((db.user_project.period <= period_temp.id) & \
                        ((db.user_project.period + db.user_project.periods) > period_temp.id))).select(db.user_project.ALL).first() is not None:
                        periods.append(period_temp)
                        added = True
                except:
                    None
            if auth.has_membership('Academic'):
                try:
                    if db((db.academic_course_assignation.carnet==academic_var.id)&(db.academic_course_assignation.semester==period_temp.id)).select().first() is not None:
                        if added == False:
                            periods.append(period_temp)

                except:
                    None


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
        None
    else:
        if request.vars['period']!='':
            period = request.vars['period']
            period = db(db.period_year.id==period).select().first()
        else:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

    response.view='activity_control/courses_list.html'
    if (auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator')):
        #coursesAdmin = db(db.project.area_level==area.id).select()
        coursesAdmin = []
        for course in db(db.project.area_level==area.id).select(orderby=db.project.name):
            average_laboratory = float(0)
            average_class = float(0)

            for letter in 'lc':
                matrix_category = []
                num_category = 0
                category_grade_total = 0

                laboratory_var = False
                if letter == 'l':
                    laboratory_var=True
                pass

                for category_var in db((db.course_activity_category.assignation == course.id) &(db.course_activity_category.semester== period.id)&(db.course_activity_category.laboratory==laboratory_var)).select() :
                    if category_var.category.category != 'Laboratorio':
                        dont_pass = False
                        
                        if dont_pass == False:

                            average=float(0)
                            total_activity=float(0)
                            num_activity=0
                            matrix_specific_grade = []
                            activity_grade_total=float(0)
                            for activity_var in db((db.course_activity.course_activity_category == category_var.id)).select() : 
                                total_grades = db(db.grades.activity==activity_var.id).count()
                                if total_grades != 0:
                                    averageA = db.executesql('select avg(grade) as average from grades where activity='+str(activity_var.id)+';',as_dict=True)
                                    for d0 in averageA:
                                        if d0['average']!=None:
                                            average=float(d0['average'])
                                        pass
                                    pass
                                    if category_var.specific_grade==False:
                                        total_activity=total_activity+average
                                    else:
                                        temp_vect2 = []
                                        temp_vect2.append(average*(float(activity_var.grade))/100)
                                        temp_vect2.append(float(activity_var.grade))
                                        matrix_specific_grade.append(temp_vect2)
                                        activity_grade_total=activity_grade_total+float(activity_var.grade)
                                    pass #-------if-category_var.specific_grade==False
                                    num_activity=num_activity+1
                                pass #-------if total_grades != 0
                            pass #-------for-activity_var

                            try:
                                if category_var.specific_grade==False:
                                    temp_vect = []
                                    
                                    temp_vect.append((total_activity)/(num_activity)) 
                                    temp_vect.append(float(category_var.grade)) 
                                    matrix_category.append(temp_vect) 
                                    if total_activity != 0:
                                        category_grade_total = category_grade_total + category_var.grade
                                    pass
                                else:
                                    temp_vect = []
                                    for var_x in matrix_specific_grade: 
                                        total_activity = total_activity+((var_x[0])*float(category_var.grade)/(activity_grade_total))
                                    pass
                                    if total_activity != 0:
                                        temp_vect.append(total_activity*100/float(category_var.grade)) 
                                        temp_vect.append(float(category_var.grade)) 
                                        matrix_category.append(temp_vect) 
                                        category_grade_total = category_grade_total + category_var.grade
                                    pass
                                pass
                            except:
                                None
                            pass
                            num_category = num_category + 1
                        pass
                    
                    else:
                        
                        validate_laboratory_var = None
                        try:
                            academic_assig = db(db.academic_course_assignation.id == request.vars['academic'] ).select().first()
                            validate_laboratory_var = db((db.validate_laboratory.carnet == academic_assig.carnet) & (db.validate_laboratory.semester == academic_assig.semester) & (db.validate_laboratory.project == academic_assig.assignation)).select().first()
                        except:
                            None
                        pass
                        
                        

                        if validate_laboratory_var is not None:
                            temp_vect = []
                            temp_vect.append(validate_laboratory_var.grade) 
                            temp_vect.append(float(category_var.grade)) 
                            matrix_category.append(temp_vect) 
                            category_grade_total = category_grade_total + category_var.grade
                        elif average_laboratory != 0:
                            temp_vect = []
                            temp_vect.append(average_laboratory) 
                            temp_vect.append(float(category_var.grade)) 
                            matrix_category.append(temp_vect) 
                            category_grade_total = category_grade_total + category_var.grade
                        pass
                    pass
                pass #-------for-category_var


                #----------------------Calculing Total Average----------
                total_average=float(0)
                for var_x in matrix_category: 
                    total_average = total_average + (var_x[0]*var_x[1]/float(category_grade_total))
                pass

                if letter == 'l':
                    average_laboratory = total_average
                else:
                    average_class = total_average
                pass
                
            pass
            coursesAdmin.append([course.id, course.name, average_class,average_laboratory])
    elif auth.has_membership('Teacher'):
        coursesAdmin =  db((db.user_project.assigned_user==auth.user.id)&\
                        (db.user_project.period == db.period_year.id)&\
                        ((db.user_project.period <= period.id) & \
                        ((db.user_project.period + db.user_project.periods) > period.id))&\
                        (db.user_project.project==db.project.id)&\
                        (db.project.area_level==area.id) ).select()
    elif auth.has_membership('Student'):
        coursesAdmin = db((db.user_project.assigned_user==auth.user.id)&\
                        (db.user_project.period == db.period_year.id)&\
                        ((db.user_project.period <= period.id) & \
                        ((db.user_project.period + db.user_project.periods) > period.id))&\
                        (db.user_project.project==db.project.id)&\
                        (db.project.area_level==area.id) ).select()
        countcoursesAdminT = len(coursesAdmin)

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


    visited = db((db.page_visited.user_id == auth.user.id) & (db.page_visited.page_name == 'courses_list')).select().first()
    return dict(visited = visited, coursesAdmin = coursesAdmin, countcoursesAdminT=countcoursesAdminT, coursesStudent=coursesStudent, coursesStudentT=coursesStudentT, split_name=split_name, split_section=split_section, periods=periods,period=period,periodo=period, currentyear_period = cpfecys.current_year_period())


@auth.requires_login()
@auth.requires(auth.has_membership('Student') or auth.has_membership('Academic') or auth.has_membership('Teacher') or auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
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

    
    assigned_to_project = False
    assigantion = None

    if auth.has_membership('Super-Administrator') == False and auth.has_membership('Ecys-Administrator') == False :
        try:
            assigantion = db((db.user_project.assigned_user==auth.user.id)&\
                        (db.user_project.project == project_var)&\
                        ((db.user_project.period <= year.id) & \
                        ((db.user_project.period + db.user_project.periods) > year.id))).select(db.user_project.ALL).first() 
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
            else:
                assigned_to_project = True
        except:
            session.flash=T('Not valid Action.')
            redirect(URL('default','index'))
    

    visited = db((db.page_visited.user_id == auth.user.id) & (db.page_visited.page_name == 'students_control')).select().first()

    return dict(project = project_var, year = year.id , name = project_select.name, nameP=(T(year.period.name)+" "+str(year.yearp)), assigned_to_project = assigned_to_project, visited = visited)



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

    course_ended = False
    course_ended_var = db((db.course_ended.project==var_project.id) & (db.course_ended.period==var_period.id) ).select().first()
    if course_ended_var != None:
        if course_ended_var.finish == True:
            course_ended=True

    if course_ended_var != None:
        if (auth.has_membership('Super-Administrator') == False and auth.has_membership('Ecys-Administrator') == False) and (course_ended_var.finish == True):
            session.flash = T('Not valid Action.')
            redirect(URL('default', 'index'))
    
    actual_period = True
    for date_var in db((db.student_control_period.period_name==T(str(cpfecys.current_year_period().period.name))+" "+str(cpfecys.current_year_period().yearp))).select():
        if  ( (var_activity.date_start < date_var.date_start_semester) or (var_activity.date_finish < date_var.date_start_semester) ):
            actual_period = False
            if (auth.has_membership('Super-Administrator') == False and auth.has_membership('Ecys-Administrator') == False) :
                session.flash = T('The activity date is out of this semester.')
                redirect(URL('default', 'index'))
        pass      
    pass

    if (auth.has_membership('Super-Administrator') == False and auth.has_membership('Ecys-Administrator') == False):

        assigantion = db((db.user_project.assigned_user==auth.user.id)&\
                        (db.user_project.project == var_project)&\
                        ((db.user_project.period <= var_period.id) & \
                        ((db.user_project.period + db.user_project.periods) > var_period.id))).select(db.user_project.ALL).first()

        exception_query = db(db.course_laboratory_exception.project == id_project).select().first()
        if exception_query is None:
            exception_s_var = False
            exception_t_var = False
        else:
            exception_t_var = exception_query.t_edit_lab
            exception_s_var = exception_query.s_edit_course
        if (assigantion is None) or (auth.has_membership('Teacher') and var_activity.laboratory == True and exception_t_var == False) or (auth.has_membership('Student') and var_activity.laboratory == False and exception_s_var == False and var_activity.teacher_permition==False and var_activity.course_activity_category.teacher_permition==False):
            session.flash=T('You do not have permission to view course requests')
            redirect(URL('default','index'))
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


    return dict(academic_assig=academic_assig, var_period=var_period, var_activity=var_activity, var_project=var_project, request_change_var =request_change_var, actual_period = actual_period, course_ended = course_ended)


@auth.requires_login()
@auth.requires(auth.has_membership('Student') or auth.has_membership('Teacher') or auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
def grades():
    id_activity = request.vars['activity']
    id_project = request.vars['project']
    id_year = request.vars['year']
    coment = request.vars['coment']
    if coment is None:
        coment = ""

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
        academic_assig =  db((db.academic.id==db.academic_course_assignation.carnet)&(db.academic_course_assignation.assignation==id_project) & (db.academic_course_assignation.semester==id_year) &  (db.academic_course_assignation.laboratorio==True)).select(orderby=db.academic.carnet)
    else:
        academic_assig =  db((db.academic.id==db.academic_course_assignation.carnet)&(db.academic_course_assignation.assignation==id_project) & (db.academic_course_assignation.semester==id_year)).select(orderby=db.academic.carnet)

    tempAcademic=[]
    for acaT in academic_assig:
        tempAcademic.append(acaT.academic_course_assignation)

    actual_period = True
    for date_var in db((db.student_control_period.period_name==T(str(cpfecys.current_year_period().period.name))+" "+str(cpfecys.current_year_period().yearp))).select():
        if  ( (var_activity.date_start < date_var.date_start_semester) or (var_activity.date_finish < date_var.date_start_semester) ):
            actual_period = False
        pass      
    pass
    
    course_ended = False
    course_ended_var = db((db.course_ended.project==var_project.id) & (db.course_ended.period==var_period.id) ).select().first()
    if course_ended_var != None:
        if course_ended_var.finish == True:
            course_ended=True

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

    #Request exist_activity_request_change
    exist_activity_request_change = False
    if db((db.requestchange_course_activity.activity==var_activity.id)&(db.requestchange_activity.status=='pending')&(db.requestchange_course_activity.requestchange_activity==db.requestchange_activity.id)).select().first() != None:
        exist_activity_request_change = True


    
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
        send_mail_var = False
        for carnet_id in carnet_list: 
            if (request.vars['op'] == "add_grade"):
                carnet_list = request.vars['carnet']
                grade_list = request.vars['grade']
                request.vars['grade'] = grade_list
            else:
                request.vars['grade'] = grade_list[cont_temp]
                cont_temp = cont_temp+1
            request.vars['carnet'] = carnet_id
            
            if request.vars['carnet'] != "":
                try:
                    academic_var =  db(db.academic.carnet==request.vars['carnet']).select().first()

                    assig_var =  db((db.academic_course_assignation.assignation==var_project.id) & (db.academic_course_assignation.semester==var_period.id) & (db.academic_course_assignation.carnet == academic_var.id)).select().first()
                      #--------------------------------------------INSERT GRADE-------------------------------------
                    if request_change_var == False:
                        if (exist_request_change == True or exist_activity_request_change == True ):
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
                                                        description = T('Inserted from Grades page')+" - "+coment
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
                        if (exist_activity_request_change == True ):
                            alert_message = True
                            message_var2 = T('Can not make operation because there is a pending request change. Please resolve it before proceeding.')
                            
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

                            send_mail_var = True
                        
                            

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
        if send_mail_var == True:
            #send mail
            project_name = var_project.name
            project_id = id_project
            check = db((db.user_project.assigned_user==auth.user.id)&\
                        (db.user_project.project == project_id)&\
                        ((db.user_project.period <= var_period.id) & \
                        ((db.user_project.period + db.user_project.periods) > var_period.id))).select(db.user_project.ALL).first()

                         #db.user_project(project = project_id, period = var_period.id, assigned_user = auth.user.id)
            #Message
            #users2 = db((db.auth_user.id==db.user_project.assigned_user)&(db.user_project.period == check.period) & (db.user_project.project==check.project)&(db.auth_membership.user_id==db.user_project.assigned_user)&(db.auth_membership.group_id==3)).select().first()
            try:
                users2 = db((db.auth_user.id==db.user_project.assigned_user)&\
                            (db.user_project.project == project_id)&\
                            ((db.user_project.period <= var_period.id) & \
                            ((db.user_project.period + db.user_project.periods) > var_period.id))&\
                            (db.auth_membership.user_id==db.user_project.assigned_user)&\
                            (db.auth_membership.group_id==3)).select().first()
                
                subject="Solicitud de cambio de notas - "+project_name
                message2="<br>Por este medio se le informa que el(la) practicante "+check.assigned_user.first_name+" "+check.assigned_user.last_name+" ha creado una solicitud de cambio en las notas del laboratorio del Curso de \""+project_name+"\"."
                message2=message2+"<br>Para aceptar o rechazar dicha solicitud dirigirse al control de solicitudes o al siguiente link: " +cpfecys.get_domain()+ "cpfecys/activity_control/solve_request_change_grades?course="+str(project_id)
                message2=message2+"<br>Saludos.<br><br>Sistema de Seguimiento de La Escuela de Ciencias y Sistemas<br>Facultad de Ingeniería - Universidad de San Carlos de Guatemala</html>"
                #Send Mail to the Teacher
                message="<html>Catedratico(a) "+users2.auth_user.first_name+" "+users2.auth_user.last_name+" reciba un cordial saludo.<br>"
                message3=message+message2

                fail1 = send_mail_to_students(message3,subject,users2.auth_user.email,check,var_period.period.name,var_period.yearp) 
                #fail1=0#Esto hay que quitarlo****************************************************************************************************************!!!!!!!
                if fail1==1:
                    alert_message = True
                    message_var2 = T("Request has been sent") + ". " + T("Failed to send email to teacher")
                
                else:
                    alert_message = True
                    message_var2 = T("Request has been sent") + ". " + T("Sent email to teacher")
            except:
                message_var2 = T("Request has been sent") + ". " + T("Failed to send email to teacher")
            
    pass
    return dict(academic_assig=tempAcademic, 
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
        add_grade_flash = add_grade_flash,
        exist_activity_request_change = exist_activity_request_change,
        coment = coment,
        actual_period = actual_period,
        course_ended = course_ended
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
@auth.requires_membership('Super-Administrator')
def partials():
    grid = SQLFORM.grid(db.partials, maxtextlength=100,csv=False,deletable=False,)
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

    assignation = db((db.user_project.assigned_user==auth.user.id)&\
                        (db.user_project.project == request.vars['project'])&\
                        ((db.user_project.period <= year.id) & \
                        ((db.user_project.period + db.user_project.periods) > year.id))).select(db.user_project.ALL).first()


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

                               
                total_var2 = float(0)
                if request.vars['type'] == 'course':
                   None
                else:
                    for project in db((db.course_activity_category.semester==year.id) & (db.course_activity_category.assignation==request.vars['project']) & (db.course_activity_category.laboratory==True)).select():

                        total_var2 = float(total_var2) +float(project.grade)
                    pass
                pass   

                select_change = db((db.request_change_weighting.status=='edit')&(db.request_change_weighting.period==int(year.id))&(db.request_change_weighting.project==request.vars['project'])).select().first()
                
                for detail_rc in db((db.request_change_weighting_detail.request_change_weighting==select_change.id) ).select():
                    
                    if detail_rc.operation_request == 'insert':
                        total_var2 = float(total_var2) + float(detail_rc.grade)

                    if detail_rc.operation_request == 'update':                        
                        total_var2 = float(total_var2) - float(detail_rc.course_category.grade)
                        total_var2 = float(total_var2) + float(detail_rc.grade)

                    if detail_rc.operation_request == 'delete':
                        total_var2 = float(total_var2) - float(detail_rc.course_category.grade)
                pass

               
                if float(total_var2) != float(100):
                    if total_var2 != None:
                        response.flash = "Error. "+ T("The sum of the weighting is incorrect") + ": " + str(total_var2)
                   
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
                    #check = db.user_project(project = check.id, period = year.id, assigned_user = auth.user.id)
                    #Message
                    #users2 = db((db.auth_user.id==db.user_project.assigned_user)&(db.user_project.period == check.period) & (db.user_project.project==check.project)&(db.auth_membership.user_id==db.user_project.assigned_user)&(db.auth_membership.group_id==3)).select().first()
                    try:
                        check = db((db.user_project.assigned_user==auth.user.id)&\
                            (db.user_project.project == request.vars['project'])&\
                            ((db.user_project.period <= int(request.vars['year'])) & \
                            ((db.user_project.period + db.user_project.periods) > int(request.vars['year']) ))).select(db.user_project.ALL).first()

                        users2 = db((db.auth_user.id==db.user_project.assigned_user)&\
                            (db.user_project.project == request.vars['project'])&\
                            ((db.user_project.period <= int(request.vars['year']) ) & \
                            ((db.user_project.period + db.user_project.periods) > int(request.vars['year']) ))&\
                            (db.auth_membership.user_id==db.user_project.assigned_user)&\
                            (db.auth_membership.group_id==3)).select().first()

                        subject="Solicitud de cambio de ponderación - "+project_name
                        message2="<br>Por este medio se le informa que el(la) practicante "+check.assigned_user.first_name+" "+check.assigned_user.last_name+" ha creado una solicitud de cambio en la ponderación del laboratorio del Curso de \""+project_name+"\"."
                        message2=message2+"<br>Para aceptar o rechazar dicha solicitud dirigirse al control de solicitudes o al siguiente link: " +cpfecys.get_domain()+ "cpfecys/activity_control/solve_request_change_weighting?course="+str(project_id)
                        message2=message2+"<br>Saludos.<br><br>Sistema de Seguimiento de La Escuela de Ciencias y Sistemas<br>Facultad de Ingeniería - Universidad de San Carlos de Guatemala</html>"
                        #Send Mail to the Teacher
                        message="<html>Catedratico(a) "+users2.auth_user.first_name+" "+users2.auth_user.last_name+" reciba un cordial saludo.<br>"
                        message3=message+message2
                        fail1 = send_mail_to_students(message3,subject,users2.auth_user.email,check,year_semester.name,year.yearp) 
                        #fail1=0#Esto hay que quitarlo****************************************************************************************************************!!!!!!!
                        if fail1==1:
                            response.flash = T("Request has been sent") + " - " + T("Failed to send email to teacher")
                        else:
                            response.flash = T("Request has been sent") + " - " + T("Sent email to teacher")                        
                    except:
                        None
                    return dict(name = project_name,
                        semester = year_semester.name,
                        year = year.yearp,
                        semestre2 = year,
                        project = request.vars['project'],
                        assignation=assignation)

    except:
        None

    return dict(name = check.name,
        semester = year_semester.name,
        year = year.yearp,
        semestre2 = year,
        project = request.vars['project'],
        assignation=assignation)

@auth.requires_login()
@auth.requires(auth.has_membership('Student') or auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator') or auth.has_membership('Teacher'))
def request_change_weighting_load():
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
    
    assignation = db((db.user_project.assigned_user==auth.user.id)&\
                        (db.user_project.project == project_id)&\
                        ((db.user_project.period <= year.id) & \
                        ((db.user_project.period + db.user_project.periods) > year.id))).select(db.user_project.ALL).first()



    if (assignation is None) & (auth.has_membership('Super-Administrator') == False) & (auth.has_membership('Ecys-Administrator') == False):
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
            course = db((db.user_project.assigned_user==auth.user.id)&\
                        (db.user_project.project == courseCheck)&\
                        ((db.user_project.period <= cpfecys.current_year_period().id) & \
                        ((db.user_project.period + db.user_project.periods) > cpfecys.current_year_period().id))).select(db.user_project.ALL).first()


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
            course = db((db.user_project.assigned_user==auth.user.id)&\
                        (db.user_project.project == courseCheck)&\
                        ((db.user_project.period <= cpfecys.current_year_period().id) & \
                        ((db.user_project.period + db.user_project.periods) > cpfecys.current_year_period().id))).select(db.user_project.ALL).first()

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

    assigantion = db((db.user_project.assigned_user==auth.user.id)&\
                        (db.user_project.project == request.vars['project'])&\
                        ((db.user_project.period <= year.id) & \
                        ((db.user_project.period + db.user_project.periods) > year.id))).select(db.user_project.ALL).first()

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
        assigantion = db((db.user_project.assigned_user==auth.user.id)&\
                        (db.user_project.project == project_var)&\
                        ((db.user_project.period <= year.id) & \
                        ((db.user_project.period + db.user_project.periods) > year.id))).select(db.user_project.ALL).first()


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
        else:
           None
    

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

    assigantion = db((db.user_project.assigned_user==auth.user.id)&\
                        (db.user_project.project == project)&\
                        ((db.user_project.period <= year.id) & \
                        ((db.user_project.period + db.user_project.periods) > year.id))).select(db.user_project.ALL).first()
    
    if assigantion is None:
        assigned_to_project = False
    else:
        assigned_to_project = True


    exception_query = db(db.course_laboratory_exception.project == request.vars['project']).select().first()
    
    if exception_query is None:
        exception_s_var = False
        exception_t_var = False
    else:
        exception_t_var = exception_query.t_edit_lab
        exception_s_var = exception_query.s_edit_course
        
    pass
    no_menu=True
    if (auth.has_membership('Super-Administrator')) or (auth.has_membership('Ecys-Administrator')) or (auth.has_membership('Teacher') and request.vars['type'] == "course"  and assigned_to_project == True) or (auth.has_membership('Student') and request.vars['type'] == "lab"  and assigned_to_project == True) or (auth.has_membership('Student')  and request.vars['type'] == "course" and exception_s_var == True  and assigned_to_project == True) or (auth.has_membership('Teacher')  and request.vars['type'] == "lab" and exception_t_var == True  and assigned_to_project == True):
        if str(request.vars['year']) == str(cpfecys.current_year_period().id):
            no_menu=False
        pass
    pass

    from datetime import datetime
    enddate=None
    for date_var in db((db.student_control_period.period_name==T(str(year.period.name))+" "+str(year.yearp))).select():
        var_exception = db((db.course_limit_exception.project == request.vars['project']) & (db.course_limit_exception.date_finish > datetime.now())).select().first()
        if var_exception != None:
            var_date_finish = var_exception.date_finish
        else:
            var_date_finish = date_var.date_finish
        pass
        if datetime.now() > date_var.date_start and datetime.now() < var_date_finish:
            enddate=var_date_finish                 
        pass
    pass


    exception_query = db(db.course_laboratory_exception.project == request.vars['project']).select().first()
    if exception_query is None:
      exception_s_var = False
      exception_t_var = False
    else:
      exception_t_var = exception_query.t_edit_lab
      exception_s_var = exception_query.s_edit_course
    pass

    temp_op = request.vars['op']
    if ((auth.has_membership('Super-Administrator') == False) & (auth.has_membership('Ecys-Administrator') == False)) & ( (((auth.has_membership('Teacher') == False) & (no_menu==True or enddate == None) & (exception_s_var == False)) or ((auth.has_membership('Teacher') == True) & (no_menu==True))) & (temp_op == "updateCategory" or temp_op == "addCategory" or temp_op == "getPreviousWeighting" or temp_op == "removeCategory")):
        return "<center>"+T("Action not allowed")+"</center>"

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

    assigantion = db((db.user_project.assigned_user==auth.user.id)&\
                        (db.user_project.project == project.id)&\
                        ((db.user_project.period <= year.id) & \
                        ((db.user_project.period + db.user_project.periods) > year.id))).select(db.user_project.ALL).first()

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
    assigantion = db((db.user_project.assigned_user==auth.user.id)&\
                        (db.user_project.project == project)&\
                        ((db.user_project.period <= year.id) & \
                        ((db.user_project.period + db.user_project.periods) > year.id))).select(db.user_project.ALL).first()


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
    check = db((db.user_project.assigned_user==auth.user.id)&\
                        (db.user_project.project == request.vars['project'])&\
                        ((db.user_project.period <= int(request.vars['year'])) & \
                        ((db.user_project.period + db.user_project.periods) > int(request.vars['year']) ))).select(db.user_project.ALL).first()


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
                functionAction=False
                rgrades = db((db.request_change_grades.status=='pending')&(db.request_change_grades.period==int(year.id))&(db.request_change_grades.project==int(project.id))).select()
                if rgrades.first()==None:
                    functionAction=True
                else:
                    validation_change=False
                    acrc_t = db((db.course_activity.course_activity_category==int(request.vars['category']))&(db.course_activity.semester==int(year.id))&(db.course_activity.assignation==int(project.id))&(db.course_activity.laboratory==True)).select()
                    for rgrades_iterator in rgrades:
                        for acrc in acrc_t:
                            if rgrades_iterator.activity==acrc.id:
                                validation_change=True
                            pass
                        pass
                    pass
                    if validation_change==False:
                        functionAction=True
                    else:
                        if Draft!=None:
                            db(db.requestchange_activity.id==Draft.id).delete()
                        pass
                    pass
                pass
                if functionAction==True:
                    #Update the request change activity
                    db(db.requestchange_activity.id==Draft.id).update(description=request.vars['activity_description_request_var'],status='Pending', date_request = datetime.datetime.now())
                    Draft = db((db.requestchange_activity.status=='Pending')&(db.requestchange_activity.semester==year.id)&(db.requestchange_activity.course==project.id)).select().first()
                    #Log of request change activity
                    idR = db.requestchange_activity_log.insert(user_request=Draft.user_id.username, roll_request='Student', status='Pending', description=request.vars['activity_description_request_var'], date_request=Draft.date_request, category_request=Draft.course_activity_category.category.category, semester=year.period.name, yearp=year.yearp, course=project.name)
                    activitiesChange = db(db.requestchange_course_activity.requestchange_activity==Draft.id).select()
                    for actChange in activitiesChange:
                        db.requestchange_course_activity_log.insert(requestchange_activity=idR, operation_request=actChange.operation_request, activity=actChange.activity, name=actChange.name, description=actChange.description, grade=actChange.grade, date_start=actChange.date_start, date_finish=actChange.date_finish)

                    check = db((db.user_project.assigned_user==auth.user.id)&\
                        (db.user_project.project == request.vars['project'])&\
                        ((db.user_project.period <= int(request.vars['year'])) & \
                        ((db.user_project.period + db.user_project.periods) > int(request.vars['year']) ))).select(db.user_project.ALL).first()

                    users2 = db((db.auth_user.id==db.user_project.assigned_user)&\
                        (db.user_project.project == request.vars['project'])&\
                        ((db.user_project.period <= int(request.vars['year']) ) & \
                        ((db.user_project.period + db.user_project.periods) > int(request.vars['year']) ))&\
                        (db.auth_membership.user_id==db.user_project.assigned_user)&\
                        (db.auth_membership.group_id==3)).select().first()

                    try:
                        subject="Solicitud de cambio de actividades - "+project.name
                        
                        message2="<br>Por este medio se le informa que el(la) practicante "+check.assigned_user.first_name+" "+check.assigned_user.last_name+" ha creado una solicitud de cambio de actividades en la categoría \""+Draft.course_activity_category.category.category+"\" dentro de la ponderación de laboratorio del Curso de \""+project.name+"\"."
                        message2=message2+"<br>Para aceptar o rechazar dicha solicitud dirigirse al control de solicitudes o al siguiente link: " +  cpfecys.get_domain()+ "cpfecys/activity_control/solve_request_change_activity?course="+str(request.vars['project'])
                        message2=message2+"<br>Saludos.<br><br>Sistema de Seguimiento de La Escuela de Ciencias y Sistemas<br>Facultad de Ingeniería - Universidad de San Carlos de Guatemala</html>"

                        #Send Mail to the Teacher
                        message="<html>catedratico(a) "+users2.auth_user.first_name+" "+users2.auth_user.last_name+" reciba un cordial saludo.<br>"
                        message3=message+message2
                        fail1 = send_mail_to_students(message3,subject,users2.auth_user.email,check,year.period.name,year.yearp)
                        #fail1=0#Esto hay que quitarlo****************************************************************************************************************!!!!!!!
                        #Refresh the var Draft
                        Draft=None
                        if fail1==1:
                            stateRequest=2
                        else:
                            stateRequest=4
                    except:
                        stateRequest=2

                else:
                    Draft=None
                    stateRequest=5


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
        courses_request = db((db.user_project.assigned_user==auth.user.id)&\
                        (db.user_project.project==db.project.id)&\
                        (db.project.area_level==area.id)&\
                        ((db.user_project.period <= cpfecys.current_year_period().id) & \
                        ((db.user_project.period + db.user_project.periods) > cpfecys.current_year_period().id))).select()


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
                        db.course_activity_log.insert(user_name=auth.user.username, roll=rol_temp, operation_log='insert', course= Accepted.course.name, yearp=cpfecys.current_year_period().yearp, period=T(cpfecys.current_year_period().period.name), metric='T', after_course_activity_category=Accepted.course_activity_category.category.category, after_name=actChange.name, after_description=actChange.description, after_grade =  actChange.grade, after_laboratory = 'T', after_teacher_permition = 'F', after_date_start = actChange.date_start, after_date_finish = actChange.date_finish)
                        db.course_activity.insert(course_activity_category = Accepted.course_activity_category, name=actChange.name, description=actChange.description, grade =  actChange.grade, semester = cpfecys.current_year_period().id,  assignation = Accepted.course,  laboratory = 'T', teacher_permition = 'F', date_start = actChange.date_start, date_finish = actChange.date_finish)
                    elif actChange.operation_request=='delete':
                        db.course_activity_log.insert(user_name=auth.user.username, roll=rol_temp, operation_log='delete', course= Accepted.course.name, yearp=cpfecys.current_year_period().yearp, period=T(cpfecys.current_year_period().period.name), metric='T', before_course_activity_category=Accepted.course_activity_category.category.category, before_name=actChange.name, before_description=actChange.description, before_grade =  actChange.grade, before_laboratory = 'T', before_teacher_permition = 'F', before_date_start = actChange.date_start, before_date_finish = actChange.date_finish)
                        db(db.course_activity.id==actChange.activity).delete()
                    elif actChange.operation_request=='update':
                        activityOldR=db(db.course_activity.id==actChange.activity).select().first()
                        db.course_activity_log.insert(user_name=auth.user.username, roll=rol_temp, operation_log='update', course= Accepted.course.name, yearp=cpfecys.current_year_period().yearp, period=T(cpfecys.current_year_period().period.name), metric='T', before_course_activity_category=activityOldR.course_activity_category.category.category, before_name=activityOldR.name, before_description=activityOldR.description, before_grade =  activityOldR.grade, before_laboratory = activityOldR.laboratory, before_teacher_permition = activityOldR.teacher_permition, before_date_start = activityOldR.date_start, before_date_finish = activityOldR.date_finish, after_course_activity_category=Accepted.course_activity_category.category.category, after_name=actChange.name, after_description=actChange.description, after_grade =  actChange.grade, after_laboratory = 'T', after_teacher_permition = 'F', after_date_start = actChange.date_start, after_date_finish = actChange.date_finish)
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
            course = db((db.user_project.assigned_user==auth.user.id)&\
                        (db.user_project.project == courseCheck)&\
                        ((db.user_project.period <= cpfecys.current_year_period().id) & \
                        ((db.user_project.period + db.user_project.periods) > cpfecys.current_year_period().id))).select(db.user_project.ALL).first()
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

    if request.vars['op']=="acceptRequestChange":
        request_change_var = db(db.request_change_grades.id == request.vars['Idrequest']).select().first()
        if request_change_var.status != 'pending':
            return T('Request Change has been resolved.')
            



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

    assigantion = db((db.user_project.assigned_user==auth.user.id)&\
                        (db.user_project.project == project.id)&\
                        ((db.user_project.period <= year.id) & \
                        ((db.user_project.period + db.user_project.periods) > year.id))).select(db.user_project.ALL).first()

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
@auth.requires(auth.has_membership('Student') or auth.has_membership('Teacher') or auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
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
            grid = SQLFORM.grid(query, csv=False, paginate=10, searchable=False)
        elif auth.has_membership('Teacher'):
            assigantion = db((db.user_project.assigned_user==auth.user.id)&\
                        (db.user_project.project == project)&\
                        ((db.user_project.period <= year.id) & \
                        ((db.user_project.period + db.user_project.periods) > year.id))).select(db.user_project.ALL).first()
            if assigantion is None:
                session.flash = T('Not valid Action.')
                redirect(URL('default','index'))
            else:
                if exception_t_var==True:
                    query = ((db.course_activity_without_metric.semester==year.id) & (db.course_activity_without_metric.assignation==project.id))
                    grid = SQLFORM.grid(query, csv=False, paginate=10, searchable=False)
                else:
                    db.course_activity_without_metric.laboratory.writable = False
                    db.course_activity_without_metric.laboratory.default = False
                    query = ((db.course_activity_without_metric.semester==year.id) & (db.course_activity_without_metric.assignation==project.id)&(db.course_activity_without_metric.laboratory==False))
                    grid = SQLFORM.grid(query, csv=False, paginate=10, searchable=False)
        elif auth.has_membership('Student'):
            assigantion = db((db.user_project.assigned_user==auth.user.id)&\
                        (db.user_project.project == project)&\
                        ((db.user_project.period <= year.id) & \
                        ((db.user_project.period + db.user_project.periods) > year.id))).select(db.user_project.ALL).first()
            if assigantion is None:
                session.flash = T('Not valid Action.')
                redirect(URL('default','index'))
            else:
                db.course_activity_without_metric.teacher_permition.writable = False
                if exception_s_var==True:
                    query = ((db.course_activity_without_metric.semester==year.id) & (db.course_activity_without_metric.assignation==project.id))
                    grid = SQLFORM.grid(query, csv=False, paginate=10, searchable=False)
                else:
                    db.course_activity_without_metric.laboratory.writable = False
                    db.course_activity_without_metric.laboratory.default = True
                    query = ((db.course_activity_without_metric.semester==year.id) & (db.course_activity_without_metric.assignation==project.id)& ((db.course_activity_without_metric.laboratory==True) | ((db.course_activity_without_metric.laboratory== False)&(db.course_activity_without_metric.teacher_permition==True))))
                    grid = SQLFORM.grid(query, csv=False, paginate=10, searchable=False)
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
#-----------------------------------------Laboratory revalidation--------------------------------------------------------

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
            if auth.has_membership('Super-Administrator') == False and auth.has_membership('Ecys-Administrator')==False:
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
        else:
            if auth.has_membership('Super-Administrator') == False and auth.has_membership('Ecys-Administrator')==False:
                assigantion = db((db.user_project.assigned_user==auth.user.id)&\
                        (db.user_project.project == project)&\
                        ((db.user_project.period <= year.id) & \
                        ((db.user_project.period + db.user_project.periods) > year.id))).select(db.user_project.ALL).first()
                if assigantion is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))

    #Grid
    query = ((db.validate_laboratory.semester==year.id)&(db.validate_laboratory.project==project.id)&(db.validate_laboratory.validation_type==True))
    grid=None
    db.validate_laboratory.id.readable = False
    db.validate_laboratory.id.writable = False
    db.validate_laboratory.project.readable = False
    db.validate_laboratory.project.writable = False
    db.validate_laboratory.project.default = project.id
    db.validate_laboratory.semester.readable = False
    db.validate_laboratory.semester.writable = False
    db.validate_laboratory.semester.default = year.id
    db.validate_laboratory.validation_type.readable = False
    db.validate_laboratory.validation_type.writable = False
    db.validate_laboratory.validation_type.default = True
    if cpfecys.current_year_period().id != year.id:
        no_actionsAll=True
        if auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'):
            if 'edit' in request.args:
                db.validate_laboratory.carnet.writable = False
                grid = SQLFORM.grid(query, csv=False, paginate=10, oncreate=oncreate_validate_laboratory, onupdate=onupdate_validate_laboratory, ondelete=ondelete_validate_laboratory, searchable=False)
            else:
                grid = SQLFORM.grid(query, csv=False, paginate=10, deletable=False, oncreate=oncreate_validate_laboratory, onupdate=onupdate_validate_laboratory, ondelete=ondelete_validate_laboratory, searchable=False)
        else:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))
    else:
        no_actionsAll=False
        
        #Check if the course has endend
        course_ended_var = db((db.course_ended.project==project.id) & (db.course_ended.period==year.id) ).select().first()
        if course_ended_var != None:
            if course_ended_var.finish == True:
                no_actionsAll=True


        #Check the time of the semester is not over
        if no_actionsAll==False:
            #Time limit of semester parameter
            from datetime import datetime
            date1=None
            tiempo=str(datetime.now())
            dateInicialP = db.executesql('SELECT date(\''+tiempo+'\');',as_dict=True)
            for d0 in dateInicialP:
                date1=d0['date(\''+tiempo+'\')']
            date_var = db((db.student_control_period.period_name==(T(year.period.name)+" "+str(year.yearp)))).select().first()
            if date1 >= date_var.date_start_semester and date1 <= date_var.date_finish_semester:
                if year.period == 1:
                    tiempo=str(datetime.strptime(str(year.yearp) + '-01-01', "%Y-%m-%d"))
                    dateInicialP = db.executesql('SELECT date(\''+tiempo+'\');',as_dict=True)
                    for d0 in dateInicialP:
                        start=d0['date(\''+tiempo+'\')']
                    tiempo=str(datetime.strptime(str(year.yearp) + '-06-01', "%Y-%m-%d"))
                    dateInicialP = db.executesql('SELECT date(\''+tiempo+'\');',as_dict=True)
                    for d0 in dateInicialP:
                        end=d0['date(\''+tiempo+'\')']
                    if date1>=start and date1<end:
                        None
                    else:
                        no_actionsAll=True
                else:
                    tiempo=str(datetime.strptime(str(year.yearp) + '-06-01', "%Y-%m-%d"))
                    dateInicialP = db.executesql('SELECT date(\''+tiempo+'\');',as_dict=True)
                    for d0 in dateInicialP:
                        start=d0['date(\''+tiempo+'\')']
                    tiempo=str(datetime.strptime(str(year.yearp) + '-12-31', "%Y-%m-%d"))
                    dateInicialP = db.executesql('SELECT date(\''+tiempo+'\');',as_dict=True)
                    for d0 in dateInicialP:
                        end=d0['date(\''+tiempo+'\')']
                    if date1>=start and date1<=end:
                        None
                    else:
                        no_actionsAll=True
            else:
                no_actionsAll=True


        #If is teacher, check if he has permitions
        if no_actionsAll==False and auth.has_membership('Teacher'):
            exception_query = db(db.course_laboratory_exception.project == project.id).select().first()
            if exception_query is not None:
                if exception_query.t_edit_lab == False:
                    no_actionsAll=True
            else:
                no_actionsAll=True


        #Show options
        if no_actionsAll==False:
            if 'edit' in request.args:
                db.validate_laboratory.carnet.writable = False
                grid = SQLFORM.grid(query, csv=False, paginate=10, oncreate=oncreate_validate_laboratory, onupdate=onupdate_validate_laboratory, ondelete=ondelete_validate_laboratory, searchable=False)
            else:
                grid = SQLFORM.grid(query, csv=False, paginate=10, oncreate=oncreate_validate_laboratory, onupdate=onupdate_validate_laboratory, ondelete=ondelete_validate_laboratory, searchable=False)
        else:
            if auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'):
                if 'edit' in request.args:
                    db.validate_laboratory.carnet.writable = False
                    grid = SQLFORM.grid(query, csv=False, paginate=10, oncreate=oncreate_validate_laboratory, onupdate=onupdate_validate_laboratory, ondelete=ondelete_validate_laboratory, searchable=False)
                else:
                    grid = SQLFORM.grid(query, csv=False, paginate=10, deletable=False, oncreate=oncreate_validate_laboratory, onupdate=onupdate_validate_laboratory, ondelete=ondelete_validate_laboratory, searchable=False)
            else:
                grid = SQLFORM.grid(query, csv=False, create=False, editable=False, deletable=False, paginate=10, searchable=False)


    academic_assig3 = db((db.academic.id==db.academic_course_assignation.carnet)&(db.academic_course_assignation.semester == request.vars['year']) & (db.academic_course_assignation.assignation==request.vars['project'])).select(orderby=db.academic.carnet)
    students=[]
    for acaT in academic_assig3:
        students.append(acaT.academic_course_assignation)
    return dict(year = year, project = project, grid=grid, students=students, no_actionsAll=no_actionsAll)

def oncreate_validate_laboratory(form):
    #Check if has one of this roles
    if auth.has_membership('Super-Administrator')==False and auth.has_membership('Ecys-Administrator')==False and auth.has_membership('Teacher')==False and auth.has_membership('Student')==False:
        db(db.validate_laboratory.id==form.vars.id).delete()
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))

    #Start the process
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
            if auth.has_membership('Super-Administrator') == False and auth.has_membership('Ecys-Administrator')==False:
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
        else:
            if auth.has_membership('Super-Administrator') == False and auth.has_membership('Ecys-Administrator')==False:
                assigantion = db((db.user_project.assigned_user==auth.user.id)&\
                        (db.user_project.project == project)&\
                        ((db.user_project.period <= year.id) & \
                        ((db.user_project.period + db.user_project.periods) > year.id))).select(db.user_project.ALL).first()

                if assigantion is None:
                    db(db.validate_laboratory.id==form.vars.id).delete()
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))


    no_actionsAll=False
    if cpfecys.current_year_period().id != year.id:
        no_actionsAll==True
    else:
        #Check if the course has endend
        course_ended_var = db((db.course_ended.project==project.id) & (db.course_ended.period==year.id) ).select().first()
        if course_ended_var != None:
            if course_ended_var.finish == True:
                no_actionsAll=True

        #Check the time of the semester is not over
        if no_actionsAll==False:
            #Time limit of semester parameter
            from datetime import datetime
            date1=None
            tiempo=str(datetime.now())
            dateInicialP = db.executesql('SELECT date(\''+tiempo+'\');',as_dict=True)
            for d0 in dateInicialP:
                date1=d0['date(\''+tiempo+'\')']
            date_var = db((db.student_control_period.period_name==(T(year.period.name)+" "+str(year.yearp)))).select().first()
            if date1 >= date_var.date_start_semester and date1 <= date_var.date_finish_semester:
                if year.period == 1:
                    tiempo=str(datetime.strptime(str(year.yearp) + '-01-01', "%Y-%m-%d"))
                    dateInicialP = db.executesql('SELECT date(\''+tiempo+'\');',as_dict=True)
                    for d0 in dateInicialP:
                        start=d0['date(\''+tiempo+'\')']
                    tiempo=str(datetime.strptime(str(year.yearp) + '-06-01', "%Y-%m-%d"))
                    dateInicialP = db.executesql('SELECT date(\''+tiempo+'\');',as_dict=True)
                    for d0 in dateInicialP:
                        end=d0['date(\''+tiempo+'\')']
                    if date1>=start and date1<end:
                        None
                    else:
                        no_actionsAll=True
                else:
                    tiempo=str(datetime.strptime(str(year.yearp) + '-06-01', "%Y-%m-%d"))
                    dateInicialP = db.executesql('SELECT date(\''+tiempo+'\');',as_dict=True)
                    for d0 in dateInicialP:
                        start=d0['date(\''+tiempo+'\')']
                    tiempo=str(datetime.strptime(str(year.yearp) + '-12-31', "%Y-%m-%d"))
                    dateInicialP = db.executesql('SELECT date(\''+tiempo+'\');',as_dict=True)
                    for d0 in dateInicialP:
                        end=d0['date(\''+tiempo+'\')']
                    if date1>=start and date1<=end:
                        None
                    else:
                        no_actionsAll=True
            else:
                no_actionsAll=True

        #If is teacher, check if he has permitions
        if no_actionsAll==False and auth.has_membership('Teacher'):
            exception_query = db(db.course_laboratory_exception.project == project.id).select().first()
            if exception_query is not None:
                if exception_query.t_edit_lab == False:
                    no_actionsAll=True
            else:
                no_actionsAll=True



    if no_actionsAll==False:
        roll_var=''
        if auth.has_membership('Super-Administrator'):
            roll_var='Super-Administrator'
        elif auth.has_membership('Ecys-Administrator'):
            roll_var='Ecys-Administrator'
        elif auth.has_membership('Teacher'):
            roll_var='Teacher'
        elif auth.has_membership('Student'):
            roll_var='Student'
        else:
            db(db.validate_laboratory.id==form.vars.id).delete()
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        usr2 = db((db.validate_laboratory.id != form.vars.id) & (db.validate_laboratory.semester == request.vars['year']) & (db.validate_laboratory.project == request.vars['project']) & (db.validate_laboratory.carnet == form.vars.carnet)).select().first()
        if usr2 is not None:
            db(db.validate_laboratory.id==form.vars.id).delete()
            session.flash = T('Error. There is a registration renewal or equivalence laboratory student in the course.')
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
                                    description = T('Inserted from validation page'),
                                    validation_type=True
                                     )
    else:
        if auth.has_membership('Super-Administrator') == True or auth.has_membership('Ecys-Administrator')==True:
            if request.vars['description_request'] is None or request.vars['description_request']=='':
                db(db.validate_laboratory.id==form.vars.id).delete()
                session.flash=T('You must enter a description of the modification.')
            else:
                roll_var='Ecys-Administrator'
                if auth.has_membership('Super-Administrator'):
                    roll_var='Super-Administrator'

                usr2 = db((db.validate_laboratory.id != form.vars.id) & (db.validate_laboratory.semester == request.vars['year']) & (db.validate_laboratory.project == request.vars['project']) & (db.validate_laboratory.carnet == form.vars.carnet)).select().first()
                if usr2 is not None:
                    db(db.validate_laboratory.id==form.vars.id).delete()
                    session.flash = T('Error. There is a registration renewal or equivalence laboratory student in the course.')
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
                                            description = str(request.vars['description_request']),
                                            validation_type=True
                                             )
        else:
            db(db.validate_laboratory.id==form.vars.id).delete()
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

def ondelete_validate_laboratory(table_involved, id_of_the_deleted_record):
    #Check if has one of this roles
    if auth.has_membership('Super-Administrator')==False and auth.has_membership('Ecys-Administrator')==False and auth.has_membership('Teacher')==False and auth.has_membership('Student')==False:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))

    #Start the process
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
        else:
            if auth.has_membership('Super-Administrator') == False and auth.has_membership('Ecys-Administrator')==False:
                assigantion = db((db.user_project.assigned_user==auth.user.id)&\
                        (db.user_project.project == project)&\
                        ((db.user_project.period <= year.id) & \
                        ((db.user_project.period + db.user_project.periods) > year.id))).select(db.user_project.ALL).first()
                if assigantion is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))


    no_actionsAll=False
    #Check if the course has endend
    course_ended_var = db((db.course_ended.project==project.id) & (db.course_ended.period==year.id) ).select().first()
    if course_ended_var != None:
        if course_ended_var.finish == True:
            no_actionsAll=True

    #Check the time of the semester is not over
    if no_actionsAll==False:
        #Time limit of semester parameter
        from datetime import datetime
        date1=None
        tiempo=str(datetime.now())
        dateInicialP = db.executesql('SELECT date(\''+tiempo+'\');',as_dict=True)
        for d0 in dateInicialP:
            date1=d0['date(\''+tiempo+'\')']
        date_var = db((db.student_control_period.period_name==(T(year.period.name)+" "+str(year.yearp)))).select().first()
        if date1 >= date_var.date_start_semester and date1 <= date_var.date_finish_semester:
            if year.period == 1:
                tiempo=str(datetime.strptime(str(year.yearp) + '-01-01', "%Y-%m-%d"))
                dateInicialP = db.executesql('SELECT date(\''+tiempo+'\');',as_dict=True)
                for d0 in dateInicialP:
                    start=d0['date(\''+tiempo+'\')']
                tiempo=str(datetime.strptime(str(year.yearp) + '-06-01', "%Y-%m-%d"))
                dateInicialP = db.executesql('SELECT date(\''+tiempo+'\');',as_dict=True)
                for d0 in dateInicialP:
                    end=d0['date(\''+tiempo+'\')']
                if date1>=start and date1<end:
                    None
                else:
                    no_actionsAll=True
            else:
                tiempo=str(datetime.strptime(str(year.yearp) + '-06-01', "%Y-%m-%d"))
                dateInicialP = db.executesql('SELECT date(\''+tiempo+'\');',as_dict=True)
                for d0 in dateInicialP:
                    start=d0['date(\''+tiempo+'\')']
                tiempo=str(datetime.strptime(str(year.yearp) + '-12-31', "%Y-%m-%d"))
                dateInicialP = db.executesql('SELECT date(\''+tiempo+'\');',as_dict=True)
                for d0 in dateInicialP:
                    end=d0['date(\''+tiempo+'\')']
                if date1>=start and date1<=end:
                    None
                else:
                    no_actionsAll=True
        else:
            no_actionsAll=True

    #If is teacher, check if he has permitions
    if no_actionsAll==False and auth.has_membership('Teacher'):
        exception_query = db(db.course_laboratory_exception.project == project.id).select().first()
        if exception_query is not None:
            if exception_query.t_edit_lab == False:
                no_actionsAll=True
        else:
            no_actionsAll=True


    if no_actionsAll==True:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    else:
        roll_var=''
        if auth.has_membership('Super-Administrator'):
            roll_var='Super-Administrator'
        elif auth.has_membership('Ecys-Administrator'):
            roll_var='Ecys-Administrator'
        elif auth.has_membership('Teacher'):
            roll_var='Teacher'
        elif auth.has_membership('Student'):
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
                                    description = T('Delete from validation page'),
                                    validation_type=True
                                     )

def onupdate_validate_laboratory(form):
    failCheck=0
    messageFail=''
    #Check if has one of this roles
    if auth.has_membership('Super-Administrator')==False and auth.has_membership('Ecys-Administrator')==False and auth.has_membership('Teacher')==False and auth.has_membership('Student')==False:
        failCheck=2
        messageFail=T('Not valid Action.')

    import cpfecys
    #Check if the period is correct
    if request.vars['year'] is None or request.vars['year']=='':
        failCheck=2
        messageFail=T('Not valid Action.')
    else:
        year = request.vars['year']
        year = db(db.period_year.id==year).select().first()
        if year is None:
            failCheck=2
            messageFail=T('Not valid Action.')
        else:
            if auth.has_membership('Super-Administrator') == False and auth.has_membership('Ecys-Administrator')==False:
                if cpfecys.current_year_period().id != year.id:
                    failCheck=2
                    messageFail=T('Not valid Action.')

    #Check if the project is correct
    if request.vars['project'] is None or request.vars['project']=='':
        failCheck=2
        messageFail=T('Not valid Action.')
    else:
        project = request.vars['project']
        project = db(db.project.id==project).select().first()
        if project is None:
            failCheck=2
            messageFail=T('Not valid Action.')
        else:
            if auth.has_membership('Super-Administrator') == False and auth.has_membership('Ecys-Administrator')==False:
                assigantion = db((db.user_project.assigned_user==auth.user.id)&\
                        (db.user_project.project == project)&\
                        ((db.user_project.period <= year.id) & \
                        ((db.user_project.period + db.user_project.periods) > year.id))).select(db.user_project.ALL).first()
                if assigantion is None:
                    failCheck=2
                    messageFail=T('Not valid Action.')

    no_actionsAll=False
    if failCheck==0:
        if cpfecys.current_year_period().id != year.id:
            no_actionsAll==True
        else:
            #Check if the course has endend
            course_ended_var = db((db.course_ended.project==project.id) & (db.course_ended.period==year.id) ).select().first()
            if course_ended_var != None:
                if course_ended_var.finish == True:
                    no_actionsAll=True

            #Check the time of the semester is not over
            if no_actionsAll==False:
                #Time limit of semester parameter
                from datetime import datetime
                date1=None
                tiempo=str(datetime.now())
                dateInicialP = db.executesql('SELECT date(\''+tiempo+'\');',as_dict=True)
                for d0 in dateInicialP:
                    date1=d0['date(\''+tiempo+'\')']
                date_var = db((db.student_control_period.period_name==(T(year.period.name)+" "+str(year.yearp)))).select().first()
                if date1 >= date_var.date_start_semester and date1 <= date_var.date_finish_semester:
                    if year.period == 1:
                        tiempo=str(datetime.strptime(str(year.yearp) + '-01-01', "%Y-%m-%d"))
                        dateInicialP = db.executesql('SELECT date(\''+tiempo+'\');',as_dict=True)
                        for d0 in dateInicialP:
                            start=d0['date(\''+tiempo+'\')']
                        tiempo=str(datetime.strptime(str(year.yearp) + '-06-01', "%Y-%m-%d"))
                        dateInicialP = db.executesql('SELECT date(\''+tiempo+'\');',as_dict=True)
                        for d0 in dateInicialP:
                            end=d0['date(\''+tiempo+'\')']
                        if date1>=start and date1<end:
                            None
                        else:
                            no_actionsAll=True
                    else:
                        tiempo=str(datetime.strptime(str(year.yearp) + '-06-01', "%Y-%m-%d"))
                        dateInicialP = db.executesql('SELECT date(\''+tiempo+'\');',as_dict=True)
                        for d0 in dateInicialP:
                            start=d0['date(\''+tiempo+'\')']
                        tiempo=str(datetime.strptime(str(year.yearp) + '-12-31', "%Y-%m-%d"))
                        dateInicialP = db.executesql('SELECT date(\''+tiempo+'\');',as_dict=True)
                        for d0 in dateInicialP:
                            end=d0['date(\''+tiempo+'\')']
                        if date1>=start and date1<=end:
                            None
                        else:
                            no_actionsAll=True
                else:
                    no_actionsAll=True

            #If is teacher, check if he has permitions
            if no_actionsAll==False and auth.has_membership('Teacher'):
                exception_query = db(db.course_laboratory_exception.project == project.id).select().first()
                if exception_query is not None:
                    if exception_query.t_edit_lab == False:
                        no_actionsAll=True
                else:
                    no_actionsAll=True


    if no_actionsAll==False and failCheck==0:
        roll_var=''
        if auth.has_membership('Super-Administrator'):
            roll_var='Super-Administrator'
        elif auth.has_membership('Ecys-Administrator'):
            roll_var='Ecys-Administrator'
        elif auth.has_membership('Teacher'):
            roll_var='Teacher'
        elif auth.has_membership('Student'):
            roll_var='Student'

        usr2 = db((db.validate_laboratory_log.id_validate_laboratory == form.vars.id)&(db.validate_laboratory_log.validation_type==True)).select(orderby=db.validate_laboratory_log.id)
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
                                    description = T('Delete from validation page'),
                                    validation_type=True
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
                                        description = T('Update from validation page'),
                                        validation_type=True
                                         )
    else:
        if no_actionsAll==True:
            if auth.has_membership('Super-Administrator') == True or auth.has_membership('Ecys-Administrator')==True:
                if request.vars['description_request'] is None or request.vars['description_request']=='':
                    messageFail=T('You must enter a description of the modification.')
                    failCheck=1
                else:
                    roll_var='Ecys-Administrator'
                    if auth.has_membership('Super-Administrator'):
                        roll_var='Super-Administrator'

                    usr2 = db((db.validate_laboratory_log.id_validate_laboratory == form.vars.id)&(db.validate_laboratory_log.validation_type==True)).select(orderby=db.validate_laboratory_log.id)
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
                                                description = str(request.vars['description_request']),
                                                validation_type=True
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
                                                    description = str(request.vars['description_request']),
                                                    validation_type=True
                                                     )
            else:
                failCheck=2
                messageFail=T('Not valid Action.')

    #Check if has to show the message
    if failCheck >0:
        usr2 = db((db.validate_laboratory_log.id_validate_laboratory == form.vars.id)&(db.validate_laboratory_log.validation_type==True)).select(orderby=db.validate_laboratory_log.id)
        academic_log=''
        academic_id_log=''
        before_grade_log=''
        id_log = 0
        id_validate_laboratory = 0
        for u in usr2:
            academic_log=u.academic
            academic_id_log=u.academic_id
            before_grade_log=u.after_grade
            id_log = int(u.id)
            id_validate_laboratory = int(u.id_validate_laboratory)

        if form.vars.delete_this_record != None:
            insertDelete = db.validate_laboratory.insert(carnet=int(academic_id_log),semester=year.id, project=project.id,grade=int(before_grade_log))
            db(db.validate_laboratory_log.id==id_log).update(id_validate_laboratory=insertDelete.id)
        else:
            if before_grade_log != form.vars.grade:
                db(db.validate_laboratory.id==id_validate_laboratory).update(grade=int(before_grade_log))

        session.flash = messageFail
        if failCheck==2:
            redirect(URL('default','index'))



#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
#-----------------Laboratory replacing-------------------------------------------------------------------------------------------------------
@auth.requires_login()
@auth.requires(auth.has_membership('Student') or auth.has_membership('Teacher') or auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
def laboratory_replacing():
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
            if auth.has_membership('Super-Administrator') == False and auth.has_membership('Ecys-Administrator')==False:
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
        else:
            if auth.has_membership('Super-Administrator') == False and auth.has_membership('Ecys-Administrator')==False:
                assigantion = db((db.user_project.assigned_user==auth.user.id)&\
                        (db.user_project.project == project)&\
                        ((db.user_project.period <= year.id) & \
                        ((db.user_project.period + db.user_project.periods) > year.id))).select(db.user_project.ALL).first()
                if assigantion is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))

    #Grid
    query = ((db.validate_laboratory.semester==year.id)&(db.validate_laboratory.project==project.id)&(db.validate_laboratory.validation_type==False))
    grid=None
    db.validate_laboratory.id.readable = False
    db.validate_laboratory.id.writable = False
    db.validate_laboratory.project.readable = False
    db.validate_laboratory.project.writable = False
    db.validate_laboratory.project.default = project.id
    db.validate_laboratory.semester.readable = False
    db.validate_laboratory.semester.writable = False
    db.validate_laboratory.semester.default = year.id
    db.validate_laboratory.validation_type.readable = False
    db.validate_laboratory.validation_type.writable = False
    db.validate_laboratory.validation_type.default = False
    if cpfecys.current_year_period().id != year.id:
        no_actionsAll=True
        if auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'):
            links = [lambda row: A(T('Reason'), 
                    _role='button', 
                    _class='btn btn-info', 
                    _onclick='set_values("'+str(db(db.academic.id==int(row.carnet)).select(db.academic.carnet).first().carnet)+'","'+str(db((db.validate_laboratory_log.period==T(year.period.name))&(db.validate_laboratory_log.yearp==year.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic==str(db(db.academic.id==int(row.carnet)).select(db.academic.carnet).first().carnet))).select(db.validate_laboratory_log.description).last().description)+'")', 
                    _title=T('Reason for Equivalence Laboratory'),**{"_data-toggle":"modal", "_data-target": "#modaltheme"})]
            if 'edit' in request.args:
                db.validate_laboratory.carnet.writable = False
                grid = SQLFORM.grid(query, csv=False, paginate=10, oncreate=oncreate_laboratory_replacing, onupdate=onupdate_laboratory_replacing, searchable=False, links=links)
            else:
                grid = SQLFORM.grid(query, csv=False, paginate=10, deletable=False, oncreate=oncreate_laboratory_replacing, onupdate=onupdate_laboratory_replacing, searchable=False, links=links)
        else:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))
    else:
        no_actionsAll=False
        
        #Check if the course has endend
        course_ended_var = db((db.course_ended.project==project.id) & (db.course_ended.period==year.id) ).select().first()
        if course_ended_var != None:
            if course_ended_var.finish == True:
                no_actionsAll=True


        #Check the time of the semester is not over
        if no_actionsAll==False:
            #Time limit of semester parameter
            from datetime import datetime
            date1=None
            tiempo=str(datetime.now())
            dateInicialP = db.executesql('SELECT date(\''+tiempo+'\');',as_dict=True)
            for d0 in dateInicialP:
                date1=d0['date(\''+tiempo+'\')']
            date_var = db((db.student_control_period.period_name==(T(year.period.name)+" "+str(year.yearp)))).select().first()
            if date1 >= date_var.date_start_semester and date1 <= date_var.date_finish_semester:
                if year.period == 1:
                    tiempo=str(datetime.strptime(str(year.yearp) + '-01-01', "%Y-%m-%d"))
                    dateInicialP = db.executesql('SELECT date(\''+tiempo+'\');',as_dict=True)
                    for d0 in dateInicialP:
                        start=d0['date(\''+tiempo+'\')']
                    tiempo=str(datetime.strptime(str(year.yearp) + '-06-01', "%Y-%m-%d"))
                    dateInicialP = db.executesql('SELECT date(\''+tiempo+'\');',as_dict=True)
                    for d0 in dateInicialP:
                        end=d0['date(\''+tiempo+'\')']
                    if date1>=start and date1<end:
                        None
                    else:
                        no_actionsAll=True
                else:
                    tiempo=str(datetime.strptime(str(year.yearp) + '-06-01', "%Y-%m-%d"))
                    dateInicialP = db.executesql('SELECT date(\''+tiempo+'\');',as_dict=True)
                    for d0 in dateInicialP:
                        start=d0['date(\''+tiempo+'\')']
                    tiempo=str(datetime.strptime(str(year.yearp) + '-12-31', "%Y-%m-%d"))
                    dateInicialP = db.executesql('SELECT date(\''+tiempo+'\');',as_dict=True)
                    for d0 in dateInicialP:
                        end=d0['date(\''+tiempo+'\')']
                    if date1>=start and date1<=end:
                        None
                    else:
                        no_actionsAll=True
            else:
                no_actionsAll=True


        #If is teacher, check if he has permitions
        if no_actionsAll==False and auth.has_membership('Teacher'):
            exception_query = db(db.course_laboratory_exception.project == project.id).select().first()
            if exception_query is not None:
                if exception_query.t_edit_lab == False:
                    no_actionsAll=True
            else:
                no_actionsAll=True


        #Show options
        if no_actionsAll==False:
            links = [lambda row: A(T('Reason'), 
                    _role='button', 
                    _class='btn btn-info', 
                    _onclick='set_values("'+str(db(db.academic.id==int(row.carnet)).select(db.academic.carnet).first().carnet)+'","'+str(db((db.validate_laboratory_log.period==T(year.period.name))&(db.validate_laboratory_log.yearp==year.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic==str(db(db.academic.id==int(row.carnet)).select(db.academic.carnet).first().carnet))).select(db.validate_laboratory_log.description).last().description)+'")', 
                    _title=T('Reason for Equivalence Laboratory'),**{"_data-toggle":"modal", "_data-target": "#modaltheme"})]
            if 'edit' in request.args:
                db.validate_laboratory.carnet.writable = False
                grid = SQLFORM.grid(query, csv=False, paginate=10, oncreate=oncreate_laboratory_replacing, onupdate=onupdate_laboratory_replacing, searchable=False, links=links)
            else:
                grid = SQLFORM.grid(query, csv=False, paginate=10, deletable=False, oncreate=oncreate_laboratory_replacing, onupdate=onupdate_laboratory_replacing, searchable=False, links=links)
        else:
            links = [lambda row: A(T('Reason'), 
                    _role='button', 
                    _class='btn btn-info', 
                    _onclick='set_values("'+str(db(db.academic.id==int(row.carnet)).select(db.academic.carnet).first().carnet)+'","'+str(db((db.validate_laboratory_log.period==T(year.period.name))&(db.validate_laboratory_log.yearp==year.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic==str(db(db.academic.id==int(row.carnet)).select(db.academic.carnet).first().carnet))).select(db.validate_laboratory_log.description).last().description)+'")', 
                    _title=T('Reason for Equivalence Laboratory'),**{"_data-toggle":"modal", "_data-target": "#modaltheme"})]
            if auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'):
                if 'edit' in request.args:
                    db.validate_laboratory.carnet.writable = False
                    grid = SQLFORM.grid(query, csv=False, paginate=10, oncreate=oncreate_laboratory_replacing, onupdate=onupdate_laboratory_replacing, searchable=False, links=links)
                else:
                    grid = SQLFORM.grid(query, csv=False, paginate=10, deletable=False, oncreate=oncreate_laboratory_replacing, onupdate=onupdate_laboratory_replacing, searchable=False, links=links)
            else:
                grid = SQLFORM.grid(query, csv=False, create=False, editable=False, deletable=False, paginate=10, searchable=False, links=links)


    academic_assig3 = db((db.academic.id==db.academic_course_assignation.carnet)&(db.academic_course_assignation.semester == request.vars['year']) & (db.academic_course_assignation.assignation==request.vars['project'])).select(orderby=db.academic.carnet)
    students=[]
    for acaT in academic_assig3:
        students.append(acaT.academic_course_assignation)
    return dict(year = year, project = project, grid=grid, students=students)

def oncreate_laboratory_replacing(form):
    #Check if has one of this roles
    if auth.has_membership('Super-Administrator')==False and auth.has_membership('Ecys-Administrator')==False and auth.has_membership('Teacher')==False and auth.has_membership('Student')==False:
        db(db.validate_laboratory.id==form.vars.id).delete()
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))

    #Start the process
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
            if auth.has_membership('Super-Administrator') == False and auth.has_membership('Ecys-Administrator')==False:
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
        else:
            if auth.has_membership('Super-Administrator') == False and auth.has_membership('Ecys-Administrator')==False:
                assigantion = db((db.user_project.assigned_user==auth.user.id)&\
                        (db.user_project.project == project)&\
                        ((db.user_project.period <= year.id) & \
                        ((db.user_project.period + db.user_project.periods) > year.id))).select(db.user_project.ALL).first()
                if assigantion is None:
                    db(db.validate_laboratory.id==form.vars.id).delete()
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))


    no_actionsAll=False
    if cpfecys.current_year_period().id != year.id:
        no_actionsAll==True
    else:
        #Check if the course has endend
        course_ended_var = db((db.course_ended.project==project.id) & (db.course_ended.period==year.id) ).select().first()
        if course_ended_var != None:
            if course_ended_var.finish == True:
                no_actionsAll=True

        #Check the time of the semester is not over
        if no_actionsAll==False:
            #Time limit of semester parameter
            from datetime import datetime
            date1=None
            tiempo=str(datetime.now())
            dateInicialP = db.executesql('SELECT date(\''+tiempo+'\');',as_dict=True)
            for d0 in dateInicialP:
                date1=d0['date(\''+tiempo+'\')']
            date_var = db((db.student_control_period.period_name==(T(year.period.name)+" "+str(year.yearp)))).select().first()
            if date1 >= date_var.date_start_semester and date1 <= date_var.date_finish_semester:
                if year.period == 1:
                    tiempo=str(datetime.strptime(str(year.yearp) + '-01-01', "%Y-%m-%d"))
                    dateInicialP = db.executesql('SELECT date(\''+tiempo+'\');',as_dict=True)
                    for d0 in dateInicialP:
                        start=d0['date(\''+tiempo+'\')']
                    tiempo=str(datetime.strptime(str(year.yearp) + '-06-01', "%Y-%m-%d"))
                    dateInicialP = db.executesql('SELECT date(\''+tiempo+'\');',as_dict=True)
                    for d0 in dateInicialP:
                        end=d0['date(\''+tiempo+'\')']
                    if date1>=start and date1<end:
                        None
                    else:
                        no_actionsAll=True
                else:
                    tiempo=str(datetime.strptime(str(year.yearp) + '-06-01', "%Y-%m-%d"))
                    dateInicialP = db.executesql('SELECT date(\''+tiempo+'\');',as_dict=True)
                    for d0 in dateInicialP:
                        start=d0['date(\''+tiempo+'\')']
                    tiempo=str(datetime.strptime(str(year.yearp) + '-12-31', "%Y-%m-%d"))
                    dateInicialP = db.executesql('SELECT date(\''+tiempo+'\');',as_dict=True)
                    for d0 in dateInicialP:
                        end=d0['date(\''+tiempo+'\')']
                    if date1>=start and date1<=end:
                        None
                    else:
                        no_actionsAll=True
            else:
                no_actionsAll=True

        #If is teacher, check if he has permitions
        if no_actionsAll==False and auth.has_membership('Teacher'):
            exception_query = db(db.course_laboratory_exception.project == project.id).select().first()
            if exception_query is not None:
                if exception_query.t_edit_lab == False:
                    no_actionsAll=True
            else:
                no_actionsAll=True



    if no_actionsAll==False:
        if request.vars['description_request'] is None or request.vars['description_request']=='':
            db(db.validate_laboratory.id==form.vars.id).delete()
            session.flash=T('You must enter a description of the modification.')
        else:
            roll_var=''
            if auth.has_membership('Super-Administrator'):
                roll_var='Super-Administrator'
            elif auth.has_membership('Ecys-Administrator'):
                roll_var='Ecys-Administrator'
            elif auth.has_membership('Teacher'):
                roll_var='Teacher'
            elif auth.has_membership('Student'):
                roll_var='Student'
            else:
                db(db.validate_laboratory.id==form.vars.id).delete()
                session.flash = T('Not valid Action.')
                redirect(URL('default','index'))

            usr2 = db((db.validate_laboratory.id != form.vars.id) & (db.validate_laboratory.semester == request.vars['year']) & (db.validate_laboratory.project == request.vars['project']) & (db.validate_laboratory.carnet == form.vars.carnet)).select().first()
            if usr2 is not None:
                db(db.validate_laboratory.id==form.vars.id).delete()
                session.flash = T('Error. There is a registration renewal or equivalence laboratory student in the course.')
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
                                        description = str(request.vars['description_request']),
                                        validation_type=False
                                         )
    else:
        if auth.has_membership('Super-Administrator') == True or auth.has_membership('Ecys-Administrator')==True:
            if request.vars['description_request'] is None or request.vars['description_request']=='':
                db(db.validate_laboratory.id==form.vars.id).delete()
                session.flash=T('You must enter a description of the modification.')
            else:
                roll_var='Ecys-Administrator'
                if auth.has_membership('Super-Administrator'):
                    roll_var='Super-Administrator'

                usr2 = db((db.validate_laboratory.id != form.vars.id) & (db.validate_laboratory.semester == request.vars['year']) & (db.validate_laboratory.project == request.vars['project']) & (db.validate_laboratory.carnet == form.vars.carnet)).select().first()
                if usr2 is not None:
                    db(db.validate_laboratory.id==form.vars.id).delete()
                    session.flash = T('Error. There is a registration renewal or equivalence laboratory student in the course.')
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
                                            description = str(request.vars['description_request']),
                                            validation_type=False
                                             )
        else:
            db(db.validate_laboratory.id==form.vars.id).delete()
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

def onupdate_laboratory_replacing(form):
    failCheck=0
    messageFail=''
    #Check if has one of this roles
    if auth.has_membership('Super-Administrator')==False and auth.has_membership('Ecys-Administrator')==False and auth.has_membership('Teacher')==False and auth.has_membership('Student')==False:
        failCheck=2
        messageFail=T('Not valid Action.')

    import cpfecys
    #Check if the period is correct
    if request.vars['year'] is None or request.vars['year']=='':
        failCheck=2
        messageFail=T('Not valid Action.')
    else:
        year = request.vars['year']
        year = db(db.period_year.id==year).select().first()
        if year is None:
            failCheck=2
            messageFail=T('Not valid Action.')
        else:
            if auth.has_membership('Super-Administrator') == False and auth.has_membership('Ecys-Administrator')==False:
                if cpfecys.current_year_period().id != year.id:
                    failCheck=2
                    messageFail=T('Not valid Action.')

    #Check if the project is correct
    if request.vars['project'] is None or request.vars['project']=='':
        failCheck=2
        messageFail=T('Not valid Action.')
    else:
        project = request.vars['project']
        project = db(db.project.id==project).select().first()
        if project is None:
            failCheck=2
            messageFail=T('Not valid Action.')
        else:
            if auth.has_membership('Super-Administrator') == False and auth.has_membership('Ecys-Administrator')==False:
                assigantion = db((db.user_project.assigned_user==auth.user.id)&\
                        (db.user_project.project == project)&\
                        ((db.user_project.period <= year.id) & \
                        ((db.user_project.period + db.user_project.periods) > year.id))).select(db.user_project.ALL).first()
                if assigantion is None:
                    failCheck=2
                    messageFail=T('Not valid Action.')

    no_actionsAll=False
    if failCheck==0:
        if cpfecys.current_year_period().id != year.id:
            no_actionsAll==True
        else:
            #Check if the course has endend
            course_ended_var = db((db.course_ended.project==project.id) & (db.course_ended.period==year.id) ).select().first()
            if course_ended_var != None:
                if course_ended_var.finish == True:
                    no_actionsAll=True

            #Check the time of the semester is not over
            if no_actionsAll==False:
                #Time limit of semester parameter
                from datetime import datetime
                date1=None
                tiempo=str(datetime.now())
                dateInicialP = db.executesql('SELECT date(\''+tiempo+'\');',as_dict=True)
                for d0 in dateInicialP:
                    date1=d0['date(\''+tiempo+'\')']
                date_var = db((db.student_control_period.period_name==(T(year.period.name)+" "+str(year.yearp)))).select().first()
                if date1 >= date_var.date_start_semester and date1 <= date_var.date_finish_semester:
                    if year.period == 1:
                        tiempo=str(datetime.strptime(str(year.yearp) + '-01-01', "%Y-%m-%d"))
                        dateInicialP = db.executesql('SELECT date(\''+tiempo+'\');',as_dict=True)
                        for d0 in dateInicialP:
                            start=d0['date(\''+tiempo+'\')']
                        tiempo=str(datetime.strptime(str(year.yearp) + '-06-01', "%Y-%m-%d"))
                        dateInicialP = db.executesql('SELECT date(\''+tiempo+'\');',as_dict=True)
                        for d0 in dateInicialP:
                            end=d0['date(\''+tiempo+'\')']
                        if date1>=start and date1<end:
                            None
                        else:
                            no_actionsAll=True
                    else:
                        tiempo=str(datetime.strptime(str(year.yearp) + '-06-01', "%Y-%m-%d"))
                        dateInicialP = db.executesql('SELECT date(\''+tiempo+'\');',as_dict=True)
                        for d0 in dateInicialP:
                            start=d0['date(\''+tiempo+'\')']
                        tiempo=str(datetime.strptime(str(year.yearp) + '-12-31', "%Y-%m-%d"))
                        dateInicialP = db.executesql('SELECT date(\''+tiempo+'\');',as_dict=True)
                        for d0 in dateInicialP:
                            end=d0['date(\''+tiempo+'\')']
                        if date1>=start and date1<=end:
                            None
                        else:
                            no_actionsAll=True
                else:
                    no_actionsAll=True

            #If is teacher, check if he has permitions
            if no_actionsAll==False and auth.has_membership('Teacher'):
                exception_query = db(db.course_laboratory_exception.project == project.id).select().first()
                if exception_query is not None:
                    if exception_query.t_edit_lab == False:
                        no_actionsAll=True
                else:
                    no_actionsAll=True


    if no_actionsAll==False and failCheck==0:
        if request.vars['description_request'] is None or request.vars['description_request']=='':
            messageFail=T('You must enter a description of the modification.')
            failCheck=1
        else:
            roll_var='Super-Administrator'
            if auth.has_membership('Ecys-Administrator'):
                roll_var='Ecys-Administrator'
            elif auth.has_membership('Teacher'):
                roll_var='Teacher'
            elif auth.has_membership('Student'):
                roll_var='Student'

            usr2 = db((db.validate_laboratory_log.id_validate_laboratory == form.vars.id)&(db.validate_laboratory_log.validation_type==False)).select(orderby=db.validate_laboratory_log.id)
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
                                        description = str(request.vars['description_request']),
                                        validation_type=False
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
                                            description = str(request.vars['description_request']),
                                            validation_type=False
                                             )
    else:
        if no_actionsAll==True:
            if auth.has_membership('Super-Administrator') == True or auth.has_membership('Ecys-Administrator')==True:
                if request.vars['description_request'] is None or request.vars['description_request']=='':
                    messageFail=T('You must enter a description of the modification.')
                    failCheck=1
                else:
                    roll_var='Ecys-Administrator'
                    if auth.has_membership('Super-Administrator'):
                        roll_var='Super-Administrator'

                    usr2 = db((db.validate_laboratory_log.id_validate_laboratory == form.vars.id)&(db.validate_laboratory_log.validation_type==False)).select(orderby=db.validate_laboratory_log.id)
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
                                                description = str(request.vars['description_request']),
                                                validation_type=False
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
                                                    description = str(request.vars['description_request']),
                                                    validation_type=False
                                                     )
            else:
                failCheck=2
                messageFail=T('Not valid Action.')

    #Check if has to show the message
    if failCheck >0:
        usr2 = db((db.validate_laboratory_log.id_validate_laboratory == form.vars.id)&(db.validate_laboratory_log.validation_type==False)).select(orderby=db.validate_laboratory_log.id)
        academic_log=''
        academic_id_log=''
        before_grade_log=''
        id_log = 0
        id_validate_laboratory = 0
        for u in usr2:
            academic_log=u.academic
            academic_id_log=u.academic_id
            before_grade_log=u.after_grade
            id_log = int(u.id)
            id_validate_laboratory = int(u.id_validate_laboratory)

        if form.vars.delete_this_record != None:
            insertDelete = db.validate_laboratory.insert(carnet=int(academic_id_log),semester=year.id, project=project.id,grade=int(before_grade_log))
            db(db.validate_laboratory_log.id==id_log).update(id_validate_laboratory=insertDelete.id)
        else:
            if before_grade_log != form.vars.grade:
                db(db.validate_laboratory.id==id_validate_laboratory).update(grade=int(before_grade_log))

        session.flash = messageFail
        if failCheck==2:
            redirect(URL('default','index'))

#------------------------------------course_first_recovery_test--------------
@auth.requires_login()
@auth.requires(auth.has_membership('Student') or auth.has_membership('Teacher') or auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
def course_first_recovery_test():
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
        if course_ended_var.finish == False:
            session.flash = T('Course hasn’t finalized.')
            redirect(URL('default','index'))
    else:
        session.flash = T('Course hasn’t finalized.')
        redirect(URL('default','index'))
    

    #Grid
    grid=None
    db.course_first_recovery_test.id.readable = False
    db.course_first_recovery_test.id.writable = False
    db.course_first_recovery_test.project.readable = False
    db.course_first_recovery_test.project.writable = False
    db.course_first_recovery_test.project.default = project.id
    db.course_first_recovery_test.semester.readable = False
    db.course_first_recovery_test.semester.writable = False
    db.course_first_recovery_test.semester.default = year.id
    if auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'):
        query = ((db.course_first_recovery_test.semester==year.id)&(db.course_first_recovery_test.project==project.id))
        if cpfecys.current_year_period().id == year.id and no_actionsAll==False:
            if 'edit' in request.args:
                db.course_first_recovery_test.carnet.writable = False
                grid = SQLFORM.grid(query, csv=False, paginate=50, oncreate=oncreate_course_first_recovery_test, onupdate=onupdate_course_first_recovery_test, ondelete=ondelete_course_first_recovery_test, searchable=False)
            else:
                grid = SQLFORM.grid(query, csv=False, paginate=50, oncreate=oncreate_course_first_recovery_test, onupdate=onupdate_course_first_recovery_test, ondelete=ondelete_course_first_recovery_test, searchable=False)
        else:
            if 'edit' in request.args:
                db.course_first_recovery_test.carnet.writable = False
                grid = SQLFORM.grid(query, csv=False, paginate=50, oncreate=oncreate_course_first_recovery_test, onupdate=onupdate_course_first_recovery_test, ondelete=ondelete_course_first_recovery_test, searchable=False)
            else:
                grid = SQLFORM.grid(query, csv=False, paginate=50, oncreate=oncreate_course_first_recovery_test, onupdate=onupdate_course_first_recovery_test, ondelete=ondelete_course_first_recovery_test, searchable=False)
    elif auth.has_membership('Student'):
        assigantion = db((db.user_project.assigned_user==auth.user.id)&\
                        (db.user_project.project == project)&\
                        ((db.user_project.period <= year.id) & \
                        ((db.user_project.period + db.user_project.periods) > year.id))).select(db.user_project.ALL).first()
        if assigantion is None:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))
        else:
            if exception_s_var==True and no_actionsAll==False:
                query = ((db.course_first_recovery_test.semester==year.id)&(db.course_first_recovery_test.project==project.id))
                if 'edit' in request.args:
                    db.course_first_recovery_test.carnet.writable = False
                    grid = SQLFORM.grid(query, csv=False, paginate=50, oncreate=oncreate_course_first_recovery_test, onupdate=onupdate_course_first_recovery_test, ondelete=ondelete_course_first_recovery_test, searchable=False)
                else:
                    grid = SQLFORM.grid(query, csv=False, paginate=50, oncreate=oncreate_course_first_recovery_test, onupdate=onupdate_course_first_recovery_test, ondelete=ondelete_course_first_recovery_test, searchable=False)
            else:
                query = ((db.course_first_recovery_test.semester==year.id)&(db.course_first_recovery_test.project==project.id))
                grid = SQLFORM.grid(query, csv=False, create=False, editable=False, deletable=False, paginate=50, searchable=False)
    elif auth.has_membership('Teacher'):
        assigantion = db((db.user_project.assigned_user==auth.user.id)&\
                        (db.user_project.project == project)&\
                        ((db.user_project.period <= year.id) & \
                        ((db.user_project.period + db.user_project.periods) > year.id))).select(db.user_project.ALL).first()
        if assigantion is None:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))
        else:
            if no_actionsAll==False:
                query = ((db.course_first_recovery_test.semester==year.id)&(db.course_first_recovery_test.project==project.id))
                if 'edit' in request.args:
                    db.course_first_recovery_test.carnet.writable = False
                    grid = SQLFORM.grid(query, csv=False, paginate=50, oncreate=oncreate_course_first_recovery_test, onupdate=onupdate_course_first_recovery_test, ondelete=ondelete_course_first_recovery_test, searchable=False)
                else:
                    grid = SQLFORM.grid(query, csv=False, paginate=50, oncreate=oncreate_course_first_recovery_test, onupdate=onupdate_course_first_recovery_test, ondelete=ondelete_course_first_recovery_test, searchable=False)
            else:
                query = ((db.course_first_recovery_test.semester==year.id)&(db.course_first_recovery_test.project==project.id))
                grid = SQLFORM.grid(query, csv=False, create=False, editable=False, deletable=False, paginate=50, searchable=False)
    else:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))

    academic_assig3 = db((db.academic.id==db.academic_course_assignation.carnet)&(db.academic_course_assignation.semester == request.vars['year']) & (db.academic_course_assignation.assignation==request.vars['project'])).select(orderby=db.academic.carnet)
    students=[]
    for acaT in academic_assig3:
        students.append(acaT.academic_course_assignation)
    
    return dict(year = year, project = project, grid=grid,students=students)




def oncreate_course_first_recovery_test(form):
    import cpfecys

    #Check if the period is correct
    if request.vars['year'] is None or request.vars['year']=='':
        db(db.course_first_recovery_test.id==form.vars.id).delete()
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    else:
        year = request.vars['year']
        year = db(db.period_year.id==year).select().first()
        if year is None:
            db(db.course_first_recovery_test.id==form.vars.id).delete()
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))
        

    #Check if the project is correct
    if request.vars['project'] is None or request.vars['project']=='':
        db(db.course_first_recovery_test.id==form.vars.id).delete()
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    else:
        project = request.vars['project']
        project = db(db.project.id==project).select().first()
        if project is None:
            db(db.course_first_recovery_test.id==form.vars.id).delete()
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))


    #Check if the course has endend
    no_actionsAll=False
    

    if no_actionsAll==False:
        roll_var=''
        if auth.has_membership('Super-Administrator'):
            roll_var='Super-Administrator'
        elif auth.has_membership('Ecys-Administrator'):
            roll_var='Ecys-Administrator'
        elif auth.has_membership('Teacher'):
            roll_var='Teacher'
        elif auth.has_membership('Student'):
            roll_var='Student'

       
        usr2 = db((db.course_first_recovery_test.id != form.vars.id) & (db.course_first_recovery_test.semester == request.vars['year']) & (db.course_first_recovery_test.project == request.vars['project']) & (db.course_first_recovery_test.carnet == form.vars.carnet)).select().first()
        if usr2 is not None:
            db(db.course_first_recovery_test.id==form.vars.id).delete()
            session.flash = T('Error. Exist a register of recovery test of the student in the course.')
        else:
            academic_s = db(db.academic.id==form.vars.carnet).select().first()
            var_assignation = db( (db.academic_course_assignation.carnet==academic_s.id)&(db.academic_course_assignation.semester==year.id)&(db.academic_course_assignation.assignation==project.id) ).select().first()
            if var_assignation is None:
                db(db.course_first_recovery_test.id==form.vars.id).delete()
                session.flash = T('Error. The academic is not assigned to the course')
            else:
                db.course_first_recovery_test_log.insert(user_name = auth.user.username,
                                    roll = roll_var,
                                    operation_log = 'insert',
                                    academic_id = academic_s.id,
                                    academic = academic_s.carnet,
                                    project = project.name,
                                    period = T(year.period.name),
                                    yearp = year.yearp,
                                    after_grade = form.vars.grade,
                                    id_course_first_recovery_test = form.vars.id,
                                    description = T('Inserted from first recovery test page')
                                     )
    

def ondelete_course_first_recovery_test(table_involved, id_of_the_deleted_record):
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
        roll_var='Teacher'
    elif auth.has_membership('Student'):
        roll_var='Student'


    course_first_recovery_test_var = db.course_first_recovery_test(id_of_the_deleted_record)
    if course_first_recovery_test_var is not None:        
        academic_s = db(db.academic.id==course_first_recovery_test_var.carnet).select().first()
        db.course_first_recovery_test_log.insert(user_name = auth.user.username,
                                roll = roll_var,
                                operation_log = 'delete',
                                academic_id = academic_s.id,
                                academic = academic_s.carnet,
                                project = project.name,
                                period = T(year.period.name),
                                yearp = year.yearp,
                                before_grade = course_first_recovery_test_var.grade,
                                description = T('Delete from first recovery test page')
                                 )

def onupdate_course_first_recovery_test(form):
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


    #Check if the course has endend
    no_actionsAll=False
    


    if no_actionsAll==False:
        roll_var=''
        if auth.has_membership('Super-Administrator'):
            roll_var='Super-Administrator'
        elif auth.has_membership('Ecys-Administrator'):
            roll_var='Ecys-Administrator'
        elif auth.has_membership('Teacher'):
            roll_var='Teacher'
        elif auth.has_membership('Student'):
            roll_var='Student'

        usr2 = db(db.course_first_recovery_test_log.id_course_first_recovery_test == form.vars.id).select(orderby=db.course_first_recovery_test_log.id)
        academic_log=''
        academic_id_log=''
        before_grade_log=''
        for u in usr2:
            academic_log=u.academic
            academic_id_log=u.academic_id
            before_grade_log=u.after_grade

        if form.vars.delete_this_record != None:
            db.course_first_recovery_test_log.insert(user_name = auth.user.username,
                                    roll = roll_var,
                                    operation_log = 'delete',
                                    academic_id = academic_id_log,
                                    academic = academic_log,
                                    project = project.name,
                                    period = T(year.period.name),
                                    yearp = year.yearp,
                                    before_grade = before_grade_log,
                                    description = T('Delete from first recovery test page')
                                     )
        else:
            if before_grade_log != form.vars.grade:
                db.course_first_recovery_test_log.insert(user_name = auth.user.username,
                                        roll = roll_var,
                                        operation_log = 'update',
                                        academic_id = academic_id_log,
                                        academic = academic_log,
                                        project = project.name,
                                        period = T(year.period.name),
                                        yearp = year.yearp,
                                        before_grade = before_grade_log,
                                        after_grade = form.vars.grade,
                                        id_course_first_recovery_test = form.vars.id,
                                        description = T('Update from first recovery test page')
                                         )
    

#------------------------------------course_second_recovery_test--------------

@auth.requires_login()
@auth.requires(auth.has_membership('Student') or auth.has_membership('Teacher') or auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
def course_second_recovery_test():
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
        if course_ended_var.finish == False:
            session.flash = T('Course hasn’t finalized.')
            redirect(URL('default','index'))
    else:
        session.flash = T('Course hasn’t finalized.')
        redirect(URL('default','index'))
    

    #Grid
    grid=None
    db.course_second_recovery_test.id.readable = False
    db.course_second_recovery_test.id.writable = False
    db.course_second_recovery_test.project.readable = False
    db.course_second_recovery_test.project.writable = False
    db.course_second_recovery_test.project.default = project.id
    db.course_second_recovery_test.semester.readable = False
    db.course_second_recovery_test.semester.writable = False
    db.course_second_recovery_test.semester.default = year.id
    if auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'):
        query = ((db.course_second_recovery_test.semester==year.id)&(db.course_second_recovery_test.project==project.id))
        if cpfecys.current_year_period().id == year.id and no_actionsAll==False:
            if 'edit' in request.args:
                db.course_second_recovery_test.carnet.writable = False
                grid = SQLFORM.grid(query, csv=False, paginate=50, oncreate=oncreate_course_second_recovery_test, onupdate=onupdate_course_second_recovery_test, ondelete=ondelete_course_second_recovery_test, searchable=False)
            else:
                grid = SQLFORM.grid(query, csv=False, paginate=50, oncreate=oncreate_course_second_recovery_test, onupdate=onupdate_course_second_recovery_test, ondelete=ondelete_course_second_recovery_test, searchable=False)
        else:
            if 'edit' in request.args:
                db.course_second_recovery_test.carnet.writable = False
                grid = SQLFORM.grid(query, csv=False, paginate=50, oncreate=oncreate_course_second_recovery_test, onupdate=onupdate_course_second_recovery_test, ondelete=ondelete_course_second_recovery_test, searchable=False)
            else:
                grid = SQLFORM.grid(query, csv=False, paginate=50, oncreate=oncreate_course_second_recovery_test, onupdate=onupdate_course_second_recovery_test, ondelete=ondelete_course_second_recovery_test, searchable=False)
    elif auth.has_membership('Student'):
        assigantion = db((db.user_project.assigned_user==auth.user.id)&\
                        (db.user_project.project == project)&\
                        ((db.user_project.period <= year.id) & \
                        ((db.user_project.period + db.user_project.periods) > year.id))).select(db.user_project.ALL).first()
        if assigantion is None:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))
        else:
            if exception_s_var==True and no_actionsAll==False:
                query = ((db.course_second_recovery_test.semester==year.id)&(db.course_second_recovery_test.project==project.id))
                if 'edit' in request.args:
                    db.course_second_recovery_test.carnet.writable = False
                    grid = SQLFORM.grid(query, csv=False, paginate=50, oncreate=oncreate_course_second_recovery_test, onupdate=onupdate_course_second_recovery_test, ondelete=ondelete_course_second_recovery_test, searchable=False)
                else:
                    grid = SQLFORM.grid(query, csv=False, paginate=50, oncreate=oncreate_course_second_recovery_test, onupdate=onupdate_course_second_recovery_test, ondelete=ondelete_course_second_recovery_test, searchable=False)
            else:
                query = ((db.course_second_recovery_test.semester==year.id)&(db.course_second_recovery_test.project==project.id))
                grid = SQLFORM.grid(query, csv=False, create=False, editable=False, deletable=False, paginate=50, searchable=False)
    elif auth.has_membership('Teacher'):
        assigantion = db((db.user_project.assigned_user==auth.user.id)&\
                        (db.user_project.project == project)&\
                        ((db.user_project.period <= year.id) & \
                        ((db.user_project.period + db.user_project.periods) > year.id))).select(db.user_project.ALL).first()
        if assigantion is None:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))
        else:
            if no_actionsAll==False:
                query = ((db.course_second_recovery_test.semester==year.id)&(db.course_second_recovery_test.project==project.id))
                if 'edit' in request.args:
                    db.course_second_recovery_test.carnet.writable = False
                    grid = SQLFORM.grid(query, csv=False, paginate=50, oncreate=oncreate_course_second_recovery_test, onupdate=onupdate_course_second_recovery_test, ondelete=ondelete_course_second_recovery_test, searchable=False)
                else:
                    grid = SQLFORM.grid(query, csv=False, paginate=50, oncreate=oncreate_course_second_recovery_test, onupdate=onupdate_course_second_recovery_test, ondelete=ondelete_course_second_recovery_test, searchable=False)
            else:
                query = ((db.course_second_recovery_test.semester==year.id)&(db.course_second_recovery_test.project==project.id))
                grid = SQLFORM.grid(query, csv=False, create=False, editable=False, deletable=False, paginate=50, searchable=False)
    else:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))

    academic_assig3 = db((db.academic.id==db.academic_course_assignation.carnet)&(db.academic_course_assignation.semester == request.vars['year']) & (db.academic_course_assignation.assignation==request.vars['project'])).select(orderby=db.academic.carnet)
    students=[]
    for acaT in academic_assig3:
        students.append(acaT.academic_course_assignation)

    return dict(year = year, project = project, grid=grid,students=students)




def oncreate_course_second_recovery_test(form):
    import cpfecys

    #Check if the period is correct
    if request.vars['year'] is None or request.vars['year']=='':
        db(db.course_second_recovery_test.id==form.vars.id).delete()
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    else:
        year = request.vars['year']
        year = db(db.period_year.id==year).select().first()
        if year is None:
            db(db.course_second_recovery_test.id==form.vars.id).delete()
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))
        

    #Check if the project is correct
    if request.vars['project'] is None or request.vars['project']=='':
        db(db.course_second_recovery_test.id==form.vars.id).delete()
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    else:
        project = request.vars['project']
        project = db(db.project.id==project).select().first()
        if project is None:
            db(db.course_second_recovery_test.id==form.vars.id).delete()
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))


    #Check if the course has endend
    no_actionsAll=False
    

    if no_actionsAll==False:
        roll_var=''
        if auth.has_membership('Super-Administrator'):
            roll_var='Super-Administrator'
        elif auth.has_membership('Ecys-Administrator'):
            roll_var='Ecys-Administrator'
        elif auth.has_membership('Teacher'):
            roll_var='Teacher'
        elif auth.has_membership('Student'):
            roll_var='Student'

       
        usr2 = db((db.course_second_recovery_test.id != form.vars.id) & (db.course_second_recovery_test.semester == request.vars['year']) & (db.course_second_recovery_test.project == request.vars['project']) & (db.course_second_recovery_test.carnet == form.vars.carnet)).select().first()
        if usr2 is not None:
            db(db.course_second_recovery_test.id==form.vars.id).delete()
            session.flash = T('Error. Exist a register of recovery test of the student in the course.')
        else:
            academic_s = db(db.academic.id==form.vars.carnet).select().first()
            var_assignation = db( (db.academic_course_assignation.carnet==academic_s.id)&(db.academic_course_assignation.semester==year.id)&(db.academic_course_assignation.assignation==project.id) ).select().first()
            if var_assignation is None:
                db(db.course_first_recovery_test.id==form.vars.id).delete()
                session.flash = T('Error. The academic is not assigned to the course')
            else:
                db.course_second_recovery_test_log.insert(user_name = auth.user.username,
                                    roll = roll_var,
                                    operation_log = 'insert',
                                    academic_id = academic_s.id,
                                    academic = academic_s.carnet,
                                    project = project.name,
                                    period = T(year.period.name),
                                    yearp = year.yearp,
                                    after_grade = form.vars.grade,
                                    id_course_second_recovery_test = form.vars.id,
                                    description = T('Inserted from second recovery test page')
                                     )
    

def ondelete_course_second_recovery_test(table_involved, id_of_the_deleted_record):
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
        roll_var='Teacher'
    elif auth.has_membership('Student'):
        roll_var='Student'


    course_second_recovery_test_var = db.course_second_recovery_test(id_of_the_deleted_record)
    if course_second_recovery_test_var is not None:        
        academic_s = db(db.academic.id==course_second_recovery_test_var.carnet).select().first()
        db.course_second_recovery_test_log.insert(user_name = auth.user.username,
                                roll = roll_var,
                                operation_log = 'delete',
                                academic_id = academic_s.id,
                                academic = academic_s.carnet,
                                project = project.name,
                                period = T(year.period.name),
                                yearp = year.yearp,
                                before_grade = course_second_recovery_test_var.grade,
                                description = T('Delete from second recovery test page')
                                 )

def onupdate_course_second_recovery_test(form):
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


    #Check if the course has endend
    no_actionsAll=False
    


    if no_actionsAll==False:
        roll_var=''
        if auth.has_membership('Super-Administrator'):
            roll_var='Super-Administrator'
        elif auth.has_membership('Ecys-Administrator'):
            roll_var='Ecys-Administrator'
        elif auth.has_membership('Teacher'):
            roll_var='Teacher'
        elif auth.has_membership('Student'):
            roll_var='Student'

        usr2 = db(db.course_second_recovery_test_log.id_course_second_recovery_test == form.vars.id).select(orderby=db.course_second_recovery_test_log.id)
        academic_log=''
        academic_id_log=''
        before_grade_log=''
        for u in usr2:
            academic_log=u.academic
            academic_id_log=u.academic_id
            before_grade_log=u.after_grade

        if form.vars.delete_this_record != None:
            db.course_second_recovery_test_log.insert(user_name = auth.user.username,
                                    roll = roll_var,
                                    operation_log = 'delete',
                                    academic_id = academic_id_log,
                                    academic = academic_log,
                                    project = project.name,
                                    period = T(year.period.name),
                                    yearp = year.yearp,
                                    before_grade = before_grade_log,
                                    description = T('Delete from second recovery test page')
                                     )
        else:
            if before_grade_log != form.vars.grade:
                db.course_second_recovery_test_log.insert(user_name = auth.user.username,
                                        roll = roll_var,
                                        operation_log = 'update',
                                        academic_id = academic_id_log,
                                        academic = academic_log,
                                        project = project.name,
                                        period = T(year.period.name),
                                        yearp = year.yearp,
                                        before_grade = before_grade_log,
                                        after_grade = form.vars.grade,
                                        id_course_second_recovery_test = form.vars.id,
                                        description = T('Update from second recovery test page')
                                         )
    


#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
@auth.requires_login()
@auth.requires(auth.has_membership('Student') or auth.has_membership('Teacher') or auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
def Course_Format_Technical_School():
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
        assigantion = db((db.user_project.assigned_user==auth.user.id)&\
                        (db.user_project.project == project_var.id)&\
                        ((db.user_project.period <= year.id) & \
                        ((db.user_project.period + db.user_project.periods) > year.id))).select(db.user_project.ALL).first()
        if assigantion is None:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))
        else:
            if auth.has_membership('Student')==True:
                exception_query = db(db.course_laboratory_exception.project == project.id).select().first()
                if exception_query is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))
                else:
                    if exception_query.s_edit_course==False:
                        session.flash = T('Not valid Action.')
                        redirect(URL('default','index'))

    #Check the correct parameters
    if (request.vars['op'] != '1' and request.vars['op'] != '2' and request.vars['op'] != '3'):
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))

    #Students    
    academic_assig3 = db((db.academic.id==db.academic_course_assignation.carnet)&(db.academic_course_assignation.semester == year.id) & (db.academic_course_assignation.assignation==project_var.id)).select(orderby=db.academic.carnet)
    students=[]
    for acaT in academic_assig3:
        students.append(acaT.academic_course_assignation)


    var_final_grade = 0.00
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
            var_final_grade = categoryC.grade
            if ( request.vars['op'] == '2' or  request.vars['op'] == '3'):
                None
            else:
                catCourseTemp=categoryC
        else:
            catVecCourseTemp.append(categoryC)
            CourseActivities.append(db((db.course_activity.semester==year.id)&(db.course_activity.assignation==project_var.id)&(db.course_activity.laboratory==False)&(db.course_activity.course_activity_category==categoryC.id)).select())
    if catCourseTemp != None:
        catVecCourseTemp.append(catCourseTemp)
        CourseActivities.append(db((db.course_activity.semester==year.id)&(db.course_activity.assignation==project_var.id)&(db.course_activity.laboratory==False)&(db.course_activity.course_activity_category==catCourseTemp.id)).select())
    CourseCategory=catVecCourseTemp

    if totalW!=float(100):
        session.flash= T('Can not find the correct weighting defined in the course. You can not use this function')
        redirect(URL('default','index'))


    totalW=float(0)
    LabCategory=None
    catLabTemp=None
    catVecLabTemp=[]
    LabActivities = None
    validateLaboratory=None
    if existLab == True:
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
    t.append(T('Carnet'))
    t.append(T('Name'))
    t.append(T('Laboratory'))
    t.append('Zona')
    if request.vars['op'] == '1':
        t.append('Final')
    elif request.vars['op'] == '2':
        t.append(T("First recovery test"))
    elif request.vars['op'] == '3':
        t.append(T("Second recovery test"))
    l.append(t) 


    t=[]
    for t1 in students:
        t=[]
        t.append(str(t1.carnet.carnet))
        try:
            var_auth_user = db((db.auth_user.id==t1.carnet.id_auth_user)).select().first()
            t.append(str(var_auth_user.first_name) + " " + str(var_auth_user.last_name))
        except:
            t.append("")
        pass
        #Position in the vector of activities-
        posVCC=0
        #Vars to the control of grade of the student
        totalCategory=float(0)
        totalActivities=0
        totalLab_Final=0
        totalFinal_Clase=0
        totalCarry=float(0)
        #<!--****************************************FILL THE GRADES OF THE STUDENT****************************************-->
        #<!--LABORATORY ACTIVITIES-->
        if existLab==True:
            totalCategory=float(0)
            isValidate=False
            #<!--Revalidation of laboratory-->
            for validate in validateLaboratory:
                if validate.carnet==t1.carnet:
                    isValidate=True
                    #<!--Show grade of laboratory-->
                    totalLab_Final=int(round(validate.grade,0))
                    if validate.validation_type==False:
                        t.append(str(totalLab_Final))
                    else:
                        t.append('')
                    totalCategory=float((totalLab_Final*totalLab)/100)


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
                #<!--Show grade of laboratory-->
                totalLab_Final=int(round(totalCarry_Lab,0))
                t.append(str(totalLab_Final))
                totalCategory=float((totalLab_Final*totalLab)/100)

            #<!--Plus the laboratory to the carry-->
            totalCarry=totalCarry+totalCategory
        else:
            #<!--Show grade of laboratory-->
            t.append('0')


        #<!--COURSE ACTIVITIES-->
        for category in CourseCategory:
            if category.category.category!="Laboratorio" and category.category.category!="Examen Final":
                totalCategory=float(0)
                totalActivities=0
                for c in CourseActivities[posVCC]:
                    studentGrade = db((db.grades.activity==c.id)&(db.grades.academic_assignation==t1.id)).select().first()
                    if studentGrade is None:
                        totalCategory=totalCategory+float(0)
                    else:
                        if category.specific_grade==True:
                            totalCategory=totalCategory+float((studentGrade.grade*c.grade)/100)
                        else:
                            totalCategory=totalCategory+float(studentGrade.grade)
                    totalActivities=totalActivities+1

                if category.specific_grade==True:
                    None
                else:
                    if totalActivities==0:
                        totalActivities=1
                    totalActivities=totalActivities*100
                    totalCategory=float((totalCategory*float(category.grade))/float(totalActivities))
                totalCarry=totalCarry+totalCategory
                posVCC=posVCC+1
            elif category.category.category=="Examen Final":
                totalCategory=float(0)
                totalActivities=0
                for c in CourseActivities[posVCC]:
                    studentGrade = db((db.grades.activity==c.id)&(db.grades.academic_assignation==t1.id)).select().first()
                    if studentGrade is None:
                        totalCategory=totalCategory+float(0)
                    else:
                        if category.specific_grade==True:
                            totalCategory=totalCategory+float((studentGrade.grade*c.grade)/100)
                        else:
                            totalCategory=totalCategory+float(studentGrade.grade)
                    totalActivities=totalActivities+1

                if category.specific_grade==True:
                    None
                else:
                    if totalActivities==0:
                        totalActivities=1
                    totalActivities=totalActivities*100
                    totalCategory=float((totalCategory*float(category.grade))/float(totalActivities))
                totalFinal_Clase=int(round(totalCategory,0))
                posVCC=posVCC+1
        totalCarry=int(round(totalCarry,0))

        if request.vars['type'] == 'class' and request.vars['op'] =='2':
                var_first_recovery_test =db((db.course_first_recovery_test.carnet==t1.carnet)&(db.course_first_recovery_test.semester==year.id)&(db.course_first_recovery_test.project==project_var.id)).select().first()
                if var_first_recovery_test is not None:
                    totalFinal_Clase=int(round( (var_first_recovery_test.grade)*var_final_grade/100,0))
                else:
                    totalFinal_Clase=int(0)

        if request.vars['type'] == 'class' and request.vars['op'] =='3':
                var_second_recovery_test =db((db.course_second_recovery_test.carnet==t1.carnet)&(db.course_second_recovery_test.semester==year.id)&(db.course_second_recovery_test.project==project_var.id)).select().first()
                if var_second_recovery_test is not None:
                    totalFinal_Clase=int(round( (var_second_recovery_test.grade)*var_final_grade/100,0))
                else:
                    totalFinal_Clase=int(0)

        

        if requirement is not None:
            if db((db.course_requirement_student.carnet==t1.carnet)&(db.course_requirement_student.requirement==requirement.id)).select().first() is not None:
                if existLab==True:
                    if totalLab_Final>=61:
                        t.append(str(totalCarry))
                        t.append(str(totalFinal_Clase))
                    else:
                        t.append('0')
                        t.append('0')
                else:
                    t.append(str(totalCarry))
                    t.append(str(totalFinal_Clase))
            else:
                t.append('0')
                t.append('0')
        else:
            if existLab==True:
                if totalLab_Final>=61:
                    t.append(str(totalCarry))
                    t.append(str(totalFinal_Clase))
                else:
                    t.append('0')
                    t.append('0')
            else:
                t.append(str(totalCarry))
                t.append(str(totalFinal_Clase))

        posVCC=0
        totalCategory=float(0)
        totalActivities=0
        totalCarry=float(0)
        totalFinal_Clase=0
        totalLab_Final=0
        l.append(t)
        t=[]


    nombre=project_var.name.replace(' ','_')+'_'+T(year.period.name).replace(' ','_')+str(year.yearp)
    return dict(filename=nombre, csvdata=l)

    
@auth.requires_login()
@auth.requires(auth.has_membership('Academic') or auth.has_membership('Student') or auth.has_membership('Teacher') or auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
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
        assigantion = db((db.user_project.assigned_user==auth.user.id)&\
                        (db.user_project.project == project_var.id)&\
                        ((db.user_project.period <= year.id) & \
                        ((db.user_project.period + db.user_project.periods) > year.id))).select(db.user_project.ALL).first()
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

    #Check the correct parameters
    if (request.vars['op'] != '1' and request.vars['op'] != '2' and request.vars['op'] != '3'):
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))

    teacher = db(((db.user_project.period <= year.id) & \
        ((db.user_project.period + db.user_project.periods) > year.id))&\
        (db.user_project.project == project_var.id) & \
        (db.user_project.assigned_user==db.auth_user.id)&\
        (db.auth_user.id==db.auth_membership.user_id)&\
        (db.auth_membership.group_id==3)).select().first()

    practice = db(((db.user_project.period <= year.id) & \
        ((db.user_project.period + db.user_project.periods) > year.id))&\
        (db.user_project.project == project_var.id) & \
        (db.user_project.assigned_user==db.auth_user.id)&\
        (db.auth_user.id==db.auth_membership.user_id)&\
        (db.auth_membership.group_id==2)).select()
    if request.vars['type'] == 'class':
        academic_assig2 = db((db.academic.id==db.academic_course_assignation.carnet)&(db.academic_course_assignation.semester == year.id) & (db.academic_course_assignation.assignation==project_var.id)).select(orderby=db.academic.carnet)
    else:
        academic_assig2 = db((db.academic.id==db.academic_course_assignation.carnet)&(db.academic_course_assignation.semester == year.id) & (db.academic_course_assignation.assignation==project_var.id) & (db.academic_course_assignation.laboratorio==True)).select(orderby=db.academic.carnet)

    students=[]
    for acaT in academic_assig2:
        students.append(acaT.academic_course_assignation)

    var_final_grade = 0.00
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
            var_final_grade = categoryC.grade
            if ( request.vars['op'] == '2' or  request.vars['op'] == '3'):
                None
            else:
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
    t.append(T('Name'))
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
    if request.vars['op'] is not None and request.vars['op']=='2':
        t.append(T("First recovery test")+'\n(100 pts)')
        t.append(T("First recovery test")+'\n('+str(var_final_grade)+' pts)')
    if request.vars['op'] is not None and request.vars['op']=='3':
        t.append(T("Second recovery test")+'\n(100 pts)')
        t.append(T("Second recovery test")+'\n('+str(var_final_grade)+' pts)')


    t.append(T('Final Grade') +'\n(100 pts)')
    l.append(t) 


    t=[]
    for t1 in students:
        t=[]
        if request.vars['type'] == 'class':
            t.append(str(t1.carnet.carnet))
            
            try:
                var_auth_user = db((db.auth_user.id==t1.carnet.id_auth_user)).select().first()
                t.append(str(var_auth_user.first_name) + " " + str(var_auth_user.last_name))
            except:
                t.append("")
            pass
            #Position in the vector of activities-
            posVCC=0
            #Vars to the control of grade of the student
            totalCategory=float(0)
            totalActivities=0
            totalCarry=float(0)
            #<!--****************************************FILL THE GRADES OF THE STUDENT****************************************-->
            #<!--COURSE ACTIVITIES-->
            for category in CourseCategory:
                if category.category.category!="Laboratorio" and category.category.category!="Examen Final":
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
                        t.append(str(round(totalCategory,2)))
                    else:
                        if totalActivities==0:
                            totalActivities=1
                        totalActivities=totalActivities*100
                        totalCategory=float((totalCategory*float(category.grade))/float(totalActivities))
                        t.append(str(round(totalCategory,2)))
                    totalCarry=totalCarry+totalCategory
                    posVCC=posVCC+1
                elif category.category.category=="Examen Final":
                    totalCarry=int(round(totalCarry,0))
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
                        t.append(str(round(totalCategory,2)))
                    else:
                        if totalActivities==0:
                            totalActivities=1
                        totalActivities=totalActivities*100
                        totalCategory=float((totalCategory*float(category.grade))/float(totalActivities))
                        t.append(str(round(totalCategory,2)))
                    totalCategory=int(round(totalCategory,0))
                    totalCarry=totalCarry+totalCategory
                    posVCC=posVCC+1


            if request.vars['type'] == 'class' and existLab==True:
                totalCategory=float(0)
                isValidate=False
                #<!--Revalidation of laboratory-->
                for validate in validateLaboratory:
                    if validate.carnet==t1.carnet:
                        isValidate=True
                        totalCategory=float((int(round(validate.grade,0))*totalLab)/100)


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
                    totalCategory=float((int(round(totalCarry_Lab,0))*totalLab)/100)


                #<!--Show grade of laboratory-->
                t.append(str(round(totalCategory,2)))
                #<!--Plus the laboratory to the carry-->
                totalCarry=totalCarry+totalCategory

            if request.vars['type'] == 'class' and requirement is not None:
                if db((db.course_requirement_student.carnet==t1.carnet)&(db.course_requirement_student.requirement==requirement.id)).select().first() is not None:
                    t.append(T('True'))
                else:
                    t.append(T('False'))

            if request.vars['type'] == 'class' and request.vars['op'] =='2':
                var_first_recovery_test =db((db.course_first_recovery_test.carnet==t1.carnet)&(db.course_first_recovery_test.semester==year.id)&(db.course_first_recovery_test.project==project_var.id)).select().first()
                if var_first_recovery_test is not None:
                    t.append(str(round((var_first_recovery_test.grade),2)))
                    t.append(str(round( (var_first_recovery_test.grade)*var_final_grade/100,2)))
                    totalCarry=totalCarry+round( (var_first_recovery_test.grade)*var_final_grade/100,0)
                else:
                    t.append('')
                    t.append('')

            if request.vars['type'] == 'class' and request.vars['op'] =='3':
                var_second_recovery_test =db((db.course_second_recovery_test.carnet==t1.carnet)&(db.course_second_recovery_test.semester==year.id)&(db.course_second_recovery_test.project==project_var.id)).select().first()
                if var_second_recovery_test is not None:
                    t.append(str(round((var_second_recovery_test.grade),2)))
                    t.append(str(round( (var_second_recovery_test.grade)*var_final_grade/100,2)))
                    totalCarry=totalCarry+round( (var_second_recovery_test.grade)*var_final_grade/100,0)
                else:
                    t.append('')
                    t.append('')

            if request.vars['type'] == 'class' and requirement is not None:
                if db((db.course_requirement_student.carnet==t1.carnet)&(db.course_requirement_student.requirement==requirement.id)).select().first() is not None:
                    if request.vars['type'] == 'class' and existLab==True:
                        if totalCategory>=float((61*totalLab)/100):
                            t.append(str(int(round(totalCarry,0))))
                        else:
                            t.append('0')
                    else:
                        t.append(str(int(round(totalCarry,0))))
                else:
                    t.append('0')
            else:
                if request.vars['type'] == 'class' and existLab==True:
                    if totalCategory>=float((61*totalLab)/100):
                        t.append(str(int(round(totalCarry,0))))
                    else:
                        t.append('0')
                else:
                    t.append(str(int(round(totalCarry,0))))
            posVCC=0
            totalCategory=float(0)
            totalActivities=0
            totalCarry=float(0)
            l.append(t)
            t=[]
        else:
            t.append(str(t1.carnet.carnet))
            try:
                var_auth_user = db((db.auth_user.id==t1.carnet.id_auth_user)).select().first()
                t.append(str(var_auth_user.first_name) + " " + str(var_auth_user.last_name))
            except:
                t.append("")
            pass
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
                    t.append(str(round(totalCategory,2)))
                else:
                    if totalActivities==0:
                        totalActivities=1
                    pass
                    totalActivities=totalActivities*100
                    totalCategory=float((totalCategory*float(category.grade))/float(totalActivities))
                    t.append(str(round(totalCategory,2)))
                totalCarry=totalCarry+totalCategory
                posVCC=posVCC+1

            t.append(str(int(round(totalCarry,0))))
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
    action_Export=False
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

    tutor_access = False
    if auth.has_membership('Super-Administrator') == False and auth.has_membership('Ecys-Administrator')==False:
        assigantion = db((db.user_project.assigned_user==auth.user.id)&\
                        (db.user_project.project == project_var.id)&\
                        ((db.user_project.period <= year.id) & \
                        ((db.user_project.period + db.user_project.periods) > year.id))).select(db.user_project.ALL).first()

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
        else:
            tutor_access = True

    exception_query = db(db.course_laboratory_exception.project == project_var.id).select().first()
    exception_s_var = False
    exception_t_var = False
    if exception_query is not None:
        exception_t_var = exception_query.t_edit_lab
        exception_s_var = exception_query.s_edit_course


    #Check the correct parameters
    if (request.vars['type'] != 'class' and request.vars['type']!='lab'):
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))

    teacher = db(((db.user_project.period <= year.id) & \
        ((db.user_project.period + db.user_project.periods) > year.id))&\
        (db.user_project.project == project_var.id) & \
        (db.user_project.assigned_user==db.auth_user.id)&\
        (db.auth_user.id==db.auth_membership.user_id)&\
        (db.auth_membership.group_id==3)).select().first()

    practice = db(((db.user_project.period <= year.id) & \
        ((db.user_project.period + db.user_project.periods) > year.id))&\
        (db.user_project.project == project_var.id) & \
        (db.user_project.assigned_user==db.auth_user.id)&\
        (db.auth_user.id==db.auth_membership.user_id)&\
        (db.auth_membership.group_id==2)).select()

    if request.vars['type'] == 'class':
        academic_assig = db((db.academic.id==db.academic_course_assignation.carnet)&(db.academic_course_assignation.semester == year.id) & (db.academic_course_assignation.assignation==project_var.id)).select(orderby=db.academic.carnet)
    else:
        academic_assig = db((db.academic.id==db.academic_course_assignation.carnet)&(db.academic_course_assignation.semester == year.id) & (db.academic_course_assignation.assignation==project_var.id) & (db.academic_course_assignation.laboratorio==True)).select(orderby=db.academic.carnet)

    students=[]
    for acaT in academic_assig:
        students.append(acaT.academic_course_assignation)

    var_final_grade = 0.00

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
            var_final_grade = categoryC.grade
            if ( request.vars['op'] == '2' or  request.vars['op'] == '3'):
                None
            else:
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

    #Enable the course
    if request.vars['list'] =='cancel':
        if (auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator')):
            course_ended_var = db((db.course_ended.project==project_var.id) & (db.course_ended.period==year.id) ).select().first()
            if course_ended_var != None:
                if course_ended_var.finish == True:
                    db((db.course_ended.project==project_var.id) & (db.course_ended.period==year.id) ).delete()
                    response.flash= T('Course has been enabled')


    #Export to CSV general activity report
    if request.vars['list'] =='True':
        if (request.vars['op'] is None) or (request.vars['op'] == '') or (request.vars['op']  == '1') or (request.vars['op']  == '0'):
                redirect(URL('activity_control','general_report_activities_export',vars=dict(project = project_var.id, period = year.id, type=request.vars['type'], op=1)))
        elif request.vars['op']  == '2':
            redirect(URL('activity_control','general_report_activities_export',vars=dict(project = project_var.id, period = year.id, type=request.vars['type'], op=2)))
        elif request.vars['op']  == '3':
            redirect(URL('activity_control','general_report_activities_export',vars=dict(project = project_var.id, period = year.id, type=request.vars['type'], op=3)))
        else:
            redirect(URL('activity_control','General_report_activities',vars=dict(project = project_var.id, period = year.id, type=request.vars['type'])))

    #Finish the course and generate the csv file format technical school    
    if request.vars['list'] =='False':
        if request.vars['type'] == 'class' and (auth.has_membership('Ecys-Administrator') or auth.has_membership('Super-Administrator') or auth.has_membership('Teacher') or (auth.has_membership('Student') and exception_s_var == True and tutor_access == True)):
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
                pass
                #Insert to course_ended           
                db.course_ended.insert(project = project_var.id,
                                period = year.id,
                                finish =  True)
                
                #Generate csv file format technical school
                action_Export=True
            else:
                #Generate csv file format technical school
                if (request.vars['op'] is None) or (request.vars['op'] == '') or (request.vars['op']  == '1') or (request.vars['op']  == '0'):
                    redirect(URL('activity_control','Course_Format_Technical_School',vars=dict(project = project_var.id, period = year.id, type=request.vars['type'], op=1)))
                elif request.vars['op']  == '2':
                    redirect(URL('activity_control','Course_Format_Technical_School',vars=dict(project = project_var.id, period = year.id, type=request.vars['type'], op=2)))
                elif request.vars['op']  == '3':
                    redirect(URL('activity_control','Course_Format_Technical_School',vars=dict(project = project_var.id, period = year.id, type=request.vars['type'], op=3)))
                else:
                    redirect(URL('activity_control','General_report_activities',vars=dict(project = project_var.id, period = year.id, type=request.vars['type'])))
        else:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))


    controlP = db((db.student_control_period.period_name==(T(year.period.name)+" "+str(year.yearp)))).select().first()
    requirement = db((db.course_requirement.semester==year.id)&(db.course_requirement.project==project_var.id)).select().first()

    course_ended = False
    course_ended_var = db((db.course_ended.project==project_var.id) & (db.course_ended.period==year.id) ).select().first()
    if course_ended_var != None:
        if course_ended_var.finish == True:
            course_ended=True

    if request.vars['op'] == '0':
        response.flash= T('Course hasn’t finalized.')


    return dict(project = project_var,
                year = year, 
                teacher=teacher, 
                practice=practice, 
                students=students, 
                CourseCategory=CourseCategory, 
                CourseActivities=CourseActivities, 
                existLab=existLab, 
                LabCategory=LabCategory, 
                LabActivities=LabActivities, 
                validateLaboratory=validateLaboratory, 
                totalLab=totalLab, 
                controlP=controlP,
                var_final_grade = var_final_grade,
                requirement=requirement, 
                course_ended = course_ended,
                exception_s_var=exception_s_var,
                exception_t_var=exception_t_var,
                tutor_access = tutor_access,
                action_Export=action_Export)




#******************************************************************************************************************************************************************
#******************************************************************************************************************************************************************
#******************************************************************************************************************************************************************
#******************************************************************************************************************************************************************



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
            if auth.has_membership('Super-Administrator') == False and auth.has_membership('Ecys-Administrator')==False:
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
        assigantion = db((db.user_project.assigned_user==auth.user.id)&\
                        (db.user_project.project == project_var.id)&\
                        ((db.user_project.period <= year.id) & \
                        ((db.user_project.period + db.user_project.periods) > year.id))).select(db.user_project.ALL).first()
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
        if activityPermition is None:
            grid = SQLFORM.grid(query, csv=False, paginate=1, searchable=False, links=links)
        else:
            grid = SQLFORM.grid(query, csv=False, paginate=1, create=False, searchable=False, links=links)
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
            if auth.has_membership('Super-Administrator') == False and auth.has_membership('Ecys-Administrator')==False:
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
        assigantion = db((db.user_project.assigned_user==auth.user.id)&\
                        (db.user_project.project == project_var.id)&\
                        ((db.user_project.period <= year.id) & \
                        ((db.user_project.period + db.user_project.periods) > year.id))).select(db.user_project.ALL).first()

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
        grid = SQLFORM.grid(query, csv=False, paginate=10, editable=False, searchable=False)
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

    academic_assig3 = db((db.academic.id==db.academic_course_assignation.carnet)&(db.academic_course_assignation.semester == request.vars['period']) & (db.academic_course_assignation.assignation==request.vars['project'])).select(orderby=db.academic.carnet)
    students=[]
    for acaT in academic_assig3:
        students.append(acaT.academic_course_assignation)
    return dict(project = project_var, year = year, requirement=requirement, grid=grid, students=students)



#********************************************************************************************************************************************************************************************************
#********************************************************************************************************************************************************************************************************
#********************************************************************************************************************************************************************************************************
#********************************************************************************************************************************************************************************************************
#***************************************************Management Report Grades***************************************************

#********************************************************
#Export full management reporting grade
@auth.requires_login()
@auth.requires(auth.has_membership('Teacher'))
def grades_management_export():
    #Vars of the report
    report=[]
    tempRemport1=[]
    tempRemport2=[]
    tempRemport3=[]
    tempRemport4=[]
    tempRemport5=[]
    #Obtain the current period of the system and all the register periods
    import cpfecys
    from datetime import datetime
    year = cpfecys.current_year_period()

    #Check if the user is assigned to the course
    assigantions = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == year.id)).select()
    if assigantions.first() is None:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))

    #Check if a search exist, verify that they are just numbers
    if session.search_grades_management != "" and session.search_grades_management is not None:
        if str(session.search_grades_management).isdigit()==False:
            session.search_grades_management = ""
            session.flash=T('The lookup value is not allowed.')
            redirect(URL('activity_control','grades_management'))

    #Vec with the months of the current period
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

    #report.append()

    #Report heading
    tempRemport1=[]
    tempRemport1.append('Reporte Gestion de Notas')
    report.append(tempRemport1)
    tempRemport1=[]
    tempRemport1.append(T(year.period.name)+' '+str(year.yearp))
    report.append(tempRemport1)

    #LEVEL 1
    #Heading Level 1
    tempRemport1=[]
    tempRemport1.append(T('Course'))
    tempRemport1.append(T('Total inserted'))
    tempRemport1.append(T('Total modified'))
    tempRemport1.append(T('Total out'))
    report.append(tempRemport1)
    #Body Level 1
    for assigantion in assigantions:
        tempRemport1=[]
        tempRemport1.append(assigantion.project.name)
        if session.search_grades_management == "" or session.search_grades_management is None:
            tempRemport1.append(str(db((db.grades_log.project==assigantion.project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.operation_log=='insert')).count(db.grades_log.id)))
            tempRemport1.append(str(db((db.grades_log.project==assigantion.project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.operation_log=='update')).count(db.grades_log.id)))
            tempRemport1.append(str(db((db.grades_log.project==assigantion.project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.operation_log=='delete')).count(db.grades_log.id)))
        else:
            tempRemport1.append(str(db((db.grades_log.project==assigantion.project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.operation_log=='insert')&(db.grades_log.academic.like('%'+str(session.search_grades_management)+'%'))).count(db.grades_log.id)))
            tempRemport1.append(str(db((db.grades_log.project==assigantion.project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.operation_log=='update')&(db.grades_log.academic.like('%'+str(session.search_grades_management)+'%'))).count(db.grades_log.id)))
            tempRemport1.append(str(db((db.grades_log.project==assigantion.project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.operation_log=='delete')&(db.grades_log.academic.like('%'+str(session.search_grades_management)+'%'))).count(db.grades_log.id)))
        pass
        report.append(tempRemport1)

        #LEVEL 2
        #Heading Level 2
        tempRemport2=[]
        tempRemport2.append('')
        tempRemport2.append(T('Month'))
        tempRemport2.append(T('Total inserted'))
        tempRemport2.append(T('Total modified'))
        tempRemport2.append(T('Total out'))
        report.append(tempRemport2)
        #Body Level 2
        for month in vecMonth:
            tempRemport2=[]
            tempRemport2.append('')
            start = datetime.strptime(str(year.yearp) + '-' + str(month[0]) +'-01', "%Y-%m-%d")
            if month[2]==1:
                end = datetime.strptime(str(year.yearp+1) + '-' + str(month[2]) +'-01', "%Y-%m-%d")
            else:
                end = datetime.strptime(str(year.yearp) + '-' + str(month[2]) +'-01', "%Y-%m-%d")
            pass
            tempRemport2.append(month[1])
            if session.search_grades_management == "" or session.search_grades_management is None:
                tempRemport2.append(str(db((db.grades_log.project==assigantion.project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.operation_log=='insert')&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))).count(db.grades_log.id)))
                tempRemport2.append(str(db((db.grades_log.project==assigantion.project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.operation_log=='update')&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))).count(db.grades_log.id)))
                tempRemport2.append(str(db((db.grades_log.project==assigantion.project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.operation_log=='delete')&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))).count(db.grades_log.id)))
            else:
                tempRemport2.append(str(db((db.grades_log.project==assigantion.project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.operation_log=='insert')&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.academic.like('%'+str(session.search_grades_management)+'%'))).count(db.grades_log.id)))
                tempRemport2.append(str(db((db.grades_log.project==assigantion.project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.operation_log=='update')&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.academic.like('%'+str(session.search_grades_management)+'%'))).count(db.grades_log.id)))
                tempRemport2.append(str(db((db.grades_log.project==assigantion.project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.operation_log=='delete')&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.academic.like('%'+str(session.search_grades_management)+'%'))).count(db.grades_log.id)))
            pass
            report.append(tempRemport2)

            #LEVEL 3
            #Heading Level 3
            tempRemport3=[]
            tempRole = []
            tempRemport3.append('')
            tempRemport3.append('')
            tempRemport3.append(T('Role'))
            tempRemport3.append(T('Total inserted'))
            tempRemport3.append(T('Total modified'))
            tempRemport3.append(T('Total out'))
            report.append(tempRemport3)
            #Body Level 3
            for tempR in db((db.auth_group.role!='Academic')&(db.auth_group.role!='DSI')).select():
                tempRole.append(tempR.role)
            for tempR in db((db.grades_log.yearp==year.yearp)&(db.grades_log.period==T(year.period.name))&(db.grades_log.project==assigantion.project.name)&(~db.grades_log.roll.belongs(tempRole))).select(db.grades_log.roll, distinct=True):
                tempRole.append(tempR.roll)
            for roll in tempRole:
                tempRemport3=[]
                tempRemport3.append('')
                tempRemport3.append('')
                tempRemport3.append(T('Rol '+str(roll)))
                pass
                if session.search_grades_management == "" or session.search_grades_management is None:
                    tempRemport3.append(str(db((db.grades_log.project==assigantion.project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.operation_log=='insert')&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.roll==roll)).count(db.grades_log.id)))
                    tempRemport3.append(str(db((db.grades_log.project==assigantion.project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.operation_log=='update')&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.roll==roll)).count(db.grades_log.id)))
                    tempRemport3.append(str(db((db.grades_log.project==assigantion.project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.operation_log=='delete')&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.roll==roll)).count(db.grades_log.id)))
                else:
                    tempRemport3.append(str(db((db.grades_log.project==assigantion.project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.operation_log=='insert')&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.roll==roll)&(db.grades_log.academic.like('%'+str(session.search_grades_management)+'%'))).count(db.grades_log.id)))
                    tempRemport3.append(str(db((db.grades_log.project==assigantion.project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.operation_log=='update')&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.roll==roll)&(db.grades_log.academic.like('%'+str(session.search_grades_management)+'%'))).count(db.grades_log.id)))
                    tempRemport3.append(str(db((db.grades_log.project==assigantion.project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.operation_log=='delete')&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.roll==roll)&(db.grades_log.academic.like('%'+str(session.search_grades_management)+'%'))).count(db.grades_log.id)))
                pass
                report.append(tempRemport3)

                #LEVEL 4
                #Heading Level 4
                tempRemport4=[]
                tempUsers=[]
                tempRemport4.append('')
                tempRemport4.append('')
                tempRemport4.append('')
                tempRemport4.append(T('User'))
                tempRemport4.append(T('Total inserted'))
                tempRemport4.append(T('Total modified'))
                tempRemport4.append(T('Total out'))
                report.append(tempRemport4)
                #Body Level 4
                tempUsers2=[]
                registerRol = db(db.auth_group.role==roll).select().first()
                if ((roll=='Super-Administrator') or (roll=='Ecys-Administrator')):
                    for valueU in db((db.auth_membership.group_id==registerRol.id)).select(db.auth_membership.user_id, distinct=True):
                        tempUsers.append(valueU.user_id.username)
                else:
                    for valueU in db((db.auth_membership.group_id==registerRol.id)).select(db.auth_membership.user_id, distinct=True):
                        tempUsers2.append(valueU.user_id)
                    for valueU in db((db.user_project.period==year.id)&(db.user_project.project==assigantion.project)&(db.user_project.assigned_user.belongs(tempUsers2))).select(db.user_project.assigned_user, distinct=True):
                        tempUsers.append(valueU.assigned_user.username)
                pass
                for valueU in db((db.grades_log.yearp==year.yearp)&(db.grades_log.period==T(year.period.name))&(db.grades_log.project==assigantion.project.name)&(db.grades_log.roll==roll)&(~db.grades_log.user_name.belongs(tempUsers))).select(db.grades_log.user_name, distinct=True):
                    tempUsers.append(valueU.user_name)
                for userr in tempUsers:
                    tempRemport4=[]
                    tempRemport4.append('')
                    tempRemport4.append('')
                    tempRemport4.append('')
                    tempRemport4.append(userr)
                    if session.search_grades_management == "" or session.search_grades_management is None:
                        tempRemport4.append(str(db((db.grades_log.project==assigantion.project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.operation_log=='insert')&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.roll==roll)&(db.grades_log.user_name==userr)).count(db.grades_log.id)))
                        tempRemport4.append(str(db((db.grades_log.project==assigantion.project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.operation_log=='update')&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.roll==roll)&(db.grades_log.user_name==userr)).count(db.grades_log.id)))
                        tempRemport4.append(str(db((db.grades_log.project==assigantion.project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.operation_log=='delete')&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.roll==roll)&(db.grades_log.user_name==userr)).count(db.grades_log.id)))
                    else:
                        tempRemport4.append(str(db((db.grades_log.project==assigantion.project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.operation_log=='insert')&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.roll==roll)&(db.grades_log.user_name==userr)&(db.grades_log.academic.like('%'+str(session.search_grades_management)+'%'))).count(db.grades_log.id)))
                        tempRemport4.append(str(db((db.grades_log.project==assigantion.project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.operation_log=='update')&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.roll==roll)&(db.grades_log.user_name==userr)&(db.grades_log.academic.like('%'+str(session.search_grades_management)+'%'))).count(db.grades_log.id)))
                        tempRemport4.append(str(db((db.grades_log.project==assigantion.project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.operation_log=='delete')&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.roll==roll)&(db.grades_log.user_name==userr)&(db.grades_log.academic.like('%'+str(session.search_grades_management)+'%'))).count(db.grades_log.id)))
                    pass
                    report.append(tempRemport4)

                    #LEVEL 5
                    temp_vecAllUserRoleMonth=[]
                    tempRemport5=[]
                    #Body Level 5
                    if session.search_grades_management == "" or session.search_grades_management is None:
                        temp_vecAllUserRoleMonth.append(db((db.grades_log.project==assigantion.project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.operation_log=='insert')&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.roll==roll)&(db.grades_log.user_name==userr)).select())
                        temp_vecAllUserRoleMonth.append(db((db.grades_log.project==assigantion.project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.operation_log=='update')&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.roll==roll)&(db.grades_log.user_name==userr)).select())
                        temp_vecAllUserRoleMonth.append(db((db.grades_log.project==assigantion.project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.operation_log=='delete')&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.roll==roll)&(db.grades_log.user_name==userr)).select())
                    else:
                        temp_vecAllUserRoleMonth.append(db((db.grades_log.project==assigantion.project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.operation_log=='insert')&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.roll==roll)&(db.grades_log.user_name==userr)&(db.grades_log.academic.like('%'+str(session.search_grades_management)+'%'))).select())
                        temp_vecAllUserRoleMonth.append(db((db.grades_log.project==assigantion.project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.operation_log=='update')&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.roll==roll)&(db.grades_log.user_name==userr)&(db.grades_log.academic.like('%'+str(session.search_grades_management)+'%'))).select())
                        temp_vecAllUserRoleMonth.append(db((db.grades_log.project==assigantion.project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.operation_log=='delete')&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.roll==roll)&(db.grades_log.user_name==userr)&(db.grades_log.academic.like('%'+str(session.search_grades_management)+'%'))).select())
                    pass
                    varTypeHead=0
                    for field in temp_vecAllUserRoleMonth:
                        for camp in field:
                            if varTypeHead==0:
                                #Heading Level 5
                                tempRemport5=[]
                                tempRemport5.append('')
                                tempRemport5.append('')
                                tempRemport5.append('')
                                tempRemport5.append('')
                                tempRemport5.append(T('User resolution'))
                                tempRemport5.append(T('Role resolution'))
                                tempRemport5.append(T('Date of resolution'))
                                tempRemport5.append(T('Operation'))
                                tempRemport5.append(T('Description'))
                                tempRemport5.append(T('Category'))
                                tempRemport5.append(T('Activity'))
                                tempRemport5.append(T('Rol Academic'))
                                tempRemport5.append(T('Before Grade'))
                                tempRemport5.append(T('Grade edited'))
                                report.append(tempRemport5)
                                varTypeHead=1
                            tempRemport5=[]
                            tempRemport5.append('')
                            tempRemport5.append('')
                            tempRemport5.append('')
                            tempRemport5.append('')
                            tempRemport5.append(str(camp.user_name))
                            tempRemport5.append(T('Rol '+str(camp.roll)))
                            tempRemport5.append(str(camp.date_log))
                            tempRemport5.append(str(camp.operation_log))
                            tempRemport5.append(str(camp.description))
                            tempRemport5.append(str(camp.category))
                            tempRemport5.append(str(camp.activity))
                            tempRemport5.append(str(camp.academic))
                            tempRemport5.append(str(camp.before_grade))
                            tempRemport5.append(str(camp.after_grade))
                            report.append(tempRemport5)
                        pass
                    pass
                    #End Level 5
                pass
                #End Level 4
                report.append('')
                report.append('')
            pass
            #End Level 3
            report.append('')
            report.append('')
            report.append('')
            report.append('')
        pass
        #End Level 2
        report.append('')
        report.append('')
        report.append('')
        report.append('')
        report.append('')
        report.append('')
    pass
    #End Level 1

    return dict(filename='ReporteGestionNotas', csvdata=report)



#********************************************************
#Export management reporting grade levels
@auth.requires_login()
@auth.requires(auth.has_membership('Teacher'))
def grades_management_level_export():
    #Vars of the report
    createReport = True
    report=[]
    tempRemport1=[]
    #Obtain the current period of the system and all the register periods
    import cpfecys
    from datetime import datetime
    year = cpfecys.current_year_period()

    #Check if the user is assigned to the course
    assigantions = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == year.id)).select()
    if assigantions.first() is None:
        createReport=False

    #Check if a search exist, verify that they are just numbers
    if session.search_grades_management != "" and session.search_grades_management is not None:
        if str(session.search_grades_management).isdigit()==False:
            session.search_grades_management = ""
            createReport=False

    #Vec with the months of the current period
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

    #Check the parameters
    if request.vars['level']=='1' or request.vars['level']=='2' or request.vars['level']=='3' or request.vars['level']=='4' or request.vars['level']=='5':
        if int(request.vars['level']) > 1 and createReport==True:
            #Check if the project is correct
            if request.vars['level_project'] is None or request.vars['level_project']=='':
                createReport=False
            else:
                level_project = request.vars['level_project']
                level_project = db(db.project.id==level_project).select().first()
                if level_project is None:
                    createReport=False
                else:
                    exportReport=False
                    for assigantion in assigantions:
                        if assigantion.project==level_project.id:
                            exportReport=True
                    if exportReport==False:
                        createReport=False
        pass

        if int(request.vars['level']) > 2 and createReport==True:
            #Check if the Month is correct
            if request.vars['level_month'] is None or request.vars['level_month']=='':
                createReport=False
            else:
                if year.period == 1:
                    try:
                        if int(request.vars['level_month']) >= 1 and int(request.vars['level_month']) <=5:
                            level_month=str(request.vars['level_month'])
                        else:
                            createReport=False
                    except:
                        createReport=False
                else:
                    try:
                        if int(request.vars['level_month']) >= 6 and int(request.vars['level_month']) <=12:
                            level_month=str(request.vars['level_month'])
                        else:
                            createReport=False
                    except:
                        createReport=False
                
            #Check if the type is correct
            if request.vars['level_tipo'] is None or request.vars['level_tipo']=='':
                createReport=False
            else:
                if str(request.vars['level_tipo'])!='all' and str(request.vars['level_tipo'])!='i' and str(request.vars['level_tipo'])!='u' and str(request.vars['level_tipo'])!='d':
                    createReport=False
                else:
                    level_tipo = str(request.vars['level_tipo'])
        pass

        if int(request.vars['level']) > 3 and createReport==True:
            if request.vars['level_rol'] is None or request.vars['level_rol']=='':
                createReport=False
            else:
                value = db(db.auth_group.role==str(request.vars['level_rol'])).select().first()
                if value is None:
                    #Check if the log has a roll that is not register
                    value = db((db.grades_log.yearp==year.yearp)&(db.grades_log.period==T(year.period.name))&(db.grades_log.project==level_project.name)&(db.grades_log.roll==str(request.vars['level_rol']))).select(db.grades_log.roll, distinct=True).first()
                    if value is None:
                        createReport=False
                    else:
                        level_rol=str(value.roll)
                else:
                    level_rol=str(value.role)
        pass

        if int(request.vars['level']) > 4 and createReport==True:
            if request.vars['level_user'] is None or request.vars['level_user']=='':
                createReport=False
            else:
                flagCheck = False
                #User Temp of auth_user where the username is equal
                userr = db(db.auth_user.username==str(request.vars['level_user'])).select().first()
                if ((level_rol=='Super-Administrator') or (level_rol=='Ecys-Administrator')):
                    if userr is not None:
                        #Check if the user has the rol specific
                        userrT = db(db.auth_membership.user_id==userr.id).select()
                        for tempUserCheck in userrT:
                            if tempUserCheck.group_id.role==level_rol:
                                flagCheck = True
                else:
                    if userr is not None:
                        #Check if the user has the rol specific
                        userrT = db(db.auth_membership.user_id==userr.id).select()
                        for tempUserCheck in userrT:
                            if tempUserCheck.group_id.role==level_rol:
                                if db((db.user_project.period==year.id)&(db.user_project.project==level_project.id)&(db.user_project.assigned_user==userr.id)).select().first() is not None:
                                    flagCheck = True

                if flagCheck==False:
                    #Check if the log has a roll that is not register
                    userr = db((db.grades_log.yearp==year.yearp)&(db.grades_log.period==T(year.period.name))&(db.grades_log.project==level_project.name)&(db.grades_log.roll==level_rol)&(db.grades_log.user_name==str(request.vars['userr']))).select().first()
                    if value is None:
                        createReport=False
                    else:
                        level_user=userr.user_name
                else:
                    level_user=userr.username
        pass
    else:
        createReport=False

    #MAKE REPORT
    if createReport==True:
        #Report heading
        tempRemport1=[]
        tempRemport1.append('Reporte Gestion de Notas')
        report.append(tempRemport1)
        tempRemport1=[]
        tempRemport1.append(T(year.period.name)+' '+str(year.yearp))
        report.append(tempRemport1)

        #LEVEL 1
        if request.vars['level']=='1':
            #Heading Level 1
            tempRemport1=[]
            tempRemport1.append('')
            report.append(tempRemport1)

            tempRemport1=[]
            tempRemport1.append(T('Detail'))
            report.append(tempRemport1)

            tempRemport1=[]
            tempRemport1.append(T('Course'))
            tempRemport1.append(T('Total inserted'))
            tempRemport1.append(T('Total modified'))
            tempRemport1.append(T('Total out'))
            report.append(tempRemport1)
            #Body Level 1
            for assigantion in assigantions:
                tempRemport1=[]
                tempRemport1.append(assigantion.project.name)
                if session.search_grades_management == "" or session.search_grades_management is None:
                    tempRemport1.append(str(db((db.grades_log.project==assigantion.project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.operation_log=='insert')).count(db.grades_log.id)))
                    tempRemport1.append(str(db((db.grades_log.project==assigantion.project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.operation_log=='update')).count(db.grades_log.id)))
                    tempRemport1.append(str(db((db.grades_log.project==assigantion.project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.operation_log=='delete')).count(db.grades_log.id)))
                else:
                    tempRemport1.append(str(db((db.grades_log.project==assigantion.project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.operation_log=='insert')&(db.grades_log.academic.like('%'+str(session.search_grades_management)+'%'))).count(db.grades_log.id)))
                    tempRemport1.append(str(db((db.grades_log.project==assigantion.project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.operation_log=='update')&(db.grades_log.academic.like('%'+str(session.search_grades_management)+'%'))).count(db.grades_log.id)))
                    tempRemport1.append(str(db((db.grades_log.project==assigantion.project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.operation_log=='delete')&(db.grades_log.academic.like('%'+str(session.search_grades_management)+'%'))).count(db.grades_log.id)))
                pass
                report.append(tempRemport1)
            pass
        

        #LEVEL 2
        elif request.vars['level']=='2':
            #Heading Level 2
            tempRemport1=[]
            tempRemport1.append(T('Course'))
            tempRemport1.append(level_project.name)
            report.append(tempRemport1)
            
            tempRemport1=[]
            tempRemport1.append('')
            report.append(tempRemport1)

            tempRemport1=[]
            tempRemport1.append(T('Detail'))
            report.append(tempRemport1)

            tempRemport1=[]
            tempRemport1.append(T('Month'))
            tempRemport1.append(T('Total inserted'))
            tempRemport1.append(T('Total modified'))
            tempRemport1.append(T('Total out'))
            report.append(tempRemport1)
            #Body Level 2
            for month in vecMonth:
                tempRemport1=[]
                start = datetime.strptime(str(year.yearp) + '-' + str(month[0]) +'-01', "%Y-%m-%d")
                if month[2]==1:
                    end = datetime.strptime(str(year.yearp+1) + '-' + str(month[2]) +'-01', "%Y-%m-%d")
                else:
                    end = datetime.strptime(str(year.yearp) + '-' + str(month[2]) +'-01', "%Y-%m-%d")
                pass
                tempRemport1.append(month[1])
                if session.search_grades_management == "" or session.search_grades_management is None:
                    tempRemport1.append(str(db((db.grades_log.project==level_project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='insert')).count(db.grades_log.id)))
                    tempRemport1.append(str(db((db.grades_log.project==level_project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='update')).count(db.grades_log.id)))
                    tempRemport1.append(str(db((db.grades_log.project==level_project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='delete')).count(db.grades_log.id)))
                else:
                    tempRemport1.append(str(db((db.grades_log.project==level_project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='insert')&(db.grades_log.academic.like('%'+str(session.search_grades_management)+'%'))).count(db.grades_log.id)))
                    tempRemport1.append(str(db((db.grades_log.project==level_project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='update')&(db.grades_log.academic.like('%'+str(session.search_grades_management)+'%'))).count(db.grades_log.id)))
                    tempRemport1.append(str(db((db.grades_log.project==level_project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='delete')&(db.grades_log.academic.like('%'+str(session.search_grades_management)+'%'))).count(db.grades_log.id)))
                pass
                report.append(tempRemport1)
        

        #LEVEL 3
        elif request.vars['level']=='3':
            #Heading Level 3
            tempRemport1=[]
            tempRemport1.append(T('Course'))
            tempRemport1.append(level_project.name)
            report.append(tempRemport1)

            tempRemport1=[]
            tempRemport1.append(T('Month'))
            for tempMonth in vecMonth:
                if str(tempMonth[0])==level_month:
                    tempRemport1.append(tempMonth[1])
                    start = datetime.strptime(str(year.yearp) + '-' + str(tempMonth[0]) +'-01', "%Y-%m-%d")
                    if tempMonth[2]==1:
                        end = datetime.strptime(str(year.yearp+1) + '-' + str(tempMonth[2]) +'-01', "%Y-%m-%d")
                    else:
                        end = datetime.strptime(str(year.yearp) + '-' + str(tempMonth[2]) +'-01', "%Y-%m-%d")
                    pass
            report.append(tempRemport1)

            tempRemport1=[]
            tempRemport1.append('')
            report.append(tempRemport1)

            tempRemport1=[]
            tempRemport1.append(T('Detail'))
            report.append(tempRemport1)

            tempRemport1=[]
            tempRole = []
            tempRemport1.append(T('Role'))
            if ((level_tipo=='all') or (level_tipo=='i')):
                tempRemport1.append(T('Total inserted'))
            if ((level_tipo=='all') or (level_tipo=='u')):
                tempRemport1.append(T('Total modified'))
            if ((level_tipo=='all') or (level_tipo=='d')):
                tempRemport1.append(T('Total out'))
            report.append(tempRemport1)
            #Body Level 3
            for tempR in db((db.auth_group.role!='Academic')&(db.auth_group.role!='DSI')).select():
                tempRole.append(tempR.role)
            for tempR in db((db.grades_log.yearp==year.yearp)&(db.grades_log.period==T(year.period.name))&(db.grades_log.project==level_project.name)&(~db.grades_log.roll.belongs(tempRole))).select(db.grades_log.roll, distinct=True):
                tempRole.append(tempR.roll)
            for roll in tempRole:
                tempRemport1=[]
                if roll=='Student':
                    tempRemport1.append(T('Rol Student'))
                else:
                    tempRemport1.append(T(roll))
                pass
                if session.search_grades_management == "" or session.search_grades_management is None:
                    if ((level_tipo=='all') or (level_tipo=='i')):
                        tempRemport1.append(str(db((db.grades_log.project==level_project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='insert')&(db.grades_log.roll==roll)).count(db.grades_log.id)))
                    if ((level_tipo=='all') or (level_tipo=='u')):
                        tempRemport1.append(str(db((db.grades_log.project==level_project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='update')&(db.grades_log.roll==roll)).count(db.grades_log.id)))
                    if ((level_tipo=='all') or (level_tipo=='d')):
                        tempRemport1.append(str(db((db.grades_log.project==level_project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='delete')&(db.grades_log.roll==roll)).count(db.grades_log.id)))
                else:
                    if ((level_tipo=='all') or (level_tipo=='i')):
                        tempRemport1.append(str(db((db.grades_log.project==level_project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='insert')&(db.grades_log.roll==roll)&(db.grades_log.academic.like('%'+str(session.search_grades_management)+'%'))).count(db.grades_log.id)))
                    if ((level_tipo=='all') or (level_tipo=='u')):
                        tempRemport1.append(str(db((db.grades_log.project==level_project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='update')&(db.grades_log.roll==roll)&(db.grades_log.academic.like('%'+str(session.search_grades_management)+'%'))).count(db.grades_log.id)))
                    if ((level_tipo=='all') or (level_tipo=='d')):
                        tempRemport1.append(str(db((db.grades_log.project==level_project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='delete')&(db.grades_log.roll==roll)&(db.grades_log.academic.like('%'+str(session.search_grades_management)+'%'))).count(db.grades_log.id)))
                pass
                report.append(tempRemport1)


        #LEVEL 4
        elif request.vars['level']=='4':
            #Heading Level 4
            tempRemport1=[]
            tempRemport1.append(T('Course'))
            tempRemport1.append(level_project.name)
            report.append(tempRemport1)

            tempRemport1=[]
            tempRemport1.append(T('Month'))
            for tempMonth in vecMonth:
                if str(tempMonth[0])==level_month:
                    tempRemport1.append(tempMonth[1])
                    start = datetime.strptime(str(year.yearp) + '-' + str(tempMonth[0]) +'-01', "%Y-%m-%d")
                    if tempMonth[2]==1:
                        end = datetime.strptime(str(year.yearp+1) + '-' + str(tempMonth[2]) +'-01', "%Y-%m-%d")
                    else:
                        end = datetime.strptime(str(year.yearp) + '-' + str(tempMonth[2]) +'-01', "%Y-%m-%d")
                    pass
            report.append(tempRemport1)

            tempRemport1=[]
            tempRemport1.append(T('Role'))
            tempRemport1.append(T('Rol '+level_rol))
            report.append(tempRemport1)

            tempRemport1=[]
            tempRemport1.append('')
            report.append(tempRemport1)

            tempRemport1=[]
            tempRemport1.append(T('Detail'))
            report.append(tempRemport1)

            tempRemport1=[]
            tempUsers=[]
            tempRemport1.append(T('User'))
            if ((level_tipo=='all') or (level_tipo=='i')):
                tempRemport1.append(T('Total inserted'))
            if ((level_tipo=='all') or (level_tipo=='u')):
                tempRemport1.append(T('Total modified'))
            if ((level_tipo=='all') or (level_tipo=='d')):
                tempRemport1.append(T('Total out'))
            report.append(tempRemport1)
            #Body Level 4
            tempUsers2=[]
            registerRol = db(db.auth_group.role==level_rol).select().first()
            if ((level_rol=='Super-Administrator') or (level_rol=='Ecys-Administrator')):
                for valueU in db((db.auth_membership.group_id==registerRol.id)).select(db.auth_membership.user_id, distinct=True):
                    tempUsers.append(valueU.user_id.username)
            else:
                for valueU in db((db.auth_membership.group_id==registerRol.id)).select(db.auth_membership.user_id, distinct=True):
                    tempUsers2.append(valueU.user_id)
                for valueU in db((db.user_project.period==year.id)&(db.user_project.project==level_project.id)&(db.user_project.assigned_user.belongs(tempUsers2))).select(db.user_project.assigned_user, distinct=True):
                    tempUsers.append(valueU.assigned_user.username)
            pass
            for valueU in db((db.grades_log.yearp==year.yearp)&(db.grades_log.period==T(year.period.name))&(db.grades_log.project==level_project.name)&(db.grades_log.roll==level_rol)&(~db.grades_log.user_name.belongs(tempUsers))).select(db.grades_log.user_name, distinct=True):
                tempUsers.append(valueU.user_name)
            for userr in tempUsers:
                tempRemport1=[]
                tempRemport1.append(userr)
                if session.search_grades_management == "" or session.search_grades_management is None:
                    if ((level_tipo=='all') or (level_tipo=='i')):
                        tempRemport1.append(str(db((db.grades_log.project==level_project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='insert')&(db.grades_log.roll==level_rol)&(db.grades_log.user_name==userr)).count(db.grades_log.id)))
                    if ((level_tipo=='all') or (level_tipo=='u')):
                        tempRemport1.append(str(db((db.grades_log.project==level_project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='update')&(db.grades_log.roll==level_rol)&(db.grades_log.user_name==userr)).count(db.grades_log.id)))
                    if ((level_tipo=='all') or (level_tipo=='d')):
                        tempRemport1.append(str(db((db.grades_log.project==level_project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='delete')&(db.grades_log.roll==level_rol)&(db.grades_log.user_name==userr)).count(db.grades_log.id)))
                else:
                    if ((level_tipo=='all') or (level_tipo=='i')):
                        tempRemport1.append(str(db((db.grades_log.project==level_project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='insert')&(db.grades_log.roll==level_rol)&(db.grades_log.user_name==userr)&(db.grades_log.academic.like('%'+str(session.search_grades_management)+'%'))).count(db.grades_log.id)))
                    if ((level_tipo=='all') or (level_tipo=='u')):
                        tempRemport1.append(str(db((db.grades_log.project==level_project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='update')&(db.grades_log.roll==level_rol)&(db.grades_log.user_name==userr)&(db.grades_log.academic.like('%'+str(session.search_grades_management)+'%'))).count(db.grades_log.id)))
                    if ((level_tipo=='all') or (level_tipo=='d')):
                        tempRemport1.append(str(db((db.grades_log.project==level_project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='delete')&(db.grades_log.roll==level_rol)&(db.grades_log.user_name==userr)&(db.grades_log.academic.like('%'+str(session.search_grades_management)+'%'))).count(db.grades_log.id)))
                pass
                report.append(tempRemport1)

        #LEVEL 5
        elif request.vars['level']=='5':
            #Head of Level 5
            tempRemport1=[]
            tempRemport1.append(T('Course'))
            tempRemport1.append(level_project.name)
            report.append(tempRemport1)

            tempRemport1=[]
            tempRemport1.append(T('Month'))
            for tempMonth in vecMonth:
                if str(tempMonth[0])==level_month:
                    tempRemport1.append(tempMonth[1])
                    start = datetime.strptime(str(year.yearp) + '-' + str(tempMonth[0]) +'-01', "%Y-%m-%d")
                    if tempMonth[2]==1:
                        end = datetime.strptime(str(year.yearp+1) + '-' + str(tempMonth[2]) +'-01', "%Y-%m-%d")
                    else:
                        end = datetime.strptime(str(year.yearp) + '-' + str(tempMonth[2]) +'-01', "%Y-%m-%d")
                    pass
            report.append(tempRemport1)

            tempRemport1=[]
            tempRemport1.append(T('Role'))
            tempRemport1.append(T('Rol '+str(level_rol)))
            report.append(tempRemport1)

            tempRemport1=[]
            tempRemport1.append(T('User'))
            tempRemport1.append(level_user)
            report.append(tempRemport1)

            tempRemport1=[]
            tempRemport1.append('')
            report.append(tempRemport1)

            tempRemport1=[]
            tempRemport1.append(T('Detail'))
            report.append(tempRemport1)

            temp_vecAllUserRoleMonth=[]
            tempRemport1=[]
            #Body Level 5
            if session.search_grades_management == "" or session.search_grades_management is None:
                if ((level_tipo=='all') or (level_tipo=='i')):
                    temp_vecAllUserRoleMonth.append(db((db.grades_log.project==level_project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='insert')&(db.grades_log.roll==level_rol)&(db.grades_log.user_name==level_user)).select())
                if ((level_tipo=='all') or (level_tipo=='u')):
                    temp_vecAllUserRoleMonth.append(db((db.grades_log.project==level_project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='update')&(db.grades_log.roll==level_rol)&(db.grades_log.user_name==level_user)).select())
                if ((level_tipo=='all') or (level_tipo=='d')):
                    temp_vecAllUserRoleMonth.append(db((db.grades_log.project==level_project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='delete')&(db.grades_log.roll==level_rol)&(db.grades_log.user_name==level_user)).select())
            else:
                if ((level_tipo=='all') or (level_tipo=='i')):
                    temp_vecAllUserRoleMonth.append(db((db.grades_log.project==level_project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='insert')&(db.grades_log.roll==level_rol)&(db.grades_log.user_name==level_user)&(db.grades_log.academic.like('%'+str(session.search_grades_management)+'%'))).select())
                if ((level_tipo=='all') or (level_tipo=='u')):
                    temp_vecAllUserRoleMonth.append(db((db.grades_log.project==level_project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='update')&(db.grades_log.roll==level_rol)&(db.grades_log.user_name==level_user)&(db.grades_log.academic.like('%'+str(session.search_grades_management)+'%'))).select())
                if ((level_tipo=='all') or (level_tipo=='d')):
                    temp_vecAllUserRoleMonth.append(db((db.grades_log.project==level_project.name)&(db.grades_log.yearp==str(year.yearp))&(db.grades_log.period==str(T(year.period.name)))&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='delete')&(db.grades_log.roll==level_rol)&(db.grades_log.user_name==level_user)&(db.grades_log.academic.like('%'+str(session.search_grades_management)+'%'))).select())
            pass
            varTypeHead=0
            for field in temp_vecAllUserRoleMonth:
                for camp in field:
                    if varTypeHead==0:
                        #Heading Level 5
                        tempRemport1=[]
                        tempRemport1.append(T('User resolution'))
                        tempRemport1.append(T('Role resolution'))
                        tempRemport1.append(T('Date of resolution'))
                        tempRemport1.append(T('Operation'))
                        tempRemport1.append(T('Description'))
                        tempRemport1.append(T('Category'))
                        tempRemport1.append(T('Activity'))
                        tempRemport1.append(T('Rol Academic'))
                        tempRemport1.append(T('Before Grade'))
                        tempRemport1.append(T('Grade edited'))
                        report.append(tempRemport1)
                        varTypeHead=1
                    tempRemport1=[]
                    tempRemport1.append(str(camp.user_name))
                    tempRemport1.append(T('Rol '+str(camp.roll)))
                    tempRemport1.append(str(camp.date_log))
                    tempRemport1.append(str(camp.operation_log))
                    tempRemport1.append(str(camp.description))
                    tempRemport1.append(str(camp.category))
                    tempRemport1.append(str(camp.activity))
                    tempRemport1.append(str(camp.academic))
                    tempRemport1.append(str(camp.before_grade))
                    tempRemport1.append(str(camp.after_grade))
                    report.append(tempRemport1)
                pass
            pass
        return dict(filename='ReporteGestionNotas', csvdata=report)
    else:
        session.flash = T('Not valid Action.')
        redirect(URL('activity_control','grades_management'))



#********************************************************
#Management Report Grade levels 1 and 2
@auth.requires_login()
@auth.requires(auth.has_membership('Teacher'))
def grades_management():
    #Export Report to CSV
    if request.vars['list'] =='True':
        redirect(URL('activity_control','grades_management_export'))

    #Export Report Nivel 0
    #redirect(URL('activity_control','request_change_activity',vars=dict(project=request.vars['project'], year=request.vars['year'])))
    if request.vars['list'] =='False':
        if request.vars['level'] =='1':
            redirect(URL('activity_control','grades_management_level_export',vars=dict(level=request.vars['level'])))
        elif request.vars['level'] =='2':
            if request.vars['level_project'] is None or request.vars['level_project']=='':
                redirect(URL('activity_control','grades_management'))
            else:
                redirect(URL('activity_control','grades_management_level_export',vars=dict(level=request.vars['level'],level_project=request.vars['level_project'])))
        else:
            redirect(URL('activity_control','grades_management'))

    import cpfecys
    #Obtain the current period of the system and all the register periods
    period = cpfecys.current_year_period()

    #Check if the user is assigned to the course
    assigantions = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == period.id)).select()
    if assigantions.first() is None:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))

    #Vec with the months of the current period
    vecMonth=[]
    tmpMonth=[]
    if period.period == 1:
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

        if (request.args(0) == 'search'):
            if str(request.vars['querySearch']) == "":
                session.search_grades_management = ""
            else:
                if str(request.vars['querySearch']).isdigit()==True:
                    session.search_grades_management = str(request.vars['querySearch'])
                else:
                    session.search_grades_management = ""
                    session.flash=T('The lookup value is not allowed.')
                    redirect(URL('activity_control','grades_management'))
        else:
            session.search_grades_management = ""

    return dict(year=period, assigantions=assigantions, vecMonth=vecMonth)



#********************************************************
#Management Report Grade levels 3
@auth.requires_login()
@auth.requires(auth.has_membership('Teacher'))
def grades_management_n2():
    import cpfecys
    #Obtain the current period of the system and all the register periods
    period = cpfecys.current_year_period()
    showLevel = True
    project = None
    tipo = None
    month=None
    vecRoleMonth=None
    messageError=''

    #Check if a search exist, verify that they are just numbers
    if session.search_grades_management != "" and session.search_grades_management is not None:
        if str(session.search_grades_management).isdigit()==False:
            session.search_grades_management = ""
            messageError=T('The lookup value is not allowed.')
            showLevel = False

    #Check the correct parameters
    if request.vars['list'] =='False':
        if request.vars['level'] =='3':
            if request.vars['level_project'] is None or request.vars['level_project']=='':
                messageError=T('Error. Unable to export the reporting level for lack of parameters.')
                showLevel = False
            else:
                if request.vars['level_month'] is None or request.vars['level_month']=='':
                    messageError=T('Error. Unable to export the reporting level for lack of parameters.')
                    showLevel = False
                else:
                    if request.vars['level_tipo'] is None or request.vars['level_tipo']=='':
                        messageError=T('Error. Unable to export the reporting level for lack of parameters.')
                        showLevel = False
                    else:
                        redirect(URL('activity_control','grades_management_level_export',vars=dict(level=request.vars['level'],level_project=request.vars['level_project'],level_month=request.vars['level_month'],level_tipo=request.vars['level_tipo'])))
        else:
            messageError=T('Error. Unable to export the reporting level for lack of parameters.')
            showLevel = False

    #Check if the project is correct
    if request.vars['tipo'] is None or request.vars['tipo']=='':
        messageError=T('Error. Unable to show the reporting level for lack of parameters.')
        showLevel = False
    else:
        if str(request.vars['tipo'])!='all' and str(request.vars['tipo'])!='i' and str(request.vars['tipo'])!='u' and str(request.vars['tipo'])!='d':
            messageError=T('Error. Unable to show the reporting level for lack of parameters.')
            showLevel = False
        else:
            tipo = str(request.vars['tipo'])

    #Check if the project is correct
    if request.vars['project'] is None or request.vars['project']=='':
        messageError=T('Error. Unable to show the reporting level for lack of parameters.')
        showLevel = False
    else:
        project = request.vars['project']
        project = db(db.project.id==project).select().first()
        if project is None:
            messageError=T('Action not allowed')
            showLevel = False

    #Check if the user is assigned to the project
    if project is None or tipo is None:
        messageError=T('Error. Unable to show the reporting level for lack of parameters.')
        showLevel = False
    else:
        if auth.has_membership('Teacher'):
            course = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == period.id) & (db.user_project.project==project.id)).select().first()
            if course is None:
                messageError=T('Action not allowed')
                showLevel = False
        else:
            messageError=T('Action not allowed')
            showLevel = False

    #Check if the month is correct
    if showLevel==True:
        if request.vars['month'] is None or request.vars['month']=='':
            messageError=T('Error. Unable to show the reporting level for lack of parameters.')
            showLevel = False
        else:
            if period.period == 1:
                if int(request.vars['month']) >= 1 and int(request.vars['month']) <=5:
                    month=str(request.vars['month'])
                else:
                    messageError=T('Action not allowed')
                    showLevel = False
            else:
                if int(request.vars['month']) >= 6 and int(request.vars['month']) <=12:
                    month=str(request.vars['month'])
                else:
                    messageError=T('Action not allowed')
                    showLevel = False


    #***************************************************************************************************************************************************************************************************************
    #***************************************************************************************************************************************************************************************************************
    #***************************************************************************************************************************************************************************************************************
    #***************************************************************************************************************************************************************************************************************


    #All the parameters are ok, start to build the report level 2
    if showLevel==True:
        from datetime import datetime
        start = datetime.strptime(str(period.yearp) + '-' + month +'-01', "%Y-%m-%d")
        if month=='12':
            end = datetime.strptime(str(period.yearp+1) + '-' + '01-01', "%Y-%m-%d")
        else:
            end = datetime.strptime(str(period.yearp) + '-' + str(int(month)+1) +'-01', "%Y-%m-%d")
        pass
        vecRoleMonth=[]
        roleTemp=[]
        for value in db((db.auth_group.role!='Academic')&(db.auth_group.role!='DSI')).select():
            optionSearch=[]
            optionSearch.append(value.role)
            roleTemp.append(value.role)
            if str(request.vars['tipo'])=='all' or str(request.vars['tipo'])=='i':
                if session.search_grades_management == "" or session.search_grades_management is None:
                    optionSearch.append(str(db((db.grades_log.project==project.name)&(db.grades_log.yearp==str(period.yearp))&(db.grades_log.period==str(T(period.period.name)))&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='insert')&(db.grades_log.roll==value.role)).count(db.grades_log.id)))
                else:
                    optionSearch.append(str(db((db.grades_log.project==project.name)&(db.grades_log.yearp==str(period.yearp))&(db.grades_log.period==str(T(period.period.name)))&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='insert')&(db.grades_log.roll==value.role)&(db.grades_log.academic.like('%'+str(session.search_grades_management)+'%'))).count(db.grades_log.id)))
                pass
            if str(request.vars['tipo'])=='all' or str(request.vars['tipo'])=='u':
                if session.search_grades_management == "" or session.search_grades_management is None:
                    optionSearch.append(str(db((db.grades_log.project==project.name)&(db.grades_log.yearp==str(period.yearp))&(db.grades_log.period==str(T(period.period.name)))&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='update')&(db.grades_log.roll==value.role)).count(db.grades_log.id)))
                else:
                    optionSearch.append(str(db((db.grades_log.project==project.name)&(db.grades_log.yearp==str(period.yearp))&(db.grades_log.period==str(T(period.period.name)))&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='update')&(db.grades_log.roll==value.role)&(db.grades_log.academic.like('%'+str(session.search_grades_management)+'%'))).count(db.grades_log.id)))
                pass
            if str(request.vars['tipo'])=='all' or str(request.vars['tipo'])=='d':
                if session.search_grades_management == "" or session.search_grades_management is None:
                    optionSearch.append(str(db((db.grades_log.project==project.name)&(db.grades_log.yearp==str(period.yearp))&(db.grades_log.period==str(T(period.period.name)))&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='delete')&(db.grades_log.roll==value.role)).count(db.grades_log.id)))
                else:
                    optionSearch.append(str(db((db.grades_log.project==project.name)&(db.grades_log.yearp==str(period.yearp))&(db.grades_log.period==str(T(period.period.name)))&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='delete')&(db.grades_log.roll==value.role)&(db.grades_log.academic.like('%'+str(session.search_grades_management)+'%'))).count(db.grades_log.id)))
                pass
            vecRoleMonth.append(optionSearch)
        #Check if the log has a roll that is not register
        for value in db((db.grades_log.yearp==period.yearp)&(db.grades_log.period==T(period.period.name))&(db.grades_log.project==project.name)&(~db.grades_log.roll.belongs(roleTemp))).select(db.grades_log.roll, distinct=True):
            optionSearch=[]
            optionSearch.append(value.roll)
            if str(request.vars['tipo'])=='all' or str(request.vars['tipo'])=='i':
                if session.search_grades_management == "" or session.search_grades_management is None:
                    optionSearch.append(str(db((db.grades_log.project==project.name)&(db.grades_log.yearp==str(period.yearp))&(db.grades_log.period==str(T(period.period.name)))&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='insert')&(db.grades_log.roll==value.roll)).count(db.grades_log.id)))
                else:
                    optionSearch.append(str(db((db.grades_log.project==project.name)&(db.grades_log.yearp==str(period.yearp))&(db.grades_log.period==str(T(period.period.name)))&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='insert')&(db.grades_log.roll==value.roll)&(db.grades_log.academic.like('%'+str(session.search_grades_management)+'%'))).count(db.grades_log.id)))
                pass
            if str(request.vars['tipo'])=='all' or str(request.vars['tipo'])=='u':
                if session.search_grades_management == "" or session.search_grades_management is None:
                    optionSearch.append(str(db((db.grades_log.project==project.name)&(db.grades_log.yearp==str(period.yearp))&(db.grades_log.period==str(T(period.period.name)))&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='insert')&(db.grades_log.roll==value.roll)).count(db.grades_log.id)))
                else:
                    optionSearch.append(str(db((db.grades_log.project==project.name)&(db.grades_log.yearp==str(period.yearp))&(db.grades_log.period==str(T(period.period.name)))&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='insert')&(db.grades_log.roll==value.roll)&(db.grades_log.academic.like('%'+str(session.search_grades_management)+'%'))).count(db.grades_log.id)))
                pass
            if str(request.vars['tipo'])=='all' or str(request.vars['tipo'])=='d':
                if session.search_grades_management == "" or session.search_grades_management is None:
                    optionSearch.append(str(db((db.grades_log.project==project.name)&(db.grades_log.yearp==str(period.yearp))&(db.grades_log.period==str(T(period.period.name)))&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='insert')&(db.grades_log.roll==value.roll)).count(db.grades_log.id)))
                else:
                    optionSearch.append(str(db((db.grades_log.project==project.name)&(db.grades_log.yearp==str(period.yearp))&(db.grades_log.period==str(T(period.period.name)))&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='insert')&(db.grades_log.roll==value.roll)&(db.grades_log.academic.like('%'+str(session.search_grades_management)+'%'))).count(db.grades_log.id)))
                pass
            vecRoleMonth.append(optionSearch)
    return dict(showLevel=showLevel, project=project, tipo=tipo, month=month, vecRoleMonth=vecRoleMonth, messageError=messageError)



#********************************************************
#Management Report Grade levels 4
@auth.requires_login()
@auth.requires(auth.has_membership('Teacher'))
def grades_management_n3():
    import cpfecys
    #Obtain the current period of the system and all the register periods
    period = cpfecys.current_year_period()
    showLevel = True
    project = None
    tipo = None
    month=None
    roll=None
    vecUserRoleMonth=None
    messageError=''

    #Check if a search exist, verify that they are just numbers
    if session.search_grades_management != "" and session.search_grades_management is not None:
        if str(session.search_grades_management).isdigit()==False:
            session.search_grades_management = ""
            messageError=T('The lookup value is not allowed.')
            showLevel = False

    #Check the correct parameters
    if request.vars['list'] =='False':
        if request.vars['level'] =='4':
            if request.vars['level_project'] is None or request.vars['level_project']=='':
                messageError=T('Error. Unable to export the reporting level for lack of parameters.')
                showLevel = False
            else:
                if request.vars['level_month'] is None or request.vars['level_month']=='':
                    messageError=T('Error. Unable to export the reporting level for lack of parameters.')
                    showLevel = False
                else:
                    if request.vars['level_tipo'] is None or request.vars['level_tipo']=='':
                        messageError=T('Error. Unable to export the reporting level for lack of parameters.')
                        showLevel = False
                    else:
                        if request.vars['level_rol'] is None or request.vars['level_rol']=='':
                            messageError=T('Error. Unable to export the reporting level for lack of parameters.')
                            showLevel = False
                        else:
                            redirect(URL('activity_control','grades_management_level_export',vars=dict(level=request.vars['level'],level_project=request.vars['level_project'],level_month=request.vars['level_month'],level_tipo=request.vars['level_tipo'],level_rol=request.vars['level_rol'])))
        else:
            messageError=T('Error. Unable to export the reporting level for lack of parameters.')
            showLevel = False

    #Check if the project is correct
    if request.vars['tipo'] is None or request.vars['tipo']=='':
        messageError=T('Error. Unable to show the reporting level for lack of parameters.')
        showLevel = False
    else:
        if str(request.vars['tipo'])!='all' and str(request.vars['tipo'])!='i' and str(request.vars['tipo'])!='u' and str(request.vars['tipo'])!='d':
            messageError=T('Error. Unable to show the reporting level for lack of parameters.')
            showLevel = False
        else:
            tipo = str(request.vars['tipo'])


    #Check if the project is correct
    if request.vars['project'] is None or request.vars['project']=='':
        messageError=T('Error. Unable to show the reporting level for lack of parameters.')
        showLevel = False
    else:
        project = request.vars['project']
        project = db(db.project.id==project).select().first()
        if project is None:
            messageError=T('Action not allowed')
            showLevel = False


    #Check if the user is assigned to the project
    if project is None or tipo is None:
        messageError=T('Error. Unable to show the reporting level for lack of parameters.')
        showLevel = False
    else:
        if auth.has_membership('Teacher'):
            course = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == period.id) & (db.user_project.project==project.id)).select().first()
            if course is None:
                messageError=T('Action not allowed')
                showLevel = False
        else:
            messageError=T('Action not allowed')
            showLevel = False


    #Check if the month is correct
    if showLevel==True:
        if request.vars['month'] is None or request.vars['month']=='':
            messageError=T('Error. Unable to show the reporting level for lack of parameters.')
            showLevel = False
        else:
            if period.period == 1:
                if int(request.vars['month']) >= 1 and int(request.vars['month']) <=5:
                    month=str(request.vars['month'])
                else:
                    messageError=T('Action not allowed')
                    showLevel = False
            else:
                if int(request.vars['month']) >= 6 and int(request.vars['month']) <=12:
                    month=str(request.vars['month'])
                else:
                    messageError=T('Action not allowed')
                    showLevel = False


    #Check if the roll is correct
    if showLevel==True:
        if request.vars['roll'] is None or request.vars['roll']=='':
            messageError=T('Error. Unable to show the reporting level for lack of parameters.')
            showLevel = False
        else:
            value = db(db.auth_group.role==str(request.vars['roll'])).select().first()
            if value is None:
                #Check if the log has a roll that is not register
                value = db((db.grades_log.yearp==period.yearp)&(db.grades_log.period==T(period.period.name))&(db.grades_log.project==project.name)&(db.grades_log.roll==str(request.vars['roll']))).select(db.grades_log.roll, distinct=True).first()
                if value is None:
                    messageError=T('Action not allowed')
                    showLevel = False
                else:
                    roll=str(value.roll)
            else:
                roll=str(value.role)


    #***************************************************************************************************************************************************************************************************************
    #***************************************************************************************************************************************************************************************************************
    #***************************************************************************************************************************************************************************************************************
    #***************************************************************************************************************************************************************************************************************


    #All the parameters are ok, start to build the report level 2
    if showLevel==True:
        from datetime import datetime
        start = datetime.strptime(str(period.yearp) + '-' + month +'-01', "%Y-%m-%d")
        if month=='12':
            end = datetime.strptime(str(period.yearp+1) + '-' + '01-01', "%Y-%m-%d")
        else:
            end = datetime.strptime(str(period.yearp) + '-' + str(int(month)+1) +'-01', "%Y-%m-%d")
        pass

        #Users in the actual registers
        tempUsers=[]
        tempUsers2=[]
        registerRol = db(db.auth_group.role==roll).select().first()
        if registerRol is not None:
            if ((roll=='Super-Administrator') or (roll=='Ecys-Administrator')):
                for value in db((db.auth_membership.group_id==registerRol.id)).select(db.auth_membership.user_id, distinct=True):
                    tempUsers.append(value.user_id.username)
            else:
                for value in db((db.auth_membership.group_id==registerRol.id)).select(db.auth_membership.user_id, distinct=True):
                    tempUsers2.append(value.user_id)
                for value in db((db.user_project.period==period.id)&(db.user_project.project==project.id)&(db.user_project.assigned_user.belongs(tempUsers2))).select(db.user_project.assigned_user, distinct=True):
                    tempUsers.append(value.assigned_user.username)
            pass
        pass
        #Check if the log has an username that is not register
        for value in db((db.grades_log.yearp==period.yearp)&(db.grades_log.period==T(period.period.name))&(db.grades_log.project==project.name)&(db.grades_log.roll==roll)&(~db.grades_log.user_name.belongs(tempUsers))).select(db.grades_log.user_name, distinct=True):
            tempUsers.append(value.user_name)
        
        vecUserRoleMonth=[]
        for value in tempUsers:
            optionSearch=[]
            optionSearch.append(value)
            if str(request.vars['tipo'])=='all' or str(request.vars['tipo'])=='i':
                if session.search_grades_management == "" or session.search_grades_management is None:
                    optionSearch.append(str(db((db.grades_log.project==project.name)&(db.grades_log.yearp==str(period.yearp))&(db.grades_log.period==str(T(period.period.name)))&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='insert')&(db.grades_log.roll==roll)&(db.grades_log.user_name==value)).count(db.grades_log.id)))
                else:
                    optionSearch.append(str(db((db.grades_log.project==project.name)&(db.grades_log.yearp==str(period.yearp))&(db.grades_log.period==str(T(period.period.name)))&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='insert')&(db.grades_log.roll==roll)&(db.grades_log.user_name==value)&(db.grades_log.academic.like('%'+str(session.search_grades_management)+'%'))).count(db.grades_log.id)))
                pass
            if str(request.vars['tipo'])=='all' or str(request.vars['tipo'])=='u':
                if session.search_grades_management == "" or session.search_grades_management is None:
                    optionSearch.append(str(db((db.grades_log.project==project.name)&(db.grades_log.yearp==str(period.yearp))&(db.grades_log.period==str(T(period.period.name)))&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='update')&(db.grades_log.roll==roll)&(db.grades_log.user_name==value)).count(db.grades_log.id)))
                else:
                    optionSearch.append(str(db((db.grades_log.project==project.name)&(db.grades_log.yearp==str(period.yearp))&(db.grades_log.period==str(T(period.period.name)))&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='update')&(db.grades_log.roll==roll)&(db.grades_log.user_name==value)&(db.grades_log.academic.like('%'+str(session.search_grades_management)+'%'))).count(db.grades_log.id)))
                pass
            if str(request.vars['tipo'])=='all' or str(request.vars['tipo'])=='d':
                if session.search_grades_management == "" or session.search_grades_management is None:
                    optionSearch.append(str(db((db.grades_log.project==project.name)&(db.grades_log.yearp==str(period.yearp))&(db.grades_log.period==str(T(period.period.name)))&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='delete')&(db.grades_log.roll==roll)&(db.grades_log.user_name==value)).count(db.grades_log.id)))
                else:
                    optionSearch.append(str(db((db.grades_log.project==project.name)&(db.grades_log.yearp==str(period.yearp))&(db.grades_log.period==str(T(period.period.name)))&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='delete')&(db.grades_log.roll==roll)&(db.grades_log.user_name==value)&(db.grades_log.academic.like('%'+str(session.search_grades_management)+'%'))).count(db.grades_log.id)))
                pass
            vecUserRoleMonth.append(optionSearch)
    return dict(showLevel=showLevel, project=project, tipo=tipo, month=month, vecUserRoleMonth=vecUserRoleMonth, roll=roll, messageError=messageError)



#********************************************************
#Management Report Grade levels 5
@auth.requires_login()
@auth.requires(auth.has_membership('Teacher'))
def grades_management_n4():
    import cpfecys
    #Obtain the current period of the system and all the register periods
    period = cpfecys.current_year_period()
    showLevel = True
    project = None
    tipo = None
    month=None
    roll=None
    userr=None
    vecAllUserRoleMonth=None
    messageError=''

    #Check if a search exist, verify that they are just numbers
    if session.search_grades_management != "" and session.search_grades_management is not None:
        if str(session.search_grades_management).isdigit()==False:
            session.search_grades_management = ""
            messageError=T('The lookup value is not allowed.')
            showLevel = False

    #Check the correct parameters
    if request.vars['list'] =='False':
        if request.vars['level'] =='5':
            if request.vars['level_project'] is None or request.vars['level_project']=='':
                messageError=T('Error. Unable to export the reporting level for lack of parameters.')
                showLevel = False
            else:
                if request.vars['level_month'] is None or request.vars['level_month']=='':
                    messageError=T('Error. Unable to export the reporting level for lack of parameters.')
                    showLevel = False
                else:
                    if request.vars['level_tipo'] is None or request.vars['level_tipo']=='':
                        messageError=T('Error. Unable to export the reporting level for lack of parameters.')
                        showLevel = False
                    else:
                        if request.vars['level_rol'] is None or request.vars['level_rol']=='':
                            messageError=T('Error. Unable to export the reporting level for lack of parameters.')
                            showLevel = False
                        else:
                            if request.vars['level_user'] is None or request.vars['level_user']=='':
                                messageError=T('Error. Unable to export the reporting level for lack of parameters.')
                                showLevel = False
                            else:
                                redirect(URL('activity_control','grades_management_level_export',vars=dict(level=request.vars['level'],level_project=request.vars['level_project'],level_month=request.vars['level_month'],level_tipo=request.vars['level_tipo'],level_rol=request.vars['level_rol'],level_user=request.vars['level_user'])))
        else:
            messageError=T('Error. Unable to export the reporting level for lack of parameters.')
            showLevel = False

    #Check if the project is correct
    if request.vars['tipo'] is None or request.vars['tipo']=='':
        messageError=T('Error. Unable to export the reporting level for lack of parameters.')
        showLevel = False
    else:
        if str(request.vars['tipo'])!='all' and str(request.vars['tipo'])!='i' and str(request.vars['tipo'])!='u' and str(request.vars['tipo'])!='d':
            messageError=T('Error. Unable to export the reporting level for lack of parameters.')
            showLevel = False
        else:
            tipo = str(request.vars['tipo'])


    #Check if the project is correct
    if request.vars['project'] is None or request.vars['project']=='':
        messageError=T('Error. Unable to export the reporting level for lack of parameters.')
        showLevel = False
    else:
        project = request.vars['project']
        project = db(db.project.id==project).select().first()
        if project is None:
            messageError=T('Action not allowed')
            showLevel = False


    #Check if the user is assigned to the project
    if project is None or tipo is None:
        messageError=T('Error. Unable to export the reporting level for lack of parameters.')
        showLevel = False
    else:
        if auth.has_membership('Teacher'):
            course = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == period.id) & (db.user_project.project==project.id)).select().first()
            if course is None:
                messageError=T('Action not allowed')
                showLevel = False
        else:
            messageError=T('Action not allowed')
            showLevel = False


    #Check if the month is correct
    if showLevel==True:
        if request.vars['month'] is None or request.vars['month']=='':
            messageError=T('Error. Unable to export the reporting level for lack of parameters.')
            showLevel = False
        else:
            if period.period == 1:
                if int(request.vars['month']) >= 1 and int(request.vars['month']) <=5:
                    month=str(request.vars['month'])
                else:
                    messageError=T('Action not allowed')
                    showLevel = False
            else:
                if int(request.vars['month']) >= 6 and int(request.vars['month']) <=12:
                    month=str(request.vars['month'])
                else:
                    messageError=T('Action not allowed')
                    showLevel = False


    #Check if the roll is correct
    if showLevel==True:
        if request.vars['roll'] is None or request.vars['roll']=='':
            messageError=T('Error. Unable to export the reporting level for lack of parameters.')
            showLevel = False
        else:
            value = db(db.auth_group.role==str(request.vars['roll'])).select().first()
            if value is None:
                #Check if the log has a roll that is not register
                value = db((db.grades_log.yearp==period.yearp)&(db.grades_log.period==T(period.period.name))&(db.grades_log.project==project.name)&(db.grades_log.roll==str(request.vars['roll']))).select(db.grades_log.roll, distinct=True).first()
                if value is None:
                    messageError=T('Action not allowed')
                    showLevel = False
                else:
                    roll=value
            else:
                roll=value.role

    #Check if the user is correct
    if showLevel==True:
        if request.vars['userr'] is None or request.vars['userr']=='':
            messageError=T('Error. Unable to export the reporting level for lack of parameters.')
            showLevel = False
        else:
            flagCheck = False
            #User Temp of auth_user where the username is equal
            userr = db(db.auth_user.username==str(request.vars['userr'])).select().first()
            if ((roll=='Super-Administrator') or (roll=='Ecys-Administrator')):
                if userr is not None:
                    #Check if the user has the rol specific
                    userrT = db(db.auth_membership.user_id==userr.id).select()
                    for tempUserCheck in userrT:
                        if tempUserCheck.group_id.role==roll:
                            flagCheck = True
            else:
                if userr is not None:
                    #Check if the user has the rol specific
                    userrT = db(db.auth_membership.user_id==userr.id).select()
                    for tempUserCheck in userrT:
                        if tempUserCheck.group_id.role==roll:
                            if db((db.user_project.period==period.id)&(db.user_project.project==project.id)&(db.user_project.assigned_user==userr.id)).select().first() is not None:
                                flagCheck = True

            if flagCheck==False:
                #Check if the log has a roll that is not register
                userr = db((db.grades_log.yearp==period.yearp)&(db.grades_log.period==T(period.period.name))&(db.grades_log.project==project.name)&(db.grades_log.roll==roll.role)&(db.grades_log.user_name==str(request.vars['userr']))).select().first()
                if value is None:
                    messageError=T('Action not allowed')
                    showLevel = False
                else:
                    userr=userr.user_name
            else:
                userr=userr.username


    #***************************************************************************************************************************************************************************************************************
    #***************************************************************************************************************************************************************************************************************
    #***************************************************************************************************************************************************************************************************************
    #***************************************************************************************************************************************************************************************************************


    #All the parameters are ok, start to build the report level 2
    if showLevel==True:
        from datetime import datetime
        start = datetime.strptime(str(period.yearp) + '-' + month +'-01', "%Y-%m-%d")
        if month=='12':
            end = datetime.strptime(str(period.yearp+1) + '-' + '01-01', "%Y-%m-%d")
        else:
            end = datetime.strptime(str(period.yearp) + '-' + str(int(month)+1) +'-01', "%Y-%m-%d")
        pass
        
        vecAllUserRoleMonth=[]
        if str(request.vars['tipo'])=='all' or str(request.vars['tipo'])=='i':
            if session.search_grades_management == "" or session.search_grades_management is None:
                vecAllUserRoleMonth.append(db((db.grades_log.project==project.name)&(db.grades_log.yearp==str(period.yearp))&(db.grades_log.period==str(T(period.period.name)))&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='insert')&(db.grades_log.roll==roll)&(db.grades_log.user_name==userr)).select())
            else:
                vecAllUserRoleMonth.append(db((db.grades_log.project==project.name)&(db.grades_log.yearp==str(period.yearp))&(db.grades_log.period==str(T(period.period.name)))&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='insert')&(db.grades_log.roll==roll)&(db.grades_log.user_name==userr)&(db.grades_log.academic.like('%'+str(session.search_grades_management)+'%'))).select())
            pass
        if str(request.vars['tipo'])=='all' or str(request.vars['tipo'])=='u':
            if session.search_grades_management == "" or session.search_grades_management is None:
                vecAllUserRoleMonth.append(db((db.grades_log.project==project.name)&(db.grades_log.yearp==str(period.yearp))&(db.grades_log.period==str(T(period.period.name)))&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='update')&(db.grades_log.roll==roll)&(db.grades_log.user_name==userr)).select())
            else:
                vecAllUserRoleMonth.append(db((db.grades_log.project==project.name)&(db.grades_log.yearp==str(period.yearp))&(db.grades_log.period==str(T(period.period.name)))&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='update')&(db.grades_log.roll==roll)&(db.grades_log.user_name==userr)&(db.grades_log.academic.like('%'+str(session.search_grades_management)+'%'))).select())
            pass
        if str(request.vars['tipo'])=='all' or str(request.vars['tipo'])=='d':
            if session.search_grades_management == "" or session.search_grades_management is None:
                vecAllUserRoleMonth.append(db((db.grades_log.project==project.name)&(db.grades_log.yearp==str(period.yearp))&(db.grades_log.period==str(T(period.period.name)))&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='delete')&(db.grades_log.roll==roll)&(db.grades_log.user_name==userr)).select())
            else:
                vecAllUserRoleMonth.append(db((db.grades_log.project==project.name)&(db.grades_log.yearp==str(period.yearp))&(db.grades_log.period==str(T(period.period.name)))&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='delete')&(db.grades_log.roll==roll)&(db.grades_log.user_name==userr)&(db.grades_log.academic.like('%'+str(session.search_grades_management)+'%'))).select())
            pass
    return dict(showLevel=showLevel, project=project, tipo=tipo, month=month, vecAllUserRoleMonth=vecAllUserRoleMonth, roll=roll, userr=userr, messageError=messageError)



########################################################################################################################################################################################################################################################################
########################################################################################################################################################################################################################################################################
########################################################################################################################################################################################################################################################################
########################################################################################################################################################################################################################################################################
#####################################################Management Report Revalidations laboratory#####################################################
#********************************************************
#Export full management reporting laboratory revalidation
@auth.requires_login()
@auth.requires(auth.has_membership('Teacher'))
def validate_laboratory_management_export():
    #Vars of the report
    report=[]
    tempRemport1=[]
    tempRemport2=[]
    tempRemport3=[]
    tempRemport4=[]
    tempRemport5=[]
    #Obtain the current period of the system and all the register periods
    import cpfecys
    from datetime import datetime
    year = cpfecys.current_year_period()

    #Check if the user is assigned to the course
    assigantions = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == year.id)).select()
    if assigantions.first() is None:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))

    #Check if a search exist, verify that they are just numbers
    if session.search_validate_laboratory_management != "" and session.search_validate_laboratory_management is not None:
        if str(session.search_validate_laboratory_management).isdigit()==False:
            session.search_validate_laboratory_management = ""
            session.flash=T('The lookup value is not allowed.')
            redirect(URL('activity_control','grades_management'))

    #Vec with the months of the current period
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

    #report.append()

    #Report heading
    tempRemport1=[]
    tempRemport1.append('Reporte de Gestión de Revalidación de Laboratorio')
    report.append(tempRemport1)
    tempRemport1=[]
    tempRemport1.append(T(year.period.name)+' '+str(year.yearp))
    report.append(tempRemport1)

    #LEVEL 1
    #Heading Level 1
    tempRemport1=[]
    tempRemport1.append(T('Course'))
    tempRemport1.append(T('Total inserted'))
    tempRemport1.append(T('Total modified'))
    tempRemport1.append(T('Total out'))
    report.append(tempRemport1)
    #Body Level 1
    for assigantion in assigantions:
        tempRemport1=[]
        tempRemport1.append(assigantion.project.name)
        if session.search_validate_laboratory_management == "" or session.search_validate_laboratory_management is None:
            tempRemport1.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==True)).count(db.validate_laboratory_log.id)))
            tempRemport1.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==True)).count(db.validate_laboratory_log.id)))
            tempRemport1.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==True)).count(db.validate_laboratory_log.id)))
        else:
            tempRemport1.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(session.search_validate_laboratory_management)+'%'))).count(db.validate_laboratory_log.id)))
            tempRemport1.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(session.search_validate_laboratory_management)+'%'))).count(db.validate_laboratory_log.id)))
            tempRemport1.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(session.search_validate_laboratory_management)+'%'))).count(db.validate_laboratory_log.id)))
        pass
        report.append(tempRemport1)

        #LEVEL 2
        #Heading Level 2
        tempRemport2=[]
        tempRemport2.append('')
        tempRemport2.append(T('Month'))
        tempRemport2.append(T('Total inserted'))
        tempRemport2.append(T('Total modified'))
        tempRemport2.append(T('Total out'))
        report.append(tempRemport2)
        #Body Level 2
        for month in vecMonth:
            tempRemport2=[]
            tempRemport2.append('')
            start = datetime.strptime(str(year.yearp) + '-' + str(month[0]) +'-01', "%Y-%m-%d")
            if month[2]==1:
                end = datetime.strptime(str(year.yearp+1) + '-' + str(month[2]) +'-01', "%Y-%m-%d")
            else:
                end = datetime.strptime(str(year.yearp) + '-' + str(month[2]) +'-01', "%Y-%m-%d")
            pass
            tempRemport2.append(month[1])
            if session.search_validate_laboratory_management == "" or session.search_validate_laboratory_management is None:
                tempRemport2.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.validation_type==True)).count(db.validate_laboratory_log.id)))
                tempRemport2.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.validation_type==True)).count(db.validate_laboratory_log.id)))
                tempRemport2.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.validation_type==True)).count(db.validate_laboratory_log.id)))
            else:
                tempRemport2.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(session.search_validate_laboratory_management)+'%'))).count(db.validate_laboratory_log.id)))
                tempRemport2.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(session.search_validate_laboratory_management)+'%'))).count(db.validate_laboratory_log.id)))
                tempRemport2.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(session.search_validate_laboratory_management)+'%'))).count(db.validate_laboratory_log.id)))
            pass
            report.append(tempRemport2)

            #LEVEL 3
            #Heading Level 3
            tempRemport3=[]
            tempRole = []
            tempRemport3.append('')
            tempRemport3.append('')
            tempRemport3.append(T('Role'))
            tempRemport3.append(T('Total inserted'))
            tempRemport3.append(T('Total modified'))
            tempRemport3.append(T('Total out'))
            report.append(tempRemport3)
            #Body Level 3
            for tempR in db((db.auth_group.role!='Academic')&(db.auth_group.role!='DSI')).select():
                tempRole.append(tempR.role)
            for tempR in db((db.validate_laboratory_log.yearp==year.yearp)&(db.validate_laboratory_log.period==T(year.period.name))&(db.validate_laboratory_log.project==assigantion.project.name)&(~db.validate_laboratory_log.roll.belongs(tempRole))).select(db.validate_laboratory_log.roll, distinct=True):
                tempRole.append(tempR.roll)
            for roll in tempRole:
                tempRemport3=[]
                tempRemport3.append('')
                tempRemport3.append('')
                if roll=='Student':
                    tempRemport3.append(T('Rol Student'))
                else:
                    tempRemport3.append(T(roll))
                pass
                if session.search_validate_laboratory_management == "" or session.search_validate_laboratory_management is None:
                    tempRemport3.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.validation_type==True)).count(db.validate_laboratory_log.id)))
                    tempRemport3.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.validation_type==True)).count(db.validate_laboratory_log.id)))
                    tempRemport3.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.validation_type==True)).count(db.validate_laboratory_log.id)))
                else:
                    tempRemport3.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(session.search_validate_laboratory_management)+'%'))).count(db.validate_laboratory_log.id)))
                    tempRemport3.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(session.search_validate_laboratory_management)+'%'))).count(db.validate_laboratory_log.id)))
                    tempRemport3.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(session.search_validate_laboratory_management)+'%'))).count(db.validate_laboratory_log.id)))
                pass
                report.append(tempRemport3)

                #LEVEL 4
                #Heading Level 4
                tempRemport4=[]
                tempUsers=[]
                tempRemport4.append('')
                tempRemport4.append('')
                tempRemport4.append('')
                tempRemport4.append(T('User'))
                tempRemport4.append(T('Total inserted'))
                tempRemport4.append(T('Total modified'))
                tempRemport4.append(T('Total out'))
                report.append(tempRemport4)
                #Body Level 4
                tempUsers2=[]
                registerRol = db(db.auth_group.role==roll).select().first()
                if ((roll=='Super-Administrator') or (roll=='Ecys-Administrator')):
                    for valueU in db((db.auth_membership.group_id==registerRol.id)).select(db.auth_membership.user_id, distinct=True):
                        tempUsers.append(valueU.user_id.username)
                else:
                    for valueU in db((db.auth_membership.group_id==registerRol.id)).select(db.auth_membership.user_id, distinct=True):
                        tempUsers2.append(valueU.user_id)
                    for valueU in db((db.user_project.period==year.id)&(db.user_project.project==assigantion.project)&(db.user_project.assigned_user.belongs(tempUsers2))).select(db.user_project.assigned_user, distinct=True):
                        tempUsers.append(valueU.assigned_user.username)
                pass
                for valueU in db((db.validate_laboratory_log.yearp==year.yearp)&(db.validate_laboratory_log.period==T(year.period.name))&(db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.roll==roll)&(~db.validate_laboratory_log.user_name.belongs(tempUsers))).select(db.validate_laboratory_log.user_name, distinct=True):
                    tempUsers.append(valueU.user_name)
                for userr in tempUsers:
                    tempRemport4=[]
                    tempRemport4.append('')
                    tempRemport4.append('')
                    tempRemport4.append('')
                    tempRemport4.append(userr)
                    if session.search_validate_laboratory_management == "" or session.search_validate_laboratory_management is None:
                        tempRemport4.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==userr)&(db.validate_laboratory_log.validation_type==True)).count(db.validate_laboratory_log.id)))
                        tempRemport4.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==userr)&(db.validate_laboratory_log.validation_type==True)).count(db.validate_laboratory_log.id)))
                        tempRemport4.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==userr)&(db.validate_laboratory_log.validation_type==True)).count(db.validate_laboratory_log.id)))
                    else:
                        tempRemport4.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==userr)&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(session.search_validate_laboratory_management)+'%'))).count(db.validate_laboratory_log.id)))
                        tempRemport4.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==userr)&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(session.search_validate_laboratory_management)+'%'))).count(db.validate_laboratory_log.id)))
                        tempRemport4.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==userr)&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(session.search_validate_laboratory_management)+'%'))).count(db.validate_laboratory_log.id)))
                    pass
                    report.append(tempRemport4)

                    #LEVEL 5
                    temp_vecAllUserRoleMonth=[]
                    tempRemport5=[]
                    #Body Level 5
                    if session.search_validate_laboratory_management == "" or session.search_validate_laboratory_management is None:
                        temp_vecAllUserRoleMonth.append(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==userr)&(db.validate_laboratory_log.validation_type==True)).select())
                        temp_vecAllUserRoleMonth.append(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==userr)&(db.validate_laboratory_log.validation_type==True)).select())
                        temp_vecAllUserRoleMonth.append(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==userr)&(db.validate_laboratory_log.validation_type==True)).select())
                    else:
                        temp_vecAllUserRoleMonth.append(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==userr)&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(session.search_validate_laboratory_management)+'%'))).select())
                        temp_vecAllUserRoleMonth.append(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==userr)&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(session.search_validate_laboratory_management)+'%'))).select())
                        temp_vecAllUserRoleMonth.append(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==userr)&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(session.search_validate_laboratory_management)+'%'))).select())
                    pass
                    varTypeHead=0
                    for field in temp_vecAllUserRoleMonth:
                        for camp in field:
                            if varTypeHead==0:
                                #Heading Level 5
                                tempRemport5=[]
                                tempRemport5.append('')
                                tempRemport5.append('')
                                tempRemport5.append('')
                                tempRemport5.append('')
                                tempRemport5.append(T('User resolution'))
                                tempRemport5.append(T('Role resolution'))
                                tempRemport5.append(T('Date of resolution'))
                                tempRemport5.append(T('Operation'))
                                tempRemport5.append(T('Description'))
                                tempRemport5.append(T('Rol Academic'))
                                tempRemport5.append(T('Before Grade'))
                                tempRemport5.append(T('Grade edited'))
                                report.append(tempRemport5)
                                varTypeHead=1
                            tempRemport5=[]
                            tempRemport5.append('')
                            tempRemport5.append('')
                            tempRemport5.append('')
                            tempRemport5.append('')
                            tempRemport5.append(str(camp.user_name))
                            tempRemport5.append(T('Rol '+str(camp.roll)))
                            tempRemport5.append(str(camp.date_log))
                            tempRemport5.append(str(camp.operation_log))
                            tempRemport5.append(str(camp.description))
                            tempRemport5.append(str(camp.academic))
                            tempRemport5.append(str(camp.before_grade))
                            tempRemport5.append(str(camp.after_grade))
                            report.append(tempRemport5)
                        pass
                    pass
                    #End Level 5
                pass
                #End Level 4
                report.append('')
                report.append('')
            pass
            #End Level 3
            report.append('')
            report.append('')
            report.append('')
            report.append('')
        pass
        #End Level 2
        report.append('')
        report.append('')
        report.append('')
        report.append('')
        report.append('')
        report.append('')
    pass
    #End Level 1

    return dict(filename='ReporteGestionRevalidaciones', csvdata=report)



#********************************************************
#Export management reporting laboratory revalidation
@auth.requires_login()
@auth.requires(auth.has_membership('Teacher'))
def validate_laboratory_management_level_export():
    #Vars of the report
    createReport = True
    report=[]
    tempRemport1=[]
    #Obtain the current period of the system and all the register periods
    import cpfecys
    from datetime import datetime
    year = cpfecys.current_year_period()

    #Check if the user is assigned to the course
    assigantions = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == year.id)).select()
    if assigantions.first() is None:
        createReport=False

    #Check if a search exist, verify that they are just numbers
    if session.search_validate_laboratory_management != "" and session.search_validate_laboratory_management is not None:
        if str(session.search_validate_laboratory_management).isdigit()==False:
            session.search_validate_laboratory_management = ""
            createReport=False

    #Vec with the months of the current period
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

    #Check the parameters
    if request.vars['level']=='1' or request.vars['level']=='2' or request.vars['level']=='3' or request.vars['level']=='4' or request.vars['level']=='5':
        if int(request.vars['level']) > 1 and createReport==True:
            #Check if the project is correct
            if request.vars['level_project'] is None or request.vars['level_project']=='':
                createReport=False
            else:
                level_project = request.vars['level_project']
                level_project = db(db.project.id==level_project).select().first()
                if level_project is None:
                    createReport=False
                else:
                    exportReport=False
                    for assigantion in assigantions:
                        if assigantion.project==level_project.id:
                            exportReport=True
                    if exportReport==False:
                        createReport=False
        pass

        if int(request.vars['level']) > 2 and createReport==True:
            #Check if the Month is correct
            if request.vars['level_month'] is None or request.vars['level_month']=='':
                createReport=False
            else:
                if year.period == 1:
                    try:
                        if int(request.vars['level_month']) >= 1 and int(request.vars['level_month']) <=5:
                            level_month=str(request.vars['level_month'])
                        else:
                            createReport=False
                    except:
                        createReport=False
                else:
                    try:
                        if int(request.vars['level_month']) >= 6 and int(request.vars['level_month']) <=12:
                            level_month=str(request.vars['level_month'])
                        else:
                            createReport=False
                    except:
                        createReport=False
                
            #Check if the type is correct
            if request.vars['level_tipo'] is None or request.vars['level_tipo']=='':
                createReport=False
            else:
                if str(request.vars['level_tipo'])!='all' and str(request.vars['level_tipo'])!='i' and str(request.vars['level_tipo'])!='u' and str(request.vars['level_tipo'])!='d':
                    createReport=False
                else:
                    level_tipo = str(request.vars['level_tipo'])
        pass

        if int(request.vars['level']) > 3 and createReport==True:
            if request.vars['level_rol'] is None or request.vars['level_rol']=='':
                createReport=False
            else:
                value = db(db.auth_group.role==str(request.vars['level_rol'])).select().first()
                if value is None:
                    #Check if the log has a roll that is not register
                    value = db((db.validate_laboratory_log.yearp==year.yearp)&(db.validate_laboratory_log.period==T(year.period.name))&(db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.roll==str(request.vars['level_rol']))).select(db.validate_laboratory_log.roll, distinct=True).first()
                    if value is None:
                        createReport=False
                    else:
                        level_rol=str(value.roll)
                else:
                    level_rol=str(value.role)
        pass

        if int(request.vars['level']) > 4 and createReport==True:
            if request.vars['level_user'] is None or request.vars['level_user']=='':
                createReport=False
            else:
                flagCheck = False
                #User Temp of auth_user where the username is equal
                userr = db(db.auth_user.username==str(request.vars['level_user'])).select().first()
                if ((level_rol=='Super-Administrator') or (level_rol=='Ecys-Administrator')):
                    if userr is not None:
                        #Check if the user has the rol specific
                        userrT = db(db.auth_membership.user_id==userr.id).select()
                        for tempUserCheck in userrT:
                            if tempUserCheck.group_id.role==level_rol:
                                flagCheck = True
                else:
                    if userr is not None:
                        #Check if the user has the rol specific
                        userrT = db(db.auth_membership.user_id==userr.id).select()
                        for tempUserCheck in userrT:
                            if tempUserCheck.group_id.role==level_rol:
                                if db((db.user_project.period==year.id)&(db.user_project.project==level_project.id)&(db.user_project.assigned_user==userr.id)).select().first() is not None:
                                    flagCheck = True

                if flagCheck==False:
                    #Check if the log has a roll that is not register
                    userr = db((db.validate_laboratory_log.yearp==year.yearp)&(db.validate_laboratory_log.period==T(year.period.name))&(db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.roll==level_rol)&(db.validate_laboratory_log.user_name==str(request.vars['userr']))).select().first()
                    if value is None:
                        createReport=False
                    else:
                        level_user=userr.user_name
                else:
                    level_user=userr.username
        pass
    else:
        createReport=False

    #MAKE REPORT
    if createReport==True:
        #Report heading
        tempRemport1=[]
        tempRemport1.append('Reporte de Gestión de Revalidación de Laboratorio')
        report.append(tempRemport1)
        tempRemport1=[]
        tempRemport1.append(T(year.period.name)+' '+str(year.yearp))
        report.append(tempRemport1)

        #LEVEL 1
        if request.vars['level']=='1':
            #Heading Level 1
            tempRemport1=[]
            tempRemport1.append('')
            report.append(tempRemport1)

            tempRemport1=[]
            tempRemport1.append(T('Detail'))
            report.append(tempRemport1)

            tempRemport1=[]
            tempRemport1.append(T('Course'))
            tempRemport1.append(T('Total inserted'))
            tempRemport1.append(T('Total modified'))
            tempRemport1.append(T('Total out'))
            report.append(tempRemport1)
            #Body Level 1
            for assigantion in assigantions:
                tempRemport1=[]
                tempRemport1.append(assigantion.project.name)
                if session.search_validate_laboratory_management == "" or session.search_validate_laboratory_management is None:
                    tempRemport1.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==True)).count(db.validate_laboratory_log.id)))
                    tempRemport1.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==True)).count(db.validate_laboratory_log.id)))
                    tempRemport1.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==True)).count(db.validate_laboratory_log.id)))
                else:
                    tempRemport1.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(session.search_validate_laboratory_management)+'%'))).count(db.validate_laboratory_log.id)))
                    tempRemport1.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(session.search_validate_laboratory_management)+'%'))).count(db.validate_laboratory_log.id)))
                    tempRemport1.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(session.search_validate_laboratory_management)+'%'))).count(db.validate_laboratory_log.id)))
                pass
                report.append(tempRemport1)
            pass
        

        #LEVEL 2
        elif request.vars['level']=='2':
            #Heading Level 2
            tempRemport1=[]
            tempRemport1.append(T('Course'))
            tempRemport1.append(level_project.name)
            report.append(tempRemport1)
            
            tempRemport1=[]
            tempRemport1.append('')
            report.append(tempRemport1)

            tempRemport1=[]
            tempRemport1.append(T('Detail'))
            report.append(tempRemport1)

            tempRemport1=[]
            tempRemport1.append(T('Month'))
            tempRemport1.append(T('Total inserted'))
            tempRemport1.append(T('Total modified'))
            tempRemport1.append(T('Total out'))
            report.append(tempRemport1)
            #Body Level 2
            for month in vecMonth:
                tempRemport1=[]
                start = datetime.strptime(str(year.yearp) + '-' + str(month[0]) +'-01', "%Y-%m-%d")
                if month[2]==1:
                    end = datetime.strptime(str(year.yearp+1) + '-' + str(month[2]) +'-01', "%Y-%m-%d")
                else:
                    end = datetime.strptime(str(year.yearp) + '-' + str(month[2]) +'-01', "%Y-%m-%d")
                pass
                tempRemport1.append(month[1])
                if session.search_validate_laboratory_management == "" or session.search_validate_laboratory_management is None:
                    tempRemport1.append(str(db((db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==True)).count(db.validate_laboratory_log.id)))
                    tempRemport1.append(str(db((db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==True)).count(db.validate_laboratory_log.id)))
                    tempRemport1.append(str(db((db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==True)).count(db.validate_laboratory_log.id)))
                else:
                    tempRemport1.append(str(db((db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(session.search_validate_laboratory_management)+'%'))).count(db.validate_laboratory_log.id)))
                    tempRemport1.append(str(db((db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(session.search_validate_laboratory_management)+'%'))).count(db.validate_laboratory_log.id)))
                    tempRemport1.append(str(db((db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(session.search_validate_laboratory_management)+'%'))).count(db.validate_laboratory_log.id)))
                pass
                report.append(tempRemport1)
        

        #LEVEL 3
        elif request.vars['level']=='3':
            #Heading Level 3
            tempRemport1=[]
            tempRemport1.append(T('Course'))
            tempRemport1.append(level_project.name)
            report.append(tempRemport1)

            tempRemport1=[]
            tempRemport1.append(T('Month'))
            for tempMonth in vecMonth:
                if str(tempMonth[0])==level_month:
                    tempRemport1.append(tempMonth[1])
                    start = datetime.strptime(str(year.yearp) + '-' + str(tempMonth[0]) +'-01', "%Y-%m-%d")
                    if tempMonth[2]==1:
                        end = datetime.strptime(str(year.yearp+1) + '-' + str(tempMonth[2]) +'-01', "%Y-%m-%d")
                    else:
                        end = datetime.strptime(str(year.yearp) + '-' + str(tempMonth[2]) +'-01', "%Y-%m-%d")
                    pass
            report.append(tempRemport1)

            tempRemport1=[]
            tempRemport1.append('')
            report.append(tempRemport1)

            tempRemport1=[]
            tempRemport1.append(T('Detail'))
            report.append(tempRemport1)

            tempRemport1=[]
            tempRole = []
            tempRemport1.append(T('Role'))
            if ((level_tipo=='all') or (level_tipo=='i')):
                tempRemport1.append(T('Total inserted'))
            if ((level_tipo=='all') or (level_tipo=='u')):
                tempRemport1.append(T('Total modified'))
            if ((level_tipo=='all') or (level_tipo=='d')):
                tempRemport1.append(T('Total out'))
            report.append(tempRemport1)
            #Body Level 3
            for tempR in db((db.auth_group.role!='Academic')&(db.auth_group.role!='DSI')).select():
                tempRole.append(tempR.role)
            for tempR in db((db.validate_laboratory_log.yearp==year.yearp)&(db.validate_laboratory_log.period==T(year.period.name))&(db.validate_laboratory_log.project==level_project.name)&(~db.validate_laboratory_log.roll.belongs(tempRole))).select(db.validate_laboratory_log.roll, distinct=True):
                tempRole.append(tempR.roll)
            for roll in tempRole:
                tempRemport1=[]
                tempRemport1.append(T('Rol '+str(roll)))
                if session.search_validate_laboratory_management == "" or session.search_validate_laboratory_management is None:
                    if ((level_tipo=='all') or (level_tipo=='i')):
                        tempRemport1.append(str(db((db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.validation_type==True)).count(db.validate_laboratory_log.id)))
                    if ((level_tipo=='all') or (level_tipo=='u')):
                        tempRemport1.append(str(db((db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.validation_type==True)).count(db.validate_laboratory_log.id)))
                    if ((level_tipo=='all') or (level_tipo=='d')):
                        tempRemport1.append(str(db((db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.validation_type==True)).count(db.validate_laboratory_log.id)))
                else:
                    if ((level_tipo=='all') or (level_tipo=='i')):
                        tempRemport1.append(str(db((db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(session.search_validate_laboratory_management)+'%'))).count(db.validate_laboratory_log.id)))
                    if ((level_tipo=='all') or (level_tipo=='u')):
                        tempRemport1.append(str(db((db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(session.search_validate_laboratory_management)+'%'))).count(db.validate_laboratory_log.id)))
                    if ((level_tipo=='all') or (level_tipo=='d')):
                        tempRemport1.append(str(db((db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(session.search_validate_laboratory_management)+'%'))).count(db.validate_laboratory_log.id)))
                pass
                report.append(tempRemport1)


        #LEVEL 4
        elif request.vars['level']=='4':
            #Heading Level 4
            tempRemport1=[]
            tempRemport1.append(T('Course'))
            tempRemport1.append(level_project.name)
            report.append(tempRemport1)

            tempRemport1=[]
            tempRemport1.append(T('Month'))
            for tempMonth in vecMonth:
                if str(tempMonth[0])==level_month:
                    tempRemport1.append(tempMonth[1])
                    start = datetime.strptime(str(year.yearp) + '-' + str(tempMonth[0]) +'-01', "%Y-%m-%d")
                    if tempMonth[2]==1:
                        end = datetime.strptime(str(year.yearp+1) + '-' + str(tempMonth[2]) +'-01', "%Y-%m-%d")
                    else:
                        end = datetime.strptime(str(year.yearp) + '-' + str(tempMonth[2]) +'-01', "%Y-%m-%d")
                    pass
            report.append(tempRemport1)

            tempRemport1=[]
            tempRemport1.append(T('Role'))
            tempRemport1.append(T('Rol '+level_rol))
            report.append(tempRemport1)

            tempRemport1=[]
            tempRemport1.append('')
            report.append(tempRemport1)

            tempRemport1=[]
            tempRemport1.append(T('Detail'))
            report.append(tempRemport1)

            tempRemport1=[]
            tempUsers=[]
            tempRemport1.append(T('User'))
            if ((level_tipo=='all') or (level_tipo=='i')):
                tempRemport1.append(T('Total inserted'))
            if ((level_tipo=='all') or (level_tipo=='u')):
                tempRemport1.append(T('Total modified'))
            if ((level_tipo=='all') or (level_tipo=='d')):
                tempRemport1.append(T('Total out'))
            report.append(tempRemport1)
            #Body Level 4
            tempUsers2=[]
            registerRol = db(db.auth_group.role==level_rol).select().first()
            if ((level_rol=='Super-Administrator') or (level_rol=='Ecys-Administrator')):
                for valueU in db((db.auth_membership.group_id==registerRol.id)).select(db.auth_membership.user_id, distinct=True):
                    tempUsers.append(valueU.user_id.username)
            else:
                for valueU in db((db.auth_membership.group_id==registerRol.id)).select(db.auth_membership.user_id, distinct=True):
                    tempUsers2.append(valueU.user_id)
                for valueU in db((db.user_project.period==year.id)&(db.user_project.project==level_project.id)&(db.user_project.assigned_user.belongs(tempUsers2))).select(db.user_project.assigned_user, distinct=True):
                    tempUsers.append(valueU.assigned_user.username)
            pass
            for valueU in db((db.validate_laboratory_log.yearp==year.yearp)&(db.validate_laboratory_log.period==T(year.period.name))&(db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.roll==level_rol)&(~db.validate_laboratory_log.user_name.belongs(tempUsers))).select(db.validate_laboratory_log.user_name, distinct=True):
                tempUsers.append(valueU.user_name)
            for userr in tempUsers:
                tempRemport1=[]
                tempRemport1.append(userr)
                if session.search_validate_laboratory_management == "" or session.search_validate_laboratory_management is None:
                    if ((level_tipo=='all') or (level_tipo=='i')):
                        tempRemport1.append(str(db((db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.roll==level_rol)&(db.validate_laboratory_log.user_name==userr)).count(db.validate_laboratory_log.id)))
                    if ((level_tipo=='all') or (level_tipo=='u')):
                        tempRemport1.append(str(db((db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.roll==level_rol)&(db.validate_laboratory_log.user_name==userr)).count(db.validate_laboratory_log.id)))
                    if ((level_tipo=='all') or (level_tipo=='d')):
                        tempRemport1.append(str(db((db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.roll==level_rol)&(db.validate_laboratory_log.user_name==userr)).count(db.validate_laboratory_log.id)))
                else:
                    if ((level_tipo=='all') or (level_tipo=='i')):
                        tempRemport1.append(str(db((db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.roll==level_rol)&(db.validate_laboratory_log.user_name==userr)&(db.validate_laboratory_log.academic.like('%'+str(session.search_validate_laboratory_management)+'%'))).count(db.validate_laboratory_log.id)))
                    if ((level_tipo=='all') or (level_tipo=='u')):
                        tempRemport1.append(str(db((db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.roll==level_rol)&(db.validate_laboratory_log.user_name==userr)&(db.validate_laboratory_log.academic.like('%'+str(session.search_validate_laboratory_management)+'%'))).count(db.validate_laboratory_log.id)))
                    if ((level_tipo=='all') or (level_tipo=='d')):
                        tempRemport1.append(str(db((db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.roll==level_rol)&(db.validate_laboratory_log.user_name==userr)&(db.validate_laboratory_log.academic.like('%'+str(session.search_validate_laboratory_management)+'%'))).count(db.validate_laboratory_log.id)))
                pass
                report.append(tempRemport1)
        

        #LEVEL 5
        elif request.vars['level']=='5':
            #Head of Level 5
            tempRemport1=[]
            tempRemport1.append(T('Course'))
            tempRemport1.append(level_project.name)
            report.append(tempRemport1)

            tempRemport1=[]
            tempRemport1.append(T('Month'))
            for tempMonth in vecMonth:
                if str(tempMonth[0])==level_month:
                    tempRemport1.append(tempMonth[1])
                    start = datetime.strptime(str(year.yearp) + '-' + str(tempMonth[0]) +'-01', "%Y-%m-%d")
                    if tempMonth[2]==1:
                        end = datetime.strptime(str(year.yearp+1) + '-' + str(tempMonth[2]) +'-01', "%Y-%m-%d")
                    else:
                        end = datetime.strptime(str(year.yearp) + '-' + str(tempMonth[2]) +'-01', "%Y-%m-%d")
                    pass
            report.append(tempRemport1)

            tempRemport1=[]
            tempRemport1.append(T('Role'))
            tempRemport1.append(T('Rol '+level_rol))
            report.append(tempRemport1)

            tempRemport1=[]
            tempRemport1.append(T('User resolution'))
            tempRemport1.append(level_user)
            report.append(tempRemport1)

            tempRemport1=[]
            tempRemport1.append('')
            report.append(tempRemport1)

            tempRemport1=[]
            tempRemport1.append(T('Detail'))
            report.append(tempRemport1)

            temp_vecAllUserRoleMonth=[]
            tempRemport1=[]
            #Body Level 5
            if session.search_validate_laboratory_management == "" or session.search_validate_laboratory_management is None:
                if ((level_tipo=='all') or (level_tipo=='i')):
                    temp_vecAllUserRoleMonth.append(db((db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.roll==level_rol)&(db.validate_laboratory_log.user_name==level_user)).select())
                if ((level_tipo=='all') or (level_tipo=='u')):
                    temp_vecAllUserRoleMonth.append(db((db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.roll==level_rol)&(db.validate_laboratory_log.user_name==level_user)).select())
                if ((level_tipo=='all') or (level_tipo=='d')):
                    temp_vecAllUserRoleMonth.append(db((db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.roll==level_rol)&(db.validate_laboratory_log.user_name==level_user)).select())
            else:
                if ((level_tipo=='all') or (level_tipo=='i')):
                    temp_vecAllUserRoleMonth.append(db((db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.roll==level_rol)&(db.validate_laboratory_log.user_name==level_user)&(db.validate_laboratory_log.academic.like('%'+str(session.search_validate_laboratory_management)+'%'))).select())
                if ((level_tipo=='all') or (level_tipo=='u')):
                    temp_vecAllUserRoleMonth.append(db((db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.roll==level_rol)&(db.validate_laboratory_log.user_name==level_user)&(db.validate_laboratory_log.academic.like('%'+str(session.search_validate_laboratory_management)+'%'))).select())
                if ((level_tipo=='all') or (level_tipo=='d')):
                    temp_vecAllUserRoleMonth.append(db((db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.roll==level_rol)&(db.validate_laboratory_log.user_name==level_user)&(db.validate_laboratory_log.academic.like('%'+str(session.search_validate_laboratory_management)+'%'))).select())
            pass
            varTypeHead=0
            for field in temp_vecAllUserRoleMonth:
                for camp in field:
                    if varTypeHead==0:
                        #Heading Level 5
                        tempRemport1=[]
                        tempRemport1.append(T('User resolution'))
                        tempRemport1.append(T('Role resolution'))
                        tempRemport1.append(T('Date of resolution'))
                        tempRemport1.append(T('Operation'))
                        tempRemport1.append(T('Description'))
                        tempRemport1.append(T('Rol Academic'))
                        tempRemport1.append(T('Before Grade'))
                        tempRemport1.append(T('Grade edited'))
                        report.append(tempRemport1)
                        varTypeHead=1
                    tempRemport1=[]
                    tempRemport1.append(str(camp.user_name))
                    tempRemport1.append(T('Rol '+str(camp.roll)))
                    tempRemport1.append(str(camp.date_log))
                    tempRemport1.append(str(camp.operation_log))
                    tempRemport1.append(str(camp.description))
                    tempRemport1.append(str(camp.academic))
                    tempRemport1.append(str(camp.before_grade))
                    tempRemport1.append(str(camp.after_grade))
                    report.append(tempRemport1)
                pass
            pass
        return dict(filename='ReporteGestionRevalidaciones', csvdata=report)
    else:
        session.flash = T('Not valid Action.')
        redirect(URL('activity_control','validate_laboratory_management'))



#Management Report revalidation laboratory levels 1 and 2
@auth.requires_login()
@auth.requires(auth.has_membership('Teacher'))
def validate_laboratory_management():
    #Export Report to CSV
    if request.vars['list'] =='True':
        redirect(URL('activity_control','validate_laboratory_management_export'))

    #Export Report Nivel 0
    if request.vars['list'] =='False':
        if request.vars['level'] =='1':
            redirect(URL('activity_control','validate_laboratory_management_level_export',vars=dict(level=request.vars['level'])))
        elif request.vars['level'] =='2':
            if request.vars['level_project'] is None or request.vars['level_project']=='':
                redirect(URL('activity_control','validate_laboratory_management'))
            else:
                redirect(URL('activity_control','validate_laboratory_management_level_export',vars=dict(level=request.vars['level'],level_project=request.vars['level_project'])))
        else:
            redirect(URL('activity_control','validate_laboratory_management'))


    import cpfecys
    #Obtain the current period of the system and all the register periods
    period = cpfecys.current_year_period()

    #Check if the user is assigned to the course
    assigantions = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == period.id)).select()
    if assigantions.first() is None:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))

    #Vec with the months of the current period
    vecMonth=[]
    tmpMonth=[]
    if period.period == 1:
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


        if (request.args(0) == 'search'):
            if str(request.vars['querySearch']) == "":
                session.search_validate_laboratory_management = ""
            else:
                if str(request.vars['querySearch']).isdigit()==True:
                    session.search_validate_laboratory_management = str(request.vars['querySearch'])
                else:
                    session.search_validate_laboratory_management = ""
                    session.flash=T('The lookup value is not allowed.')
                    redirect(URL('activity_control','validate_laboratory_management'))
        else:
            session.search_validate_laboratory_management = ""

    return dict(year=period, assigantions=assigantions, vecMonth=vecMonth)



#********************************************************
#Management Report revalidation laboratory level 3
@auth.requires_login()
@auth.requires(auth.has_membership('Teacher'))
def validate_laboratory_management_n2():
    import cpfecys
    #Obtain the current period of the system and all the register periods
    period = cpfecys.current_year_period()
    showLevel = True
    project = None
    tipo = None
    month=None
    vecRoleMonth=None
    messageError=''

    #Check if a search exist, verify that they are just numbers
    if session.search_validate_laboratory_management != "" and session.search_validate_laboratory_management is not None:
        if str(session.search_validate_laboratory_management).isdigit()==False:
            session.search_validate_laboratory_management = ""
            messageError=T('The lookup value is not allowed.')
            showLevel = False

    #Check the correct parameters
    if request.vars['list'] =='False':
        if request.vars['level'] =='3':
            if request.vars['level_project'] is None or request.vars['level_project']=='':
                messageError=T('Error. Unable to export the reporting level for lack of parameters.')
                showLevel = False
            else:
                if request.vars['level_month'] is None or request.vars['level_month']=='':
                    messageError=T('Error. Unable to export the reporting level for lack of parameters.')
                    showLevel = False
                else:
                    if request.vars['level_tipo'] is None or request.vars['level_tipo']=='':
                        messageError=T('Error. Unable to export the reporting level for lack of parameters.')
                        showLevel = False
                    else:
                        redirect(URL('activity_control','validate_laboratory_management_level_export',vars=dict(level=request.vars['level'],level_project=request.vars['level_project'],level_month=request.vars['level_month'],level_tipo=request.vars['level_tipo'])))
        else:
            messageError=T('Error. Unable to export the reporting level for lack of parameters.')
            showLevel = False

    #Check if the project is correct
    if request.vars['tipo'] is None or request.vars['tipo']=='':
        messageError=T('Error. Unable to show the reporting level for lack of parameters.')
        showLevel = False
    else:
        if str(request.vars['tipo'])!='all' and str(request.vars['tipo'])!='i' and str(request.vars['tipo'])!='u' and str(request.vars['tipo'])!='d':
            messageError=T('Error. Unable to show the reporting level for lack of parameters.')
            showLevel = False
        else:
            tipo = str(request.vars['tipo'])


    #Check if the project is correct
    if request.vars['project'] is None or request.vars['project']=='':
        messageError=T('Error. Unable to show the reporting level for lack of parameters.')
        showLevel = False
    else:
        project = request.vars['project']
        project = db(db.project.id==project).select().first()
        if project is None:
            messageError=T('Action not allowed')
            showLevel = False


    #Check if the user is assigned to the project
    if project is None or tipo is None:
        messageError=T('Error. Unable to show the reporting level for lack of parameters.')
        showLevel = False
    else:
        if auth.has_membership('Teacher'):
            course = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == period.id) & (db.user_project.project==project.id)).select().first()
            if course is None:
                messageError=T('Action not allowed')
                showLevel = False
        else:
            messageError=T('Action not allowed')
            showLevel = False


    #Check if the month is correct
    if showLevel==True:
        if request.vars['month'] is None or request.vars['month']=='':
            messageError=T('Error. Unable to show the reporting level for lack of parameters.')
            showLevel = False
        else:
            if period.period == 1:
                if int(request.vars['month']) >= 1 and int(request.vars['month']) <=5:
                    month=str(request.vars['month'])
                else:
                    messageError=T('Action not allowed')
                    showLevel = False
            else:
                if int(request.vars['month']) >= 6 and int(request.vars['month']) <=12:
                    month=str(request.vars['month'])
                else:
                    messageError=T('Action not allowed')
                    showLevel = False


    #***************************************************************************************************************************************************************************************************************
    #***************************************************************************************************************************************************************************************************************
    #***************************************************************************************************************************************************************************************************************
    #***************************************************************************************************************************************************************************************************************


    #All the parameters are ok, start to build the report level 2
    if showLevel==True:
        from datetime import datetime
        start = datetime.strptime(str(period.yearp) + '-' + month +'-01', "%Y-%m-%d")
        if month=='12':
            end = datetime.strptime(str(period.yearp+1) + '-' + '01-01', "%Y-%m-%d")
        else:
            end = datetime.strptime(str(period.yearp) + '-' + str(int(month)+1) +'-01', "%Y-%m-%d")
        pass
        vecRoleMonth=[]
        roleTemp=[]
        for value in db((db.auth_group.role!='Academic')&(db.auth_group.role!='DSI')).select():
            optionSearch=[]
            optionSearch.append(value.role)
            roleTemp.append(value.role)
            if str(request.vars['tipo'])=='all' or str(request.vars['tipo'])=='i':
                if session.search_validate_laboratory_management == "" or session.search_validate_laboratory_management is None:
                    optionSearch.append(str(db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.yearp==str(period.yearp))&(db.validate_laboratory_log.period==str(T(period.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.roll==value.role)&(db.validate_laboratory_log.validation_type==True)).count(db.validate_laboratory_log.id)))
                else:
                    optionSearch.append(str(db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.yearp==str(period.yearp))&(db.validate_laboratory_log.period==str(T(period.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.roll==value.role)&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(session.search_validate_laboratory_management)+'%'))).count(db.validate_laboratory_log.id)))
                pass
            if str(request.vars['tipo'])=='all' or str(request.vars['tipo'])=='u':
                if session.search_validate_laboratory_management == "" or session.search_validate_laboratory_management is None:
                    optionSearch.append(str(db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.yearp==str(period.yearp))&(db.validate_laboratory_log.period==str(T(period.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.roll==value.role)&(db.validate_laboratory_log.validation_type==True)).count(db.validate_laboratory_log.id)))
                else:
                    optionSearch.append(str(db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.yearp==str(period.yearp))&(db.validate_laboratory_log.period==str(T(period.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.roll==value.role)&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(session.search_validate_laboratory_management)+'%'))).count(db.validate_laboratory_log.id)))
                pass
            if str(request.vars['tipo'])=='all' or str(request.vars['tipo'])=='d':
                if session.search_validate_laboratory_management == "" or session.search_validate_laboratory_management is None:
                    optionSearch.append(str(db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.yearp==str(period.yearp))&(db.validate_laboratory_log.period==str(T(period.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.roll==value.role)&(db.validate_laboratory_log.validation_type==True)).count(db.validate_laboratory_log.id)))
                else:
                    optionSearch.append(str(db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.yearp==str(period.yearp))&(db.validate_laboratory_log.period==str(T(period.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.roll==value.role)&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(session.search_validate_laboratory_management)+'%'))).count(db.validate_laboratory_log.id)))
                pass
            vecRoleMonth.append(optionSearch)
        #Check if the log has a roll that is not register
        for value in db((db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.project==project.name)&(~db.validate_laboratory_log.roll.belongs(roleTemp))).select(db.validate_laboratory_log.roll, distinct=True):
            optionSearch=[]
            optionSearch.append(value.roll)
            if str(request.vars['tipo'])=='all' or str(request.vars['tipo'])=='i':
                if session.search_validate_laboratory_management == "" or session.search_validate_laboratory_management is None:
                    optionSearch.append(str(db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.yearp==str(period.yearp))&(db.validate_laboratory_log.period==str(T(period.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.roll==value.roll)&(db.validate_laboratory_log.validation_type==True)).count(db.validate_laboratory_log.id)))
                else:
                    optionSearch.append(str(db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.yearp==str(period.yearp))&(db.validate_laboratory_log.period==str(T(period.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.roll==value.roll)&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(session.search_validate_laboratory_management)+'%'))).count(db.validate_laboratory_log.id)))
                pass
            if str(request.vars['tipo'])=='all' or str(request.vars['tipo'])=='u':
                if session.search_validate_laboratory_management == "" or session.search_validate_laboratory_management is None:
                    optionSearch.append(str(db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.yearp==str(period.yearp))&(db.validate_laboratory_log.period==str(T(period.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.roll==value.roll)&(db.validate_laboratory_log.validation_type==True)).count(db.validate_laboratory_log.id)))
                else:
                    optionSearch.append(str(db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.yearp==str(period.yearp))&(db.validate_laboratory_log.period==str(T(period.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.roll==value.roll)&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(session.search_validate_laboratory_management)+'%'))).count(db.validate_laboratory_log.id)))
                pass
            if str(request.vars['tipo'])=='all' or str(request.vars['tipo'])=='d':
                if session.search_validate_laboratory_management == "" or session.search_validate_laboratory_management is None:
                    optionSearch.append(str(db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.yearp==str(period.yearp))&(db.validate_laboratory_log.period==str(T(period.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.roll==value.roll)&(db.validate_laboratory_log.validation_type==True)).count(db.validate_laboratory_log.id)))
                else:
                    optionSearch.append(str(db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.yearp==str(period.yearp))&(db.validate_laboratory_log.period==str(T(period.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.roll==value.roll)&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(session.search_validate_laboratory_management)+'%'))).count(db.validate_laboratory_log.id)))
                pass
            vecRoleMonth.append(optionSearch)
    return dict(showLevel=showLevel, project=project, tipo=tipo, month=month, vecRoleMonth=vecRoleMonth, messageError=messageError)



#********************************************************
#Management Report revalidation laboratory level 4
@auth.requires_login()
@auth.requires(auth.has_membership('Teacher'))
def validate_laboratory_management_n3():
    import cpfecys
    #Obtain the current period of the system and all the register periods
    period = cpfecys.current_year_period()
    showLevel = True
    project = None
    tipo = None
    month=None
    roll=None
    vecUserRoleMonth=None
    messageError=''

    #Check if a search exist, verify that they are just numbers
    if session.search_validate_laboratory_management != "" and session.search_validate_laboratory_management is not None:
        if str(session.search_validate_laboratory_management).isdigit()==False:
            session.search_validate_laboratory_management = ""
            messageError=T('The lookup value is not allowed.')
            showLevel = False

    #Check the correct parameters
    if request.vars['list'] =='False':
        if request.vars['level'] =='4':
            if request.vars['level_project'] is None or request.vars['level_project']=='':
                messageError=T('Error. Unable to export the reporting level for lack of parameters.')
                showLevel = False
            else:
                if request.vars['level_month'] is None or request.vars['level_month']=='':
                    messageError=T('Error. Unable to export the reporting level for lack of parameters.')
                    showLevel = False
                else:
                    if request.vars['level_tipo'] is None or request.vars['level_tipo']=='':
                        messageError=T('Error. Unable to export the reporting level for lack of parameters.')
                        showLevel = False
                    else:
                        if request.vars['level_rol'] is None or request.vars['level_rol']=='':
                            messageError=T('Error. Unable to export the reporting level for lack of parameters.')
                            showLevel = False
                        else:
                            redirect(URL('activity_control','validate_laboratory_management_level_export',vars=dict(level=request.vars['level'],level_project=request.vars['level_project'],level_month=request.vars['level_month'],level_tipo=request.vars['level_tipo'],level_rol=request.vars['level_rol'])))
        else:
            messageError=T('Error. Unable to export the reporting level for lack of parameters.')
            showLevel = False

    #Check if the project is correct
    if request.vars['tipo'] is None or request.vars['tipo']=='':
        messageError=T('Error. Unable to show the reporting level for lack of parameters.')
        showLevel = False
    else:
        if str(request.vars['tipo'])!='all' and str(request.vars['tipo'])!='i' and str(request.vars['tipo'])!='u' and str(request.vars['tipo'])!='d':
            messageError=T('Error. Unable to show the reporting level for lack of parameters.')
            showLevel = False
        else:
            tipo = str(request.vars['tipo'])


    #Check if the project is correct
    if request.vars['project'] is None or request.vars['project']=='':
        messageError=T('Error. Unable to show the reporting level for lack of parameters.')
        showLevel = False
    else:
        project = request.vars['project']
        project = db(db.project.id==project).select().first()
        if project is None:
            messageError=T('Action not allowed')
            showLevel = False


    #Check if the user is assigned to the project
    if project is None or tipo is None:
        messageError=T('Error. Unable to show the reporting level for lack of parameters.')
        showLevel = False
    else:
        if auth.has_membership('Teacher'):
            course = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == period.id) & (db.user_project.project==project.id)).select().first()
            if course is None:
                messageError=T('Action not allowed')
                showLevel = False
        else:
            messageError=T('Action not allowed')
            showLevel = False


    #Check if the month is correct
    if showLevel==True:
        if request.vars['month'] is None or request.vars['month']=='':
            messageError=T('Error. Unable to show the reporting level for lack of parameters.')
            showLevel = False
        else:
            if period.period == 1:
                if int(request.vars['month']) >= 1 and int(request.vars['month']) <=5:
                    month=str(request.vars['month'])
                else:
                    messageError=T('Action not allowed')
                    showLevel = False
            else:
                if int(request.vars['month']) >= 6 and int(request.vars['month']) <=12:
                    month=str(request.vars['month'])
                else:
                    messageError=T('Action not allowed')
                    showLevel = False


    #Check if the roll is correct
    if showLevel==True:
        if request.vars['roll'] is None or request.vars['roll']=='':
            messageError=T('Error. Unable to show the reporting level for lack of parameters.')
            showLevel = False
        else:
            value = db(db.auth_group.role==str(request.vars['roll'])).select().first()
            if value is None:
                #Check if the log has a roll that is not register
                value = db((db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.roll==str(request.vars['roll']))).select(db.validate_laboratory_log.roll, distinct=True).first()
                if value is None:
                    messageError=T('Action not allowed')
                    showLevel = False
                else:
                    roll=str(value.roll)
            else:
                roll=str(value.role)


    #***************************************************************************************************************************************************************************************************************
    #***************************************************************************************************************************************************************************************************************
    #***************************************************************************************************************************************************************************************************************
    #***************************************************************************************************************************************************************************************************************


    #All the parameters are ok, start to build the report level 2
    if showLevel==True:
        from datetime import datetime
        start = datetime.strptime(str(period.yearp) + '-' + month +'-01', "%Y-%m-%d")
        if month=='12':
            end = datetime.strptime(str(period.yearp+1) + '-' + '01-01', "%Y-%m-%d")
        else:
            end = datetime.strptime(str(period.yearp) + '-' + str(int(month)+1) +'-01', "%Y-%m-%d")
        pass

        #Users in the actual registers
        tempUsers=[]
        tempUsers2=[]
        registerRol = db(db.auth_group.role==roll).select().first()
        if registerRol is not None:
            if ((roll=='Super-Administrator') or (roll=='Ecys-Administrator')):
                for value in db((db.auth_membership.group_id==registerRol.id)).select(db.auth_membership.user_id, distinct=True):
                    tempUsers.append(value.user_id.username)
            else:
                for value in db((db.auth_membership.group_id==registerRol.id)).select(db.auth_membership.user_id, distinct=True):
                    tempUsers2.append(value.user_id)
                for value in db((db.user_project.period==period.id)&(db.user_project.project==project.id)&(db.user_project.assigned_user.belongs(tempUsers2))).select(db.user_project.assigned_user, distinct=True):
                    tempUsers.append(value.assigned_user.username)
            pass
        pass
        #Check if the log has an username that is not register
        for value in db((db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.roll==roll)&(~db.validate_laboratory_log.user_name.belongs(tempUsers))).select(db.validate_laboratory_log.user_name, distinct=True):
            tempUsers.append(value.user_name)
        
        vecUserRoleMonth=[]
        for value in tempUsers:
            optionSearch=[]
            optionSearch.append(value)
            if str(request.vars['tipo'])=='all' or str(request.vars['tipo'])=='i':
                if session.search_validate_laboratory_management == "" or session.search_validate_laboratory_management is None:
                    optionSearch.append(str(db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.yearp==str(period.yearp))&(db.validate_laboratory_log.period==str(T(period.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==value)).count(db.validate_laboratory_log.id)))
                else:
                    optionSearch.append(str(db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.yearp==str(period.yearp))&(db.validate_laboratory_log.period==str(T(period.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==value)&(db.validate_laboratory_log.academic.like('%'+str(session.search_validate_laboratory_management)+'%'))).count(db.validate_laboratory_log.id)))
                pass
            if str(request.vars['tipo'])=='all' or str(request.vars['tipo'])=='u':
                if session.search_validate_laboratory_management == "" or session.search_validate_laboratory_management is None:
                    optionSearch.append(str(db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.yearp==str(period.yearp))&(db.validate_laboratory_log.period==str(T(period.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==value)).count(db.validate_laboratory_log.id)))
                else:
                    optionSearch.append(str(db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.yearp==str(period.yearp))&(db.validate_laboratory_log.period==str(T(period.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==value)&(db.validate_laboratory_log.academic.like('%'+str(session.search_validate_laboratory_management)+'%'))).count(db.validate_laboratory_log.id)))
                pass
            if str(request.vars['tipo'])=='all' or str(request.vars['tipo'])=='d':
                if session.search_validate_laboratory_management == "" or session.search_validate_laboratory_management is None:
                    optionSearch.append(str(db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.yearp==str(period.yearp))&(db.validate_laboratory_log.period==str(T(period.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==value)).count(db.validate_laboratory_log.id)))
                else:
                    optionSearch.append(str(db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.yearp==str(period.yearp))&(db.validate_laboratory_log.period==str(T(period.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==value)&(db.validate_laboratory_log.academic.like('%'+str(session.search_validate_laboratory_management)+'%'))).count(db.validate_laboratory_log.id)))
                pass
            vecUserRoleMonth.append(optionSearch)
    return dict(showLevel=showLevel, project=project, tipo=tipo, month=month, vecUserRoleMonth=vecUserRoleMonth, roll=roll, messageError=messageError)



#********************************************************
#Management Report revalidation laboratory level 5
@auth.requires_login()
@auth.requires(auth.has_membership('Teacher'))
def validate_laboratory_management_n4():
    import cpfecys
    #Obtain the current period of the system and all the register periods
    period = cpfecys.current_year_period()
    showLevel = True
    project = None
    tipo = None
    month=None
    roll=None
    userr=None
    vecAllUserRoleMonth=None
    messageError=''

    #Check if a search exist, verify that they are just numbers
    if session.search_validate_laboratory_management != "" and session.search_validate_laboratory_management is not None:
        if str(session.search_validate_laboratory_management).isdigit()==False:
            session.search_validate_laboratory_management = ""
            messageError=T('The lookup value is not allowed.')
            showLevel = False

    #Check the correct parameters
    if request.vars['list'] =='False':
        if request.vars['level'] =='5':
            if request.vars['level_project'] is None or request.vars['level_project']=='':
                messageError=T('Error. Unable to export the reporting level for lack of parameters.')
                showLevel = False
            else:
                if request.vars['level_month'] is None or request.vars['level_month']=='':
                    messageError=T('Error. Unable to export the reporting level for lack of parameters.')
                    showLevel = False
                else:
                    if request.vars['level_tipo'] is None or request.vars['level_tipo']=='':
                        messageError=T('Error. Unable to export the reporting level for lack of parameters.')
                        showLevel = False
                    else:
                        if request.vars['level_rol'] is None or request.vars['level_rol']=='':
                            messageError=T('Error. Unable to export the reporting level for lack of parameters.')
                            showLevel = False
                        else:
                            if request.vars['level_user'] is None or request.vars['level_user']=='':
                                messageError=T('Error. Unable to export the reporting level for lack of parameters.')
                                showLevel = False
                            else:
                                redirect(URL('activity_control','validate_laboratory_management_level_export',vars=dict(level=request.vars['level'],level_project=request.vars['level_project'],level_month=request.vars['level_month'],level_tipo=request.vars['level_tipo'],level_rol=request.vars['level_rol'],level_user=request.vars['level_user'])))
        else:
            messageError=T('Error. Unable to export the reporting level for lack of parameters.')
            showLevel = False

    #Check if the project is correct
    if request.vars['tipo'] is None or request.vars['tipo']=='':
        messageError=T('Error. Unable to export the reporting level for lack of parameters.')
        showLevel = False
    else:
        if str(request.vars['tipo'])!='all' and str(request.vars['tipo'])!='i' and str(request.vars['tipo'])!='u' and str(request.vars['tipo'])!='d':
            messageError=T('Error. Unable to export the reporting level for lack of parameters.')
            showLevel = False
        else:
            tipo = str(request.vars['tipo'])


    #Check if the project is correct
    if request.vars['project'] is None or request.vars['project']=='':
        messageError=T('Error. Unable to export the reporting level for lack of parameters.')
        showLevel = False
    else:
        project = request.vars['project']
        project = db(db.project.id==project).select().first()
        if project is None:
            messageError=T('Action not allowed')
            showLevel = False


    #Check if the user is assigned to the project
    if project is None or tipo is None:
        messageError=T('Error. Unable to export the reporting level for lack of parameters.')
        showLevel = False
    else:
        if auth.has_membership('Teacher'):
            course = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == period.id) & (db.user_project.project==project.id)).select().first()
            if course is None:
                messageError=T('Action not allowed')
                showLevel = False
        else:
            messageError=T('Action not allowed')
            showLevel = False


    #Check if the month is correct
    if showLevel==True:
        if request.vars['month'] is None or request.vars['month']=='':
            messageError=T('Error. Unable to export the reporting level for lack of parameters.')
            showLevel = False
        else:
            if period.period == 1:
                if int(request.vars['month']) >= 1 and int(request.vars['month']) <=5:
                    month=str(request.vars['month'])
                else:
                    messageError=T('Action not allowed')
                    showLevel = False
            else:
                if int(request.vars['month']) >= 6 and int(request.vars['month']) <=12:
                    month=str(request.vars['month'])
                else:
                    messageError=T('Action not allowed')
                    showLevel = False


    #Check if the roll is correct
    if showLevel==True:
        if request.vars['roll'] is None or request.vars['roll']=='':
            messageError=T('Error. Unable to export the reporting level for lack of parameters.')
            showLevel = False
        else:
            value = db(db.auth_group.role==str(request.vars['roll'])).select().first()
            if value is None:
                #Check if the log has a roll that is not register
                value = db((db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.roll==str(request.vars['roll']))).select(db.validate_laboratory_log.roll, distinct=True).first()
                if value is None:
                    messageError=T('Action not allowed')
                    showLevel = False
                else:
                    roll=value
            else:
                roll=value.role

    #Check if the user is correct
    if showLevel==True:
        if request.vars['userr'] is None or request.vars['userr']=='':
            messageError=T('Error. Unable to export the reporting level for lack of parameters.')
            showLevel = False
        else:
            flagCheck = False
            #User Temp of auth_user where the username is equal
            userr = db(db.auth_user.username==str(request.vars['userr'])).select().first()
            if ((roll=='Super-Administrator') or (roll=='Ecys-Administrator')):
                if userr is not None:
                    #Check if the user has the rol specific
                    userrT = db(db.auth_membership.user_id==userr.id).select()
                    for tempUserCheck in userrT:
                        if tempUserCheck.group_id.role==roll:
                            flagCheck = True
            else:
                if userr is not None:
                    #Check if the user has the rol specific
                    userrT = db(db.auth_membership.user_id==userr.id).select()
                    for tempUserCheck in userrT:
                        if tempUserCheck.group_id.role==roll:
                            if db((db.user_project.period==period.id)&(db.user_project.project==project.id)&(db.user_project.assigned_user==userr.id)).select().first() is not None:
                                flagCheck = True

            if flagCheck==False:
                #Check if the log has a roll that is not register
                userr = db((db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==str(request.vars['userr']))).select().first()
                if value is None:
                    messageError=T('Action not allowed')
                    showLevel = False
                else:
                    userr=userr.user_name
            else:
                userr=userr.username


    #***************************************************************************************************************************************************************************************************************
    #***************************************************************************************************************************************************************************************************************
    #***************************************************************************************************************************************************************************************************************
    #***************************************************************************************************************************************************************************************************************


    #All the parameters are ok, start to build the report level 2
    if showLevel==True:
        from datetime import datetime
        start = datetime.strptime(str(period.yearp) + '-' + month +'-01', "%Y-%m-%d")
        if month=='12':
            end = datetime.strptime(str(period.yearp+1) + '-' + '01-01', "%Y-%m-%d")
        else:
            end = datetime.strptime(str(period.yearp) + '-' + str(int(month)+1) +'-01', "%Y-%m-%d")
        pass
        
        vecAllUserRoleMonth=[]
        if str(request.vars['tipo'])=='all' or str(request.vars['tipo'])=='i':            
            if session.search_validate_laboratory_management == "" or session.search_validate_laboratory_management is None:
                vecAllUserRoleMonth.append(db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.yearp==str(period.yearp))&(db.validate_laboratory_log.period==str(T(period.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==userr)).select())
            else:
                vecAllUserRoleMonth.append(db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.yearp==str(period.yearp))&(db.validate_laboratory_log.period==str(T(period.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==userr)&(db.validate_laboratory_log.academic.like('%'+str(session.search_validate_laboratory_management)+'%'))).select())
            pass
        if str(request.vars['tipo'])=='all' or str(request.vars['tipo'])=='u':
            if session.search_validate_laboratory_management == "" or session.search_validate_laboratory_management is None:
                vecAllUserRoleMonth.append(db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.yearp==str(period.yearp))&(db.validate_laboratory_log.period==str(T(period.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==userr)).select())
            else:
                vecAllUserRoleMonth.append(db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.yearp==str(period.yearp))&(db.validate_laboratory_log.period==str(T(period.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==userr)&(db.validate_laboratory_log.academic.like('%'+str(session.search_validate_laboratory_management)+'%'))).select())
            pass
        if str(request.vars['tipo'])=='all' or str(request.vars['tipo'])=='d':
            if session.search_validate_laboratory_management == "" or session.search_validate_laboratory_management is None:
                vecAllUserRoleMonth.append(db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.yearp==str(period.yearp))&(db.validate_laboratory_log.period==str(T(period.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==userr)).select())
            else:
                vecAllUserRoleMonth.append(db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.yearp==str(period.yearp))&(db.validate_laboratory_log.period==str(T(period.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==userr)&(db.validate_laboratory_log.academic.like('%'+str(session.search_validate_laboratory_management)+'%'))).select())
            pass
    return dict(showLevel=showLevel, project=project, tipo=tipo, month=month, vecAllUserRoleMonth=vecAllUserRoleMonth, roll=roll, userr=userr, messageError=messageError)





########################################################################################################################################################################################################################################################################
########################################################################################################################################################################################################################################################################
########################################################################################################################################################################################################################################################################
########################################################################################################################################################################################################################################################################
#####################################################Management Report Equivalence  laboratory#####################################################
#********************************************************
#Export full management reporting laboratory revalidation
@auth.requires_login()
@auth.requires(auth.has_membership('Teacher'))
def laboratory_replacing_management_export():
    #Vars of the report
    report=[]
    tempRemport1=[]
    tempRemport2=[]
    tempRemport3=[]
    tempRemport4=[]
    tempRemport5=[]
    #Obtain the current period of the system and all the register periods
    import cpfecys
    from datetime import datetime
    year = cpfecys.current_year_period()

    #Check if the user is assigned to the course
    assigantions = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == year.id)).select()
    if assigantions.first() is None:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))

    #Check if a search exist, verify that they are just numbers
    if session.search_laboratory_replacing_management != "" and session.search_laboratory_replacing_management is not None:
        if str(session.search_laboratory_replacing_management).isdigit()==False:
            session.search_laboratory_replacing_management = ""
            session.flash=T('The lookup value is not allowed.')
            redirect(URL('activity_control','grades_management'))

    #Vec with the months of the current period
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

    #report.append()

    #Report heading
    tempRemport1=[]
    tempRemport1.append('Reporte de Gestión de Equivalencias de Laboratorio')
    report.append(tempRemport1)
    tempRemport1=[]
    tempRemport1.append(T(year.period.name)+' '+str(year.yearp))
    report.append(tempRemport1)

    #LEVEL 1
    #Heading Level 1
    tempRemport1=[]
    tempRemport1.append(T('Course'))
    tempRemport1.append(T('Total inserted'))
    tempRemport1.append(T('Total modified'))
    tempRemport1.append(T('Total out'))
    report.append(tempRemport1)
    #Body Level 1
    for assigantion in assigantions:
        tempRemport1=[]
        tempRemport1.append(assigantion.project.name)
        if session.search_laboratory_replacing_management == "" or session.search_laboratory_replacing_management is None:
            tempRemport1.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==False)).count(db.validate_laboratory_log.id)))
            tempRemport1.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==False)).count(db.validate_laboratory_log.id)))
            tempRemport1.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==False)).count(db.validate_laboratory_log.id)))
        else:
            tempRemport1.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(session.search_laboratory_replacing_management)+'%'))).count(db.validate_laboratory_log.id)))
            tempRemport1.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(session.search_laboratory_replacing_management)+'%'))).count(db.validate_laboratory_log.id)))
            tempRemport1.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(session.search_laboratory_replacing_management)+'%'))).count(db.validate_laboratory_log.id)))
        pass
        report.append(tempRemport1)

        #LEVEL 2
        #Heading Level 2
        tempRemport2=[]
        tempRemport2.append('')
        tempRemport2.append(T('Month'))
        tempRemport2.append(T('Total inserted'))
        tempRemport2.append(T('Total modified'))
        tempRemport2.append(T('Total out'))
        report.append(tempRemport2)
        #Body Level 2
        for month in vecMonth:
            tempRemport2=[]
            tempRemport2.append('')
            start = datetime.strptime(str(year.yearp) + '-' + str(month[0]) +'-01', "%Y-%m-%d")
            if month[2]==1:
                end = datetime.strptime(str(year.yearp+1) + '-' + str(month[2]) +'-01', "%Y-%m-%d")
            else:
                end = datetime.strptime(str(year.yearp) + '-' + str(month[2]) +'-01', "%Y-%m-%d")
            pass
            tempRemport2.append(month[1])
            if session.search_laboratory_replacing_management == "" or session.search_laboratory_replacing_management is None:
                tempRemport2.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.validation_type==False)).count(db.validate_laboratory_log.id)))
                tempRemport2.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.validation_type==False)).count(db.validate_laboratory_log.id)))
                tempRemport2.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.validation_type==False)).count(db.validate_laboratory_log.id)))
            else:
                tempRemport2.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(session.search_laboratory_replacing_management)+'%'))).count(db.validate_laboratory_log.id)))
                tempRemport2.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(session.search_laboratory_replacing_management)+'%'))).count(db.validate_laboratory_log.id)))
                tempRemport2.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(session.search_laboratory_replacing_management)+'%'))).count(db.validate_laboratory_log.id)))
            pass
            report.append(tempRemport2)

            #LEVEL 3
            #Heading Level 3
            tempRemport3=[]
            tempRole = []
            tempRemport3.append('')
            tempRemport3.append('')
            tempRemport3.append(T('Role'))
            tempRemport3.append(T('Total inserted'))
            tempRemport3.append(T('Total modified'))
            tempRemport3.append(T('Total out'))
            report.append(tempRemport3)
            #Body Level 3
            for tempR in db((db.auth_group.role!='Academic')&(db.auth_group.role!='DSI')).select():
                tempRole.append(tempR.role)
            for tempR in db((db.validate_laboratory_log.yearp==year.yearp)&(db.validate_laboratory_log.period==T(year.period.name))&(db.validate_laboratory_log.project==assigantion.project.name)&(~db.validate_laboratory_log.roll.belongs(tempRole))).select(db.validate_laboratory_log.roll, distinct=True):
                tempRole.append(tempR.roll)
            for roll in tempRole:
                tempRemport3=[]
                tempRemport3.append('')
                tempRemport3.append('')
                if roll=='Student':
                    tempRemport3.append(T('Rol Student'))
                else:
                    tempRemport3.append(T(roll))
                pass
                if session.search_laboratory_replacing_management == "" or session.search_laboratory_replacing_management is None:
                    tempRemport3.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.validation_type==False)).count(db.validate_laboratory_log.id)))
                    tempRemport3.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.validation_type==False)).count(db.validate_laboratory_log.id)))
                    tempRemport3.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.validation_type==False)).count(db.validate_laboratory_log.id)))
                else:
                    tempRemport3.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(session.search_laboratory_replacing_management)+'%'))).count(db.validate_laboratory_log.id)))
                    tempRemport3.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(session.search_laboratory_replacing_management)+'%'))).count(db.validate_laboratory_log.id)))
                    tempRemport3.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(session.search_laboratory_replacing_management)+'%'))).count(db.validate_laboratory_log.id)))
                pass
                report.append(tempRemport3)

                #LEVEL 4
                #Heading Level 4
                tempRemport4=[]
                tempUsers=[]
                tempRemport4.append('')
                tempRemport4.append('')
                tempRemport4.append('')
                tempRemport4.append(T('User'))
                tempRemport4.append(T('Total inserted'))
                tempRemport4.append(T('Total modified'))
                tempRemport4.append(T('Total out'))
                report.append(tempRemport4)
                #Body Level 4
                tempUsers2=[]
                registerRol = db(db.auth_group.role==roll).select().first()
                if ((roll=='Super-Administrator') or (roll=='Ecys-Administrator')):
                    for valueU in db((db.auth_membership.group_id==registerRol.id)).select(db.auth_membership.user_id, distinct=True):
                        tempUsers.append(valueU.user_id.username)
                else:
                    for valueU in db((db.auth_membership.group_id==registerRol.id)).select(db.auth_membership.user_id, distinct=True):
                        tempUsers2.append(valueU.user_id)
                    for valueU in db((db.user_project.period==year.id)&(db.user_project.project==assigantion.project)&(db.user_project.assigned_user.belongs(tempUsers2))).select(db.user_project.assigned_user, distinct=True):
                        tempUsers.append(valueU.assigned_user.username)
                pass
                for valueU in db((db.validate_laboratory_log.yearp==year.yearp)&(db.validate_laboratory_log.period==T(year.period.name))&(db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.roll==roll)&(~db.validate_laboratory_log.user_name.belongs(tempUsers))).select(db.validate_laboratory_log.user_name, distinct=True):
                    tempUsers.append(valueU.user_name)
                for userr in tempUsers:
                    tempRemport4=[]
                    tempRemport4.append('')
                    tempRemport4.append('')
                    tempRemport4.append('')
                    tempRemport4.append(userr)
                    if session.search_laboratory_replacing_management == "" or session.search_laboratory_replacing_management is None:
                        tempRemport4.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==userr)&(db.validate_laboratory_log.validation_type==False)).count(db.validate_laboratory_log.id)))
                        tempRemport4.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==userr)&(db.validate_laboratory_log.validation_type==False)).count(db.validate_laboratory_log.id)))
                        tempRemport4.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==userr)&(db.validate_laboratory_log.validation_type==False)).count(db.validate_laboratory_log.id)))
                    else:
                        tempRemport4.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==userr)&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(session.search_laboratory_replacing_management)+'%'))).count(db.validate_laboratory_log.id)))
                        tempRemport4.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==userr)&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(session.search_laboratory_replacing_management)+'%'))).count(db.validate_laboratory_log.id)))
                        tempRemport4.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==userr)&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(session.search_laboratory_replacing_management)+'%'))).count(db.validate_laboratory_log.id)))
                    pass
                    report.append(tempRemport4)

                    #LEVEL 5
                    temp_vecAllUserRoleMonth=[]
                    tempRemport5=[]
                    #Body Level 5
                    if session.search_laboratory_replacing_management == "" or session.search_laboratory_replacing_management is None:
                        temp_vecAllUserRoleMonth.append(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==userr)&(db.validate_laboratory_log.validation_type==False)).select())
                        temp_vecAllUserRoleMonth.append(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==userr)&(db.validate_laboratory_log.validation_type==False)).select())
                        temp_vecAllUserRoleMonth.append(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==userr)&(db.validate_laboratory_log.validation_type==False)).select())
                    else:
                        temp_vecAllUserRoleMonth.append(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==userr)&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(session.search_laboratory_replacing_management)+'%'))).select())
                        temp_vecAllUserRoleMonth.append(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==userr)&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(session.search_laboratory_replacing_management)+'%'))).select())
                        temp_vecAllUserRoleMonth.append(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==userr)&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(session.search_laboratory_replacing_management)+'%'))).select())
                    pass
                    varTypeHead=0
                    for field in temp_vecAllUserRoleMonth:
                        for camp in field:
                            if varTypeHead==0:
                                #Heading Level 5
                                tempRemport5=[]
                                tempRemport5.append('')
                                tempRemport5.append('')
                                tempRemport5.append('')
                                tempRemport5.append('')
                                tempRemport5.append(T('User resolution'))
                                tempRemport5.append(T('Role resolution'))
                                tempRemport5.append(T('Date of resolution'))
                                tempRemport5.append(T('Operation'))
                                tempRemport5.append(T('Description'))
                                tempRemport5.append(T('Rol Academic'))
                                tempRemport5.append(T('Before Grade'))
                                tempRemport5.append(T('Grade edited'))
                                report.append(tempRemport5)
                                varTypeHead=1
                            tempRemport5=[]
                            tempRemport5.append('')
                            tempRemport5.append('')
                            tempRemport5.append('')
                            tempRemport5.append('')
                            tempRemport5.append(str(camp.user_name))
                            tempRemport5.append(T('Rol '+str(camp.roll)))
                            tempRemport5.append(str(camp.date_log))
                            tempRemport5.append(str(camp.operation_log))
                            tempRemport5.append(str(camp.description))
                            tempRemport5.append(str(camp.academic))
                            tempRemport5.append(str(camp.before_grade))
                            tempRemport5.append(str(camp.after_grade))
                            report.append(tempRemport5)
                        pass
                    pass
                    #End Level 5
                pass
                #End Level 4
                report.append('')
                report.append('')
            pass
            #End Level 3
            report.append('')
            report.append('')
            report.append('')
            report.append('')
        pass
        #End Level 2
        report.append('')
        report.append('')
        report.append('')
        report.append('')
        report.append('')
        report.append('')
    pass
    #End Level 1

    return dict(filename='ReporteGestionEquivalencias', csvdata=report)



#********************************************************
#Export management reporting laboratory Equivalence
@auth.requires_login()
@auth.requires(auth.has_membership('Teacher'))
def laboratory_replacing_management_level_export():
    #Vars of the report
    createReport = True
    report=[]
    tempRemport1=[]
    #Obtain the current period of the system and all the register periods
    import cpfecys
    from datetime import datetime
    year = cpfecys.current_year_period()

    #Check if the user is assigned to the course
    assigantions = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == year.id)).select()
    if assigantions.first() is None:
        createReport=False

    #Check if a search exist, verify that they are just numbers
    if session.search_laboratory_replacing_management != "" and session.search_laboratory_replacing_management is not None:
        if str(session.search_laboratory_replacing_management).isdigit()==False:
            session.search_laboratory_replacing_management = ""
            createReport=False

    #Vec with the months of the current period
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

    #Check the parameters
    if request.vars['level']=='1' or request.vars['level']=='2' or request.vars['level']=='3' or request.vars['level']=='4' or request.vars['level']=='5':
        if int(request.vars['level']) > 1 and createReport==True:
            #Check if the project is correct
            if request.vars['level_project'] is None or request.vars['level_project']=='':
                createReport=False
            else:
                level_project = request.vars['level_project']
                level_project = db(db.project.id==level_project).select().first()
                if level_project is None:
                    createReport=False
                else:
                    exportReport=False
                    for assigantion in assigantions:
                        if assigantion.project==level_project.id:
                            exportReport=True
                    if exportReport==False:
                        createReport=False
        pass

        if int(request.vars['level']) > 2 and createReport==True:
            #Check if the Month is correct
            if request.vars['level_month'] is None or request.vars['level_month']=='':
                createReport=False
            else:
                if year.period == 1:
                    try:
                        if int(request.vars['level_month']) >= 1 and int(request.vars['level_month']) <=5:
                            level_month=str(request.vars['level_month'])
                        else:
                            createReport=False
                    except:
                        createReport=False
                else:
                    try:
                        if int(request.vars['level_month']) >= 6 and int(request.vars['level_month']) <=12:
                            level_month=str(request.vars['level_month'])
                        else:
                            createReport=False
                    except:
                        createReport=False
                
            #Check if the type is correct
            if request.vars['level_tipo'] is None or request.vars['level_tipo']=='':
                createReport=False
            else:
                if str(request.vars['level_tipo'])!='all' and str(request.vars['level_tipo'])!='i' and str(request.vars['level_tipo'])!='u' and str(request.vars['level_tipo'])!='d':
                    createReport=False
                else:
                    level_tipo = str(request.vars['level_tipo'])
        pass

        if int(request.vars['level']) > 3 and createReport==True:
            if request.vars['level_rol'] is None or request.vars['level_rol']=='':
                createReport=False
            else:
                value = db(db.auth_group.role==str(request.vars['level_rol'])).select().first()
                if value is None:
                    #Check if the log has a roll that is not register
                    value = db((db.validate_laboratory_log.yearp==year.yearp)&(db.validate_laboratory_log.period==T(year.period.name))&(db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.roll==str(request.vars['level_rol']))).select(db.validate_laboratory_log.roll, distinct=True).first()
                    if value is None:
                        createReport=False
                    else:
                        level_rol=str(value.roll)
                else:
                    level_rol=str(value.role)
        pass

        if int(request.vars['level']) > 4 and createReport==True:
            if request.vars['level_user'] is None or request.vars['level_user']=='':
                createReport=False
            else:
                flagCheck = False
                #User Temp of auth_user where the username is equal
                userr = db(db.auth_user.username==str(request.vars['level_user'])).select().first()
                if ((level_rol=='Super-Administrator') or (level_rol=='Ecys-Administrator')):
                    if userr is not None:
                        #Check if the user has the rol specific
                        userrT = db(db.auth_membership.user_id==userr.id).select()
                        for tempUserCheck in userrT:
                            if tempUserCheck.group_id.role==level_rol:
                                flagCheck = True
                else:
                    if userr is not None:
                        #Check if the user has the rol specific
                        userrT = db(db.auth_membership.user_id==userr.id).select()
                        for tempUserCheck in userrT:
                            if tempUserCheck.group_id.role==level_rol:
                                if db((db.user_project.period==year.id)&(db.user_project.project==level_project.id)&(db.user_project.assigned_user==userr.id)).select().first() is not None:
                                    flagCheck = True

                if flagCheck==False:
                    #Check if the log has a roll that is not register
                    userr = db((db.validate_laboratory_log.yearp==year.yearp)&(db.validate_laboratory_log.period==T(year.period.name))&(db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.roll==level_rol)&(db.validate_laboratory_log.user_name==str(request.vars['userr']))).select().first()
                    if value is None:
                        createReport=False
                    else:
                        level_user=userr.user_name
                else:
                    level_user=userr.username
        pass
    else:
        createReport=False

    #MAKE REPORT
    if createReport==True:
        #Report heading
        tempRemport1=[]
        tempRemport1.append('Reporte de Gestión de Equivalencias de Laboratorio')
        report.append(tempRemport1)
        tempRemport1=[]
        tempRemport1.append(T(year.period.name)+' '+str(year.yearp))
        report.append(tempRemport1)

        #LEVEL 1
        if request.vars['level']=='1':
            #Heading Level 1
            tempRemport1=[]
            tempRemport1.append('')
            report.append(tempRemport1)

            tempRemport1=[]
            tempRemport1.append(T('Detail'))
            report.append(tempRemport1)

            tempRemport1=[]
            tempRemport1.append(T('Course'))
            tempRemport1.append(T('Total inserted'))
            tempRemport1.append(T('Total modified'))
            tempRemport1.append(T('Total out'))
            report.append(tempRemport1)
            #Body Level 1
            for assigantion in assigantions:
                tempRemport1=[]
                tempRemport1.append(assigantion.project.name)
                if session.search_laboratory_replacing_management == "" or session.search_laboratory_replacing_management is None:
                    tempRemport1.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==False)).count(db.validate_laboratory_log.id)))
                    tempRemport1.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==False)).count(db.validate_laboratory_log.id)))
                    tempRemport1.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==False)).count(db.validate_laboratory_log.id)))
                else:
                    tempRemport1.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(session.search_laboratory_replacing_management)+'%'))).count(db.validate_laboratory_log.id)))
                    tempRemport1.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(session.search_laboratory_replacing_management)+'%'))).count(db.validate_laboratory_log.id)))
                    tempRemport1.append(str(db((db.validate_laboratory_log.project==assigantion.project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(session.search_laboratory_replacing_management)+'%'))).count(db.validate_laboratory_log.id)))
                pass
                report.append(tempRemport1)
            pass
        

        #LEVEL 2
        elif request.vars['level']=='2':
            #Heading Level 2
            tempRemport1=[]
            tempRemport1.append(T('Course'))
            tempRemport1.append(level_project.name)
            report.append(tempRemport1)
            
            tempRemport1=[]
            tempRemport1.append('')
            report.append(tempRemport1)

            tempRemport1=[]
            tempRemport1.append(T('Detail'))
            report.append(tempRemport1)

            tempRemport1=[]
            tempRemport1.append(T('Month'))
            tempRemport1.append(T('Total inserted'))
            tempRemport1.append(T('Total modified'))
            tempRemport1.append(T('Total out'))
            report.append(tempRemport1)
            #Body Level 2
            for month in vecMonth:
                tempRemport1=[]
                start = datetime.strptime(str(year.yearp) + '-' + str(month[0]) +'-01', "%Y-%m-%d")
                if month[2]==1:
                    end = datetime.strptime(str(year.yearp+1) + '-' + str(month[2]) +'-01', "%Y-%m-%d")
                else:
                    end = datetime.strptime(str(year.yearp) + '-' + str(month[2]) +'-01', "%Y-%m-%d")
                pass
                tempRemport1.append(month[1])
                if session.search_laboratory_replacing_management == "" or session.search_laboratory_replacing_management is None:
                    tempRemport1.append(str(db((db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==False)).count(db.validate_laboratory_log.id)))
                    tempRemport1.append(str(db((db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==False)).count(db.validate_laboratory_log.id)))
                    tempRemport1.append(str(db((db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==False)).count(db.validate_laboratory_log.id)))
                else:
                    tempRemport1.append(str(db((db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(session.search_laboratory_replacing_management)+'%'))).count(db.validate_laboratory_log.id)))
                    tempRemport1.append(str(db((db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(session.search_laboratory_replacing_management)+'%'))).count(db.validate_laboratory_log.id)))
                    tempRemport1.append(str(db((db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(session.search_laboratory_replacing_management)+'%'))).count(db.validate_laboratory_log.id)))
                pass
                report.append(tempRemport1)
        

        #LEVEL 3
        elif request.vars['level']=='3':
            #Heading Level 3
            tempRemport1=[]
            tempRemport1.append(T('Course'))
            tempRemport1.append(level_project.name)
            report.append(tempRemport1)

            tempRemport1=[]
            tempRemport1.append(T('Month'))
            for tempMonth in vecMonth:
                if str(tempMonth[0])==level_month:
                    tempRemport1.append(tempMonth[1])
                    start = datetime.strptime(str(year.yearp) + '-' + str(tempMonth[0]) +'-01', "%Y-%m-%d")
                    if tempMonth[2]==1:
                        end = datetime.strptime(str(year.yearp+1) + '-' + str(tempMonth[2]) +'-01', "%Y-%m-%d")
                    else:
                        end = datetime.strptime(str(year.yearp) + '-' + str(tempMonth[2]) +'-01', "%Y-%m-%d")
                    pass
            report.append(tempRemport1)

            tempRemport1=[]
            tempRemport1.append('')
            report.append(tempRemport1)

            tempRemport1=[]
            tempRemport1.append(T('Detail'))
            report.append(tempRemport1)

            tempRemport1=[]
            tempRole = []
            tempRemport1.append(T('Role'))
            if ((level_tipo=='all') or (level_tipo=='i')):
                tempRemport1.append(T('Total inserted'))
            if ((level_tipo=='all') or (level_tipo=='u')):
                tempRemport1.append(T('Total modified'))
            if ((level_tipo=='all') or (level_tipo=='d')):
                tempRemport1.append(T('Total out'))
            report.append(tempRemport1)
            #Body Level 3
            for tempR in db((db.auth_group.role!='Academic')&(db.auth_group.role!='DSI')).select():
                tempRole.append(tempR.role)
            for tempR in db((db.validate_laboratory_log.yearp==year.yearp)&(db.validate_laboratory_log.period==T(year.period.name))&(db.validate_laboratory_log.project==level_project.name)&(~db.validate_laboratory_log.roll.belongs(tempRole))).select(db.validate_laboratory_log.roll, distinct=True):
                tempRole.append(tempR.roll)
            for roll in tempRole:
                tempRemport1=[]
                tempRemport1.append(T('Rol '+str(roll)))
                if session.search_laboratory_replacing_management == "" or session.search_laboratory_replacing_management is None:
                    if ((level_tipo=='all') or (level_tipo=='i')):
                        tempRemport1.append(str(db((db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.validation_type==False)).count(db.validate_laboratory_log.id)))
                    if ((level_tipo=='all') or (level_tipo=='u')):
                        tempRemport1.append(str(db((db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.validation_type==False)).count(db.validate_laboratory_log.id)))
                    if ((level_tipo=='all') or (level_tipo=='d')):
                        tempRemport1.append(str(db((db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.validation_type==False)).count(db.validate_laboratory_log.id)))
                else:
                    if ((level_tipo=='all') or (level_tipo=='i')):
                        tempRemport1.append(str(db((db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(session.search_laboratory_replacing_management)+'%'))).count(db.validate_laboratory_log.id)))
                    if ((level_tipo=='all') or (level_tipo=='u')):
                        tempRemport1.append(str(db((db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(session.search_laboratory_replacing_management)+'%'))).count(db.validate_laboratory_log.id)))
                    if ((level_tipo=='all') or (level_tipo=='d')):
                        tempRemport1.append(str(db((db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(session.search_laboratory_replacing_management)+'%'))).count(db.validate_laboratory_log.id)))
                pass
                report.append(tempRemport1)


        #LEVEL 4
        elif request.vars['level']=='4':
            #Heading Level 4
            tempRemport1=[]
            tempRemport1.append(T('Course'))
            tempRemport1.append(level_project.name)
            report.append(tempRemport1)

            tempRemport1=[]
            tempRemport1.append(T('Month'))
            for tempMonth in vecMonth:
                if str(tempMonth[0])==level_month:
                    tempRemport1.append(tempMonth[1])
                    start = datetime.strptime(str(year.yearp) + '-' + str(tempMonth[0]) +'-01', "%Y-%m-%d")
                    if tempMonth[2]==1:
                        end = datetime.strptime(str(year.yearp+1) + '-' + str(tempMonth[2]) +'-01', "%Y-%m-%d")
                    else:
                        end = datetime.strptime(str(year.yearp) + '-' + str(tempMonth[2]) +'-01', "%Y-%m-%d")
                    pass
            report.append(tempRemport1)

            tempRemport1=[]
            tempRemport1.append(T('Role'))
            tempRemport1.append(T('Rol '+level_rol))
            report.append(tempRemport1)

            tempRemport1=[]
            tempRemport1.append('')
            report.append(tempRemport1)

            tempRemport1=[]
            tempRemport1.append(T('Detail'))
            report.append(tempRemport1)

            tempRemport1=[]
            tempUsers=[]
            tempRemport1.append(T('User'))
            if ((level_tipo=='all') or (level_tipo=='i')):
                tempRemport1.append(T('Total inserted'))
            if ((level_tipo=='all') or (level_tipo=='u')):
                tempRemport1.append(T('Total modified'))
            if ((level_tipo=='all') or (level_tipo=='d')):
                tempRemport1.append(T('Total out'))
            report.append(tempRemport1)
            #Body Level 4
            tempUsers2=[]
            registerRol = db(db.auth_group.role==level_rol).select().first()
            if ((level_rol=='Super-Administrator') or (level_rol=='Ecys-Administrator')):
                for valueU in db((db.auth_membership.group_id==registerRol.id)).select(db.auth_membership.user_id, distinct=True):
                    tempUsers.append(valueU.user_id.username)
            else:
                for valueU in db((db.auth_membership.group_id==registerRol.id)).select(db.auth_membership.user_id, distinct=True):
                    tempUsers2.append(valueU.user_id)
                for valueU in db((db.user_project.period==year.id)&(db.user_project.project==level_project.id)&(db.user_project.assigned_user.belongs(tempUsers2))).select(db.user_project.assigned_user, distinct=True):
                    tempUsers.append(valueU.assigned_user.username)
            pass
            for valueU in db((db.validate_laboratory_log.yearp==year.yearp)&(db.validate_laboratory_log.period==T(year.period.name))&(db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.roll==level_rol)&(~db.validate_laboratory_log.user_name.belongs(tempUsers))).select(db.validate_laboratory_log.user_name, distinct=True):
                tempUsers.append(valueU.user_name)
            for userr in tempUsers:
                tempRemport1=[]
                tempRemport1.append(userr)
                if session.search_laboratory_replacing_management == "" or session.search_laboratory_replacing_management is None:
                    if ((level_tipo=='all') or (level_tipo=='i')):
                        tempRemport1.append(str(db((db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.roll==level_rol)&(db.validate_laboratory_log.user_name==userr)).count(db.validate_laboratory_log.id)))
                    if ((level_tipo=='all') or (level_tipo=='u')):
                        tempRemport1.append(str(db((db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.roll==level_rol)&(db.validate_laboratory_log.user_name==userr)).count(db.validate_laboratory_log.id)))
                    if ((level_tipo=='all') or (level_tipo=='d')):
                        tempRemport1.append(str(db((db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.roll==level_rol)&(db.validate_laboratory_log.user_name==userr)).count(db.validate_laboratory_log.id)))
                else:
                    if ((level_tipo=='all') or (level_tipo=='i')):
                        tempRemport1.append(str(db((db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.roll==level_rol)&(db.validate_laboratory_log.user_name==userr)&(db.validate_laboratory_log.academic.like('%'+str(session.search_laboratory_replacing_management)+'%'))).count(db.validate_laboratory_log.id)))
                    if ((level_tipo=='all') or (level_tipo=='u')):
                        tempRemport1.append(str(db((db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.roll==level_rol)&(db.validate_laboratory_log.user_name==userr)&(db.validate_laboratory_log.academic.like('%'+str(session.search_laboratory_replacing_management)+'%'))).count(db.validate_laboratory_log.id)))
                    if ((level_tipo=='all') or (level_tipo=='d')):
                        tempRemport1.append(str(db((db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.roll==level_rol)&(db.validate_laboratory_log.user_name==userr)&(db.validate_laboratory_log.academic.like('%'+str(session.search_laboratory_replacing_management)+'%'))).count(db.validate_laboratory_log.id)))
                pass
                report.append(tempRemport1)
        

        #LEVEL 5
        elif request.vars['level']=='5':
            #Head of Level 5
            tempRemport1=[]
            tempRemport1.append(T('Course'))
            tempRemport1.append(level_project.name)
            report.append(tempRemport1)

            tempRemport1=[]
            tempRemport1.append(T('Month'))
            for tempMonth in vecMonth:
                if str(tempMonth[0])==level_month:
                    tempRemport1.append(tempMonth[1])
                    start = datetime.strptime(str(year.yearp) + '-' + str(tempMonth[0]) +'-01', "%Y-%m-%d")
                    if tempMonth[2]==1:
                        end = datetime.strptime(str(year.yearp+1) + '-' + str(tempMonth[2]) +'-01', "%Y-%m-%d")
                    else:
                        end = datetime.strptime(str(year.yearp) + '-' + str(tempMonth[2]) +'-01', "%Y-%m-%d")
                    pass
            report.append(tempRemport1)

            tempRemport1=[]
            tempRemport1.append(T('Role'))
            tempRemport1.append(T('Rol '+level_rol))
            report.append(tempRemport1)

            tempRemport1=[]
            tempRemport1.append(T('User resolution'))
            tempRemport1.append(level_user)
            report.append(tempRemport1)

            tempRemport1=[]
            tempRemport1.append('')
            report.append(tempRemport1)

            tempRemport1=[]
            tempRemport1.append(T('Detail'))
            report.append(tempRemport1)

            temp_vecAllUserRoleMonth=[]
            tempRemport1=[]
            #Body Level 5
            if session.search_laboratory_replacing_management == "" or session.search_laboratory_replacing_management is None:
                if ((level_tipo=='all') or (level_tipo=='i')):
                    temp_vecAllUserRoleMonth.append(db((db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.roll==level_rol)&(db.validate_laboratory_log.user_name==level_user)).select())
                if ((level_tipo=='all') or (level_tipo=='u')):
                    temp_vecAllUserRoleMonth.append(db((db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.roll==level_rol)&(db.validate_laboratory_log.user_name==level_user)).select())
                if ((level_tipo=='all') or (level_tipo=='d')):
                    temp_vecAllUserRoleMonth.append(db((db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.roll==level_rol)&(db.validate_laboratory_log.user_name==level_user)).select())
            else:
                if ((level_tipo=='all') or (level_tipo=='i')):
                    temp_vecAllUserRoleMonth.append(db((db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.roll==level_rol)&(db.validate_laboratory_log.user_name==level_user)&(db.validate_laboratory_log.academic.like('%'+str(session.search_laboratory_replacing_management)+'%'))).select())
                if ((level_tipo=='all') or (level_tipo=='u')):
                    temp_vecAllUserRoleMonth.append(db((db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.roll==level_rol)&(db.validate_laboratory_log.user_name==level_user)&(db.validate_laboratory_log.academic.like('%'+str(session.search_laboratory_replacing_management)+'%'))).select())
                if ((level_tipo=='all') or (level_tipo=='d')):
                    temp_vecAllUserRoleMonth.append(db((db.validate_laboratory_log.project==level_project.name)&(db.validate_laboratory_log.yearp==str(year.yearp))&(db.validate_laboratory_log.period==str(T(year.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.roll==level_rol)&(db.validate_laboratory_log.user_name==level_user)&(db.validate_laboratory_log.academic.like('%'+str(session.search_laboratory_replacing_management)+'%'))).select())
            pass
            varTypeHead=0
            for field in temp_vecAllUserRoleMonth:
                for camp in field:
                    if varTypeHead==0:
                        #Heading Level 5
                        tempRemport1=[]
                        tempRemport1.append(T('User resolution'))
                        tempRemport1.append(T('Role resolution'))
                        tempRemport1.append(T('Date of resolution'))
                        tempRemport1.append(T('Operation'))
                        tempRemport1.append(T('Description'))
                        tempRemport1.append(T('Rol Academic'))
                        tempRemport1.append(T('Before Grade'))
                        tempRemport1.append(T('Grade edited'))
                        report.append(tempRemport1)
                        varTypeHead=1
                    tempRemport1=[]
                    tempRemport1.append(str(camp.user_name))
                    tempRemport1.append(T('Rol '+str(camp.roll)))
                    tempRemport1.append(str(camp.date_log))
                    tempRemport1.append(str(camp.operation_log))
                    tempRemport1.append(str(camp.description))
                    tempRemport1.append(str(camp.academic))
                    tempRemport1.append(str(camp.before_grade))
                    tempRemport1.append(str(camp.after_grade))
                    report.append(tempRemport1)
                pass
            pass
        return dict(filename='ReporteGestionEquivalencia', csvdata=report)
    else:
        session.flash = T('Not valid Action.')
        redirect(URL('activity_control','validate_laboratory_management'))



#Management Report Equivalence laboratory levels 1 and 2
@auth.requires_login()
@auth.requires(auth.has_membership('Teacher'))
def laboratory_replacing_management():
    #Export Report to CSV
    if request.vars['list'] =='True':
        redirect(URL('activity_control','laboratory_replacing_management_export'))

    #Export Report Nivel 0
    if request.vars['list'] =='False':
        if request.vars['level'] =='1':
            redirect(URL('activity_control','laboratory_replacing_management_level_export',vars=dict(level=request.vars['level'])))
        elif request.vars['level'] =='2':
            if request.vars['level_project'] is None or request.vars['level_project']=='':
                redirect(URL('activity_control','laboratory_replacing_management'))
            else:
                redirect(URL('activity_control','laboratory_replacing_management_level_export',vars=dict(level=request.vars['level'],level_project=request.vars['level_project'])))
        else:
            redirect(URL('activity_control','laboratory_replacing_management'))


    import cpfecys
    #Obtain the current period of the system and all the register periods
    period = cpfecys.current_year_period()

    #Check if the user is assigned to the course
    assigantions = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == period.id)).select()
    if assigantions.first() is None:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))

    #Vec with the months of the current period
    vecMonth=[]
    tmpMonth=[]
    if period.period == 1:
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


        if (request.args(0) == 'search'):
            if str(request.vars['querySearch']) == "":
                session.search_laboratory_replacing_management = ""
            else:
                if str(request.vars['querySearch']).isdigit()==True:
                    session.search_laboratory_replacing_management = str(request.vars['querySearch'])
                else:
                    session.search_laboratory_replacing_management = ""
                    session.flash=T('The lookup value is not allowed.')
                    redirect(URL('activity_control','laboratory_replacing_management'))
        else:
            session.search_laboratory_replacing_management = ""

    return dict(year=period, assigantions=assigantions, vecMonth=vecMonth)



#********************************************************
#Management Report Equivalence  laboratory level 3
@auth.requires_login()
@auth.requires(auth.has_membership('Teacher'))
def laboratory_replacing_management_n2():
    import cpfecys
    #Obtain the current period of the system and all the register periods
    period = cpfecys.current_year_period()
    showLevel = True
    project = None
    tipo = None
    month=None
    vecRoleMonth=None
    messageError=''

    #Check if a search exist, verify that they are just numbers
    if session.search_laboratory_replacing_management != "" and session.search_laboratory_replacing_management is not None:
        if str(session.search_laboratory_replacing_management).isdigit()==False:
            session.search_laboratory_replacing_management = ""
            messageError=T('The lookup value is not allowed.')
            showLevel = False

    #Check the correct parameters
    if request.vars['list'] =='False':
        if request.vars['level'] =='3':
            if request.vars['level_project'] is None or request.vars['level_project']=='':
                messageError=T('Error. Unable to export the reporting level for lack of parameters.')
                showLevel = False
            else:
                if request.vars['level_month'] is None or request.vars['level_month']=='':
                    messageError=T('Error. Unable to export the reporting level for lack of parameters.')
                    showLevel = False
                else:
                    if request.vars['level_tipo'] is None or request.vars['level_tipo']=='':
                        messageError=T('Error. Unable to export the reporting level for lack of parameters.')
                        showLevel = False
                    else:
                        redirect(URL('activity_control','laboratory_replacing_management_level_export',vars=dict(level=request.vars['level'],level_project=request.vars['level_project'],level_month=request.vars['level_month'],level_tipo=request.vars['level_tipo'])))
        else:
            messageError=T('Error. Unable to export the reporting level for lack of parameters.')
            showLevel = False

    #Check if the project is correct
    if request.vars['tipo'] is None or request.vars['tipo']=='':
        messageError=T('Error. Unable to show the reporting level for lack of parameters.')
        showLevel = False
    else:
        if str(request.vars['tipo'])!='all' and str(request.vars['tipo'])!='i' and str(request.vars['tipo'])!='u' and str(request.vars['tipo'])!='d':
            messageError=T('Error. Unable to show the reporting level for lack of parameters.')
            showLevel = False
        else:
            tipo = str(request.vars['tipo'])


    #Check if the project is correct
    if request.vars['project'] is None or request.vars['project']=='':
        messageError=T('Error. Unable to show the reporting level for lack of parameters.')
        showLevel = False
    else:
        project = request.vars['project']
        project = db(db.project.id==project).select().first()
        if project is None:
            messageError=T('Action not allowed')
            showLevel = False


    #Check if the user is assigned to the project
    if project is None or tipo is None:
        messageError=T('Error. Unable to show the reporting level for lack of parameters.')
        showLevel = False
    else:
        if auth.has_membership('Teacher'):
            course = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == period.id) & (db.user_project.project==project.id)).select().first()
            if course is None:
                messageError=T('Action not allowed')
                showLevel = False
        else:
            messageError=T('Action not allowed')
            showLevel = False


    #Check if the month is correct
    if showLevel==True:
        if request.vars['month'] is None or request.vars['month']=='':
            messageError=T('Error. Unable to show the reporting level for lack of parameters.')
            showLevel = False
        else:
            if period.period == 1:
                if int(request.vars['month']) >= 1 and int(request.vars['month']) <=5:
                    month=str(request.vars['month'])
                else:
                    messageError=T('Action not allowed')
                    showLevel = False
            else:
                if int(request.vars['month']) >= 6 and int(request.vars['month']) <=12:
                    month=str(request.vars['month'])
                else:
                    messageError=T('Action not allowed')
                    showLevel = False


    #***************************************************************************************************************************************************************************************************************
    #***************************************************************************************************************************************************************************************************************
    #***************************************************************************************************************************************************************************************************************
    #***************************************************************************************************************************************************************************************************************


    #All the parameters are ok, start to build the report level 2
    if showLevel==True:
        from datetime import datetime
        start = datetime.strptime(str(period.yearp) + '-' + month +'-01', "%Y-%m-%d")
        if month=='12':
            end = datetime.strptime(str(period.yearp+1) + '-' + '01-01', "%Y-%m-%d")
        else:
            end = datetime.strptime(str(period.yearp) + '-' + str(int(month)+1) +'-01', "%Y-%m-%d")
        pass
        vecRoleMonth=[]
        roleTemp=[]
        for value in db((db.auth_group.role!='Academic')&(db.auth_group.role!='DSI')).select():
            optionSearch=[]
            optionSearch.append(value.role)
            roleTemp.append(value.role)
            if str(request.vars['tipo'])=='all' or str(request.vars['tipo'])=='i':
                if session.search_laboratory_replacing_management == "" or session.search_laboratory_replacing_management is None:
                    optionSearch.append(str(db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.yearp==str(period.yearp))&(db.validate_laboratory_log.period==str(T(period.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.roll==value.role)&(db.validate_laboratory_log.validation_type==False)).count(db.validate_laboratory_log.id)))
                else:
                    optionSearch.append(str(db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.yearp==str(period.yearp))&(db.validate_laboratory_log.period==str(T(period.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.roll==value.role)&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(session.search_laboratory_replacing_management)+'%'))).count(db.validate_laboratory_log.id)))
                pass
            if str(request.vars['tipo'])=='all' or str(request.vars['tipo'])=='u':
                if session.search_laboratory_replacing_management == "" or session.search_laboratory_replacing_management is None:
                    optionSearch.append(str(db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.yearp==str(period.yearp))&(db.validate_laboratory_log.period==str(T(period.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.roll==value.role)&(db.validate_laboratory_log.validation_type==False)).count(db.validate_laboratory_log.id)))
                else:
                    optionSearch.append(str(db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.yearp==str(period.yearp))&(db.validate_laboratory_log.period==str(T(period.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.roll==value.role)&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(session.search_laboratory_replacing_management)+'%'))).count(db.validate_laboratory_log.id)))
                pass
            if str(request.vars['tipo'])=='all' or str(request.vars['tipo'])=='d':
                if session.search_laboratory_replacing_management == "" or session.search_laboratory_replacing_management is None:
                    optionSearch.append(str(db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.yearp==str(period.yearp))&(db.validate_laboratory_log.period==str(T(period.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.roll==value.role)&(db.validate_laboratory_log.validation_type==False)).count(db.validate_laboratory_log.id)))
                else:
                    optionSearch.append(str(db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.yearp==str(period.yearp))&(db.validate_laboratory_log.period==str(T(period.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.roll==value.role)&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(session.search_laboratory_replacing_management)+'%'))).count(db.validate_laboratory_log.id)))
                pass
            vecRoleMonth.append(optionSearch)
        #Check if the log has a roll that is not register
        for value in db((db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.project==project.name)&(~db.validate_laboratory_log.roll.belongs(roleTemp))).select(db.validate_laboratory_log.roll, distinct=True):
            optionSearch=[]
            optionSearch.append(value.roll)
            if str(request.vars['tipo'])=='all' or str(request.vars['tipo'])=='i':
                if session.search_laboratory_replacing_management == "" or session.search_laboratory_replacing_management is None:
                    optionSearch.append(str(db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.yearp==str(period.yearp))&(db.validate_laboratory_log.period==str(T(period.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.roll==value.roll)&(db.validate_laboratory_log.validation_type==False)).count(db.validate_laboratory_log.id)))
                else:
                    optionSearch.append(str(db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.yearp==str(period.yearp))&(db.validate_laboratory_log.period==str(T(period.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.roll==value.roll)&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(session.search_laboratory_replacing_management)+'%'))).count(db.validate_laboratory_log.id)))
                pass
            if str(request.vars['tipo'])=='all' or str(request.vars['tipo'])=='u':
                if session.search_laboratory_replacing_management == "" or session.search_laboratory_replacing_management is None:
                    optionSearch.append(str(db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.yearp==str(period.yearp))&(db.validate_laboratory_log.period==str(T(period.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.roll==value.roll)&(db.validate_laboratory_log.validation_type==False)).count(db.validate_laboratory_log.id)))
                else:
                    optionSearch.append(str(db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.yearp==str(period.yearp))&(db.validate_laboratory_log.period==str(T(period.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.roll==value.roll)&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(session.search_laboratory_replacing_management)+'%'))).count(db.validate_laboratory_log.id)))
                pass
            if str(request.vars['tipo'])=='all' or str(request.vars['tipo'])=='d':
                if session.search_laboratory_replacing_management == "" or session.search_laboratory_replacing_management is None:
                    optionSearch.append(str(db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.yearp==str(period.yearp))&(db.validate_laboratory_log.period==str(T(period.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.roll==value.roll)&(db.validate_laboratory_log.validation_type==False)).count(db.validate_laboratory_log.id)))
                else:
                    optionSearch.append(str(db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.yearp==str(period.yearp))&(db.validate_laboratory_log.period==str(T(period.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.roll==value.roll)&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(session.search_laboratory_replacing_management)+'%'))).count(db.validate_laboratory_log.id)))
                pass
            vecRoleMonth.append(optionSearch)
    return dict(showLevel=showLevel, project=project, tipo=tipo, month=month, vecRoleMonth=vecRoleMonth, messageError=messageError)



#********************************************************
#Management Report Equivalence laboratory level 4
@auth.requires_login()
@auth.requires(auth.has_membership('Teacher'))
def laboratory_replacing_management_n3():
    import cpfecys
    #Obtain the current period of the system and all the register periods
    period = cpfecys.current_year_period()
    showLevel = True
    project = None
    tipo = None
    month=None
    roll=None
    vecUserRoleMonth=None
    messageError=''

    #Check if a search exist, verify that they are just numbers
    if session.search_laboratory_replacing_management != "" and session.search_laboratory_replacing_management is not None:
        if str(session.search_laboratory_replacing_management).isdigit()==False:
            session.search_laboratory_replacing_management = ""
            messageError=T('The lookup value is not allowed.')
            showLevel = False

    #Check the correct parameters
    if request.vars['list'] =='False':
        if request.vars['level'] =='4':
            if request.vars['level_project'] is None or request.vars['level_project']=='':
                messageError=T('Error. Unable to export the reporting level for lack of parameters.')
                showLevel = False
            else:
                if request.vars['level_month'] is None or request.vars['level_month']=='':
                    messageError=T('Error. Unable to export the reporting level for lack of parameters.')
                    showLevel = False
                else:
                    if request.vars['level_tipo'] is None or request.vars['level_tipo']=='':
                        messageError=T('Error. Unable to export the reporting level for lack of parameters.')
                        showLevel = False
                    else:
                        if request.vars['level_rol'] is None or request.vars['level_rol']=='':
                            messageError=T('Error. Unable to export the reporting level for lack of parameters.')
                            showLevel = False
                        else:
                            redirect(URL('activity_control','laboratory_replacing_management_level_export',vars=dict(level=request.vars['level'],level_project=request.vars['level_project'],level_month=request.vars['level_month'],level_tipo=request.vars['level_tipo'],level_rol=request.vars['level_rol'])))
        else:
            messageError=T('Error. Unable to export the reporting level for lack of parameters.')
            showLevel = False

    #Check if the project is correct
    if request.vars['tipo'] is None or request.vars['tipo']=='':
        messageError=T('Error. Unable to show the reporting level for lack of parameters.')
        showLevel = False
    else:
        if str(request.vars['tipo'])!='all' and str(request.vars['tipo'])!='i' and str(request.vars['tipo'])!='u' and str(request.vars['tipo'])!='d':
            messageError=T('Error. Unable to show the reporting level for lack of parameters.')
            showLevel = False
        else:
            tipo = str(request.vars['tipo'])


    #Check if the project is correct
    if request.vars['project'] is None or request.vars['project']=='':
        messageError=T('Error. Unable to show the reporting level for lack of parameters.')
        showLevel = False
    else:
        project = request.vars['project']
        project = db(db.project.id==project).select().first()
        if project is None:
            messageError=T('Action not allowed')
            showLevel = False


    #Check if the user is assigned to the project
    if project is None or tipo is None:
        messageError=T('Error. Unable to show the reporting level for lack of parameters.')
        showLevel = False
    else:
        if auth.has_membership('Teacher'):
            course = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == period.id) & (db.user_project.project==project.id)).select().first()
            if course is None:
                messageError=T('Action not allowed')
                showLevel = False
        else:
            messageError=T('Action not allowed')
            showLevel = False


    #Check if the month is correct
    if showLevel==True:
        if request.vars['month'] is None or request.vars['month']=='':
            messageError=T('Error. Unable to show the reporting level for lack of parameters.')
            showLevel = False
        else:
            if period.period == 1:
                if int(request.vars['month']) >= 1 and int(request.vars['month']) <=5:
                    month=str(request.vars['month'])
                else:
                    messageError=T('Action not allowed')
                    showLevel = False
            else:
                if int(request.vars['month']) >= 6 and int(request.vars['month']) <=12:
                    month=str(request.vars['month'])
                else:
                    messageError=T('Action not allowed')
                    showLevel = False


    #Check if the roll is correct
    if showLevel==True:
        if request.vars['roll'] is None or request.vars['roll']=='':
            messageError=T('Error. Unable to show the reporting level for lack of parameters.')
            showLevel = False
        else:
            value = db(db.auth_group.role==str(request.vars['roll'])).select().first()
            if value is None:
                #Check if the log has a roll that is not register
                value = db((db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.roll==str(request.vars['roll']))).select(db.validate_laboratory_log.roll, distinct=True).first()
                if value is None:
                    messageError=T('Action not allowed')
                    showLevel = False
                else:
                    roll=str(value.roll)
            else:
                roll=str(value.role)


    #***************************************************************************************************************************************************************************************************************
    #***************************************************************************************************************************************************************************************************************
    #***************************************************************************************************************************************************************************************************************
    #***************************************************************************************************************************************************************************************************************


    #All the parameters are ok, start to build the report level 2
    if showLevel==True:
        from datetime import datetime
        start = datetime.strptime(str(period.yearp) + '-' + month +'-01', "%Y-%m-%d")
        if month=='12':
            end = datetime.strptime(str(period.yearp+1) + '-' + '01-01', "%Y-%m-%d")
        else:
            end = datetime.strptime(str(period.yearp) + '-' + str(int(month)+1) +'-01', "%Y-%m-%d")
        pass

        #Users in the actual registers
        tempUsers=[]
        tempUsers2=[]
        registerRol = db(db.auth_group.role==roll).select().first()
        if registerRol is not None:
            if ((roll=='Super-Administrator') or (roll=='Ecys-Administrator')):
                for value in db((db.auth_membership.group_id==registerRol.id)).select(db.auth_membership.user_id, distinct=True):
                    tempUsers.append(value.user_id.username)
            else:
                for value in db((db.auth_membership.group_id==registerRol.id)).select(db.auth_membership.user_id, distinct=True):
                    tempUsers2.append(value.user_id)
                for value in db((db.user_project.period==period.id)&(db.user_project.project==project.id)&(db.user_project.assigned_user.belongs(tempUsers2))).select(db.user_project.assigned_user, distinct=True):
                    tempUsers.append(value.assigned_user.username)
            pass
        pass
        #Check if the log has an username that is not register
        for value in db((db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.roll==roll)&(~db.validate_laboratory_log.user_name.belongs(tempUsers))).select(db.validate_laboratory_log.user_name, distinct=True):
            tempUsers.append(value.user_name)
        
        vecUserRoleMonth=[]
        for value in tempUsers:
            optionSearch=[]
            optionSearch.append(value)
            if str(request.vars['tipo'])=='all' or str(request.vars['tipo'])=='i':
                if session.search_laboratory_replacing_management == "" or session.search_laboratory_replacing_management is None:
                    optionSearch.append(str(db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.yearp==str(period.yearp))&(db.validate_laboratory_log.period==str(T(period.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==value)).count(db.validate_laboratory_log.id)))
                else:
                    optionSearch.append(str(db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.yearp==str(period.yearp))&(db.validate_laboratory_log.period==str(T(period.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==value)&(db.validate_laboratory_log.academic.like('%'+str(session.search_laboratory_replacing_management)+'%'))).count(db.validate_laboratory_log.id)))
                pass
            if str(request.vars['tipo'])=='all' or str(request.vars['tipo'])=='u':
                if session.search_laboratory_replacing_management == "" or session.search_laboratory_replacing_management is None:
                    optionSearch.append(str(db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.yearp==str(period.yearp))&(db.validate_laboratory_log.period==str(T(period.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==value)).count(db.validate_laboratory_log.id)))
                else:
                    optionSearch.append(str(db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.yearp==str(period.yearp))&(db.validate_laboratory_log.period==str(T(period.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==value)&(db.validate_laboratory_log.academic.like('%'+str(session.search_laboratory_replacing_management)+'%'))).count(db.validate_laboratory_log.id)))
                pass
            if str(request.vars['tipo'])=='all' or str(request.vars['tipo'])=='d':
                if session.search_laboratory_replacing_management == "" or session.search_laboratory_replacing_management is None:
                    optionSearch.append(str(db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.yearp==str(period.yearp))&(db.validate_laboratory_log.period==str(T(period.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==value)).count(db.validate_laboratory_log.id)))
                else:
                    optionSearch.append(str(db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.yearp==str(period.yearp))&(db.validate_laboratory_log.period==str(T(period.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==value)&(db.validate_laboratory_log.academic.like('%'+str(session.search_laboratory_replacing_management)+'%'))).count(db.validate_laboratory_log.id)))
                pass
            vecUserRoleMonth.append(optionSearch)
    return dict(showLevel=showLevel, project=project, tipo=tipo, month=month, vecUserRoleMonth=vecUserRoleMonth, roll=roll, messageError=messageError)



#********************************************************
#Management Report Equivalence laboratory level 5
@auth.requires_login()
@auth.requires(auth.has_membership('Teacher'))
def laboratory_replacing_management_n4():
    import cpfecys
    #Obtain the current period of the system and all the register periods
    period = cpfecys.current_year_period()
    showLevel = True
    project = None
    tipo = None
    month=None
    roll=None
    userr=None
    vecAllUserRoleMonth=None
    messageError=''

    #Check if a search exist, verify that they are just numbers
    if session.search_laboratory_replacing_management != "" and session.search_laboratory_replacing_management is not None:
        if str(session.search_laboratory_replacing_management).isdigit()==False:
            session.search_laboratory_replacing_management = ""
            messageError=T('The lookup value is not allowed.')
            showLevel = False

    #Check the correct parameters
    if request.vars['list'] =='False':
        if request.vars['level'] =='5':
            if request.vars['level_project'] is None or request.vars['level_project']=='':
                messageError=T('Error. Unable to export the reporting level for lack of parameters.')
                showLevel = False
            else:
                if request.vars['level_month'] is None or request.vars['level_month']=='':
                    messageError=T('Error. Unable to export the reporting level for lack of parameters.')
                    showLevel = False
                else:
                    if request.vars['level_tipo'] is None or request.vars['level_tipo']=='':
                        messageError=T('Error. Unable to export the reporting level for lack of parameters.')
                        showLevel = False
                    else:
                        if request.vars['level_rol'] is None or request.vars['level_rol']=='':
                            messageError=T('Error. Unable to export the reporting level for lack of parameters.')
                            showLevel = False
                        else:
                            if request.vars['level_user'] is None or request.vars['level_user']=='':
                                messageError=T('Error. Unable to export the reporting level for lack of parameters.')
                                showLevel = False
                            else:
                                redirect(URL('activity_control','laboratory_replacing_management_level_export',vars=dict(level=request.vars['level'],level_project=request.vars['level_project'],level_month=request.vars['level_month'],level_tipo=request.vars['level_tipo'],level_rol=request.vars['level_rol'],level_user=request.vars['level_user'])))
        else:
            messageError=T('Error. Unable to export the reporting level for lack of parameters.')
            showLevel = False

    #Check if the project is correct
    if request.vars['tipo'] is None or request.vars['tipo']=='':
        messageError=T('Error. Unable to export the reporting level for lack of parameters.')
        showLevel = False
    else:
        if str(request.vars['tipo'])!='all' and str(request.vars['tipo'])!='i' and str(request.vars['tipo'])!='u' and str(request.vars['tipo'])!='d':
            messageError=T('Error. Unable to export the reporting level for lack of parameters.')
            showLevel = False
        else:
            tipo = str(request.vars['tipo'])


    #Check if the project is correct
    if request.vars['project'] is None or request.vars['project']=='':
        messageError=T('Error. Unable to export the reporting level for lack of parameters.')
        showLevel = False
    else:
        project = request.vars['project']
        project = db(db.project.id==project).select().first()
        if project is None:
            messageError=T('Action not allowed')
            showLevel = False


    #Check if the user is assigned to the project
    if project is None or tipo is None:
        messageError=T('Error. Unable to export the reporting level for lack of parameters.')
        showLevel = False
    else:
        if auth.has_membership('Teacher'):
            course = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == period.id) & (db.user_project.project==project.id)).select().first()
            if course is None:
                messageError=T('Action not allowed')
                showLevel = False
        else:
            messageError=T('Action not allowed')
            showLevel = False


    #Check if the month is correct
    if showLevel==True:
        if request.vars['month'] is None or request.vars['month']=='':
            messageError=T('Error. Unable to export the reporting level for lack of parameters.')
            showLevel = False
        else:
            if period.period == 1:
                if int(request.vars['month']) >= 1 and int(request.vars['month']) <=5:
                    month=str(request.vars['month'])
                else:
                    messageError=T('Action not allowed')
                    showLevel = False
            else:
                if int(request.vars['month']) >= 6 and int(request.vars['month']) <=12:
                    month=str(request.vars['month'])
                else:
                    messageError=T('Action not allowed')
                    showLevel = False


    #Check if the roll is correct
    if showLevel==True:
        if request.vars['roll'] is None or request.vars['roll']=='':
            messageError=T('Error. Unable to export the reporting level for lack of parameters.')
            showLevel = False
        else:
            value = db(db.auth_group.role==str(request.vars['roll'])).select().first()
            if value is None:
                #Check if the log has a roll that is not register
                value = db((db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.roll==str(request.vars['roll']))).select(db.validate_laboratory_log.roll, distinct=True).first()
                if value is None:
                    messageError=T('Action not allowed')
                    showLevel = False
                else:
                    roll=value
            else:
                roll=value.role

    #Check if the user is correct
    if showLevel==True:
        if request.vars['userr'] is None or request.vars['userr']=='':
            messageError=T('Error. Unable to export the reporting level for lack of parameters.')
            showLevel = False
        else:
            flagCheck = False
            #User Temp of auth_user where the username is equal
            userr = db(db.auth_user.username==str(request.vars['userr'])).select().first()
            if ((roll=='Super-Administrator') or (roll=='Ecys-Administrator')):
                if userr is not None:
                    #Check if the user has the rol specific
                    userrT = db(db.auth_membership.user_id==userr.id).select()
                    for tempUserCheck in userrT:
                        if tempUserCheck.group_id.role==roll:
                            flagCheck = True
            else:
                if userr is not None:
                    #Check if the user has the rol specific
                    userrT = db(db.auth_membership.user_id==userr.id).select()
                    for tempUserCheck in userrT:
                        if tempUserCheck.group_id.role==roll:
                            if db((db.user_project.period==period.id)&(db.user_project.project==project.id)&(db.user_project.assigned_user==userr.id)).select().first() is not None:
                                flagCheck = True

            if flagCheck==False:
                #Check if the log has a roll that is not register
                userr = db((db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==str(request.vars['userr']))).select().first()
                if value is None:
                    messageError=T('Action not allowed')
                    showLevel = False
                else:
                    userr=userr.user_name
            else:
                userr=userr.username


    #***************************************************************************************************************************************************************************************************************
    #***************************************************************************************************************************************************************************************************************
    #***************************************************************************************************************************************************************************************************************
    #***************************************************************************************************************************************************************************************************************


    #All the parameters are ok, start to build the report level 2
    if showLevel==True:
        from datetime import datetime
        start = datetime.strptime(str(period.yearp) + '-' + month +'-01', "%Y-%m-%d")
        if month=='12':
            end = datetime.strptime(str(period.yearp+1) + '-' + '01-01', "%Y-%m-%d")
        else:
            end = datetime.strptime(str(period.yearp) + '-' + str(int(month)+1) +'-01', "%Y-%m-%d")
        pass
        
        vecAllUserRoleMonth=[]
        if str(request.vars['tipo'])=='all' or str(request.vars['tipo'])=='i':            
            if session.search_laboratory_replacing_management == "" or session.search_laboratory_replacing_management is None:
                vecAllUserRoleMonth.append(db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.yearp==str(period.yearp))&(db.validate_laboratory_log.period==str(T(period.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==userr)).select())
            else:
                vecAllUserRoleMonth.append(db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.yearp==str(period.yearp))&(db.validate_laboratory_log.period==str(T(period.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==userr)&(db.validate_laboratory_log.academic.like('%'+str(session.search_laboratory_replacing_management)+'%'))).select())
            pass
        if str(request.vars['tipo'])=='all' or str(request.vars['tipo'])=='u':
            if session.search_laboratory_replacing_management == "" or session.search_laboratory_replacing_management is None:
                vecAllUserRoleMonth.append(db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.yearp==str(period.yearp))&(db.validate_laboratory_log.period==str(T(period.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==userr)).select())
            else:
                vecAllUserRoleMonth.append(db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.yearp==str(period.yearp))&(db.validate_laboratory_log.period==str(T(period.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==userr)&(db.validate_laboratory_log.academic.like('%'+str(session.search_laboratory_replacing_management)+'%'))).select())
            pass
        if str(request.vars['tipo'])=='all' or str(request.vars['tipo'])=='d':
            if session.search_laboratory_replacing_management == "" or session.search_laboratory_replacing_management is None:
                vecAllUserRoleMonth.append(db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.yearp==str(period.yearp))&(db.validate_laboratory_log.period==str(T(period.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==userr)).select())
            else:
                vecAllUserRoleMonth.append(db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.yearp==str(period.yearp))&(db.validate_laboratory_log.period==str(T(period.period.name)))&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==userr)&(db.validate_laboratory_log.academic.like('%'+str(session.search_laboratory_replacing_management)+'%'))).select())
            pass
    return dict(showLevel=showLevel, project=project, tipo=tipo, month=month, vecAllUserRoleMonth=vecAllUserRoleMonth, roll=roll, userr=userr, messageError=messageError)



#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
@auth.requires_login()
def control_assigned_activity():
    try:
        import time
        from datetime import date, datetime, timedelta
        officialTime = date.today()
        futureTime = officialTime + timedelta(days=1)

        year = db(db.period_year.id == request.vars['year']).select().first() 
        year_semester = year.period
        project = db(db.project.id==request.vars['project']).select().first()

        assigantion = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.project == project.id) & ((db.user_project.period <= year.id) & ((db.user_project.period + db.user_project.periods) > year.id))).select().first()

        if assigantion is None:
            assigned_to_project = False
        else:
            assigned_to_project = True
            activities = db((db.course_assigned_activity.semester==year.id)&(db.course_assigned_activity.assignation==project.id)).select()
    except:
        assigned_to_project = False

    return dict(semestre2 = year,
            project = project,
            assigned_to_project = assigned_to_project,
            activities=activities)


@auth.requires_login()
@auth.requires(auth.has_membership('Student') or auth.has_membership('Teacher'))
def management_assigned_activity():
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
        else:
            assigantion = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.project == project.id) & ((db.user_project.period <= year.id) & ((db.user_project.period + db.user_project.periods) > year.id))).select().first()
            if assigantion is None:
                session.flash = T('Not valid Action.')
                redirect(URL('default','index'))

    if auth.has_membership('Teacher'):
        db.course_assigned_activity.assignation.readable = False
        db.course_assigned_activity.assignation.writable = False
        db.course_assigned_activity.assignation.default = project.id
        db.course_assigned_activity.semester.readable = False
        db.course_assigned_activity.semester.writable = False
        db.course_assigned_activity.semester.default = year.id
        db.course_assigned_activity.fileReport.readable = False
        db.course_assigned_activity.fileReport.writable = False
        query = ((db.course_assigned_activity.semester==year.id) & (db.course_assigned_activity.assignation==project.id))
        grid = SQLFORM.grid(query, csv=False, paginate=10, searchable=False, oncreate=oncreate_assigned_activity, onupdate=onupdate_assigned_activity, ondelete=ondelete_assigned_activity)
        return dict(year = year, project = project, grid=grid)
    else:
        if request.vars['activity'] is None or request.vars['activity']=='':
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))
        else:
            activity = request.vars['activity']
            activity = db((db.course_assigned_activity.semester==year.id)&(db.course_assigned_activity.assignation==project.id)&(db.course_assigned_activity.id==activity)).select().first()
            if activity is None:
                session.flash = T('Not valid Action.')
                redirect(URL('default','index'))
            else:
                if activity.report_required==False:
                    session.flash=T('Action invalid. The activity does not require climbing a report.')
                    redirect(URL('activity_control', 'students_control', vars=dict(project = project.id, period = year.id)))

                import time
                from datetime import date
                if activity.date_start>=date.today():
                    session.flash=T('Action invalid. The activity has not yet completed.')
                    redirect(URL('activity_control', 'students_control', vars=dict(project = project.id, period = year.id)))

            upload_form = FORM(INPUT(_name='activity_id',_type='text'),
                        INPUT(_name='file_upload',_type='file',requires=[IS_UPLOAD_FILENAME(extension = '(pdf|zip)',error_message='Solo se aceptan archivos con extension zip|pdf'),IS_LENGTH(2097152,error_message='El tamaño máximo del archivo es 2MB')]))

            if upload_form.accepts(request.vars,formname='upload_form'):
                try:
                    if ( upload_form.vars.activity_id is "" ) or ( upload_form.vars.file_upload is ""):
                        response.flash = T('You must enter all fields.')
                    else:
                        #FILE UPLOAD
                        file_var = db.course_assigned_activity.fileReport.store(upload_form.vars.file_upload.file, upload_form.vars.file_upload.filename)

                        #STATUS OF ACTIVITY
                        status=T('Teacher Failed')
                        if activity.status!=T('Teacher Failed'):
                            status = T('Completed')
                            if activity.automatic_approval==False:
                                status = T('Grade pending')

                        #CHECK IF THE ACTIVITY HAS A REPORT OF HAS BEEN REPLACED THE REPORT
                        if activity.fileReport is None:
                            description_log=T('The academic tutor has recorded the activity report.')
                        else:
                            description_log=T('The academic tutor has replaced the activity report.')

                        #LOG OF ACTIVITY
                        db.course_assigned_activity_log.insert(user_name = auth.user.username,
                                                roll = 'Student',
                                                operation_log = 'update',
                                                description_log=description_log,
                                                id_course_assigned_activity=activity.id,
                                                project = project.name,
                                                period = T(year.period.name),
                                                yearp = year.yearp,
                                                before_name=activity.name,
                                                before_description=activity.description,
                                                before_report_required=activity.report_required,
                                                before_status=activity.status,
                                                before_automatic_approval=activity.automatic_approval,
                                                before_date_start=activity.date_start,
                                                before_fileReport=activity.fileReport,
                                                after_name=activity.name,
                                                after_description=activity.description,
                                                after_report_required=activity.report_required,
                                                after_status=status,
                                                after_automatic_approval=activity.automatic_approval,
                                                after_date_start=activity.date_start,
                                                after_fileReport=file_var
                                                )

                        db(db.course_assigned_activity.id==int(upload_form.vars.activity_id)).update(fileReport = file_var, status=status)
                        response.flash = T('File loaded successfully.')
                        activity = db(db.course_assigned_activity.id==int(upload_form.vars.activity_id)).select().first()
                except:
                    response.flash = T('Error loading file.')

            return dict(year = year, project = project, activity=activity)

def oncreate_assigned_activity(form):
    #Check if has one of this roles
    if auth.has_membership('Teacher')==False:
        db(db.course_assigned_activity.id==form.vars.id).delete()
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))

    #Start the process
    import cpfecys
    #Check if the period is correct
    if request.vars['year'] is None or request.vars['year']=='':
        db(db.course_assigned_activity.id==form.vars.id).delete()
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    else:
        year = request.vars['year']
        year = db(db.period_year.id==year).select().first()
        if year is None:
            db(db.course_assigned_activity.id==form.vars.id).delete()
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))
        else:
            if cpfecys.current_year_period().id != year.id:
                db(db.course_assigned_activity.id==form.vars.id).delete()
                session.flash = T('Not valid Action.')
                redirect(URL('default','index'))

    #Check if the project is correct
    if request.vars['project'] is None or request.vars['project']=='':
        db(db.course_assigned_activity.id==form.vars.id).delete()
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    else:
        project = request.vars['project']
        project = db(db.project.id==project).select().first()
        if project is None:
            db(db.course_assigned_activity.id==form.vars.id).delete()
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))
        else:
            assigantion = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.project == project) & ((db.user_project.period <= year.id) & ((db.user_project.period + db.user_project.periods) > year.id))).select().first()
            if assigantion is None:
                db(db.course_assigned_activity.id==form.vars.id).delete()
                session.flash = T('Not valid Action.')
                redirect(URL('default','index'))

    #Check the periods
    from datetime import datetime
    if period.period.id==1:
        start = datetime.strptime(str(period.yearp) + '-01-01', "%Y-%m-%d")
        end = datetime.strptime(str(period.yearp) + '-06-01', "%Y-%m-%d")
    else:
        start = datetime.strptime(str(period.yearp) + '-06-01', "%Y-%m-%d")
        end = datetime.strptime(str(period.yearp+1) + '-01-01', "%Y-%m-%d")

    #Check if the date of activity is intro the valid dates
    activityAssigned = db((db.course_assigned_activity.id==form.vars.id)&(db.course_assigned_activity.semester==period.id)&(db.course_assigned_activity.assignation==project.id)&(db.course_assigned_activity.date_start>=start)&(db.course_assigned_activity.date_start<end)).select().first()
    if activityAssigned is None:
        db(db.course_assigned_activity.id==form.vars.id).delete()
        session.flash = T('The activity date is out of this semester.')

    #Check status of activity
    import time
    from datetime import date
    tiempo = date.today()
    #STATUS OF ACTIVITY
    if activityAssigned.date_start>=tiempo:
        status=T('Pending')
        if activityAssigned.date_start==tiempo:
            status=T('Active')
        #SEND MAIL TO THE STUDENTS
        subject = T('Activity assigned by the professor')
        message = '<html>' +T('Please be advised that the Professor:')+' "'+auth.user.username+'" '+ T('has been assigned an activity that should develop.')+'<br>'
        message += T('Activity data:')+'<br>'
        message += T('Name')+': '+form.vars.name+'<br>'
        message += T('Description')+': '+form.vars.description+'<br>'
        message += T('Date')+': '+str(form.vars.date_start)+'<br>'
        if form.vars.report_required == True:
            message += T('Report Required')+': '+T('You need to enter a report of the activity to be taken as valid.')+'<br>'
        message += project.name+'<br>'+T(period.period.name)+' '+str(period.yearp)+'<br>Sistema de Seguimiento de La Escuela de Ciencias y Sistemas<br> Facultad de Ingeniería - Universidad de San Carlos de Guatemala</html>'
        #Log General del Envio
        row = db.notification_general_log4.insert(subject=subject,
                                            sent_message=message,
                                            emisor=auth.user.username,
                                            course=project.name,
                                            yearp=period.yearp,
                                            period=(period.period.name))
        ListadoCorreos=None
        email_list_log=None
        for usersT in db((db.user_project.project==project.id) & (db.user_project.assigned_user != auth.user.id) & ((db.user_project.period <= period.id) & ((db.user_project.period + db.user_project.periods) > period.id))).select():
            if ListadoCorreos is None:
                ListadoCorreos=[]
                email_list_log=usersT.assigned_user.email
            else:
                email_list_log+=','+usersT.assigned_user.email
            ListadoCorreos.append(usersT.assigned_user.email)
        if ListadoCorreos is not None:
            was_sent = mail.send(to='dtt.ecys@dtt-ecys.org',subject=subject,message=message, bcc=ListadoCorreos)
            db.mailer_log.insert(sent_message = message, destination = email_list_log, result_log = str(mail.error or '') + ':' + str(mail.result), success = was_sent, emisor=str(auth.user.username))
            #Notification LOG
            email_list =str(email_list_log).split(",")
            for email_temp in email_list:
                user_var = db((db.auth_user.email == email_temp)).select().first()
                if user_var is not None:
                    username_var = user_var.username
                else:
                    user_var = db((db.academic.email == email_temp)).select().first()
                    if user_var is not None:
                        username_var = user_var.carnet
                    else:
                        username_var = 'None'
                db.notification_log4.insert(destination = email_temp, 
                                            username = username_var,
                                            result_log = str(mail.error or '') + ':' + str(mail.result), 
                                            success = was_sent, 
                                            register=row.id)
    else:
        status = T('Completed')
        if activityAssigned.report_required==True:
            status = T('Pending') +' '+T('Item Delivery')
        else:
            if activityAssigned.automatic_approval==False:
                status = T('Grade pending')
    #LOG OF ACTIVITY
    db.course_assigned_activity_log.insert(id_course_assigned_activity = form.vars.id,
                            user_name = auth.user.username,
                            roll = 'Teacher',
                            operation_log = 'insert',
                            description_log=T('An activity is assigned to the academic tutor from the administration page of activities assigned'),
                            project = project.name,
                            period = T(year.period.name),
                            yearp = year.yearp,
                            after_name=form.vars.name,
                            after_description=form.vars.description,
                            after_report_required=form.vars.report_required,
                            after_status=status,
                            after_automatic_approval=form.vars.automatic_approval,
                            after_date_start=form.vars.date_start
                            )
    #STATUS OF ACTIVITY
    db(db.course_assigned_activity.id == form.vars.id).update(status = status)

def ondelete_assigned_activity(table_involved, id_of_the_deleted_record):
    #Check if has one of this roles
    if auth.has_membership('Teacher')==False:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))

    #Start the process
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
        else:
            assigantion = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.project == project) & ((db.user_project.period <= year.id) & ((db.user_project.period + db.user_project.periods) > year.id))).select().first()
            if assigantion is None:
                session.flash = T('Not valid Action.')
                redirect(URL('default','index'))

    #Check if the activity is correct
    course_assigned_activity_log_var = db.course_assigned_activity(id_of_the_deleted_record)

    #Check if the activity is of the course and the period
    if (course_assigned_activity_log_var is None) and (course_assigned_activity_log_var is not None and (course_assigned_activity_log_var.assignation != project.id or course_assigned_activity_log_var.semester!=year.id)):
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))

    #LOG OF ACTIVITY
    db.course_assigned_activity_log.insert(user_name = auth.user.username,
                            roll = 'Teacher',
                            operation_log = 'delete',
                            description_log=T('Activity has been removed from the site administration activities assigned'),
                            project = project.name,
                            period = T(year.period.name),
                            yearp = year.yearp,
                            before_name=course_assigned_activity_log_var.name,
                            before_description=course_assigned_activity_log_var.description,
                            before_report_required=course_assigned_activity_log_var.report_required,
                            before_status=course_assigned_activity_log_var.status,
                            before_automatic_approval=course_assigned_activity_log_var.automatic_approval,
                            before_date_start=course_assigned_activity_log_var.date_start,
                            before_fileReport=course_assigned_activity_log_var.fileReport
                            )

def onupdate_assigned_activity(form):
    failCheck=0
    messageFail=''
    #Check if has one of this roles
    if auth.has_membership('Teacher')==False:
        failCheck=2
        messageFail=T('Not valid Action.')

    #Start the process
    import cpfecys
    #Check if the period is correct
    if request.vars['year'] is None or request.vars['year']=='':
        failCheck=2
        messageFail=T('Not valid Action.')
    else:
        year = request.vars['year']
        year = db(db.period_year.id==year).select().first()
        if year is None:
            failCheck=2
            messageFail=T('Not valid Action.')
        else:
            if cpfecys.current_year_period().id != year.id:
                failCheck=2
                messageFail=T('Not valid Action.')

    #Check if the project is correct
    if request.vars['project'] is None or request.vars['project']=='':
        failCheck=2
        messageFail=T('Not valid Action.')
    else:
        project = request.vars['project']
        project = db(db.project.id==project).select().first()
        if project is None:
            failCheck=2
            messageFail=T('Not valid Action.')
        else:
            assigantion = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.project == project) & ((db.user_project.period <= year.id) & ((db.user_project.period + db.user_project.periods) > year.id))).select().first()
            if assigantion is None:
                failCheck=2
                messageFail=T('Not valid Action.')

    #LOG OF ACTIVITY
    nameA=None
    descriptionA=None
    report_requiredA=None
    statusA=None
    automatic_approvalA=None
    fileReportA=None
    date_startA=None
    idlogA=None
    projectA=None
    periodA=None
    yearpA=None
    for activityLog in db(db.course_assigned_activity_log.id_course_assigned_activity == form.vars.id).select(orderby=db.course_assigned_activity_log.id):
        nameA = activityLog.after_name
        descriptionA=activityLog.after_description
        report_requiredA=activityLog.after_report_required
        statusA=activityLog.after_status
        automatic_approvalA=activityLog.after_automatic_approval
        fileReportA=activityLog.after_fileReport
        date_startA=activityLog.after_date_start
        idlogA=activityLog.id_course_assigned_activity
        projectA=activityLog.project
        periodA=activityLog.period
        yearpA=activityLog.yearp

    #Check if the activity is of the course and the period
    if projectA!=project.name or yearpA!=str(year.yearp) and periodA!=T(year.period.name):
        failCheck=2
        messageFail=T('Not valid Action.')
        project=db(db.project.name==nameA).select().first()
        if periodA=='Primer Semestre':
            year=db((db.period_year.period==1)&(db.period_year.yearp==int(yearpA))).select().first()
        else:
            year=db((db.period_year.period==2)&(db.period_year.yearp==int(yearpA))).select().first()
    else:
        #Check the periods
        from datetime import datetime
        if period.period.id==1:
            start = datetime.strptime(str(period.yearp) + '-01-01', "%Y-%m-%d")
            end = datetime.strptime(str(period.yearp) + '-06-01', "%Y-%m-%d")
        else:
            start = datetime.strptime(str(period.yearp) + '-06-01', "%Y-%m-%d")
            end = datetime.strptime(str(period.yearp+1) + '-01-01', "%Y-%m-%d")

        #Check if the date of activity is intro the valid dates
        activityAssigned = db((db.course_assigned_activity.id==form.vars.id)&(db.course_assigned_activity.semester==period.id)&(db.course_assigned_activity.assignation==project.id)&(db.course_assigned_activity.date_start>=start)&(db.course_assigned_activity.date_start<end)).select().first()
        if activityAssigned is None:
            failCheck=1
            messageFail= T('The activity date is out of this semester.')


    #Check if has to show the message or save the log
    if failCheck >0:
        if form.vars.delete_this_record != None:
            oldActivityAssigned = db.course_assigned_activity.insert(name=nameA,
                description=descriptionA,
                report_required=report_requiredA,
                status=statusA,
                automatic_approval=automatic_approvalA,
                fileReport=fileReportA,
                date_start=date_startA,
                semester=period.id,
                assigantion=project.id
                )
            db(db.course_assigned_activity.id==oldActivityAssigned).update(id=idlogA)
        else:
            db(db.course_assigned_activity.id==idlogA).update(name=nameA,
                description=descriptionA,
                report_required=report_requiredA,
                status=statusA,
                automatic_approval=automatic_approvalA,
                fileReport=fileReportA,
                date_start=date_startA,
                semester=period.id,
                assigantion=project.id
                )

        session.flash = messageFail
        if failCheck==2:
            redirect(URL('default','index'))
    else:
        if form.vars.delete_this_record != None:
            #LOG OF ACTIVITY
            db.course_assigned_activity_log.insert(user_name = auth.user.username,
                                    roll = 'Teacher',
                                    operation_log = 'delete',
                                    description_log=T('Activity has been removed from the site administration activities assigned'),
                                    project = project.name,
                                    period = T(year.period.name),
                                    yearp = year.yearp,
                                    before_name=nameA,
                                    before_description=descriptionA,
                                    before_report_required=report_requiredA,
                                    before_status=statusA,
                                    before_automatic_approval=automatic_approvalA,
                                    before_date_start=date_startA,
                                    before_fileReport=fileReportA
                                    )
        else:
            #Check the periods
            from datetime import datetime
            if period.period.id==1:
                start = datetime.strptime(str(period.yearp) + '-01-01', "%Y-%m-%d")
                end = datetime.strptime(str(period.yearp) + '-06-01', "%Y-%m-%d")
            else:
                start = datetime.strptime(str(period.yearp) + '-06-01', "%Y-%m-%d")
                end = datetime.strptime(str(period.yearp+1) + '-01-01', "%Y-%m-%d")
            activityAssigned = db(db.course_assigned_activity.id==form.vars.id).select().first()
            if (activityAssigned.name!=nameA or activityAssigned.description!=descriptionA or activityAssigned.report_required!=report_requiredA or activityAssigned.automatic_approval!=automatic_approvalA or activityAssigned.fileReport!=fileReportA or activityAssigned.date_start!=date_startA):
                import time
                from datetime import date
                tiempo = date.today()
                #STATUS OF ACTIVITY
                status = activityAssigned.status
                if activityAssigned.date_start>=tiempo:
                    status=T('Pending')
                    if activityAssigned.date_start==tiempo:
                        status=T('Active')
                    #REPORT OF ACTIVITY
                    db(db.course_assigned_activity.id == form.vars.id).update(fileReport = None)
                else:
                    if activityAssigned.report_required==False and report_requiredA==True:
                        db(db.course_assigned_activity.id == form.vars.id).update(fileReport = None)
                    status = activityAssigned.status
                    if activityAssigned.status!=T('Teacher Failed'):
                        if activityAssigned.status==T('Accomplished'):
                            if activityAssigned.report_required==True and activityAssigned.fileReport is None:
                                status = T('Pending') +' '+T('Item Delivery')
                        else:
                            if activityAssigned.report_required==True:
                                if activityAssigned.fileReport is None:
                                    status = T('Pending') +' '+T('Item Delivery')
                                else:
                                    if activityAssigned.automatic_approval == False:
                                        status = T('Grade pending')
                                    else:
                                        status = T('Accomplished')
                            else:
                                if activityAssigned.automatic_approval == False:
                                    status = T('Grade pending')
                                else:
                                    status = T('Accomplished')
                
                #STATUS OF ACTIVITY
                db(db.course_assigned_activity.id == form.vars.id).update(status = status)

                #LOG OF ACTIVITY
                db.course_assigned_activity_log.insert(user_name = auth.user.username,
                                        roll = 'Teacher',
                                        operation_log = 'update',
                                        description_log=T('Updated the activity from the site administration activities assigned'),
                                        id_course_assigned_activity=form.vars.id,
                                        project = project.name,
                                        period = T(year.period.name),
                                        yearp = year.yearp,
                                        before_name=nameA,
                                        before_description=descriptionA,
                                        before_report_required=report_requiredA,
                                        before_status=statusA,
                                        before_automatic_approval=automatic_approvalA,
                                        before_date_start=date_startA,
                                        before_fileReport=fileReportA,
                                        after_name=form.vars.name,
                                        after_description=form.vars.description,
                                        after_report_required=form.vars.report_required,
                                        after_status=status,
                                        after_automatic_approval=form.vars.automatic_approval,
                                        after_date_start=form.vars.date_start,
                                        after_fileReport=fileReportA
                                        )


@auth.requires_login()
@auth.requires_membership('Teacher')
def rate_assigned_activity():
    try:
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
            else:
                assigantion = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.project == project.id) & ((db.user_project.period <= year.id) & ((db.user_project.period + db.user_project.periods) > year.id))).select().first()
                if assigantion is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))

        #Check if the activity is valid or the operation on the activity is valid
        if request.vars['activity'] is None or request.vars['activity']=='' or request.vars['op'] is None or request.vars['op']=='' or (request.vars['op']!='1' and request.vars['op']!='2'):
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        activity = db((db.course_assigned_activity.semester==year.id)&(db.course_assigned_activity.assignation==project.id)&(db.course_assigned_activity.id==request.vars['activity'])).select().first()
        if activity is None:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))
    except:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))

    if activity.status==T('Pending') or activity.status==T('Active'):
        session.flash=T('Action invalid. The activity has not yet completed.')
        redirect(URL('activity_control', 'students_control.html', vars=dict(project = project.id, period = year.id)))

    if request.vars['op']=='2':
        status = T('Teacher Failed')
    else:
        status = T('Accomplished')
        if activity.report_required==True:
            if activity.fileReport is None:
                status = T('Pending') +' '+T('Item Delivery')
    db(db.course_assigned_activity.id == activity.id).update(status = status)
    session.flash=T('Qualified Activity')
    redirect(URL('activity_control', 'students_control', vars=dict(project = project.id, period = year.id)))
