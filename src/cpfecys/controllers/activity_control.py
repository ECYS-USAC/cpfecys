@auth.requires_login()
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
            #session.flash=str(coursesStudent)
            #redirect(URL('default','index'))
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

    academic_assig =  db((db.academic_course_assignation.assignation==id_project) & (db.academic_course_assignation.semester==id_year) &  (db.academic_course_assignation.laboratorio==var_activity.laboratory)).select()

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

    academic_assig =  db((db.academic_course_assignation.assignation==id_project) & (db.academic_course_assignation.semester==id_year) &  (db.academic_course_assignation.laboratorio==var_activity.laboratory)).select()

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
        session.flash = "Action not allowed"
        redirect(URL('default','index'))


@auth.requires_login()
@auth.requires(auth.has_membership('Student') or auth.has_membership('Teacher') or auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
def students_control():
    import cpfecys
    year = cpfecys.current_year_period().id
    project_var = request.vars['project']
    if auth.has_membership('Super-Administrator') == False and auth.has_membership('Ecys-Administrator'):
        assigantion = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == year) & (db.user_project.project == project_var)).select().first()
        
        if assigantion is None:
            academic_var = db(db.academic.carnet==auth.user.username).select().first()
            try:
                academic_assig = db((db.academic_course_assignation.carnet == academic_var.id) & (db.academic_course_assignation.semester == year) & (db.academic_course_assignation.assignation==project_var) ).select().first()
            
                if academic_assig is None:
                    session.flash=T('You do not have permission to view course requests')
                    redirect(URL('default','index'))
            except:
                session.flash=T('You do not have permission to view course requests')
                redirect(URL('default','index'))
        
    return dict(project = project_var, year = year)

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
    
    year = db(db.period_year.id == request.vars['year']).select().first() 

    project_var = request.vars['project']
    if auth.has_membership('Super-Administrator') == False and auth.has_membership('Ecys-Administrator'):
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
                year = year.yearp)

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
   
    year = db(db.period_year.id == request.vars['year']).select().first() 
    
    return dict(semestre2 = year, project = project)






#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
def control_activity():
    import cpfecys
    #Obtener la asignacion del estudiante
    assignation = request.vars['assignation']
    
    year = db(db.period_year.id == request.vars['year']).select().first() 
    year_semester = year.period
    
    if assignation == 'None':
        check = db(db.project.id == request.vars['project']).select().first()
        return dict(name = check.name,
            semester = year_semester.name,
            year = year.yearp,
            assignation=assignation,
            semestre2 = year,
            project = request.vars['project'])
    else:
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
        
        return dict(name = check.project.name,
                    semester = year_semester.name,
                    year = year.yearp,
                    assignation=assignation,
                    semestre2 = year)

def activity():
    import cpfecys
    #Obtener la asignacion del estudiante
    assignation = request.vars['assignation']
    project = request.vars['project']
    
    year = db(db.period_year.id == request.vars['year']).select().first() 
    
    return dict(semestre2 = year, project = project)


def control_students_modals2():
    import cpfecys
    #Obtener la asignacion del estudiante
    assignation = request.vars['assignation']
    project = request.vars['project']
    
    year = db(db.period_year.id == request.vars['year']).select().first() 

    
    if (assignation == 'None'):
        project_var = db(db.project.id == request.vars['project']).select().first() 
        return dict(semestre2 = year, name=project_var.name)
    else:
        check = db.user_project(id = assignation, assigned_user = auth.user.id)
        return dict(semestre2 = year, name=check.project.name)


def request_change_activity():
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

    return dict(name = check.project.name,
                semester = year_semester.name,
                semestre2 = year,
                year = year.yearp,
                assignation=assignation)



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

    return dict(courses_request = courses_request, split_name=split_name, split_section=split_section)


@auth.requires_login()
@auth.requires(auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator') or auth.has_membership('Teacher'))
def solve_request_change_activity():
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
def activityRequest():
    import cpfecys
    currentyear_period = cpfecys.current_year_period()
    return dict(semestre2 = currentyear_period)
