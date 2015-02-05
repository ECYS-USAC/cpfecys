@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def audit_academic():    

    db.academic_log.id_period.readable = False
    db.academic_log.id_academic.readable = False

    query = ((db.academic_log))       
    grid = SQLFORM.grid(query, exportclasses = None, orderby=db.academic_log.date_log, deletable=False, editable=False, create=False, maxtextlength={'academic_log.description' : 256})
    return dict(grid=grid )


@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def audit_academic_assignation_areas():    
    areas = db(db.area_level).select()
    role = request.vars['role']
    response.view='audit/audit_academic_assignation_areas.html'
    return dict(areas=areas, role=role)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def audit_academic_assignation_courses_list():
#db.user_project.assigned_user == auth.user.id
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
        response.view = 'audit/audit_academic_assignation_courses_list.html'
        projects = db(db.project.area_level==area).select()

        return dict(projects=projects,area=area)
    else:
        session.flash = "Action not allowed"
        redirect(URL('default','index'))

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def audit_academic_assignation():
#db.user_project.assigned_user == auth.user.id
    #Obtain the current period of the system and all the register periods
    period = cpfecys.current_year_period()
    periods = db(db.period_year).select()
 

    #Check if the period is change
    #Obtain the select period
    if request.vars['period'] != None:
        period = request.vars['period']
        project = request.vars['project']
        period = db(db.period_year.id==period).select().first()
        if not period:
            session.flash = T('Not valid Action.')
            redirect(URL('default', 'index'))

    if request.vars['project'] == None:
        if session.project_var == None:
            session.flash = T('Not valid Action.')
            redirect(URL('default', 'index'))
        else:
            project = session.project_var
    else:
        project = request.vars['project'];
        session.project_var = project


    if request.vars['area'] == None:
        if session.area_var == None:
            session.flash = T('Not valid Action.')
            redirect(URL('default', 'index'))
        else:
            area = session.area_var
    else:
        area = request.vars['area'];
        session.area_var = area
    
    #Search name project
    name_project = ''
    project_result = db(db.project.id == project).select()
    for a in project_result:
        name_project = a.name

    
    db.academic_course_assignation_log.before_course.readable = False
    db.academic_course_assignation_log.after_course.readable = False
    db.academic_course_assignation_log.before_year.readable = False
    db.academic_course_assignation_log.after_year.readable = False
    db.academic_course_assignation_log.before_semester.readable = False
    db.academic_course_assignation_log.after_semester.readable = False
    db.academic_course_assignation_log.id_period.readable = False
    db.academic_course_assignation_log.id_academic_course_assignation.readable = False


    query = ((db.academic_course_assignation_log.id_period==period) & ((db.academic_course_assignation_log.after_course ==name_project) | (db.academic_course_assignation_log.before_course ==name_project) ))       
    grid = SQLFORM.grid(query,  deletable=False, editable=False, create=False, details=False, maxtextlength={'academic_course_assignation_log.description' : 256}, csv=False)
    return dict(grid=grid , project=project,  periods= periods, period=period,  area=area)




@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def audit_register_mail_notifications_detail():
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
    response.view='audit/audit_register_mail_notifications_detail.html'

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
    query = ((db.notification_log4.register==notice)&(db.notification_general_log4.id==db.notification_log4.register))
    grid = SQLFORM.grid(query, deletable=False, editable=False, create=False, paginate=10, details=False, maxtextlength={'notification_log4.result_log' : 256},csv=False)
    
    return dict(subject=asunto, grid=grid, notice=notice)



