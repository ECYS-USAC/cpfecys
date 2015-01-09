#*************************************************************************************************************************************
#*************************************************************************************************************************************
#*****************************************************FEATURES EXTRAS FOR REPORTS*****************************************************
#???????????????????????????????????????????????????????????
#VALIDATE REPORT
@auth.requires_login()
@auth.requires_membership('Super-Administrator')
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
@auth.requires_membership('Super-Administrator')
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
@auth.requires_membership('Super-Administrator')
def VALIDATE_PERIOD(period):
    try:
        period = db(db.period_year.id==int(period)).select().first()
        return period
    except:
        return None


@auth.requires_login()
@auth.requires_membership('Super-Administrator')
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
@auth.requires_membership('Super-Administrator')
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
            else:
                roll=None
        else:
            roll=roll.role

        #RETURN ROLE
        return roll
    except:
        return None


@auth.requires_login()
@auth.requires_membership('Super-Administrator')
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
                projectT = db(db.project.name==project).select().first()
                if projectT is not None:
                    userP=db((db.auth_membership.group_id==rollT.id)&(db.auth_membership.user_id==db.auth_user.id)&(db.auth_user.username==idUser)&(db.auth_user.id==db.user_project.assigned_user)&(db.user_project.project==projectT.id)&(db.user_project.period == db.period_year.id)&((db.user_project.period <= period.id) & ((db.user_project.period + db.user_project.periods) > period.id))).select(db.auth_user.ALL).first()
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
            else:
                userP = None
        return userP
    except:
        return None


#???????????????????????????????????????????????????????????
#GROUP OF INFORMATION
@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def GET_YEARS():
    years = []
    for period in db(db.period_year).select(db.period_year.yearp,distinct=True):
        years.append(period.yearp)
    return years


@auth.requires_login()
@auth.requires_membership('Super-Administrator')
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
    else:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    return projects


@auth.requires_login()
@auth.requires_membership('Super-Administrator')
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
    else:
        session.flash = T('Not valid Action.')+'2'
        redirect(URL('default','index'))
    return roles


@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def GET_USERS(period,project,roll,typeReport):
    usersProject=[]
    #OFFICIAL USERS
    rollT = db((db.auth_group.role==roll)&(db.auth_group.role!='Academic')&(db.auth_group.role!='DSI')).select().first()
    if rollT is not None:
        if roll=='Super-Administrator' or roll=='Ecys-Administrator':
            for userT in db((db.auth_user.id==db.auth_membership.user_id)&(db.auth_membership.group_id==rollT.id)).select(db.auth_user.ALL):
                usersProject.append(userT.username)
        else:
            projectT = db(db.project.name==project).select().first()
            if projectT is not None:
                for userT in db((db.auth_membership.group_id==rollT.id)&(db.auth_membership.user_id==db.auth_user.id)&(db.auth_user.id==db.user_project.assigned_user)&(db.user_project.project==projectT.id)&(db.user_project.period == db.period_year.id)&((db.user_project.period <= period.id) & ((db.user_project.period + db.user_project.periods) > period.id))).select(db.auth_user.ALL):
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
    else:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    return usersProject


@auth.requires_login()
@auth.requires_membership('Super-Administrator')
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
    else:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    return categories


@auth.requires_login()
@auth.requires_membership('Super-Administrator')
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
    else:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    return activities


@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def GET_DESCRIPTIONS(typeReport):
    descriptions = []
    #ROLES IN LOGS
    if typeReport == 'grades_log':
        for description in db(db.grades_log).select(db.grades_log.description, distinct=True):
            descriptions.append(description.description)
    else:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    return descriptions


