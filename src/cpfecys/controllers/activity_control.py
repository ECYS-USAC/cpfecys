@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def activity_category():
    query = db.activity_category
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
@auth.requires(auth.has_membership('Student') or auth.has_membership('Teacher'))
def students_control():
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

    query = db.activity_category
    grid = SQLFORM.grid(query, maxtextlength=100,csv=False)
    return dict(name = check.project.name)

def control_weighting():
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
                year = year.yearp,
                assignation=assignation,
                semestre2 = year)

def students_control_full():
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
                year = year.yearp,
                assignation=assignation)

def control_students_modals():
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
    return dict(semestre2 = year, name=check.project.name)

def weighting():
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
    return dict(semestre2 = year)






#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
def control_activity():
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
                year = year.yearp,
                assignation=check,
                semestre2 = year)


def activity():
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
    return dict(semestre2 = year)

def control_students_modals2():
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