@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def audit_register_mail_notifications():
    period = cpfecys.current_year_period()
    if request.vars['period'] != None:
        period = request.vars['period']
        area = request.vars['area']
        period = db(db.period_year.id==period).select().first()
        if not period:
            session.flash = T('Not valid Action.')
            redirect(URL('default', 'index'))

    user = request.vars['user']
    if user == None:
        session.flash = T('Not valid Action.')
        redirect(URL('default', 'index'))

    def obtain_nameProject(user):
        student = db((db.user_project.id==user)).select()
        project =''
        for s in student:
            project = s
        return project

    def obtain_period(periodo):
        semester = db(db.period.id==periodo).select()
        nameS = ''
        for s in semester:
            nameS=s.name
        return nameS

    #obtain all the registers of the send notices of the student
    def obtain_notices(user):
        #name project
        n=obtain_nameProject(user)
        return db((db.notification_general_log4.emisor==n.assigned_user.username) & (db.notification_general_log4.course==n.project.name)&(db.notification_general_log4.period==period.period.name)&(db.notification_general_log4.yearp==period.yearp)).select()

    return dict(user=user, obtain_nameProject=obtain_nameProject, obtain_notices=obtain_notices)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def audit_teacher_mail_notifications_courses_list():
#db.user_project.assigned_user == auth.user.id
    #Obtain the current period of the system and all the register periods
    period = cpfecys.current_year_period()
    periods = db(db.period_year).select()
    area = None

    #Check if the period is change
    #Obtain the select period
    if request.vars['period'] != None:
        period = request.vars['period']
        area = request.vars['area']
        period = db(db.period_year.id==period).select().first()
        if not period:
            session.flash = T('Not valid Action.')
            redirect(URL('default', 'index'))

    if request.vars['area'] != None:
        area = request.vars['area']
        response.view = 'audit/audit_teacher_mail_notifications_courses_list.html'
        projects = db(db.project.area_level==area).select()

        #Obtain all the teachers that has register in the system in the select period
        def current_teacher(project):
            students = db((db.user_project.project==project)&((db.user_project.period <= period) & ((db.user_project.period + db.user_project.periods) > period))&(db.auth_membership.user_id==db.user_project.assigned_user)&(db.auth_membership.group_id==3)).select()
            return students

        #Functions that ar use to obtain the notices
        def total_notices(project):
            return db((db.notification_general_log4.emisor==project.assigned_user.username) & (db.notification_general_log4.course==project.project.name)&(db.notification_general_log4.period==period.period.name)&(db.notification_general_log4.yearp==period.yearp)).count()
        return dict(projects=projects, periods=periods, area=area, current_teacher=current_teacher, total_notices=total_notices, periodA=period)
    else:
        session.flash = "Action not allowed"
        redirect(URL('default','index'))

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def audit_teacher_mail_notifications_areas():    
    areas = db(db.area_level).select()
    response.view='audit/audit_teacher_mail_notifications_areas.html'
    return dict(areas=areas)




@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def audit_student_mail_notifications_courses_list():
#db.user_project.assigned_user == auth.user.id
    #Obtain the current period of the system and all the register periods
    period = cpfecys.current_year_period()
    periods = db(db.period_year).select()
    area = None

    #Check if the period is change
    #Obtain the select period
    if request.vars['period'] != None:
        period = request.vars['period']
        area = request.vars['area']
        period = db(db.period_year.id==period).select().first()
        if not period:
            session.flash = T('Not valid Action.')
            redirect(URL('default', 'index'))

    if request.vars['area'] != None:
        area = request.vars['area']
        response.view = 'audit/audit_student_mail_notifications_courses_list.html'
        projects = db(db.project.area_level==area).select()

        #Obtain all the practising that has register in the system in the select period
        def current_practising(project):
            students = db((db.user_project.project==project)&((db.user_project.period <= period) & ((db.user_project.period + db.user_project.periods) > period))&(db.auth_membership.user_id==db.user_project.assigned_user)&(db.auth_membership.group_id==2)).select()
            return students

        #Functions that ar use to obtain the notices
        def total_notices(project):
            return db((db.notification_general_log4.emisor==project.assigned_user.username) & (db.notification_general_log4.course==project.project.name)&(db.notification_general_log4.period==period.period.name)&(db.notification_general_log4.yearp==period.yearp)).count()

        return dict(projects=projects, periods=periods, area=area, current_practising=current_practising, total_notices=total_notices, periodA=period)
    else:
        session.flash = "Action not allowed"
        redirect(URL('default','index'))

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def audit_student_mail_notifications_areas():    
    areas = db(db.area_level).select()
    response.view='audit/audit_student_mail_notifications_areas.html'
    return dict(areas=areas)