@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def GET_DATES(typeReport):
    dates = []
    #ROLES IN LOGS
    if typeReport == 'grades_log':
        for dat in db(db.grades_log).select(db.grades_log.date_log, distinct=True):
            dates.append(dat.date_log)
    elif typeReport == 'course_activity_log':
        for dat in db(db.course_activity_log).select(db.course_activity_log.date_log, distinct=True):
            dates.append(dat.date_log)
    else:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    return dates
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
        if request.vars['level'] is not None and (int(request.vars['level'])<1 and int(request.vars['level'])>6):
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
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "insert" and grades_log.date_log >="'+str(start)+'" and grades_log.date_log<="'+str(end)+'"'
                else:
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "insert" and grades_log.date_log >="'+str(start)+'" and grades_log.date_log<="'+str(end)+'" and '+personal_query
                countI = db.smart_query(db.grades_log,search).count()
                infoeLevelTemp.append(countI)
            #UPDATE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "update" and grades_log.date_log>="'+str(start)+'" and grades_log.date_log<="'+str(end)+'"'
                else:
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "update" and grades_log.date_log>="'+str(start)+'" and grades_log.date_log<="'+str(end)+'" and '+personal_query
                countI = db.smart_query(db.grades_log,search).count()
                infoeLevelTemp.append(countI)
            #DELETE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "delete" and grades_log.date_log>="'+str(start)+'" and grades_log.date_log<="'+str(end)+'"'
                else:
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "delete" and grades_log.date_log>="'+str(start)+'" and grades_log.date_log<="'+str(end)+'" and '+personal_query
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
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "insert" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+project+'"'
                else:
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "insert" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+project+'" and '+personal_query
                countI = db.smart_query(db.grades_log,search).count()
                infoeLevelTemp.append(countI)
            #UPDATE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "update" and grades_log.date_log>="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+project+'"'
                else:
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "update" and grades_log.date_log>="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+project+'" and '+personal_query
                countI = db.smart_query(db.grades_log,search).count()
                infoeLevelTemp.append(countI)
            #DELETE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "delete" and grades_log.date_log>="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+project+'"'
                else:
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "delete" and grades_log.date_log>="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+project+'" and '+personal_query
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
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "insert" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'"'
                else:
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "insert" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and '+personal_query
                countI = db.smart_query(db.grades_log,search).count()
                infoeLevelTemp.append(countI)
            #UPDATE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "update" and grades_log.date_log>="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'"'
                else:
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "update" and grades_log.date_log>="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and '+personal_query
                countI = db.smart_query(db.grades_log,search).count()
                infoeLevelTemp.append(countI)
            #DELETE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "delete" and grades_log.date_log>="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'"'
                else:
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "delete" and grades_log.date_log>="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and '+personal_query
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
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "insert" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'"'
                else:
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "insert" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'" and '+personal_query
                countI = db.smart_query(db.grades_log,search).count()
                infoeLevelTemp.append(countI)
            #UPDATE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "update" and grades_log.date_log>="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'"'
                else:
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "update" and grades_log.date_log>="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'" and '+personal_query
                countI = db.smart_query(db.grades_log,search).count()
                infoeLevelTemp.append(countI)
            #DELETE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "delete" and grades_log.date_log>="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'"'
                else:
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "delete" and grades_log.date_log>="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'" and '+personal_query
                countI = db.smart_query(db.grades_log,search).count()
                infoeLevelTemp.append(countI)
            #INSERT PROJECT
            infoLevel.append(infoeLevelTemp)
    #DATA
    elif str(request.vars['level'])=="6":
        #DATA
        if str(request.vars['type_L'])=="all":
            if personal_query == '':
                search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'"'
            else:
                search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'" and '+personal_query
        elif str(request.vars['type_L'])=="i":
            if personal_query == '':
                search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "insert" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'"'
            else:
                search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "insert" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'" and '+personal_query
        elif str(request.vars['type_L'])=="u":
            if personal_query == '':
                search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "update" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'"'
            else:
                search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "update" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'" and '+personal_query
        elif str(request.vars['type_L'])=="d":
            if personal_query == '':
                search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "delete" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'"'
            else:
                search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "delete" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'" and '+personal_query
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
        infoeLevelTemp.append(T('Log'))
        infoeLevelTemp.append(T('Description')+' '+T('Log'))
        infoeLevelTemp.append(T('Category'))
        infoeLevelTemp.append(T('Activity'))
        infoeLevelTemp.append(T('Student'))
        infoeLevelTemp.append(T('Before Grade'))
        infoeLevelTemp.append(T('Grade'))
        infoLevel.append(infoeLevelTemp)
        for operation in db.smart_query(db.grades_log,search).select():
            infoeLevelTemp=[]
            infoeLevelTemp.append(operation.date_log)
            infoeLevelTemp.append(operation.description)
            infoeLevelTemp.append(operation.category)
            infoeLevelTemp.append(operation.activity)
            infoeLevelTemp.append(operation.academic)
            infoeLevelTemp.append(operation.before_grade)
            infoeLevelTemp.append(operation.after_grade)
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
    if request.vars['querySearch'] is not None and str(request.vars['querySearch']) != "":
        #PERSONALIZED QUERY SURE WORK
        try:
            personal_query = str(request.vars['querySearch'])
            countI = db.smart_query(db.grades_log,personal_query).count()
        except:
            response.flash = T('The query is not valid. The report is displayed without applying any query.')
            personal_query = ''


    #****************************************************************************************************************
    #****************************************************************************************************************
    #******************************************VERIFY THAT ACCURATE PARAMETERS***************************************
    try:
        #CHECK THAT THE LEVEL OF REPORT IS VALID
        if request.vars['level'] is not None and (int(request.vars['level'])<1 and int(request.vars['level'])>6):
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
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "insert" and grades_log.date_log >="'+str(start)+'" and grades_log.date_log<="'+str(end)+'"'
                else:
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "insert" and grades_log.date_log >="'+str(start)+'" and grades_log.date_log<="'+str(end)+'" and '+personal_query
                countI = db.smart_query(db.grades_log,search).count()
                infoeLevelTemp.append(countI)
            #UPDATE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "update" and grades_log.date_log>="'+str(start)+'" and grades_log.date_log<="'+str(end)+'"'
                else:
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "update" and grades_log.date_log>="'+str(start)+'" and grades_log.date_log<="'+str(end)+'" and '+personal_query
                countI = db.smart_query(db.grades_log,search).count()
                infoeLevelTemp.append(countI)
            #DELETE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "delete" and grades_log.date_log>="'+str(start)+'" and grades_log.date_log<="'+str(end)+'"'
                else:
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "delete" and grades_log.date_log>="'+str(start)+'" and grades_log.date_log<="'+str(end)+'" and '+personal_query
                countI = db.smart_query(db.grades_log,search).count()
                infoeLevelTemp.append(countI)
            #INSERT MONTH
            infoLevel.append(infoeLevelTemp)
    #PER PROJECT
    elif str(request.vars['level'])=="3":
        if len(projects) == 0:
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('management_reports', 'grades_management',vars=dict(list='level',level='2',period = str(request.vars['period']), type_L = str(request.vars['type_U']), querySearch=personal_query)))
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
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "insert" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+project+'"'
                else:
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "insert" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+project+'" and '+personal_query
                countI = db.smart_query(db.grades_log,search).count()
                infoeLevelTemp.append(countI)
            #UPDATE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "update" and grades_log.date_log>="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+project+'"'
                else:
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "update" and grades_log.date_log>="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+project+'" and '+personal_query
                countI = db.smart_query(db.grades_log,search).count()
                infoeLevelTemp.append(countI)
            #DELETE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "delete" and grades_log.date_log>="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+project+'"'
                else:
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "delete" and grades_log.date_log>="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+project+'" and '+personal_query
                countI = db.smart_query(db.grades_log,search).count()
                infoeLevelTemp.append(countI)
            #INSERT PROJECT
            infoLevel.append(infoeLevelTemp)

        #TOP 5 OF PROJECT
        if personal_query == '':
            search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'"'
        else:
            search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and '+personal_query
        top5 = db.smart_query(db.grades_log,search).select(db.grades_log.project, db.grades_log.id.count(), orderby=~db.grades_log.id.count(), limitby=(0, 5), groupby=db.grades_log.project)
    #PER ROL
    elif str(request.vars['level'])=="4":
        if len(roles) == 0:
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('management_reports', 'grades_management',vars=dict(list='level',level='3', period = str(request.vars['period']), month = str(request.vars['month']), type_L = str(request.vars['type_U']), type_U = str(request.vars['type_U']), querySearch=personal_query)))

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
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "insert" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'"'
                else:
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "insert" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and '+personal_query
                countI = db.smart_query(db.grades_log,search).count()
                infoeLevelTemp.append(countI)
            #UPDATE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "update" and grades_log.date_log>="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'"'
                else:
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "update" and grades_log.date_log>="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and '+personal_query
                countI = db.smart_query(db.grades_log,search).count()
                infoeLevelTemp.append(countI)
            #DELETE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "delete" and grades_log.date_log>="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'"'
                else:
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "delete" and grades_log.date_log>="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and '+personal_query
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
            redirect(URL('management_reports', 'grades_management',vars=dict(list='level',level='4', period = str(request.vars['period']), month = str(request.vars['month']), project = str(request.vars['project']), type_L = str(request.vars['type_U']), type_U = str(request.vars['type_U']), querySearch=personal_query)))

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
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "insert" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'"'
                else:
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "insert" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'" and '+personal_query
                countI = db.smart_query(db.grades_log,search).count()
                infoeLevelTemp.append(countI)
            #UPDATE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "update" and grades_log.date_log>="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'"'
                else:
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "update" and grades_log.date_log>="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'" and '+personal_query
                countI = db.smart_query(db.grades_log,search).count()
                infoeLevelTemp.append(countI)
            #DELETE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "delete" and grades_log.date_log>="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'"'
                else:
                    search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "delete" and grades_log.date_log>="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'" and '+personal_query
                countI = db.smart_query(db.grades_log,search).count()
                infoeLevelTemp.append(countI)
            #INSERT PROJECT
            infoLevel.append(infoeLevelTemp)
    #DATA
    elif str(request.vars['level'])=="6":
        if str(request.vars['type_L'])=="all":
            if personal_query == '':
                search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'"'
            else:
                search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'" and '+personal_query
        elif str(request.vars['type_L'])=="i":
            if personal_query == '':
                search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "insert" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'"'
            else:
                search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "insert" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'" and '+personal_query
        elif str(request.vars['type_L'])=="u":
            if personal_query == '':
                search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "update" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'"'
            else:
                search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "update" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'" and '+personal_query
        elif str(request.vars['type_L'])=="d":
            if personal_query == '':
                search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "delete" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'"'
            else:
                search='grades_log.period = "'+T(period.period.name)+'" and grades_log.yearp = "'+str(period.yearp)+'" and grades_log.operation_log = "delete" and grades_log.date_log >="'+str(month[1])+'" and grades_log.date_log<="'+str(month[2])+'" and grades_log.project ="'+str(project)+'" and grades_log.roll ="'+str(roll)+'" and grades_log.user_name ="'+str(userP)+'" and '+personal_query
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
        grid=SQLFORM.smartgrid(db.grades_log, constraints = dict(grades_log=search), csv=False, create=False, editable=False, deletable=False, paginate=9, searchable=False)
    return dict(fsearch=fsearch, filtered_by=filtered_by, personal_query=personal_query, infoLevel=infoLevel, top5=top5, grid=grid) 


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
        if request.vars['level'] is not None and (int(request.vars['level'])<1 and int(request.vars['level'])>6):
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
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "insert" and course_activity_log.date_log >="'+str(start)+'" and course_activity_log.date_log<="'+str(end)+'"'
                else:
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "insert" and course_activity_log.date_log >="'+str(start)+'" and course_activity_log.date_log<="'+str(end)+'" and '+personal_query
                countI = db.smart_query(db.course_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #UPDATE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "update" and course_activity_log.date_log>="'+str(start)+'" and course_activity_log.date_log<="'+str(end)+'"'
                else:
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "update" and course_activity_log.date_log>="'+str(start)+'" and course_activity_log.date_log<="'+str(end)+'" and '+personal_query
                countI = db.smart_query(db.course_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #DELETE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "delete" and course_activity_log.date_log>="'+str(start)+'" and course_activity_log.date_log<="'+str(end)+'"'
                else:
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "delete" and course_activity_log.date_log>="'+str(start)+'" and course_activity_log.date_log<="'+str(end)+'" and '+personal_query
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
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "insert" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+project+'"'
                else:
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "insert" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+project+'" and '+personal_query
                countI = db.smart_query(db.course_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #UPDATE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "update" and course_activity_log.date_log>="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+project+'"'
                else:
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "update" and course_activity_log.date_log>="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+project+'" and '+personal_query
                countI = db.smart_query(db.course_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #DELETE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "delete" and course_activity_log.date_log>="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+project+'"'
                else:
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "delete" and course_activity_log.date_log>="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+project+'" and '+personal_query
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
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "insert" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'"'
                else:
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "insert" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and '+personal_query
                countI = db.smart_query(db.course_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #UPDATE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "update" and course_activity_log.date_log>="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'"'
                else:
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "update" and course_activity_log.date_log>="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and '+personal_query
                countI = db.smart_query(db.course_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #DELETE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "delete" and course_activity_log.date_log>="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'"'
                else:
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "delete" and course_activity_log.date_log>="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and '+personal_query
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
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "insert" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'"'
                else:
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "insert" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'" and '+personal_query
                countI = db.smart_query(db.course_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #UPDATE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "update" and course_activity_log.date_log>="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'"'
                else:
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "update" and course_activity_log.date_log>="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'" and '+personal_query
                countI = db.smart_query(db.course_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #DELETE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "delete" and course_activity_log.date_log>="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'"'
                else:
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "delete" and course_activity_log.date_log>="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'" and '+personal_query
                countI = db.smart_query(db.course_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #INSERT PROJECT
            infoLevel.append(infoeLevelTemp)
    #DATA
    elif str(request.vars['level'])=="6":
        if str(request.vars['type_L'])=="all":
            if personal_query == '':
                search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'"'
            else:
                search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'" and '+personal_query
        elif str(request.vars['type_L'])=="i":
            if personal_query == '':
                search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "insert" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'"'
            else:
                search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "insert" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'" and '+personal_query
        elif str(request.vars['type_L'])=="u":
            if personal_query == '':
                search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "update" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'"'
            else:
                search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "update" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'" and '+personal_query
        elif str(request.vars['type_L'])=="d":
            if personal_query == '':
                search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "delete" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'"'
            else:
                search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "delete" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'" and '+personal_query
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
    if request.vars['querySearch'] is not None and str(request.vars['querySearch']) != "":
        #PERSONALIZED QUERY SURE WORK
        try:
            personal_query = str(request.vars['querySearch'])
            countI = db.smart_query(db.course_activity_log,personal_query).count()
        except:
            response.flash = T('The query is not valid. The report is displayed without applying any query.')
            personal_query = ''


    #****************************************************************************************************************
    #****************************************************************************************************************
    #******************************************VERIFY THAT ACCURATE PARAMETERS***************************************
    try:
        #CHECK THAT THE LEVEL OF REPORT IS VALID
        if request.vars['level'] is not None and (int(request.vars['level'])<1 and int(request.vars['level'])>6):
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
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "insert" and course_activity_log.date_log >="'+str(start)+'" and course_activity_log.date_log<="'+str(end)+'"'
                else:
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "insert" and course_activity_log.date_log >="'+str(start)+'" and course_activity_log.date_log<="'+str(end)+'" and '+personal_query
                countI = db.smart_query(db.course_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #UPDATE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "update" and course_activity_log.date_log>="'+str(start)+'" and course_activity_log.date_log<="'+str(end)+'"'
                else:
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "update" and course_activity_log.date_log>="'+str(start)+'" and course_activity_log.date_log<="'+str(end)+'" and '+personal_query
                countI = db.smart_query(db.course_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #DELETE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "delete" and course_activity_log.date_log>="'+str(start)+'" and course_activity_log.date_log<="'+str(end)+'"'
                else:
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "delete" and course_activity_log.date_log>="'+str(start)+'" and course_activity_log.date_log<="'+str(end)+'" and '+personal_query
                countI = db.smart_query(db.course_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #INSERT MONTH
            infoLevel.append(infoeLevelTemp)
    #PER PROJECT
    elif str(request.vars['level'])=="3":
        if len(projects) == 0:
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('management_reports', 'activities_withmetric_management',vars=dict(list='level',level='2',period = str(request.vars['period']), type_L = str(request.vars['type_U']), querySearch=personal_query)))
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
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "insert" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+project+'"'
                else:
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "insert" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+project+'" and '+personal_query
                countI = db.smart_query(db.course_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #UPDATE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "update" and course_activity_log.date_log>="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+project+'"'
                else:
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "update" and course_activity_log.date_log>="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+project+'" and '+personal_query
                countI = db.smart_query(db.course_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #DELETE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "delete" and course_activity_log.date_log>="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+project+'"'
                else:
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "delete" and course_activity_log.date_log>="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+project+'" and '+personal_query
                countI = db.smart_query(db.course_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #INSERT PROJECT
            infoLevel.append(infoeLevelTemp)

        #TOP 5 OF PROJECT
        if personal_query == '':
            search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'"'
        else:
            search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and '+personal_query
        top5 = db.smart_query(db.course_activity_log,search).select(db.course_activity_log.course, db.course_activity_log.id.count(), orderby=~db.course_activity_log.id.count(), limitby=(0, 5), groupby=db.course_activity_log.course)
    #PER ROL
    elif str(request.vars['level'])=="4":
        if len(roles) == 0:
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('management_reports', 'activities_withmetric_management',vars=dict(list='level',level='3', period = str(request.vars['period']), month = str(request.vars['month']), type_L = str(request.vars['type_U']), type_U = str(request.vars['type_U']), querySearch=personal_query)))

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
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "insert" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'"'
                else:
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "insert" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and '+personal_query
                countI = db.smart_query(db.course_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #UPDATE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "update" and course_activity_log.date_log>="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'"'
                else:
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "update" and course_activity_log.date_log>="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and '+personal_query
                countI = db.smart_query(db.course_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #DELETE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "delete" and course_activity_log.date_log>="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'"'
                else:
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "delete" and course_activity_log.date_log>="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and '+personal_query
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
            redirect(URL('management_reports', 'activities_withmetric_management',vars=dict(list='level',level='4', period = str(request.vars['period']), month = str(request.vars['month']), project = str(request.vars['project']), type_L = str(request.vars['type_U']), type_U = str(request.vars['type_U']), querySearch=personal_query)))

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
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "insert" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'"'
                else:
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "insert" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'" and '+personal_query
                countI = db.smart_query(db.course_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #UPDATE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                if personal_query == '':
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "update" and course_activity_log.date_log>="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'"'
                else:
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "update" and course_activity_log.date_log>="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'" and '+personal_query
                countI = db.smart_query(db.course_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #DELETE
            if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                if personal_query == '':
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "delete" and course_activity_log.date_log>="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'"'
                else:
                    search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "delete" and course_activity_log.date_log>="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'" and '+personal_query
                countI = db.smart_query(db.course_activity_log,search).count()
                infoeLevelTemp.append(countI)
            #INSERT PROJECT
            infoLevel.append(infoeLevelTemp)
    #DATA
    elif str(request.vars['level'])=="6":
        if str(request.vars['type_L'])=="all":
            if personal_query == '':
                search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'"'
            else:
                search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'" and '+personal_query
        elif str(request.vars['type_L'])=="i":
            if personal_query == '':
                search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "insert" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'"'
            else:
                search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "insert" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'" and '+personal_query
        elif str(request.vars['type_L'])=="u":
            if personal_query == '':
                search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "update" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'"'
            else:
                search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "update" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'" and '+personal_query
        elif str(request.vars['type_L'])=="d":
            if personal_query == '':
                search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "delete" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'"'
            else:
                search='course_activity_log.period = "'+T(period.period.name)+'" and course_activity_log.yearp = "'+str(period.yearp)+'" and course_activity_log.operation_log = "delete" and course_activity_log.date_log >="'+str(month[1])+'" and course_activity_log.date_log<="'+str(month[2])+'" and course_activity_log.course ="'+str(project)+'" and course_activity_log.roll ="'+str(roll)+'" and course_activity_log.user_name ="'+str(userP)+'" and '+personal_query
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
        grid=SQLFORM.smartgrid(db.course_activity_log, constraints = dict(course_activity_log=search), csv=False, create=False, editable=False, deletable=False, paginate=9, searchable=False)
    return dict(fsearch=fsearch, filtered_by=filtered_by, personal_query=personal_query, infoLevel=infoLevel, top5=top5, grid=grid)
