#*************************************************************************************************************************************
#*************************************************************************************************************************************
#*****************************************************FEATURES EXTRAS FOR REPORTS*****************************************************
#???????????????????????????????????????????????????????????
#VALIDATE REPORT
@auth.requires_login()
@auth.requires(auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
def GET_MONTH_PERIOD(year):
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
    return vecMonth


@auth.requires_login()
@auth.requires(auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
def VALIDATE_MONTH(month, period):
    from datetime import datetime
    vecMonth=None
    if month is not None:
        if period.period == 1:
            if int(month) == 1:
                vecMonth=[]
                vecMonth.append('Enero')
                vecMonth.append(datetime.strptime(str(period.yearp) + '-' + month +'-01', "%Y-%m-%d"))
                vecMonth.append(datetime.strptime(str(period.yearp) + '-' + str(int(month)+1) +'-01', "%Y-%m-%d"))
            elif int(month) == 2:
                vecMonth=[]
                vecMonth.append('Febrero')
                vecMonth.append(datetime.strptime(str(period.yearp) + '-' + month +'-01', "%Y-%m-%d"))
                vecMonth.append(datetime.strptime(str(period.yearp) + '-' + str(int(month)+1) +'-01', "%Y-%m-%d"))
            elif int(month) == 3:
                vecMonth=[]
                vecMonth.append('Marzo')
                vecMonth.append(datetime.strptime(str(period.yearp) + '-' + month +'-01', "%Y-%m-%d"))
                vecMonth.append(datetime.strptime(str(period.yearp) + '-' + str(int(month)+1) +'-01', "%Y-%m-%d"))
            elif int(month) == 4:
                vecMonth=[]
                vecMonth.append('Abril')
                vecMonth.append(datetime.strptime(str(period.yearp) + '-' + month +'-01', "%Y-%m-%d"))
                vecMonth.append(datetime.strptime(str(period.yearp) + '-' + str(int(month)+1) +'-01', "%Y-%m-%d"))
            elif int(month) == 5:
                vecMonth=[]
                vecMonth.append('Mayo')
                vecMonth.append(datetime.strptime(str(period.yearp) + '-' + month +'-01', "%Y-%m-%d"))
                vecMonth.append(datetime.strptime(str(period.yearp) + '-' + str(int(month)+1) +'-01', "%Y-%m-%d"))
        else:
            if int(month) == 6:
                vecMonth=[]
                vecMonth.append('Junio')
                vecMonth.append(datetime.strptime(str(period.yearp) + '-' + month +'-01', "%Y-%m-%d"))
                vecMonth.append(datetime.strptime(str(period.yearp) + '-' + str(int(month)+1) +'-01', "%Y-%m-%d"))
            elif int(month) == 7:
                vecMonth=[]
                vecMonth.append('Julio')
                vecMonth.append(datetime.strptime(str(period.yearp) + '-' + month +'-01', "%Y-%m-%d"))
                vecMonth.append(datetime.strptime(str(period.yearp) + '-' + str(int(month)+1) +'-01', "%Y-%m-%d"))
            elif int(month) == 8:
                vecMonth=[]
                vecMonth.append('Agosto')
                vecMonth.append(datetime.strptime(str(period.yearp) + '-' + month +'-01', "%Y-%m-%d"))
                vecMonth.append(datetime.strptime(str(period.yearp) + '-' + str(int(month)+1) +'-01', "%Y-%m-%d"))
            elif int(month) == 9:
                vecMonth=[]
                vecMonth.append('Septiembre')
                vecMonth.append(datetime.strptime(str(period.yearp) + '-' + month +'-01', "%Y-%m-%d"))
                vecMonth.append(datetime.strptime(str(period.yearp) + '-' + str(int(month)+1) +'-01', "%Y-%m-%d"))
            elif int(month) == 10:
                vecMonth=[]
                vecMonth.append('Octubre')
                vecMonth.append(datetime.strptime(str(period.yearp) + '-' + month +'-01', "%Y-%m-%d"))
                vecMonth.append(datetime.strptime(str(period.yearp) + '-' + str(int(month)+1) +'-01', "%Y-%m-%d"))
            elif int(month) == 11:
                vecMonth=[]
                vecMonth.append('Noviembre')
                vecMonth.append(datetime.strptime(str(period.yearp) + '-' + month +'-01', "%Y-%m-%d"))
                vecMonth.append(datetime.strptime(str(period.yearp) + '-' + str(int(month)+1) +'-01', "%Y-%m-%d"))
            elif int(month) == 12:
                vecMonth=[]
                vecMonth.append('Diciembre')
                vecMonth.append(datetime.strptime(str(period.yearp) + '-' + month +'-01', "%Y-%m-%d"))
                vecMonth.append(datetime.strptime(str(period.yearp+1) + '-' + '01-01', "%Y-%m-%d"))
    return vecMonth


@auth.requires_login()
@auth.requires(auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
def VALIDATE_PERIOD(period):
    try:
        period = db(db.period_year.id==int(period)).select().first()
        return period
    except:
        return None


@auth.requires_login()
@auth.requires(auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
def VALIDATE_EVALUATION(evaluation):
    try:
        evaluation = db(db.repository_evaluation.id==int(evaluation)).select().first()
        return evaluation
    except:
        return None


@auth.requires_login()
@auth.requires(auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
def VALIDATE_PROJECT(projectI,typeReport):
    try:
        #CHECK IN THE LOG IF THE PROJECT EXIST
        flag=False
        if typeReport=='grades_log':
            flag=True
            project=db(db.grades_log.project==projectI).select().first()
            if project is not None:
                project=project.project
        elif typeReport=='course_activity_log':
            flag=True
            project=db(db.course_activity_log.course==projectI).select().first()
            if project is not None:
                project=project.course
        elif typeReport=='academic_course_assignation_log':
            flag=True
            project=db((db.academic_course_assignation_log.before_course==projectI)|(db.academic_course_assignation_log.after_course==projectI)).select().first()
            if project is not None:
                if project.before_course is not None:
                    project=project.before_course
                else:
                    project=project.after_course
        elif typeReport=='requestchange_activity_log':
            flag=True
            project=db(db.requestchange_activity_log.course==projectI).select().first()
            if project is not None:
                project=project.course
        elif typeReport=='request_change_g_log':
            flag=True
            project=db(db.request_change_g_log.project==projectI).select().first()
            if project is not None:
                project=project.project
        else:
            project = None

        #TYPE OF REPORT CORRECT BUT THE PROJECT IS NOT IN THE LOG
        if project is None and flag==True:
            area = db(db.area_level.name=='DTT Tutor Académico').select().first()
            project = db((db.project.name==projectI)&(db.project.area_level==area.id)).select().first()
            if project is not None:
                project = project.name

        #RETURN PROJECT
        return project
    except:
        return None


@auth.requires_login()
@auth.requires(auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
def VALIDATE_ROLE(nameRole,typeReport):
    try:
        #CHECK IF THE ROLE EXIST IN THE OFFICIAL ROLES
        roll = db((db.auth_group.role==nameRole)&(db.auth_group.role!='Academic')&(db.auth_group.role!='DSI')).select().first()
        if roll is None:
            #CHECK IF THE ROLE EXIT IN THE LOGS OF SYSTEM 
            if typeReport=='grades_log':
                roll = db((db.grades_log.roll==nameRole)&(db.grades_log.roll!='Academic')&(db.grades_log.roll!='DSI')).select().first()
                if roll is not None:
                    roll=roll.roll
            elif typeReport=='course_activity_log':
                roll = db((db.course_activity_log.roll==nameRole)&(db.course_activity_log.roll!='Academic')&(db.course_activity_log.roll!='DSI')).select().first()
                if roll is not None:
                    roll=roll.roll
            elif typeReport=='academic_log':
                roll=db(db.academic_log.roll.like('%'+nameRole+'%')).select().first()
                if roll is not None:
                    roll=roll.roll
            elif typeReport=='academic_course_assignation_log':
                roll=db(db.academic_course_assignation_log.roll.like('%'+nameRole+'%')).select().first()
                if roll is not None:
                    roll=roll.roll
            else:
                roll=None
        else:
            roll=roll.role

        #RETURN ROLE
        return roll
    except:
        return None


@auth.requires_login()
@auth.requires(auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
def VALIDATE_USER(period,project,roll,idUser,typeReport):
    try:
        #CHECK IF THE USER EXIST IN THE OFFICIAL USERS
        userP = None
        rollT = db((db.auth_group.role==roll)&(db.auth_group.role!='Academic')&(db.auth_group.role!='DSI')).select().first()
        if rollT is not None:
            if roll=='Super-Administrator' or roll=='Ecys-Administrator':
                userP = db((db.auth_user.username==idUser)&(db.auth_user.id==db.auth_membership.user_id)&(db.auth_membership.group_id==rollT.id)).select(db.auth_user.ALL).first()
                if userP is not None:
                    userP=userP.username
            else:
                if typeReport != 'academic_log':
                    projectT = db(db.project.name==project).select().first()
                    if projectT is not None:
                        userP=db((db.auth_membership.group_id==rollT.id)&(db.auth_membership.user_id==db.auth_user.id)&(db.auth_user.username==idUser)&(db.auth_user.id==db.user_project.assigned_user)&(db.user_project.project==projectT.id)&(db.user_project.period == db.period_year.id)&((db.user_project.period <= period.id) & ((db.user_project.period + db.user_project.periods) > period.id))).select(db.auth_user.ALL).first()
                        if userP is not None:
                            userP=userP.username
                else:
                    userP=db((db.auth_membership.group_id==rollT.id)&(db.auth_membership.user_id==db.auth_user.id)&(db.auth_user.username==idUser)&(db.auth_user.id==db.user_project.assigned_user)&(db.user_project.period == db.period_year.id)&((db.user_project.period <= period.id) & ((db.user_project.period + db.user_project.periods) > period.id))).select(db.auth_user.ALL).first()
                    if userP is not None:
                        userP=userP.username

        
        #CHECK IF THE ROLE EXIT IN THE LOGS OF SYSTEM 
        if userP is None:
            if typeReport=='grades_log':
                userP = db((db.grades_log.project==project)&(db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.roll==roll)&(db.grades_log.user_name==idUser)).select().first()
                if userP is not None:
                    userP=userP.user_name
            elif typeReport=='course_activity_log':
                userP = db((db.course_activity_log.course==project)&(db.course_activity_log.period==T(period.period.name))&(db.course_activity_log.yearp==period.yearp)&(db.course_activity_log.roll==roll)&(db.course_activity_log.user_name==idUser)).select().first()
                if userP is not None:
                    userP=userP.user_name
            elif typeReport=='academic_log':
                userP = db((db.academic_log.id_period==period.id)&(db.academic_log.roll.like('%'+str(roll)+'%'))&(db.academic_log.user_name==idUser)).select().first()
                if userP is not None:
                    userP=userP.user_name
            elif typeReport=='academic_course_assignation_log':
                userP = db((db.academic_course_assignation_log.id_period==period.id)&((db.academic_course_assignation_log.before_course==project)|(db.academic_course_assignation_log.after_course==project))&(db.academic_course_assignation_log.roll.like('%'+str(roll)+'%'))&(db.academic_course_assignation_log.user_name==idUser)).select().first()
                if userP is not None:
                    userP=userP.user_name
            elif typeReport =='requestchange_activity_log':
                userP = db((db.requestchange_activity_log.course==project)&(db.requestchange_activity_log.semester==period.period.name)&(db.requestchange_activity_log.yearp==period.yearp)&(db.requestchange_activity_log.roll_request==roll)&(db.requestchange_activity_log.user_request==idUser)).select().first()
                if userP is not None:
                    userP=userP.user_request
            elif typeReport =='request_change_g_log':
                userP = db((db.request_change_g_log.project==project)&(db.request_change_g_log.semester==T(period.period.name))&(db.request_change_g_log.yearp==period.yearp)&(db.request_change_g_log.roll==roll)&(db.request_change_g_log.username==idUser)).select().first()
                if userP is not None:
                    userP=userP.user_request
            else:
                userP = None
        return userP
    except:
        return None


#???????????????????????????????????????????????????????????
#GROUP OF INFORMATION
@auth.requires_login()
@auth.requires(auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
def GET_YEARS():
    years = []
    for period in db(db.period_year).select(db.period_year.yearp,distinct=True):
        years.append(period.yearp)
    return years


@auth.requires_login()
@auth.requires(auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
def GET_PROJECTS(typeReport):
    projects=[]
    #OFFICIAL PROJECTS
    area = db(db.area_level.name=='DTT Tutor Académico').select().first()
    if area is not None:
        for project in db(db.project.area_level==area.id).select(db.project.name.with_alias('name'), distinct=True):
            projects.append(project.name)

    #PROJECTS IN LOGS
    if typeReport == 'grades_log':
        if len(projects) == 0:
            projectsTemp = db(db.grades_log).select(db.grades_log.project.with_alias('name'), distinct=True)
        else:
            projectsTemp = db(~db.grades_log.project.belongs(projects)).select(db.grades_log.project.with_alias('name'), distinct=True)
        for project in projectsTemp:
            projects.append(project.name)
    elif typeReport == 'course_activity_log':
        if len(projects) == 0:
            projectsTemp = db(db.course_activity_log).select(db.course_activity_log.course.with_alias('name'), distinct=True)
        else:
            projectsTemp = db(~db.course_activity_log.course.belongs(projects)).select(db.course_activity_log.course.with_alias('name'), distinct=True)
        for project in projectsTemp:
            projects.append(project.name)
    elif typeReport == 'academic_course_assignation_log':
        if len(projects) == 0:
            projectsTemp = db(db.academic_course_assignation_log).select(db.academic_course_assignation_log.before_course.with_alias('name'), distinct=True)
        else:
            projectsTemp = db(~db.academic_course_assignation_log.before_course.belongs(projects)).select(db.academic_course_assignation_log.before_course.with_alias('name'), distinct=True)
        for project in projectsTemp:
            projects.append(project.name)

        if len(projects) == 0:
            projectsTemp = db(db.academic_course_assignation_log).select(db.academic_course_assignation_log.after_course.with_alias('name'), distinct=True)
        else:
            projectsTemp = db(~db.academic_course_assignation_log.after_course.belongs(projects)).select(db.academic_course_assignation_log.after_course.with_alias('name'), distinct=True)
        for project in projectsTemp:
            projects.append(project.name)
    elif typeReport == 'requestchange_activity_log':
        if len(projects) == 0:
            projectsTemp = db(db.requestchange_activity_log).select(db.requestchange_activity_log.course.with_alias('name'), distinct=True)
        else:
            projectsTemp = db(~db.requestchange_activity_log.course.belongs(projects)).select(db.requestchange_activity_log.course.with_alias('name'), distinct=True)
        for project in projectsTemp:
            projects.append(project.name)
    elif typeReport == 'request_change_g_log':
        if len(projects) == 0:
            projectsTemp = db(db.request_change_g_log).select(db.request_change_g_log.project.with_alias('name'), distinct=True)
        else:
            projectsTemp = db(~db.request_change_g_log.project.belongs(projects)).select(db.request_change_g_log.project.with_alias('name'), distinct=True)
        for project in projectsTemp:
            projects.append(project.name)
    else:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    return projects


@auth.requires_login()
@auth.requires(auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
def GET_ROLES(typeReport):
    roles=[]
    #OFFICIAL ROLES
    for roll in db((db.auth_group.role!='Academic')&(db.auth_group.role!='DSI')).select(db.auth_group.role.with_alias('roll'), distinct=True):
        roles.append(roll.roll)

    #ROLES IN LOGS
    if typeReport == 'grades_log':
        if len(roles) == 0:
            rolesTemp = db((db.grades_log.roll!='Academic')&(db.grades_log.roll!='DSI')).select(db.grades_log.roll.with_alias('roll'), distinct=True)
        else:
            rolesTemp = db(~db.grades_log.roll.belongs(roles)&(db.grades_log.roll!='Academic')&(db.grades_log.roll!='DSI')).select(db.grades_log.roll.with_alias('roll'), distinct=True)
        for roll in rolesTemp:
            roles.append(roll.roll)
    elif typeReport == 'course_activity_log':
        if len(roles) == 0:
            rolesTemp = db((db.course_activity_log.roll!='Academic')&(db.course_activity_log.roll!='DSI')).select(db.course_activity_log.roll.with_alias('roll'), distinct=True)
        else:
            rolesTemp = db(~db.course_activity_log.roll.belongs(roles)&(db.course_activity_log.roll!='Academic')&(db.course_activity_log.roll!='DSI')).select(db.course_activity_log.roll.with_alias('roll'), distinct=True)
        for roll in rolesTemp:
            roles.append(roll.roll)
    elif typeReport == 'academic_log':
        roles.append('system')
        rolesTemp = db(~db.academic_log.roll.belongs(roles)&(db.academic_log.roll!='Academic')&(db.academic_log.roll!='DSI')).select(db.academic_log.roll.with_alias('roll'), distinct=True)
        for roll in rolesTemp:
            roles.append(roll.roll)
    elif typeReport == 'academic_course_assignation_log':
        if len(roles) == 0:
            rolesTemp = db((db.academic_course_assignation_log.roll!='Academic')&(db.academic_course_assignation_log.roll!='DSI')).select(db.academic_course_assignation_log.roll.with_alias('roll'), distinct=True)
        else:
            rolesTemp = db(~db.academic_course_assignation_log.roll.belongs(roles)&(db.academic_course_assignation_log.roll!='Academic')&(db.academic_course_assignation_log.roll!='DSI')).select(db.academic_course_assignation_log.roll.with_alias('roll'), distinct=True)
        for roll in rolesTemp:
            roles.append(roll.roll)
    else:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    return roles

@auth.requires_login()
@auth.requires(auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
def GET_USERS(period,project,roll,typeReport):
    usersProject=[]
    #OFFICIAL USERS
    rollT = db((db.auth_group.role==roll)&(db.auth_group.role!='Academic')&(db.auth_group.role!='DSI')).select().first()
    if rollT is not None:
        if roll=='Super-Administrator' or roll=='Ecys-Administrator':
            for userT in db((db.auth_user.id==db.auth_membership.user_id)&(db.auth_membership.group_id==rollT.id)).select(db.auth_user.ALL):
                usersProject.append(userT.username)
        else:
            if (typeReport != 'academic_log' and typeReport != 'evaluation_result' ):
                projectT = db(db.project.name==project).select().first()
                if projectT is not None:
                    for userT in db((db.auth_membership.group_id==rollT.id)&(db.auth_membership.user_id==db.auth_user.id)&(db.auth_user.id==db.user_project.assigned_user)&(db.user_project.project==projectT.id)&(db.user_project.period == db.period_year.id)&((db.user_project.period <= period.id) & ((db.user_project.period + db.user_project.periods) > period.id))).select(db.auth_user.ALL):
                        usersProject.append(userT.username)
            else:
                for userT in db((db.auth_membership.group_id==rollT.id)&(db.auth_membership.user_id==db.auth_user.id)&(db.auth_user.id==db.user_project.assigned_user)&(db.user_project.period == db.period_year.id)&((db.user_project.period <= period.id) & ((db.user_project.period + db.user_project.periods) > period.id))).select(db.auth_user.ALL, distinct=True):
                    usersProject.append(userT.username)

    #USERS IN LOGS
    if typeReport == 'grades_log':
        if len(usersProject) ==0:
            usersProjectT = db((db.grades_log.project==project)&(db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.roll==roll)).select(db.grades_log.user_name, distinct=True)
        else:
            usersProjectT = db((db.grades_log.project==project)&(db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.roll==roll)&(~db.grades_log.user_name.belongs(usersProject))).select(db.grades_log.user_name, distinct=True)
        for userT in usersProjectT:
            usersProject.append(userT.user_name)
    elif typeReport == 'course_activity_log':
        if len(usersProject) ==0:
            usersProjectT = db((db.course_activity_log.course==project)&(db.course_activity_log.period==T(period.period.name))&(db.course_activity_log.yearp==period.yearp)&(db.course_activity_log.roll==roll)).select(db.course_activity_log.user_name, distinct=True)
        else:
            usersProjectT = db((db.course_activity_log.course==project)&(db.course_activity_log.period==T(period.period.name))&(db.course_activity_log.yearp==period.yearp)&(db.course_activity_log.roll==roll)&(~db.course_activity_log.user_name.belongs(usersProject))).select(db.course_activity_log.user_name, distinct=True)
        for userT in usersProjectT:
            usersProject.append(userT.user_name)
    elif typeReport == 'academic_log':
        if len(usersProject) == 0:
            usersProjectT = db((db.academic_log.id_period==period.id)&(db.academic_log.roll.like('%'+str(roll)+'%'))).select(db.academic_log.user_name, distinct=True)
        else:
            usersProjectT = db((db.academic_log.id_period==period.id)&(db.academic_log.roll.like('%'+str(roll)+'%'))&(~db.academic_log.user_name.belongs(usersProject))).select(db.academic_log.user_name, distinct=True)
        for userT in usersProjectT:
            usersProject.append(userT.user_name)
    elif typeReport == 'academic_course_assignation_log':
        if len(usersProject) == 0:
            usersProjectT = db((db.academic_course_assignation_log.id_period==period.id)&((db.academic_course_assignation_log.before_course==project)|(db.academic_course_assignation_log.after_course==project))&(db.academic_course_assignation_log.roll.like('%'+str(roll)+'%'))).select(db.academic_course_assignation_log.user_name, distinct=True)
        else:
            usersProjectT = db((db.academic_course_assignation_log.id_period==period.id)&((db.academic_course_assignation_log.before_course==project)|(db.academic_course_assignation_log.after_course==project))&(db.academic_course_assignation_log.roll.like('%'+str(roll)+'%'))&(~db.academic_course_assignation_log.user_name.belongs(usersProject))).select(db.academic_course_assignation_log.user_name, distinct=True)
        for userT in usersProjectT:
            usersProject.append(userT.user_name)
    elif typeReport == 'evaluation_result':
        condition = ''
        for userTT in usersProject:
            if condition=='':
                condition='and academic_log.user_name != "'+userTT+'"'
            else:
                condition=condition+' and academic_log.user_name != "'+userTT+'"'
        searchT='academic_log.id_period = "'+str(period.id)+'" and academic_log.roll contains "'+str(roll)+'" '+condition
        for userT in db.smart_query(db.academic_log,searchT).select(db.academic_log.user_name, distinct=True):
            usersProject.append(userT.user_name)
    elif typeReport == 'requestchange_activity_log':
        if len(usersProject) ==0:
            usersProjectT = db((db.requestchange_activity_log.course==project)&(db.requestchange_activity_log.semester==period.period.name)&(db.requestchange_activity_log.yearp==period.yearp)&(db.requestchange_activity_log.roll_request==roll)).select(db.requestchange_activity_log.user_request, distinct=True)
        else:
            usersProjectT = db((db.requestchange_activity_log.course==project)&(db.requestchange_activity_log.semester==period.period.name)&(db.requestchange_activity_log.yearp==period.yearp)&(db.requestchange_activity_log.roll_request==roll)&(~db.requestchange_activity_log.user_request.belongs(usersProject))).select(db.requestchange_activity_log.user_request, distinct=True)
        for userT in usersProjectT:
            usersProject.append(userT.user_request)
    elif typeReport == 'request_change_g_log':
        if len(usersProject) ==0:
            usersProjectT = db((db.request_change_g_log.project==project)&(db.request_change_g_log.semester==T(period.period.name))&(db.request_change_g_log.yearp==period.yearp)&(db.request_change_g_log.roll==roll)).select(db.request_change_g_log.username, distinct=True)
        else:
            usersProjectT = db((db.request_change_g_log.project==project)&(db.request_change_g_log.semester==T(period.period.name))&(db.request_change_g_log.yearp==period.yearp)&(db.request_change_g_log.roll==roll)&(~db.request_change_g_log.username.belongs(usersProject))).select(db.request_change_g_log.username, distinct=True)
        for userT in usersProjectT:
            usersProject.append(userT.username)
    else:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    return usersProject


@auth.requires_login()
@auth.requires(auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
def GET_CATEGORIES(typeReport):
    categories = []
    #OFFICIAL CATEGORIES
    for category in db(db.activity_category).select(db.activity_category.category, distinct=True):
        categories.append(category.category)

    #CATEGORIES IN LOGS
    if typeReport == 'grades_log':
        if len(categories) == 0:
            categoriesTemp = db(db.grades_log).select(db.grades_log.category, distinct=True)
        else:
            categoriesTemp = db(~db.grades_log.category.belongs(categories)).select(db.grades_log.category, distinct=True)
        for category in categoriesTemp:
            categories.append(category.category)
    elif typeReport == 'course_activity_log':
        if len(categories) == 0:
            categoriesTemp = db(db.course_activity_log).select(db.course_activity_log.before_course_activity_category, distinct=True)
        else:
            categoriesTemp = db((~db.course_activity_log.before_course_activity_category.belongs(categories))).select(db.course_activity_log.before_course_activity_category, distinct=True)
        for category in categoriesTemp:
            categories.append(category.before_course_activity_category)

        if len(categories) == 0:
            categoriesTemp = db(db.course_activity_log).select(db.course_activity_log.after_course_activity_category, distinct=True)
        else:
            categoriesTemp = db((~db.course_activity_log.after_course_activity_category.belongs(categories))).select(db.course_activity_log.after_course_activity_category, distinct=True)
        for category in categoriesTemp:
            categories.append(category.after_course_activity_category)
    elif typeReport == 'requestchange_activity_log':
        if len(categories) == 0:
            categoriesTemp = db(db.requestchange_activity_log).select(db.requestchange_activity_log.category_request, distinct=True)
        else:
            categoriesTemp = db(~db.requestchange_activity_log.category_request.belongs(categories)).select(db.requestchange_activity_log.category_request, distinct=True)
        for category in categoriesTemp:
            categories.append(category.category_request)
    elif typeReport == 'request_change_g_log':
        if len(categories) == 0:
            categoriesTemp = db(db.request_change_g_log).select(db.request_change_g_log.category, distinct=True)
        else:
            categoriesTemp = db(~db.request_change_g_log.category.belongs(categories)).select(db.request_change_g_log.category, distinct=True)
        for category in categoriesTemp:
            categories.append(category.category)
    else:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    return categories


@auth.requires_login()
@auth.requires(auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
def GET_ACTIVITIES(typeReport):
    activities = []
    #OFFICIAL CATEGORIES
    for activity in db(db.course_activity).select(db.course_activity.name, distinct=True):
        activities.append(activity.name)

    #ACTIVITIES IN LOGS
    if typeReport == 'grades_log':
        if len(activities) == 0:
            activitiesTemp = db(db.grades_log).select(db.grades_log.activity, distinct=True)
        else:
            activitiesTemp = db(~db.grades_log.activity.belongs(activities)).select(db.grades_log.activity, distinct=True)
        for activity in activitiesTemp:
            activities.append(activity.activity)
    elif typeReport == 'course_activity_log':
        if len(activities) == 0:
            activitiesTemp = db(db.course_activity_log).select(db.course_activity_log.before_name, distinct=True)
        else:
            activitiesTemp = db((~db.course_activity_log.before_name.belongs(activities))).select(db.course_activity_log.before_name, distinct=True)
        for activity in activitiesTemp:
            activities.append(activity.before_name)

        if len(activities) == 0:
            activitiesTemp = db(db.course_activity_log).select(db.course_activity_log.after_name, distinct=True)
        else:
            activitiesTemp = db((~db.course_activity_log.after_name.belongs(activities))).select(db.course_activity_log.after_name, distinct=True)
        for activity in activitiesTemp:
            activities.append(activity.after_name)
    elif typeReport == 'request_change_g_log':
        if len(activities) == 0:
            activitiesTemp = db(db.request_change_g_log).select(db.request_change_g_log.activity, distinct=True)
        else:
            activitiesTemp = db(~db.request_change_g_log.activity.belongs(activities)).select(db.request_change_g_log.activity, distinct=True)
        for activity in activitiesTemp:
            activities.append(activity.activity)
    else:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    return activities


@auth.requires_login()
@auth.requires(auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
def GET_DESCRIPTIONS(typeReport):
    descriptions = []
    #ROLES IN LOGS
    if typeReport == 'grades_log':
        for description in db(db.grades_log).select(db.grades_log.description, distinct=True):
            descriptions.append(description.description)
    elif typeReport == 'academic_log':
        for description in db(db.academic_log).select(db.academic_log.description, distinct=True):
            descriptions.append(description.description)
    elif typeReport == 'academic_course_assignation_log':
        for description in db(db.academic_course_assignation_log).select(db.academic_course_assignation_log.description, distinct=True):
            descriptions.append(description.description)
    else:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    return descriptions


@auth.requires_login()
@auth.requires(auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
def GET_DATES(typeReport):
    dates = []
    #ROLES IN LOGS
    if typeReport == 'grades_log':
        for dat in db(db.grades_log).select(db.grades_log.date_log, distinct=True):
            dates.append(dat.date_log)
    elif typeReport == 'course_activity_log':
        for dat in db(db.course_activity_log).select(db.course_activity_log.date_log, distinct=True):
            dates.append(dat.date_log)
    elif typeReport == 'academic_log':
        for dat in db(db.academic_log).select(db.academic_log.date_log, distinct=True):
            dates.append(dat.date_log)
    elif typeReport == 'academic_course_assignation_log':
        for dat in db(db.academic_course_assignation_log).select(db.academic_course_assignation_log.date_log, distinct=True):
            dates.append(dat.date_log)
    elif typeReport == 'requestchange_activity_log':
        for dat in db(db.requestchange_activity_log).select(db.requestchange_activity_log.date_request, distinct=True):
            dates.append(dat.date_request)
    elif typeReport == 'request_change_g_log':
        for dat in db(db.request_change_g_log).select(db.request_change_g_log.date_request, distinct=True):
            dates.append(dat.date_request)
    else:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    return dates


@auth.requires_login()
@auth.requires(auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
def GET_EVALUATIONS(period):
    years = []
    for period in db(db.period_year).select(db.period_year.yearp,distinct=True):
        years.append(period.yearp)
    return years
#*****************************************************FEATURES EXTRAS FOR REPORTS*****************************************************
#*************************************************************************************************************************************
#*************************************************************************************************************************************




#*************************************************************************************************************************************
#*************************************************************************************************************************************
#*****************************************************MANAGEMENT REPORT GRADES********************************************************
@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def grades_management_export():
    #VERIFI THAT ACCURATE PARAMETERS
    try:
        #CHECK IF THE TYPE OF EXPORT IS VALID
        if request.vars['list_type'] is None or str(request.vars['list_type'])!="csv":
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #CHECK THAT THE LEVEL OF REPORT IS VALID
        if request.vars['level'] is not None and (int(request.vars['level'])<1 or int(request.vars['level'])>6):
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('default','index'))
        
        #VERIFY THAT THE PARAMETERS OF EACH LEVEL BE VALID
        if request.vars['level'] is not None:
            #LEVEL MORE THAN 1
            if int(request.vars['level'])>1:
                #CHECK IF THE TYPE OF REPORT IS VALID
                if request.vars['type_L'] is None or (str(request.vars['type_L'])!="all" and str(request.vars['type_L'])!="i" and str(request.vars['type_L'])!="u" and str(request.vars['type_L'])!="d"):
                    session.flash = T('Report no visible: There are no parameters required to display the report.')
                    redirect(URL('default','index'))

                period = VALIDATE_PERIOD(request.vars['period'])
                if period is None:
                    session.flash = T('Report no visible: There are no parameters required to display the report.')
                    redirect(URL('default','index'))
            
            #LEVEL MORE THAN 2
            if int(request.vars['level'])>2:
                #CHECK IF THE TYPE OF REPORT IS VALID
                if request.vars['type_U'] is None or (str(request.vars['type_U'])!="all" and str(request.vars['type_U'])!="i" and str(request.vars['type_U'])!="u" and str(request.vars['type_U'])!="d"):
                    session.flash = T('Report no visible: There are no parameters required to display the report.')
                    redirect(URL('default','index'))

                #CHECK IF THE MONTH IS VALID
                month = VALIDATE_MONTH(request.vars['month'],period)
                if month is None:
                    session.flash = T('Report no visible: There are no parameters required to display the report.')
                    redirect(URL('default','index'))

            #LEVEL MORE THAN 3
            if int(request.vars['level'])>3:
                #CHECK IF THE PROJECT IS VALID
                project = VALIDATE_PROJECT(request.vars['project'],'grades_log')
                if project is None:
                    session.flash = T('Report no visible: There are no parameters required to display the report.')
                    redirect(URL('default','index'))

            #LEVEL MORE THAN 4
            if int(request.vars['level'])>4:
                #CHECK IF THE ROLE IS VALID
                roll = VALIDATE_ROLE(request.vars['roll'],'grades_log')
                if roll is None:
                    session.flash = T('Report no visible: There are no parameters required to display the report.')
                    redirect(URL('default','index'))

            #LEVEL MORE THAN 5
            if int(request.vars['level'])>5:
                #CHECK IF THE USER IS VALID
                userP = VALIDATE_USER(period,project,roll,request.vars['userP'],'grades_log')
                if userP is None:
                    session.flash = T('Report no visible: There are no parameters required to display the report.')
                    redi*rect(URL('default','index'))
    except:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))

    #CHECK IF THERE IS A PERSONALIZED QUERY
    personal_query = ''
    if request.vars['querySearch'] is not None and str(request.vars['querySearch']) != "":
        #PERSONALIZED QUERY SURE WORK
        try:
            personal_query = str(request.vars['querySearch'])
            countI = db.smart_query(db.grades_log,personal_query).count()
        except:
            personal_query = ''

    #****************************************************************************************************************
    #****************************************************************************************************************
    #*****************************************************REPORT*****************************************************
    from datetime import datetime
    #TITLE
    infoLevel = []
    infoeLevelTemp=[]
    infoeLevelTemp.append('Universidad de San Carlos de Guatemala')
    infoLevel.append(infoeLevelTemp)
    infoeLevelTemp=[]
    infoeLevelTemp.append('Facultad de Ingeniería')
    infoLevel.append(infoeLevelTemp)
    infoeLevelTemp=[]
    infoeLevelTemp.append('Escuela de Ciencias y Sistemas')
    infoLevel.append(infoeLevelTemp)
    #TYPE OF REPORT
    infoeLevelTemp=[]
    infoeLevelTemp.append(T('Type'))
    infoeLevelTemp.append(T('Grades Management'))
    infoLevel.append(infoeLevelTemp)
    #DESCRIPTION OF REPORT
    infoeLevelTemp=[]
    infoeLevelTemp.append(T('Description'))
    infoeLevelTemp.append(T('Report of transactions on the notes of students'))
    infoLevel.append(infoeLevelTemp)
    #LEVELS OF REPORT
    #ALL SEMESTERS
    if request.vars['level'] is None or str(request.vars['level'])=="1":#ALL SEMESTERS
        #MIDDLE LINE OF REPORT
        infoeLevelTemp=[]
        infoLevel.append(infoeLevelTemp)
        #LABLE DETAIL OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Detail'))
        infoLevel.append(infoeLevelTemp)
        #LABELS OF DATA OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Period'))
        infoeLevelTemp.append(T('Total inserted'))
        infoeLevelTemp.append(T('Total modified'))
        infoeLevelTemp.append(T('Total out'))
        infoLevel.append(infoeLevelTemp)
        for period in db(db.period_year).select(orderby=~db.period_year.id):
            infoeLevelTemp = []
            #NAME OF PERIOD
            infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
            #INSERT
            if personal_query == '':
                search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "insert"'
            else:
                search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "insert" and '+personal_query
            countI = db.smart_query(db.grades_log,search).count()
            infoeLevelTemp.append(countI)
            #UPDATE
            if personal_query == '':
                search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "update"'
            else:
                search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "update" and '+personal_query
            countI = db.smart_query(db.grades_log,search).count()
            infoeLevelTemp.append(countI)
            #DELETE
            if personal_query == '':
                search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "delete"'
            else:
                search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "delete" and '+personal_query
            countI = db.smart_query(db.grades_log,search).count()
            infoeLevelTemp.append(countI)
            #INSERT PERIOD
            infoLevel.append(infoeLevelTemp)
    #PER MONTH
    elif str(request.vars['level'])=="2":
        #PERIOD OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Period'))
        infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
        infoLevel.append(infoeLevelTemp)
        #MIDDLE LINE OF REPORT
        infoeLevelTemp=[]
        infoLevel.append(infoeLevelTemp)
        #LABLE DETAIL OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Detail'))
        infoLevel.append(infoeLevelTemp)
        #LABELS OF DATA OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Month'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
            infoeLevelTemp.append(T('Total inserted'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
            infoeLevelTemp.append(T('Total modified'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
            infoeLevelTemp.append(T('Total out'))
        infoLevel.append(infoeLevelTemp)

        for month in GET_MONTH_PERIOD(period):
            start = datetime.strptime(str(period.yearp) + '-' + str(month[0]) +'-01', "%Y-%m-%d")
            if month[2]==1:
                end = datetime.strptime(str(period.yearp+1) + '-' + str(month[2]) +'-01', "%Y-%m-%d")
            else:
                end = datetime.strptime(str(period.yearp) + '-' + str(month[2]) +'-01', "%Y-%m-%d")
            infoeLevelTemp = []
            #NAME OF MONTH
            infoeLevelTemp.append(month[1]+' '+str(period.yearp))
            #INSERT
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                if personal_query == '':
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "insert" and grades_log.date_log >="'+str(start)+'" and grades_log.date_log<"'+str(end)+'"'
                else:
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "insert" and grades_log.date_log >="'+str(start)+'" and grades_log.date_log<"'+str(end)+'" and '+personal_query
                countI = db.smart_query(db.grades_log,search).count()
                infoeLevelTemp.append(countI)
            #UPDATE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "update" and grades_log.date_log>="'+str(start)+'" and grades_log.date_log<"'+str(end)+'"'
                else:
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "update" and grades_log.date_log>="'+str(start)+'" and grades_log.date_log<"'+str(end)+'" and '+personal_query
                countI = db.smart_query(db.grades_log,search).count()
                infoeLevelTemp.append(countI)
            #DELETE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "delete" and grades_log.date_log>="'+str(start)+'" and grades_log.date_log<"'+str(end)+'"'
                else:
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "delete" and grades_log.date_log>="'+str(start)+'" and grades_log.date_log<"'+str(end)+'" and '+personal_query
                countI = db.smart_query(db.grades_log,search).count()
                infoeLevelTemp.append(countI)
            #INSERT MONTH
            infoLevel.append(infoeLevelTemp)
    #PER PROJECT
    elif str(request.vars['level'])=="3":
        #PROJECTS
        projects = GET_PROJECTS('grades_log')
        projects=sorted(projects)
        #PERIOD OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Period'))
        infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
        infoLevel.append(infoeLevelTemp)
        #MONTH OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Month'))
        infoeLevelTemp.append(str(month[0]))
        infoLevel.append(infoeLevelTemp)
        #MIDDLE LINE OF REPORT
        infoeLevelTemp=[]
        infoLevel.append(infoeLevelTemp)
        #LABLE DETAIL OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Detail'))
        infoLevel.append(infoeLevelTemp)
        #LABELS OF DATA OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Project'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
            infoeLevelTemp.append(T('Total inserted'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
            infoeLevelTemp.append(T('Total modified'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
            infoeLevelTemp.append(T('Total out'))
        infoLevel.append(infoeLevelTemp)

        for projectT in projects:
            project=db(db.project.name==projectT).select().first()
            if project is None:
                project=db(db.grades_log.project==projectT).select().first()
                project=project.project
            else:
                project=project.name
            infoeLevelTemp = []
            #NAME OF PROJECT
            infoeLevelTemp.append(project)
            #INSERT
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                if personal_query == '':
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "insert" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+project+'"'
                else:
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "insert" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+project+'" and '+personal_query
                countI = db.smart_query(db.grades_log,search).count()
                infoeLevelTemp.append(countI)
            #UPDATE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "update" and grades_log.date_log>="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+project+'"'
                else:
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "update" and grades_log.date_log>="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+project+'" and '+personal_query
                countI = db.smart_query(db.grades_log,search).count()
                infoeLevelTemp.append(countI)
            #DELETE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "delete" and grades_log.date_log>="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+project+'"'
                else:
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "delete" and grades_log.date_log>="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+project+'" and '+personal_query
                countI = db.smart_query(db.grades_log,search).count()
                infoeLevelTemp.append(countI)
            #INSERT PROJECT
            infoLevel.append(infoeLevelTemp)
    #PER ROL
    elif str(request.vars['level'])=="4":
        #ROLES
        roles = GET_ROLES('grades_log')
        #PERIOD OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Period'))
        infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
        infoLevel.append(infoeLevelTemp)
        #MONTH OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Month'))
        infoeLevelTemp.append(str(month[0]))
        infoLevel.append(infoeLevelTemp)
        #PROJECT OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Project'))
        infoeLevelTemp.append(str(project))
        infoLevel.append(infoeLevelTemp)
        #MIDDLE LINE OF REPORT
        infoeLevelTemp=[]
        infoLevel.append(infoeLevelTemp)
        #LABLE DETAIL OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Detail'))
        infoLevel.append(infoeLevelTemp)
        #LABELS OF DATA OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Role'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
            infoeLevelTemp.append(T('Total inserted'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
            infoeLevelTemp.append(T('Total modified'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
            infoeLevelTemp.append(T('Total out'))
        infoLevel.append(infoeLevelTemp)

        for rollT in roles:
            roll=db(db.auth_group.role==rollT).select().first()
            if roll is None:
                roll=db(db.grades_log.roll==rollT).select().first()
                roll=roll.roll
            else:
                roll=roll.role
            infoeLevelTemp = []
            #NAME OF ROLE
            infoeLevelTemp.append(T('Rol '+roll))
            #INSERT
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                if personal_query == '':
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "insert" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'"'
                else:
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "insert" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and '+personal_query
                countI = db.smart_query(db.grades_log,search).count()
                infoeLevelTemp.append(countI)
            #UPDATE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "update" and grades_log.date_log>="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'"'
                else:
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "update" and grades_log.date_log>="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and '+personal_query
                countI = db.smart_query(db.grades_log,search).count()
                infoeLevelTemp.append(countI)
            #DELETE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "delete" and grades_log.date_log>="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'"'
                else:
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "delete" and grades_log.date_log>="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and '+personal_query
                countI = db.smart_query(db.grades_log,search).count()
                infoeLevelTemp.append(countI)
            #INSERT PROJECT
            infoLevel.append(infoeLevelTemp)
    #PER USER
    elif str(request.vars['level'])=="5":
        #USERS
        usersProject = GET_USERS(period,project,roll,'grades_log')
        #PERIOD OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Period'))
        infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
        infoLevel.append(infoeLevelTemp)
        #MONTH OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Month'))
        infoeLevelTemp.append(str(month[0]))
        infoLevel.append(infoeLevelTemp)
        #PROJECT OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Project'))
        infoeLevelTemp.append(str(project))
        infoLevel.append(infoeLevelTemp)
        #ROL OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Role'))
        infoeLevelTemp.append(T('Rol '+roll))
        infoLevel.append(infoeLevelTemp)
        #MIDDLE LINE OF REPORT
        infoeLevelTemp=[]
        infoLevel.append(infoeLevelTemp)
        #LABLE DETAIL OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Detail'))
        infoLevel.append(infoeLevelTemp)
        #LABELS OF DATA OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('User'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
            infoeLevelTemp.append(T('Total inserted'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
            infoeLevelTemp.append(T('Total modified'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
            infoeLevelTemp.append(T('Total out'))
        infoLevel.append(infoeLevelTemp)

        for userPT in usersProject:
            userP=db(db.auth_user.username==userPT).select().first()
            if userP is None:
                userP=db(db.grades_log.user_name==userPT).select().first()
                userP=userP.user_name
            else:
                userP=userP.username
            infoeLevelTemp=[]
            #NAME OF USER
            infoeLevelTemp.append(userP)
            #INSERT
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                if personal_query == '':
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "insert" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'"'
                else:
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "insert" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'" and '+personal_query
                countI = db.smart_query(db.grades_log,search).count()
                infoeLevelTemp.append(countI)
            #UPDATE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "update" and grades_log.date_log>="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'"'
                else:
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "update" and grades_log.date_log>="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'" and '+personal_query
                countI = db.smart_query(db.grades_log,search).count()
                infoeLevelTemp.append(countI)
            #DELETE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "delete" and grades_log.date_log>="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'"'
                else:
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "delete" and grades_log.date_log>="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'" and '+personal_query
                countI = db.smart_query(db.grades_log,search).count()
                infoeLevelTemp.append(countI)
            #INSERT PROJECT
            infoLevel.append(infoeLevelTemp)
    #DATA
    elif str(request.vars['level'])=="6":
        #DATA
        if str(request.vars['type_L'])=="all":
            if personal_query == '':
                search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'"'
            else:
                search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'" and '+personal_query
        elif str(request.vars['type_L'])=="i":
            if personal_query == '':
                search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "insert" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'"'
            else:
                search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "insert" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'" and '+personal_query
        elif str(request.vars['type_L'])=="u":
            if personal_query == '':
                search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "update" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'"'
            else:
                search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "update" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'" and '+personal_query
        elif str(request.vars['type_L'])=="d":
            if personal_query == '':
                search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "delete" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'"'
            else:
                search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "delete" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'" and '+personal_query
        #PERIOD
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Period'))
        infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
        infoLevel.append(infoeLevelTemp)
        #MONTH
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Month'))
        infoeLevelTemp.append(str(month[0]))
        infoLevel.append(infoeLevelTemp)
        #PROJECT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Project'))
        infoeLevelTemp.append(str(project))
        infoLevel.append(infoeLevelTemp)
        #ROL
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Role'))
        infoeLevelTemp.append(T('Rol '+roll))
        infoLevel.append(infoeLevelTemp)
        #USER
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('User'))
        infoeLevelTemp.append(str(userP))
        infoLevel.append(infoeLevelTemp)
        #MIDDLE LINE
        infoeLevelTemp=[]
        infoeLevelTemp.append('')
        infoLevel.append(infoeLevelTemp)
        #DETAIL
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Detail'))
        infoLevel.append(infoeLevelTemp)
        #TITLE OF TABLE
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Operation'))
        infoeLevelTemp.append(T('Academic'))
        infoeLevelTemp.append(T('Activity'))
        infoeLevelTemp.append(T('Category'))
        infoeLevelTemp.append(T('Grade Before'))
        infoeLevelTemp.append(T('Grade After'))
        infoeLevelTemp.append(T('Date'))
        infoeLevelTemp.append(T('Description'))
        infoLevel.append(infoeLevelTemp)
        for operation in db.smart_query(db.grades_log,search).select():
            infoeLevelTemp=[]
            infoeLevelTemp.append(operation.operation_log)
            infoeLevelTemp.append(operation.academic)
            infoeLevelTemp.append(operation.activity)
            infoeLevelTemp.append(operation.category)
            infoeLevelTemp.append(operation.before_grade)
            infoeLevelTemp.append(operation.after_grade)
            infoeLevelTemp.append(operation.date_log)
            infoeLevelTemp.append(operation.description)
            infoLevel.append(infoeLevelTemp)
    #*****************************************************REPORT*****************************************************
    #****************************************************************************************************************
    #****************************************************************************************************************
    return dict(filename='ReporteGestionNotas', csvdata=infoLevel)


@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def grades_management():
    #****************************************************************************************************************
    #****************************************************************************************************************
    #***************************************CHECK IF THERE IS A PERSONALIZED QUERY***********************************
    personal_query = ''
    makeRedirect = False
    if request.vars['querySearch'] is not None and str(request.vars['querySearch']) != "":
        #PERSONALIZED QUERY SURE WORK
        try:
            personal_query = str(request.vars['querySearch'])
            countI = db.smart_query(db.grades_log,personal_query).count()
            if request.vars['searchT'] is not None and str(request.vars['searchT']) == 'T':
                makeRedirect = True
        except:
            response.flash = T('The query is not valid. The report is displayed without applying any query.')
            personal_query = ''
    if makeRedirect == True:
        redirect(URL('management_reports', 'grades_management',vars=dict(level = 6, period = request.vars['period'], month = str(request.vars['month']), project = str(request.vars['project']), roll = str(request.vars['roll']), userP = str(request.vars['userP']), type_L=request.vars['type_L'], type_U=request.vars['type_U'], querySearch=request.vars['querySearch'])))


    #****************************************************************************************************************
    #****************************************************************************************************************
    #******************************************VERIFY THAT ACCURATE PARAMETERS***************************************
    try:
        #CHECK THAT THE LEVEL OF REPORT IS VALID
        if request.vars['level'] is not None and (int(request.vars['level'])<1 or int(request.vars['level'])>6):
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))
        
        #VERIFY THAT THE PARAMETERS OF EACH LEVEL BE VALID
        if request.vars['level'] is not None:
            #LEVEL MORE THAN 1
            if int(request.vars['level'])>1:
                #CHECK IF THE TYPE OF REPORT IS VALID
                if request.vars['type_L'] is None or (str(request.vars['type_L'])!="all" and str(request.vars['type_L'])!="i" and str(request.vars['type_L'])!="u" and str(request.vars['type_L'])!="d"):
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))

                period = VALIDATE_PERIOD(request.vars['period'])
                if period is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))
            
            #LEVEL MORE THAN 2
            if int(request.vars['level'])>2:
                #CHECK IF THE TYPE OF REPORT IS VALID
                if request.vars['type_U'] is None or (str(request.vars['type_U'])!="all" and str(request.vars['type_U'])!="i" and str(request.vars['type_U'])!="u" and str(request.vars['type_U'])!="d"):
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))

                #CHECK IF THE MONTH IS VALID
                month = VALIDATE_MONTH(request.vars['month'],period)
                if month is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))

            #LEVEL MORE THAN 3
            if int(request.vars['level'])>3:
                #CHECK IF THE PROJECT IS VALID
                project = VALIDATE_PROJECT(request.vars['project'],'grades_log')
                if project is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))

            #LEVEL MORE THAN 4
            if int(request.vars['level'])>4:
                #CHECK IF THE ROLE IS VALID
                roll = VALIDATE_ROLE(request.vars['roll'],'grades_log')
                if roll is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))

            #LEVEL MORE THAN 5
            if int(request.vars['level'])>5:
                #CHECK IF THE USER IS VALID
                userP = VALIDATE_USER(period,project,roll,request.vars['userP'],'grades_log')
                if userP is None:
                    session.flash = T('Not valid Action.')
                    redi*rect(URL('default','index'))
    except:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))


    #****************************************************************************************************************
    #****************************************************************************************************************
    #**************************************************SEARCH REPORT*************************************************
    def filtered_by(flag):
        fsearch_Option=[]
        fsearch_Option.append('=')
        fsearch_Option.append('!=')
        fsearch_Option.append('<')
        fsearch_Option.append('>')
        fsearch_Option.append('<=')
        fsearch_Option.append('>=')
        if flag==True:
            fsearch_Option.append('starts with')
            fsearch_Option.append('contains')
            fsearch_Option.append('in')
            fsearch_Option.append('not in')
        return fsearch_Option

    fsearch = []
    #******************************COMBOS INFORMATION******************************
    #YEARS
    if request.vars['level']=='1' or request.vars['level'] is None:
        groupYears = GET_YEARS()
        if len(groupYears) != 0:
            fsearch.append(['yearp','Año',False,[3,sorted(groupYears)]])
    #PROJECTS
    if request.vars['level'] is None or int(request.vars['level'])<=3:
        projects = GET_PROJECTS('grades_log')
        if len(projects) != 0:
            fsearch_Values=[]
            fsearch_Values.append(4)
            for projectT in projects:
                project=db(db.project.name==projectT).select().first()
                if project is None:
                    project=db(db.grades_log.project==projectT).select().first()
                    project=project.project
                else:
                    project=project.name
                fsearch_Values.append(project)
            fsearch.append(['project','Curso',False,fsearch_Values])
    #ROLES
    if request.vars['level'] is None or int(request.vars['level'])<=4:
        roles = GET_ROLES('grades_log')
        if len(roles) != 0:
            fsearch.append(['roll','Rol',False,[5,sorted(roles)]])
    #CATEGORIES
    groupCategories = GET_CATEGORIES('grades_log')
    if len(groupCategories) != 0:
        fsearch.append(['category','Categoria',False,[3,sorted(groupCategories)]])
    #ACTIVITIES
    groupActivities = GET_ACTIVITIES('grades_log')
    if len(groupActivities) != 0:
        fsearch.append(['activity','Actividad',False,[3,sorted(groupActivities)]])
    #DESCRIPTION
    groupDescription = GET_DESCRIPTIONS('grades_log')
    if len(groupDescription) != 0:
        fsearch.append(['description','Descripción',False,[3,sorted(groupDescription)]])
    #DATE
    groupDates = GET_DATES('grades_log')
    if len(groupDates) != 0:
        fsearch.append(['date_log','Fecha',False,[3,sorted(groupDates)]])
    #OPERATION LOG
    fsearch.append(['operation_log','Operación Registrada',False,[3,['insert','update','delete']]])
    #******************************ENTERING USER******************************
    #CARNET
    fsearch.append(['academic','Estudiante',True,[1]])
    if request.vars['level'] is None or int(request.vars['level'])<=5:
        #ID OF PERSON WHO REGISTER THE GRADE
        fsearch.append(['user_name','Usuario Registro',True,[1]])
    #BEFORE GRADE
    fsearch.append(['before_grade','Nota Previa',False,[1]])
    #OFFICIAL GRADE
    fsearch.append(['after_grade','Nota Oficial',False,[1]])
    

    #****************************************************************************************************************
    #****************************************************************************************************************
    #*****************************************************REPORT*****************************************************
    #LEVELS OF REPORT
    from datetime import datetime
    infoLevel = []
    top5=[]
    grid=None
    #ALL SEMESTERS
    if request.vars['level']=='1' or request.vars['level'] is None:
        if db(db.period_year).select().first() is None:
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('default','index'))
            

        for period in db(db.period_year).select(orderby=~db.period_year.id):
            infoeLevelTemp = []
            #ID OF PERIOD
            infoeLevelTemp.append(period.id)
            #NAME OF PERIOD
            infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
            #INSERT
            if personal_query == '':
                search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "insert"'
            else:
                search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "insert" and '+personal_query
            countI = db.smart_query(db.grades_log,search).count()
            infoeLevelTemp.append(countI)
            #UPDATE
            if personal_query == '':
                search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "update"'
            else:
                search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "update" and '+personal_query
            countI = db.smart_query(db.grades_log,search).count()
            infoeLevelTemp.append(countI)
            #DELETE
            if personal_query == '':
                search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "delete"'
            else:
                search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "delete" and '+personal_query
            countI = db.smart_query(db.grades_log,search).count()
            infoeLevelTemp.append(countI)
            #INSERT PERIOD
            infoLevel.append(infoeLevelTemp)

        #TOP 5 OF PERIOD
        if personal_query == '':
            search='grades_log.id != "-1"'
        else:
            search=personal_query
        top5 = db.smart_query(db.grades_log,search).select(db.grades_log.period, db.grades_log.yearp, db.grades_log.id.count(), orderby=~db.grades_log.id.count(), limitby=(0, 5), groupby=[db.grades_log.period, db.grades_log.yearp])
    #PER MONTH
    elif str(request.vars['level'])=="2":
        for month in GET_MONTH_PERIOD(period):
            start = datetime.strptime(str(period.yearp) + '-' + str(month[0]) +'-01', "%Y-%m-%d")
            if month[2]==1:
                end = datetime.strptime(str(period.yearp+1) + '-' + str(month[2]) +'-01', "%Y-%m-%d")
            else:
                end = datetime.strptime(str(period.yearp) + '-' + str(month[2]) +'-01', "%Y-%m-%d")
            infoeLevelTemp = []
            #NAME OF PERIOD
            infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
            #ID OF MONTH
            infoeLevelTemp.append(month[0])
            #NAME OF MONTH
            infoeLevelTemp.append(month[1]+' '+str(period.yearp))
            #INSERT
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                if personal_query == '':
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "insert" and grades_log.date_log >="'+str(start)+'" and grades_log.date_log<"'+str(end)+'"'
                else:
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "insert" and grades_log.date_log >="'+str(start)+'" and grades_log.date_log<"'+str(end)+'" and '+personal_query
                countI = db.smart_query(db.grades_log,search).count()
                infoeLevelTemp.append(countI)
            #UPDATE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "update" and grades_log.date_log>="'+str(start)+'" and grades_log.date_log<"'+str(end)+'"'
                else:
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "update" and grades_log.date_log>="'+str(start)+'" and grades_log.date_log<"'+str(end)+'" and '+personal_query
                countI = db.smart_query(db.grades_log,search).count()
                infoeLevelTemp.append(countI)
            #DELETE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "delete" and grades_log.date_log>="'+str(start)+'" and grades_log.date_log<"'+str(end)+'"'
                else:
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "delete" and grades_log.date_log>="'+str(start)+'" and grades_log.date_log<"'+str(end)+'" and '+personal_query
                countI = db.smart_query(db.grades_log,search).count()
                infoeLevelTemp.append(countI)
            #INSERT MONTH
            infoLevel.append(infoeLevelTemp)
    #PER PROJECT
    elif str(request.vars['level'])=="3":
        if len(projects) == 0:
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('management_reports', 'grades_management',vars=dict(level='2',period = str(request.vars['period']), type_L = str(request.vars['type_U']), querySearch=personal_query)))
        projects=sorted(projects)

        for projectT in projects:
            project=db(db.project.name==projectT).select().first()
            if project is None:
                project=db(db.grades_log.project==projectT).select().first()
                project=project.project
            else:
                project=project.name
            infoeLevelTemp = []
            #NAME OF PERIOD
            infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
            #NAME OF MONTH
            infoeLevelTemp.append(month[0])
            #ID OF PROJECT
            infoeLevelTemp.append(project)
            #NAME OF PROJECT
            infoeLevelTemp.append(project)
            #INSERT
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                if personal_query == '':
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "insert" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+project+'"'
                else:
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "insert" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+project+'" and '+personal_query
                countI = db.smart_query(db.grades_log,search).count()
                infoeLevelTemp.append(countI)
            #UPDATE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "update" and grades_log.date_log>="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+project+'"'
                else:
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "update" and grades_log.date_log>="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+project+'" and '+personal_query
                countI = db.smart_query(db.grades_log,search).count()
                infoeLevelTemp.append(countI)
            #DELETE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "delete" and grades_log.date_log>="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+project+'"'
                else:
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "delete" and grades_log.date_log>="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+project+'" and '+personal_query
                countI = db.smart_query(db.grades_log,search).count()
                infoeLevelTemp.append(countI)
            #INSERT PROJECT
            infoLevel.append(infoeLevelTemp)

        #TOP 5 OF PROJECT
        if personal_query == '':
            search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'"'
        else:
            search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and '+personal_query
        top5 = db.smart_query(db.grades_log,search).select(db.grades_log.project, db.grades_log.id.count(), orderby=~db.grades_log.id.count(), limitby=(0, 5), groupby=db.grades_log.project)
    #PER ROL
    elif str(request.vars['level'])=="4":
        if len(roles) == 0:
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('management_reports', 'grades_management',vars=dict(level='3', period = str(request.vars['period']), month = str(request.vars['month']), type_L = str(request.vars['type_U']), type_U = str(request.vars['type_U']), querySearch=personal_query)))

        for rollT in roles:
            roll=db(db.auth_group.role==rollT).select().first()
            if roll is None:
                roll=db(db.grades_log.roll==rollT).select().first()
                roll=roll.roll
            else:
                roll=roll.role
            infoeLevelTemp = []
            #NAME OF PERIOD
            infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
            #NAME OF MONTH
            infoeLevelTemp.append(month[0])
            #NAME OF PROJECT
            infoeLevelTemp.append(project)
            #ID OF ROLE
            infoeLevelTemp.append(roll)
            #NAME OF ROLE
            infoeLevelTemp.append(T('Rol '+roll))
            #INSERT
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                if personal_query == '':
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "insert" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'"'
                else:
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "insert" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and '+personal_query
                countI = db.smart_query(db.grades_log,search).count()
                infoeLevelTemp.append(countI)
            #UPDATE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "update" and grades_log.date_log>="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'"'
                else:
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "update" and grades_log.date_log>="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and '+personal_query
                countI = db.smart_query(db.grades_log,search).count()
                infoeLevelTemp.append(countI)
            #DELETE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "delete" and grades_log.date_log>="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'"'
                else:
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "delete" and grades_log.date_log>="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and '+personal_query
                countI = db.smart_query(db.grades_log,search).count()
                infoeLevelTemp.append(countI)
            #INSERT PROJECT
            infoLevel.append(infoeLevelTemp)
    #PER USER
    elif str(request.vars['level'])=="5":
        #VERIFY THAT CAN SHOW THE LEVEL OF THE REPORT
        usersProject = GET_USERS(period,project,roll,'grades_log')
        if len(usersProject) == 0:
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('management_reports', 'grades_management',vars=dict(level='4', period = str(request.vars['period']), month = str(request.vars['month']), project = str(request.vars['project']), type_L = str(request.vars['type_U']), type_U = str(request.vars['type_U']), querySearch=personal_query)))

        for userPT in usersProject:
            userP=db(db.auth_user.username==userPT).select().first()
            if userP is None:
                userP=db(db.grades_log.user_name==userPT).select().first()
                userP=userP.user_name
            else:
                userP=userP.username
            infoeLevelTemp = []
            #NAME OF PERIOD
            infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
            #NAME OF MONTH
            infoeLevelTemp.append(month[0])
            #NAME OF PROJECT
            infoeLevelTemp.append(project)
            #NAME OF ROLE
            infoeLevelTemp.append(T('Rol '+roll))
            #ID OF USER
            infoeLevelTemp.append(userP)
            #NAME OF USER
            infoeLevelTemp.append(userP)
            #INSERT
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                if personal_query == '':
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "insert" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'"'
                else:
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "insert" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'" and '+personal_query
                countI = db.smart_query(db.grades_log,search).count()
                infoeLevelTemp.append(countI)
            #UPDATE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "update" and grades_log.date_log>="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'"'
                else:
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "update" and grades_log.date_log>="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'" and '+personal_query
                countI = db.smart_query(db.grades_log,search).count()
                infoeLevelTemp.append(countI)
            #DELETE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "delete" and grades_log.date_log>="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'"'
                else:
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "delete" and grades_log.date_log>="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'" and '+personal_query
                countI = db.smart_query(db.grades_log,search).count()
                infoeLevelTemp.append(countI)
            #INSERT PROJECT
            infoLevel.append(infoeLevelTemp)
    #DATA
    elif str(request.vars['level'])=="6":
        if str(request.vars['type_L'])=="all":
            if personal_query == '':
                search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'"'
            else:
                search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'" and '+personal_query
        elif str(request.vars['type_L'])=="i":
            if personal_query == '':
                search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "insert" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'"'
            else:
                search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "insert" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'" and '+personal_query
        elif str(request.vars['type_L'])=="u":
            if personal_query == '':
                search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "update" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'"'
            else:
                search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "update" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'" and '+personal_query
        elif str(request.vars['type_L'])=="d":
            if personal_query == '':
                search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "delete" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'"'
            else:
                search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "delete" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<"'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'" and '+personal_query
        grid = []
        for data in db.smart_query(db.grades_log,search).select():
                grid.append(data.id)
        if len(grid) == 0:
            grid.append(-1)

        infoeLevelTemp=[]
        infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
        infoeLevelTemp.append(str(month[0]))
        infoeLevelTemp.append(str(project))
        infoeLevelTemp.append(T('Rol '+roll))
        infoeLevelTemp.append(str(userP))
        infoLevel.append(infoeLevelTemp)
        #GRID
        db.grades_log.id.readable = False
        db.grades_log.id.writable = False
        db.grades_log.user_name.readable = False
        db.grades_log.user_name.writable = False
        db.grades_log.roll.readable = False
        db.grades_log.roll.writable = False
        db.grades_log.academic_assignation_id.readable = False
        db.grades_log.academic_assignation_id.writable = False
        db.grades_log.activity_id.readable = False
        db.grades_log.activity_id.writable = False
        db.grades_log.project.readable = False
        db.grades_log.project.writable = False
        db.grades_log.yearp.readable = False
        db.grades_log.yearp.writable = False
        db.grades_log.period.readable = False
        db.grades_log.period.writable = False
        grid = SQLFORM.grid(db.grades_log.id.belongs(grid), csv=False, create=False, editable=False, deletable=False, paginate=9, searchable=False)
    return dict(fsearch=fsearch, filtered_by=filtered_by, personal_query=personal_query, infoLevel=infoLevel, top5=top5, grid=grid) 


#*************************************************************************************************************************************
#*************************************************************************************************************************************
#*****************************************************MANAGEMENT REPORT GRADES********************************************************
@auth.requires_login()
@auth.requires(auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
def evaluation_result_export():
    #VERIFI THAT ACCURATE PARAMETERS
    try:
        #CHECK IF THE TYPE OF EXPORT IS VALID
        if request.vars['list_type'] is None or str(request.vars['list_type'])!="csv":
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #CHECK THAT THE LEVEL OF REPORT IS VALID
        if (request.vars['level'] is not None) and (int(request.vars['level'])<1 or int(request.vars['level'])>5):
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('default','index'))
        
        #Check if the period is change
        if request.vars['period'] is None:
            import cpfecys
            cperiod = cpfecys.current_year_period()
            period = db(db.period_year.id==cperiod.id).select().first()
        else:
            if request.vars['period']!='':
                period = request.vars['period']
                period = db(db.period_year.id==period).select().first()
            else:
                session.flash = T('Not valid Action.')
                redirect(URL('default','index'))

        #VERIFY THAT THE PARAMETERS OF EACH LEVEL BE VALID
        if request.vars['level'] is not None:
            #LEVEL MORE THAN 1
            if int(request.vars['level'])>1:
                #CHECK IF THE TYPE OF REPORT IS VALID
                if request.vars['type_L'] is None or (str(request.vars['type_L'])!="all" and str(request.vars['type_L'])!="a" and str(request.vars['type_L'])!="r"):
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))

                evaluation = VALIDATE_EVALUATION(request.vars['evaluation'])
                if evaluation is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))
            
            #LEVEL MORE THAN 2
            if int(request.vars['level'])>2:
                #CHECK IF THE TYPE OF REPORT IS VALID                
                project = db(db.project.id==request.vars['project']).select().first()                 
                if project is None:
                    session.flash = T('Not valid Action.')
                    redi*rect(URL('default','index'))
                if request.vars['type_U'] is None or (str(request.vars['type_U'])!="all" and str(request.vars['type_U'])!="a" and str(request.vars['type_U'])!="r"):
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))

            if int(request.vars['level'])>3:
                #CHECK THE USER
                userP = db(db.auth_user.id==request.vars['user']).select().first()                 
                if userP is None:
                    session.flash = T('Not valid Action.')
                    redi*rect(URL('default','index'))

            #LEVEL MORE THAN 4
            if int(request.vars['level'])>4:
                #CHECK IF THE CATEGORY IS VALID
                category = db((db.question_repository.repository_evaluation==request.vars['evaluation'])&(db.question_repository.question_type_name==request.vars['category'])).select()
                if category is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))

    except:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))

    
    #****************************************************************************************************************
    #****************************************************************************************************************
    #*****************************************************REPORT*****************************************************
    from datetime import datetime
    #TITLE
    infoLevel = []
    infoeLevelTemp=[]
    infoeLevelTemp.append('Universidad de San Carlos de Guatemala')
    infoLevel.append(infoeLevelTemp)
    infoeLevelTemp=[]
    infoeLevelTemp.append('Facultad de Ingeniería')
    infoLevel.append(infoeLevelTemp)
    infoeLevelTemp=[]
    infoeLevelTemp.append('Escuela de Ciencias y Sistemas')
    infoLevel.append(infoeLevelTemp)
        #LEVELS OF REPORT
    if request.vars['level']=='1' or request.vars['level'] is None:
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Evaluations'))
        infoeLevelTemp.append(T('Rol'))
        infoeLevelTemp.append(T('Approveds'))
        infoeLevelTemp.append(T('Reprobates'))
        infoeLevelTemp.append(T('Total'))
        infoLevel.append(infoeLevelTemp)
        #aqui for evaluation in db(db.evaluation_result.period==period.id).select():
        for evaluation in db(db.evaluation_result.period==period.id).select(groupby=db.evaluation_result.repository_evaluation):
            infoeLevelTemp = []
            #ID OF evaluation
            infoeLevelTemp.append(evaluation.repository_evaluation)
            #NAME OF EVALUATION
            infoeLevelTemp.append((evaluation.repository_evaluation.name))
            #NAME OF ROLS
            infoeLevelTemp.append((evaluation.repository_evaluation.user_type_evaluated.role))
            
            
            count_r = 0
            count_a = 0
            for evaluation_result in db(db.evaluation_result.repository_evaluation==evaluation.repository_evaluation).select():
                result_cat = 0
                count_cat = 0
                for quetions_rep in db(db.question_repository.repository_evaluation==evaluation_result.repository_evaluation).select(groupby=db.question_repository.question_type_name):
                    count_question = 0
                    count_result = 0
                    for quetions_rep_2 in db((db.question_repository.repository_evaluation==evaluation_result.repository_evaluation)&\
                        (db.question_repository.question_type_name==quetions_rep.question_type_name)).select():
                        count_answers = 0
                        result_answers = 0
                        for var_evaluation_solve_detail in db((db.evaluation_solve_detail.evaluation_result==evaluation_result.id)\
                            &(db.evaluation_solve_detail.question_repository==quetions_rep_2.id)).select():
                            result_answers = long(result_answers + (var_evaluation_solve_detail.repository_answer.grade*var_evaluation_solve_detail.total_count)/100)
                            count_answers = count_answers + 1

                        if count_answers!= 0:
                            result_answers = long(result_answers / count_answers)

                            count_question = count_question + 1                
                            count_result = count_result + (result_answers)
                    try:
                        result_cat_temp = long(count_result*100/count_question)
                        result_cat = result_cat + result_cat_temp
                        count_cat= count_cat +1
                    except:
                        None
                result_temp = long(result_cat/count_cat)
                if result_temp < 61:
                    count_r = count_r + 1
                else:
                    count_a = count_a + 1

                
                
            infoeLevelTemp.append(count_a)
            infoeLevelTemp.append(count_r)
            
            
            
            infoeLevelTemp.append(db(db.evaluation_result.repository_evaluation==evaluation.repository_evaluation).count())
            infoLevel.append(infoeLevelTemp)

    elif str(request.vars['level'])=="2":
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Project'))

        if (str(request.vars['type_L']) == "all") or (str(request.vars['type_L']) == "a"):
            infoeLevelTemp.append(T('Approveds'))
        pass
        if (str(request.vars['type_L']) == "all") or (str(request.vars['type_L']) == "r"):
            infoeLevelTemp.append(T('Reprobates'))
        pass
        if (str(request.vars['type_L']) == "all"):
            infoeLevelTemp.append(T('Total')) 
        pass
        infoLevel.append(infoeLevelTemp)

        evaluations = db((db.evaluation_result.repository_evaluation==request.vars["evaluation"])&(db.evaluation_result.period==period.id)).select(groupby=db.evaluation_result.project)
        
        for evaluation in evaluations:
            infoeLevelTemp = []
            infoeLevelTemp.append(evaluation.project.name)
            
           
            
            count_r = 0
            count_a = 0

            for evaluation_result in db((db.evaluation_result.repository_evaluation==request.vars["evaluation"])&(db.evaluation_result.period==period.id)&(db.evaluation_result.project==evaluation.project)).select():
                result_cat = 0
                count_cat = 0
                for quetions_rep in db(db.question_repository.repository_evaluation==evaluation_result.repository_evaluation).select(groupby=db.question_repository.question_type_name):
                    count_question = 0
                    count_result = 0
                    for quetions_rep_2 in db((db.question_repository.repository_evaluation==evaluation_result.repository_evaluation)&\
                        (db.question_repository.question_type_name==quetions_rep.question_type_name)).select():
                        count_answers = 0
                        result_answers = 0
                        for var_evaluation_solve_detail in db((db.evaluation_solve_detail.evaluation_result==evaluation_result.id)\
                            &(db.evaluation_solve_detail.question_repository==quetions_rep_2.id)).select():
                            result_answers = long(result_answers + (var_evaluation_solve_detail.repository_answer.grade*var_evaluation_solve_detail.total_count)/100)
                            count_answers = count_answers + 1

                        if count_answers!= 0:
                            result_answers = long(result_answers / count_answers)

                            count_question = count_question + 1                
                            count_result = count_result + (result_answers)
                    try:
                        result_cat_temp = long(count_result*100/count_question)
                        result_cat = result_cat + result_cat_temp
                        count_cat= count_cat +1
                    except:
                        None
                result_temp = long(result_cat/count_cat)


                if result_temp < 61:
                    count_r = count_r + 1
                else:
                    count_a = count_a + 1
                

            infoeLevelTemp.append(count_a)
            infoeLevelTemp.append(count_r)
            infoeLevelTemp.append(count_a + count_r)

            infoLevel.append(infoeLevelTemp)
    
    elif str(request.vars['level'])=="3":
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('User name'))
        infoeLevelTemp.append(T('Name'))
        infoeLevelTemp.append(T('Evaluation Result'))
        infoLevel.append(infoeLevelTemp)
        evaluations = db((db.evaluation_result.repository_evaluation==request.vars["evaluation"])&(db.evaluation_result.project==request.vars["project"])&(db.evaluation_result.period==period.id)).select()
        
        for evaluation in evaluations:
            
            result_cat = 0
            count_cat = 0
            for quetions_rep in db(db.question_repository.repository_evaluation==evaluation.repository_evaluation).select(groupby=db.question_repository.question_type_name):
                count_question = 0
                count_result = 0
                for quetions_rep_2 in db((db.question_repository.repository_evaluation==evaluation.repository_evaluation)&\
                    (db.question_repository.question_type_name==quetions_rep.question_type_name)).select():
                    count_answers = 0
                    result_answers = 0
                    for var_evaluation_solve_detail in db((db.evaluation_solve_detail.evaluation_result==evaluation.id)\
                        &(db.evaluation_solve_detail.question_repository==quetions_rep_2.id)).select():
                        result_answers = long(result_answers + (var_evaluation_solve_detail.repository_answer.grade*var_evaluation_solve_detail.total_count)/100)
                        count_answers = count_answers + 1

                    if count_answers!= 0:
                        result_answers = long(result_answers / count_answers)

                        count_question = count_question + 1                
                        count_result = count_result + (result_answers)
                try: 
                    result_cat_temp = long(count_result*100/count_question)
                    result_cat = result_cat + result_cat_temp
                    count_cat= count_cat +1
                except:
                    None

            result_temp = long(result_cat/count_cat)
            
            add_user = False
            if str(request.vars['type_U'])=="all":
                add_user = True
            if str(request.vars['type_U'])=="r":
                if result_temp < 61:
                    add_user = True
            if str(request.vars['type_U'])=="a":
                if result_temp >= 61:
                    add_user = True
            if add_user == True:
                infoeLevelTemp = []
                infoeLevelTemp.append(evaluation.evaluated.username)
                infoeLevelTemp.append(evaluation.evaluated.first_name + " "+ evaluation.evaluated.last_name)
                infoeLevelTemp.append(result_temp)
                
                infoLevel.append(infoeLevelTemp)
          
    elif str(request.vars['level'])=="4":
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Category'))
        infoeLevelTemp.append(T('Result'))
        infoLevel.append(infoeLevelTemp)
        evaluation = db((db.evaluation_result.repository_evaluation==request.vars["evaluation"])&\
            (db.evaluation_result.project==request.vars["project"])&\
            (db.evaluation_result.period==period.id)&\
            (db.evaluation_result.evaluated==str(request.vars['user']))).select().first()

        for quetions_rep in db(db.question_repository.repository_evaluation==evaluation.repository_evaluation).select(groupby=db.question_repository.question_type_name):
            count_question = 0
            count_result = 0
            for quetions_rep_2 in db((db.question_repository.repository_evaluation==evaluation.repository_evaluation)&\
                (db.question_repository.question_type_name==quetions_rep.question_type_name)).select():
                count_answers = 0
                result_answers = 0
                for var_evaluation_solve_detail in db((db.evaluation_solve_detail.evaluation_result==evaluation.id)\
                    &(db.evaluation_solve_detail.question_repository==quetions_rep_2.id)).select():
                    result_answers = long(result_answers + (var_evaluation_solve_detail.repository_answer.grade*var_evaluation_solve_detail.total_count)/100)
                    count_answers = count_answers + 1

                if count_answers!= 0:
                    result_answers = long(result_answers / count_answers)

                    count_question = count_question + 1                
                    count_result = count_result + (result_answers)
                
            try:
                result_temp = long(count_result*100/count_question)
                infoeLevelTemp = []
                infoeLevelTemp.append(quetions_rep.question_type_name)
                infoeLevelTemp.append(result_temp)

                infoLevel.append(infoeLevelTemp)

            except:
                result_temp = long(-1)
                infoeLevelTemp = []
                infoeLevelTemp.append(quetions_rep.question_type_name)
                infoeLevelTemp.append(result_temp)

                infoLevel.append(infoeLevelTemp)

    elif str(request.vars['level'])=="5":
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Question'))
        infoeLevelTemp.append(T('Result'))
        infoLevel.append(infoeLevelTemp)
        evaluation = db((db.evaluation_result.repository_evaluation==request.vars["evaluation"])&\
            (db.evaluation_result.project==request.vars["project"])&\
            (db.evaluation_result.period==period.id)&\
            (db.evaluation_result.evaluated==str(request.vars['user']))).select().first()

        count_question = 0
        count_result = 0
        for quetions_rep_2 in db((db.question_repository.repository_evaluation==evaluation.repository_evaluation)&\
            (db.question_repository.question_type_name==request.vars['category'])).select():
            count_answers = 0
            result_answers = 0
            for var_evaluation_solve_detail in db((db.evaluation_solve_detail.evaluation_result==evaluation.id)\
                &(db.evaluation_solve_detail.question_repository==quetions_rep_2.id)).select():
                result_answers = long(result_answers + (var_evaluation_solve_detail.repository_answer.grade*var_evaluation_solve_detail.total_count)/100)
                count_answers = count_answers + 1

            if count_answers!= 0:
                result_answers = long(result_answers / count_answers)

                result_temp = long(result_answers*100)
                count_question = count_question + 1                
                count_result = count_result + (result_answers)
            
        
            try:
                infoeLevelTemp = []
                infoeLevelTemp.append(quetions_rep_2.question)
                infoeLevelTemp.append(result_temp)

                infoLevel.append(infoeLevelTemp)
            except:
                infoeLevelTemp = []
                infoeLevelTemp.append(quetions_rep_2.question)
                infoeLevelTemp.append(-1)

                infoLevel.append(infoeLevelTemp)
    
    #*****************************************************REPORT*****************************************************
    #****************************************************************************************************************
    #****************************************************************************************************************
    return dict(filename='ResultadoDeEvaluaciones', csvdata=infoLevel)



@auth.requires_login()
@auth.requires(auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
def evaluation_result():
    #****************************************************************************************************************
    #****************************************************************************************************************
    #******************************************VERIFY THAT ACCURATE PARAMETERS***************************************
    try:
        #CHECK THAT THE LEVEL OF REPORT IS VALID
        if (request.vars['level'] is not None) and (int(request.vars['level'])<1 or int(request.vars['level'])>5):
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))
        
        #Check if the period is change
        if request.vars['period'] is None:
            import cpfecys
            cperiod = cpfecys.current_year_period()
            period = db(db.period_year.id==cperiod.id).select().first()
        else:
            if request.vars['period']!='':
                period = request.vars['period']
                period = db(db.period_year.id==period).select().first()
            else:
                session.flash = T('Not valid Action.')
                redirect(URL('default','index'))

        #VERIFY THAT THE PARAMETERS OF EACH LEVEL BE VALID
        if request.vars['level'] is not None:
            #LEVEL MORE THAN 1
            if int(request.vars['level'])>1:
                #CHECK IF THE TYPE OF REPORT IS VALID
                if request.vars['type_L'] is None or (str(request.vars['type_L'])!="all" and str(request.vars['type_L'])!="a" and str(request.vars['type_L'])!="r"):
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))

                evaluation = VALIDATE_EVALUATION(request.vars['evaluation'])
                if evaluation is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))
            
            #LEVEL MORE THAN 2
            if int(request.vars['level'])>2:
                #CHECK IF THE TYPE OF REPORT IS VALID                
                project = db(db.project.id==request.vars['project']).select().first()                 
                if project is None:
                    session.flash = T('Not valid Action.')
                    redi*rect(URL('default','index'))
                if request.vars['type_U'] is None or (str(request.vars['type_U'])!="all" and str(request.vars['type_U'])!="a" and str(request.vars['type_U'])!="r"):
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))

            if int(request.vars['level'])>3:
                #CHECK THE USER
                userP = db(db.auth_user.id==request.vars['user']).select().first()                 
                if userP is None:
                    session.flash = T('Not valid Action.')
                    redi*rect(URL('default','index'))

            #LEVEL MORE THAN 4
            if int(request.vars['level'])>4:
                #CHECK IF THE CATEGORY IS VALID
                category = db((db.question_repository.repository_evaluation==request.vars['evaluation'])&(db.question_repository.question_type_name==request.vars['category'])).select()
                if category is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))

    except:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))

    #****************************************************************************************************************
    #****************************************************************************************************************
    #*****************************************************REPORT*****************************************************
    #LEVELS OF REPORT
    from datetime import datetime
    infoLevel = []
    top5=[]
    grid=None
    #ALL SEMESTERS
    personal_query=""
    if request.vars['level']=='1' or request.vars['level'] is None:
        
        #aqui for evaluation in db(db.evaluation_result.period==period.id).select():
        for evaluation in db(db.evaluation_result.period==period.id).select(groupby=db.evaluation_result.repository_evaluation):
            infoeLevelTemp = []
            #ID OF evaluation
            infoeLevelTemp.append(evaluation.repository_evaluation)
            #NAME OF EVALUATION
            infoeLevelTemp.append((evaluation.repository_evaluation.name))
            #NAME OF ROLS
            infoeLevelTemp.append((evaluation.repository_evaluation.user_type_evaluated.role))
            
            
            count_r = 0
            count_a = 0
            for evaluation_result in db(db.evaluation_result.repository_evaluation==evaluation.repository_evaluation).select():
                result_cat = 0
                count_cat = 0
                for quetions_rep in db(db.question_repository.repository_evaluation==evaluation_result.repository_evaluation).select(groupby=db.question_repository.question_type_name):
                    count_question = 0
                    count_result = 0
                    for quetions_rep_2 in db((db.question_repository.repository_evaluation==evaluation_result.repository_evaluation)&\
                        (db.question_repository.question_type_name==quetions_rep.question_type_name)).select():
                        count_answers = 0
                        result_answers = 0
                        for var_evaluation_solve_detail in db((db.evaluation_solve_detail.evaluation_result==evaluation_result.id)\
                            &(db.evaluation_solve_detail.question_repository==quetions_rep_2.id)).select():
                            result_answers = long(result_answers + (var_evaluation_solve_detail.repository_answer.grade*var_evaluation_solve_detail.total_count))
                            count_answers = count_answers + var_evaluation_solve_detail.total_count

                        if count_answers!= 0:
                            result_answers = long(result_answers / count_answers)

                            count_question = count_question + 1                
                            count_result = count_result + (result_answers)
                    try:
                        result_cat_temp = long(count_result/count_question)
                        result_cat = result_cat + result_cat_temp
                        count_cat= count_cat +1
                    except:
                        None
                result_temp = long(result_cat/count_cat)
                if result_temp < 61:
                    count_r = count_r + 1
                else:
                    count_a = count_a + 1

                
                
            infoeLevelTemp.append(count_a)
            infoeLevelTemp.append(count_r)
            
            
            
            infoeLevelTemp.append(db(db.evaluation_result.repository_evaluation==evaluation.repository_evaluation).count())
            infoLevel.append(infoeLevelTemp)

    elif str(request.vars['level'])=="2":
        evaluations = db((db.evaluation_result.repository_evaluation==request.vars["evaluation"])&(db.evaluation_result.period==period.id)).select(groupby=db.evaluation_result.project)
        
        for evaluation in evaluations:
            infoeLevelTemp = []
            infoeLevelTemp.append(evaluation.project)
            infoeLevelTemp.append(evaluation.project.name)
            
           
            
            count_r = 0
            count_a = 0

            for evaluation_result in db((db.evaluation_result.repository_evaluation==request.vars["evaluation"])&(db.evaluation_result.period==period.id)&(db.evaluation_result.project==evaluation.project)).select():
                result_cat = 0
                count_cat = 0
                for quetions_rep in db(db.question_repository.repository_evaluation==evaluation_result.repository_evaluation).select(groupby=db.question_repository.question_type_name):
                    count_question = 0
                    count_result = 0
                    for quetions_rep_2 in db((db.question_repository.repository_evaluation==evaluation_result.repository_evaluation)&\
                        (db.question_repository.question_type_name==quetions_rep.question_type_name)).select():
                        count_answers = 0
                        result_answers = 0
                        for var_evaluation_solve_detail in db((db.evaluation_solve_detail.evaluation_result==evaluation_result.id)\
                            &(db.evaluation_solve_detail.question_repository==quetions_rep_2.id)).select():
                            result_answers = long(result_answers + (var_evaluation_solve_detail.repository_answer.grade*var_evaluation_solve_detail.total_count))
                            count_answers = count_answers + var_evaluation_solve_detail.total_count

                        if count_answers!= 0:
                            result_answers = long(result_answers / count_answers)

                            count_question = count_question + 1                
                            count_result = count_result + (result_answers)
                    try:
                        result_cat_temp = long(count_result/count_question)
                        result_cat = result_cat + result_cat_temp
                        count_cat= count_cat +1
                    except:
                        None
                result_temp = long(result_cat/count_cat)


                if result_temp < 61:
                    count_r = count_r + 1
                else:
                    count_a = count_a + 1
                

            infoeLevelTemp.append(count_a)
            infoeLevelTemp.append(count_r)

            infoLevel.append(infoeLevelTemp)
    elif str(request.vars['level'])=="3":
        evaluations = db((db.evaluation_result.repository_evaluation==request.vars["evaluation"])&(db.evaluation_result.project==request.vars["project"])&(db.evaluation_result.period==period.id)).select()
        
        for evaluation in evaluations:
            
            result_cat = 0
            count_cat = 0
            for quetions_rep in db(db.question_repository.repository_evaluation==evaluation.repository_evaluation).select(groupby=db.question_repository.question_type_name):
                count_question = 0
                count_result = 0
                for quetions_rep_2 in db((db.question_repository.repository_evaluation==evaluation.repository_evaluation)&\
                    (db.question_repository.question_type_name==quetions_rep.question_type_name)).select():
                    count_answers = 0
                    result_answers = 0
                    for var_evaluation_solve_detail in db((db.evaluation_solve_detail.evaluation_result==evaluation.id)\
                        &(db.evaluation_solve_detail.question_repository==quetions_rep_2.id)).select():
                        result_answers = long(result_answers + (var_evaluation_solve_detail.repository_answer.grade*var_evaluation_solve_detail.total_count))
                        count_answers = count_answers + var_evaluation_solve_detail.total_count

                    if count_answers!= 0:
                        result_answers = long(result_answers / count_answers)

                        count_question = count_question + 1                
                        count_result = count_result + (result_answers)
                try: 
                    result_cat_temp = long(count_result/count_question)
                    result_cat = result_cat + result_cat_temp
                    count_cat= count_cat +1
                except:
                    None

            result_temp = long(result_cat/count_cat)
            
            add_user = False
            if str(request.vars['type_U'])=="all":
                add_user = True
            if str(request.vars['type_U'])=="r":
                if result_temp < 61:
                    add_user = True
            if str(request.vars['type_U'])=="a":
                if result_temp >= 61:
                    add_user = True
            if add_user == True:
                infoeLevelTemp = []
                infoeLevelTemp.append(evaluation.evaluated)            
                infoeLevelTemp.append(evaluation.evaluated.username)
                infoeLevelTemp.append(evaluation.evaluated.first_name + " "+ evaluation.evaluated.last_name)
                infoeLevelTemp.append(result_temp)
                
                infoLevel.append(infoeLevelTemp)
          
            
    #PER PROJECT
    elif str(request.vars['level'])=="4":
        evaluation = db((db.evaluation_result.repository_evaluation==request.vars["evaluation"])&\
            (db.evaluation_result.project==request.vars["project"])&\
            (db.evaluation_result.period==period.id)&\
            (db.evaluation_result.evaluated==str(request.vars['user']))).select().first()

        for quetions_rep in db(db.question_repository.repository_evaluation==evaluation.repository_evaluation).select(groupby=db.question_repository.question_type_name):
            count_question = 0
            count_result = 0
            for quetions_rep_2 in db((db.question_repository.repository_evaluation==evaluation.repository_evaluation)&\
                (db.question_repository.question_type_name==quetions_rep.question_type_name)).select():
                count_answers = 0
                result_answers = 0
                for var_evaluation_solve_detail in db((db.evaluation_solve_detail.evaluation_result==evaluation.id)\
                    &(db.evaluation_solve_detail.question_repository==quetions_rep_2.id)).select():
                    result_answers = long(result_answers + (var_evaluation_solve_detail.repository_answer.grade*var_evaluation_solve_detail.total_count))
                    count_answers = count_answers + var_evaluation_solve_detail.total_count

                if count_answers!= 0:
                    result_answers = long(result_answers / count_answers)

                    count_question = count_question + 1                
                    count_result = count_result + (result_answers)
                
            try:
                result_temp = long(count_result/count_question)
                infoeLevelTemp = []
                infoeLevelTemp.append(quetions_rep.question_type_name)
                infoeLevelTemp.append(result_temp)

                infoLevel.append(infoeLevelTemp)

            except:
                result_temp = long(-1)
                infoeLevelTemp = []
                infoeLevelTemp.append(quetions_rep.question_type_name)
                infoeLevelTemp.append(result_temp)

                infoLevel.append(infoeLevelTemp)

        

        
    elif str(request.vars['level'])=="5":
        evaluation = db((db.evaluation_result.repository_evaluation==request.vars["evaluation"])&\
            (db.evaluation_result.project==request.vars["project"])&\
            (db.evaluation_result.period==period.id)&\
            (db.evaluation_result.evaluated==str(request.vars['user']))).select().first()

        count_question = 0
        count_result = 0

        for quetions_rep_2 in db((db.question_repository.repository_evaluation==evaluation.repository_evaluation)&\
            (db.question_repository.question_type_name==request.vars['category'])).select():
            count_answers = 0
            result_answers = 0
            result_temp = -1
            text_show = None
            answer_detail = db((db.evaluation_solve_detail.evaluation_result==evaluation.id)\
                &(db.evaluation_solve_detail.question_repository==quetions_rep_2.id)).select()

            if answer_detail.first() is None:
                text_show = db((db.evaluation_solve_text.evaluation_result==evaluation.id)\
                &(db.evaluation_solve_text.question_repository==quetions_rep_2.id)).select()
                if text_show.first() is None:
                    text_show= None

                
            for var_evaluation_solve_detail in answer_detail:
                result_answers = long(result_answers + (var_evaluation_solve_detail.repository_answer.grade*var_evaluation_solve_detail.total_count))
                count_answers = count_answers + var_evaluation_solve_detail.total_count

            if count_answers!= 0:
                result_answers = long(result_answers / count_answers)

                result_temp = long(result_answers)
                count_question = count_question + 1                
                count_result = count_result + (result_answers)
            
        
            try:
                infoeLevelTemp = []
                infoeLevelTemp.append(quetions_rep_2.question)
                infoeLevelTemp.append(result_temp)
                infoeLevelTemp.append(text_show)

                infoLevel.append(infoeLevelTemp)
            except:
                infoeLevelTemp = []
                infoeLevelTemp.append(quetions_rep_2.question)
                infoeLevelTemp.append(-1)

                infoLevel.append(infoeLevelTemp)
    
    return dict(infoLevel=infoLevel, top5=top5, grid=grid, period_var=period) 




#*************************************************************************************************************************************
#*************************************************************************************************************************************
#*****************************************************MANAGEMENT REPORT ACTIVITIES WITH METRIC****************************************
@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def activities_withmetric_management_export():
    #VERIFI THAT ACCURATE PARAMETERS
    try:
        #CHECK IF THE TYPE OF EXPORT IS VALID
        if request.vars['list_type'] is None or str(request.vars['list_type'])!="csv":
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #CHECK THAT THE LEVEL OF REPORT IS VALID
        if request.vars['level'] is not None and (int(request.vars['level'])<1 or int(request.vars['level'])>6):
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #VERIFY THAT THE PARAMETERS OF EACH LEVEL BE VALID
        if request.vars['level'] is not None:
            #LEVEL MORE THAN 1
            if int(request.vars['level'])>1:
                #CHECK IF THE TYPE OF REPORT IS VALID
                if request.vars['type_L'] is None or (str(request.vars['type_L'])!="all" and str(request.vars['type_L'])!="i" and str(request.vars['type_L'])!="u" and str(request.vars['type_L'])!="d"):
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))

                period = VALIDATE_PERIOD(request.vars['period'])
                if period is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))

            #LEVEL MORE THAN 2
            if int(request.vars['level'])>2:
                #CHECK IF THE TYPE OF REPORT IS VALID
                if request.vars['type_U'] is None or (str(request.vars['type_U'])!="all" and str(request.vars['type_U'])!="i" and str(request.vars['type_U'])!="u" and str(request.vars['type_U'])!="d"):
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))

                #CHECK IF THE MONTH IS VALID
                month = VALIDATE_MONTH(request.vars['month'],period)
                if month is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))

            #LEVEL MORE THAN 3
            if int(request.vars['level'])>3:
                #CHECK IF THE PROJECT IS VALID
                project = VALIDATE_PROJECT(request.vars['project'],'course_activity_log')
                if project is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))

            #LEVEL MORE THAN 4
            if int(request.vars['level'])>4:
                #CHECK IF THE ROLE IS VALID
                roll = VALIDATE_ROLE(request.vars['roll'],'course_activity_log')
                if roll is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))

            #LEVEL MORE THAN 5
            if int(request.vars['level'])>5:
                #CHECK IF THE USER IS VALID
                userP = VALIDATE_USER(period,project,roll,request.vars['userP'],'course_activity_log')
                if userP is None:
                    session.flash = T('Not valid Action.')
                    redi*rect(URL('default','index'))
    except:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))

    #CHECK IF THERE IS A PERSONALIZED QUERY
    personal_query = ''
    if request.vars['querySearch'] is not None and str(request.vars['querySearch']) != "":
        #PERSONALIZED QUERY SURE WORK
        try:
            personal_query = str(request.vars['querySearch'])
            countI = db.smart_query(db.course_activity_log,personal_query).count()
        except:
            personal_query = ''

    #****************************************************************************************************************
    #****************************************************************************************************************
    #*****************************************************REPORT*****************************************************
    from datetime import datetime
    #TITLE
    infoLevel = []
    infoeLevelTemp=[]
    infoeLevelTemp.append('Universidad de San Carlos de Guatemala')
    infoLevel.append(infoeLevelTemp)
    infoeLevelTemp=[]
    infoeLevelTemp.append('Facultad de Ingeniería')
    infoLevel.append(infoeLevelTemp)
    infoeLevelTemp=[]
    infoeLevelTemp.append('Escuela de Ciencias y Sistemas')
    infoLevel.append(infoeLevelTemp)
    #TYPE OF REPORT
    infoeLevelTemp=[]
    infoeLevelTemp.append(T('Type'))
    infoeLevelTemp.append(T('Metrics Management Course Activities'))
    infoLevel.append(infoeLevelTemp)
    #DESCRIPTION OF REPORT
    infoeLevelTemp=[]
    infoeLevelTemp.append(T('Description'))
    infoeLevelTemp.append(T('Report of operations management activities metric course'))
    infoLevel.append(infoeLevelTemp)
    #LEVELS OF REPORT
    #ALL SEMESTERS
    if request.vars['level'] is None or str(request.vars['level'])=="1":
        #MIDDLE LINE OF REPORT
        infoeLevelTemp=[]
        infoLevel.append(infoeLevelTemp)
        #LABLE DETAIL OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Detail'))
        infoLevel.append(infoeLevelTemp)
        #LABELS OF DATA OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Period'))
        infoeLevelTemp.append(T('Total inserted'))
        infoeLevelTemp.append(T('Total modified'))
        infoeLevelTemp.append(T('Total out'))
        infoLevel.append(infoeLevelTemp)
        for period in db(db.period_year).select(orderby=~db.period_year.id):
            infoeLevelTemp = []
            #NAME OF PERIOD
            infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
            #INSERT
            if personal_query == '':
                search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "insert"'
            else:
                search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "insert" and '+personal_query
            countI = db.smart_query(db.course_activity_log,search).count()
            infoeLevelTemp.append(countI)
            #UPDATE
            if personal_query == '':
                search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "update"'
            else:
                search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "update" and '+personal_query
            countI = db.smart_query(db.course_activity_log,search).count()
            infoeLevelTemp.append(countI)
            #DELETE
            if personal_query == '':
                search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "delete"'
            else:
                search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "delete" and '+personal_query
            countI = db.smart_query(db.course_activity_log,search).count()
            infoeLevelTemp.append(countI)
            #INSERT PERIOD
            infoLevel.append(infoeLevelTemp)
    #PER MONTH
    elif str(request.vars['level'])=="2":
        #PERIOD OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Period'))
        infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
        infoLevel.append(infoeLevelTemp)
        #MIDDLE LINE OF REPORT
        infoeLevelTemp=[]
        infoLevel.append(infoeLevelTemp)
        #LABLE DETAIL OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Detail'))
        infoLevel.append(infoeLevelTemp)
        #LABELS OF DATA OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Month'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
            infoeLevelTemp.append(T('Total inserted'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
            infoeLevelTemp.append(T('Total modified'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
            infoeLevelTemp.append(T('Total out'))
        infoLevel.append(infoeLevelTemp)

        for month in GET_MONTH_PERIOD(period):
            start = datetime.strptime(str(period.yearp) + '-' + str(month[0]) +'-01', "%Y-%m-%d")
            if month[2]==1:
                end = datetime.strptime(str(period.yearp+1) + '-' + str(month[2]) +'-01', "%Y-%m-%d")
            else:
                end = datetime.strptime(str(period.yearp) + '-' + str(month[2]) +'-01', "%Y-%m-%d")
            infoeLevelTemp = []
            #NAME OF MONTH
            infoeLevelTemp.append(month[1]+' '+str(period.yearp))
            #INSERT
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                if personal_query == '':
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "insert" and course_activity_log.date_log >="'+str(start)+'" and course_activity_log.date_log<"'+str(end)+'"'
                else:
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "insert" and course_activity_log.date_log >="'+str(start)+'" and course_activity_log.date_log<"'+str(end)+'" and '+personal_query
                countI = db.smart_query(db.course_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #UPDATE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "update" and course_activity_log.date_log>="'+str(start)+'" and course_activity_log.date_log<"'+str(end)+'"'
                else:
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "update" and course_activity_log.date_log>="'+str(start)+'" and course_activity_log.date_log<"'+str(end)+'" and '+personal_query
                countI = db.smart_query(db.course_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #DELETE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "delete" and course_activity_log.date_log>="'+str(start)+'" and course_activity_log.date_log<"'+str(end)+'"'
                else:
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "delete" and course_activity_log.date_log>="'+str(start)+'" and course_activity_log.date_log<"'+str(end)+'" and '+personal_query
                countI = db.smart_query(db.course_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #INSERT MONTH
            infoLevel.append(infoeLevelTemp)
    #PER PROJECT
    elif str(request.vars['level'])=="3":
        #PROJECTS
        projects = GET_PROJECTS('course_activity_log')
        projects=sorted(projects)
        #PERIOD OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Period'))
        infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
        infoLevel.append(infoeLevelTemp)
        #MONTH OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Month'))
        infoeLevelTemp.append(str(month[0]))
        infoLevel.append(infoeLevelTemp)
        #MIDDLE LINE OF REPORT
        infoeLevelTemp=[]
        infoLevel.append(infoeLevelTemp)
        #LABLE DETAIL OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Detail'))
        infoLevel.append(infoeLevelTemp)
        #LABELS OF DATA OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Project'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
            infoeLevelTemp.append(T('Total inserted'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
            infoeLevelTemp.append(T('Total modified'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
            infoeLevelTemp.append(T('Total out'))
        infoLevel.append(infoeLevelTemp)

        for projectT in projects:
            project=db(db.project.name==projectT).select().first()
            if project is None:
                project=db(db.course_activity_log.course==projectT).select().first()
                project=project.project
            else:
                project=project.name
            infoeLevelTemp = []
            #NAME OF PROJECT
            infoeLevelTemp.append(project)
            #INSERT
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                if personal_query == '':
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "insert" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+project+'"'
                else:
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "insert" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+project+'" and '+personal_query
                countI = db.smart_query(db.course_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #UPDATE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "update" and course_activity_log.date_log>="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+project+'"'
                else:
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "update" and course_activity_log.date_log>="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+project+'" and '+personal_query
                countI = db.smart_query(db.course_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #DELETE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "delete" and course_activity_log.date_log>="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+project+'"'
                else:
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "delete" and course_activity_log.date_log>="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+project+'" and '+personal_query
                countI = db.smart_query(db.course_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #INSERT PROJECT
            infoLevel.append(infoeLevelTemp)
    #PER ROL
    elif str(request.vars['level'])=="4":
        #ROLES
        roles = GET_ROLES('course_activity_log')
        #PERIOD OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Period'))
        infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
        infoLevel.append(infoeLevelTemp)
        #MONTH OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Month'))
        infoeLevelTemp.append(str(month[0]))
        infoLevel.append(infoeLevelTemp)
        #PROJECT OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Project'))
        infoeLevelTemp.append(str(project))
        infoLevel.append(infoeLevelTemp)
        #MIDDLE LINE OF REPORT
        infoeLevelTemp=[]
        infoLevel.append(infoeLevelTemp)
        #LABLE DETAIL OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Detail'))
        infoLevel.append(infoeLevelTemp)
        #LABELS OF DATA OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Role'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
            infoeLevelTemp.append(T('Total inserted'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
            infoeLevelTemp.append(T('Total modified'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
            infoeLevelTemp.append(T('Total out'))
        infoLevel.append(infoeLevelTemp)

        for rollT in roles:
            roll=db(db.auth_group.role==rollT).select().first()
            if roll is None:
                roll=db(db.course_activity_log.roll==rollT).select().first()
                roll=roll.roll
            else:
                roll=roll.role
            infoeLevelTemp = []
            #NAME OF ROLE
            infoeLevelTemp.append(T('Rol '+roll))
            #INSERT
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                if personal_query == '':
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "insert" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'"'
                else:
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "insert" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and '+personal_query
                countI = db.smart_query(db.course_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #UPDATE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "update" and course_activity_log.date_log>="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'"'
                else:
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "update" and course_activity_log.date_log>="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and '+personal_query
                countI = db.smart_query(db.course_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #DELETE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "delete" and course_activity_log.date_log>="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'"'
                else:
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "delete" and course_activity_log.date_log>="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and '+personal_query
                countI = db.smart_query(db.course_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #INSERT PROJECT
            infoLevel.append(infoeLevelTemp)
    #PER USER
    elif str(request.vars['level'])=="5":
        #USERS
        usersProject = GET_USERS(period,project,roll,'course_activity_log')
        #PERIOD OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Period'))
        infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
        infoLevel.append(infoeLevelTemp)
        #MONTH OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Month'))
        infoeLevelTemp.append(str(month[0]))
        infoLevel.append(infoeLevelTemp)
        #PROJECT OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Project'))
        infoeLevelTemp.append(str(project))
        infoLevel.append(infoeLevelTemp)
        #ROL OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Role'))
        infoeLevelTemp.append(T('Rol '+roll))
        infoLevel.append(infoeLevelTemp)
        #MIDDLE LINE OF REPORT
        infoeLevelTemp=[]
        infoLevel.append(infoeLevelTemp)
        #LABLE DETAIL OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Detail'))
        infoLevel.append(infoeLevelTemp)
        #LABELS OF DATA OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('User'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
            infoeLevelTemp.append(T('Total inserted'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
            infoeLevelTemp.append(T('Total modified'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
            infoeLevelTemp.append(T('Total out'))
        infoLevel.append(infoeLevelTemp)

        for userPT in usersProject:
            userP=db(db.auth_user.username==userPT).select().first()
            if userP is None:
                userP=db(db.course_activity_log.user_name==userPT).select().first()
                userP=userP.user_name
            else:
                userP=userP.username
            infoeLevelTemp = []
            #NAME OF USER
            infoeLevelTemp.append(userP)
            #INSERT
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                if personal_query == '':
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "insert" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'"'
                else:
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "insert" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'" and '+personal_query
                countI = db.smart_query(db.course_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #UPDATE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "update" and course_activity_log.date_log>="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'"'
                else:
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "update" and course_activity_log.date_log>="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'" and '+personal_query
                countI = db.smart_query(db.course_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #DELETE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "delete" and course_activity_log.date_log>="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'"'
                else:
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "delete" and course_activity_log.date_log>="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'" and '+personal_query
                countI = db.smart_query(db.course_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #INSERT PROJECT
            infoLevel.append(infoeLevelTemp)
    #DATA
    elif str(request.vars['level'])=="6":
        if str(request.vars['type_L'])=="all":
            if personal_query == '':
                search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'"'
            else:
                search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'" and '+personal_query
        elif str(request.vars['type_L'])=="i":
            if personal_query == '':
                search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "insert" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'"'
            else:
                search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "insert" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'" and '+personal_query
        elif str(request.vars['type_L'])=="u":
            if personal_query == '':
                search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "update" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'"'
            else:
                search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "update" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'" and '+personal_query
        elif str(request.vars['type_L'])=="d":
            if personal_query == '':
                search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "delete" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'"'
            else:
                search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "delete" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'" and '+personal_query
        #PERIOD
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Period'))
        infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
        infoLevel.append(infoeLevelTemp)
        #MONTH
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Month'))
        infoeLevelTemp.append(str(month[0]))
        infoLevel.append(infoeLevelTemp)
        #PROJECT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Project'))
        infoeLevelTemp.append(str(project))
        infoLevel.append(infoeLevelTemp)
        #ROL
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Role'))
        infoeLevelTemp.append(T('Rol '+roll))
        infoLevel.append(infoeLevelTemp)
        #USER
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('User'))
        infoeLevelTemp.append(str(userP))
        infoLevel.append(infoeLevelTemp)
        #MIDDLE LINE
        infoeLevelTemp=[]
        infoeLevelTemp.append('')
        infoLevel.append(infoeLevelTemp)
        #DETAIL
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Detail'))
        infoLevel.append(infoeLevelTemp)
        #TITLE OF TABLE
        infoeLevelTemp=[]
        infoeLevelTemp.append('Operación')
        infoeLevelTemp.append('Categoria Anterior')
        infoeLevelTemp.append('Categoria Actual')
        infoeLevelTemp.append('Nombre Anterior')
        infoeLevelTemp.append('Nombre Actual')
        infoeLevelTemp.append('Descripcion Anterior')
        infoeLevelTemp.append('Descripcion Actual')
        infoeLevelTemp.append('Nota Anterior')
        infoeLevelTemp.append('Nota Actual')
        infoeLevelTemp.append('Laboratorio Anterior')
        infoeLevelTemp.append('Laboratorio Actual')
        infoeLevelTemp.append('Permiso Catedratico Anterior')
        infoeLevelTemp.append('Permiso Catedratico Actual')
        infoeLevelTemp.append('Fecha Inicio Anterior')
        infoeLevelTemp.append('Fecha Inicio Actual')
        infoeLevelTemp.append('Fecha Finalizacion Anterior')
        infoeLevelTemp.append('Fecha Finalizacion Actual')
        infoeLevelTemp.append('Fecha')
        infoLevel.append(infoeLevelTemp)
        for operation in db.smart_query(db.course_activity_log,search).select():
            infoeLevelTemp=[]
            infoeLevelTemp.append(operation.operation_log)
            infoeLevelTemp.append(operation.before_course_activity_category)
            infoeLevelTemp.append(operation.after_course_activity_category)
            infoeLevelTemp.append(operation.before_name)
            infoeLevelTemp.append(operation.after_name)
            infoeLevelTemp.append(operation.before_description)
            infoeLevelTemp.append(operation.after_description)
            infoeLevelTemp.append(operation.before_grade)
            infoeLevelTemp.append(operation.after_grade)
            infoeLevelTemp.append(operation.before_laboratory)
            infoeLevelTemp.append(operation.after_laboratory)
            infoeLevelTemp.append(operation.before_teacher_permition)
            infoeLevelTemp.append(operation.after_teacher_permition)
            infoeLevelTemp.append(operation.before_date_start)
            infoeLevelTemp.append(operation.after_date_start)
            infoeLevelTemp.append(operation.before_date_finish)
            infoeLevelTemp.append(operation.after_date_finish)
            infoeLevelTemp.append(operation.date_log)
            infoLevel.append(infoeLevelTemp)
    #*****************************************************REPORT*****************************************************
    #****************************************************************************************************************
    #****************************************************************************************************************
    return dict(filename='ReporteGestionActividadesConMetrica', csvdata=infoLevel)


@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def activities_withmetric_management():
    #****************************************************************************************************************
    #****************************************************************************************************************
    #***************************************CHECK IF THERE IS A PERSONALIZED QUERY***********************************
    personal_query = ''
    makeRedirect = False
    if request.vars['querySearch'] is not None and str(request.vars['querySearch']) != "":
        #PERSONALIZED QUERY SURE WORK
        try:
            personal_query = str(request.vars['querySearch'])
            countI = db.smart_query(db.course_activity_log,personal_query).count()
            if request.vars['searchT'] is not None and str(request.vars['searchT']) == 'T':
                makeRedirect = True
        except:
            response.flash = T('The query is not valid. The report is displayed without applying any query.')
            personal_query = ''
    if makeRedirect == True:
        redirect(URL('management_reports', 'activities_withmetric_management',vars=dict(level = 6, period = request.vars['period'], month = str(request.vars['month']), project = str(request.vars['project']), roll = str(request.vars['roll']), userP = str(request.vars['userP']), type_L=request.vars['type_L'], type_U=request.vars['type_U'], querySearch=request.vars['querySearch'])))


    #****************************************************************************************************************
    #****************************************************************************************************************
    #******************************************VERIFY THAT ACCURATE PARAMETERS***************************************
    try:
        #CHECK THAT THE LEVEL OF REPORT IS VALID
        if request.vars['level'] is not None and (int(request.vars['level'])<1 or int(request.vars['level'])>6):
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #VERIFY THAT THE PARAMETERS OF EACH LEVEL BE VALID
        if request.vars['level'] is not None:
            #LEVEL MORE THAN 1
            if int(request.vars['level'])>1:
                #CHECK IF THE TYPE OF REPORT IS VALID
                if request.vars['type_L'] is None or (str(request.vars['type_L'])!="all" and str(request.vars['type_L'])!="i" and str(request.vars['type_L'])!="u" and str(request.vars['type_L'])!="d"):
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))

                period = VALIDATE_PERIOD(request.vars['period'])
                if period is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))

            #LEVEL MORE THAN 2
            if int(request.vars['level'])>2:
                #CHECK IF THE TYPE OF REPORT IS VALID
                if request.vars['type_U'] is None or (str(request.vars['type_U'])!="all" and str(request.vars['type_U'])!="i" and str(request.vars['type_U'])!="u" and str(request.vars['type_U'])!="d"):
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))

                #CHECK IF THE MONTH IS VALID
                month = VALIDATE_MONTH(request.vars['month'],period)
                if month is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))

            #LEVEL MORE THAN 3
            if int(request.vars['level'])>3:
                #CHECK IF THE PROJECT IS VALID
                project = VALIDATE_PROJECT(request.vars['project'],'course_activity_log')
                if project is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))

            #LEVEL MORE THAN 4
            if int(request.vars['level'])>4:
                #CHECK IF THE ROLE IS VALID
                roll = VALIDATE_ROLE(request.vars['roll'],'course_activity_log')
                if roll is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))

            #LEVEL MORE THAN 5
            if int(request.vars['level'])>5:
                #CHECK IF THE USER IS VALID
                userP = VALIDATE_USER(period,project,roll,request.vars['userP'],'course_activity_log')
                if userP is None:
                    session.flash = T('Not valid Action.')
                    redi*rect(URL('default','index'))
    except:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))


    #****************************************************************************************************************
    #****************************************************************************************************************
    #**************************************************SEARCH REPORT*************************************************
    def filtered_by(flag):
        fsearch_Option=[]
        fsearch_Option.append('=')
        fsearch_Option.append('!=')
        fsearch_Option.append('<')
        fsearch_Option.append('>')
        fsearch_Option.append('<=')
        fsearch_Option.append('>=')
        if flag==True:
            fsearch_Option.append('starts with')
            fsearch_Option.append('contains')
            fsearch_Option.append('in')
            fsearch_Option.append('not in')
        return fsearch_Option
    
    fsearch = []
    #******************************COMBOS INFORMATION******************************
    #YEARS
    if request.vars['level']=='1' or request.vars['level'] is None:
        groupYears = GET_YEARS()
        if len(groupYears) != 0:
            fsearch.append(['yearp','Año',False,[3,sorted(groupYears)]])
    #PROJECTS
    if request.vars['level'] is None or int(request.vars['level'])<=3:
        projects = GET_PROJECTS('course_activity_log')
        if len(projects) != 0:
            fsearch_Values=[]
            fsearch_Values.append(4)
            for projectT in projects:
                project=db(db.project.name==projectT).select().first()
                if project is None:
                    project=db(db.course_activity_log.course==projectT).select().first()
                    project=project.course
                else:
                    project=project.name
                fsearch_Values.append(project)
            fsearch.append(['course','Curso',False,fsearch_Values])
    #ROLES
    if request.vars['level'] is None or int(request.vars['level'])<=4:
        roles = GET_ROLES('course_activity_log')
        if len(roles) != 0:
            fsearch.append(['roll','Rol',False,[5,sorted(roles)]])
    #CATEGORIES BEFORE
    groupCategories = GET_CATEGORIES('course_activity_log')
    if len(groupCategories) != 0:
        fsearch.append(['before_course_activity_category','Categoria Anterior',False,[3,sorted(groupCategories)]])
    #CATEGORIES AFTER
    if len(groupCategories) != 0:
        fsearch.append(['after_course_activity_category','Categoria Actual',False,[3,sorted(groupCategories)]])
    #ACTIVITIES BEFORE
    groupActivities = GET_ACTIVITIES('course_activity_log')
    if len(groupActivities) != 0:
        fsearch.append(['before_name','Nombre Anterior',False,[3,sorted(groupActivities)]])
    #ACTIVITIES AFTER
    if len(groupActivities) != 0:
        fsearch.append(['after_name','Nombre Actual',False,[3,sorted(groupActivities)]])
    #DATE
    groupDates = GET_DATES('course_activity_log')
    if len(groupDates) != 0:
        fsearch.append(['date_log','Fecha',False,[3,sorted(groupDates)]])
    #OPERATION LOG
    fsearch.append(['operation_log','Operación',False,[3,['insert','update','delete']]])
    #******************************ENTERING USER******************************
    if request.vars['level'] is None or int(request.vars['level'])<=5:
        #ID OF PERSON WHO REGISTER THE GRADE
        fsearch.append(['user_name','Usuario Registro',True,[1]])
    #BEFORE DESCRIPTION OF ACTIVITY
    fsearch.append(['before_description','Descripción Anterior',True,[1]])
    #OFFICIAL DESCRIPTION OF ACTIVITY
    fsearch.append(['after_description','Descripción Actual',True,[1]])
    #BEFORE GRADE
    fsearch.append(['before_grade','Nota Anterior',False,[1]])
    #OFFICIAL GRADE
    fsearch.append(['after_grade','Nota Actual',False,[1]])
    #BEFORE DATE START
    fsearch.append(['before_date_start','Fecha Inicio Anterior',False,[2]])
    #OFFICIAL DATE START
    fsearch.append(['after_date_start','Fecha Inicio Actual',False,[2]])
    #BEFORE DATE FINISH
    fsearch.append(['before_date_finish','Fecha Finalizacion Anterior',False,[2]])
    #OFFICIAL DATE FINISH
    fsearch.append(['after_date_finish','Fecha Finalizacion Actual',False,[2]])
    #LABORATORY BEFORE
    fsearch.append(['before_laboratory','Laboratorio Anterior',False,[6,['True','False']]])
    #LABORATORY AFTER
    fsearch.append(['after_laboratory','Laboratorio Actual',False,[6,['True','False']]])
    #PERMITION TEACHER BEFORE
    fsearch.append(['before_teacher_permition','Permiso Catedratico Anterior',False,[6,['True','False']]])
    #PERMITION TEACHER AFTER
    fsearch.append(['after_teacher_permition','Permiso Catedratico Actual',False,[6,['True','False']]])


    


    #****************************************************************************************************************
    #****************************************************************************************************************
    #*****************************************************REPORT*****************************************************
    #LEVELS OF REPORT
    from datetime import datetime
    infoLevel = []
    top5=[]
    grid=None
    #ALL SEMESTERS
    if request.vars['level'] is None or str(request.vars['level'])=="1":
        if db(db.period_year).select().first() is None:
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('default','index'))
            

        for period in db(db.period_year).select(orderby=~db.period_year.id):
            infoeLevelTemp = []
            #ID OF PERIOD
            infoeLevelTemp.append(period.id)
            #NAME OF PERIOD
            infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
            #INSERT
            if personal_query == '':
                search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "insert"'
            else:
                search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "insert" and '+personal_query
            countI = db.smart_query(db.course_activity_log,search).count()
            infoeLevelTemp.append(countI)
            #UPDATE
            if personal_query == '':
                search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "update"'
            else:
                search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "update" and '+personal_query
            countI = db.smart_query(db.course_activity_log,search).count()
            infoeLevelTemp.append(countI)
            #DELETE
            if personal_query == '':
                search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "delete"'
            else:
                search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "delete" and '+personal_query
            countI = db.smart_query(db.course_activity_log,search).count()
            infoeLevelTemp.append(countI)
            #INSERT PERIOD
            infoLevel.append(infoeLevelTemp)

        #TOP 5 OF PERIOD
        if personal_query == '':
            search='course_activity_log.id != "-1"'
        else:
            search=personal_query
        top5 = db.smart_query(db.course_activity_log,search).select(db.course_activity_log.period, db.course_activity_log.yearp, db.course_activity_log.id.count(), orderby=~db.course_activity_log.id.count(), limitby=(0, 5), groupby=[db.course_activity_log.period, db.course_activity_log.yearp])
    #PER MONTH
    elif str(request.vars['level'])=="2":
        for month in GET_MONTH_PERIOD(period):
            start = datetime.strptime(str(period.yearp) + '-' + str(month[0]) +'-01', "%Y-%m-%d")
            if month[2]==1:
                end = datetime.strptime(str(period.yearp+1) + '-' + str(month[2]) +'-01', "%Y-%m-%d")
            else:
                end = datetime.strptime(str(period.yearp) + '-' + str(month[2]) +'-01', "%Y-%m-%d")
            infoeLevelTemp = []
            #NAME OF PERIOD
            infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
            #ID OF MONTH
            infoeLevelTemp.append(month[0])
            #NAME OF MONTH
            infoeLevelTemp.append(month[1]+' '+str(period.yearp))
            #INSERT
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                if personal_query == '':
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "insert" and course_activity_log.date_log >="'+str(start)+'" and course_activity_log.date_log<"'+str(end)+'"'
                else:
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "insert" and course_activity_log.date_log >="'+str(start)+'" and course_activity_log.date_log<"'+str(end)+'" and '+personal_query
                countI = db.smart_query(db.course_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #UPDATE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "update" and course_activity_log.date_log>="'+str(start)+'" and course_activity_log.date_log<"'+str(end)+'"'
                else:
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "update" and course_activity_log.date_log>="'+str(start)+'" and course_activity_log.date_log<"'+str(end)+'" and '+personal_query
                countI = db.smart_query(db.course_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #DELETE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "delete" and course_activity_log.date_log>="'+str(start)+'" and course_activity_log.date_log<"'+str(end)+'"'
                else:
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "delete" and course_activity_log.date_log>="'+str(start)+'" and course_activity_log.date_log<"'+str(end)+'" and '+personal_query
                countI = db.smart_query(db.course_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #INSERT MONTH
            infoLevel.append(infoeLevelTemp)
    #PER PROJECT
    elif str(request.vars['level'])=="3":
        if len(projects) == 0:
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('management_reports', 'activities_withmetric_management',vars=dict(level='2',period = str(request.vars['period']), type_L = str(request.vars['type_U']), querySearch=personal_query)))
        projects=sorted(projects)

        for projectT in projects:
            project=db(db.project.name==projectT).select().first()
            if project is None:
                project=db(db.course_activity_log.course==projectT).select().first()
                project=project.project
            else:
                project=project.name
            infoeLevelTemp = []
            #NAME OF PERIOD
            infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
            #NAME OF MONTH
            infoeLevelTemp.append(month[0])
            #ID OF PROJECT
            infoeLevelTemp.append(project)
            #NAME OF PROJECT
            infoeLevelTemp.append(project)
            #INSERT
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                if personal_query == '':
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "insert" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+project+'"'
                else:
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "insert" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+project+'" and '+personal_query
                countI = db.smart_query(db.course_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #UPDATE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "update" and course_activity_log.date_log>="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+project+'"'
                else:
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "update" and course_activity_log.date_log>="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+project+'" and '+personal_query
                countI = db.smart_query(db.course_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #DELETE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "delete" and course_activity_log.date_log>="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+project+'"'
                else:
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "delete" and course_activity_log.date_log>="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+project+'" and '+personal_query
                countI = db.smart_query(db.course_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #INSERT PROJECT
            infoLevel.append(infoeLevelTemp)

        #TOP 5 OF PROJECT
        if personal_query == '':
            search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'"'
        else:
            search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and '+personal_query
        top5 = db.smart_query(db.course_activity_log,search).select(db.course_activity_log.course, db.course_activity_log.id.count(), orderby=~db.course_activity_log.id.count(), limitby=(0, 5), groupby=db.course_activity_log.course)
    #PER ROL
    elif str(request.vars['level'])=="4":
        if len(roles) == 0:
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('management_reports', 'activities_withmetric_management',vars=dict(level='3', period = str(request.vars['period']), month = str(request.vars['month']), type_L = str(request.vars['type_U']), type_U = str(request.vars['type_U']), querySearch=personal_query)))

        for rollT in roles:
            roll=db(db.auth_group.role==rollT).select().first()
            if roll is None:
                roll=db(db.course_activity_log.roll==rollT).select().first()
                roll=roll.roll
            else:
                roll=roll.role
            infoeLevelTemp = []
            #NAME OF PERIOD
            infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
            #NAME OF MONTH
            infoeLevelTemp.append(month[0])
            #NAME OF PROJECT
            infoeLevelTemp.append(project)
            #ID OF ROLE
            infoeLevelTemp.append(roll)
            #NAME OF ROLE
            infoeLevelTemp.append(T('Rol '+roll))
            #INSERT
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                if personal_query == '':
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "insert" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'"'
                else:
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "insert" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and '+personal_query
                countI = db.smart_query(db.course_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #UPDATE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "update" and course_activity_log.date_log>="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'"'
                else:
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "update" and course_activity_log.date_log>="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and '+personal_query
                countI = db.smart_query(db.course_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #DELETE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "delete" and course_activity_log.date_log>="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'"'
                else:
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "delete" and course_activity_log.date_log>="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and '+personal_query
                countI = db.smart_query(db.course_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #INSERT PROJECT
            infoLevel.append(infoeLevelTemp)
    #PER USER
    elif str(request.vars['level'])=="5":
        #VERIFY THAT CAN SHOW THE LEVEL OF THE REPORT
        usersProject = GET_USERS(period,project,roll,'course_activity_log')
        if len(usersProject) == 0:
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('management_reports', 'activities_withmetric_management',vars=dict(level='4', period = str(request.vars['period']), month = str(request.vars['month']), project = str(request.vars['project']), type_L = str(request.vars['type_U']), type_U = str(request.vars['type_U']), querySearch=personal_query)))

        for userPT in usersProject:
            userP=db(db.auth_user.username==userPT).select().first()
            if userP is None:
                userP=db(db.course_activity_log.user_name==userPT).select().first()
                userP=userP.user_name
            else:
                userP=userP.username
            infoeLevelTemp = []
            #NAME OF PERIOD
            infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
            #NAME OF MONTH
            infoeLevelTemp.append(month[0])
            #NAME OF PROJECT
            infoeLevelTemp.append(project)
            #NAME OF ROLE
            infoeLevelTemp.append(T('Rol '+roll))
            #ID OF USER
            infoeLevelTemp.append(userP)
            #NAME OF USER
            infoeLevelTemp.append(userP)
            #INSERT
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                if personal_query == '':
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "insert" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'"'
                else:
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "insert" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'" and '+personal_query
                countI = db.smart_query(db.course_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #UPDATE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "update" and course_activity_log.date_log>="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'"'
                else:
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "update" and course_activity_log.date_log>="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'" and '+personal_query
                countI = db.smart_query(db.course_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #DELETE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "delete" and course_activity_log.date_log>="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'"'
                else:
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "delete" and course_activity_log.date_log>="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'" and '+personal_query
                countI = db.smart_query(db.course_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #INSERT PROJECT
            infoLevel.append(infoeLevelTemp)
    #DATA
    elif str(request.vars['level'])=="6":
        if str(request.vars['type_L'])=="all":
            if personal_query == '':
                search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'"'
            else:
                search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'" and '+personal_query
        elif str(request.vars['type_L'])=="i":
            if personal_query == '':
                search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "insert" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'"'
            else:
                search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "insert" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'" and '+personal_query
        elif str(request.vars['type_L'])=="u":
            if personal_query == '':
                search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "update" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'"'
            else:
                search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "update" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'" and '+personal_query
        elif str(request.vars['type_L'])=="d":
            if personal_query == '':
                search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "delete" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'"'
            else:
                search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "delete" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<"'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'" and '+personal_query
        grid = []
        for data in db.smart_query(db.course_activity_log,search).select():
            grid.append(data.id)
        #REPORT
        if len(grid) == 0:
            grid.append(-1)

        infoeLevelTemp=[]
        infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
        infoeLevelTemp.append(str(month[0]))
        infoeLevelTemp.append(str(project))
        infoeLevelTemp.append(T('Rol '+roll))
        infoeLevelTemp.append(str(userP))
        infoLevel.append(infoeLevelTemp)
        #GRID
        db.course_activity_log.id.readable = False
        db.course_activity_log.id.writable = False
        db.course_activity_log.user_name.readable = False
        db.course_activity_log.user_name.writable = False
        db.course_activity_log.roll.readable = False
        db.course_activity_log.roll.writable = False
        db.course_activity_log.course.readable = False
        db.course_activity_log.course.writable = False
        db.course_activity_log.yearp.readable = False
        db.course_activity_log.yearp.writable = False
        db.course_activity_log.period.readable = False
        db.course_activity_log.period.writable = False
        db.course_activity_log.metric.readable = False
        db.course_activity_log.metric.writable = False
        db.course_activity_log.before_file.readable = False
        db.course_activity_log.before_file.writable = False
        db.course_activity_log.after_file.readable = False
        db.course_activity_log.after_file.writable = False
        grid = SQLFORM.grid(db.course_activity_log.id.belongs(grid), csv=False, create=False, editable=False, deletable=False, paginate=9, searchable=False)
    return dict(fsearch=fsearch, filtered_by=filtered_by, personal_query=personal_query, infoLevel=infoLevel, top5=top5, grid=grid)


#*************************************************************************************************************************************
#*************************************************************************************************************************************
#*****************************************************MANAGEMENT REPORT STUDENTS******************************************************
@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def student_management_export():
    #VERIFI THAT ACCURATE PARAMETERS
    try:
        #CHECK IF THE TYPE OF EXPORT IS VALID
        if request.vars['list_type'] is None or str(request.vars['list_type'])!="csv":
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #CHECK THAT THE LEVEL OF REPORT IS VALID
        if request.vars['level'] is not None and (int(request.vars['level'])<1 or int(request.vars['level'])>5):
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('default','index'))
        
        #VERIFY THAT THE PARAMETERS OF EACH LEVEL BE VALID
        if request.vars['level'] is not None:
            #LEVEL MORE THAN 1
            if int(request.vars['level'])>1:
                #CHECK IF THE TYPE OF REPORT IS VALID
                if request.vars['type_L'] is None or (str(request.vars['type_L'])!="all" and str(request.vars['type_L'])!="i" and str(request.vars['type_L'])!="u" and str(request.vars['type_L'])!="d"):
                    session.flash = T('Report no visible: There are no parameters required to display the report.')
                    redirect(URL('default','index'))

                period = VALIDATE_PERIOD(request.vars['period'])
                if period is None:
                    session.flash = T('Report no visible: There are no parameters required to display the report.')
                    redirect(URL('default','index'))
            
            #LEVEL MORE THAN 2
            if int(request.vars['level'])>2:
                #CHECK IF THE TYPE OF REPORT IS VALID
                if request.vars['type_U'] is None or (str(request.vars['type_U'])!="all" and str(request.vars['type_U'])!="i" and str(request.vars['type_U'])!="u" and str(request.vars['type_U'])!="d"):
                    session.flash = T('Report no visible: There are no parameters required to display the report.')
                    redirect(URL('default','index'))

                #CHECK IF THE MONTH IS VALID
                month = VALIDATE_MONTH(request.vars['month'],period)
                if month is None:
                    session.flash = T('Report no visible: There are no parameters required to display the report.')
                    redirect(URL('default','index'))

            #LEVEL MORE THAN 3
            if int(request.vars['level'])>3:
                #CHECK IF THE ROLE IS VALID
                roll = VALIDATE_ROLE(request.vars['roll'],'academic_log')
                if roll is None:
                    session.flash = T('Report no visible: There are no parameters required to display the report.')
                    redirect(URL('default','index'))

            #LEVEL MORE THAN 4
            if int(request.vars['level'])>4:
                #CHECK IF THE USER IS VALID
                userP = VALIDATE_USER(period,None,roll,request.vars['userP'],'academic_log')
                if userP is None:
                    session.flash = T('Report no visible: There are no parameters required to display the report.')
                    redi*rect(URL('default','index'))
    except:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))

    #CHECK IF THERE IS A PERSONALIZED QUERY
    personal_query = ''
    if request.vars['querySearch'] is not None and str(request.vars['querySearch']) != "":
        #PERSONALIZED QUERY SURE WORK
        try:
            personal_query = str(request.vars['querySearch'])
            countI = db.smart_query(db.academic_log,personal_query).count()
        except:
            personal_query = ''

    #****************************************************************************************************************
    #****************************************************************************************************************
    #*****************************************************REPORT*****************************************************
    from datetime import datetime
    #TITLE
    infoLevel = []
    infoeLevelTemp=[]
    infoeLevelTemp.append('Universidad de San Carlos de Guatemala')
    infoLevel.append(infoeLevelTemp)
    infoeLevelTemp=[]
    infoeLevelTemp.append('Facultad de Ingeniería')
    infoLevel.append(infoeLevelTemp)
    infoeLevelTemp=[]
    infoeLevelTemp.append('Escuela de Ciencias y Sistemas')
    infoLevel.append(infoeLevelTemp)
    #TYPE OF REPORT
    infoeLevelTemp=[]
    infoeLevelTemp.append(T('Type'))
    infoeLevelTemp.append(T('Management Students'))
    infoLevel.append(infoeLevelTemp)
    #DESCRIPTION OF REPORT
    infoeLevelTemp=[]
    infoeLevelTemp.append(T('Description'))
    infoeLevelTemp.append(T('Report of operations management students'))
    infoLevel.append(infoeLevelTemp)
    #LEVELS OF REPORT
    #ALL SEMESTERS
    if request.vars['level'] is None or str(request.vars['level'])=="1":
        #MIDDLE LINE OF REPORT
        infoeLevelTemp=[]
        infoLevel.append(infoeLevelTemp)
        #LABLE DETAIL OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Detail'))
        infoLevel.append(infoeLevelTemp)
        #LABELS OF DATA OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Period'))
        infoeLevelTemp.append(T('Total inserted'))
        infoeLevelTemp.append(T('Total modified'))
        infoeLevelTemp.append(T('Total out'))
        infoLevel.append(infoeLevelTemp)
        for period in db(db.period_year).select(orderby=~db.period_year.id):
            infoeLevelTemp = []
            #NAME OF PERIOD
            infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
            #INSERT
            if personal_query == '':
                search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "insert"'
            else:
                search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "insert" and '+personal_query
            countI = db.smart_query(db.academic_log,search).count()
            infoeLevelTemp.append(countI)
            #UPDATE
            if personal_query == '':
                search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "update"'
            else:
                search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "update" and '+personal_query
            countI = db.smart_query(db.academic_log,search).count()
            infoeLevelTemp.append(countI)
            #DELETE
            if personal_query == '':
                search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "delete"'
            else:
                search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "delete" and '+personal_query
            countI = db.smart_query(db.academic_log,search).count()
            infoeLevelTemp.append(countI)
            #INSERT PERIOD
            infoLevel.append(infoeLevelTemp)
    #PER MONTH
    elif str(request.vars['level'])=="2":
        #PERIOD OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Period'))
        infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
        infoLevel.append(infoeLevelTemp)
        #MIDDLE LINE OF REPORT
        infoeLevelTemp=[]
        infoLevel.append(infoeLevelTemp)
        #LABLE DETAIL OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Detail'))
        infoLevel.append(infoeLevelTemp)
        #LABELS OF DATA OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Month'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
            infoeLevelTemp.append(T('Total inserted'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
            infoeLevelTemp.append(T('Total modified'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
            infoeLevelTemp.append(T('Total out'))
        infoLevel.append(infoeLevelTemp)

        for month in GET_MONTH_PERIOD(period):
            start = datetime.strptime(str(period.yearp) + '-' + str(month[0]) +'-01', "%Y-%m-%d")
            if month[2]==1:
                end = datetime.strptime(str(period.yearp+1) + '-' + str(month[2]) +'-01', "%Y-%m-%d")
            else:
                end = datetime.strptime(str(period.yearp) + '-' + str(month[2]) +'-01', "%Y-%m-%d")
            infoeLevelTemp = []
            #NAME OF MONTH
            infoeLevelTemp.append(month[1]+' '+str(period.yearp))
            #INSERT
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                if personal_query == '':
                    search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "insert" and academic_log.date_log >="'+str(start)+'" and academic_log.date_log<"'+str(end)+'"'
                else:
                    search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "insert" and academic_log.date_log >="'+str(start)+'" and academic_log.date_log<"'+str(end)+'" and '+personal_query
                countI = db.smart_query(db.academic_log,search).count()
                infoeLevelTemp.append(countI)
            #UPDATE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "update" and academic_log.date_log>="'+str(start)+'" and academic_log.date_log<"'+str(end)+'"'
                else:
                    search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "update" and academic_log.date_log>="'+str(start)+'" and academic_log.date_log<"'+str(end)+'" and '+personal_query
                countI = db.smart_query(db.academic_log,search).count()
                infoeLevelTemp.append(countI)
            #DELETE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "delete" and academic_log.date_log>="'+str(start)+'" and academic_log.date_log<"'+str(end)+'"'
                else:
                    search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "delete" and academic_log.date_log>="'+str(start)+'" and academic_log.date_log<"'+str(end)+'" and '+personal_query
                countI = db.smart_query(db.academic_log,search).count()
                infoeLevelTemp.append(countI)
            #INSERT MONTH
            infoLevel.append(infoeLevelTemp)
    #PER ROL
    elif str(request.vars['level'])=="3":
        #ROLES
        roles = GET_ROLES('academic_log')
        #PERIOD OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Period'))
        infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
        infoLevel.append(infoeLevelTemp)
        #MONTH OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Month'))
        infoeLevelTemp.append(str(month[0]))
        infoLevel.append(infoeLevelTemp)
        #MIDDLE LINE OF REPORT
        infoeLevelTemp=[]
        infoLevel.append(infoeLevelTemp)
        #LABLE DETAIL OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Detail'))
        infoLevel.append(infoeLevelTemp)
        #LABELS OF DATA OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Role'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
            infoeLevelTemp.append(T('Total inserted'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
            infoeLevelTemp.append(T('Total modified'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
            infoeLevelTemp.append(T('Total out'))
        infoLevel.append(infoeLevelTemp)

        for rollT in roles:
            roll=db(db.auth_group.role==rollT).select().first()
            if roll is None:
                roll=db(db.academic_log.roll==rollT).select().first()
                roll=roll.roll
            else:
                roll=roll.role
            infoeLevelTemp = []
            #NAME OF ROLE
            infoeLevelTemp.append(T('Rol '+roll))
            #INSERT
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                if personal_query == '':
                    search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "insert" and academic_log.date_log >="'+str(month[1])+'" and academic_log.date_log<"'+str(month[2])+'" and academic_log.roll contains "'+str(roll)+'"'
                else:
                    search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "insert" and academic_log.date_log >="'+str(month[1])+'" and academic_log.date_log<"'+str(month[2])+'" and academic_log.roll contains "'+str(roll)+'" and '+personal_query
                countI = db.smart_query(db.academic_log,search).count()
                infoeLevelTemp.append(countI)
            #UPDATE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "update" and academic_log.date_log >="'+str(month[1])+'" and academic_log.date_log<"'+str(month[2])+'" and academic_log.roll contains "'+str(roll)+'"'
                else:
                    search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "update" and academic_log.date_log >="'+str(month[1])+'" and academic_log.date_log<"'+str(month[2])+'" and academic_log.roll contains "'+str(roll)+'" and '+personal_query
                countI = db.smart_query(db.academic_log,search).count()
                infoeLevelTemp.append(countI)
            #DELETE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "delete" and academic_log.date_log >="'+str(month[1])+'" and academic_log.date_log<"'+str(month[2])+'" and academic_log.roll contains "'+str(roll)+'"'
                else:
                    search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "delete" and academic_log.date_log >="'+str(month[1])+'" and academic_log.date_log<"'+str(month[2])+'" and academic_log.roll contains "'+str(roll)+'" and '+personal_query
                countI = db.smart_query(db.academic_log,search).count()
                infoeLevelTemp.append(countI)
            #INSERT PROJECT
            infoLevel.append(infoeLevelTemp)
    #PER USER
    elif str(request.vars['level'])=="4":
        #VERIFY THAT CAN SHOW THE LEVEL OF THE REPORT
        usersProject = GET_USERS(period,None,roll,'academic_log')
        #PERIOD OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Period'))
        infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
        infoLevel.append(infoeLevelTemp)
        #MONTH OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Month'))
        infoeLevelTemp.append(str(month[0]))
        infoLevel.append(infoeLevelTemp)
        #ROL OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Role'))
        infoeLevelTemp.append(T('Rol '+roll))
        infoLevel.append(infoeLevelTemp)
        #MIDDLE LINE OF REPORT
        infoeLevelTemp=[]
        infoLevel.append(infoeLevelTemp)
        #LABLE DETAIL OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Detail'))
        infoLevel.append(infoeLevelTemp)
        #LABELS OF DATA OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('User'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
            infoeLevelTemp.append(T('Total inserted'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
            infoeLevelTemp.append(T('Total modified'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
            infoeLevelTemp.append(T('Total out'))
        infoLevel.append(infoeLevelTemp)

        for userPT in usersProject:
            userP=db(db.auth_user.username==userPT).select().first()
            if userP is None:
                userP=db(db.academic_log.user_name==userPT).select().first()
                userP=userP.user_name
            else:
                userP=userP.username
            infoeLevelTemp = []
            #NAME OF USER
            infoeLevelTemp.append(userP)
            #INSERT
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                if personal_query == '':
                    search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "insert" and academic_log.date_log >="'+str(month[1])+'" and academic_log.date_log<"'+str(month[2])+'" and academic_log.roll contains "'+str(roll)+'" and academic_log.user_name ="'+str(userP)+'"'
                else:
                    search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "insert" and academic_log.date_log >="'+str(month[1])+'" and academic_log.date_log<"'+str(month[2])+'" and academic_log.roll contains "'+str(roll)+'" and academic_log.user_name ="'+str(userP)+'" and '+personal_query
                countI = db.smart_query(db.academic_log,search).count()
                infoeLevelTemp.append(countI)
            #UPDATE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "update" and academic_log.date_log >="'+str(month[1])+'" and academic_log.date_log<"'+str(month[2])+'" and academic_log.roll contains "'+str(roll)+'" and academic_log.user_name ="'+str(userP)+'"'
                else:
                    search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "update" and academic_log.date_log >="'+str(month[1])+'" and academic_log.date_log<"'+str(month[2])+'" and academic_log.roll contains "'+str(roll)+'" and academic_log.user_name ="'+str(userP)+'" and '+personal_query
                countI = db.smart_query(db.academic_log,search).count()
                infoeLevelTemp.append(countI)
            #DELETE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "delete" and academic_log.date_log >="'+str(month[1])+'" and academic_log.date_log<"'+str(month[2])+'" and academic_log.roll contains "'+str(roll)+'" and academic_log.user_name ="'+str(userP)+'"'
                else:
                    search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "delete" and academic_log.date_log >="'+str(month[1])+'" and academic_log.date_log<"'+str(month[2])+'" and academic_log.roll contains "'+str(roll)+'" and academic_log.user_name ="'+str(userP)+'" and '+personal_query
                countI = db.smart_query(db.academic_log,search).count()
                infoeLevelTemp.append(countI)
            #INSERT PROJECT
            infoLevel.append(infoeLevelTemp)
    #DATA
    elif str(request.vars['level'])=="5":
        if str(request.vars['type_L'])=="all":
            if personal_query == '':
                search='academic_log.id_period = "'+str(period.id)+'" and academic_log.date_log >="'+str(month[1])+'" and academic_log.date_log<"'+str(month[2])+'" and academic_log.roll contains "'+str(roll)+'" and academic_log.user_name ="'+str(userP)+'"'
            else:
                search='academic_log.id_period = "'+str(period.id)+'" and academic_log.date_log >="'+str(month[1])+'" and academic_log.date_log<"'+str(month[2])+'" and academic_log.roll contains "'+str(roll)+'" and academic_log.user_name ="'+str(userP)+'" and '+personal_query
        elif str(request.vars['type_L'])=="i":
            if personal_query == '':
                search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "insert" and academic_log.date_log >="'+str(month[1])+'" and academic_log.date_log<"'+str(month[2])+'" and academic_log.roll contains "'+str(roll)+'" and academic_log.user_name ="'+str(userP)+'"'
            else:
                search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "insert" and academic_log.date_log >="'+str(month[1])+'" and academic_log.date_log<"'+str(month[2])+'" and academic_log.roll contains "'+str(roll)+'" and academic_log.user_name ="'+str(userP)+'" and '+personal_query
        elif str(request.vars['type_L'])=="u":
            if personal_query == '':
                search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "update" and academic_log.date_log >="'+str(month[1])+'" and academic_log.date_log<"'+str(month[2])+'" and academic_log.roll contains "'+str(roll)+'" and academic_log.user_name ="'+str(userP)+'"'
            else:
                search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "update" and academic_log.date_log >="'+str(month[1])+'" and academic_log.date_log<"'+str(month[2])+'" and academic_log.roll contains "'+str(roll)+'" and academic_log.user_name ="'+str(userP)+'" and '+personal_query
        elif str(request.vars['type_L'])=="d":
            if personal_query == '':
                search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "delete" and academic_log.date_log >="'+str(month[1])+'" and academic_log.date_log<"'+str(month[2])+'" and academic_log.roll contains "'+str(roll)+'" and academic_log.user_name ="'+str(userP)+'"'
            else:
                search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "delete" and academic_log.date_log >="'+str(month[1])+'" and academic_log.date_log<"'+str(month[2])+'" and academic_log.roll contains "'+str(roll)+'" and academic_log.user_name ="'+str(userP)+'" and '+personal_query
        #PERIOD
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Period'))
        infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
        infoLevel.append(infoeLevelTemp)
        #MONTH
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Month'))
        infoeLevelTemp.append(str(month[0]))
        infoLevel.append(infoeLevelTemp)
        #ROL
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Role'))
        infoeLevelTemp.append(T('Rol '+roll))
        infoLevel.append(infoeLevelTemp)
        #USER
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('User'))
        infoeLevelTemp.append(str(userP))
        infoLevel.append(infoeLevelTemp)
        #MIDDLE LINE
        infoeLevelTemp=[]
        infoeLevelTemp.append('')
        infoLevel.append(infoeLevelTemp)
        #DETAIL
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Detail'))
        infoLevel.append(infoeLevelTemp)
        #TITLE OF TABLE
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Operacion'))
        infoeLevelTemp.append(T('Carnet anterior'))
        infoeLevelTemp.append(T('Carnet actual'))
        infoeLevelTemp.append(T('Correo anterior'))
        infoeLevelTemp.append(T('Correo actual'))
        infoeLevelTemp.append(T('Descripcion'))
        infoeLevelTemp.append(T('Fecha'))
        infoLevel.append(infoeLevelTemp)
        for operation in db.smart_query(db.academic_log,search).select():
            infoeLevelTemp=[]
            infoeLevelTemp.append(operation.operation_log)
            infoeLevelTemp.append(operation.before_carnet)
            infoeLevelTemp.append(operation.after_carnet)
            infoeLevelTemp.append(operation.before_email)
            infoeLevelTemp.append(operation.after_email)
            infoeLevelTemp.append(operation.description)
            infoeLevelTemp.append(operation.date_log)
            infoLevel.append(infoeLevelTemp)
    #*****************************************************REPORT*****************************************************
    #****************************************************************************************************************
    #****************************************************************************************************************
    return dict(filename='ReporteGestionEstudiantes', csvdata=infoLevel)


@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def student_management():
    #****************************************************************************************************************
    #****************************************************************************************************************
    #***************************************CHECK IF THERE IS A PERSONALIZED QUERY***********************************
    personal_query = ''
    makeRedirect = False
    if request.vars['querySearch'] is not None and str(request.vars['querySearch']) != "":
        #PERSONALIZED QUERY SURE WORK
        try:
            personal_query = str(request.vars['querySearch'])
            countI = db.smart_query(db.academic_log,personal_query).count()
            if request.vars['searchT'] is not None and str(request.vars['searchT']) == 'T':
                makeRedirect = True
        except:
            response.flash = T('The query is not valid. The report is displayed without applying any query.')
            personal_query = ''
    if makeRedirect == True:
        redirect(URL('management_reports', 'student_management', vars=dict(level = 5, period = request.vars['period'], month = str(request.vars['month']), roll = str(request.vars['roll']), userP = str(request.vars['userP']), type_L=request.vars['type_L'], type_U=request.vars['type_U'], querySearch=request.vars['querySearch'])))
    

    #****************************************************************************************************************
    #****************************************************************************************************************
    #******************************************VERIFY THAT ACCURATE PARAMETERS***************************************
    try:
        #CHECK THAT THE LEVEL OF REPORT IS VALID
        if request.vars['level'] is not None and (int(request.vars['level'])<1 or int(request.vars['level'])>5):
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #VERIFY THAT THE PARAMETERS OF EACH LEVEL BE VALID
        if request.vars['level'] is not None:
            #LEVEL MORE THAN 1
            if int(request.vars['level'])>1:
                #CHECK IF THE TYPE OF REPORT IS VALID
                if request.vars['type_L'] is None or (str(request.vars['type_L'])!="all" and str(request.vars['type_L'])!="i" and str(request.vars['type_L'])!="u" and str(request.vars['type_L'])!="d"):
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))

                period = VALIDATE_PERIOD(request.vars['period'])
                if period is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))
            #LEVEL MORE THAN 2
            if int(request.vars['level'])>2:
                #CHECK IF THE TYPE OF REPORT IS VALID
                if request.vars['type_U'] is None or (str(request.vars['type_U'])!="all" and str(request.vars['type_U'])!="i" and str(request.vars['type_U'])!="u" and str(request.vars['type_U'])!="d"):
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))

                #CHECK IF THE MONTH IS VALID
                month = VALIDATE_MONTH(request.vars['month'],period)
                if month is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))
            #LEVEL MORE THAN 3
            if int(request.vars['level'])>3:
                #CHECK IF THE ROLE IS VALID
                roll = VALIDATE_ROLE(request.vars['roll'],'academic_log')
                if roll is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))

            #LEVEL MORE THAN 4
            if int(request.vars['level'])>4:
                #CHECK IF THE USER IS VALID
                userP = VALIDATE_USER(period,None,roll,request.vars['userP'],'academic_log')
                if userP is None:
                    session.flash = T('Not valid Action.')
                    redi*rect(URL('default','index'))
    except:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))


    #****************************************************************************************************************
    #****************************************************************************************************************
    #**************************************************SEARCH REPORT*************************************************
    def filtered_by(flag):
        fsearch_Option=[]
        fsearch_Option.append('=')
        fsearch_Option.append('!=')
        fsearch_Option.append('<')
        fsearch_Option.append('>')
        fsearch_Option.append('<=')
        fsearch_Option.append('>=')
        if flag==True:
            fsearch_Option.append('starts with')
            fsearch_Option.append('contains')
            fsearch_Option.append('in')
            fsearch_Option.append('not in')
        return fsearch_Option


    fsearch = []
    #******************************COMBOS INFORMATION******************************
    #ROLES
    if request.vars['level'] is None or int(request.vars['level'])<=3:
        roles = GET_ROLES('academic_log')
        if len(roles) != 0:
            fsearch.append(['roll',T('Rol'),False,[4,sorted(roles)]])
    #PERIODS
    if request.vars['level']=='1' or request.vars['level'] is None:
        groupPeriods = db(db.period_year).select(orderby=~db.period_year.id)
        if len(groupPeriods) != 0:
            fsearch.append(['id_period','Periodo',False,[2,groupPeriods]])
    #DESCRIPTION
    groupDescription = GET_DESCRIPTIONS('academic_log')
    if len(groupDescription) != 0:
        fsearch.append(['description','Descripción',False,[3,sorted(groupDescription)]])
    #DATE
    groupDates = GET_DATES('academic_log')
    if len(groupDates) != 0:
        fsearch.append(['date_log','Fecha',False,[3,sorted(groupDates)]])
    #OPERATION LOG
    fsearch.append(['operation_log',T('Operacion'),False,[3,['insert','update','delete']]])
    #******************************ENTERING USER******************************
    if request.vars['level'] is None or int(request.vars['level'])<=4:
        #ID OF PERSON WHO REGISTER THE GRADE
        fsearch.append(['user_name',T('Usuario'),True,[1]])
    #BEFORE CARNET
    fsearch.append(['before_carnet','Carnet anterior',True,[1]])
    #AFTER CARNET
    fsearch.append(['after_carnet','Carnet actual',True,[1]])
    #BEFORE EMAIL
    fsearch.append(['before_email','Correo anterior',True,[1]])
    #AFTER EMAIL
    fsearch.append(['after_email','Correo actual',True,[1]])


    #****************************************************************************************************************
    #****************************************************************************************************************
    #*****************************************************REPORT*****************************************************
    #LEVELS OF REPORT
    from datetime import datetime
    infoLevel = []
    top5=[]
    grid=None
    #ALL SEMESTERS
    if request.vars['level']=='1' or request.vars['level'] is None:
        if len(groupPeriods) == 0:
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('default','index'))
            

        for period in groupPeriods:
            infoeLevelTemp = []
            #ID OF PERIOD
            infoeLevelTemp.append(period.id)
            #NAME OF PERIOD
            infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
            #INSERT
            if personal_query == '':
                search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "insert"'
            else:
                search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "insert" and '+personal_query
            countI = db.smart_query(db.academic_log,search).count()
            infoeLevelTemp.append(countI)
            #UPDATE
            if personal_query == '':
                search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "update"'
            else:
                search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "update" and '+personal_query
            countI = db.smart_query(db.academic_log,search).count()
            infoeLevelTemp.append(countI)
            #DELETE
            if personal_query == '':
                search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "delete"'
            else:
                search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "delete" and '+personal_query
            countI = db.smart_query(db.academic_log,search).count()
            infoeLevelTemp.append(countI)
            #INSERT PERIOD
            infoLevel.append(infoeLevelTemp)

        #TOP 5 OF PERIOD
        if personal_query == '':
            search='academic_log.id != "-1"'
        else:
            search=personal_query
        top5 = db.smart_query(db.academic_log,search).select(db.academic_log.id_period, db.academic_log.id.count(), orderby=~db.academic_log.id.count(), limitby=(0, 5), groupby=db.academic_log.id_period)
        top5T=[]
        for top in top5:
            periodTop = db(db.period_year.id==top['academic_log.id_period']).select().first()
            top5T.append([T(periodTop.period.name)+' '+str(periodTop.yearp),top['COUNT(academic_log.id)']])
        top5=top5T
    #PER MONTH
    elif str(request.vars['level'])=="2":
        for month in GET_MONTH_PERIOD(period):
            start = datetime.strptime(str(period.yearp) + '-' + str(month[0]) +'-01', "%Y-%m-%d")
            if month[2]==1:
                end = datetime.strptime(str(period.yearp+1) + '-' + str(month[2]) +'-01', "%Y-%m-%d")
            else:
                end = datetime.strptime(str(period.yearp) + '-' + str(month[2]) +'-01', "%Y-%m-%d")
            infoeLevelTemp = []
            #NAME OF PERIOD
            infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
            #ID OF MONTH
            infoeLevelTemp.append(month[0])
            #NAME OF MONTH
            infoeLevelTemp.append(month[1]+' '+str(period.yearp))
            #INSERT
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                if personal_query == '':
                    search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "insert" and academic_log.date_log >="'+str(start)+'" and academic_log.date_log<"'+str(end)+'"'
                else:
                    search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "insert" and academic_log.date_log >="'+str(start)+'" and academic_log.date_log<"'+str(end)+'" and '+personal_query
                countI = db.smart_query(db.academic_log,search).count()
                infoeLevelTemp.append(countI)
            #UPDATE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "update" and academic_log.date_log>="'+str(start)+'" and academic_log.date_log<"'+str(end)+'"'
                else:
                    search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "update" and academic_log.date_log>="'+str(start)+'" and academic_log.date_log<"'+str(end)+'" and '+personal_query
                countI = db.smart_query(db.academic_log,search).count()
                infoeLevelTemp.append(countI)
            #DELETE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "delete" and academic_log.date_log>="'+str(start)+'" and academic_log.date_log<"'+str(end)+'"'
                else:
                    search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "delete" and academic_log.date_log>="'+str(start)+'" and academic_log.date_log<"'+str(end)+'" and '+personal_query
                countI = db.smart_query(db.academic_log,search).count()
                infoeLevelTemp.append(countI)
            #INSERT MONTH
            infoLevel.append(infoeLevelTemp)
    #PER ROL
    elif str(request.vars['level'])=="3":
        if len(roles) == 0:
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('management_reports', 'student_management',vars=dict(level='2', period = str(request.vars['period']), month = str(request.vars['month']), type_L = str(request.vars['type_U']), type_U = str(request.vars['type_U']), querySearch=personal_query)))

        for rollT in roles:
            roll=db(db.auth_group.role==rollT).select().first()
            if roll is None:
                roll=db(db.academic_log.roll.like('%'+rollT+'%')).select().first()
                roll=roll.roll
            else:
                roll=roll.role
            infoeLevelTemp = []
            #NAME OF PERIOD
            infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
            #NAME OF MONTH
            infoeLevelTemp.append(month[0])
            #ID OF ROLE
            infoeLevelTemp.append(roll)
            #NAME OF ROLE
            infoeLevelTemp.append(T('Rol '+roll))
            #INSERT
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                if personal_query == '':
                    search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "insert" and academic_log.date_log >="'+str(month[1])+'" and academic_log.date_log<"'+str(month[2])+'" and academic_log.roll contains "'+str(roll)+'"'
                else:
                    search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "insert" and academic_log.date_log >="'+str(month[1])+'" and academic_log.date_log<"'+str(month[2])+'" and academic_log.roll contains "'+str(roll)+'" and '+personal_query
                countI = db.smart_query(db.academic_log,search).count()
                infoeLevelTemp.append(countI)
            #UPDATE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "update" and academic_log.date_log >="'+str(month[1])+'" and academic_log.date_log<"'+str(month[2])+'" and academic_log.roll contains "'+str(roll)+'"'
                else:
                    search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "update" and academic_log.date_log >="'+str(month[1])+'" and academic_log.date_log<"'+str(month[2])+'" and academic_log.roll contains "'+str(roll)+'" and '+personal_query
                countI = db.smart_query(db.academic_log,search).count()
                infoeLevelTemp.append(countI)
            #DELETE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "delete" and academic_log.date_log >="'+str(month[1])+'" and academic_log.date_log<"'+str(month[2])+'" and academic_log.roll contains "'+str(roll)+'"'
                else:
                    search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "delete" and academic_log.date_log >="'+str(month[1])+'" and academic_log.date_log<"'+str(month[2])+'" and academic_log.roll contains "'+str(roll)+'" and '+personal_query
                countI = db.smart_query(db.academic_log,search).count()
                infoeLevelTemp.append(countI)
            #INSERT PROJECT
            infoLevel.append(infoeLevelTemp)
    #PER USER
    elif str(request.vars['level'])=="4":
        #VERIFY THAT CAN SHOW THE LEVEL OF THE REPORT
        usersProject = GET_USERS(period,None,roll,'academic_log')
        if len(usersProject) == 0:
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('management_reports', 'student_management',vars=dict(level='3', period = str(request.vars['period']), month = str(request.vars['month']), type_L = str(request.vars['type_U']), type_U = str(request.vars['type_U']), querySearch=personal_query)))

        for userPT in usersProject:
            userP=db(db.auth_user.username==userPT).select().first()
            if userP is None:
                userP=db(db.academic_log.user_name==userPT).select().first()
                userP=userP.user_name
            else:
                userP=userP.username
            infoeLevelTemp = []
            #NAME OF PERIOD
            infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
            #NAME OF MONTH
            infoeLevelTemp.append(month[0])
            #NAME OF ROLE
            infoeLevelTemp.append(T('Rol '+roll))
            #ID OF USER
            infoeLevelTemp.append(userP)
            #NAME OF USER
            infoeLevelTemp.append(userP)
            #INSERT
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                if personal_query == '':
                    search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "insert" and academic_log.date_log >="'+str(month[1])+'" and academic_log.date_log<"'+str(month[2])+'" and academic_log.roll contains "'+str(roll)+'" and academic_log.user_name ="'+str(userP)+'"'
                else:
                    search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "insert" and academic_log.date_log >="'+str(month[1])+'" and academic_log.date_log<"'+str(month[2])+'" and academic_log.roll contains "'+str(roll)+'" and academic_log.user_name ="'+str(userP)+'" and '+personal_query
                countI = db.smart_query(db.academic_log,search).count()
                infoeLevelTemp.append(countI)
            #UPDATE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "update" and academic_log.date_log >="'+str(month[1])+'" and academic_log.date_log<"'+str(month[2])+'" and academic_log.roll contains "'+str(roll)+'" and academic_log.user_name ="'+str(userP)+'"'
                else:
                    search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "update" and academic_log.date_log >="'+str(month[1])+'" and academic_log.date_log<"'+str(month[2])+'" and academic_log.roll contains "'+str(roll)+'" and academic_log.user_name ="'+str(userP)+'" and '+personal_query
                countI = db.smart_query(db.academic_log,search).count()
                infoeLevelTemp.append(countI)
            #DELETE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "delete" and academic_log.date_log >="'+str(month[1])+'" and academic_log.date_log<"'+str(month[2])+'" and academic_log.roll contains "'+str(roll)+'" and academic_log.user_name ="'+str(userP)+'"'
                else:
                    search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "delete" and academic_log.date_log >="'+str(month[1])+'" and academic_log.date_log<"'+str(month[2])+'" and academic_log.roll contains "'+str(roll)+'" and academic_log.user_name ="'+str(userP)+'" and '+personal_query
                countI = db.smart_query(db.academic_log,search).count()
                infoeLevelTemp.append(countI)
            #INSERT PROJECT
            infoLevel.append(infoeLevelTemp)

        #TOP 5 OF USERS
        if personal_query == '':
            search='academic_log.id_period = "'+str(period.id)+'" and academic_log.date_log >="'+str(month[1])+'" and academic_log.date_log<"'+str(month[2])+'" and academic_log.roll contains "'+str(roll)+'"'
        else:
            search='academic_log.id_period = "'+str(period.id)+'" and academic_log.date_log >="'+str(month[1])+'" and academic_log.date_log<"'+str(month[2])+'" and academic_log.roll contains "'+str(roll)+'" and '+personal_query
        top5 = db.smart_query(db.academic_log,search).select(db.academic_log.user_name, db.academic_log.id.count(), orderby=~db.academic_log.id.count(), limitby=(0, 5), groupby=db.academic_log.user_name)
    #DATA
    elif str(request.vars['level'])=="5":
        if str(request.vars['type_L'])=="all":
            if personal_query == '':
                search='academic_log.id_period = "'+str(period.id)+'" and academic_log.date_log >="'+str(month[1])+'" and academic_log.date_log<"'+str(month[2])+'" and academic_log.roll LIKE "%'+str(roll)+'%" and academic_log.user_name ="'+str(userP)+'"'
            else:
                search='academic_log.id_period = "'+str(period.id)+'" and academic_log.date_log >="'+str(month[1])+'" and academic_log.date_log<"'+str(month[2])+'" and academic_log.roll LIKE "%'+str(roll)+'%" and academic_log.user_name ="'+str(userP)+'" and '+personal_query
        elif str(request.vars['type_L'])=="i":
            if personal_query == '':
                search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "insert" and academic_log.date_log >="'+str(month[1])+'" and academic_log.date_log<"'+str(month[2])+'" and academic_log.roll LIKE "%'+str(roll)+'%" and academic_log.user_name ="'+str(userP)+'"'
            else:
                search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "insert" and academic_log.date_log >="'+str(month[1])+'" and academic_log.date_log<"'+str(month[2])+'" and academic_log.roll LIKE "%'+str(roll)+'%" and academic_log.user_name ="'+str(userP)+'" and '+personal_query
        elif str(request.vars['type_L'])=="u":
            if personal_query == '':
                search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "update" and academic_log.date_log >="'+str(month[1])+'" and academic_log.date_log<"'+str(month[2])+'" and academic_log.roll LIKE "%'+str(roll)+'%" and academic_log.user_name ="'+str(userP)+'"'
            else:
                search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "update" and academic_log.date_log >="'+str(month[1])+'" and academic_log.date_log<"'+str(month[2])+'" and academic_log.roll LIKE "%'+str(roll)+'%" and academic_log.user_name ="'+str(userP)+'" and '+personal_query
        elif str(request.vars['type_L'])=="d":
            if personal_query == '':
                search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "delete" and academic_log.date_log >="'+str(month[1])+'" and academic_log.date_log<"'+str(month[2])+'" and academic_log.roll LIKE "%'+str(roll)+'%" and academic_log.user_name ="'+str(userP)+'"'
            else:
                search='academic_log.id_period = "'+str(period.id)+'" and academic_log.operation_log = "delete" and academic_log.date_log >="'+str(month[1])+'" and academic_log.date_log<"'+str(month[2])+'" and academic_log.roll LIKE "%'+str(roll)+'%" and academic_log.user_name ="'+str(userP)+'" and '+personal_query
        grid = []
        for data in db.smart_query(db.academic_log,search).select():
            grid.append(data.id)
        #REPORT
        if len(grid) == 0:
            grid.append(-1)
        infoeLevelTemp=[]
        infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
        infoeLevelTemp.append(str(month[0]))
        infoeLevelTemp.append(T('Rol '+roll))
        infoeLevelTemp.append(str(userP))
        infoLevel.append(infoeLevelTemp)
        #GRID
        db.academic_log.id.readable = False
        db.academic_log.id.writable = False
        db.academic_log.user_name.readable = False
        db.academic_log.user_name.writable = False
        db.academic_log.roll.readable = False
        db.academic_log.roll.writable = False
        db.academic_log.id_academic.readable = False
        db.academic_log.id_academic.writable = False
        db.academic_log.id_period.readable = False
        db.academic_log.id_period.writable = False
        grid = SQLFORM.grid(db.academic_log.id.belongs(grid), csv=False, create=False, editable=False, deletable=False, paginate=9, searchable=False)
    return dict(fsearch=fsearch, filtered_by=filtered_by, personal_query=personal_query, infoLevel=infoLevel, top5=top5, grid=grid) 


#*************************************************************************************************************************************
#*************************************************************************************************************************************
#*****************************************************MANAGEMENT REPORT STUDENTS ASSIGNMENT*******************************************
@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def student_assignment_management_export():
    #VERIFI THAT ACCURATE PARAMETERS
    try:
        #CHECK IF THE TYPE OF EXPORT IS VALID
        if request.vars['list_type'] is None or str(request.vars['list_type'])!="csv":
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #CHECK THAT THE LEVEL OF REPORT IS VALID
        if request.vars['level'] is not None and (int(request.vars['level'])<1 or int(request.vars['level'])>6):
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('default','index'))

        #VERIFY THAT THE PARAMETERS OF EACH LEVEL BE VALID
        if request.vars['level'] is not None:
            #LEVEL MORE THAN 1
            if int(request.vars['level'])>1:
                #CHECK IF THE TYPE OF REPORT IS VALID
                if request.vars['type_L'] is None or (str(request.vars['type_L'])!="all" and str(request.vars['type_L'])!="i" and str(request.vars['type_L'])!="u" and str(request.vars['type_L'])!="d"):
                    session.flash = T('Report no visible: There are no parameters required to display the report.')
                    redirect(URL('default','index'))

                period = VALIDATE_PERIOD(request.vars['period'])
                if period is None:
                    session.flash = T('Report no visible: There are no parameters required to display the report.')
                    redirect(URL('default','index'))
            
            #LEVEL MORE THAN 2
            if int(request.vars['level'])>2:
                #CHECK IF THE TYPE OF REPORT IS VALID
                if request.vars['type_U'] is None or (str(request.vars['type_U'])!="all" and str(request.vars['type_U'])!="i" and str(request.vars['type_U'])!="u" and str(request.vars['type_U'])!="d"):
                    session.flash = T('Report no visible: There are no parameters required to display the report.')
                    redirect(URL('default','index'))

                #CHECK IF THE MONTH IS VALID
                month = VALIDATE_MONTH(request.vars['month'],period)
                if month is None:
                    session.flash = T('Report no visible: There are no parameters required to display the report.')
                    redirect(URL('default','index'))
            
            #LEVEL MORE THAN 3
            if int(request.vars['level'])>3:
                #CHECK IF THE PROJECT IS VALID
                project = VALIDATE_PROJECT(request.vars['project'],'academic_course_assignation_log')
                if project is None:
                    session.flash = T('Report no visible: There are no parameters required to display the report.')
                    redirect(URL('default','index'))
            #LEVEL MORE THAN 4
            if int(request.vars['level'])>4:
                #CHECK IF THE ROLE IS VALID
                roll = VALIDATE_ROLE(request.vars['roll'],'academic_course_assignation_log')
                if roll is None:
                    session.flash = T('Report no visible: There are no parameters required to display the report.')
                    redirect(URL('default','index'))

            #LEVEL MORE THAN 5
            if int(request.vars['level'])>5:
                #CHECK IF THE USER IS VALID
                userP = VALIDATE_USER(period,project,roll,request.vars['userP'],'academic_course_assignation_log')
                if userP is None:
                    session.flash = T('Report no visible: There are no parameters required to display the report.')
                    redi*rect(URL('default','index'))
    except:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))

    #CHECK IF THERE IS A PERSONALIZED QUERY
    personal_query = ''
    if request.vars['querySearch'] is not None and str(request.vars['querySearch']) != "":
        #PERSONALIZED QUERY SURE WORK
        try:
            personal_query = str(request.vars['querySearch'])
            countI = db.smart_query(db.academic_course_assignation_log,personal_query).count()
        except:
            personal_query = ''

    #****************************************************************************************************************
    #****************************************************************************************************************
    #*****************************************************REPORT*****************************************************
    from datetime import datetime
    #TITLE
    infoLevel = []
    infoeLevelTemp=[]
    infoeLevelTemp.append('Universidad de San Carlos de Guatemala')
    infoLevel.append(infoeLevelTemp)
    infoeLevelTemp=[]
    infoeLevelTemp.append('Facultad de Ingeniería')
    infoLevel.append(infoeLevelTemp)
    infoeLevelTemp=[]
    infoeLevelTemp.append('Escuela de Ciencias y Sistemas')
    infoLevel.append(infoeLevelTemp)
    #TYPE OF REPORT
    infoeLevelTemp=[]
    infoeLevelTemp.append(T('Type'))
    infoeLevelTemp.append(T('Student Assignment Management'))
    infoLevel.append(infoeLevelTemp)
    #DESCRIPTION OF REPORT
    infoeLevelTemp=[]
    infoeLevelTemp.append(T('Description'))
    infoeLevelTemp.append(T('Report of operations management assignment of students'))
    infoLevel.append(infoeLevelTemp)
    #LEVELS OF REPORT
    #ALL SEMESTERS
    if request.vars['level'] is None or str(request.vars['level'])=="1":
        #MIDDLE LINE OF REPORT
        infoeLevelTemp=[]
        infoLevel.append(infoeLevelTemp)
        #LABLE DETAIL OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Detail'))
        infoLevel.append(infoeLevelTemp)
        #LABELS OF DATA OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Period'))
        infoeLevelTemp.append(T('Total inserted'))
        infoeLevelTemp.append(T('Total modified'))
        infoeLevelTemp.append(T('Total out'))
        infoLevel.append(infoeLevelTemp)
        for period in db(db.period_year).select(orderby=~db.period_year.id):
            infoeLevelTemp = []
            #NAME OF PERIOD
            infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
            #INSERT
            if personal_query == '':
                search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "insert"'
            else:
                search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "insert" and '+personal_query
            countI = db.smart_query(db.academic_course_assignation_log,search).count()
            infoeLevelTemp.append(countI)
            #UPDATE
            if personal_query == '':
                search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "update"'
            else:
                search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "update" and '+personal_query
            countI = db.smart_query(db.academic_course_assignation_log,search).count()
            infoeLevelTemp.append(countI)
            #DELETE
            if personal_query == '':
                search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "delete"'
            else:
                search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "delete" and '+personal_query
            countI = db.smart_query(db.academic_course_assignation_log,search).count()
            infoeLevelTemp.append(countI)
            #INSERT PERIOD
            infoLevel.append(infoeLevelTemp)
    #PER MONTH
    elif str(request.vars['level'])=="2":
        #PERIOD OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Period'))
        infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
        infoLevel.append(infoeLevelTemp)
        #MIDDLE LINE OF REPORT
        infoeLevelTemp=[]
        infoLevel.append(infoeLevelTemp)
        #LABLE DETAIL OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Detail'))
        infoLevel.append(infoeLevelTemp)
        #LABELS OF DATA OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Month'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
            infoeLevelTemp.append(T('Total inserted'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
            infoeLevelTemp.append(T('Total modified'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
            infoeLevelTemp.append(T('Total out'))
        infoLevel.append(infoeLevelTemp)

        for month in GET_MONTH_PERIOD(period):
            start = datetime.strptime(str(period.yearp) + '-' + str(month[0]) +'-01', "%Y-%m-%d")
            if month[2]==1:
                end = datetime.strptime(str(period.yearp+1) + '-' + str(month[2]) +'-01', "%Y-%m-%d")
            else:
                end = datetime.strptime(str(period.yearp) + '-' + str(month[2]) +'-01', "%Y-%m-%d")
            infoeLevelTemp = []
            #NAME OF MONTH
            infoeLevelTemp.append(month[1]+' '+str(period.yearp))
            #INSERT
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                if personal_query == '':
                    search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "insert" and academic_course_assignation_log.date_log >="'+str(start)+'" and academic_course_assignation_log.date_log<"'+str(end)+'"'
                else:
                    search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "insert" and academic_course_assignation_log.date_log >="'+str(start)+'" and academic_course_assignation_log.date_log<"'+str(end)+'" and '+personal_query
                countI = db.smart_query(db.academic_course_assignation_log,search).count()
                infoeLevelTemp.append(countI)
            #UPDATE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "update" and academic_course_assignation_log.date_log>="'+str(start)+'" and academic_course_assignation_log.date_log<"'+str(end)+'"'
                else:
                    search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "update" and academic_course_assignation_log.date_log>="'+str(start)+'" and academic_course_assignation_log.date_log<"'+str(end)+'" and '+personal_query
                countI = db.smart_query(db.academic_course_assignation_log,search).count()
                infoeLevelTemp.append(countI)
            #DELETE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "delete" and academic_course_assignation_log.date_log>="'+str(start)+'" and academic_course_assignation_log.date_log<"'+str(end)+'"'
                else:
                    search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "delete" and academic_course_assignation_log.date_log>="'+str(start)+'" and academic_course_assignation_log.date_log<"'+str(end)+'" and '+personal_query
                countI = db.smart_query(db.academic_course_assignation_log,search).count()
                infoeLevelTemp.append(countI)
            #INSERT MONTH
            infoLevel.append(infoeLevelTemp)
    #PER PROJECT
    elif str(request.vars['level'])=="3":
        #PROJECTS
        projects = GET_PROJECTS('academic_course_assignation_log')
        projects=sorted(projects)
        #PERIOD OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Period'))
        infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
        infoLevel.append(infoeLevelTemp)
        #MONTH OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Month'))
        infoeLevelTemp.append(str(month[0]))
        infoLevel.append(infoeLevelTemp)
        #MIDDLE LINE OF REPORT
        infoeLevelTemp=[]
        infoLevel.append(infoeLevelTemp)
        #LABLE DETAIL OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Detail'))
        infoLevel.append(infoeLevelTemp)
        #LABELS OF DATA OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Project'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
            infoeLevelTemp.append(T('Total inserted'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
            infoeLevelTemp.append(T('Total modified'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
            infoeLevelTemp.append(T('Total out'))
        infoLevel.append(infoeLevelTemp)

        for projectT in projects:
            project=db(db.project.name==projectT).select().first()
            if project is None:
                project=db((db.course_activity_log.before_course==projectT)|(db.course_activity_log.after_course==projectT)).select().first()
                if project.before_course is not None:
                    project=project.before_course
                else:
                    project=project.after_course
            else:
                project=project.name
            infoeLevelTemp = []
            #NAME OF PROJECT
            infoeLevelTemp.append(project)
            #INSERT
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                if personal_query == '':
                    search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "insert" and academic_course_assignation_log.date_log >="'+str(month[1])+'" and academic_course_assignation_log.date_log<"'+str(month[2])+'" and academic_course_assignation_log.after_course = "'+str(project)+'"'
                else:
                    search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "insert" and academic_course_assignation_log.date_log >="'+str(month[1])+'" and academic_course_assignation_log.date_log<"'+str(month[2])+'" and academic_course_assignation_log.after_course = "'+str(project)+'" and '+personal_query
                countI = db.smart_query(db.academic_course_assignation_log,search).count()
                infoeLevelTemp.append(countI)
            #UPDATE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "update" and academic_course_assignation_log.date_log >="'+str(month[1])+'" and academic_course_assignation_log.date_log<"'+str(month[2])+'" and academic_course_assignation_log.after_course = "'+str(project)+'" and academic_course_assignation_log.before_course = "'+str(project)+'"'
                else:
                    search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "update" and academic_course_assignation_log.date_log >="'+str(month[1])+'" and academic_course_assignation_log.date_log<"'+str(month[2])+'" and academic_course_assignation_log.after_course = "'+str(project)+'" and academic_course_assignation_log.before_course = "'+str(project)+'" and '+personal_query
                countI = db.smart_query(db.academic_course_assignation_log,search).count()
                infoeLevelTemp.append(countI)
            #DELETE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "delete" and academic_course_assignation_log.date_log >="'+str(month[1])+'" and academic_course_assignation_log.date_log<"'+str(month[2])+'" and academic_course_assignation_log.before_course = "'+str(project)+'"'
                else:
                    search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "delete" and academic_course_assignation_log.date_log >="'+str(month[1])+'" and academic_course_assignation_log.date_log<"'+str(month[2])+'" and academic_course_assignation_log.before_course = "'+str(project)+'" and '+personal_query
                countI = db.smart_query(db.academic_course_assignation_log,search).count()
                infoeLevelTemp.append(countI)
            #INSERT PROJECT
            infoLevel.append(infoeLevelTemp)
    #PER ROL
    elif str(request.vars['level'])=="4":
        #ROLES
        roles = GET_ROLES('academic_course_assignation_log')
        #PERIOD OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Period'))
        infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
        infoLevel.append(infoeLevelTemp)
        #MONTH OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Month'))
        infoeLevelTemp.append(str(month[0]))
        infoLevel.append(infoeLevelTemp)
        #PROJECT OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Project'))
        infoeLevelTemp.append(str(project))
        infoLevel.append(infoeLevelTemp)
        #MIDDLE LINE OF REPORT
        infoeLevelTemp=[]
        infoLevel.append(infoeLevelTemp)
        #LABLE DETAIL OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Detail'))
        infoLevel.append(infoeLevelTemp)
        #LABELS OF DATA OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Role'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
            infoeLevelTemp.append(T('Total inserted'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
            infoeLevelTemp.append(T('Total modified'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
            infoeLevelTemp.append(T('Total out'))
        infoLevel.append(infoeLevelTemp)

        for rollT in roles:
            roll=db(db.auth_group.role==rollT).select().first()
            if roll is None:
                roll=db(db.academic_course_assignation_log.roll.like('%'+rollT+'%')).select().first()
                roll=roll.roll
            else:
                roll=roll.role
            infoeLevelTemp = []
            #NAME OF ROLE
            infoeLevelTemp.append(T('Rol '+roll))
            #INSERT
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                if personal_query == '':
                    search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "insert" and academic_course_assignation_log.date_log >="'+str(month[1])+'" and academic_course_assignation_log.date_log<"'+str(month[2])+'" and academic_course_assignation_log.after_course = "'+str(project)+'" and academic_course_assignation_log.roll contains "'+str(roll)+'"'
                else:
                    search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "insert" and academic_course_assignation_log.date_log >="'+str(month[1])+'" and academic_course_assignation_log.date_log<"'+str(month[2])+'" and academic_course_assignation_log.after_course = "'+str(project)+'" and academic_course_assignation_log.roll contains "'+str(roll)+'" and '+personal_query
                countI = db.smart_query(db.academic_course_assignation_log,search).count()
                infoeLevelTemp.append(countI)
            #UPDATE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "update" and academic_course_assignation_log.date_log >="'+str(month[1])+'" and academic_course_assignation_log.date_log<"'+str(month[2])+'" and academic_course_assignation_log.before_course = "'+str(project)+'" and academic_course_assignation_log.after_course = "'+str(project)+'" and academic_course_assignation_log.roll contains "'+str(roll)+'"'
                else:
                    search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "update" and academic_course_assignation_log.date_log >="'+str(month[1])+'" and academic_course_assignation_log.date_log<"'+str(month[2])+'" and academic_course_assignation_log.before_course = "'+str(project)+'" and academic_course_assignation_log.after_course = "'+str(project)+'" and academic_course_assignation_log.roll contains "'+str(roll)+'" and '+personal_query
                countI = db.smart_query(db.academic_course_assignation_log,search).count()
                infoeLevelTemp.append(countI)
            #DELETE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "delete" and academic_course_assignation_log.date_log >="'+str(month[1])+'" and academic_course_assignation_log.date_log<"'+str(month[2])+'" and academic_course_assignation_log.before_course = "'+str(project)+'" and academic_course_assignation_log.roll contains "'+str(roll)+'"'
                else:
                    search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "delete" and academic_course_assignation_log.date_log >="'+str(month[1])+'" and academic_course_assignation_log.date_log<"'+str(month[2])+'" and academic_course_assignation_log.before_course = "'+str(project)+'" and academic_course_assignation_log.roll contains "'+str(roll)+'" and '+personal_query
                countI = db.smart_query(db.academic_course_assignation_log,search).count()
                infoeLevelTemp.append(countI)
            #INSERT ROLE
            infoLevel.append(infoeLevelTemp)
    #PER USER
    elif str(request.vars['level'])=="5":
        #USERS
        usersProject = GET_USERS(period,project,roll,'academic_course_assignation_log')
        #PERIOD OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Period'))
        infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
        infoLevel.append(infoeLevelTemp)
        #MONTH OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Month'))
        infoeLevelTemp.append(str(month[0]))
        infoLevel.append(infoeLevelTemp)
        #PROJECT OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Project'))
        infoeLevelTemp.append(str(project))
        infoLevel.append(infoeLevelTemp)
        #ROL OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Role'))
        infoeLevelTemp.append(T('Rol '+roll))
        infoLevel.append(infoeLevelTemp)
        #MIDDLE LINE OF REPORT
        infoeLevelTemp=[]
        infoLevel.append(infoeLevelTemp)
        #LABLE DETAIL OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Detail'))
        infoLevel.append(infoeLevelTemp)
        #LABELS OF DATA OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('User'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
            infoeLevelTemp.append(T('Total inserted'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
            infoeLevelTemp.append(T('Total modified'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
            infoeLevelTemp.append(T('Total out'))
        infoLevel.append(infoeLevelTemp)

        for userPT in usersProject:
            userP=db(db.auth_user.username==userPT).select().first()
            if userP is None:
                userP=db(db.academic_course_assignation_log.user_name==userPT).select().first()
                userP=userP.user_name
            else:
                userP=userP.username
            infoeLevelTemp = []
            #NAME OF USER
            infoeLevelTemp.append(userP)
            #INSERT
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                if personal_query == '':
                    search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "insert" and academic_course_assignation_log.date_log >="'+str(month[1])+'" and academic_course_assignation_log.date_log<"'+str(month[2])+'" and academic_course_assignation_log.after_course = "'+str(project)+'" and academic_course_assignation_log.roll contains "'+str(roll)+'" and academic_course_assignation_log.user_name ="'+str(userP)+'"'
                else:
                    search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "insert" and academic_course_assignation_log.date_log >="'+str(month[1])+'" and academic_course_assignation_log.date_log<"'+str(month[2])+'" and academic_course_assignation_log.after_course = "'+str(project)+'" and academic_course_assignation_log.roll contains "'+str(roll)+'" and academic_course_assignation_log.user_name ="'+str(userP)+'" and '+personal_query
                countI = db.smart_query(db.academic_course_assignation_log,search).count()
                infoeLevelTemp.append(countI)
            #UPDATE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "update" and academic_course_assignation_log.date_log >="'+str(month[1])+'" and academic_course_assignation_log.date_log<"'+str(month[2])+'" and academic_course_assignation_log.before_course = "'+str(project)+'" and academic_course_assignation_log.after_course = "'+str(project)+'" and academic_course_assignation_log.roll contains "'+str(roll)+'" and academic_course_assignation_log.user_name ="'+str(userP)+'"'
                else:
                    search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "update" and academic_course_assignation_log.date_log >="'+str(month[1])+'" and academic_course_assignation_log.date_log<"'+str(month[2])+'" and academic_course_assignation_log.before_course = "'+str(project)+'" and academic_course_assignation_log.after_course = "'+str(project)+'" and academic_course_assignation_log.roll contains "'+str(roll)+'" and academic_course_assignation_log.user_name ="'+str(userP)+'" and '+personal_query
                countI = db.smart_query(db.academic_course_assignation_log,search).count()
                infoeLevelTemp.append(countI)
            #DELETE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "delete" and academic_course_assignation_log.date_log >="'+str(month[1])+'" and academic_course_assignation_log.date_log<"'+str(month[2])+'" and academic_course_assignation_log.before_course = "'+str(project)+'" and academic_course_assignation_log.roll contains "'+str(roll)+'" and academic_course_assignation_log.user_name ="'+str(userP)+'"'
                else:
                    search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "delete" and academic_course_assignation_log.date_log >="'+str(month[1])+'" and academic_course_assignation_log.date_log<"'+str(month[2])+'" and academic_course_assignation_log.before_course = "'+str(project)+'" and academic_course_assignation_log.roll contains "'+str(roll)+'" and academic_course_assignation_log.user_name ="'+str(userP)+'" and '+personal_query
                countI = db.smart_query(db.academic_course_assignation_log,search).count()
                infoeLevelTemp.append(countI)
            #INSERT USER
            infoLevel.append(infoeLevelTemp)
    #DATA
    elif str(request.vars['level'])=="6":
        #DATA
        grid=[]
        if str(request.vars['type_L'])=="i" or str(request.vars['type_L'])=="all":
            if personal_query == '':
                search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "insert" and academic_course_assignation_log.date_log >="'+str(month[1])+'" and academic_course_assignation_log.date_log<"'+str(month[2])+'" and academic_course_assignation_log.after_course = "'+str(project)+'" and academic_course_assignation_log.roll LIKE "%'+str(roll)+'%" and academic_course_assignation_log.user_name ="'+str(userP)+'"'
            else:
                search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "insert" and academic_course_assignation_log.date_log >="'+str(month[1])+'" and academic_course_assignation_log.date_log<"'+str(month[2])+'" and academic_course_assignation_log.after_course = "'+str(project)+'" and academic_course_assignation_log.roll LIKE "%'+str(roll)+'%" and academic_course_assignation_log.user_name ="'+str(userP)+'" and '+personal_query
            grid.append(db.smart_query(db.academic_course_assignation_log,search).select())
        if str(request.vars['type_L'])=="u" or str(request.vars['type_L'])=="all":
            if personal_query == '':
                search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "update" and academic_course_assignation_log.date_log >="'+str(month[1])+'" and academic_course_assignation_log.date_log<"'+str(month[2])+'" and academic_course_assignation_log.before_course = "'+str(project)+'" and academic_course_assignation_log.after_course = "'+str(project)+'" and academic_course_assignation_log.roll LIKE "%'+str(roll)+'%" and academic_course_assignation_log.user_name ="'+str(userP)+'"'
            else:
                search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "update" and academic_course_assignation_log.date_log >="'+str(month[1])+'" and academic_course_assignation_log.date_log<"'+str(month[2])+'" and academic_course_assignation_log.before_course = "'+str(project)+'" and academic_course_assignation_log.after_course = "'+str(project)+'" and academic_course_assignation_log.roll LIKE "%'+str(roll)+'%" and academic_course_assignation_log.user_name ="'+str(userP)+'" and '+personal_query
            grid.append(db.smart_query(db.academic_course_assignation_log,search).select())
        if str(request.vars['type_L'])=="d" or str(request.vars['type_L'])=="all":
            if personal_query == '':
                search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "delete" and academic_course_assignation_log.date_log >="'+str(month[1])+'" and academic_course_assignation_log.date_log<"'+str(month[2])+'" and academic_course_assignation_log.before_course = "'+str(project)+'" and academic_course_assignation_log.roll LIKE "%'+str(roll)+'%" and academic_course_assignation_log.user_name ="'+str(userP)+'"'
            else:
                search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "delete" and academic_course_assignation_log.date_log >="'+str(month[1])+'" and academic_course_assignation_log.date_log<"'+str(month[2])+'" and academic_course_assignation_log.before_course = "'+str(project)+'" and academic_course_assignation_log.roll LIKE "%'+str(roll)+'%" and academic_course_assignation_log.user_name ="'+str(userP)+'" and '+personal_query
            grid.append(db.smart_query(db.academic_course_assignation_log,search).select())
        #PERIOD
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Period'))
        infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
        infoLevel.append(infoeLevelTemp)
        #MONTH
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Month'))
        infoeLevelTemp.append(str(month[0]))
        infoLevel.append(infoeLevelTemp)
        #PROJECT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Project'))
        infoeLevelTemp.append(str(project))
        infoLevel.append(infoeLevelTemp)
        #ROL
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Role'))
        infoeLevelTemp.append(T('Rol '+roll))
        infoLevel.append(infoeLevelTemp)
        #USER
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('User'))
        infoeLevelTemp.append(str(userP))
        infoLevel.append(infoeLevelTemp)
        #MIDDLE LINE
        infoeLevelTemp=[]
        infoeLevelTemp.append('')
        infoLevel.append(infoeLevelTemp)
        #DETAIL
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Detail'))
        infoLevel.append(infoeLevelTemp)
        #TITLE OF TABLE
        infoeLevelTemp=[]
        infoeLevelTemp.append('Operación')
        infoeLevelTemp.append('Carnet anterior')
        infoeLevelTemp.append('Carnet actual')
        infoeLevelTemp.append('Laboratorio anterior')
        infoeLevelTemp.append('Laboratorio actual')
        infoeLevelTemp.append('Descripción')
        infoeLevelTemp.append('Fecha')
        infoLevel.append(infoeLevelTemp)
        for data in grid:
            for row in data:
                infoeLevelTemp=[]
                infoeLevelTemp.append(row.operation_log)
                infoeLevelTemp.append(row.before_carnet)
                infoeLevelTemp.append(row.after_carnet)
                infoeLevelTemp.append(row.before_laboratory)
                infoeLevelTemp.append(row.after_laboratory)
                infoeLevelTemp.append(row.description)
                infoeLevelTemp.append(row.date_log)
                infoLevel.append(infoeLevelTemp)
    #*****************************************************REPORT*****************************************************
    #****************************************************************************************************************
    #****************************************************************************************************************
    return dict(filename='ReporteGestionAsignaciones', csvdata=infoLevel)


@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def student_assignment_management():
    #****************************************************************************************************************
    #****************************************************************************************************************
    #***************************************CHECK IF THERE IS A PERSONALIZED QUERY***********************************
    personal_query = ''
    makeRedirect = False
    if request.vars['querySearch'] is not None and str(request.vars['querySearch']) != "":
        #PERSONALIZED QUERY SURE WORK
        try:
            personal_query = str(request.vars['querySearch'])
            countI = db.smart_query(db.academic_course_assignation_log,personal_query).count()
            if request.vars['searchT'] is not None and str(request.vars['searchT']) == 'T':
                makeRedirect = True
        except:
            response.flash = T('The query is not valid. The report is displayed without applying any query.')
            personal_query = ''
    if makeRedirect == True:
        redirect(URL('management_reports', 'student_assignment_management',vars=dict(level = 6, period = request.vars['period'], month = str(request.vars['month']), project = str(request.vars['project']), roll = str(request.vars['roll']), userP = str(request.vars['userP']), type_L=request.vars['type_L'], type_U=request.vars['type_U'], querySearch=request.vars['querySearch'])))

    #****************************************************************************************************************
    #****************************************************************************************************************
    #******************************************VERIFY THAT ACCURATE PARAMETERS***************************************
    try:
        #CHECK THAT THE LEVEL OF REPORT IS VALID
        if request.vars['level'] is not None and (int(request.vars['level'])<1 or int(request.vars['level'])>6):
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #VERIFY THAT THE PARAMETERS OF EACH LEVEL BE VALID
        if request.vars['level'] is not None:
            #LEVEL MORE THAN 1
            if int(request.vars['level'])>1:
                #CHECK IF THE TYPE OF REPORT IS VALID
                if request.vars['type_L'] is None or (str(request.vars['type_L'])!="all" and str(request.vars['type_L'])!="i" and str(request.vars['type_L'])!="u" and str(request.vars['type_L'])!="d"):
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))

                period = VALIDATE_PERIOD(request.vars['period'])
                if period is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))
            
            #LEVEL MORE THAN 2
            if int(request.vars['level'])>2:
                #CHECK IF THE TYPE OF REPORT IS VALID
                if request.vars['type_U'] is None or (str(request.vars['type_U'])!="all" and str(request.vars['type_U'])!="i" and str(request.vars['type_U'])!="u" and str(request.vars['type_U'])!="d"):
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))

                #CHECK IF THE MONTH IS VALID
                month = VALIDATE_MONTH(request.vars['month'],period)
                if month is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))
            
            #LEVEL MORE THAN 3
            if int(request.vars['level'])>3:
                #CHECK IF THE PROJECT IS VALID
                project = VALIDATE_PROJECT(request.vars['project'],'academic_course_assignation_log')
                if project is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))
            #LEVEL MORE THAN 4
            if int(request.vars['level'])>4:
                #CHECK IF THE ROLE IS VALID
                roll = VALIDATE_ROLE(request.vars['roll'],'academic_course_assignation_log')
                if roll is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))

            #LEVEL MORE THAN 5
            if int(request.vars['level'])>5:
                #CHECK IF THE USER IS VALID
                userP = VALIDATE_USER(period,project,roll,request.vars['userP'],'academic_course_assignation_log')
                if userP is None:
                    session.flash = T('Not valid Action.')
                    redi*rect(URL('default','index'))
    except:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))


    #****************************************************************************************************************
    #****************************************************************************************************************
    #**************************************************SEARCH REPORT*************************************************
    def filtered_by(flag):
        fsearch_Option=[]
        fsearch_Option.append('=')
        fsearch_Option.append('!=')
        fsearch_Option.append('<')
        fsearch_Option.append('>')
        fsearch_Option.append('<=')
        fsearch_Option.append('>=')
        if flag==True:
            fsearch_Option.append('starts with')
            fsearch_Option.append('contains')
            fsearch_Option.append('in')
            fsearch_Option.append('not in')
        return fsearch_Option


    fsearch = []
    #******************************COMBOS INFORMATION******************************
    #PROJECTS
    if request.vars['level'] is None or int(request.vars['level'])<=3:
        projects = GET_PROJECTS('academic_course_assignation_log')
        if len(projects) != 0:
            projects=sorted(projects)
            fsearch.append(['before_course','Curso anterior',False,[3,projects]])
            fsearch.append(['after_course','Curso actual',False,[3,projects]])
    #ROLES
    if request.vars['level'] is None or int(request.vars['level'])<=4:
        roles = GET_ROLES('academic_course_assignation_log')
        if len(roles) != 0:
            fsearch.append(['roll',T('Rol'),False,[4,sorted(roles)]])
    #PERIODS
    if request.vars['level']=='1' or request.vars['level'] is None:
        groupPeriods = db(db.period_year).select(orderby=~db.period_year.id)
        if len(groupPeriods) != 0:
            fsearch.append(['id_period','Periodo',False,[2,groupPeriods]])
    #DESCRIPTION
    groupDescription = GET_DESCRIPTIONS('academic_course_assignation_log')
    if len(groupDescription) != 0:
        fsearch.append(['description','Descripción',False,[3,sorted(groupDescription)]])
    #DATE
    groupDates = GET_DATES('academic_course_assignation_log')
    if len(groupDates) != 0:
        fsearch.append(['date_log','Fecha',False,[3,sorted(groupDates)]])
    #OPERATION LOG
    fsearch.append(['operation_log',T('Operacion'),False,[3,['insert','update','delete']]])
    #******************************ENTERING USER******************************
    if request.vars['level'] is None or int(request.vars['level'])<=5:
        #ID OF PERSON WHO REGISTER THE GRADE
        fsearch.append(['user_name',T('Usuario'),True,[1]])
    #BEFORE LABORATORY
    fsearch.append(['before_laboratory','Laboratorio anterior',False,[3,['True','False']]])
    #AFTER LABORATORY
    fsearch.append(['after_laboratory','Laboratorio actual',False,[3,['True','False']]])
    #BEFORE CARNET
    fsearch.append(['before_carnet','Carnet anterior',True,[1]])
    #AFTER CARNET
    fsearch.append(['after_carnet','Carnet actual',True,[1]])


    #****************************************************************************************************************
    #****************************************************************************************************************
    #*****************************************************REPORT*****************************************************
    #LEVELS OF REPORT
    from datetime import datetime
    infoLevel = []
    top5=[]
    grid=[]
    #ALL SEMESTERS
    if request.vars['level']=='1' or request.vars['level'] is None:
        if len(groupPeriods) == 0:
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('default','index'))
            

        for period in groupPeriods:
            infoeLevelTemp = []
            #ID OF PERIOD
            infoeLevelTemp.append(period.id)
            #NAME OF PERIOD
            infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
            #INSERT
            if personal_query == '':
                search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "insert"'
            else:
                search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "insert" and '+personal_query
            countI = db.smart_query(db.academic_course_assignation_log,search).count()
            infoeLevelTemp.append(countI)
            #UPDATE
            if personal_query == '':
                search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "update"'
            else:
                search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "update" and '+personal_query
            countI = db.smart_query(db.academic_course_assignation_log,search).count()
            infoeLevelTemp.append(countI)
            #DELETE
            if personal_query == '':
                search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "delete"'
            else:
                search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "delete" and '+personal_query
            countI = db.smart_query(db.academic_course_assignation_log,search).count()
            infoeLevelTemp.append(countI)
            #INSERT PERIOD
            infoLevel.append(infoeLevelTemp)

        #TOP 5 OF PERIOD
        if personal_query == '':
            search='academic_course_assignation_log.id != "-1"'
        else:
            search=personal_query
        top5 = db.smart_query(db.academic_course_assignation_log,search).select(db.academic_course_assignation_log.id_period, db.academic_course_assignation_log.id.count(), orderby=~db.academic_course_assignation_log.id.count(), limitby=(0, 5), groupby=db.academic_course_assignation_log.id_period)
        top5T=[]
        for top in top5:
            periodTop = db(db.period_year.id==top['academic_course_assignation_log.id_period']).select().first()
            top5T.append([T(periodTop.period.name)+' '+str(periodTop.yearp),top['COUNT(academic_course_assignation_log.id)']])
        top5=top5T
    #PER MONTH
    elif str(request.vars['level'])=="2":
        for month in GET_MONTH_PERIOD(period):
            start = datetime.strptime(str(period.yearp) + '-' + str(month[0]) +'-01', "%Y-%m-%d")
            if month[2]==1:
                end = datetime.strptime(str(period.yearp+1) + '-' + str(month[2]) +'-01', "%Y-%m-%d")
            else:
                end = datetime.strptime(str(period.yearp) + '-' + str(month[2]) +'-01', "%Y-%m-%d")
            infoeLevelTemp = []
            #NAME OF PERIOD
            infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
            #ID OF MONTH
            infoeLevelTemp.append(month[0])
            #NAME OF MONTH
            infoeLevelTemp.append(month[1]+' '+str(period.yearp))
            #INSERT
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                if personal_query == '':
                    search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "insert" and academic_course_assignation_log.date_log >="'+str(start)+'" and academic_course_assignation_log.date_log<"'+str(end)+'"'
                else:
                    search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "insert" and academic_course_assignation_log.date_log >="'+str(start)+'" and academic_course_assignation_log.date_log<"'+str(end)+'" and '+personal_query
                countI = db.smart_query(db.academic_course_assignation_log,search).count()
                infoeLevelTemp.append(countI)
            #UPDATE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "update" and academic_course_assignation_log.date_log>="'+str(start)+'" and academic_course_assignation_log.date_log<"'+str(end)+'"'
                else:
                    search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "update" and academic_course_assignation_log.date_log>="'+str(start)+'" and academic_course_assignation_log.date_log<"'+str(end)+'" and '+personal_query
                countI = db.smart_query(db.academic_course_assignation_log,search).count()
                infoeLevelTemp.append(countI)
            #DELETE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "delete" and academic_course_assignation_log.date_log>="'+str(start)+'" and academic_course_assignation_log.date_log<"'+str(end)+'"'
                else:
                    search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "delete" and academic_course_assignation_log.date_log>="'+str(start)+'" and academic_course_assignation_log.date_log<"'+str(end)+'" and '+personal_query
                countI = db.smart_query(db.academic_course_assignation_log,search).count()
                infoeLevelTemp.append(countI)
            #INSERT MONTH
            infoLevel.append(infoeLevelTemp)
    #PER PROJECT
    elif str(request.vars['level'])=="3":
        if len(projects) == 0:
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('management_reports', 'student_assignment_management',vars=dict(level='2',period = str(request.vars['period']), type_L = str(request.vars['type_U']), querySearch=personal_query)))

        #TOP 5 OF PROJECT
        top5Tempo = []
        for projectT in projects:
            project=db(db.project.name==projectT).select().first()
            if project is None:
                project=db((db.course_activity_log.before_course==projectT)|(db.course_activity_log.after_course==projectT)).select().first()
                if project.before_course is not None:
                    project=project.before_course
                else:
                    project=project.after_course
            else:
                project=project.name
            infoeLevelTemp = []
            #NAME OF PERIOD
            infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
            #NAME OF MONTH
            infoeLevelTemp.append(month[0])
            #ID OF PROJECT
            infoeLevelTemp.append(project)
            #NAME OF PROJECT
            infoeLevelTemp.append(project)
            #TOP 5 OF PROJECT
            totalTemp=0
            #INSERT
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                if personal_query == '':
                    search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "insert" and academic_course_assignation_log.date_log >="'+str(month[1])+'" and academic_course_assignation_log.date_log<"'+str(month[2])+'" and academic_course_assignation_log.after_course = "'+str(project)+'"'
                else:
                    search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "insert" and academic_course_assignation_log.date_log >="'+str(month[1])+'" and academic_course_assignation_log.date_log<"'+str(month[2])+'" and academic_course_assignation_log.after_course = "'+str(project)+'" and '+personal_query
                countI = db.smart_query(db.academic_course_assignation_log,search).count()
                infoeLevelTemp.append(countI)
                #TOP 5 OF PROJECT
                totalTemp=totalTemp+countI
            #UPDATE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "update" and academic_course_assignation_log.date_log >="'+str(month[1])+'" and academic_course_assignation_log.date_log<"'+str(month[2])+'" and academic_course_assignation_log.after_course = "'+str(project)+'" and academic_course_assignation_log.before_course = "'+str(project)+'"'
                else:
                    search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "update" and academic_course_assignation_log.date_log >="'+str(month[1])+'" and academic_course_assignation_log.date_log<"'+str(month[2])+'" and academic_course_assignation_log.after_course = "'+str(project)+'" and academic_course_assignation_log.before_course = "'+str(project)+'" and '+personal_query
                countI = db.smart_query(db.academic_course_assignation_log,search).count()
                infoeLevelTemp.append(countI)
                #TOP 5 OF PROJECT
                totalTemp=totalTemp+countI
            #DELETE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "delete" and academic_course_assignation_log.date_log >="'+str(month[1])+'" and academic_course_assignation_log.date_log<"'+str(month[2])+'" and academic_course_assignation_log.before_course = "'+str(project)+'"'
                else:
                    search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "delete" and academic_course_assignation_log.date_log >="'+str(month[1])+'" and academic_course_assignation_log.date_log<"'+str(month[2])+'" and academic_course_assignation_log.before_course = "'+str(project)+'" and '+personal_query
                countI = db.smart_query(db.academic_course_assignation_log,search).count()
                infoeLevelTemp.append(countI)
                #TOP 5 OF PROJECT
                totalTemp=totalTemp+countI
            #INSERT PROJECT
            infoLevel.append(infoeLevelTemp)
            #TOP 5 OF PROJECT
            if totalTemp>0:
                top5Tempo.append([totalTemp,project])
        #TOP 5 OF PROJECT
        top5Tempo=sorted(top5Tempo,reverse = True)
        countTop=0
        for top in top5Tempo:
            if countTop<5:
                top5.append(top)
            countTop=countTop+1
    #PER ROL
    elif str(request.vars['level'])=="4":
        if len(roles) == 0:
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('management_reports', 'student_assignment_management',vars=dict(level='3', period = str(request.vars['period']), month = str(request.vars['month']), type_L = str(request.vars['type_U']), type_U = str(request.vars['type_U']), querySearch=personal_query)))

        for rollT in roles:
            roll=db(db.auth_group.role==rollT).select().first()
            if roll is None:
                roll=db(db.academic_course_assignation_log.roll.like('%'+rollT+'%')).select().first()
                roll=roll.roll
            else:
                roll=roll.role
            infoeLevelTemp = []
            #NAME OF PERIOD
            infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
            #NAME OF MONTH
            infoeLevelTemp.append(month[0])
            #NAME OF PROJECT
            infoeLevelTemp.append(project)
            #ID OF ROLE
            infoeLevelTemp.append(roll)
            #NAME OF ROLE
            infoeLevelTemp.append(T('Rol '+roll))
            #INSERT
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                if personal_query == '':
                    search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "insert" and academic_course_assignation_log.date_log >="'+str(month[1])+'" and academic_course_assignation_log.date_log<"'+str(month[2])+'" and academic_course_assignation_log.after_course = "'+str(project)+'" and academic_course_assignation_log.roll contains "'+str(roll)+'"'
                else:
                    search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "insert" and academic_course_assignation_log.date_log >="'+str(month[1])+'" and academic_course_assignation_log.date_log<"'+str(month[2])+'" and academic_course_assignation_log.after_course = "'+str(project)+'" and academic_course_assignation_log.roll contains "'+str(roll)+'" and '+personal_query
                countI = db.smart_query(db.academic_course_assignation_log,search).count()
                infoeLevelTemp.append(countI)
            #UPDATE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "update" and academic_course_assignation_log.date_log >="'+str(month[1])+'" and academic_course_assignation_log.date_log<"'+str(month[2])+'" and academic_course_assignation_log.before_course = "'+str(project)+'" and academic_course_assignation_log.after_course = "'+str(project)+'" and academic_course_assignation_log.roll contains "'+str(roll)+'"'
                else:
                    search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "update" and academic_course_assignation_log.date_log >="'+str(month[1])+'" and academic_course_assignation_log.date_log<"'+str(month[2])+'" and academic_course_assignation_log.before_course = "'+str(project)+'" and academic_course_assignation_log.after_course = "'+str(project)+'" and academic_course_assignation_log.roll contains "'+str(roll)+'" and '+personal_query
                countI = db.smart_query(db.academic_course_assignation_log,search).count()
                infoeLevelTemp.append(countI)
            #DELETE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "delete" and academic_course_assignation_log.date_log >="'+str(month[1])+'" and academic_course_assignation_log.date_log<"'+str(month[2])+'" and academic_course_assignation_log.before_course = "'+str(project)+'" and academic_course_assignation_log.roll contains "'+str(roll)+'"'
                else:
                    search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "delete" and academic_course_assignation_log.date_log >="'+str(month[1])+'" and academic_course_assignation_log.date_log<"'+str(month[2])+'" and academic_course_assignation_log.before_course = "'+str(project)+'" and academic_course_assignation_log.roll contains "'+str(roll)+'" and '+personal_query
                countI = db.smart_query(db.academic_course_assignation_log,search).count()
                infoeLevelTemp.append(countI)
            #INSERT ROLE
            infoLevel.append(infoeLevelTemp)
    #PER USER
    elif str(request.vars['level'])=="5":
        #VERIFY THAT CAN SHOW THE LEVEL OF THE REPORT
        usersProject = GET_USERS(period,project,roll,'academic_course_assignation_log')
        if len(usersProject) == 0:
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('management_reports', 'student_assignment_management',vars=dict(level='4', period = str(request.vars['period']), month = str(request.vars['month']), project = str(request.vars['project']), type_L = str(request.vars['type_U']), type_U = str(request.vars['type_U']), querySearch=personal_query)))

        #TOP 5 OF PROJECT
        top5Tempo = []
        for userPT in usersProject:
            userP=db(db.auth_user.username==userPT).select().first()
            if userP is None:
                userP=db(db.academic_course_assignation_log.user_name==userPT).select().first()
                userP=userP.user_name
            else:
                userP=userP.username
            infoeLevelTemp = []
            #NAME OF PERIOD
            infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
            #NAME OF MONTH
            infoeLevelTemp.append(month[0])
            #NAME OF PROJECT
            infoeLevelTemp.append(project)
            #NAME OF ROLE
            infoeLevelTemp.append(T('Rol '+roll))
            #ID OF USER
            infoeLevelTemp.append(userP)
            #NAME OF USER
            infoeLevelTemp.append(userP)
            #TOP 5 OF USER
            totalTemp=0
            #INSERT
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                if personal_query == '':
                    search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "insert" and academic_course_assignation_log.date_log >="'+str(month[1])+'" and academic_course_assignation_log.date_log<"'+str(month[2])+'" and academic_course_assignation_log.after_course = "'+str(project)+'" and academic_course_assignation_log.roll contains "'+str(roll)+'" and academic_course_assignation_log.user_name ="'+str(userP)+'"'
                else:
                    search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "insert" and academic_course_assignation_log.date_log >="'+str(month[1])+'" and academic_course_assignation_log.date_log<"'+str(month[2])+'" and academic_course_assignation_log.after_course = "'+str(project)+'" and academic_course_assignation_log.roll contains "'+str(roll)+'" and academic_course_assignation_log.user_name ="'+str(userP)+'" and '+personal_query
                countI = db.smart_query(db.academic_course_assignation_log,search).count()
                infoeLevelTemp.append(countI)
                #TOP 5 OF USER
                totalTemp=totalTemp+countI
            #UPDATE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "update" and academic_course_assignation_log.date_log >="'+str(month[1])+'" and academic_course_assignation_log.date_log<"'+str(month[2])+'" and academic_course_assignation_log.before_course = "'+str(project)+'" and academic_course_assignation_log.after_course = "'+str(project)+'" and academic_course_assignation_log.roll contains "'+str(roll)+'" and academic_course_assignation_log.user_name ="'+str(userP)+'"'
                else:
                    search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "update" and academic_course_assignation_log.date_log >="'+str(month[1])+'" and academic_course_assignation_log.date_log<"'+str(month[2])+'" and academic_course_assignation_log.before_course = "'+str(project)+'" and academic_course_assignation_log.after_course = "'+str(project)+'" and academic_course_assignation_log.roll contains "'+str(roll)+'" and academic_course_assignation_log.user_name ="'+str(userP)+'" and '+personal_query
                countI = db.smart_query(db.academic_course_assignation_log,search).count()
                infoeLevelTemp.append(countI)
                #TOP 5 OF USER
                totalTemp=totalTemp+countI
            #DELETE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "delete" and academic_course_assignation_log.date_log >="'+str(month[1])+'" and academic_course_assignation_log.date_log<"'+str(month[2])+'" and academic_course_assignation_log.before_course = "'+str(project)+'" and academic_course_assignation_log.roll contains "'+str(roll)+'" and academic_course_assignation_log.user_name ="'+str(userP)+'"'
                else:
                    search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "delete" and academic_course_assignation_log.date_log >="'+str(month[1])+'" and academic_course_assignation_log.date_log<"'+str(month[2])+'" and academic_course_assignation_log.before_course = "'+str(project)+'" and academic_course_assignation_log.roll contains "'+str(roll)+'" and academic_course_assignation_log.user_name ="'+str(userP)+'" and '+personal_query
                countI = db.smart_query(db.academic_course_assignation_log,search).count()
                infoeLevelTemp.append(countI)
                #TOP 5 OF USER
                totalTemp=totalTemp+countI
            #INSERT USER
            infoLevel.append(infoeLevelTemp)
            #TOP 5 OF USER
            top5Tempo.append([totalTemp,userP])
        #TOP 5 OF USER
        top5Tempo=sorted(top5Tempo,reverse = True)
        countTop=0
        for top in top5Tempo:
            if countTop<5:
                top5.append(top)
            countTop=countTop+1
    #DATA
    elif str(request.vars['level'])=="6":
        grid = []
        if str(request.vars['type_L'])=="i" or str(request.vars['type_L'])=="all":
            if personal_query == '':
                search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "insert" and academic_course_assignation_log.date_log >="'+str(month[1])+'" and academic_course_assignation_log.date_log<"'+str(month[2])+'" and academic_course_assignation_log.after_course = "'+str(project)+'" and academic_course_assignation_log.roll LIKE "%'+str(roll)+'%" and academic_course_assignation_log.user_name ="'+str(userP)+'"'
            else:
                search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "insert" and academic_course_assignation_log.date_log >="'+str(month[1])+'" and academic_course_assignation_log.date_log<"'+str(month[2])+'" and academic_course_assignation_log.after_course = "'+str(project)+'" and academic_course_assignation_log.roll LIKE "%'+str(roll)+'%" and academic_course_assignation_log.user_name ="'+str(userP)+'" and '+personal_query
            for data in db.smart_query(db.academic_course_assignation_log,search).select():
                grid.append(data.id)
        if str(request.vars['type_L'])=="u" or str(request.vars['type_L'])=="all":
            if personal_query == '':
                search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "update" and academic_course_assignation_log.date_log >="'+str(month[1])+'" and academic_course_assignation_log.date_log<"'+str(month[2])+'" and academic_course_assignation_log.before_course = "'+str(project)+'" and academic_course_assignation_log.after_course = "'+str(project)+'" and academic_course_assignation_log.roll LIKE "%'+str(roll)+'%" and academic_course_assignation_log.user_name ="'+str(userP)+'"'
            else:
                search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "update" and academic_course_assignation_log.date_log >="'+str(month[1])+'" and academic_course_assignation_log.date_log<"'+str(month[2])+'" and academic_course_assignation_log.before_course = "'+str(project)+'" and academic_course_assignation_log.after_course = "'+str(project)+'" and academic_course_assignation_log.roll LIKE "%'+str(roll)+'%" and academic_course_assignation_log.user_name ="'+str(userP)+'" and '+personal_query
            for data in db.smart_query(db.academic_course_assignation_log,search).select():
                grid.append(data.id)
        if str(request.vars['type_L'])=="d" or str(request.vars['type_L'])=="all":
            if personal_query == '':
                search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "delete" and academic_course_assignation_log.date_log >="'+str(month[1])+'" and academic_course_assignation_log.date_log<"'+str(month[2])+'" and academic_course_assignation_log.before_course = "'+str(project)+'" and academic_course_assignation_log.roll LIKE "%'+str(roll)+'%" and academic_course_assignation_log.user_name ="'+str(userP)+'"'
            else:
                search='academic_course_assignation_log.id_period = "'+str(period.id)+'" and academic_course_assignation_log.operation_log = "delete" and academic_course_assignation_log.date_log >="'+str(month[1])+'" and academic_course_assignation_log.date_log<"'+str(month[2])+'" and academic_course_assignation_log.before_course = "'+str(project)+'" and academic_course_assignation_log.roll LIKE "%'+str(roll)+'%" and academic_course_assignation_log.user_name ="'+str(userP)+'" and '+personal_query
            for data in db.smart_query(db.academic_course_assignation_log,search).select():
                grid.append(data.id)
        #TITLE
        infoeLevelTemp=[]
        infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
        infoeLevelTemp.append(str(month[0]))
        infoeLevelTemp.append(project)
        infoeLevelTemp.append(T('Rol '+roll))
        infoeLevelTemp.append(str(userP))
        infoLevel.append(infoeLevelTemp)
        #REPORT
        if len(grid) == 0:
            grid.append(-1)
        #GRID
        db.academic_course_assignation_log.id.readable = False
        db.academic_course_assignation_log.id.writable = False
        db.academic_course_assignation_log.user_name.readable = False
        db.academic_course_assignation_log.user_name.writable = False
        db.academic_course_assignation_log.roll.readable = False
        db.academic_course_assignation_log.roll.writable = False
        db.academic_course_assignation_log.before_course.readable = False
        db.academic_course_assignation_log.before_course.writable = False
        db.academic_course_assignation_log.after_course.readable = False
        db.academic_course_assignation_log.after_course.writable = False
        db.academic_course_assignation_log.before_year.readable = False
        db.academic_course_assignation_log.before_year.writable = False
        db.academic_course_assignation_log.after_year.readable = False
        db.academic_course_assignation_log.after_year.writable = False
        db.academic_course_assignation_log.before_semester.readable = False
        db.academic_course_assignation_log.before_semester.writable = False
        db.academic_course_assignation_log.after_semester.readable = False
        db.academic_course_assignation_log.after_semester.writable = False
        db.academic_course_assignation_log.id_academic_course_assignation.readable = False
        db.academic_course_assignation_log.id_academic_course_assignation.writable = False
        db.academic_course_assignation_log.id_period.readable = False
        db.academic_course_assignation_log.id_period.writable = False
        grid = SQLFORM.grid(db.academic_course_assignation_log.id.belongs(grid), csv=False, create=False, editable=False, deletable=False, paginate=9, searchable=False)
    return dict(fsearch=fsearch, filtered_by=filtered_by, personal_query=personal_query, infoLevel=infoLevel, top5=top5, grid=grid) 


#*************************************************************************************************************************************
#*************************************************************************************************************************************
#********************************************MANAGEMENT REPORT CHANGE REQUEST ACTIVITIES WITH METRIC**********************************
@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def change_request_activities_with_metric_management_export():
    #VERIFI THAT ACCURATE PARAMETERS
    try:
        #CHECK IF THE TYPE OF EXPORT IS VALID
        if request.vars['list_type'] is None or str(request.vars['list_type'])!="csv":
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #CHECK THAT THE LEVEL OF REPORT IS VALID
        if request.vars['level'] is not None and (int(request.vars['level'])<1 or int(request.vars['level'])>5):
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('default','index'))

        #VERIFY THAT THE PARAMETERS OF EACH LEVEL BE VALID
        if request.vars['level'] is not None:
            #LEVEL MORE THAN 1
            if int(request.vars['level'])>1:
                #CHECK IF THE TYPE OF REPORT IS VALID
                if request.vars['type_L'] is None or (str(request.vars['type_L'])!="all" and str(request.vars['type_L'])!="i" and str(request.vars['type_L'])!="u" and str(request.vars['type_L'])!="d" and str(request.vars['type_L'])!="p"):
                    session.flash = T('Report no visible: There are no parameters required to display the report.')
                    redirect(URL('default','index'))

                period = VALIDATE_PERIOD(request.vars['period'])
                if period is None:
                    session.flash = T('Report no visible: There are no parameters required to display the report.')
                    redirect(URL('default','index'))
            
            #LEVEL MORE THAN 2
            if int(request.vars['level'])>2:
                #CHECK IF THE TYPE OF REPORT IS VALID
                if request.vars['type_U'] is None or (str(request.vars['type_U'])!="all" and str(request.vars['type_U'])!="i" and str(request.vars['type_U'])!="u" and str(request.vars['type_U'])!="d" and str(request.vars['type_L'])!="p"):
                    session.flash = T('Report no visible: There are no parameters required to display the report.')
                    redirect(URL('default','index'))

                #CHECK IF THE MONTH IS VALID
                month = VALIDATE_MONTH(request.vars['month'],period)
                if month is None:
                    session.flash = T('Report no visible: There are no parameters required to display the report.')
                    redirect(URL('default','index'))
            
            #LEVEL MORE THAN 3
            if int(request.vars['level'])>3:
                #CHECK IF THE PROJECT IS VALID
                project = VALIDATE_PROJECT(request.vars['project'],'requestchange_activity_log')
                if project is None:
                    session.flash = T('Report no visible: There are no parameters required to display the report.')
                    redirect(URL('default','index'))

            #LEVEL MORE THAN 4
            if int(request.vars['level'])>4:
                #CHECK IF THE USER IS VALID
                userP = VALIDATE_USER(period,project,'Student',request.vars['userP'],'academic_course_assignation_log')
                if userP is None:
                    session.flash = T('Report no visible: There are no parameters required to display the report.')
                    redirect(URL('default','index'))
    except:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))

    #CHECK IF THERE IS A PERSONALIZED QUERY
    personal_query = ''
    if request.vars['querySearch'] is not None and str(request.vars['querySearch']) != "":
        #PERSONALIZED QUERY SURE WORK
        try:
            personal_query = str(request.vars['querySearch'])
            countI = db.smart_query(db.requestchange_activity_log,personal_query).count()
        except:
            personal_query = ''

    #****************************************************************************************************************
    #****************************************************************************************************************
    #*****************************************************REPORT*****************************************************
    from datetime import datetime
    #TITLE
    infoLevel = []
    infoeLevelTemp=[]
    infoeLevelTemp.append('Universidad de San Carlos de Guatemala')
    infoLevel.append(infoeLevelTemp)
    infoeLevelTemp=[]
    infoeLevelTemp.append('Facultad de Ingeniería')
    infoLevel.append(infoeLevelTemp)
    infoeLevelTemp=[]
    infoeLevelTemp.append('Escuela de Ciencias y Sistemas')
    infoLevel.append(infoeLevelTemp)
    #TYPE OF REPORT
    infoeLevelTemp=[]
    infoeLevelTemp.append(T('Type'))
    infoeLevelTemp.append(T('Change Request Management Activity with Metric'))
    infoLevel.append(infoeLevelTemp)
    #DESCRIPTION OF REPORT
    infoeLevelTemp=[]
    infoeLevelTemp.append(T('Description'))
    infoeLevelTemp.append(T('Report of operations for managing change requests metric activities'))
    infoLevel.append(infoeLevelTemp)
    #LEVELS OF REPORT
    #ALL SEMESTERS
    if request.vars['level'] is None or str(request.vars['level'])=="1":
        #MIDDLE LINE OF REPORT
        infoeLevelTemp=[]
        infoLevel.append(infoeLevelTemp)
        #LABLE DETAIL OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Detail'))
        infoLevel.append(infoeLevelTemp)
        #LABELS OF DATA OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Period'))
        infoeLevelTemp.append(T('Total Made Requests'))
        infoeLevelTemp.append(T('Total Accepted request'))
        infoeLevelTemp.append(T('Total Rejected request'))
        infoeLevelTemp.append(T('Total Pending Requests'))
        infoLevel.append(infoeLevelTemp)
        for period in db(db.period_year).select(orderby=~db.period_year.id):
            infoeLevelTemp = []
            #NAME OF PERIOD
            infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
            #MADE
            if personal_query == '':
                search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.status = "Pending"'
            else:
                search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.status = "Pending" and '+personal_query
            countI = db.smart_query(db.requestchange_activity_log,search).count()
            infoeLevelTemp.append(countI)
            #ACCEPTED
            if personal_query == '':
                search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.status = "Accepted"'
            else:
                search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.status = "Accepted" and '+personal_query
            countI = db.smart_query(db.requestchange_activity_log,search).count()
            infoeLevelTemp.append(countI)
            #REJECTED
            if personal_query == '':
                search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.status = "Rejected"'
            else:
                search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.status = "Rejected" and '+personal_query
            countI = db.smart_query(db.requestchange_activity_log,search).count()
            infoeLevelTemp.append(countI)
            #PENDING
            infoeLevelTemp.append(infoeLevelTemp[1]-infoeLevelTemp[2]-infoeLevelTemp[3])
            #INSERT PERIOD
            infoLevel.append(infoeLevelTemp)
    #PER MONTH
    elif str(request.vars['level'])=="2":
        #PERIOD OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Period'))
        infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
        infoLevel.append(infoeLevelTemp)
        #MIDDLE LINE OF REPORT
        infoeLevelTemp=[]
        infoLevel.append(infoeLevelTemp)
        #LABLE DETAIL OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Detail'))
        infoLevel.append(infoeLevelTemp)
        #LABELS OF DATA OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Month'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
            infoeLevelTemp.append(T('Total Made Requests'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
            infoeLevelTemp.append(T('Total Accepted request'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
            infoeLevelTemp.append(T('Total Rejected request'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="p":
            infoeLevelTemp.append(T('Total Pending Requests'))
        infoLevel.append(infoeLevelTemp)

        for month in GET_MONTH_PERIOD(period):
            start = datetime.strptime(str(period.yearp) + '-' + str(month[0]) +'-01', "%Y-%m-%d")
            if month[2]==1:
                end = datetime.strptime(str(period.yearp+1) + '-' + str(month[2]) +'-01', "%Y-%m-%d")
            else:
                end = datetime.strptime(str(period.yearp) + '-' + str(month[2]) +'-01', "%Y-%m-%d")
            infoeLevelTemp = []
            #NAME OF MONTH
            infoeLevelTemp.append(month[1]+' '+str(period.yearp))
            #MADE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(start)+'" and requestchange_activity_log.date_request<"'+str(end)+'" and requestchange_activity_log.status = "Pending"'
                else:
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(start)+'" and requestchange_activity_log.date_request<"'+str(end)+'" and requestchange_activity_log.status = "Pending" and '+personal_query
                countI = db.smart_query(db.requestchange_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #ACCEPTED
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                if personal_query == '':
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(start)+'" and requestchange_activity_log.date_request_resolve<"'+str(end)+'" and requestchange_activity_log.status = "Accepted"'
                else:
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(start)+'" and requestchange_activity_log.date_request_resolve<"'+str(end)+'" and requestchange_activity_log.status = "Accepted" and '+personal_query
                countI = db.smart_query(db.requestchange_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #REJECTED
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(start)+'" and requestchange_activity_log.date_request_resolve<"'+str(end)+'" and requestchange_activity_log.status = "Rejected"'
                else:
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(start)+'" and requestchange_activity_log.date_request_resolve<"'+str(end)+'" and requestchange_activity_log.status = "Rejected" and '+personal_query
                countI = db.smart_query(db.requestchange_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #PENDING
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="p":
                if period.period==1:
                    if personal_query == '':
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(period.yearp)+'-01-01" and requestchange_activity_log.date_request<"'+str(end)+'" and requestchange_activity_log.status = "Pending"'
                    else:
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(period.yearp)+'-01-01" and requestchange_activity_log.date_request<"'+str(end)+'" and requestchange_activity_log.status = "Pending" and '+personal_query
                    countP = db.smart_query(db.requestchange_activity_log,search).count()
                    if personal_query == '':
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(period.yearp)+'-01-01" and requestchange_activity_log.date_request_resolve<"'+str(end)+'" and requestchange_activity_log.status != "Pending"'
                    else:
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(period.yearp)+'-01-01" and requestchange_activity_log.date_request_resolve<"'+str(end)+'" and requestchange_activity_log.status != "Pending" and '+personal_query
                    countNP = db.smart_query(db.requestchange_activity_log,search).count()
                else:
                    if personal_query == '':
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(period.yearp)+'-06-01" and requestchange_activity_log.date_request<"'+str(end)+'" and requestchange_activity_log.status = "Pending"'
                    else:
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(period.yearp)+'-06-01" and requestchange_activity_log.date_request<"'+str(end)+'" and requestchange_activity_log.status = "Pending" and '+personal_query
                    countP = db.smart_query(db.requestchange_activity_log,search).count()
                    if personal_query == '':
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(period.yearp)+'-06-01" and requestchange_activity_log.date_request_resolve<"'+str(end)+'" and requestchange_activity_log.status != "Pending"'
                    else:
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(period.yearp)+'-06-01" and requestchange_activity_log.date_request_resolve<"'+str(end)+'" and requestchange_activity_log.status != "Pending" and '+personal_query
                    countNP = db.smart_query(db.requestchange_activity_log,search).count()
                infoeLevelTemp.append(countP-countNP)
            #INSERT MONTH
            infoLevel.append(infoeLevelTemp)
    #PER PROJECT
    elif str(request.vars['level'])=="3":
        #PROJECTS
        projects = GET_PROJECTS('requestchange_activity_log')
        projects=sorted(projects)
        #PERIOD OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Period'))
        infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
        infoLevel.append(infoeLevelTemp)
        #MONTH OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Month'))
        infoeLevelTemp.append(str(month[0]))
        infoLevel.append(infoeLevelTemp)
        #MIDDLE LINE OF REPORT
        infoeLevelTemp=[]
        infoLevel.append(infoeLevelTemp)
        #LABLE DETAIL OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Detail'))
        infoLevel.append(infoeLevelTemp)
        #LABELS OF DATA OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Project'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
            infoeLevelTemp.append(T('Total Made Requests'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
            infoeLevelTemp.append(T('Total Accepted request'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
            infoeLevelTemp.append(T('Total Rejected request'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="p":
            infoeLevelTemp.append(T('Total Pending Requests'))
        infoLevel.append(infoeLevelTemp)

        for projectT in projects:
            project=db(db.project.name==projectT).select().first()
            if project is None:
                project=db((db.course_activity_log.before_course==projectT)|(db.course_activity_log.after_course==projectT)).select().first()
                if project.before_course is not None:
                    project=project.before_course
                else:
                    project=project.after_course
            else:
                project=project.name
            infoeLevelTemp = []
            #NAME OF PROJECT
            infoeLevelTemp.append(project)
            #MADE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(month[1])+'" and requestchange_activity_log.date_request<"'+str(month[2])+'" and requestchange_activity_log.status = "Pending" and requestchange_activity_log.course = "'+str(project)+'"'
                else:
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(month[1])+'" and requestchange_activity_log.date_request<"'+str(month[2])+'" and requestchange_activity_log.status = "Pending" and requestchange_activity_log.course = "'+str(project)+'" and '+personal_query
                countI = db.smart_query(db.requestchange_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #ACCEPTED
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                if personal_query == '':
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(month[1])+'" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status = "Accepted" and requestchange_activity_log.course = "'+str(project)+'"'
                else:
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(month[1])+'" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status = "Accepted" and requestchange_activity_log.course = "'+str(project)+'" and '+personal_query
                countI = db.smart_query(db.requestchange_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #REJECTED
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(month[1])+'" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status = "Rejected" and requestchange_activity_log.course = "'+str(project)+'"'
                else:
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(month[1])+'" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status = "Rejected" and requestchange_activity_log.course = "'+str(project)+'" and '+personal_query
                countI = db.smart_query(db.requestchange_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #PENDING
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="p":
                if period.period==1:
                    if personal_query == '':
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(period.yearp)+'-01-01" and requestchange_activity_log.date_request<"'+str(month[2])+'" and requestchange_activity_log.status = "Pending" and requestchange_activity_log.course = "'+str(project)+'"'
                    else:
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(period.yearp)+'-01-01" and requestchange_activity_log.date_request<"'+str(month[2])+'" and requestchange_activity_log.status = "Pending" and requestchange_activity_log.course = "'+str(project)+'" and '+personal_query
                    countP = db.smart_query(db.requestchange_activity_log,search).count()
                    if personal_query == '':
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(period.yearp)+'-01-01" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status != "Pending" and requestchange_activity_log.course = "'+str(project)+'"'
                    else:
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(period.yearp)+'-01-01" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status != "Pending" and requestchange_activity_log.course = "'+str(project)+'" and '+personal_query
                    countNP = db.smart_query(db.requestchange_activity_log,search).count()
                else:
                    if personal_query == '':
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(period.yearp)+'-06-01" and requestchange_activity_log.date_request<"'+str(month[2])+'" and requestchange_activity_log.status = "Pending" and requestchange_activity_log.course = "'+str(project)+'"'
                    else:
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(period.yearp)+'-06-01" and requestchange_activity_log.date_request<"'+str(month[2])+'" and requestchange_activity_log.status = "Pending" and requestchange_activity_log.course = "'+str(project)+'" and '+personal_query
                    countP = db.smart_query(db.requestchange_activity_log,search).count()
                    if personal_query == '':
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(period.yearp)+'-06-01" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status != "Pending" and requestchange_activity_log.course = "'+str(project)+'"'
                    else:
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(period.yearp)+'-06-01" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status != "Pending" and requestchange_activity_log.course = "'+str(project)+'" and '+personal_query
                    countNP = db.smart_query(db.requestchange_activity_log,search).count()
                infoeLevelTemp.append(countP-countNP)
            #INSERT PROJECT
            infoLevel.append(infoeLevelTemp)
    #PER USER
    elif str(request.vars['level'])=="4":
        #USERS
        usersProject = GET_USERS(period,project,'Student','requestchange_activity_log')
        #PERIOD OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Period'))
        infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
        infoLevel.append(infoeLevelTemp)
        #MONTH OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Month'))
        infoeLevelTemp.append(str(month[0]))
        infoLevel.append(infoeLevelTemp)
        #PROJECT OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Project'))
        infoeLevelTemp.append(str(project))
        infoLevel.append(infoeLevelTemp)
        #ROL OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Role'))
        infoeLevelTemp.append(T('Rol Student'))
        infoLevel.append(infoeLevelTemp)
        #MIDDLE LINE OF REPORT
        infoeLevelTemp=[]
        infoLevel.append(infoeLevelTemp)
        #LABLE DETAIL OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Detail'))
        infoLevel.append(infoeLevelTemp)
        #LABELS OF DATA OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('User'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
            infoeLevelTemp.append(T('Total Made Requests'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
            infoeLevelTemp.append(T('Total Accepted request'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
            infoeLevelTemp.append(T('Total Rejected request'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="p":
            infoeLevelTemp.append(T('Total Pending Requests'))
        infoLevel.append(infoeLevelTemp)

        for userPT in usersProject:
            userP=db(db.auth_user.username==userPT).select().first()
            if userP is None:
                userP=db(db.requestchange_activity_log.user_request==userPT).select().first()
                userP=userP.user_request
            else:
                userP=userP.username
            infoeLevelTemp = []
            #NAME OF USER
            infoeLevelTemp.append(userP)
            #MADE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                countI = 0
                if personal_query == '':
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(month[1])+'" and requestchange_activity_log.date_request<"'+str(month[2])+'" and requestchange_activity_log.status = "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'"'
                else:
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(month[1])+'" and requestchange_activity_log.date_request<"'+str(month[2])+'" and requestchange_activity_log.status = "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'" and '+personal_query
                countI = db.smart_query(db.requestchange_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #ACCEPTED
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                if personal_query == '':
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(month[1])+'" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status = "Accepted" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'"'
                else:
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(month[1])+'" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status = "Accepted" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'" and '+personal_query
                countI = db.smart_query(db.requestchange_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #REJECTED
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(month[1])+'" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status = "Rejected" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'"'
                else:
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(month[1])+'" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status = "Rejected" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'" and '+personal_query
                countI = db.smart_query(db.requestchange_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #PENDING
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="p":
                if period.period==1:
                    if personal_query == '':
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(period.yearp)+'-01-01" and requestchange_activity_log.date_request<"'+str(month[2])+'" and requestchange_activity_log.status = "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'"'
                    else:
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(period.yearp)+'-01-01" and requestchange_activity_log.date_request<"'+str(month[2])+'" and requestchange_activity_log.status = "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'" and '+personal_query
                    countP = db.smart_query(db.requestchange_activity_log,search).count()
                    if personal_query == '':
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(period.yearp)+'-01-01" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status != "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'"'
                    else:
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(period.yearp)+'-01-01" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status != "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'" and '+personal_query
                    countNP = db.smart_query(db.requestchange_activity_log,search).count()
                else:
                    if personal_query == '':
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(period.yearp)+'-06-01" and requestchange_activity_log.date_request<"'+str(month[2])+'" and requestchange_activity_log.status = "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'"'
                    else:
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(period.yearp)+'-06-01" and requestchange_activity_log.date_request<"'+str(month[2])+'" and requestchange_activity_log.status = "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'" and '+personal_query
                    countP = db.smart_query(db.requestchange_activity_log,search).count()
                    if personal_query == '':
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(period.yearp)+'-06-01" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status != "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'"'
                    else:
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(period.yearp)+'-06-01" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status != "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'" and '+personal_query
                    countNP = db.smart_query(db.requestchange_activity_log,search).count()
                infoeLevelTemp.append(countP-countNP)
            #INSERT USER
            infoLevel.append(infoeLevelTemp)
    #DATA
    elif str(request.vars['level'])=="5":
        #PERIOD
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Period'))
        infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
        infoLevel.append(infoeLevelTemp)
        #MONTH
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Month'))
        infoeLevelTemp.append(str(month[0]))
        infoLevel.append(infoeLevelTemp)
        #PROJECT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Project'))
        infoeLevelTemp.append(str(project))
        infoLevel.append(infoeLevelTemp)
        #ROL
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Role'))
        infoeLevelTemp.append(T('Rol Student'))
        infoLevel.append(infoeLevelTemp)
        #USER
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('User'))
        infoeLevelTemp.append(str(userP))
        infoLevel.append(infoeLevelTemp)
        #MIDDLE LINE
        infoeLevelTemp=[]
        infoeLevelTemp.append('')
        infoLevel.append(infoeLevelTemp)
        #DETAIL
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Detail'))
        infoLevel.append(infoeLevelTemp)
        #TITLE OF TABLE
        infoeLevelTemp=[]
        infoeLevelTemp.append('Estado')
        infoeLevelTemp.append('Usuario Resolvio')
        infoeLevelTemp.append('Rol Resolvio')
        infoeLevelTemp.append('Descripción')
        infoeLevelTemp.append('Fecha')
        infoeLevelTemp.append('Fecha Resolvio')
        infoeLevelTemp.append('Categoria')
        infoLevel.append(infoeLevelTemp)

        #MADE
        if str(request.vars['type_L'])=="d":
            if personal_query == '':
                search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(month[1])+'" and requestchange_activity_log.date_request<"'+str(month[2])+'" and requestchange_activity_log.status = "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'"'
            else:
                search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(month[1])+'" and requestchange_activity_log.date_request<"'+str(month[2])+'" and requestchange_activity_log.status = "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'" and '+personal_query
            for data in db.smart_query(db.requestchange_activity_log,search).select():
                infoeLevelTemp=[]
                infoeLevelTemp.append(data.status)
                infoeLevelTemp.append(data.user_resolve)
                infoeLevelTemp.append(data.roll_resolve)
                infoeLevelTemp.append(data.description)
                infoeLevelTemp.append(data.date_request)
                infoeLevelTemp.append(data.date_request_resolve)
                infoeLevelTemp.append(data.category_request)
                infoLevel.append(infoeLevelTemp)
                infoeLevelTemp=[]
                infoeLevelTemp.append('')
                infoeLevelTemp.append('')
                infoeLevelTemp.append(T('Operation'))
                infoeLevelTemp.append(T('Name Activity'))
                infoeLevelTemp.append(T('Description of Activity'))
                infoeLevelTemp.append(T('Grade of Activity'))
                infoeLevelTemp.append(T('Start Date'))
                infoeLevelTemp.append(T('End Date'))
                infoLevel.append(infoeLevelTemp)
                for details in db(db.requestchange_course_activity_log.requestchange_activity==data.id).select():
                    infoeLevelTemp=[]
                    infoeLevelTemp.append('')
                    infoeLevelTemp.append('')
                    infoeLevelTemp.append(details.operation_request)
                    infoeLevelTemp.append(details.name)
                    infoeLevelTemp.append(details.description)
                    infoeLevelTemp.append(details.grade)
                    infoeLevelTemp.append(details.date_start)
                    infoeLevelTemp.append(details.date_finish)
                    infoLevel.append(infoeLevelTemp)
                infoeLevelTemp=[]
                infoeLevelTemp.append('')
                infoLevel.append(infoeLevelTemp)
        #ACCEPTED
        elif str(request.vars['type_L'])=="i":
            if personal_query == '':
                search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(month[1])+'" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status = "Accepted" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'"'
            else:
                search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(month[1])+'" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status = "Accepted" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'" and '+personal_query
            for data in db.smart_query(db.requestchange_activity_log,search).select():
                infoeLevelTemp=[]
                infoeLevelTemp.append(data.status)
                infoeLevelTemp.append(data.user_resolve)
                infoeLevelTemp.append(data.roll_resolve)
                infoeLevelTemp.append(data.description)
                infoeLevelTemp.append(data.date_request)
                infoeLevelTemp.append(data.date_request_resolve)
                infoeLevelTemp.append(data.category_request)
                infoLevel.append(infoeLevelTemp)
                infoeLevelTemp=[]
                infoeLevelTemp.append('')
                infoeLevelTemp.append('')
                infoeLevelTemp.append(T('Operation'))
                infoeLevelTemp.append(T('Name Activity'))
                infoeLevelTemp.append(T('Description of Activity'))
                infoeLevelTemp.append(T('Grade of Activity'))
                infoeLevelTemp.append(T('Start Date'))
                infoeLevelTemp.append(T('End Date'))
                infoLevel.append(infoeLevelTemp)
                for details in db(db.requestchange_course_activity_log.requestchange_activity==data.id).select():
                    infoeLevelTemp=[]
                    infoeLevelTemp.append('')
                    infoeLevelTemp.append('')
                    infoeLevelTemp.append(details.operation_request)
                    infoeLevelTemp.append(details.name)
                    infoeLevelTemp.append(details.description)
                    infoeLevelTemp.append(details.grade)
                    infoeLevelTemp.append(details.date_start)
                    infoeLevelTemp.append(details.date_finish)
                    infoLevel.append(infoeLevelTemp)
                infoeLevelTemp=[]
                infoeLevelTemp.append('')
                infoLevel.append(infoeLevelTemp)
        #REJECTED
        elif str(request.vars['type_L'])=="u":
            if personal_query == '':
                search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(month[1])+'" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status = "Rejected" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'"'
            else:
                search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(month[1])+'" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status = "Rejected" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'" and '+personal_query
            for data in db.smart_query(db.requestchange_activity_log,search).select():
                infoeLevelTemp=[]
                infoeLevelTemp.append(data.status)
                infoeLevelTemp.append(data.user_resolve)
                infoeLevelTemp.append(data.roll_resolve)
                infoeLevelTemp.append(data.description)
                infoeLevelTemp.append(data.date_request)
                infoeLevelTemp.append(data.date_request_resolve)
                infoeLevelTemp.append(data.category_request)
                infoLevel.append(infoeLevelTemp)
                infoeLevelTemp=[]
                infoeLevelTemp.append('')
                infoeLevelTemp.append('')
                infoeLevelTemp.append(T('Operation'))
                infoeLevelTemp.append(T('Name Activity'))
                infoeLevelTemp.append(T('Description of Activity'))
                infoeLevelTemp.append(T('Grade of Activity'))
                infoeLevelTemp.append(T('Start Date'))
                infoeLevelTemp.append(T('End Date'))
                infoLevel.append(infoeLevelTemp)
                for details in db(db.requestchange_course_activity_log.requestchange_activity==data.id).select():
                    infoeLevelTemp=[]
                    infoeLevelTemp.append('')
                    infoeLevelTemp.append('')
                    infoeLevelTemp.append(details.operation_request)
                    infoeLevelTemp.append(details.name)
                    infoeLevelTemp.append(details.description)
                    infoeLevelTemp.append(details.grade)
                    infoeLevelTemp.append(details.date_start)
                    infoeLevelTemp.append(details.date_finish)
                    infoLevel.append(infoeLevelTemp)
                infoeLevelTemp=[]
                infoeLevelTemp.append('')
                infoLevel.append(infoeLevelTemp)
        #PENDING
        elif str(request.vars['type_L'])=="p":
            if period.period==1:
                if personal_query == '':
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(period.yearp)+'-01-01" and requestchange_activity_log.date_request<"'+str(month[2])+'" and requestchange_activity_log.status = "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'"'
                else:
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(period.yearp)+'-01-01" and requestchange_activity_log.date_request<"'+str(month[2])+'" and requestchange_activity_log.status = "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'" and '+personal_query
                for pending in  db.smart_query(db.requestchange_activity_log,search).select():
                    if personal_query == '':
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(period.yearp)+'-01-01" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status != "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'" and requestchange_activity_log.description = "'+pending.description+'" and requestchange_activity_log.date_request = "'+str(pending.date_request)+'" and requestchange_activity_log.category_request = "'+pending.category_request+'"'
                    else:
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(period.yearp)+'-01-01" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status != "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'" and requestchange_activity_log.description = "'+pending.description+'" and requestchange_activity_log.date_request = "'+str(pending.date_request)+'" and requestchange_activity_log.category_request = "'+pending.category_request+'" and '+personal_query
                    if db.smart_query(db.requestchange_activity_log,search).select().first() is None:
                        infoeLevelTemp=[]
                        infoeLevelTemp.append(pending.status)
                        infoeLevelTemp.append(pending.user_resolve)
                        infoeLevelTemp.append(pending.roll_resolve)
                        infoeLevelTemp.append(pending.description)
                        infoeLevelTemp.append(pending.date_request)
                        infoeLevelTemp.append(pending.date_request_resolve)
                        infoeLevelTemp.append(pending.category_request)
                        infoLevel.append(infoeLevelTemp)
                        infoeLevelTemp=[]
                        infoeLevelTemp.append('')
                        infoeLevelTemp.append('')
                        infoeLevelTemp.append(T('Operation'))
                        infoeLevelTemp.append(T('Name Activity'))
                        infoeLevelTemp.append(T('Description of Activity'))
                        infoeLevelTemp.append(T('Grade of Activity'))
                        infoeLevelTemp.append(T('Start Date'))
                        infoeLevelTemp.append(T('End Date'))
                        infoLevel.append(infoeLevelTemp)
                        for details in db(db.requestchange_course_activity_log.requestchange_activity==pending.id).select():
                            infoeLevelTemp=[]
                            infoeLevelTemp.append('')
                            infoeLevelTemp.append('')
                            infoeLevelTemp.append(details.operation_request)
                            infoeLevelTemp.append(details.name)
                            infoeLevelTemp.append(details.description)
                            infoeLevelTemp.append(details.grade)
                            infoeLevelTemp.append(details.date_start)
                            infoeLevelTemp.append(details.date_finish)
                            infoLevel.append(infoeLevelTemp)
                        infoeLevelTemp=[]
                        infoeLevelTemp.append('')
                        infoLevel.append(infoeLevelTemp)
            else:
                if personal_query == '':
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(period.yearp)+'-06-01" and requestchange_activity_log.date_request<"'+str(month[2])+'" and requestchange_activity_log.status = "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'"'
                else:
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(period.yearp)+'-06-01" and requestchange_activity_log.date_request<"'+str(month[2])+'" and requestchange_activity_log.status = "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'" and '+personal_query
                for pending in  db.smart_query(db.requestchange_activity_log,search).select():
                    if personal_query == '':
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(period.yearp)+'-06-01" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status != "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'" and requestchange_activity_log.description = "'+pending.description+'" and requestchange_activity_log.date_request = "'+str(pending.date_request)+'" and requestchange_activity_log.category_request = "'+pending.category_request+'"'
                    else:
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(period.yearp)+'-06-01" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status != "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'" and requestchange_activity_log.description = "'+pending.description+'" and requestchange_activity_log.date_request = "'+str(pending.date_request)+'" and requestchange_activity_log.category_request = "'+pending.category_request+'" and '+personal_query
                    if db.smart_query(db.requestchange_activity_log,search).select().first() is None:
                        infoeLevelTemp=[]
                        infoeLevelTemp.append(pending.status)
                        infoeLevelTemp.append(pending.user_resolve)
                        infoeLevelTemp.append(pending.roll_resolve)
                        infoeLevelTemp.append(pending.description)
                        infoeLevelTemp.append(pending.date_request)
                        infoeLevelTemp.append(pending.date_request_resolve)
                        infoeLevelTemp.append(pending.category_request)
                        infoLevel.append(infoeLevelTemp)
                        infoeLevelTemp=[]
                        infoeLevelTemp.append('')
                        infoeLevelTemp.append('')
                        infoeLevelTemp.append(T('Operation'))
                        infoeLevelTemp.append(T('Name Activity'))
                        infoeLevelTemp.append(T('Description of Activity'))
                        infoeLevelTemp.append(T('Grade of Activity'))
                        infoeLevelTemp.append(T('Start Date'))
                        infoeLevelTemp.append(T('End Date'))
                        infoLevel.append(infoeLevelTemp)
                        for details in db(db.requestchange_course_activity_log.requestchange_activity==pending.id).select():
                            infoeLevelTemp=[]
                            infoeLevelTemp.append('')
                            infoeLevelTemp.append('')
                            infoeLevelTemp.append(details.operation_request)
                            infoeLevelTemp.append(details.name)
                            infoeLevelTemp.append(details.description)
                            infoeLevelTemp.append(details.grade)
                            infoeLevelTemp.append(details.date_start)
                            infoeLevelTemp.append(details.date_finish)
                            infoLevel.append(infoeLevelTemp)
                        infoeLevelTemp=[]
                        infoeLevelTemp.append('')
                        infoLevel.append(infoeLevelTemp)
        #ALL
        elif str(request.vars['type_L'])=="all":
            #MADE AND PENDING
            if period.period==1:
                if personal_query == '':
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(period.yearp)+'-01-01" and requestchange_activity_log.date_request<"'+str(month[2])+'" and requestchange_activity_log.status = "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'"'
                else:
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(period.yearp)+'-01-01" and requestchange_activity_log.date_request<"'+str(month[2])+'" and requestchange_activity_log.status = "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'" and '+personal_query
                for pending in  db.smart_query(db.requestchange_activity_log,search).select():
                    if personal_query == '':
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(period.yearp)+'-01-01" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status != "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'" and requestchange_activity_log.description = "'+pending.description+'" and requestchange_activity_log.date_request = "'+str(pending.date_request)+'" and requestchange_activity_log.category_request = "'+pending.category_request+'"'
                    else:
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(period.yearp)+'-01-01" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status != "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'" and requestchange_activity_log.description = "'+pending.description+'" and requestchange_activity_log.date_request = "'+str(pending.date_request)+'" and requestchange_activity_log.category_request = "'+pending.category_request+'" and '+personal_query
                    if db.smart_query(db.requestchange_activity_log,search).select().first() is None:
                        infoeLevelTemp=[]
                        infoeLevelTemp.append(pending.status)
                        infoeLevelTemp.append(pending.user_resolve)
                        infoeLevelTemp.append(pending.roll_resolve)
                        infoeLevelTemp.append(pending.description)
                        infoeLevelTemp.append(pending.date_request)
                        infoeLevelTemp.append(pending.date_request_resolve)
                        infoeLevelTemp.append(pending.category_request)
                        infoLevel.append(infoeLevelTemp)
                        infoeLevelTemp=[]
                        infoeLevelTemp.append('')
                        infoeLevelTemp.append('')
                        infoeLevelTemp.append(T('Operation'))
                        infoeLevelTemp.append(T('Name Activity'))
                        infoeLevelTemp.append(T('Description of Activity'))
                        infoeLevelTemp.append(T('Grade of Activity'))
                        infoeLevelTemp.append(T('Start Date'))
                        infoeLevelTemp.append(T('End Date'))
                        infoLevel.append(infoeLevelTemp)
                        for details in db(db.requestchange_course_activity_log.requestchange_activity==pending.id).select():
                            infoeLevelTemp=[]
                            infoeLevelTemp.append('')
                            infoeLevelTemp.append('')
                            infoeLevelTemp.append(details.operation_request)
                            infoeLevelTemp.append(details.name)
                            infoeLevelTemp.append(details.description)
                            infoeLevelTemp.append(details.grade)
                            infoeLevelTemp.append(details.date_start)
                            infoeLevelTemp.append(details.date_finish)
                            infoLevel.append(infoeLevelTemp)
                        infoeLevelTemp=[]
                        infoeLevelTemp.append('')
                        infoLevel.append(infoeLevelTemp)
            else:
                if personal_query == '':
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(period.yearp)+'-06-01" and requestchange_activity_log.date_request<"'+str(month[2])+'" and requestchange_activity_log.status = "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'"'
                else:
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(period.yearp)+'-06-01" and requestchange_activity_log.date_request<"'+str(month[2])+'" and requestchange_activity_log.status = "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'" and '+personal_query
                for pending in  db.smart_query(db.requestchange_activity_log,search).select():
                    if personal_query == '':
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(period.yearp)+'-06-01" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status != "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'" and requestchange_activity_log.description = "'+pending.description+'" and requestchange_activity_log.date_request = "'+str(pending.date_request)+'" and requestchange_activity_log.category_request = "'+pending.category_request+'"'
                    else:
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(period.yearp)+'-06-01" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status != "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'" and requestchange_activity_log.description = "'+pending.description+'" and requestchange_activity_log.date_request = "'+str(pending.date_request)+'" and requestchange_activity_log.category_request = "'+pending.category_request+'" and '+personal_query
                    if db.smart_query(db.requestchange_activity_log,search).select().first() is None:
                        infoeLevelTemp=[]
                        infoeLevelTemp.append(pending.status)
                        infoeLevelTemp.append(pending.user_resolve)
                        infoeLevelTemp.append(pending.roll_resolve)
                        infoeLevelTemp.append(pending.description)
                        infoeLevelTemp.append(pending.date_request)
                        infoeLevelTemp.append(pending.date_request_resolve)
                        infoeLevelTemp.append(pending.category_request)
                        infoLevel.append(infoeLevelTemp)
                        infoeLevelTemp=[]
                        infoeLevelTemp.append('')
                        infoeLevelTemp.append('')
                        infoeLevelTemp.append(T('Operation'))
                        infoeLevelTemp.append(T('Name Activity'))
                        infoeLevelTemp.append(T('Description of Activity'))
                        infoeLevelTemp.append(T('Grade of Activity'))
                        infoeLevelTemp.append(T('Start Date'))
                        infoeLevelTemp.append(T('End Date'))
                        infoLevel.append(infoeLevelTemp)
                        for details in db(db.requestchange_course_activity_log.requestchange_activity==pending.id).select():
                            infoeLevelTemp=[]
                            infoeLevelTemp.append('')
                            infoeLevelTemp.append('')
                            infoeLevelTemp.append(details.operation_request)
                            infoeLevelTemp.append(details.name)
                            infoeLevelTemp.append(details.description)
                            infoeLevelTemp.append(details.grade)
                            infoeLevelTemp.append(details.date_start)
                            infoeLevelTemp.append(details.date_finish)
                            infoLevel.append(infoeLevelTemp)
                        infoeLevelTemp=[]
                        infoeLevelTemp.append('')
                        infoLevel.append(infoeLevelTemp)
            #ACCEPTED
            if personal_query == '':
                search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(month[1])+'" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status = "Accepted" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'"'
            else:
                search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(month[1])+'" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status = "Accepted" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'" and '+personal_query
            for data in db.smart_query(db.requestchange_activity_log,search).select():
                infoeLevelTemp=[]
                infoeLevelTemp.append(data.status)
                infoeLevelTemp.append(data.user_resolve)
                infoeLevelTemp.append(data.roll_resolve)
                infoeLevelTemp.append(data.description)
                infoeLevelTemp.append(data.date_request)
                infoeLevelTemp.append(data.date_request_resolve)
                infoeLevelTemp.append(data.category_request)
                infoLevel.append(infoeLevelTemp)
                infoeLevelTemp=[]
                infoeLevelTemp.append('')
                infoeLevelTemp.append('')
                infoeLevelTemp.append(T('Operation'))
                infoeLevelTemp.append(T('Name Activity'))
                infoeLevelTemp.append(T('Description of Activity'))
                infoeLevelTemp.append(T('Grade of Activity'))
                infoeLevelTemp.append(T('Start Date'))
                infoeLevelTemp.append(T('End Date'))
                infoLevel.append(infoeLevelTemp)
                for details in db(db.requestchange_course_activity_log.requestchange_activity==data.id).select():
                    infoeLevelTemp=[]
                    infoeLevelTemp.append('')
                    infoeLevelTemp.append('')
                    infoeLevelTemp.append(details.operation_request)
                    infoeLevelTemp.append(details.name)
                    infoeLevelTemp.append(details.description)
                    infoeLevelTemp.append(details.grade)
                    infoeLevelTemp.append(details.date_start)
                    infoeLevelTemp.append(details.date_finish)
                    infoLevel.append(infoeLevelTemp)
                infoeLevelTemp=[]
                infoeLevelTemp.append('')
                infoLevel.append(infoeLevelTemp)
            #REJECTED
            if personal_query == '':
                search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(month[1])+'" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status = "Rejected" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'"'
            else:
                search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(month[1])+'" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status = "Rejected" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'" and '+personal_query
            for data in db.smart_query(db.requestchange_activity_log,search).select():
                infoeLevelTemp=[]
                infoeLevelTemp.append(data.status)
                infoeLevelTemp.append(data.user_resolve)
                infoeLevelTemp.append(data.roll_resolve)
                infoeLevelTemp.append(data.description)
                infoeLevelTemp.append(data.date_request)
                infoeLevelTemp.append(data.date_request_resolve)
                infoeLevelTemp.append(data.category_request)
                infoLevel.append(infoeLevelTemp)
                infoeLevelTemp=[]
                infoeLevelTemp.append('')
                infoeLevelTemp.append('')
                infoeLevelTemp.append(T('Operation'))
                infoeLevelTemp.append(T('Name Activity'))
                infoeLevelTemp.append(T('Description of Activity'))
                infoeLevelTemp.append(T('Grade of Activity'))
                infoeLevelTemp.append(T('Start Date'))
                infoeLevelTemp.append(T('End Date'))
                infoLevel.append(infoeLevelTemp)
                for details in db(db.requestchange_course_activity_log.requestchange_activity==data.id).select():
                    infoeLevelTemp=[]
                    infoeLevelTemp.append('')
                    infoeLevelTemp.append('')
                    infoeLevelTemp.append(details.operation_request)
                    infoeLevelTemp.append(details.name)
                    infoeLevelTemp.append(details.description)
                    infoeLevelTemp.append(details.grade)
                    infoeLevelTemp.append(details.date_start)
                    infoeLevelTemp.append(details.date_finish)
                    infoLevel.append(infoeLevelTemp)
                infoeLevelTemp=[]
                infoeLevelTemp.append('')
                infoLevel.append(infoeLevelTemp)
    #*****************************************************REPORT*****************************************************
    #****************************************************************************************************************
    #****************************************************************************************************************
    return dict(filename='ReporteGestionSolicitudesCambioActividadesConMetrica', csvdata=infoLevel)


@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def crawm_LOAD():
    requestC = None
    requestD = None
    showLevel=False
    try:
        requestC = db(db.requestchange_activity_log.id==int(request.vars['id'])).select().first()
        if requestC is not None:
            showLevel=True
            requestD = db(db.requestchange_course_activity_log.requestchange_activity==int(request.vars['id'])).select()
    except:
        showLevel=False
    return dict(showLevel=showLevel, requestC=requestC, requestD=requestD)


@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def change_request_activities_with_metric_management():
    #****************************************************************************************************************
    #****************************************************************************************************************
    #***************************************CHECK IF THERE IS A PERSONALIZED QUERY***********************************
    personal_query = ''
    makeRedirect = False
    if request.vars['querySearch'] is not None and str(request.vars['querySearch']) != "":
        #PERSONALIZED QUERY SURE WORK
        try:
            personal_query = str(request.vars['querySearch'])
            countI = db.smart_query(db.requestchange_activity_log,personal_query).count()
            if request.vars['searchT'] is not None and str(request.vars['searchT']) == 'T':
                makeRedirect = True
        except:
            response.flash = T('The query is not valid. The report is displayed without applying any query.')
            personal_query = ''
    if makeRedirect == True:
        redirect(URL('management_reports', 'change_request_activities_with_metric_management',vars=dict(level = '5', period = request.vars['period'], month = str(request.vars['month']), project = str(request.vars['project']), userP = str(request.vars['userP']), type_L=request.vars['type_L'], type_U=request.vars['type_U'], querySearch=request.vars['querySearch'])))
    

    #****************************************************************************************************************
    #****************************************************************************************************************
    #******************************************VERIFY THAT ACCURATE PARAMETERS***************************************
    try:
        #CHECK THAT THE LEVEL OF REPORT IS VALID
        if request.vars['level'] is not None and (int(request.vars['level'])<1 or int(request.vars['level'])>5):
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #VERIFY THAT THE PARAMETERS OF EACH LEVEL BE VALID
        if request.vars['level'] is not None:
            #LEVEL MORE THAN 1
            if int(request.vars['level'])>1:
                #CHECK IF THE TYPE OF REPORT IS VALID
                if request.vars['type_L'] is None or (str(request.vars['type_L'])!="all" and str(request.vars['type_L'])!="i" and str(request.vars['type_L'])!="u" and str(request.vars['type_L'])!="d" and str(request.vars['type_L'])!="p"):
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))

                period = VALIDATE_PERIOD(request.vars['period'])
                if period is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))
            
            #LEVEL MORE THAN 2
            if int(request.vars['level'])>2:
                #CHECK IF THE TYPE OF REPORT IS VALID
                if request.vars['type_U'] is None or (str(request.vars['type_U'])!="all" and str(request.vars['type_U'])!="i" and str(request.vars['type_U'])!="u" and str(request.vars['type_U'])!="d" and str(request.vars['type_L'])!="p"):
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))

                #CHECK IF THE MONTH IS VALID
                month = VALIDATE_MONTH(request.vars['month'],period)
                if month is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))
            
            #LEVEL MORE THAN 3
            if int(request.vars['level'])>3:
                #CHECK IF THE PROJECT IS VALID
                project = VALIDATE_PROJECT(request.vars['project'],'requestchange_activity_log')
                if project is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))

            #LEVEL MORE THAN 4
            if int(request.vars['level'])>4:
                #CHECK IF THE USER IS VALID
                userP = VALIDATE_USER(period,project,'Student',request.vars['userP'],'requestchange_activity_log')
                if userP is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))
    except:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))

    
    #****************************************************************************************************************
    #****************************************************************************************************************
    #**************************************************SEARCH REPORT*************************************************
    def filtered_by(flag):
        fsearch_Option=[]
        fsearch_Option.append('=')
        fsearch_Option.append('!=')
        fsearch_Option.append('<')
        fsearch_Option.append('>')
        fsearch_Option.append('<=')
        fsearch_Option.append('>=')
        if flag==True:
            fsearch_Option.append('starts with')
            fsearch_Option.append('contains')
            fsearch_Option.append('in')
            fsearch_Option.append('not in')
        return fsearch_Option


    fsearch = []
    #******************************COMBOS INFORMATION******************************
    #YEARS
    if request.vars['level']=='1' or request.vars['level'] is None:
        groupYears = GET_YEARS()
        if len(groupYears) != 0:
            fsearch.append(['yearp','Año',False,[3,sorted(groupYears)]])
    #PROJECTS
    if request.vars['level'] is None or int(request.vars['level'])<=3:
        projects = GET_PROJECTS('requestchange_activity_log')
        if len(projects) != 0:
            fsearch_Values=[]
            fsearch_Values.append(2)
            for projectT in projects:
                project=db(db.project.name==projectT).select().first()
                if project is None:
                    project=db(db.requestchange_activity_log.project==projectT).select().first()
                    project=project.project
                else:
                    project=project.name
                fsearch_Values.append(project)
            fsearch.append(['course','Curso',False,fsearch_Values])
    #OPERATION LOG
    fsearch.append(['status','Estado',False,[3,['Accepted','Rejected','Pending']]])
    #CATEGORIES
    groupCategories = GET_CATEGORIES('requestchange_activity_log')
    if len(groupCategories) != 0:
        fsearch.append(['category_request','Categoria',False,[3,sorted(groupCategories)]])
    #DATES
    dates = GET_DATES('requestchange_activity_log')
    if len(dates) != 0:
        fsearch.append(['date_request','Fecha',False,[3,sorted(dates)]])
    #******************************ENTERING USER******************************
    #USER REQUEST
    if request.vars['level'] is None or int(request.vars['level'])<=4:
        fsearch.append(['user_request','Usuario Solicitud',False,[1]])
    fsearch.append(['description','Descripción',True,[1]])



    #****************************************************************************************************************
    #****************************************************************************************************************
    #*****************************************************REPORT*****************************************************
    #LEVELS OF REPORT
    from datetime import datetime
    infoLevel = []
    grid = []
    #ALL SEMESTERS
    if request.vars['level']=='1' or request.vars['level'] is None:
        groupPeriods = db(db.period_year).select(orderby=~db.period_year.id)
        if len(groupPeriods) == 0:
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('default','index'))
        for period in groupPeriods:
            infoeLevelTemp = []
            #ID OF PERIOD
            infoeLevelTemp.append(period.id)
            #NAME OF PERIOD
            infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
            #MADE
            if personal_query == '':
                search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.status = "Pending"'
            else:
                search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.status = "Pending" and '+personal_query
            countI = db.smart_query(db.requestchange_activity_log,search).count()
            infoeLevelTemp.append(countI)
            #ACCEPTED
            if personal_query == '':
                search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.status = "Accepted"'
            else:
                search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.status = "Accepted" and '+personal_query
            countI = db.smart_query(db.requestchange_activity_log,search).count()
            infoeLevelTemp.append(countI)
            #REJECTED
            if personal_query == '':
                search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.status = "Rejected"'
            else:
                search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.status = "Rejected" and '+personal_query
            countI = db.smart_query(db.requestchange_activity_log,search).count()
            infoeLevelTemp.append(countI)
            #PENDING
            infoeLevelTemp.append(infoeLevelTemp[2]-infoeLevelTemp[3]-infoeLevelTemp[4])
            #INSERT PERIOD
            infoLevel.append(infoeLevelTemp)
    #PER MONTH
    elif str(request.vars['level'])=="2":
        for month in GET_MONTH_PERIOD(period):
            start = datetime.strptime(str(period.yearp) + '-' + str(month[0]) +'-01', "%Y-%m-%d")
            if month[2]==1:
                end = datetime.strptime(str(period.yearp+1) + '-' + str(month[2]) +'-01', "%Y-%m-%d")
            else:
                end = datetime.strptime(str(period.yearp) + '-' + str(month[2]) +'-01', "%Y-%m-%d")
            infoeLevelTemp = []
            #NAME OF PERIOD
            infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
            #ID OF MONTH
            infoeLevelTemp.append(month[0])
            #NAME OF MONTH
            infoeLevelTemp.append(month[1]+' '+str(period.yearp))
            #MADE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(start)+'" and requestchange_activity_log.date_request<"'+str(end)+'" and requestchange_activity_log.status = "Pending"'
                else:
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(start)+'" and requestchange_activity_log.date_request<"'+str(end)+'" and requestchange_activity_log.status = "Pending" and '+personal_query
                countI = db.smart_query(db.requestchange_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #ACCEPTED
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                if personal_query == '':
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(start)+'" and requestchange_activity_log.date_request_resolve<"'+str(end)+'" and requestchange_activity_log.status = "Accepted"'
                else:
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(start)+'" and requestchange_activity_log.date_request_resolve<"'+str(end)+'" and requestchange_activity_log.status = "Accepted" and '+personal_query
                countI = db.smart_query(db.requestchange_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #REJECTED
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(start)+'" and requestchange_activity_log.date_request_resolve<"'+str(end)+'" and requestchange_activity_log.status = "Rejected"'
                else:
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(start)+'" and requestchange_activity_log.date_request_resolve<"'+str(end)+'" and requestchange_activity_log.status = "Rejected" and '+personal_query
                countI = db.smart_query(db.requestchange_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #PENDING
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="p":
                if period.period==1:
                    if personal_query == '':
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(period.yearp)+'-01-01" and requestchange_activity_log.date_request<"'+str(end)+'" and requestchange_activity_log.status = "Pending"'
                    else:
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(period.yearp)+'-01-01" and requestchange_activity_log.date_request<"'+str(end)+'" and requestchange_activity_log.status = "Pending" and '+personal_query
                    countP = db.smart_query(db.requestchange_activity_log,search).count()
                    if personal_query == '':
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(period.yearp)+'-01-01" and requestchange_activity_log.date_request_resolve<"'+str(end)+'" and requestchange_activity_log.status != "Pending"'
                    else:
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(period.yearp)+'-01-01" and requestchange_activity_log.date_request_resolve<"'+str(end)+'" and requestchange_activity_log.status != "Pending" and '+personal_query
                    countNP = db.smart_query(db.requestchange_activity_log,search).count()
                else:
                    if personal_query == '':
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(period.yearp)+'-06-01" and requestchange_activity_log.date_request<"'+str(end)+'" and requestchange_activity_log.status = "Pending"'
                    else:
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(period.yearp)+'-06-01" and requestchange_activity_log.date_request<"'+str(end)+'" and requestchange_activity_log.status = "Pending" and '+personal_query
                    countP = db.smart_query(db.requestchange_activity_log,search).count()
                    if personal_query == '':
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(period.yearp)+'-06-01" and requestchange_activity_log.date_request_resolve<"'+str(end)+'" and requestchange_activity_log.status != "Pending"'
                    else:
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(period.yearp)+'-06-01" and requestchange_activity_log.date_request_resolve<"'+str(end)+'" and requestchange_activity_log.status != "Pending" and '+personal_query
                    countNP = db.smart_query(db.requestchange_activity_log,search).count()
                infoeLevelTemp.append(countP-countNP)
            #INSERT MONTH
            infoLevel.append(infoeLevelTemp)
    #PER PROJECT
    elif str(request.vars['level'])=="3":
        if len(projects) == 0:
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('management_reports', 'change_request_activities_with_metric_management',vars=dict(level='2',period = str(request.vars['period']), type_L = str(request.vars['type_U']), querySearch=personal_query)))

        for projectT in projects:
            project=db(db.project.name==projectT).select().first()
            if project is None:
                project=db((db.course_activity_log.before_course==projectT)|(db.course_activity_log.after_course==projectT)).select().first()
                if project.before_course is not None:
                    project=project.before_course
                else:
                    project=project.after_course
            else:
                project=project.name
            infoeLevelTemp = []
            #NAME OF PERIOD
            infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
            #NAME OF MONTH
            infoeLevelTemp.append(month[0])
            #ID OF PROJECT
            infoeLevelTemp.append(project)
            #NAME OF PROJECT
            infoeLevelTemp.append(project)
            #MADE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(month[1])+'" and requestchange_activity_log.date_request<"'+str(month[2])+'" and requestchange_activity_log.status = "Pending" and requestchange_activity_log.course = "'+str(project)+'"'
                else:
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(month[1])+'" and requestchange_activity_log.date_request<"'+str(month[2])+'" and requestchange_activity_log.status = "Pending" and requestchange_activity_log.course = "'+str(project)+'" and '+personal_query
                countI = db.smart_query(db.requestchange_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #ACCEPTED
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                if personal_query == '':
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(month[1])+'" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status = "Accepted" and requestchange_activity_log.course = "'+str(project)+'"'
                else:
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(month[1])+'" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status = "Accepted" and requestchange_activity_log.course = "'+str(project)+'" and '+personal_query
                countI = db.smart_query(db.requestchange_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #REJECTED
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(month[1])+'" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status = "Rejected" and requestchange_activity_log.course = "'+str(project)+'"'
                else:
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(month[1])+'" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status = "Rejected" and requestchange_activity_log.course = "'+str(project)+'" and '+personal_query
                countI = db.smart_query(db.requestchange_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #PENDING
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="p":
                if period.period==1:
                    if personal_query == '':
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(period.yearp)+'-01-01" and requestchange_activity_log.date_request<"'+str(month[2])+'" and requestchange_activity_log.status = "Pending" and requestchange_activity_log.course = "'+str(project)+'"'
                    else:
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(period.yearp)+'-01-01" and requestchange_activity_log.date_request<"'+str(month[2])+'" and requestchange_activity_log.status = "Pending" and requestchange_activity_log.course = "'+str(project)+'" and '+personal_query
                    countP = db.smart_query(db.requestchange_activity_log,search).count()
                    if personal_query == '':
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(period.yearp)+'-01-01" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status != "Pending" and requestchange_activity_log.course = "'+str(project)+'"'
                    else:
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(period.yearp)+'-01-01" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status != "Pending" and requestchange_activity_log.course = "'+str(project)+'" and '+personal_query
                    countNP = db.smart_query(db.requestchange_activity_log,search).count()
                else:
                    if personal_query == '':
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(period.yearp)+'-06-01" and requestchange_activity_log.date_request<"'+str(month[2])+'" and requestchange_activity_log.status = "Pending" and requestchange_activity_log.course = "'+str(project)+'"'
                    else:
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(period.yearp)+'-06-01" and requestchange_activity_log.date_request<"'+str(month[2])+'" and requestchange_activity_log.status = "Pending" and requestchange_activity_log.course = "'+str(project)+'" and '+personal_query
                    countP = db.smart_query(db.requestchange_activity_log,search).count()
                    if personal_query == '':
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(period.yearp)+'-06-01" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status != "Pending" and requestchange_activity_log.course = "'+str(project)+'"'
                    else:
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(period.yearp)+'-06-01" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status != "Pending" and requestchange_activity_log.course = "'+str(project)+'" and '+personal_query
                    countNP = db.smart_query(db.requestchange_activity_log,search).count()
                infoeLevelTemp.append(countP-countNP)
            #INSERT PROJECT
            infoLevel.append(infoeLevelTemp)
    #PER USER
    elif str(request.vars['level'])=="4":
        #VERIFY THAT CAN SHOW THE LEVEL OF THE REPORT
        usersProject = GET_USERS(period,project,'Student','requestchange_activity_log')
        if len(usersProject) == 0:
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('management_reports', 'change_request_activities_with_metric_management',vars=dict(level='3', period = str(request.vars['period']), month = str(request.vars['month']), type_L = str(request.vars['type_U']), type_U = str(request.vars['type_U']), querySearch=personal_query)))

        for userPT in usersProject:
            userP=db(db.auth_user.username==userPT).select().first()
            if userP is None:
                userP=db(db.requestchange_activity_log.user_request==userPT).select().first()
                userP=userP.user_request
            else:
                userP=userP.username
            infoeLevelTemp = []
            #NAME OF PERIOD
            infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
            #NAME OF MONTH
            infoeLevelTemp.append(month[0])
            #NAME OF PROJECT
            infoeLevelTemp.append(project)
            #ID OF USER
            infoeLevelTemp.append(userP)
            #NAME OF USER
            infoeLevelTemp.append(userP)
            #MADE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                countI = 0
                if personal_query == '':
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(month[1])+'" and requestchange_activity_log.date_request<"'+str(month[2])+'" and requestchange_activity_log.status = "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'"'
                else:
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(month[1])+'" and requestchange_activity_log.date_request<"'+str(month[2])+'" and requestchange_activity_log.status = "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'" and '+personal_query
                countI = db.smart_query(db.requestchange_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #ACCEPTED
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                if personal_query == '':
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(month[1])+'" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status = "Accepted" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'"'
                else:
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(month[1])+'" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status = "Accepted" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'" and '+personal_query
                countI = db.smart_query(db.requestchange_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #REJECTED
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(month[1])+'" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status = "Rejected" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'"'
                else:
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(month[1])+'" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status = "Rejected" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'" and '+personal_query
                countI = db.smart_query(db.requestchange_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #PENDING
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="p":
                if period.period==1:
                    if personal_query == '':
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(period.yearp)+'-01-01" and requestchange_activity_log.date_request<"'+str(month[2])+'" and requestchange_activity_log.status = "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'"'
                    else:
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(period.yearp)+'-01-01" and requestchange_activity_log.date_request<"'+str(month[2])+'" and requestchange_activity_log.status = "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'" and '+personal_query
                    countP = db.smart_query(db.requestchange_activity_log,search).count()
                    if personal_query == '':
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(period.yearp)+'-01-01" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status != "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'"'
                    else:
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(period.yearp)+'-01-01" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status != "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'" and '+personal_query
                    countNP = db.smart_query(db.requestchange_activity_log,search).count()
                else:
                    if personal_query == '':
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(period.yearp)+'-06-01" and requestchange_activity_log.date_request<"'+str(month[2])+'" and requestchange_activity_log.status = "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'"'
                    else:
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(period.yearp)+'-06-01" and requestchange_activity_log.date_request<"'+str(month[2])+'" and requestchange_activity_log.status = "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'" and '+personal_query
                    countP = db.smart_query(db.requestchange_activity_log,search).count()
                    if personal_query == '':
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(period.yearp)+'-06-01" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status != "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'"'
                    else:
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(period.yearp)+'-06-01" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status != "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'" and '+personal_query
                    countNP = db.smart_query(db.requestchange_activity_log,search).count()
                infoeLevelTemp.append(countP-countNP)
            #INSERT USER
            infoLevel.append(infoeLevelTemp)
    #DATA
    elif str(request.vars['level'])=="5":
        #MADE
        if str(request.vars['type_L'])=="d":
            if personal_query == '':
                search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(month[1])+'" and requestchange_activity_log.date_request<"'+str(month[2])+'" and requestchange_activity_log.status = "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'"'
            else:
                search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(month[1])+'" and requestchange_activity_log.date_request<"'+str(month[2])+'" and requestchange_activity_log.status = "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'" and '+personal_query
            for data in db.smart_query(db.requestchange_activity_log,search).select():
                grid.append(data.id)
        #ACCEPTED
        elif str(request.vars['type_L'])=="i":
            if personal_query == '':
                search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(month[1])+'" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status = "Accepted" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'"'
            else:
                search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(month[1])+'" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status = "Accepted" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'" and '+personal_query
            for data in db.smart_query(db.requestchange_activity_log,search).select():
                grid.append(data.id)
        #REJECTED
        elif str(request.vars['type_L'])=="u":
            if personal_query == '':
                search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(month[1])+'" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status = "Rejected" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'"'
            else:
                search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(month[1])+'" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status = "Rejected" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'" and '+personal_query
            for data in db.smart_query(db.requestchange_activity_log,search).select():
                grid.append(data.id)
        #PENDING
        elif str(request.vars['type_L'])=="p":
            if period.period==1:
                if personal_query == '':
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(period.yearp)+'-01-01" and requestchange_activity_log.date_request<"'+str(month[2])+'" and requestchange_activity_log.status = "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'"'
                else:
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(period.yearp)+'-01-01" and requestchange_activity_log.date_request<"'+str(month[2])+'" and requestchange_activity_log.status = "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'" and '+personal_query
                for pending in  db.smart_query(db.requestchange_activity_log,search).select():
                    if personal_query == '':
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(period.yearp)+'-01-01" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status != "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'" and requestchange_activity_log.description = "'+pending.description+'" and requestchange_activity_log.date_request = "'+str(pending.date_request)+'" and requestchange_activity_log.category_request = "'+pending.category_request+'"'
                    else:
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(period.yearp)+'-01-01" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status != "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'" and requestchange_activity_log.description = "'+pending.description+'" and requestchange_activity_log.date_request = "'+str(pending.date_request)+'" and requestchange_activity_log.category_request = "'+pending.category_request+'" and '+personal_query
                    if db.smart_query(db.requestchange_activity_log,search).select().first() is None:
                        grid.append(pending.id)
            else:
                if personal_query == '':
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(period.yearp)+'-06-01" and requestchange_activity_log.date_request<"'+str(month[2])+'" and requestchange_activity_log.status = "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'"'
                else:
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(period.yearp)+'-06-01" and requestchange_activity_log.date_request<"'+str(month[2])+'" and requestchange_activity_log.status = "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'" and '+personal_query
                for pending in  db.smart_query(db.requestchange_activity_log,search).select():
                    if personal_query == '':
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(period.yearp)+'-06-01" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status != "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'" and requestchange_activity_log.description = "'+pending.description+'" and requestchange_activity_log.date_request = "'+str(pending.date_request)+'" and requestchange_activity_log.category_request = "'+pending.category_request+'"'
                    else:
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(period.yearp)+'-06-01" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status != "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'" and requestchange_activity_log.description = "'+pending.description+'" and requestchange_activity_log.date_request = "'+str(pending.date_request)+'" and requestchange_activity_log.category_request = "'+pending.category_request+'" and '+personal_query
                    if db.smart_query(db.requestchange_activity_log,search).select().first() is None:
                        grid.append(pending.id)
        #ALL
        elif str(request.vars['type_L'])=="all":
            #MADE AND PENDING
            if period.period==1:
                if personal_query == '':
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(period.yearp)+'-01-01" and requestchange_activity_log.date_request<"'+str(month[2])+'" and requestchange_activity_log.status = "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'"'
                else:
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(period.yearp)+'-01-01" and requestchange_activity_log.date_request<"'+str(month[2])+'" and requestchange_activity_log.status = "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'" and '+personal_query
                for pending in  db.smart_query(db.requestchange_activity_log,search).select():
                    if personal_query == '':
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(period.yearp)+'-01-01" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status != "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'" and requestchange_activity_log.description = "'+pending.description+'" and requestchange_activity_log.date_request = "'+str(pending.date_request)+'" and requestchange_activity_log.category_request = "'+pending.category_request+'"'
                    else:
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(period.yearp)+'-01-01" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status != "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'" and requestchange_activity_log.description = "'+pending.description+'" and requestchange_activity_log.date_request = "'+str(pending.date_request)+'" and requestchange_activity_log.category_request = "'+pending.category_request+'" and '+personal_query
                    if db.smart_query(db.requestchange_activity_log,search).select().first() is None:
                        grid.append(pending.id)
            else:
                if personal_query == '':
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(period.yearp)+'-06-01" and requestchange_activity_log.date_request<"'+str(month[2])+'" and requestchange_activity_log.status = "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'"'
                else:
                    search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request >="'+str(period.yearp)+'-06-01" and requestchange_activity_log.date_request<"'+str(month[2])+'" and requestchange_activity_log.status = "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'" and '+personal_query
                for pending in  db.smart_query(db.requestchange_activity_log,search).select():
                    if personal_query == '':
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(period.yearp)+'-06-01" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status != "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'" and requestchange_activity_log.description = "'+pending.description+'" and requestchange_activity_log.date_request = "'+str(pending.date_request)+'" and requestchange_activity_log.category_request = "'+pending.category_request+'"'
                    else:
                        search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(period.yearp)+'-06-01" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status != "Pending" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'" and requestchange_activity_log.description = "'+pending.description+'" and requestchange_activity_log.date_request = "'+str(pending.date_request)+'" and requestchange_activity_log.category_request = "'+pending.category_request+'" and '+personal_query
                    if db.smart_query(db.requestchange_activity_log,search).select().first() is None:
                        grid.append(pending.id)
            #ACCEPTED
            if personal_query == '':
                search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(month[1])+'" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status = "Accepted" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'"'
            else:
                search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(month[1])+'" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status = "Accepted" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'" and '+personal_query
            for data in db.smart_query(db.requestchange_activity_log,search).select():
                grid.append(data.id)
            #REJECTED
            if personal_query == '':
                search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(month[1])+'" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status = "Rejected" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'"'
            else:
                search='requestchange_activity_log.semester = "'+period.period.name+'" and requestchange_activity_log.yearp = "'+str(period.yearp)+'" and requestchange_activity_log.date_request_resolve >="'+str(month[1])+'" and requestchange_activity_log.date_request_resolve<"'+str(month[2])+'" and requestchange_activity_log.status = "Rejected" and requestchange_activity_log.course = "'+str(project)+'" and requestchange_activity_log.roll_request = "Student" and requestchange_activity_log.user_request = "'+str(userP)+'" and '+personal_query
            for data in db.smart_query(db.requestchange_activity_log,search).select():
                grid.append(data.id)

        #TITLE
        infoeLevelTemp=[]
        infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
        infoeLevelTemp.append(str(month[0]))
        infoeLevelTemp.append(project)
        infoeLevelTemp.append(T('Rol Student'))
        infoeLevelTemp.append(str(userP))
        infoLevel.append(infoeLevelTemp)
        #REPORT
        if len(grid) == 0:
            grid.append(-1)
        db.requestchange_activity_log.id.readable = False
        db.requestchange_activity_log.id.writable = False
        db.requestchange_activity_log.user_request.readable = False
        db.requestchange_activity_log.user_request.writable = False
        db.requestchange_activity_log.roll_request.readable = False
        db.requestchange_activity_log.roll_request.writable = False
        db.requestchange_activity_log.semester.readable = False
        db.requestchange_activity_log.semester.writable = False
        db.requestchange_activity_log.yearp.readable = False
        db.requestchange_activity_log.yearp.writable = False
        db.requestchange_activity_log.course.readable = False
        db.requestchange_activity_log.course.writable = False
        links = [lambda row: A(T('Detail'),
        _role='button', 
        _class= 'btn btn-info', 
        _onclick='set_values("'+str(row.id)+'");', 
        _title=T('View Detail') ,**{"_data-toggle":"modal", "_data-target": "#detailModal"})]
        grid = SQLFORM.grid(db.requestchange_activity_log.id.belongs(grid), links=links, csv=False, create=False, editable=False, deletable=False, details=False, paginate=9, searchable=False)
    return dict(fsearch=fsearch, filtered_by=filtered_by, personal_query=personal_query, infoLevel=infoLevel, grid=grid)


#*************************************************************************************************************************************
#*************************************************************************************************************************************
#**************************************************MANAGEMENT REPORT CHANGE REQUEST GRADES********************************************
@auth.requires_login()
@auth.requires(auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
def change_request_grades_management_export():
    #VERIFI THAT ACCURATE PARAMETERS
    try:
        #CHECK IF THE TYPE OF EXPORT IS VALID
        if request.vars['list_type'] is None or str(request.vars['list_type'])!="csv":
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #CHECK THAT THE LEVEL OF REPORT IS VALID
        if request.vars['level'] is not None and (int(request.vars['level'])<1 or int(request.vars['level'])>5):
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('default','index'))

        #VERIFY THAT THE PARAMETERS OF EACH LEVEL BE VALID
        if request.vars['level'] is not None:
            #LEVEL MORE THAN 1
            if int(request.vars['level'])>1:
                #CHECK IF THE TYPE OF REPORT IS VALID
                if request.vars['type_L'] is None or (str(request.vars['type_L'])!="all" and str(request.vars['type_L'])!="i" and str(request.vars['type_L'])!="u" and str(request.vars['type_L'])!="d" and str(request.vars['type_L'])!="p" and str(request.vars['type_L'])!="c"):
                    session.flash = T('Report no visible: There are no parameters required to display the report.')
                    redirect(URL('default','index'))

                period = VALIDATE_PERIOD(request.vars['period'])
                if period is None:
                    session.flash = T('Report no visible: There are no parameters required to display the report.')
                    redirect(URL('default','index'))
            
            #LEVEL MORE THAN 2
            if int(request.vars['level'])>2:
                #CHECK IF THE TYPE OF REPORT IS VALID
                if request.vars['type_U'] is None or (str(request.vars['type_U'])!="all" and str(request.vars['type_U'])!="i" and str(request.vars['type_U'])!="u" and str(request.vars['type_U'])!="d" and str(request.vars['type_L'])!="p" and str(request.vars['type_L'])!="c"):
                    session.flash = T('Report no visible: There are no parameters required to display the report.')
                    redirect(URL('default','index'))

                #CHECK IF THE MONTH IS VALID
                month = VALIDATE_MONTH(request.vars['month'],period)
                if month is None:
                    session.flash = T('Report no visible: There are no parameters required to display the report.')
                    redirect(URL('default','index'))
            
            #LEVEL MORE THAN 3
            if int(request.vars['level'])>3:
                #CHECK IF THE PROJECT IS VALID
                project = VALIDATE_PROJECT(request.vars['project'],'request_change_g_log')
                if project is None:
                    session.flash = T('Report no visible: There are no parameters required to display the report.')
                    redirect(URL('default','index'))

            #LEVEL MORE THAN 4
            if int(request.vars['level'])>4:
                #CHECK IF THE USER IS VALID
                userP = VALIDATE_USER(period,project,'Student',request.vars['userP'],'request_change_g_log')
                if userP is None:
                    session.flash = T('Report no visible: There are no parameters required to display the report.')
                    redirect(URL('default','index'))
    except:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))

    #CHECK IF THERE IS A PERSONALIZED QUERY
    personal_query = ''
    if request.vars['querySearch'] is not None and str(request.vars['querySearch']) != "":
        #PERSONALIZED QUERY SURE WORK
        try:
            personal_query = str(request.vars['querySearch'])
            countI = db.smart_query(db.request_change_g_log,personal_query).count()
        except:
            personal_query = ''

    #****************************************************************************************************************
    #****************************************************************************************************************
    #*****************************************************REPORT*****************************************************
    from datetime import datetime
    #TITLE
    infoLevel = []
    infoeLevelTemp=[]
    infoeLevelTemp.append('Universidad de San Carlos de Guatemala')
    infoLevel.append(infoeLevelTemp)
    infoeLevelTemp=[]
    infoeLevelTemp.append('Facultad de Ingeniería')
    infoLevel.append(infoeLevelTemp)
    infoeLevelTemp=[]
    infoeLevelTemp.append('Escuela de Ciencias y Sistemas')
    infoLevel.append(infoeLevelTemp)
    #TYPE OF REPORT
    infoeLevelTemp=[]
    infoeLevelTemp.append(T('Type'))
    infoeLevelTemp.append(T('Change Request Management Grades'))
    infoLevel.append(infoeLevelTemp)
    #DESCRIPTION OF REPORT
    infoeLevelTemp=[]
    infoeLevelTemp.append(T('Description'))
    infoeLevelTemp.append(T('Report of operations for managing change requests grades'))
    infoLevel.append(infoeLevelTemp)
    #LEVELS OF REPORT
    #ALL SEMESTERS
    if request.vars['level'] is None or str(request.vars['level'])=="1":
        #MIDDLE LINE OF REPORT
        infoeLevelTemp=[]
        infoLevel.append(infoeLevelTemp)
        #LABLE DETAIL OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Detail'))
        infoLevel.append(infoeLevelTemp)
        #LABELS OF DATA OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Period'))
        infoeLevelTemp.append(T('Total Made Requests'))
        infoeLevelTemp.append(T('Total Accepted request'))
        infoeLevelTemp.append(T('Total Rejected request'))
        infoeLevelTemp.append(T('Total Canceled request'))
        infoeLevelTemp.append(T('Total Pending Requests'))
        infoLevel.append(infoeLevelTemp)
        for period in groupPeriods:
            infoeLevelTemp = []
            #NAME OF PERIOD
            infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
            #MADE
            if personal_query == '':
                search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.after_status = "pending"'
            else:
                search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.after_status = "pending" and '+personal_query
            countI = db.smart_query(db.request_change_g_log,search).count()
            infoeLevelTemp.append(countI)
            #ACCEPTED
            if personal_query == '':
                search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.after_status = "accepted"'
            else:
                search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.after_status = "accepted" and '+personal_query
            countI = db.smart_query(db.request_change_g_log,search).count()
            infoeLevelTemp.append(countI)
            #REJECTED
            if personal_query == '':
                search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.after_status = "rejected"'
            else:
                search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.after_status = "rejected" and '+personal_query
            countI = db.smart_query(db.request_change_g_log,search).count()
            infoeLevelTemp.append(countI)
            #CANCELED
            if personal_query == '':
                search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.after_status = "canceled"'
            else:
                search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.after_status = "canceled" and '+personal_query
            countI = db.smart_query(db.request_change_g_log,search).count()
            infoeLevelTemp.append(countI)
            #PENDING
            infoeLevelTemp.append(infoeLevelTemp[2]-infoeLevelTemp[3]-infoeLevelTemp[4]-infoeLevelTemp[5])
            #INSERT PERIOD
            infoLevel.append(infoeLevelTemp)
    #PER MONTH
    elif str(request.vars['level'])=="2":
        #PERIOD OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Period'))
        infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
        infoLevel.append(infoeLevelTemp)
        #MIDDLE LINE OF REPORT
        infoeLevelTemp=[]
        infoLevel.append(infoeLevelTemp)
        #LABLE DETAIL OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Detail'))
        infoLevel.append(infoeLevelTemp)
        #LABELS OF DATA OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Month'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
            infoeLevelTemp.append(T('Total Made Requests'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
            infoeLevelTemp.append(T('Total Accepted request'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
            infoeLevelTemp.append(T('Total Rejected request'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="c":
            infoeLevelTemp.append(T('Total Canceled request'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="p":
            infoeLevelTemp.append(T('Total Pending Requests'))
        infoLevel.append(infoeLevelTemp)

        for month in GET_MONTH_PERIOD(period):
            start = datetime.strptime(str(period.yearp) + '-' + str(month[0]) +'-01', "%Y-%m-%d")
            if month[2]==1:
                end = datetime.strptime(str(period.yearp+1) + '-' + str(month[2]) +'-01', "%Y-%m-%d")
            else:
                end = datetime.strptime(str(period.yearp) + '-' + str(month[2]) +'-01', "%Y-%m-%d")
            infoeLevelTemp = []
            #NAME OF MONTH
            infoeLevelTemp.append(month[1]+' '+str(period.yearp))
            #MADE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(start)+'" and request_change_g_log.date_request<"'+str(end)+'" and request_change_g_log.after_status = "pending"'
                else:
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(start)+'" and request_change_g_log.date_request<"'+str(end)+'" and request_change_g_log.after_status = "pending" and '+personal_query
                countI = db.smart_query(db.request_change_g_log,search).count()
                infoeLevelTemp.append(countI)
            #ACCEPTED
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                if personal_query == '':
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(start)+'" and request_change_g_log.date_operation<"'+str(end)+'" and request_change_g_log.after_status = "accepted"'
                else:
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(start)+'" and request_change_g_log.date_operation<"'+str(end)+'" and request_change_g_log.after_status = "accepted" and '+personal_query
                countI = db.smart_query(db.request_change_g_log,search).count()
                infoeLevelTemp.append(countI)
            #REJECTED
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(start)+'" and request_change_g_log.date_operation<"'+str(end)+'" and request_change_g_log.after_status = "rejected"'
                else:
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(start)+'" and request_change_g_log.date_operation<"'+str(end)+'" and request_change_g_log.after_status = "rejected" and '+personal_query
                countI = db.smart_query(db.request_change_g_log,search).count()
                infoeLevelTemp.append(countI)
            ##CANCELED
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="c":
                if personal_query == '':
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(start)+'" and request_change_g_log.date_operation<"'+str(end)+'" and request_change_g_log.after_status = "canceled"'
                else:
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(start)+'" and request_change_g_log.date_operation<"'+str(end)+'" and request_change_g_log.after_status = "canceled" and '+personal_query
                countI = db.smart_query(db.request_change_g_log,search).count()
                infoeLevelTemp.append(countI)
            #PENDING
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="p":
                if period.period==1:
                    if personal_query == '':
                        search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(period.yearp)+'-01-01" and request_change_g_log.date_request<"'+str(end)+'" and request_change_g_log.after_status = "pending"'
                    else:
                        search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(period.yearp)+'-01-01" and request_change_g_log.date_request<"'+str(end)+'" and request_change_g_log.after_status = "pending" and '+personal_query
                    countP = db.smart_query(db.request_change_g_log,search).count()
                    if personal_query == '':
                        search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(period.yearp)+'-01-01" and request_change_g_log.date_operation<"'+str(end)+'" and request_change_g_log.after_status != "pending"'
                    else:
                        search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(period.yearp)+'-01-01" and request_change_g_log.date_operation<"'+str(end)+'" and request_change_g_log.after_status != "pending" and '+personal_query
                    countNP = db.smart_query(db.request_change_g_log,search).count()
                else:
                    if personal_query == '':
                        search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(period.yearp)+'-06-01" and request_change_g_log.date_request<"'+str(end)+'" and request_change_g_log.after_status = "pending"'
                    else:
                        search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(period.yearp)+'-06-01" and request_change_g_log.date_request<"'+str(end)+'" and request_change_g_log.after_status = "pending" and '+personal_query
                    countP = db.smart_query(db.request_change_g_log,search).count()
                    if personal_query == '':
                        search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(period.yearp)+'-06-01" and request_change_g_log.date_operation<"'+str(end)+'" and request_change_g_log.after_status != "pending"'
                    else:
                        search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(period.yearp)+'-06-01" and request_change_g_log.date_operation<"'+str(end)+'" and request_change_g_log.after_status != "pending" and '+personal_query
                    countNP = db.smart_query(db.request_change_g_log,search).count()
                infoeLevelTemp.append(countP-countNP)
            #INSERT MONTH
            infoLevel.append(infoeLevelTemp)
    #PER PROJECT
    elif str(request.vars['level'])=="3":
        #PROJECTS
        projects = GET_PROJECTS('requestchange_activity_log')
        projects=sorted(projects)
        #PERIOD OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Period'))
        infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
        infoLevel.append(infoeLevelTemp)
        #MONTH OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Month'))
        infoeLevelTemp.append(str(month[0]))
        infoLevel.append(infoeLevelTemp)
        #MIDDLE LINE OF REPORT
        infoeLevelTemp=[]
        infoLevel.append(infoeLevelTemp)
        #LABLE DETAIL OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Detail'))
        infoLevel.append(infoeLevelTemp)
        #LABELS OF DATA OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Project'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
            infoeLevelTemp.append(T('Total Made Requests'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
            infoeLevelTemp.append(T('Total Accepted request'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
            infoeLevelTemp.append(T('Total Rejected request'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="c":
            infoeLevelTemp.append(T('Total Canceled request'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="p":
            infoeLevelTemp.append(T('Total Pending Requests'))
        infoLevel.append(infoeLevelTemp)

        for projectT in projects:
            project=db(db.project.name==projectT).select().first()
            if project is None:
                project=db((db.course_activity_log.before_course==projectT)|(db.course_activity_log.after_course==projectT)).select().first()
                if project.before_course is not None:
                    project=project.before_course
                else:
                    project=project.after_course
            else:
                project=project.name
            infoeLevelTemp = []
            #NAME OF PROJECT
            infoeLevelTemp.append(project)
            #MADE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(month[1])+'" and request_change_g_log.date_request<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.after_status = "pending"'
                else:
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(month[1])+'" and request_change_g_log.date_request<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.after_status = "pending" and '+personal_query
                countI = db.smart_query(db.request_change_g_log,search).count()
                infoeLevelTemp.append(countI)
            #ACCEPTED
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                if personal_query == '':
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(month[1])+'" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.after_status = "accepted"'
                else:
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(month[1])+'" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.after_status = "accepted" and '+personal_query
                countI = db.smart_query(db.request_change_g_log,search).count()
                infoeLevelTemp.append(countI)
            #REJECTED
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(month[1])+'" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.after_status = "rejected"'
                else:
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(month[1])+'" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.after_status = "rejected" and '+personal_query
                countI = db.smart_query(db.request_change_g_log,search).count()
                infoeLevelTemp.append(countI)
            ##CANCELED
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="c":
                if personal_query == '':
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(month[1])+'" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.after_status = "canceled"'
                else:
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(month[1])+'" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.after_status = "canceled" and '+personal_query
                countI = db.smart_query(db.request_change_g_log,search).count()
                infoeLevelTemp.append(countI)
            #PENDING
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="p":
                if period.period==1:
                    if personal_query == '':
                        search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(period.yearp)+'-01-01" and request_change_g_log.date_request<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.after_status = "pending"'
                    else:
                        search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(period.yearp)+'-01-01" and request_change_g_log.date_request<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.after_status = "pending" and '+personal_query
                    countP = db.smart_query(db.request_change_g_log,search).count()
                    if personal_query == '':
                        search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(period.yearp)+'-01-01" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.after_status != "pending"'
                    else:
                        search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(period.yearp)+'-01-01" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.after_status != "pending" and '+personal_query
                    countNP = db.smart_query(db.request_change_g_log,search).count()
                else:
                    if personal_query == '':
                        search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(period.yearp)+'-06-01" and request_change_g_log.date_request<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.after_status = "pending"'
                    else:
                        search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(period.yearp)+'-06-01" and request_change_g_log.date_request<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.after_status = "pending" and '+personal_query
                    countP = db.smart_query(db.request_change_g_log,search).count()
                    if personal_query == '':
                        search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(period.yearp)+'-06-01" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.after_status != "pending"'
                    else:
                        search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(period.yearp)+'-06-01" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.after_status != "pending" and '+personal_query
                    countNP = db.smart_query(db.request_change_g_log,search).count()
                infoeLevelTemp.append(countP-countNP)
            #INSERT PROJECT
            infoLevel.append(infoeLevelTemp)
    #PER USER
    elif str(request.vars['level'])=="4":
        #USERS
        usersProject = GET_USERS(period,project,'Student','requestchange_activity_log')
        #PERIOD OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Period'))
        infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
        infoLevel.append(infoeLevelTemp)
        #MONTH OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Month'))
        infoeLevelTemp.append(str(month[0]))
        infoLevel.append(infoeLevelTemp)
        #PROJECT OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Project'))
        infoeLevelTemp.append(str(project))
        infoLevel.append(infoeLevelTemp)
        #ROL OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Role'))
        infoeLevelTemp.append(T('Rol Student'))
        infoLevel.append(infoeLevelTemp)
        #MIDDLE LINE OF REPORT
        infoeLevelTemp=[]
        infoLevel.append(infoeLevelTemp)
        #LABLE DETAIL OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Detail'))
        infoLevel.append(infoeLevelTemp)
        #LABELS OF DATA OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('User'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
            infoeLevelTemp.append(T('Total Made Requests'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
            infoeLevelTemp.append(T('Total Accepted request'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
            infoeLevelTemp.append(T('Total Rejected request'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="c":
            infoeLevelTemp.append(T('Total Canceled request'))
        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="p":
            infoeLevelTemp.append(T('Total Pending Requests'))
        infoLevel.append(infoeLevelTemp)

        for userPT in usersProject:
            userP=db(db.auth_user.username==userPT).select().first()
            if userP is None:
                userP=db(db.request_change_g_log.user_request==userPT).select().first()
                userP=userP.user_request
            else:
                userP=userP.username
            infoeLevelTemp = []
            #NAME OF USER
            infoeLevelTemp.append(userP)
            #MADE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(month[1])+'" and request_change_g_log.date_request<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "pending"'
                else:
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(month[1])+'" and request_change_g_log.date_request<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "pending" and '+personal_query
                countI = db.smart_query(db.request_change_g_log,search).count()
                infoeLevelTemp.append(countI)
            #ACCEPTED
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                if personal_query == '':
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(month[1])+'" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "accepted"'
                else:
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(month[1])+'" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "accepted" and '+personal_query
                countI = db.smart_query(db.request_change_g_log,search).count()
                infoeLevelTemp.append(countI)
            #REJECTED
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(month[1])+'" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "rejected"'
                else:
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(month[1])+'" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "rejected" and '+personal_query
                countI = db.smart_query(db.request_change_g_log,search).count()
                infoeLevelTemp.append(countI)
            ##CANCELED
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="c":
                if personal_query == '':
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(month[1])+'" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "canceled"'
                else:
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(month[1])+'" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "canceled" and '+personal_query
                countI = db.smart_query(db.request_change_g_log,search).count()
                infoeLevelTemp.append(countI)
            #PENDING
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="p":
                if period.period==1:
                    if personal_query == '':
                        search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(period.yearp)+'-01-01" and request_change_g_log.date_request<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "pending"'
                    else:
                        search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(period.yearp)+'-01-01" and request_change_g_log.date_request<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "pending" and '+personal_query
                    countP = db.smart_query(db.request_change_g_log,search).count()
                    if personal_query == '':
                        search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(period.yearp)+'-01-01" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status != "pending"'
                    else:
                        search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(period.yearp)+'-01-01" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status != "pending" and '+personal_query
                    countNP = db.smart_query(db.request_change_g_log,search).count()
                else:
                    if personal_query == '':
                        search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(period.yearp)+'-06-01" and request_change_g_log.date_request<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "pending"'
                    else:
                        search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(period.yearp)+'-06-01" and request_change_g_log.date_request<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "pending" and '+personal_query
                    countP = db.smart_query(db.request_change_g_log,search).count()
                    if personal_query == '':
                        search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(period.yearp)+'-06-01" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status != "pending"'
                    else:
                        search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(period.yearp)+'-06-01" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status != "pending" and '+personal_query
                    countNP = db.smart_query(db.request_change_g_log,search).count()
                infoeLevelTemp.append(countP-countNP)
            #INSERT USER
            infoLevel.append(infoeLevelTemp)
    #DATA
    elif str(request.vars['level'])=="5":
        #PERIOD
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Period'))
        infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
        infoLevel.append(infoeLevelTemp)
        #MONTH
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Month'))
        infoeLevelTemp.append(str(month[0]))
        infoLevel.append(infoeLevelTemp)
        #PROJECT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Project'))
        infoeLevelTemp.append(str(project))
        infoLevel.append(infoeLevelTemp)
        #ROL
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Role'))
        infoeLevelTemp.append(T('Rol Student'))
        infoLevel.append(infoeLevelTemp)
        #USER
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('User'))
        infoeLevelTemp.append(str(userP))
        infoLevel.append(infoeLevelTemp)
        #MIDDLE LINE
        infoeLevelTemp=[]
        infoeLevelTemp.append('')
        infoLevel.append(infoeLevelTemp)
        #DETAIL
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Detail'))
        infoLevel.append(infoeLevelTemp)
        #TITLE OF TABLE
        infoeLevelTemp=[]
        infoeLevelTemp.append('Estado')
        infoeLevelTemp.append('Estado')
        infoeLevelTemp.append('Usuario Resolvio')
        infoeLevelTemp.append('Rol Resolvio')
        infoeLevelTemp.append('Descripción')
        infoeLevelTemp.append('Descripción LOG')
        infoeLevelTemp.append('Fecha')
        infoeLevelTemp.append('Fecha Solicitud')
        infoeLevelTemp.append('Fecha Resolvio')
        infoeLevelTemp.append('Actividad')
        infoeLevelTemp.append('Categoria')
        infoLevel.append(infoeLevelTemp)

        #MADE
        if str(request.vars['type_L'])=="d":
            if personal_query == '':
                search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(month[1])+'" and request_change_g_log.date_request<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "pending"'
            else:
                search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(month[1])+'" and request_change_g_log.date_request<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "pending" and '+personal_query
            for data in db.smart_query(db.request_change_g_log,search).select():
                infoeLevelTemp=[]
                infoeLevelTemp.append(data.before_status)
                infoeLevelTemp.append(data.after_status)
                infoeLevelTemp.append(data.resolve_user)
                infoeLevelTemp.append(data.roll_resolve)
                infoeLevelTemp.append(data.description)
                infoeLevelTemp.append(data.description_log)
                infoeLevelTemp.append(data.date_operation)
                infoeLevelTemp.append(data.date_request)
                infoeLevelTemp.append(data.date_request_resolve)
                infoeLevelTemp.append(data.activity)
                infoeLevelTemp.append(data.category)
                infoLevel.append(infoeLevelTemp)
                infoeLevelTemp=[]
                infoeLevelTemp.append('')
                infoeLevelTemp.append('')
                infoeLevelTemp.append(T('Operation'))
                infoeLevelTemp.append(T('Academic'))
                infoeLevelTemp.append(T('Before Grade'))
                infoeLevelTemp.append(T('After Grade'))
                infoLevel.append(infoeLevelTemp)
                for details in db(db.request_change_grade_d_log.request_change_g_log==data.id).select():
                    infoeLevelTemp=[]
                    infoeLevelTemp.append('')
                    infoeLevelTemp.append('')
                    infoeLevelTemp.append(details.operation_request)
                    infoeLevelTemp.append(details.academic)
                    infoeLevelTemp.append(details.before_grade)
                    infoeLevelTemp.append(details.after_grade)
                    infoLevel.append(infoeLevelTemp)
                infoeLevelTemp=[]
                infoeLevelTemp.append('')
                infoLevel.append(infoeLevelTemp)
        #ACCEPTED
        elif str(request.vars['type_L'])=="i":
            if personal_query == '':
                search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(month[1])+'" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "accepted"'
            else:
                search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(month[1])+'" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "accepted" and '+personal_query
            for data in db.smart_query(db.request_change_g_log,search).select():
                infoeLevelTemp=[]
                infoeLevelTemp.append(data.before_status)
                infoeLevelTemp.append(data.after_status)
                infoeLevelTemp.append(data.resolve_user)
                infoeLevelTemp.append(data.roll_resolve)
                infoeLevelTemp.append(data.description)
                infoeLevelTemp.append(data.description_log)
                infoeLevelTemp.append(data.date_operation)
                infoeLevelTemp.append(data.date_request)
                infoeLevelTemp.append(data.date_request_resolve)
                infoeLevelTemp.append(data.activity)
                infoeLevelTemp.append(data.category)
                infoLevel.append(infoeLevelTemp)
                infoeLevelTemp=[]
                infoeLevelTemp.append('')
                infoeLevelTemp.append('')
                infoeLevelTemp.append(T('Operation'))
                infoeLevelTemp.append(T('Academic'))
                infoeLevelTemp.append(T('Before Grade'))
                infoeLevelTemp.append(T('After Grade'))
                infoLevel.append(infoeLevelTemp)
                for details in db(db.request_change_grade_d_log.request_change_g_log==data.id).select():
                    infoeLevelTemp=[]
                    infoeLevelTemp.append('')
                    infoeLevelTemp.append('')
                    infoeLevelTemp.append(details.operation_request)
                    infoeLevelTemp.append(details.academic)
                    infoeLevelTemp.append(details.before_grade)
                    infoeLevelTemp.append(details.after_grade)
                    infoLevel.append(infoeLevelTemp)
                infoeLevelTemp=[]
                infoeLevelTemp.append('')
                infoLevel.append(infoeLevelTemp)
        #REJECTED
        elif str(request.vars['type_L'])=="u":
            if personal_query == '':
                search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(month[1])+'" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "rejected"'
            else:
                search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(month[1])+'" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "rejected" and '+personal_query
            for data in db.smart_query(db.request_change_g_log,search).select():
                infoeLevelTemp=[]
                infoeLevelTemp.append(data.before_status)
                infoeLevelTemp.append(data.after_status)
                infoeLevelTemp.append(data.resolve_user)
                infoeLevelTemp.append(data.roll_resolve)
                infoeLevelTemp.append(data.description)
                infoeLevelTemp.append(data.description_log)
                infoeLevelTemp.append(data.date_operation)
                infoeLevelTemp.append(data.date_request)
                infoeLevelTemp.append(data.date_request_resolve)
                infoeLevelTemp.append(data.activity)
                infoeLevelTemp.append(data.category)
                infoLevel.append(infoeLevelTemp)
                infoeLevelTemp=[]
                infoeLevelTemp.append('')
                infoeLevelTemp.append('')
                infoeLevelTemp.append(T('Operation'))
                infoeLevelTemp.append(T('Academic'))
                infoeLevelTemp.append(T('Before Grade'))
                infoeLevelTemp.append(T('After Grade'))
                infoLevel.append(infoeLevelTemp)
                for details in db(db.request_change_grade_d_log.request_change_g_log==data.id).select():
                    infoeLevelTemp=[]
                    infoeLevelTemp.append('')
                    infoeLevelTemp.append('')
                    infoeLevelTemp.append(details.operation_request)
                    infoeLevelTemp.append(details.academic)
                    infoeLevelTemp.append(details.before_grade)
                    infoeLevelTemp.append(details.after_grade)
                    infoLevel.append(infoeLevelTemp)
                infoeLevelTemp=[]
                infoeLevelTemp.append('')
                infoLevel.append(infoeLevelTemp)
        ##CANCELED
        elif str(request.vars['type_L'])=="c":
            if personal_query == '':
                search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(month[1])+'" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "canceled"'
            else:
                search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(month[1])+'" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "canceled" and '+personal_query
            for data in db.smart_query(db.request_change_g_log,search).select():
                infoeLevelTemp=[]
                infoeLevelTemp.append(data.before_status)
                infoeLevelTemp.append(data.after_status)
                infoeLevelTemp.append(data.resolve_user)
                infoeLevelTemp.append(data.roll_resolve)
                infoeLevelTemp.append(data.description)
                infoeLevelTemp.append(data.description_log)
                infoeLevelTemp.append(data.date_operation)
                infoeLevelTemp.append(data.date_request)
                infoeLevelTemp.append(data.date_request_resolve)
                infoeLevelTemp.append(data.activity)
                infoeLevelTemp.append(data.category)
                infoLevel.append(infoeLevelTemp)
                infoeLevelTemp=[]
                infoeLevelTemp.append('')
                infoeLevelTemp.append('')
                infoeLevelTemp.append(T('Operation'))
                infoeLevelTemp.append(T('Academic'))
                infoeLevelTemp.append(T('Before Grade'))
                infoeLevelTemp.append(T('After Grade'))
                infoLevel.append(infoeLevelTemp)
                for details in db(db.request_change_grade_d_log.request_change_g_log==data.id).select():
                    infoeLevelTemp=[]
                    infoeLevelTemp.append('')
                    infoeLevelTemp.append('')
                    infoeLevelTemp.append(details.operation_request)
                    infoeLevelTemp.append(details.academic)
                    infoeLevelTemp.append(details.before_grade)
                    infoeLevelTemp.append(details.after_grade)
                    infoLevel.append(infoeLevelTemp)
                infoeLevelTemp=[]
                infoeLevelTemp.append('')
                infoLevel.append(infoeLevelTemp)
        #PENDING
        elif str(request.vars['type_L'])=="p":
            if period.period==1:
                if personal_query == '':
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(period.yearp)+'-01-01" and request_change_g_log.date_request<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "pending"'
                else:
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(period.yearp)+'-01-01" and request_change_g_log.date_request<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "pending" and '+personal_query
                for pending in db.smart_query(db.request_change_g_log,search).select():
                    if personal_query == '':
                        search='request_change_g_log.r_c_g_id = "'+str(pending.r_c_g_id)+'" and request_change_g_log.after_status != "pending"'
                    else:
                        search='request_change_g_log.r_c_g_id = "'+str(pending.r_c_g_id)+'" and request_change_g_log.after_status != "pending" and '+personal_query
                    if db.smart_query(db.request_change_g_log,search).select().first() is None:
                        infoeLevelTemp=[]
                        infoeLevelTemp.append(pending.before_status)
                        infoeLevelTemp.append(pending.after_status)
                        infoeLevelTemp.append(pending.resolve_user)
                        infoeLevelTemp.append(pending.roll_resolve)
                        infoeLevelTemp.append(pending.description)
                        infoeLevelTemp.append(pending.description_log)
                        infoeLevelTemp.append(pending.date_operation)
                        infoeLevelTemp.append(pending.date_request)
                        infoeLevelTemp.append(pending.date_request_resolve)
                        infoeLevelTemp.append(pending.activity)
                        infoeLevelTemp.append(pending.category)
                        infoLevel.append(infoeLevelTemp)
                        infoeLevelTemp=[]
                        infoeLevelTemp.append('')
                        infoeLevelTemp.append('')
                        infoeLevelTemp.append(T('Operation'))
                        infoeLevelTemp.append(T('Academic'))
                        infoeLevelTemp.append(T('Before Grade'))
                        infoeLevelTemp.append(T('After Grade'))
                        infoLevel.append(infoeLevelTemp)
                        for details in db(db.request_change_grade_d_log.request_change_g_log==pending.id).select():
                            infoeLevelTemp=[]
                            infoeLevelTemp.append('')
                            infoeLevelTemp.append('')
                            infoeLevelTemp.append(details.operation_request)
                            infoeLevelTemp.append(details.academic)
                            infoeLevelTemp.append(details.before_grade)
                            infoeLevelTemp.append(details.after_grade)
                            infoLevel.append(infoeLevelTemp)
                        infoeLevelTemp=[]
                        infoeLevelTemp.append('')
                        infoLevel.append(infoeLevelTemp)
            else:
                if personal_query == '':
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(period.yearp)+'-06-01" and request_change_g_log.date_request<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "pending"'
                else:
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(period.yearp)+'-06-01" and request_change_g_log.date_request<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "pending" and '+personal_query
                for pending in db.smart_query(db.request_change_g_log,search).select():
                    if personal_query == '':
                        search='request_change_g_log.r_c_g_id = "'+str(pending.r_c_g_id)+'" and request_change_g_log.after_status != "pending"'
                    else:
                        search='request_change_g_log.r_c_g_id = "'+str(pending.r_c_g_id)+'" and request_change_g_log.after_status != "pending" and '+personal_query
                    if db.smart_query(db.request_change_g_log,search).select().first() is None:
                        infoeLevelTemp=[]
                        infoeLevelTemp.append(pending.before_status)
                        infoeLevelTemp.append(pending.after_status)
                        infoeLevelTemp.append(pending.resolve_user)
                        infoeLevelTemp.append(pending.roll_resolve)
                        infoeLevelTemp.append(pending.description)
                        infoeLevelTemp.append(pending.description_log)
                        infoeLevelTemp.append(pending.date_operation)
                        infoeLevelTemp.append(pending.date_request)
                        infoeLevelTemp.append(pending.date_request_resolve)
                        infoeLevelTemp.append(pending.activity)
                        infoeLevelTemp.append(pending.category)
                        infoLevel.append(infoeLevelTemp)
                        infoeLevelTemp=[]
                        infoeLevelTemp.append('')
                        infoeLevelTemp.append('')
                        infoeLevelTemp.append(T('Operation'))
                        infoeLevelTemp.append(T('Academic'))
                        infoeLevelTemp.append(T('Before Grade'))
                        infoeLevelTemp.append(T('After Grade'))
                        infoLevel.append(infoeLevelTemp)
                        for details in db(db.request_change_grade_d_log.request_change_g_log==pending.id).select():
                            infoeLevelTemp=[]
                            infoeLevelTemp.append('')
                            infoeLevelTemp.append('')
                            infoeLevelTemp.append(details.operation_request)
                            infoeLevelTemp.append(details.academic)
                            infoeLevelTemp.append(details.before_grade)
                            infoeLevelTemp.append(details.after_grade)
                            infoLevel.append(infoeLevelTemp)
                        infoeLevelTemp=[]
                        infoeLevelTemp.append('')
                        infoLevel.append(infoeLevelTemp)
        #ALL
        elif str(request.vars['type_L'])=="all":
            #MADE AND PENDING
            if period.period==1:
                if personal_query == '':
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(period.yearp)+'-01-01" and request_change_g_log.date_request<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "pending"'
                else:
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(period.yearp)+'-01-01" and request_change_g_log.date_request<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "pending" and '+personal_query
                for pending in db.smart_query(db.request_change_g_log,search).select():
                    if personal_query == '':
                        search='request_change_g_log.r_c_g_id = "'+str(pending.r_c_g_id)+'" and request_change_g_log.after_status != "pending"'
                    else:
                        search='request_change_g_log.r_c_g_id = "'+str(pending.r_c_g_id)+'" and request_change_g_log.after_status != "pending" and '+personal_query
                    if db.smart_query(db.request_change_g_log,search).select().first() is None:
                        infoeLevelTemp=[]
                        infoeLevelTemp.append(pending.before_status)
                        infoeLevelTemp.append(pending.after_status)
                        infoeLevelTemp.append(pending.resolve_user)
                        infoeLevelTemp.append(pending.roll_resolve)
                        infoeLevelTemp.append(pending.description)
                        infoeLevelTemp.append(pending.description_log)
                        infoeLevelTemp.append(pending.date_operation)
                        infoeLevelTemp.append(pending.date_request)
                        infoeLevelTemp.append(pending.date_request_resolve)
                        infoeLevelTemp.append(pending.activity)
                        infoeLevelTemp.append(pending.category)
                        infoLevel.append(infoeLevelTemp)
                        infoeLevelTemp=[]
                        infoeLevelTemp.append('')
                        infoeLevelTemp.append('')
                        infoeLevelTemp.append(T('Operation'))
                        infoeLevelTemp.append(T('Academic'))
                        infoeLevelTemp.append(T('Before Grade'))
                        infoeLevelTemp.append(T('After Grade'))
                        infoLevel.append(infoeLevelTemp)
                        for details in db(db.request_change_grade_d_log.request_change_g_log==pending.id).select():
                            infoeLevelTemp=[]
                            infoeLevelTemp.append('')
                            infoeLevelTemp.append('')
                            infoeLevelTemp.append(details.operation_request)
                            infoeLevelTemp.append(details.academic)
                            infoeLevelTemp.append(details.before_grade)
                            infoeLevelTemp.append(details.after_grade)
                            infoLevel.append(infoeLevelTemp)
                        infoeLevelTemp=[]
                        infoeLevelTemp.append('')
                        infoLevel.append(infoeLevelTemp)
            else:
                if personal_query == '':
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(period.yearp)+'-06-01" and request_change_g_log.date_request<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "pending"'
                else:
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(period.yearp)+'-06-01" and request_change_g_log.date_request<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "pending" and '+personal_query
                for pending in db.smart_query(db.request_change_g_log,search).select():
                    if personal_query == '':
                        search='request_change_g_log.r_c_g_id = "'+str(pending.r_c_g_id)+'" and request_change_g_log.after_status != "pending"'
                    else:
                        search='request_change_g_log.r_c_g_id = "'+str(pending.r_c_g_id)+'" and request_change_g_log.after_status != "pending" and '+personal_query
                    if db.smart_query(db.request_change_g_log,search).select().first() is None:
                        infoeLevelTemp=[]
                        infoeLevelTemp.append(pending.before_status)
                        infoeLevelTemp.append(pending.after_status)
                        infoeLevelTemp.append(pending.resolve_user)
                        infoeLevelTemp.append(pending.roll_resolve)
                        infoeLevelTemp.append(pending.description)
                        infoeLevelTemp.append(pending.description_log)
                        infoeLevelTemp.append(pending.date_operation)
                        infoeLevelTemp.append(pending.date_request)
                        infoeLevelTemp.append(pending.date_request_resolve)
                        infoeLevelTemp.append(pending.activity)
                        infoeLevelTemp.append(pending.category)
                        infoLevel.append(infoeLevelTemp)
                        infoeLevelTemp=[]
                        infoeLevelTemp.append('')
                        infoeLevelTemp.append('')
                        infoeLevelTemp.append(T('Operation'))
                        infoeLevelTemp.append(T('Academic'))
                        infoeLevelTemp.append(T('Before Grade'))
                        infoeLevelTemp.append(T('After Grade'))
                        infoLevel.append(infoeLevelTemp)
                        for details in db(db.request_change_grade_d_log.request_change_g_log==pending.id).select():
                            infoeLevelTemp=[]
                            infoeLevelTemp.append('')
                            infoeLevelTemp.append('')
                            infoeLevelTemp.append(details.operation_request)
                            infoeLevelTemp.append(details.academic)
                            infoeLevelTemp.append(details.before_grade)
                            infoeLevelTemp.append(details.after_grade)
                            infoLevel.append(infoeLevelTemp)
                        infoeLevelTemp=[]
                        infoeLevelTemp.append('')
                        infoLevel.append(infoeLevelTemp)
            #ACCEPTED
            if personal_query == '':
                search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(month[1])+'" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "accepted"'
            else:
                search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(month[1])+'" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "accepted" and '+personal_query
            for data in db.smart_query(db.request_change_g_log,search).select():
                infoeLevelTemp=[]
                infoeLevelTemp.append(data.before_status)
                infoeLevelTemp.append(data.after_status)
                infoeLevelTemp.append(data.resolve_user)
                infoeLevelTemp.append(data.roll_resolve)
                infoeLevelTemp.append(data.description)
                infoeLevelTemp.append(data.description_log)
                infoeLevelTemp.append(data.date_operation)
                infoeLevelTemp.append(data.date_request)
                infoeLevelTemp.append(data.date_request_resolve)
                infoeLevelTemp.append(data.activity)
                infoeLevelTemp.append(data.category)
                infoLevel.append(infoeLevelTemp)
                infoeLevelTemp=[]
                infoeLevelTemp.append('')
                infoeLevelTemp.append('')
                infoeLevelTemp.append(T('Operation'))
                infoeLevelTemp.append(T('Academic'))
                infoeLevelTemp.append(T('Before Grade'))
                infoeLevelTemp.append(T('After Grade'))
                infoLevel.append(infoeLevelTemp)
                for details in db(db.request_change_grade_d_log.request_change_g_log==data.id).select():
                    infoeLevelTemp=[]
                    infoeLevelTemp.append('')
                    infoeLevelTemp.append('')
                    infoeLevelTemp.append(details.operation_request)
                    infoeLevelTemp.append(details.academic)
                    infoeLevelTemp.append(details.before_grade)
                    infoeLevelTemp.append(details.after_grade)
                    infoLevel.append(infoeLevelTemp)
                infoeLevelTemp=[]
                infoeLevelTemp.append('')
                infoLevel.append(infoeLevelTemp)
            #REJECTED
            if personal_query == '':
                search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(month[1])+'" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "rejected"'
            else:
                search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(month[1])+'" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "rejected" and '+personal_query
            for data in db.smart_query(db.request_change_g_log,search).select():
                infoeLevelTemp=[]
                infoeLevelTemp.append(data.before_status)
                infoeLevelTemp.append(data.after_status)
                infoeLevelTemp.append(data.resolve_user)
                infoeLevelTemp.append(data.roll_resolve)
                infoeLevelTemp.append(data.description)
                infoeLevelTemp.append(data.description_log)
                infoeLevelTemp.append(data.date_operation)
                infoeLevelTemp.append(data.date_request)
                infoeLevelTemp.append(data.date_request_resolve)
                infoeLevelTemp.append(data.activity)
                infoeLevelTemp.append(data.category)
                infoLevel.append(infoeLevelTemp)
                infoeLevelTemp=[]
                infoeLevelTemp.append('')
                infoeLevelTemp.append('')
                infoeLevelTemp.append(T('Operation'))
                infoeLevelTemp.append(T('Academic'))
                infoeLevelTemp.append(T('Before Grade'))
                infoeLevelTemp.append(T('After Grade'))
                infoLevel.append(infoeLevelTemp)
                for details in db(db.request_change_grade_d_log.request_change_g_log==data.id).select():
                    infoeLevelTemp=[]
                    infoeLevelTemp.append('')
                    infoeLevelTemp.append('')
                    infoeLevelTemp.append(details.operation_request)
                    infoeLevelTemp.append(details.academic)
                    infoeLevelTemp.append(details.before_grade)
                    infoeLevelTemp.append(details.after_grade)
                    infoLevel.append(infoeLevelTemp)
                infoeLevelTemp=[]
                infoeLevelTemp.append('')
                infoLevel.append(infoeLevelTemp)
            ##CANCELED
            if personal_query == '':
                search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(month[1])+'" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "canceled"'
            else:
                search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(month[1])+'" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "canceled" and '+personal_query
            for data in db.smart_query(db.request_change_g_log,search).select():
                infoeLevelTemp=[]
                infoeLevelTemp.append(data.before_status)
                infoeLevelTemp.append(data.after_status)
                infoeLevelTemp.append(data.resolve_user)
                infoeLevelTemp.append(data.roll_resolve)
                infoeLevelTemp.append(data.description)
                infoeLevelTemp.append(data.description_log)
                infoeLevelTemp.append(data.date_operation)
                infoeLevelTemp.append(data.date_request)
                infoeLevelTemp.append(data.date_request_resolve)
                infoeLevelTemp.append(data.activity)
                infoeLevelTemp.append(data.category)
                infoLevel.append(infoeLevelTemp)
                infoeLevelTemp=[]
                infoeLevelTemp.append('')
                infoeLevelTemp.append('')
                infoeLevelTemp.append(T('Operation'))
                infoeLevelTemp.append(T('Academic'))
                infoeLevelTemp.append(T('Before Grade'))
                infoeLevelTemp.append(T('After Grade'))
                infoLevel.append(infoeLevelTemp)
                for details in db(db.request_change_grade_d_log.request_change_g_log==data.id).select():
                    infoeLevelTemp=[]
                    infoeLevelTemp.append('')
                    infoeLevelTemp.append('')
                    infoeLevelTemp.append(details.operation_request)
                    infoeLevelTemp.append(details.academic)
                    infoeLevelTemp.append(details.before_grade)
                    infoeLevelTemp.append(details.after_grade)
                    infoLevel.append(infoeLevelTemp)
                infoeLevelTemp=[]
                infoeLevelTemp.append('')
                infoLevel.append(infoeLevelTemp)
    #*****************************************************REPORT*****************************************************
    #****************************************************************************************************************
    #****************************************************************************************************************
    return dict(filename='ReporteGestionSolicitudesCambioNotas', csvdata=infoLevel)


@auth.requires_login()
@auth.requires(auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
def crg_LOAD():
    requestC = None
    requestD = None
    showLevel=False
    try:
        requestC = db(db.request_change_g_log.id==int(request.vars['id'])).select().first()
        if requestC is not None:
            showLevel=True
            requestD = db(db.request_change_grade_d_log.request_change_g_log==int(request.vars['id'])).select()
    except:
        showLevel=False
    return dict(showLevel=showLevel, requestC=requestC, requestD=requestD)


@auth.requires_login()
@auth.requires(auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
def change_request_grades_management():
    #****************************************************************************************************************
    #****************************************************************************************************************
    #***************************************CHECK IF THERE IS A PERSONALIZED QUERY***********************************
    personal_query = ''
    makeRedirect = False
    if request.vars['querySearch'] is not None and str(request.vars['querySearch']) != "":
        #PERSONALIZED QUERY SURE WORK
        try:
            personal_query = str(request.vars['querySearch'])
            countI = db.smart_query(db.request_change_g_log,personal_query).count()
            if request.vars['searchT'] is not None and str(request.vars['searchT']) == 'T':
                makeRedirect = True
        except:
            response.flash = T('The query is not valid. The report is displayed without applying any query.')
            personal_query = ''
    if makeRedirect == True:
        redirect(URL('management_reports', 'change_request_grades_management',vars=dict(level = '5', period = request.vars['period'], month = str(request.vars['month']), project = str(request.vars['project']), userP = str(request.vars['userP']), type_L=request.vars['type_L'], type_U=request.vars['type_U'], querySearch=request.vars['querySearch'])))
    

    #****************************************************************************************************************
    #****************************************************************************************************************
    #******************************************VERIFY THAT ACCURATE PARAMETERS***************************************
    try:
        #CHECK THAT THE LEVEL OF REPORT IS VALID
        if request.vars['level'] is not None and (int(request.vars['level'])<1 or int(request.vars['level'])>5):
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #VERIFY THAT THE PARAMETERS OF EACH LEVEL BE VALID
        if request.vars['level'] is not None:
            #LEVEL MORE THAN 1
            if int(request.vars['level'])>1:
                #CHECK IF THE TYPE OF REPORT IS VALID
                if request.vars['type_L'] is None or (str(request.vars['type_L'])!="all" and str(request.vars['type_L'])!="i" and str(request.vars['type_L'])!="u" and str(request.vars['type_L'])!="d" and str(request.vars['type_L'])!="p" and str(request.vars['type_L'])!="c"):
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))

                period = VALIDATE_PERIOD(request.vars['period'])
                if period is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))
            
            #LEVEL MORE THAN 2
            if int(request.vars['level'])>2:
                #CHECK IF THE TYPE OF REPORT IS VALID
                if request.vars['type_U'] is None or (str(request.vars['type_U'])!="all" and str(request.vars['type_U'])!="i" and str(request.vars['type_U'])!="u" and str(request.vars['type_U'])!="d" and str(request.vars['type_L'])!="p" and str(request.vars['type_L'])!="c"):
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))

                #CHECK IF THE MONTH IS VALID
                month = VALIDATE_MONTH(request.vars['month'],period)
                if month is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))
            
            #LEVEL MORE THAN 3
            if int(request.vars['level'])>3:
                #CHECK IF THE PROJECT IS VALID
                project = VALIDATE_PROJECT(request.vars['project'],'request_change_g_log')
                if project is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))

            #LEVEL MORE THAN 4
            if int(request.vars['level'])>4:
                #CHECK IF THE USER IS VALID
                userP = VALIDATE_USER(period,project,'Student',request.vars['userP'],'request_change_g_log')
                if userP is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))
    except:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))

    
    #****************************************************************************************************************
    #****************************************************************************************************************
    #**************************************************SEARCH REPORT*************************************************
    def filtered_by(flag):
        fsearch_Option=[]
        fsearch_Option.append('=')
        fsearch_Option.append('!=')
        fsearch_Option.append('<')
        fsearch_Option.append('>')
        fsearch_Option.append('<=')
        fsearch_Option.append('>=')
        if flag==True:
            fsearch_Option.append('starts with')
            fsearch_Option.append('contains')
            fsearch_Option.append('in')
            fsearch_Option.append('not in')
        return fsearch_Option


    fsearch = []
    #******************************COMBOS INFORMATION******************************
    #YEARS
    if request.vars['level']=='1' or request.vars['level'] is None:
        groupYears = GET_YEARS()
        if len(groupYears) != 0:
            fsearch.append(['yearp','Año',False,[3,sorted(groupYears)]])
    #PROJECTS
    if request.vars['level'] is None or int(request.vars['level'])<=3:
        projects = GET_PROJECTS('request_change_g_log')
        if len(projects) != 0:
            fsearch_Values=[]
            fsearch_Values.append(2)
            for projectT in projects:
                project=db(db.project.name==projectT).select().first()
                if project is None:
                    project=db(db.request_change_g_log.project==projectT).select().first()
                    project=project.project
                else:
                    project=project.name
                fsearch_Values.append(project)
            fsearch.append(['project','Curso',False,fsearch_Values])
    #OPERATION LOG
    fsearch.append(['after_status','Estado',False,[3,['accepted','rejected','pending','canceled']]])
    #CATEGORIES
    groupCategories = GET_CATEGORIES('request_change_g_log')
    if len(groupCategories) != 0:
        fsearch.append(['category','Categoria',False,[3,sorted(groupCategories)]])
    #ACTIVITIES
    groupActivities = GET_ACTIVITIES('request_change_g_log')
    if len(groupActivities) !=0:
        fsearch.append(['activity','Actividad',False,[3,sorted(groupActivities)]])
    #DATES
    dates = GET_DATES('request_change_g_log')
    if len(dates) != 0:
        fsearch.append(['date_request','Fecha',False,[3,sorted(dates)]])
    #******************************ENTERING USER******************************
    #USER REQUEST
    if request.vars['level'] is None or int(request.vars['level'])<=4:
        fsearch.append(['user_request','Usuario Solicitud',False,[1]])


    #****************************************************************************************************************
    #****************************************************************************************************************
    #*****************************************************REPORT*****************************************************
    #LEVELS OF REPORT
    from datetime import datetime
    infoLevel = []
    grid=[]
    #ALL SEMESTERS
    if request.vars['level']=='1' or request.vars['level'] is None:
        groupPeriods = db(db.period_year).select(orderby=~db.period_year.id)
        if len(groupPeriods) == 0:
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('default','index'))
        for period in groupPeriods:
            infoeLevelTemp = []
            #ID OF PERIOD
            infoeLevelTemp.append(period.id)
            #NAME OF PERIOD
            infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
            #MADE
            if personal_query == '':
                search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.after_status = "pending"'
            else:
                search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.after_status = "pending" and '+personal_query
            countI = db.smart_query(db.request_change_g_log,search).count()
            infoeLevelTemp.append(countI)
            #ACCEPTED
            if personal_query == '':
                search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.after_status = "accepted"'
            else:
                search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.after_status = "accepted" and '+personal_query
            countI = db.smart_query(db.request_change_g_log,search).count()
            infoeLevelTemp.append(countI)
            #REJECTED
            if personal_query == '':
                search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.after_status = "rejected"'
            else:
                search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.after_status = "rejected" and '+personal_query
            countI = db.smart_query(db.request_change_g_log,search).count()
            infoeLevelTemp.append(countI)
            #CANCELED
            if personal_query == '':
                search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.after_status = "canceled"'
            else:
                search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.after_status = "canceled" and '+personal_query
            countI = db.smart_query(db.request_change_g_log,search).count()
            infoeLevelTemp.append(countI)
            #PENDING
            infoeLevelTemp.append(infoeLevelTemp[2]-infoeLevelTemp[3]-infoeLevelTemp[4]-infoeLevelTemp[5])
            #INSERT PERIOD
            infoLevel.append(infoeLevelTemp)
    #PER MONTH
    elif str(request.vars['level'])=="2":
        for month in GET_MONTH_PERIOD(period):
            start = datetime.strptime(str(period.yearp) + '-' + str(month[0]) +'-01', "%Y-%m-%d")
            if month[2]==1:
                end = datetime.strptime(str(period.yearp+1) + '-' + str(month[2]) +'-01', "%Y-%m-%d")
            else:
                end = datetime.strptime(str(period.yearp) + '-' + str(month[2]) +'-01', "%Y-%m-%d")
            infoeLevelTemp = []
            #NAME OF PERIOD
            infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
            #ID OF MONTH
            infoeLevelTemp.append(month[0])
            #NAME OF MONTH
            infoeLevelTemp.append(month[1]+' '+str(period.yearp))
            #MADE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(start)+'" and request_change_g_log.date_request<"'+str(end)+'" and request_change_g_log.after_status = "pending"'
                else:
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(start)+'" and request_change_g_log.date_request<"'+str(end)+'" and request_change_g_log.after_status = "pending" and '+personal_query
                countI = db.smart_query(db.request_change_g_log,search).count()
                infoeLevelTemp.append(countI)
            #ACCEPTED
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                if personal_query == '':
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(start)+'" and request_change_g_log.date_operation<"'+str(end)+'" and request_change_g_log.after_status = "accepted"'
                else:
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(start)+'" and request_change_g_log.date_operation<"'+str(end)+'" and request_change_g_log.after_status = "accepted" and '+personal_query
                countI = db.smart_query(db.request_change_g_log,search).count()
                infoeLevelTemp.append(countI)
            #REJECTED
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(start)+'" and request_change_g_log.date_operation<"'+str(end)+'" and request_change_g_log.after_status = "rejected"'
                else:
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(start)+'" and request_change_g_log.date_operation<"'+str(end)+'" and request_change_g_log.after_status = "rejected" and '+personal_query
                countI = db.smart_query(db.request_change_g_log,search).count()
                infoeLevelTemp.append(countI)
            ##CANCELED
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="c":
                if personal_query == '':
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(start)+'" and request_change_g_log.date_operation<"'+str(end)+'" and request_change_g_log.after_status = "canceled"'
                else:
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(start)+'" and request_change_g_log.date_operation<"'+str(end)+'" and request_change_g_log.after_status = "canceled" and '+personal_query
                countI = db.smart_query(db.request_change_g_log,search).count()
                infoeLevelTemp.append(countI)
            #PENDING
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="p":
                if period.period==1:
                    if personal_query == '':
                        search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(period.yearp)+'-01-01" and request_change_g_log.date_request<"'+str(end)+'" and request_change_g_log.after_status = "pending"'
                    else:
                        search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(period.yearp)+'-01-01" and request_change_g_log.date_request<"'+str(end)+'" and request_change_g_log.after_status = "pending" and '+personal_query
                    countP = db.smart_query(db.request_change_g_log,search).count()
                    if personal_query == '':
                        search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(period.yearp)+'-01-01" and request_change_g_log.date_operation<"'+str(end)+'" and request_change_g_log.after_status != "pending"'
                    else:
                        search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(period.yearp)+'-01-01" and request_change_g_log.date_operation<"'+str(end)+'" and request_change_g_log.after_status != "pending" and '+personal_query
                    countNP = db.smart_query(db.request_change_g_log,search).count()
                else:
                    if personal_query == '':
                        search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(period.yearp)+'-06-01" and request_change_g_log.date_request<"'+str(end)+'" and request_change_g_log.after_status = "pending"'
                    else:
                        search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(period.yearp)+'-06-01" and request_change_g_log.date_request<"'+str(end)+'" and request_change_g_log.after_status = "pending" and '+personal_query
                    countP = db.smart_query(db.request_change_g_log,search).count()
                    if personal_query == '':
                        search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(period.yearp)+'-06-01" and request_change_g_log.date_operation<"'+str(end)+'" and request_change_g_log.after_status != "pending"'
                    else:
                        search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(period.yearp)+'-06-01" and request_change_g_log.date_operation<"'+str(end)+'" and request_change_g_log.after_status != "pending" and '+personal_query
                    countNP = db.smart_query(db.request_change_g_log,search).count()
                infoeLevelTemp.append(countP-countNP)
            #INSERT MONTH
            infoLevel.append(infoeLevelTemp)
    #PER PROJECT
    elif str(request.vars['level'])=="3":
        if len(projects) == 0:
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('management_reports', 'change_request_grades_management',vars=dict(level='2',period = str(request.vars['period']), type_L = str(request.vars['type_U']), querySearch=personal_query)))

        for projectT in projects:
            project=db(db.project.name==projectT).select().first()
            if project is None:
                project=db((db.course_activity_log.before_course==projectT)|(db.course_activity_log.after_course==projectT)).select().first()
                if project.before_course is not None:
                    project=project.before_course
                else:
                    project=project.after_course
            else:
                project=project.name
            infoeLevelTemp = []
            #NAME OF PERIOD
            infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
            #NAME OF MONTH
            infoeLevelTemp.append(month[0])
            #ID OF PROJECT
            infoeLevelTemp.append(project)
            #NAME OF PROJECT
            infoeLevelTemp.append(project)
            #MADE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(month[1])+'" and request_change_g_log.date_request<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.after_status = "pending"'
                else:
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(month[1])+'" and request_change_g_log.date_request<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.after_status = "pending" and '+personal_query
                countI = db.smart_query(db.request_change_g_log,search).count()
                infoeLevelTemp.append(countI)
            #ACCEPTED
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                if personal_query == '':
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(month[1])+'" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.after_status = "accepted"'
                else:
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(month[1])+'" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.after_status = "accepted" and '+personal_query
                countI = db.smart_query(db.request_change_g_log,search).count()
                infoeLevelTemp.append(countI)
            #REJECTED
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(month[1])+'" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.after_status = "rejected"'
                else:
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(month[1])+'" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.after_status = "rejected" and '+personal_query
                countI = db.smart_query(db.request_change_g_log,search).count()
                infoeLevelTemp.append(countI)
            ##CANCELED
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="c":
                if personal_query == '':
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(month[1])+'" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.after_status = "canceled"'
                else:
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(month[1])+'" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.after_status = "canceled" and '+personal_query
                countI = db.smart_query(db.request_change_g_log,search).count()
                infoeLevelTemp.append(countI)
            #PENDING
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="p":
                if period.period==1:
                    if personal_query == '':
                        search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(period.yearp)+'-01-01" and request_change_g_log.date_request<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.after_status = "pending"'
                    else:
                        search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(period.yearp)+'-01-01" and request_change_g_log.date_request<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.after_status = "pending" and '+personal_query
                    countP = db.smart_query(db.request_change_g_log,search).count()
                    if personal_query == '':
                        search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(period.yearp)+'-01-01" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.after_status != "pending"'
                    else:
                        search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(period.yearp)+'-01-01" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.after_status != "pending" and '+personal_query
                    countNP = db.smart_query(db.request_change_g_log,search).count()
                else:
                    if personal_query == '':
                        search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(period.yearp)+'-06-01" and request_change_g_log.date_request<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.after_status = "pending"'
                    else:
                        search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(period.yearp)+'-06-01" and request_change_g_log.date_request<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.after_status = "pending" and '+personal_query
                    countP = db.smart_query(db.request_change_g_log,search).count()
                    if personal_query == '':
                        search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(period.yearp)+'-06-01" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.after_status != "pending"'
                    else:
                        search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(period.yearp)+'-06-01" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.after_status != "pending" and '+personal_query
                    countNP = db.smart_query(db.request_change_g_log,search).count()
                infoeLevelTemp.append(countP-countNP)
            #INSERT PROJECT
            infoLevel.append(infoeLevelTemp)
    #PER USER
    elif str(request.vars['level'])=="4":
        #VERIFY THAT CAN SHOW THE LEVEL OF THE REPORT
        usersProject = GET_USERS(period,project,'Student','request_change_g_log')
        if len(usersProject) == 0:
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('management_reports', 'change_request_grades_management',vars=dict(level='3', period = str(request.vars['period']), month = str(request.vars['month']), type_L = str(request.vars['type_U']), type_U = str(request.vars['type_U']), querySearch=personal_query)))

        for userPT in usersProject:
            userP=db(db.auth_user.username==userPT).select().first()
            if userP is None:
                userP=db(db.request_change_g_log.user_request==userPT).select().first()
                userP=userP.user_request
            else:
                userP=userP.username
            infoeLevelTemp = []
            #NAME OF PERIOD
            infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
            #NAME OF MONTH
            infoeLevelTemp.append(month[0])
            #NAME OF PROJECT
            infoeLevelTemp.append(project)
            #ID OF USER
            infoeLevelTemp.append(userP)
            #NAME OF USER
            infoeLevelTemp.append(userP)
            #MADE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(month[1])+'" and request_change_g_log.date_request<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "pending"'
                else:
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(month[1])+'" and request_change_g_log.date_request<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "pending" and '+personal_query
                countI = db.smart_query(db.request_change_g_log,search).count()
                infoeLevelTemp.append(countI)
            #ACCEPTED
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                if personal_query == '':
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(month[1])+'" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "accepted"'
                else:
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(month[1])+'" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "accepted" and '+personal_query
                countI = db.smart_query(db.request_change_g_log,search).count()
                infoeLevelTemp.append(countI)
            #REJECTED
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(month[1])+'" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "rejected"'
                else:
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(month[1])+'" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "rejected" and '+personal_query
                countI = db.smart_query(db.request_change_g_log,search).count()
                infoeLevelTemp.append(countI)
            ##CANCELED
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="c":
                if personal_query == '':
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(month[1])+'" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "canceled"'
                else:
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(month[1])+'" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "canceled" and '+personal_query
                countI = db.smart_query(db.request_change_g_log,search).count()
                infoeLevelTemp.append(countI)
            #PENDING
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="p":
                if period.period==1:
                    if personal_query == '':
                        search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(period.yearp)+'-01-01" and request_change_g_log.date_request<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "pending"'
                    else:
                        search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(period.yearp)+'-01-01" and request_change_g_log.date_request<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "pending" and '+personal_query
                    countP = db.smart_query(db.request_change_g_log,search).count()
                    if personal_query == '':
                        search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(period.yearp)+'-01-01" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status != "pending"'
                    else:
                        search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(period.yearp)+'-01-01" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status != "pending" and '+personal_query
                    countNP = db.smart_query(db.request_change_g_log,search).count()
                else:
                    if personal_query == '':
                        search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(period.yearp)+'-06-01" and request_change_g_log.date_request<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "pending"'
                    else:
                        search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(period.yearp)+'-06-01" and request_change_g_log.date_request<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "pending" and '+personal_query
                    countP = db.smart_query(db.request_change_g_log,search).count()
                    if personal_query == '':
                        search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(period.yearp)+'-06-01" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status != "pending"'
                    else:
                        search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(period.yearp)+'-06-01" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status != "pending" and '+personal_query
                    countNP = db.smart_query(db.request_change_g_log,search).count()
                infoeLevelTemp.append(countP-countNP)
            #INSERT USER
            infoLevel.append(infoeLevelTemp)
    #DATA
    elif str(request.vars['level'])=="5":
        #MADE
        if str(request.vars['type_L'])=="d":
            if personal_query == '':
                search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(month[1])+'" and request_change_g_log.date_request<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "pending"'
            else:
                search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(month[1])+'" and request_change_g_log.date_request<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "pending" and '+personal_query
            for data in db.smart_query(db.request_change_g_log,search).select():
                grid.append(data.id)
        #ACCEPTED
        elif str(request.vars['type_L'])=="i":
            if personal_query == '':
                search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(month[1])+'" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "accepted"'
            else:
                search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(month[1])+'" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "accepted" and '+personal_query
            for data in db.smart_query(db.request_change_g_log,search).select():
                grid.append(data.id)
        #REJECTED
        elif str(request.vars['type_L'])=="u":
            if personal_query == '':
                search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(month[1])+'" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "rejected"'
            else:
                search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(month[1])+'" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "rejected" and '+personal_query
            for data in db.smart_query(db.request_change_g_log,search).select():
                grid.append(data.id)
        ##CANCELED
        elif str(request.vars['type_L'])=="c":
            if personal_query == '':
                search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(month[1])+'" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "canceled"'
            else:
                search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(month[1])+'" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "canceled" and '+personal_query
            for data in db.smart_query(db.request_change_g_log,search).select():
                grid.append(data.id)
        #PENDING
        elif str(request.vars['type_L'])=="p":
            if period.period==1:
                if personal_query == '':
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(period.yearp)+'-01-01" and request_change_g_log.date_request<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "pending"'
                else:
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(period.yearp)+'-01-01" and request_change_g_log.date_request<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "pending" and '+personal_query
                for pending in db.smart_query(db.request_change_g_log,search).select():
                    if personal_query == '':
                        search='request_change_g_log.r_c_g_id = "'+str(pending.r_c_g_id)+'" and request_change_g_log.after_status != "pending"'
                    else:
                        search='request_change_g_log.r_c_g_id = "'+str(pending.r_c_g_id)+'" and request_change_g_log.after_status != "pending" and '+personal_query
                    if db.smart_query(db.request_change_g_log,search).select().first() is None:
                        grid.append(pending.id)
            else:
                if personal_query == '':
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(period.yearp)+'-06-01" and request_change_g_log.date_request<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "pending"'
                else:
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(period.yearp)+'-06-01" and request_change_g_log.date_request<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "pending" and '+personal_query
                for pending in db.smart_query(db.request_change_g_log,search).select():
                    if personal_query == '':
                        search='request_change_g_log.r_c_g_id = "'+str(pending.r_c_g_id)+'" and request_change_g_log.after_status != "pending"'
                    else:
                        search='request_change_g_log.r_c_g_id = "'+str(pending.r_c_g_id)+'" and request_change_g_log.after_status != "pending" and '+personal_query
                    if db.smart_query(db.request_change_g_log,search).select().first() is None:
                        grid.append(pending.id)
        #ALL
        elif str(request.vars['type_L'])=="all":
            #MADE AND PENDING
            if period.period==1:
                if personal_query == '':
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(period.yearp)+'-01-01" and request_change_g_log.date_request<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "pending"'
                else:
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(period.yearp)+'-01-01" and request_change_g_log.date_request<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "pending" and '+personal_query
                for pending in db.smart_query(db.request_change_g_log,search).select():
                    if personal_query == '':
                        search='request_change_g_log.r_c_g_id = "'+str(pending.r_c_g_id)+'" and request_change_g_log.after_status != "pending"'
                    else:
                        search='request_change_g_log.r_c_g_id = "'+str(pending.r_c_g_id)+'" and request_change_g_log.after_status != "pending" and '+personal_query
                    if db.smart_query(db.request_change_g_log,search).select().first() is None:
                        grid.append(pending.id)
            else:
                if personal_query == '':
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(period.yearp)+'-06-01" and request_change_g_log.date_request<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "pending"'
                else:
                    search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_request >="'+str(period.yearp)+'-06-01" and request_change_g_log.date_request<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "pending" and '+personal_query
                for pending in db.smart_query(db.request_change_g_log,search).select():
                    if personal_query == '':
                        search='request_change_g_log.r_c_g_id = "'+str(pending.r_c_g_id)+'" and request_change_g_log.after_status != "pending"'
                    else:
                        search='request_change_g_log.r_c_g_id = "'+str(pending.r_c_g_id)+'" and request_change_g_log.after_status != "pending" and '+personal_query
                    if db.smart_query(db.request_change_g_log,search).select().first() is None:
                        grid.append(pending.id)
            #ACCEPTED
            if personal_query == '':
                search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(month[1])+'" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "accepted"'
            else:
                search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(month[1])+'" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "accepted" and '+personal_query
            for data in db.smart_query(db.request_change_g_log,search).select():
                grid.append(data.id)
            #REJECTED
            if personal_query == '':
                search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(month[1])+'" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "rejected"'
            else:
                search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(month[1])+'" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "rejected" and '+personal_query
            for data in db.smart_query(db.request_change_g_log,search).select():
                grid.append(data.id)
            ##CANCELED
            if personal_query == '':
                search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(month[1])+'" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "canceled"'
            else:
                search='request_change_g_log.semester = "'+T(period.period.name)+'" and request_change_g_log.yearp = "'+str(period.yearp)+'" and request_change_g_log.date_operation >="'+str(month[1])+'" and request_change_g_log.date_operation<"'+str(month[2])+'" and request_change_g_log.project = "'+str(project)+'" and request_change_g_log.roll = "Student" and request_change_g_log.username = "'+str(userP)+'" and request_change_g_log.after_status = "canceled" and '+personal_query
            for data in db.smart_query(db.request_change_g_log,search).select():
                grid.append(data.id)

        #TITLE
        infoeLevelTemp=[]
        infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
        infoeLevelTemp.append(str(month[0]))
        infoeLevelTemp.append(project)
        infoeLevelTemp.append(T('Rol Student'))
        infoeLevelTemp.append(str(userP))
        infoLevel.append(infoeLevelTemp)
        #REPORT
        if len(grid) == 0:
            grid.append(-1)
        db.request_change_g_log.id.readable = False
        db.request_change_g_log.id.writable = False
        db.request_change_g_log.username.readable = False
        db.request_change_g_log.username.writable = False
        db.request_change_g_log.roll.readable = False
        db.request_change_g_log.roll.writable = False
        db.request_change_g_log.semester.readable = False
        db.request_change_g_log.semester.writable = False
        db.request_change_g_log.yearp.readable = False
        db.request_change_g_log.yearp.writable = False
        db.request_change_g_log.project.readable = False
        db.request_change_g_log.project.writable = False
        db.request_change_g_log.r_c_g_id.readable = False
        db.request_change_g_log.r_c_g_id.writable = False
        links = [lambda row: A(T('Detail'),
        _role='button', 
        _class= 'btn btn-info', 
        _onclick='set_values("'+str(row.id)+'");', 
        _title=T('View Detail') ,**{"_data-toggle":"modal", "_data-target": "#detailModal"})]
        grid = SQLFORM.grid(db.request_change_g_log.id.belongs(grid), links=links, csv=False, create=False, editable=False, deletable=False, details=False, paginate=9, searchable=False)
    return dict(fsearch=fsearch, filtered_by=filtered_by, personal_query=personal_query, infoLevel=infoLevel, grid=grid) 



#*************************************************************************************************************************************
#*************************************************************************************************************************************
#**************************************************MANAGEMENT REPORT PERFORMANCE OF STUDENTS******************************************
@auth.requires_login()
@auth.requires(auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
def performance_students():
    #************************************************PARAMETERS AND VALIDATION***************************************
    from datetime import datetime
    infoLevel = []
    exist_Laboratory = False
    groupPeriods = None
    project = None
    period = None
    typeFinal = None
    categoriesLevel = []
    try:
        #CHECK THAT THE LEVEL OF REPORT IS VALID
        if request.vars['level'] is not None and (int(request.vars['level'])<1 or int(request.vars['level'])>3):
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #CHECK THAT THE AREA EXIST
        area = db(db.area_level.name=='DTT Tutor Académico').select().first()
        if area is None:
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('default','index'))

        #CHECK IF THE PERIOD IS CHANGE
        if request.vars['period'] is None:
            import cpfecys
            cperiod = cpfecys.current_year_period()
            period = db(db.period_year.id==cperiod.id).select().first()
        else:
            period = VALIDATE_PERIOD(request.vars['period'])
            if period is None:
                session.flash = T('Not valid Action.')
                redirect(URL('default','index'))

        #CHECK PARAMETERS
        if request.vars['level']=='1' or request.vars['level'] is None:
            groupPeriods = db(db.period_year).select(orderby=~db.period_year.id)
            if len(groupPeriods) == 0:
                session.flash = T('Report no visible: There are no parameters required to display the report.')
                redirect(URL('default','index'))

            groupProjects = db(db.project.area_level==area.id).select(orderby=db.project.name)
            if len(groupProjects) == 0:
                session.flash = T('Report no visible: There are no parameters required to display the report.')
                redirect(URL('default','index'))
        else:
            project = db((db.project.id==request.vars['project'])&(db.project.area_level==area.id)).select().first()
            if project is None:
                session.flash = T('Not valid Action.')
                redirect(URL('default','index'))

            if request.vars['level']=='2':
                #CHECK IF THE TYPE OF REPORT IS VALID
                if str(request.vars['type_L'])!="all" and str(request.vars['type_L'])!="i" and str(request.vars['type_L'])!="u"  and str(request.vars['type_L'])!="d":
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))
            elif request.vars['level']=='3':
                #CHECK IF THE TYPE OF THE LEVEL UP OF REPORT IS VALID
                if str(request.vars['type_U'])!="all" and str(request.vars['type_U'])!="i" and str(request.vars['type_U'])!="u"  and str(request.vars['type_U'])!="d":
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))

                #CHECK IF THE TYPE OF REPORT IS VALID
                if str(request.vars['type_L'])!="l_all" and str(request.vars['type_L'])!="l_i" and str(request.vars['type_L'])!="l_u"  and str(request.vars['type_L'])!="l_d" and str(request.vars['type_L'])!="c_all" and str(request.vars['type_L'])!="c_i" and str(request.vars['type_L'])!="c_u"  and str(request.vars['type_L'])!="c_d":
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))

    except:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))


    #*****************************************************REPORT*****************************************************
    #ALL SEMESTERS
    if request.vars['level']=='1' or request.vars['level'] is None:
        #CHECK FOR THE PARAMETERS
        controlP = db(db.student_control_period.period_name==(T(period.period.name)+" "+str(period.yearp))).select().first()
        if controlP is not None:
            #ALL PROJECTS
            for project in groupProjects:
                infoeLevelTemp = []
                #ID OF PROJECT
                infoeLevelTemp.append(project.id)
                #NAME OF PROJECT
                infoeLevelTemp.append(project.name)
                #GRADES ABOVE AVERAGE
                infoeLevelTemp.append(0)
                #GRADES ON THE AVERAGE
                infoeLevelTemp.append(0)
                #GRADES BELOW AVERAGE
                infoeLevelTemp.append(0)

                CourseCategory = db((db.course_activity_category.semester==period.id)&(db.course_activity_category.assignation==project.id)&(db.course_activity_category.laboratory==False)).select()
                if CourseCategory.first() is not None:
                    categoriesClass = []
                    for categories in CourseCategory:
                        if categories.category.category != 'Laboratorio':
                            activityClass = []
                            totalA=0
                            for activity in db(db.course_activity.course_activity_category == categories.id).select():
                                if db(db.grades.activity==activity.id).select().first():
                                    activityClass.append(activity)
                                totalA=totalA+1
                            if len(activityClass)>0:
                                categoriesClass.append([categories,activityClass,totalA])
                        else:
                            categoriesClass.append([categories,0])

                    categoriesLab = []
                    for categories in db((db.course_activity_category.assignation == project.id) &(db.course_activity_category.semester== period.id)&(db.course_activity_category.laboratory==True)).select():
                        activityClass = []
                        totalA=0
                        for activity in db(db.course_activity.course_activity_category == categories.id).select():
                            if db(db.grades.activity==activity.id).select().first():
                                activityClass.append(activity)
                            totalA=totalA+1
                        if len(activityClass)>0:
                            categoriesLab.append([categories,activityClass,totalA])

                    for student in db((db.academic_course_assignation.semester==period.id)&(db.academic_course_assignation.assignation==project.id)).select():
                        totalCarry=float(0)
                        totalFinal=float(0)
                        for categoryClass in categoriesClass:
                            totalCategory=float(0)
                            if categoryClass[0].category.category == 'Examen Final':
                                for c in categoryClass[1]:
                                    studentGrade = db((db.grades.activity==c.id)&(db.grades.academic_assignation==student.id)).select().first()
                                    if studentGrade is not None:
                                        if categoryClass[0].specific_grade==True:
                                            totalFinal=totalFinal+float((studentGrade.grade*c.grade)/100)
                                        else:
                                            totalFinal=totalFinal+float(studentGrade.grade)

                                if categoryClass[0].specific_grade==False:
                                    totalActivities=categoryClass[2]*100
                                    totalFinal=float((totalFinal*float(categoryClass[0].grade))/float(totalActivities))
                                totalFinal=int(round(totalFinal,0))
                            elif categoryClass[0].category.category == 'Laboratorio':
                                validate_laboratory = db((db.validate_laboratory.semester==period.id)&(db.validate_laboratory.project==project.id)&(db.validate_laboratory.carnet==student.id)).select().first()
                                if validate_laboratory is not None:
                                    totalCategory=float((int(round(validate_laboratory.grade,0))*categoryClass[0].grade)/100)
                                else:
                                    totalCarry_Lab=float(0)
                                    if student.laboratorio==True:
                                        for category_Lab in categoriesLab:
                                            totalCategory_Lab=float(0)
                                            for c_Lab in category_Lab[1]:
                                                studentGrade = db((db.grades.activity==c_Lab.id)&(db.grades.academic_assignation==student.id)).select().first()
                                                if studentGrade is not None:
                                                    if category_Lab[0].specific_grade==True:
                                                        totalCategory_Lab=totalCategory_Lab+float((studentGrade.grade*c_Lab.grade)/100)
                                                    else:
                                                        totalCategory_Lab=totalCategory_Lab+float(studentGrade.grade)

                                            if category_Lab[0].specific_grade==False:
                                                totalActivities_Lab=category_Lab[2]*100
                                                totalCategory_Lab=float((totalCategory_Lab*float(category_Lab[0].grade))/float(totalActivities_Lab))
                                            totalCarry_Lab=totalCarry_Lab+totalCategory_Lab
                                    totalCategory=float((int(round(totalCarry_Lab,0))*categoryClass[0].grade)/100)
                                totalCarry=totalCarry+totalCategory
                            else:
                                for c in categoryClass[1]:
                                    studentGrade = db((db.grades.activity==c.id)&(db.grades.academic_assignation==student.id)).select().first()
                                    if studentGrade is not None:
                                        if categoryClass[0].specific_grade==True:
                                            totalCategory=totalCategory+float((studentGrade.grade*c.grade)/100)
                                        else:
                                            totalCategory=totalCategory+float(studentGrade.grade)

                                if categoryClass[0].specific_grade==False:
                                    totalActivities=categoryClass[2]*100
                                    totalCategory=float((totalCategory*float(categoryClass[0].grade))/float(totalActivities))

                                totalCarry=totalCarry+totalCategory
                        totalCarry=int(round(totalCarry,0))+totalFinal
                        if totalCarry<int(controlP.min_average):
                            infoeLevelTemp[4]=infoeLevelTemp[4]+1
                        elif totalCarry>=int(controlP.min_average) and totalCarry<=int(controlP.max_average):
                            infoeLevelTemp[3]=infoeLevelTemp[3]+1
                        else:
                            infoeLevelTemp[2]=infoeLevelTemp[2]+1
                infoLevel.append(infoeLevelTemp)
    #PROJECT
    elif request.vars['level']=='2':
        #CHECK FOR THE PARAMETERS
        controlP = db(db.student_control_period.period_name==(T(period.period.name)+" "+str(period.yearp))).select().first()
        if controlP is not None:
            if str(request.vars['type_L'])=="all":
                infoLevel.append(['c','Clase',0,0,0])
                infoLevel.append(['l','Laboratorio',0,0,0])
            else:
                infoLevel.append(['c','Clase',0])
                infoLevel.append(['l','Laboratorio',0])

            #LABORATORY
            categoriesLab = []
            for categories in db((db.course_activity_category.assignation == project.id) &(db.course_activity_category.semester== period.id)&(db.course_activity_category.laboratory==True)).select():
                activityClass = []
                totalA=0
                for activity in db(db.course_activity.course_activity_category == categories.id).select():
                    if db(db.grades.activity==activity.id).select().first():
                        activityClass.append(activity)
                    totalA=totalA+1
                if len(activityClass)>0:
                    categoriesLab.append([categories,activityClass,totalA])

            #CLASS
            categoriesClass = []
            for categories in db((db.course_activity_category.assignation == project.id) &(db.course_activity_category.semester== period.id)&(db.course_activity_category.laboratory==False)).select():
                if categories.category.category != 'Laboratorio':
                    activityClass = []
                    totalA=0
                    for activity in db(db.course_activity.course_activity_category == categories.id).select():
                        if db(db.grades.activity==activity.id).select().first():
                            activityClass.append(activity)
                        totalA=totalA+1
                    if len(activityClass)>0:
                        categoriesClass.append([categories,activityClass,totalA])
                else:
                    exist_Laboratory=True
                    categoriesClass.append([categories,0])

            #GRADE OF STUDENT
            for student in db((db.academic_course_assignation.semester==period.id)&(db.academic_course_assignation.assignation==project.id)).select():
                #GRADE OF LABORATORY
                grade_Laboratory = int(0)
                validate_laboratory = db((db.validate_laboratory.semester==period.id)&(db.validate_laboratory.project==project.id)&(db.validate_laboratory.carnet==student.id)).select().first()
                if validate_laboratory is None:
                    if student.laboratorio==True:
                        if len(categoriesLab)>0:
                            totalCarry_Lab=float(0)
                            for category_Lab in categoriesLab:
                                totalCategory_Lab=float(0)
                                for c_Lab in category_Lab[1]:
                                    studentGrade = db((db.grades.activity==c_Lab.id)&(db.grades.academic_assignation==student.id)).select().first()
                                    if studentGrade is not None:
                                        if category_Lab[0].specific_grade==True:
                                            totalCategory_Lab=totalCategory_Lab+float((studentGrade.grade*c_Lab.grade)/100)
                                        else:
                                            totalCategory_Lab=totalCategory_Lab+float(studentGrade.grade)

                                if category_Lab[0].specific_grade==False:
                                    totalActivities_Lab=category_Lab[2]*100
                                    totalCategory_Lab=float((totalCategory_Lab*float(category_Lab[0].grade))/float(totalActivities_Lab))
                                totalCarry_Lab=totalCarry_Lab+totalCategory_Lab
                            grade_Laboratory=int(round(totalCarry_Lab,0))
                            if grade_Laboratory<int(controlP.min_average):
                                if str(request.vars['type_L'])=="all":
                                    infoLevel[1][4]=infoLevel[1][4]+1
                                elif str(request.vars['type_L'])=="d":
                                    infoLevel[1][2]=infoLevel[1][2]+1
                            elif grade_Laboratory>=int(controlP.min_average) and grade_Laboratory<=int(controlP.max_average):
                                if str(request.vars['type_L'])=="all":
                                    infoLevel[1][3]=infoLevel[1][3]+1
                                elif str(request.vars['type_L'])=="u":
                                    infoLevel[1][2]=infoLevel[1][2]+1
                            else:
                                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                                    infoLevel[1][2]=infoLevel[1][2]+1
                else:
                    grade_Laboratory=int(round(validate_laboratory.grade,0))
                
                #GRADE OF CLASS
                totalCarry=float(0)
                totalFinal=float(0)
                if len(categoriesClass)>0:
                    for categoryClass in categoriesClass:
                        totalCategory=float(0)
                        if categoryClass[0].category.category == 'Examen Final':
                            for c in categoryClass[1]:
                                studentGrade = db((db.grades.activity==c.id)&(db.grades.academic_assignation==student.id)).select().first()
                                if studentGrade is not None:
                                    if categoryClass[0].specific_grade==True:
                                        totalFinal=totalFinal+float((studentGrade.grade*c.grade)/100)
                                    else:
                                        totalFinal=totalFinal+float(studentGrade.grade)

                            if categoryClass[0].specific_grade==False:
                                totalActivities=categoryClass[2]*100
                                totalFinal=float((totalFinal*float(categoryClass[0].grade))/float(totalActivities))
                            totalFinal=int(round(totalFinal,0))
                        elif categoryClass[0].category.category == 'Laboratorio':
                            totalCategory=float((grade_Laboratory*categoryClass[0].grade)/100)
                            totalCarry=totalCarry+totalCategory
                        else:
                            for c in categoryClass[1]:
                                studentGrade = db((db.grades.activity==c.id)&(db.grades.academic_assignation==student.id)).select().first()
                                if studentGrade is not None:
                                    if categoryClass[0].specific_grade==True:
                                        totalCategory=totalCategory+float((studentGrade.grade*c.grade)/100)
                                    else:
                                        totalCategory=totalCategory+float(studentGrade.grade)

                            if categoryClass[0].specific_grade==False:
                                totalActivities=categoryClass[2]*100
                                totalCategory=float((totalCategory*float(categoryClass[0].grade))/float(totalActivities))

                            totalCarry=totalCarry+totalCategory
                    totalCarry=int(round(totalCarry,0))+totalFinal
                    if totalCarry<int(controlP.min_average):
                        if str(request.vars['type_L'])=="all":
                            infoLevel[0][4]=infoLevel[0][4]+1
                        elif str(request.vars['type_L'])=="d":
                            infoLevel[0][2]=infoLevel[0][2]+1
                    elif totalCarry>=int(controlP.min_average) and totalCarry<=int(controlP.max_average):
                        if str(request.vars['type_L'])=="all":
                            infoLevel[0][3]=infoLevel[0][3]+1
                        elif str(request.vars['type_L'])=="u":
                            infoLevel[0][2]=infoLevel[0][2]+1
                    else:
                        if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                            infoLevel[0][2]=infoLevel[0][2]+1
    #TYPE FOR PROJECT
    elif request.vars['level']=='3':
        #CHECK FOR THE PARAMETERS
        controlP = db(db.student_control_period.period_name==(T(period.period.name)+" "+str(period.yearp))).select().first()
        if controlP is not None:
            type_Level = str(request.vars['type_L']).split('_')
            #LABORATORY
            if type_Level[0]=='l' or type_Level[0]=='c':
                typeFinal = 'Laboratorio'
                categoriesLab = []
                for categories in db((db.course_activity_category.assignation == project.id) &(db.course_activity_category.semester== period.id)&(db.course_activity_category.laboratory==True)).select():
                    activityClass = []
                    totalA=0
                    for activity in db(db.course_activity.course_activity_category == categories.id).select():
                        activityClass.append(activity)
                        totalA=totalA+1
                    categoriesLab.append([categories,activityClass,totalA])

            #CLASS
            if type_Level[0]=='c':
                typeFinal = 'Clase'
                categoriesClass = []
                for categories in db((db.course_activity_category.assignation == project.id) &(db.course_activity_category.semester== period.id)&(db.course_activity_category.laboratory==False)).select():
                    if categories.category.category != 'Laboratorio':
                        activityClass = []
                        totalA=0
                        for activity in db(db.course_activity.course_activity_category == categories.id).select():
                            activityClass.append(activity)
                            totalA=totalA+1
                        categoriesClass.append([categories,activityClass,totalA])
                    else:
                        categoriesClass.append([categories,0])

            #GRADE OF STUDENT
            for student in db((db.academic_course_assignation.semester==period.id)&(db.academic_course_assignation.assignation==project.id)).select():
                grade_Laboratory = int(0)
                totalCarry=float(0)
                totalFinal=float(0)

                #GRADE OF LABORATORY
                validate_laboratory = db((db.validate_laboratory.semester==period.id)&(db.validate_laboratory.project==project.id)&(db.validate_laboratory.carnet==student.id)).select().first()
                if validate_laboratory is None:
                    if student.laboratorio==True:
                        if len(categoriesLab)>0:
                            totalCarry_Lab=float(0)
                            for category_Lab in categoriesLab:
                                totalCategory_Lab=float(0)
                                for c_Lab in category_Lab[1]:
                                    studentGrade = db((db.grades.activity==c_Lab.id)&(db.grades.academic_assignation==student.id)).select().first()
                                    if studentGrade is not None:
                                        if category_Lab[0].specific_grade==True:
                                            totalCategory_Lab=totalCategory_Lab+float((studentGrade.grade*c_Lab.grade)/100)
                                        else:
                                            totalCategory_Lab=totalCategory_Lab+float(studentGrade.grade)

                                if category_Lab[0].specific_grade==False:
                                    totalActivities_Lab=category_Lab[2]*100
                                    totalCategory_Lab=float((totalCategory_Lab*float(category_Lab[0].grade))/float(totalActivities_Lab))
                                totalCarry_Lab=totalCarry_Lab+totalCategory_Lab
                            grade_Laboratory=int(round(totalCarry_Lab,0))
                else:
                    grade_Laboratory=int(round(validate_laboratory.grade,0))
                

                #GRADE OF CLASS
                if type_Level[0]=='c':
                    for categoryClass in categoriesClass:
                        totalCategory=float(0)
                        if categoryClass[0].category.category == 'Examen Final':
                            for c in categoryClass[1]:
                                studentGrade = db((db.grades.activity==c.id)&(db.grades.academic_assignation==student.id)).select().first()
                                if studentGrade is not None:
                                    if categoryClass[0].specific_grade==True:
                                        totalFinal=totalFinal+float((studentGrade.grade*c.grade)/100)
                                    else:
                                        totalFinal=totalFinal+float(studentGrade.grade)

                            if categoryClass[0].specific_grade==False:
                                totalActivities=categoryClass[2]*100
                                totalFinal=float((totalFinal*float(categoryClass[0].grade))/float(totalActivities))
                            totalFinal=int(round(totalFinal,0))
                        elif categoryClass[0].category.category == 'Laboratorio':
                            totalCategory=float((grade_Laboratory*categoryClass[0].grade)/100)
                            totalCarry=totalCarry+totalCategory
                        else:
                            for c in categoryClass[1]:
                                studentGrade = db((db.grades.activity==c.id)&(db.grades.academic_assignation==student.id)).select().first()
                                if studentGrade is not None:
                                    if categoryClass[0].specific_grade==True:
                                        totalCategory=totalCategory+float((studentGrade.grade*c.grade)/100)
                                    else:
                                        totalCategory=totalCategory+float(studentGrade.grade)

                            if categoryClass[0].specific_grade==False:
                                totalActivities=categoryClass[2]*100
                                totalCategory=float((totalCategory*float(categoryClass[0].grade))/float(totalActivities))

                            totalCarry=totalCarry+totalCategory
                    totalCarry=int(round(totalCarry,0))+totalFinal
    return dict(groupPeriods=groupPeriods, period=period, project = project, infoLevel=infoLevel, exist_Laboratory=exist_Laboratory, typeFinal=typeFinal, categoriesLevel=categoriesLevel)