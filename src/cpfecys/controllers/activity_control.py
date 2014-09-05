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
def student_control_period():
    import cpfecys
    year = cpfecys.current_year_period()
    year_semester = db.period(id=year.period)

    query = db.student_control_period
    db.student_control_period.period_name.default = T(str(year_semester.name)) +" " + str(year.yearp)
    db.student_control_period.period_name.writable = False
    
    date1 = None
    date2 = None
    if year_semester.id==1:
        dateInicial = db.executesql('SELECT date(\''+str(year.yearp)+'-01-01\');',as_dict=True)
        for d0 in dateInicial:
            date1=d0['date(\''+str(year.yearp)+'-01-01\')']
        dateEnd = db.executesql('SELECT date(\''+str(year.yearp)+'-05-31\');',as_dict=True)
        for d0 in dateEnd:
            date2=d0['date(\''+str(year.yearp)+'-05-31\')']
    else:
        dateInicial = db.executesql('SELECT date(\''+str(year.yearp)+'-07-01\');',as_dict=True)
        for d0 in dateInicial:
            date1=d0['date(\''+str(year.yearp)+'-07-01\')']

        dateEnd = db.executesql('SELECT date(\''+str(year.yearp)+'-11-30\');',as_dict=True)
        for d1 in dateEnd:
            date2=d1['date(\''+str(year.yearp)+'-11-30\')']
    db.student_control_period.date_finish_semester.default = date2
    db.student_control_period.date_start_semester.default = date1
    db.student_control_period.date_start_semester.writable=False
    db.student_control_period.date_finish_semester.writable=False
    grid = SQLFORM.grid(query, maxtextlength=100,csv=False)
    return dict(grid=grid)

@auth.requires_login()
@auth.requires(auth.has_membership('Student') or auth.has_membership('Teacher'))
def courses_list():
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
@auth.requires(auth.has_membership('Student') or auth.has_membership('Teacher') or auth.has_membership('Super-Administrator'))
def students_control():
    import cpfecys
    #Obtener la asignacion del estudiante
    assignation = request.vars['assignation']
    #Obtener al tutor del proyecto
    year = cpfecys.current_year_period().id
    check = db.user_project(id = assignation, assigned_user = auth.user.id)
    if (check is None):
        #check if there is no assignation or if it is locked (shouldn't be touched)
        if (session.last_assignation is None):
            return dict(project = request.vars['project'], year = year)
        else:
            check = db.user_project(id = session.last_assignation)
            if cpfecys.assignation_is_locked(check):
                redirect(URL('default','index'))
                return
    else:
        session.last_assignation = check.id

    #year = db.period_year(id=check.period)
    #year_semester = db.period(id=year.period)

    return dict(project = request.vars['project'], year = year)

@auth.requires_login()
def control_weighting():
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

@auth.requires_login()
def students_control_full():
    import cpfecys
    #Obtener la asignacion del estudiante
    assignation = request.vars['assignation']
    project = request.vars['project']
    
    year = db(db.period_year.id == request.vars['year']).select().first() 
    
    
    return dict(name = '',
                semester = year.period.name,
                year = year.yearp,
                assignation=assignation)

@auth.requires_login()
def control_students_modals():
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

@auth.requires_login()
def weighting():
    import cpfecys
    #Obtener la asignacion del estudiante
    assignation = request.vars['assignation']
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

    print "entro yearp++ +" + str(request.vars['year'])
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