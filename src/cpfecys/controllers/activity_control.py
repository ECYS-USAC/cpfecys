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
    if auth.has_membership('Super-Administrator') == False and auth.has_membership('Ecys-Administrator') == False :
        assigantion = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == year.id) & (db.user_project.project == project_var)).select().first()
        
        if assigantion is None:
            academic_var = db(db.academic.carnet==auth.user.username).select().first()
            try:
                academic_assig = db((db.academic_course_assignation.carnet == academic_var.id) & (db.academic_course_assignation.semester == year.id) & (db.academic_course_assignation.assignation==project_var) ).select().first()
            
                if academic_assig is None:
                    session.flash=T('You do not have permission to view course requests')
                    redirect(URL('default','index'))
            except:
                session.flash=T('You do not have permission to view course requests')
                redirect(URL('default','index'))
        
    return dict(project = project_var, year = year.id)



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

    return dict(academic_assig=academic_assig, var_period=var_period, var_activity=var_activity, var_project=var_project)


@auth.requires_login()
@auth.requires(auth.has_membership('Student') or auth.has_membership('Teacher') or auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
def grades():
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

    if var_activity.laboratory == True:
        academic_assig =  db((db.academic_course_assignation.assignation==id_project) & (db.academic_course_assignation.semester==id_year) &  (db.academic_course_assignation.laboratorio==True)).select()
    else:
        academic_assig =  db((db.academic_course_assignation.assignation==id_project) & (db.academic_course_assignation.semester==id_year)).select()


    return dict(academic_assig=academic_assig, var_period=var_period, var_activity=var_activity, var_project=var_project)





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
@auth.requires(auth.has_membership('Super-Administrator'))
def admin_areas_list():
    areas = db(db.area_level).select()
    role = request.vars['role']
    response.view='activity_control/admin_areas_list.html'
    return dict(areas=areas, role=role)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def admin_courses_list():
    #Obtain the current period of the system and all the register periods
    period = cpfecys.current_year_period()
    periods = db(db.period_year).select()
    area = None
    role = None

    #Check if the period is change
    #Obtain the select period
    if request.vars['period'] != None:
        period = request.vars['period']
        area = request.vars['areas']
        period = db(db.period_year.id==period).select().first()
        if not period:
            session.flash = T('Not valid Action.')
            redirect(URL('default', 'index'))

    if request.vars['area'] != None:
        area = request.vars['area']        
        response.view = 'activity_control/admin_courses_list.html'
        projects = db(db.project.area_level==area).select()

        return dict(projects=projects,area=area,periods =periods)
    else:
        session.flash = T("Action not allowed")
        redirect(URL('default','index'))

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
                    response.flash = T("Request has been sent")
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
            change = db((db.request_change_weighting.period == year.id) & (db.request_change_weighting.project == project_id) & ((db.request_change_weighting.status != 'accepted') & (db.request_change_weighting.status != 'rejected'))).select().first()
            if change is None:
                change = db.request_change_weighting.insert(user_id=auth.user.id,
                                                            roll='Student',
                                                            status='edit',
                                                            period=year.id,
                                                            project=project_id)
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
                    session.flash=T('You do not have permission to view course requests')
                    redirect(URL('default','index'))
            except:
                session.flash=T('You do not have permission to view course requests')
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
   
    year = db(db.period_year.id == request.vars['year']).select().first() 
    assigantion = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == year.id) & (db.user_project.project == project)).select().first()
    return dict(semestre2 = year, project = project, assigantion=assigantion, rol_log = rol_log)



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
    return dict(semestre2 = year, name=project_var.name)

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
                nameP=None
                nameS=None
                try:
                    (nameP, projectSection) = str(Rejected.course.name).split('(')
                    (nameS,garbage) = str(projectSection).split(')')
                    (garbage,nameS) = str(nameS).split(' ')
                except:
                    nameP=project.name
                idR = db.requestchange_activity_log.insert(user_request=Rejected.user_id.username, roll_request=Rejected.roll, status='Rejected', user_resolve=Rejected.user_resolve.username, roll_resolve=Rejected.roll_resolve, description=Rejected.description, date_request=Rejected.date_request, date_request_resolve=Rejected.date_request_resolve, category_request=Rejected.course_activity_category.category.category, semester=Rejected.semester.period.name, yearp=Rejected.semester.yearp, course=nameP, course_section=nameS)
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
                nameP=None
                nameS=None
                try:
                    (nameP, projectSection) = str(project.name).split('(')
                    (nameS,garbage) = str(projectSection).split(')')
                    (garbage,nameS) = str(nameS).split(' ')
                except:
                    nameP=project.name
                idR = db.requestchange_activity_log.insert(user_request=Draft.user_id.username, roll_request='Student', status='Pending', description=request.vars['activity_description_request_var'], date_request=Draft.date_request, category_request=Draft.course_activity_category.category.category, semester=year.period.name, yearp=year.yearp, course=nameP, course_section=nameS)
                activitiesChange = db(db.requestchange_course_activity.requestchange_activity==Draft.id).select()
                for actChange in activitiesChange:
                    db.requestchange_course_activity_log.insert(requestchange_activity=idR, operation_request=actChange.operation_request, activity=actChange.activity, name=actChange.name, description=actChange.description, grade=actChange.grade, date_start=actChange.date_start, date_finish=actChange.date_finish)
                #Check the user project
                check = db.user_project(project = request.vars['project'], period = request.vars['year'], assigned_user = auth.user.id)
                #Message
                users2 = db((db.auth_user.id==db.user_project.assigned_user)&(db.user_project.period == check.period) & (db.user_project.project==check.project)&(db.auth_membership.user_id==db.user_project.assigned_user)&(db.auth_membership.group_id==3)).select().first()
                subject="Solicitud de cambio de actividades - "+project.name
                
                message2="<br>Por este medio se le informa que el(la) practicante "+check.assigned_user.first_name+" "+check.assigned_user.last_name+" ha creado una solicitud de cambio de actividades en la categoría \""+Draft.course_activity_category.category.category+"\" dentro de la ponderación de laboratorio del Curso de \""+project.name+"\"."
                message2=message2+"<br>Para aceptar o rechazar dicha solicitud dirigirse al control de solicitudes o al siguiente link: "
                message2=message2+"<br>Saludos.<br><br>Sistema de Seguimiento de La Escuela de Ciencias y Sistemas<br>Facultad de Ingeniería - Universidad de San Carlos de Guatemala</html>"

                #Send Mail to the Teacher
                message="<html>catedratico(a) "+users2.auth_user.first_name+" "+users2.auth_user.last_name+" reciba un cordial saludo.<br>"
                message3=message+message2
                fail1 = send_mail_to_students(message3,subject,users2.auth_user.email,check,year.period.name,year.yearp)
                fail1=1
                #Send Mail to the DTT Administrator
                message="<html>Administrator de DTT reciba un cordial saludo.<br>"
                message3=message+message2
                fail2 = send_mail_to_students(message3,subject,'dtt.ecys@dtt-ecys.org',check,year.period.name,year.yearp)
                fail2=1
                #Refresh the var Draft
                Draft=None
                if fail1==1 and fail2==1:
                    stateRequest=1
                elif fail1==1:
                    stateRequest=2
                elif fail2==1:
                    stateRequest=3
                else:
                    stateRequest=4


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
                nameP=None
                nameS=None
                try:
                    (nameP, projectSection) = str(Rejected.course.name).split('(')
                    (nameS,garbage) = str(projectSection).split(')')
                    (garbage,nameS) = str(nameS).split(' ')
                except:
                    nameP=project.name
                idR = db.requestchange_activity_log.insert(user_request=Rejected.user_id.username, roll_request=Rejected.roll, status='Rejected', user_resolve=Rejected.user_resolve.username, roll_resolve=Rejected.roll_resolve, description=Rejected.description, date_request=Rejected.date_request, date_request_resolve=Rejected.date_request_resolve, category_request=Rejected.course_activity_category.category.category, semester=Rejected.semester.period.name, yearp=Rejected.semester.yearp, course=nameP, course_section=nameS)
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
                nameP=None
                nameS=None
                try:
                    (nameP, projectSection) = str(Accepted.course.name).split('(')
                    (nameS,garbage) = str(projectSection).split(')')
                    (garbage,nameS) = str(nameS).split(' ')
                except:
                    nameP=Accepted.course.name
                idR = db.requestchange_activity_log.insert(user_request=Accepted.user_id.username, roll_request=Accepted.roll, status='Accepted', user_resolve=Accepted.user_resolve.username, roll_resolve=Accepted.roll_resolve, description=Accepted.description, date_request=Accepted.date_request, date_request_resolve=Accepted.date_request_resolve, category_request=Accepted.course_activity_category.category.category, semester=Accepted.semester.period.name, yearp=Accepted.semester.yearp, course=nameP, course_section=nameS)
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



#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------


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
        if year is None:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

    project_var = project_var.id
    if auth.has_membership('Super-Administrator') == False:
        assigantion = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == year.id) & (db.user_project.project == project_var)).select().first()
        if assigantion is None:
            academic_var = db(db.academic.carnet==auth.user.username).select().first()
            try:
                academic_assig = db((db.academic_course_assignation.carnet == academic_var.id) & (db.academic_course_assignation.semester == year.id) & (db.academic_course_assignation.assignation==project_var) ).select().first()
                if academic_assig is None:
                    session.flash=T('You do not have permission to view course requests')
                    redirect(URL('default','index'))
            except:
                session.flash=T('You do not have permission to view course requests')
                redirect(URL('default','index'))

    
    teacher = db((db.user_project.period == year.id) & (db.user_project.project == project_var)).select().first()
    practice = db((db.user_project.period == year.id) & (db.user_project.project == project_var)).select()
    students = db((db.academic_course_assignation.semester == year.id) & (db.academic_course_assignation.assignation==project_var) ).select()
        
    return dict(project = project_var, year = year.id, teacher=teacher, practice=practice, students=students)
