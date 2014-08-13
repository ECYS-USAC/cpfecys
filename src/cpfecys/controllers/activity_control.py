@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def activity_category():
    query = db.activity_category
    grid = SQLFORM.grid(query, maxtextlength=100,csv=False)
    return dict(grid=grid)

@auth.requires_login()
@auth.requires_membership('Student')
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
@auth.requires_membership('Student')
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
    return dict(name = check.project.name,)

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
                assignation=assignation)

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
    return dict(name='hola')
