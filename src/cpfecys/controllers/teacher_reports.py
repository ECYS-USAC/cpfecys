#*************************************************************************************************************************************
#*************************************************************************************************************************************
#*****************************************************FEATURES EXTRAS FOR REPORTS*****************************************************
#???????????????????????????????????????????????????????????
#VALIDATE REPORT
@auth.requires_login()
@auth.requires(auth.has_membership('Teacher'))
def GET_MONTH_PERIOD():
    import cpfecys
    year = cpfecys.current_year_period()
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
@auth.requires(auth.has_membership('Teacher'))
def VALIDATE_MONTH(month):
    import cpfecys
    period = cpfecys.current_year_period()
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
@auth.requires(auth.has_membership('Teacher'))
def VALIDATE_PROJECT(projectI,typeReport):
    import cpfecys
    period = cpfecys.current_year_period()
    try:
        #CHECK IN THE LOG IF THE PROJECT EXIST
        project=db((db.user_project.assigned_user==auth.user.id)&(db.user_project.project==projectI)&((db.user_project.period <= period.id) & ((db.user_project.period + db.user_project.periods) > period.id))).select().first()
        project = db(db.project.id==project.project).select().first()
        return project
    except:
        return None


@auth.requires_login()
@auth.requires(auth.has_membership('Teacher'))
def VALIDATE_ROLE(nameRole,typeReport):
    import cpfecys
    period = cpfecys.current_year_period()
    try:
        #CHECK IF THE ROLE EXIST IN THE OFFICIAL ROLES
        roll = db((db.auth_group.role==nameRole)&(db.auth_group.role!='Academic')&(db.auth_group.role!='DSI')).select().first()
        if roll is None:
            #CHECK IF THE ROLE EXIT IN THE LOGS OF SYSTEM 
            if typeReport=='grades_log':
                roll = db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.roll==nameRole)&(db.grades_log.roll!='Academic')&(db.grades_log.roll!='DSI')).select().first()
                if roll is not None:
                    roll=roll.roll
            elif typeReport == 'validate_laboratory_log':
                roll = db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.roll==nameRole)&(db.validate_laboratory_log.roll!='Academic')&(db.validate_laboratory_log.roll!='DSI')).select().first()
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
@auth.requires(auth.has_membership('Teacher'))
def VALIDATE_USER(project,roll,idUser,typeReport):
    import cpfecys
    period = cpfecys.current_year_period()
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
                userP=db((db.auth_membership.group_id==rollT.id)&(db.auth_membership.user_id==db.auth_user.id)&(db.auth_user.username==idUser)&(db.auth_user.id==db.user_project.assigned_user)&(db.user_project.project==project.id)&(db.user_project.period == db.period_year.id)&((db.user_project.period <= period.id) & ((db.user_project.period + db.user_project.periods) > period.id))).select(db.auth_user.ALL).first()
                if userP is not None:
                    userP=userP.username

        
        #CHECK IF THE ROLE EXIT IN THE LOGS OF SYSTEM 
        if userP is None:
            if typeReport=='grades_log':
                userP = db((db.grades_log.project==project.name)&(db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.roll==roll)&(db.grades_log.user_name==idUser)).select().first()
                if userP is not None:
                    userP=userP.user_name
            elif typeReport =='validate_laboratory_log':
                userP = db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.roll==roll)&(db.validate_laboratory_log.user_name==idUser)).select().first()
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
@auth.requires(auth.has_membership('Teacher'))
def GET_ROLES(typeReport):
    import cpfecys
    period = cpfecys.current_year_period()
    roles=[]
    #OFFICIAL ROLES
    for roll in db((db.auth_group.role!='Academic')&(db.auth_group.role!='DSI')).select(db.auth_group.role.with_alias('roll'), distinct=True):
        roles.append(roll.roll)

    #ROLES IN LOGS
    if typeReport == 'grades_log':
        if len(roles) == 0:
            rolesTemp = db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.roll!='Academic')&(db.grades_log.roll!='DSI')).select(db.grades_log.roll.with_alias('roll'), distinct=True)
        else:
            rolesTemp = db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(~db.grades_log.roll.belongs(roles))&(db.grades_log.roll!='Academic')&(db.grades_log.roll!='DSI')).select(db.grades_log.roll.with_alias('roll'), distinct=True)
        for roll in rolesTemp:
            roles.append(roll.roll)
    elif typeReport =='validate_laboratory_log':
        if len(roles) == 0:
            rolesTemp = db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.roll!='Academic')&(db.validate_laboratory_log.roll!='DSI')).select(db.validate_laboratory_log.roll.with_alias('roll'), distinct=True)
        else:
            rolesTemp = db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(~db.validate_laboratory_log.roll.belongs(roles))&(db.validate_laboratory_log.roll!='Academic')&(db.validate_laboratory_log.roll!='DSI')).select(db.validate_laboratory_log.roll.with_alias('roll'), distinct=True)
        for roll in rolesTemp:
            roles.append(roll.roll)
    else:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    return roles

@auth.requires_login()
@auth.requires(auth.has_membership('Teacher'))
def GET_USERS(project,roll,typeReport):
    import cpfecys
    period = cpfecys.current_year_period()
    usersProject=[]
    #OFFICIAL USERS
    rollT = db((db.auth_group.role==roll)&(db.auth_group.role!='Academic')&(db.auth_group.role!='DSI')).select().first()
    if rollT is not None:
        if roll=='Super-Administrator' or roll=='Ecys-Administrator':
            for userT in db((db.auth_user.id==db.auth_membership.user_id)&(db.auth_membership.group_id==rollT.id)).select(db.auth_user.ALL):
                usersProject.append(userT.username)
        else:
            for userT in db((db.auth_membership.group_id==rollT.id)&(db.auth_membership.user_id==db.auth_user.id)&(db.auth_user.id==db.user_project.assigned_user)&(db.user_project.project==project.id)&(db.user_project.period == db.period_year.id)&((db.user_project.period <= period.id) & ((db.user_project.period + db.user_project.periods) > period.id))).select(db.auth_user.ALL):
                usersProject.append(userT.username)

    #USERS IN LOGS
    if typeReport == 'grades_log':
        if len(usersProject) ==0:
            usersProjectT = db((db.grades_log.project==project.name)&(db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.roll==roll)).select(db.grades_log.user_name, distinct=True)
        else:
            usersProjectT = db((db.grades_log.project==project.name)&(db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.roll==roll)&(~db.grades_log.user_name.belongs(usersProject))).select(db.grades_log.user_name, distinct=True)
        for userT in usersProjectT:
            usersProject.append(userT.user_name)
    elif typeReport == 'validate_laboratory_log':
        if len(usersProject) ==0:
            usersProjectT = db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.roll==roll)).select(db.validate_laboratory_log.user_name, distinct=True)
        else:
            usersProjectT = db((db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.roll==roll)&(~db.validate_laboratory_log.user_name.belongs(usersProject))).select(db.validate_laboratory_log.user_name, distinct=True)
        for userT in usersProjectT:
            usersProject.append(userT.user_name)
    else:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    return usersProject
#*****************************************************FEATURES EXTRAS FOR REPORTS*****************************************************
#*************************************************************************************************************************************
#*************************************************************************************************************************************




#*************************************************************************************************************************************
#*************************************************************************************************************************************
#*****************************************************MANAGEMENT REPORT GRADES********************************************************
@auth.requires_login()
@auth.requires(auth.has_membership('Teacher'))
def grades_management_export():
    #****************************************************************************************************************
    #****************************************************************************************************************
    #***************************************CHECK IF THERE IS A PERSONALIZED QUERY***********************************
    import cpfecys
    period = cpfecys.current_year_period()
    from datetime import datetime
    infoLevel = []
    personal_query = ''
    if request.vars['querySearch'] is not None and str(request.vars['querySearch']) != "":
        #PERSONALIZED QUERY SURE WORK
        try:
            personal_query = int(request.vars['querySearch'])
            countI = db(db.grades_log.academic==personal_query).count()
        except:
            personal_query = ''


    #****************************************************************************************************************
    #****************************************************************************************************************
    #******************************************VERIFY THAT ACCURATE PARAMETERS***************************************
    try:
        #CHECK IF THE TYPE OF EXPORT IS VALID
        if request.vars['list_type'] is None or str(request.vars['list_type'])!="csv":
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

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

                #CHECK IF THE PROJECT IS VALID
                project = VALIDATE_PROJECT(request.vars['project'],'grades_log')
                if project is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))
            
            #LEVEL MORE THAN 2
            if int(request.vars['level'])>2:
                #CHECK IF THE TYPE OF REPORT IS VALID
                if request.vars['type_U'] is None or (str(request.vars['type_U'])!="all" and str(request.vars['type_U'])!="i" and str(request.vars['type_U'])!="u" and str(request.vars['type_U'])!="d"):
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))

                #CHECK IF THE MONTH IS VALID
                month = VALIDATE_MONTH(request.vars['month'])
                if month is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))
                #OBTAIN ROLES
                roles=GET_ROLES('grades_log')
            
            #LEVEL MORE THAN 4
            if int(request.vars['level'])>3:
                #CHECK IF THE ROLE IS VALID
                roll = VALIDATE_ROLE(request.vars['roll'],'grades_log')
                if roll is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))
                #OBTAIN USERS
                usersProject = GET_USERS(project,roll,'grades_log')

            #LEVEL MORE THAN 5
            if int(request.vars['level'])>4:
                #CHECK IF THE USER IS VALID
                userP = VALIDATE_USER(project,roll,request.vars['userP'],'grades_log')
                if userP is None:
                    session.flash = T('Not valid Action.')
                    redi*rect(URL('default','index'))
    except:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    
    #****************************************************************************************************************
    #****************************************************************************************************************
    #*****************************************************REPORT*****************************************************
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
    #PERIOD OF REPORT
    infoeLevelTemp=[]
    infoeLevelTemp.append(T('Period'))
    infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
    infoLevel.append(infoeLevelTemp)
    #ALL SEMESTERS
    if request.vars['level']=='1' or request.vars['level'] is None:
        #MIDDLE LINE OF REPORT
        infoeLevelTemp=[]
        infoLevel.append(infoeLevelTemp)
        #LABLE DETAIL OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Detail'))
        infoLevel.append(infoeLevelTemp)
        #LABELS OF DATA OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Course'))
        infoeLevelTemp.append(T('Total inserted'))
        infoeLevelTemp.append(T('Total modified'))
        infoeLevelTemp.append(T('Total out'))
        infoLevel.append(infoeLevelTemp)
        for project in db((db.user_project.assigned_user==auth.user.id)&((db.user_project.period <= period.id) & ((db.user_project.period + db.user_project.periods) > period.id))).select():
            infoeLevelTemp = []
            #NAME OF PERIOD
            infoeLevelTemp.append(project.project.name)
            #COUNTS
            if personal_query == '':
                infoeLevelTemp.append(db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.project.name)&(db.grades_log.operation_log=='insert')).count())
                infoeLevelTemp.append(db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.project.name)&(db.grades_log.operation_log=='update')).count())
                infoeLevelTemp.append(db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.project.name)&(db.grades_log.operation_log=='delete')).count())
            else:
                infoeLevelTemp.append(db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.project.name)&(db.grades_log.operation_log=='insert')&(db.grades_log.academic.like('%'+str(personal_query)+'%'))).count())
                infoeLevelTemp.append(db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.project.name)&(db.grades_log.operation_log=='update')&(db.grades_log.academic.like('%'+str(personal_query)+'%'))).count())
                infoeLevelTemp.append(db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.project.name)&(db.grades_log.operation_log=='delete')&(db.grades_log.academic.like('%'+str(personal_query)+'%'))).count())
            #INSERT PROJECT
            infoLevel.append(infoeLevelTemp)
    #PER MONTH
    elif str(request.vars['level'])=="2":
        #PROJECT OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Course'))
        infoeLevelTemp.append(project.name)
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

        for month in GET_MONTH_PERIOD():
            start = datetime.strptime(str(period.yearp) + '-' + str(month[0]) +'-01', "%Y-%m-%d")
            if month[2]==1:
                end = datetime.strptime(str(period.yearp+1) + '-' + str(month[2]) +'-01', "%Y-%m-%d")
            else:
                end = datetime.strptime(str(period.yearp) + '-' + str(month[2]) +'-01', "%Y-%m-%d")
            infoeLevelTemp = []
            #NAME OF MONTH
            infoeLevelTemp.append(month[1]+' '+str(period.yearp))
            #COUNTS
            if personal_query == '':
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                    infoeLevelTemp.append(db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='insert')).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                    infoeLevelTemp.append(db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='update')).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                    infoeLevelTemp.append(db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='delete')).count())
            else:
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                    infoeLevelTemp.append(db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='insert')&(db.grades_log.academic.like('%'+str(personal_query)+'%'))).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                    infoeLevelTemp.append(db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='update')&(db.grades_log.academic.like('%'+str(personal_query)+'%'))).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                    infoeLevelTemp.append(db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='delete')&(db.grades_log.academic.like('%'+str(personal_query)+'%'))).count())
            #INSERT MONTH
            infoLevel.append(infoeLevelTemp)
    #PER ROL
    elif str(request.vars['level'])=="3":
        #PROJECT OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Course'))
        infoeLevelTemp.append(project.name)
        infoLevel.append(infoeLevelTemp)
        #MONTH OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Month'))
        infoeLevelTemp.append(month[0])
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
            #COUNTS
            if personal_query == '':
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                    infoeLevelTemp.append(db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(month[1]))&(db.grades_log.date_log<str(month[2]))&(db.grades_log.roll==str(roll))&(db.grades_log.operation_log=='insert')).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                    infoeLevelTemp.append(db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(month[1]))&(db.grades_log.date_log<str(month[2]))&(db.grades_log.roll==str(roll))&(db.grades_log.operation_log=='update')).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                    infoeLevelTemp.append(db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(month[1]))&(db.grades_log.date_log<str(month[2]))&(db.grades_log.roll==str(roll))&(db.grades_log.operation_log=='delete')).count())
            else:
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                    infoeLevelTemp.append(db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(month[1]))&(db.grades_log.date_log<str(month[2]))&(db.grades_log.roll==str(roll))&(db.grades_log.operation_log=='insert')&(db.grades_log.academic.like('%'+str(personal_query)+'%'))).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                    infoeLevelTemp.append(db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(month[1]))&(db.grades_log.date_log<str(month[2]))&(db.grades_log.roll==str(roll))&(db.grades_log.operation_log=='update')&(db.grades_log.academic.like('%'+str(personal_query)+'%'))).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                    infoeLevelTemp.append(db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(month[1]))&(db.grades_log.date_log<str(month[2]))&(db.grades_log.roll==str(roll))&(db.grades_log.operation_log=='delete')&(db.grades_log.academic.like('%'+str(personal_query)+'%'))).count())
            #INSERT ROLL
            infoLevel.append(infoeLevelTemp)
    #PER USER
    elif str(request.vars['level'])=="4":
        #PROJECT OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Course'))
        infoeLevelTemp.append(project.name)
        infoLevel.append(infoeLevelTemp)
        #MONTH OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Month'))
        infoeLevelTemp.append(month[0])
        infoLevel.append(infoeLevelTemp)
        #ROLE OF REPORT
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
        infoeLevelTemp.append(T('Month'))
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
            infoeLevelTemp = []
            #NAME OF USER
            infoeLevelTemp.append(userP)
            #COUNTS
            if personal_query == '':
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                    infoeLevelTemp.append(db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(month[1]))&(db.grades_log.date_log<str(month[2]))&(db.grades_log.roll==str(roll))&(db.grades_log.user_name==str(userP))&(db.grades_log.operation_log=='insert')).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                    infoeLevelTemp.append(db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(month[1]))&(db.grades_log.date_log<str(month[2]))&(db.grades_log.roll==str(roll))&(db.grades_log.user_name==str(userP))&(db.grades_log.operation_log=='update')).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                    infoeLevelTemp.append(db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(month[1]))&(db.grades_log.date_log<str(month[2]))&(db.grades_log.roll==str(roll))&(db.grades_log.user_name==str(userP))&(db.grades_log.operation_log=='delete')).count())
            else:
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                    infoeLevelTemp.append(db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(month[1]))&(db.grades_log.date_log<str(month[2]))&(db.grades_log.roll==str(roll))&(db.grades_log.user_name==str(userP))&(db.grades_log.operation_log=='insert')&(db.grades_log.academic.like('%'+str(personal_query)+'%'))).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                    infoeLevelTemp.append(db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(month[1]))&(db.grades_log.date_log<str(month[2]))&(db.grades_log.roll==str(roll))&(db.grades_log.user_name==str(userP))&(db.grades_log.operation_log=='update')&(db.grades_log.academic.like('%'+str(personal_query)+'%'))).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                    infoeLevelTemp.append(db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(month[1]))&(db.grades_log.date_log<str(month[2]))&(db.grades_log.roll==str(roll))&(db.grades_log.user_name==str(userP))&(db.grades_log.operation_log=='delete')&(db.grades_log.academic.like('%'+str(personal_query)+'%'))).count())
            #INSERT USER
            infoLevel.append(infoeLevelTemp)
    #DATA
    elif str(request.vars['level'])=="5":
        #PROJECT OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Course'))
        infoeLevelTemp.append(project.name)
        infoLevel.append(infoeLevelTemp)
        #MONTH OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Month'))
        infoeLevelTemp.append(month[0])
        infoLevel.append(infoeLevelTemp)
        #ROLE OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Role'))
        infoeLevelTemp.append(T('Rol '+roll))
        infoLevel.append(infoeLevelTemp)
        #ROLE OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('User'))
        infoeLevelTemp.append(userP)
        infoLevel.append(infoeLevelTemp)
        #MIDDLE LINE OF REPORT
        infoeLevelTemp=[]
        infoLevel.append(infoeLevelTemp)
        #LABLE DETAIL OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Detail'))
        infoLevel.append(infoeLevelTemp)
        #COUNTS
        if personal_query == '':
            if str(request.vars['type_L'])=="all":
                allData = db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(month[1]))&(db.grades_log.date_log<str(month[2]))&(db.grades_log.roll==str(roll))&(db.grades_log.user_name==str(userP))).select()
            elif str(request.vars['type_L'])=="i":
                allData = db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(month[1]))&(db.grades_log.date_log<str(month[2]))&(db.grades_log.roll==str(roll))&(db.grades_log.user_name==str(userP))&(db.grades_log.operation_log=='insert')).select()
            elif str(request.vars['type_L'])=="u":
                allData = db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(month[1]))&(db.grades_log.date_log<str(month[2]))&(db.grades_log.roll==str(roll))&(db.grades_log.user_name==str(userP))&(db.grades_log.operation_log=='update')).select()
            elif str(request.vars['type_L'])=="d":
                allData = db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(month[1]))&(db.grades_log.date_log<str(month[2]))&(db.grades_log.roll==str(roll))&(db.grades_log.user_name==str(userP))&(db.grades_log.operation_log=='delete')).select()
        else:
            if str(request.vars['type_L'])=="all":
                allData = db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(month[1]))&(db.grades_log.date_log<str(month[2]))&(db.grades_log.roll==str(roll))&(db.grades_log.user_name==str(userP))&(db.grades_log.academic.like('%'+str(personal_query)+'%'))).select()
            elif str(request.vars['type_L'])=="i":
                allData = db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(month[1]))&(db.grades_log.date_log<str(month[2]))&(db.grades_log.roll==str(roll))&(db.grades_log.user_name==str(userP))&(db.grades_log.operation_log=='insert')&(db.grades_log.academic.like('%'+str(personal_query)+'%'))).select()
            elif str(request.vars['type_L'])=="u":
                allData = db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(month[1]))&(db.grades_log.date_log<str(month[2]))&(db.grades_log.roll==str(roll))&(db.grades_log.user_name==str(userP))&(db.grades_log.operation_log=='update')&(db.grades_log.academic.like('%'+str(personal_query)+'%'))).select()
            elif str(request.vars['type_L'])=="d":
                allData = db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(month[1]))&(db.grades_log.date_log<str(month[2]))&(db.grades_log.roll==str(roll))&(db.grades_log.user_name==str(userP))&(db.grades_log.operation_log=='delete')&(db.grades_log.academic.like('%'+str(personal_query)+'%'))).select()
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
        for operation in allData:
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
    return dict(filename='ReporteGestionNotas', csvdata=infoLevel)
    

@auth.requires_login()
@auth.requires(auth.has_membership('Teacher'))
def grades_management():
    #****************************************************************************************************************
    #****************************************************************************************************************
    #***************************************CHECK IF THERE IS A PERSONALIZED QUERY***********************************
    import cpfecys
    period = cpfecys.current_year_period()
    from datetime import datetime
    infoLevel = []
    personal_query = ''
    makeRedirect = False
    project=None
    month=None
    roll=None
    userP=None
    grid=None
    if request.vars['querySearch'] is not None and str(request.vars['querySearch']) != "":
        #PERSONALIZED QUERY SURE WORK
        try:
            personal_query = int(request.vars['querySearch'])
            countI = db(db.grades_log.academic==personal_query).count()
            if request.vars['searchT'] is not None and str(request.vars['searchT']) == 'T':
                makeRedirect = True
        except:
            response.flash = T('The query is not valid. The report is displayed without applying any query.')
            personal_query = ''
    if makeRedirect == True:
        redirect(URL('teacher_reports', 'grades_management',vars=dict(level = 5, project = str(request.vars['project']), month = str(request.vars['month']), roll = str(request.vars['roll']), userP = str(request.vars['userP']), type_L=request.vars['type_L'], type_U=request.vars['type_U'], querySearch=request.vars['querySearch'])))


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

                #CHECK IF THE PROJECT IS VALID
                project = VALIDATE_PROJECT(request.vars['project'],'grades_log')
                if project is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))
            
            #LEVEL MORE THAN 2
            if int(request.vars['level'])>2:
                #CHECK IF THE TYPE OF REPORT IS VALID
                if request.vars['type_U'] is None or (str(request.vars['type_U'])!="all" and str(request.vars['type_U'])!="i" and str(request.vars['type_U'])!="u" and str(request.vars['type_U'])!="d"):
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))

                #CHECK IF THE MONTH IS VALID
                month = VALIDATE_MONTH(request.vars['month'])
                if month is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))
                #OBTAIN ROLES
                roles=GET_ROLES('grades_log')
            
            #LEVEL MORE THAN 4
            if int(request.vars['level'])>3:
                #CHECK IF THE ROLE IS VALID
                roll = VALIDATE_ROLE(request.vars['roll'],'grades_log')
                if roll is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))
                #OBTAIN USERS
                usersProject = GET_USERS(project,roll,'grades_log')

            #LEVEL MORE THAN 5
            if int(request.vars['level'])>4:
                #CHECK IF THE USER IS VALID
                userP = VALIDATE_USER(project,roll,request.vars['userP'],'grades_log')
                if userP is None:
                    session.flash = T('Not valid Action.')
                    redi*rect(URL('default','index'))
    except:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    
    #****************************************************************************************************************
    #****************************************************************************************************************
    #*****************************************************REPORT*****************************************************
    #LEVELS OF REPORT
    #ALL SEMESTERS
    if request.vars['level']=='1' or request.vars['level'] is None:
        projects = db((db.user_project.assigned_user==auth.user.id)&((db.user_project.period <= period.id) & ((db.user_project.period + db.user_project.periods) > period.id))).select()
        if projects.first() is None:
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('activity_control','courses_list'))

        for project in projects:
            infoeLevelTemp = []
            #ID OF PERIOD
            infoeLevelTemp.append(project.project.id)
            #NAME OF PERIOD
            infoeLevelTemp.append(project.project.name)
            #COUNTS
            if personal_query == '':
                infoeLevelTemp.append(db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.project.name)&(db.grades_log.operation_log=='insert')).count())
                infoeLevelTemp.append(db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.project.name)&(db.grades_log.operation_log=='update')).count())
                infoeLevelTemp.append(db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.project.name)&(db.grades_log.operation_log=='delete')).count())
            else:
                infoeLevelTemp.append(db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.project.name)&(db.grades_log.operation_log=='insert')&(db.grades_log.academic.like('%'+str(personal_query)+'%'))).count())
                infoeLevelTemp.append(db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.project.name)&(db.grades_log.operation_log=='update')&(db.grades_log.academic.like('%'+str(personal_query)+'%'))).count())
                infoeLevelTemp.append(db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.project.name)&(db.grades_log.operation_log=='delete')&(db.grades_log.academic.like('%'+str(personal_query)+'%'))).count())
            #INSERT PROJECT
            infoLevel.append(infoeLevelTemp)
    #PER MONTH
    elif str(request.vars['level'])=="2":
        for month in GET_MONTH_PERIOD():
            start = datetime.strptime(str(period.yearp) + '-' + str(month[0]) +'-01', "%Y-%m-%d")
            if month[2]==1:
                end = datetime.strptime(str(period.yearp+1) + '-' + str(month[2]) +'-01', "%Y-%m-%d")
            else:
                end = datetime.strptime(str(period.yearp) + '-' + str(month[2]) +'-01', "%Y-%m-%d")
            infoeLevelTemp = []
            #ID OF MONTH
            infoeLevelTemp.append(month[0])
            #NAME OF MONTH
            infoeLevelTemp.append(month[1]+' '+str(period.yearp))
            #COUNTS
            if personal_query == '':
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                    infoeLevelTemp.append(db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='insert')).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                    infoeLevelTemp.append(db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='update')).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                    infoeLevelTemp.append(db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='delete')).count())
            else:
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                    infoeLevelTemp.append(db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='insert')&(db.grades_log.academic.like('%'+str(personal_query)+'%'))).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                    infoeLevelTemp.append(db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='update')&(db.grades_log.academic.like('%'+str(personal_query)+'%'))).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                    infoeLevelTemp.append(db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(start))&(db.grades_log.date_log<str(end))&(db.grades_log.operation_log=='delete')&(db.grades_log.academic.like('%'+str(personal_query)+'%'))).count())
            #INSERT MONTH
            infoLevel.append(infoeLevelTemp)
    #PER ROL
    elif str(request.vars['level'])=="3":
        if len(roles) == 0:
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('teacher_reports', 'grades_management',vars=dict(level='2', type_L = str(request.vars['type_U']), querySearch=personal_query)))

        for rollT in roles:
            roll=db(db.auth_group.role==rollT).select().first()
            if roll is None:
                roll=db(db.grades_log.roll==rollT).select().first()
                roll=roll.roll
            else:
                roll=roll.role
            infoeLevelTemp = []
            #ID OF ROLE
            infoeLevelTemp.append(roll)
            #NAME OF ROLE
            infoeLevelTemp.append(T('Rol '+roll))
            #COUNTS
            if personal_query == '':
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                    infoeLevelTemp.append(db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(month[1]))&(db.grades_log.date_log<str(month[2]))&(db.grades_log.roll==str(roll))&(db.grades_log.operation_log=='insert')).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                    infoeLevelTemp.append(db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(month[1]))&(db.grades_log.date_log<str(month[2]))&(db.grades_log.roll==str(roll))&(db.grades_log.operation_log=='update')).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                    infoeLevelTemp.append(db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(month[1]))&(db.grades_log.date_log<str(month[2]))&(db.grades_log.roll==str(roll))&(db.grades_log.operation_log=='delete')).count())
            else:
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                    infoeLevelTemp.append(db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(month[1]))&(db.grades_log.date_log<str(month[2]))&(db.grades_log.roll==str(roll))&(db.grades_log.operation_log=='insert')&(db.grades_log.academic.like('%'+str(personal_query)+'%'))).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                    infoeLevelTemp.append(db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(month[1]))&(db.grades_log.date_log<str(month[2]))&(db.grades_log.roll==str(roll))&(db.grades_log.operation_log=='update')&(db.grades_log.academic.like('%'+str(personal_query)+'%'))).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                    infoeLevelTemp.append(db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(month[1]))&(db.grades_log.date_log<str(month[2]))&(db.grades_log.roll==str(roll))&(db.grades_log.operation_log=='delete')&(db.grades_log.academic.like('%'+str(personal_query)+'%'))).count())
            #INSERT ROLL
            infoLevel.append(infoeLevelTemp)
    #PER USER
    elif str(request.vars['level'])=="4":
        if len(usersProject) == 0:
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('teacher_reports', 'grades_management',vars=dict(level='3', month = str(request.vars['month']), type_L = str(request.vars['type_U']), type_U = str(request.vars['type_U']), querySearch=personal_query)))

        for userPT in usersProject:
            userP=db(db.auth_user.username==userPT).select().first()
            if userP is None:
                userP=db(db.grades_log.user_name==userPT).select().first()
                userP=userP.user_name
            else:
                userP=userP.username
            infoeLevelTemp = []
            #ID OF USER
            infoeLevelTemp.append(userP)
            #NAME OF USER
            infoeLevelTemp.append(userP)
            #COUNTS
            if personal_query == '':
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                    infoeLevelTemp.append(db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(month[1]))&(db.grades_log.date_log<str(month[2]))&(db.grades_log.roll==str(roll))&(db.grades_log.user_name==str(userP))&(db.grades_log.operation_log=='insert')).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                    infoeLevelTemp.append(db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(month[1]))&(db.grades_log.date_log<str(month[2]))&(db.grades_log.roll==str(roll))&(db.grades_log.user_name==str(userP))&(db.grades_log.operation_log=='update')).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                    infoeLevelTemp.append(db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(month[1]))&(db.grades_log.date_log<str(month[2]))&(db.grades_log.roll==str(roll))&(db.grades_log.user_name==str(userP))&(db.grades_log.operation_log=='delete')).count())
            else:
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                    infoeLevelTemp.append(db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(month[1]))&(db.grades_log.date_log<str(month[2]))&(db.grades_log.roll==str(roll))&(db.grades_log.user_name==str(userP))&(db.grades_log.operation_log=='insert')&(db.grades_log.academic.like('%'+str(personal_query)+'%'))).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                    infoeLevelTemp.append(db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(month[1]))&(db.grades_log.date_log<str(month[2]))&(db.grades_log.roll==str(roll))&(db.grades_log.user_name==str(userP))&(db.grades_log.operation_log=='update')&(db.grades_log.academic.like('%'+str(personal_query)+'%'))).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                    infoeLevelTemp.append(db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(month[1]))&(db.grades_log.date_log<str(month[2]))&(db.grades_log.roll==str(roll))&(db.grades_log.user_name==str(userP))&(db.grades_log.operation_log=='delete')&(db.grades_log.academic.like('%'+str(personal_query)+'%'))).count())
            #INSERT USER
            infoLevel.append(infoeLevelTemp)
    #DATA
    elif str(request.vars['level'])=="5":
        #COUNTS
        if personal_query == '':
            if str(request.vars['type_L'])=="all":
                allData = db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(month[1]))&(db.grades_log.date_log<str(month[2]))&(db.grades_log.roll==str(roll))&(db.grades_log.user_name==str(userP))).select()
            elif str(request.vars['type_L'])=="i":
                allData = db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(month[1]))&(db.grades_log.date_log<str(month[2]))&(db.grades_log.roll==str(roll))&(db.grades_log.user_name==str(userP))&(db.grades_log.operation_log=='insert')).select()
            elif str(request.vars['type_L'])=="u":
                allData = db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(month[1]))&(db.grades_log.date_log<str(month[2]))&(db.grades_log.roll==str(roll))&(db.grades_log.user_name==str(userP))&(db.grades_log.operation_log=='update')).select()
            elif str(request.vars['type_L'])=="d":
                allData = db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(month[1]))&(db.grades_log.date_log<str(month[2]))&(db.grades_log.roll==str(roll))&(db.grades_log.user_name==str(userP))&(db.grades_log.operation_log=='delete')).select()
        else:
            if str(request.vars['type_L'])=="all":
                allData = db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(month[1]))&(db.grades_log.date_log<str(month[2]))&(db.grades_log.roll==str(roll))&(db.grades_log.user_name==str(userP))&(db.grades_log.academic.like('%'+str(personal_query)+'%'))).select()
            elif str(request.vars['type_L'])=="i":
                allData = db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(month[1]))&(db.grades_log.date_log<str(month[2]))&(db.grades_log.roll==str(roll))&(db.grades_log.user_name==str(userP))&(db.grades_log.operation_log=='insert')&(db.grades_log.academic.like('%'+str(personal_query)+'%'))).select()
            elif str(request.vars['type_L'])=="u":
                allData = db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(month[1]))&(db.grades_log.date_log<str(month[2]))&(db.grades_log.roll==str(roll))&(db.grades_log.user_name==str(userP))&(db.grades_log.operation_log=='update')&(db.grades_log.academic.like('%'+str(personal_query)+'%'))).select()
            elif str(request.vars['type_L'])=="d":
                allData = db((db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.project==project.name)&(db.grades_log.date_log>=str(month[1]))&(db.grades_log.date_log<str(month[2]))&(db.grades_log.roll==str(roll))&(db.grades_log.user_name==str(userP))&(db.grades_log.operation_log=='delete')&(db.grades_log.academic.like('%'+str(personal_query)+'%'))).select()
        grid = []
        for data in allData:
                grid.append(data.id)
        if len(grid) == 0:
            grid.append(-1)
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
    return dict(personal_query=personal_query, infoLevel=infoLevel, period=period, project=project, month=month, roll=roll, userP=userP, grid=grid)


#*************************************************************************************************************************************
#*************************************************************************************************************************************
#*****************************************************MANAGEMENT REPORT VALIDATE******************************************************
@auth.requires_login()
@auth.requires(auth.has_membership('Teacher'))
def validate_laboratory_management_export():
    #****************************************************************************************************************
    #****************************************************************************************************************
    #***************************************CHECK IF THERE IS A PERSONALIZED QUERY***********************************
    import cpfecys
    period = cpfecys.current_year_period()
    from datetime import datetime
    infoLevel = []
    personal_query = ''
    if request.vars['querySearch'] is not None and str(request.vars['querySearch']) != "":
        #PERSONALIZED QUERY SURE WORK
        try:
            personal_query = int(request.vars['querySearch'])
            countI = db(db.validate_laboratory_log.academic==personal_query).count()
        except:
            personal_query = ''


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

                #CHECK IF THE PROJECT IS VALID
                project = VALIDATE_PROJECT(request.vars['project'],'validate_laboratory_log')
                if project is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))
            
            #LEVEL MORE THAN 2
            if int(request.vars['level'])>2:
                #CHECK IF THE TYPE OF REPORT IS VALID
                if request.vars['type_U'] is None or (str(request.vars['type_U'])!="all" and str(request.vars['type_U'])!="i" and str(request.vars['type_U'])!="u" and str(request.vars['type_U'])!="d"):
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))

                #CHECK IF THE MONTH IS VALID
                month = VALIDATE_MONTH(request.vars['month'])
                if month is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))
                #OBTAIN ROLES
                roles=GET_ROLES('validate_laboratory_log')
            
            #LEVEL MORE THAN 4
            if int(request.vars['level'])>3:
                #CHECK IF THE ROLE IS VALID
                roll = VALIDATE_ROLE(request.vars['roll'],'validate_laboratory_log')
                if roll is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))
                #OBTAIN USERS
                usersProject = GET_USERS(project,roll,'validate_laboratory_log')

            #LEVEL MORE THAN 5
            if int(request.vars['level'])>4:
                #CHECK IF THE USER IS VALID
                userP = VALIDATE_USER(project,roll,request.vars['userP'],'validate_laboratory_log')
                if userP is None:
                    session.flash = T('Not valid Action.')
                    redi*rect(URL('default','index'))
    except:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    
    #****************************************************************************************************************
    #****************************************************************************************************************
    #*****************************************************REPORT*****************************************************
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
    infoeLevelTemp.append(T('Management Reports Laboratory Revalidations'))
    infoLevel.append(infoeLevelTemp)
    #PERIOD OF REPORT
    infoeLevelTemp=[]
    infoeLevelTemp.append(T('Period'))
    infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
    infoLevel.append(infoeLevelTemp)
    #ALL SEMESTERS
    if request.vars['level']=='1' or request.vars['level'] is None:
        #MIDDLE LINE OF REPORT
        infoeLevelTemp=[]
        infoLevel.append(infoeLevelTemp)
        #LABLE DETAIL OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Detail'))
        infoLevel.append(infoeLevelTemp)
        #LABELS OF DATA OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Course'))
        infoeLevelTemp.append(T('Total inserted'))
        infoeLevelTemp.append(T('Total modified'))
        infoeLevelTemp.append(T('Total out'))
        infoLevel.append(infoeLevelTemp)
        for project in db((db.user_project.assigned_user==auth.user.id)&((db.user_project.period <= period.id) & ((db.user_project.period + db.user_project.periods) > period.id))).select():
            infoeLevelTemp = []
            #NAME OF PERIOD
            infoeLevelTemp.append(project.project.name)
            #COUNTS
            if personal_query == '':
                infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.project.name)&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==True)).count())
                infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.project.name)&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==True)).count())
                infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.project.name)&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==True)).count())
            else:
                infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.project.name)&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).count())
                infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.project.name)&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).count())
                infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.project.name)&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).count())
            #INSERT PROJECT
            infoLevel.append(infoeLevelTemp)
    #PER MONTH
    elif str(request.vars['level'])=="2":
        #PROJECT OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Course'))
        infoeLevelTemp.append(project.name)
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

        for month in GET_MONTH_PERIOD():
            start = datetime.strptime(str(period.yearp) + '-' + str(month[0]) +'-01', "%Y-%m-%d")
            if month[2]==1:
                end = datetime.strptime(str(period.yearp+1) + '-' + str(month[2]) +'-01', "%Y-%m-%d")
            else:
                end = datetime.strptime(str(period.yearp) + '-' + str(month[2]) +'-01', "%Y-%m-%d")
            infoeLevelTemp = []
            #NAME OF MONTH
            infoeLevelTemp.append(month[1]+' '+str(period.yearp))
            #COUNTS
            if personal_query == '':
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==True)).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==True)).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==True)).count())
            else:
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).count())
            #INSERT MONTH
            infoLevel.append(infoeLevelTemp)
    #PER ROL
    elif str(request.vars['level'])=="3":
        #PROJECT OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Course'))
        infoeLevelTemp.append(project.name)
        infoLevel.append(infoeLevelTemp)
        #MONTH OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Month'))
        infoeLevelTemp.append(month[0])
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
                roll=db(db.validate_laboratory_log.roll==rollT).select().first()
                roll=roll.roll
            else:
                roll=roll.role
            infoeLevelTemp = []
            #NAME OF ROLE
            infoeLevelTemp.append(T('Rol '+roll))
            #COUNTS
            if personal_query == '':
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==True)).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==True)).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==True)).count())
            else:
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).count())
            #INSERT ROLL
            infoLevel.append(infoeLevelTemp)
    #PER USER
    elif str(request.vars['level'])=="4":
        #PROJECT OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Course'))
        infoeLevelTemp.append(project.name)
        infoLevel.append(infoeLevelTemp)
        #MONTH OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Month'))
        infoeLevelTemp.append(month[0])
        infoLevel.append(infoeLevelTemp)
        #ROLE OF REPORT
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
                userP=db(db.validate_laboratory_log.user_name==userPT).select().first()
                userP=userP.user_name
            else:
                userP=userP.username
            infoeLevelTemp = []
            #NAME OF USER
            infoeLevelTemp.append(userP)
            #COUNTS
            if personal_query == '':
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==True)).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==True)).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==True)).count())
            else:
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).count())
            #INSERT USER
            infoLevel.append(infoeLevelTemp)
    #DATA
    elif str(request.vars['level'])=="5":
        #PROJECT OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Course'))
        infoeLevelTemp.append(project.name)
        infoLevel.append(infoeLevelTemp)
        #MONTH OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Month'))
        infoeLevelTemp.append(month[0])
        infoLevel.append(infoeLevelTemp)
        #ROLE OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Role'))
        infoeLevelTemp.append(T('Rol '+roll))
        infoLevel.append(infoeLevelTemp)
        #ROLE OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('User'))
        infoeLevelTemp.append(userP)
        infoLevel.append(infoeLevelTemp)
        #MIDDLE LINE OF REPORT
        infoeLevelTemp=[]
        infoLevel.append(infoeLevelTemp)
        #LABLE DETAIL OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Detail'))
        infoLevel.append(infoeLevelTemp)
        #COUNTS
        if personal_query == '':
            if str(request.vars['type_L'])=="all":
                allData = db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.validation_type==True)).select()
            elif str(request.vars['type_L'])=="i":
                allData = db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==True)).select()
            elif str(request.vars['type_L'])=="u":
                allData = db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==True)).select()
            elif str(request.vars['type_L'])=="d":
                allData = db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==True)).select()
        else:
            if str(request.vars['type_L'])=="all":
                allData = db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).select()
            elif str(request.vars['type_L'])=="i":
                allData = db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).select()
            elif str(request.vars['type_L'])=="u":
                allData = db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).select()
            elif str(request.vars['type_L'])=="d":
                allData = db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).select()
        #TITLE OF TABLE
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Operation'))
        infoeLevelTemp.append(T('Academic'))
        infoeLevelTemp.append(T('Grade Before'))
        infoeLevelTemp.append(T('Grade After'))
        infoeLevelTemp.append(T('Date'))
        infoeLevelTemp.append(T('Description'))
        infoLevel.append(infoeLevelTemp)
        for operation in allData:
            infoeLevelTemp=[]
            infoeLevelTemp.append(operation.operation_log)
            infoeLevelTemp.append(operation.academic)
            infoeLevelTemp.append(operation.before_grade)
            infoeLevelTemp.append(operation.after_grade)
            infoeLevelTemp.append(operation.date_log)
            infoeLevelTemp.append(operation.description)
    return dict(filename='ReporteGestionRevalidaciones', csvdata=infoLevel)
    

@auth.requires_login()
@auth.requires(auth.has_membership('Teacher'))
def validate_laboratory_management():
    #****************************************************************************************************************
    #****************************************************************************************************************
    #***************************************CHECK IF THERE IS A PERSONALIZED QUERY***********************************
    import cpfecys
    period = cpfecys.current_year_period()
    from datetime import datetime
    infoLevel = []
    personal_query = ''
    makeRedirect = False
    project=None
    month=None
    roll=None
    userP=None
    grid=None
    if request.vars['querySearch'] is not None and str(request.vars['querySearch']) != "":
        #PERSONALIZED QUERY SURE WORK
        try:
            personal_query = int(request.vars['querySearch'])
            countI = db(db.validate_laboratory_log.academic==personal_query).count()
            if request.vars['searchT'] is not None and str(request.vars['searchT']) == 'T':
                makeRedirect = True
        except:
            response.flash = T('The query is not valid. The report is displayed without applying any query.')
            personal_query = ''
    if makeRedirect == True:
        redirect(URL('teacher_reports', 'validate_laboratory_management',vars=dict(level = 5, project = str(request.vars['project']), month = str(request.vars['month']), roll = str(request.vars['roll']), userP = str(request.vars['userP']), type_L=request.vars['type_L'], type_U=request.vars['type_U'], querySearch=request.vars['querySearch'])))


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

                #CHECK IF THE PROJECT IS VALID
                project = VALIDATE_PROJECT(request.vars['project'],'validate_laboratory_log')
                if project is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))
            
            #LEVEL MORE THAN 2
            if int(request.vars['level'])>2:
                #CHECK IF THE TYPE OF REPORT IS VALID
                if request.vars['type_U'] is None or (str(request.vars['type_U'])!="all" and str(request.vars['type_U'])!="i" and str(request.vars['type_U'])!="u" and str(request.vars['type_U'])!="d"):
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))

                #CHECK IF THE MONTH IS VALID
                month = VALIDATE_MONTH(request.vars['month'])
                if month is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))
                #OBTAIN ROLES
                roles=GET_ROLES('validate_laboratory_log')
            
            #LEVEL MORE THAN 4
            if int(request.vars['level'])>3:
                #CHECK IF THE ROLE IS VALID
                roll = VALIDATE_ROLE(request.vars['roll'],'validate_laboratory_log')
                if roll is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))
                #OBTAIN USERS
                usersProject = GET_USERS(project,roll,'validate_laboratory_log')

            #LEVEL MORE THAN 5
            if int(request.vars['level'])>4:
                #CHECK IF THE USER IS VALID
                userP = VALIDATE_USER(project,roll,request.vars['userP'],'validate_laboratory_log')
                if userP is None:
                    session.flash = T('Not valid Action.')
                    redi*rect(URL('default','index'))
    except:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    
    #****************************************************************************************************************
    #****************************************************************************************************************
    #*****************************************************REPORT*****************************************************
    #LEVELS OF REPORT
    #ALL SEMESTERS
    if request.vars['level']=='1' or request.vars['level'] is None:
        projects = db((db.user_project.assigned_user==auth.user.id)&((db.user_project.period <= period.id) & ((db.user_project.period + db.user_project.periods) > period.id))).select()
        if projects.first() is None:
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('activity_control','courses_list'))

        for project in projects:
            infoeLevelTemp = []
            #ID OF PERIOD
            infoeLevelTemp.append(project.project.id)
            #NAME OF PERIOD
            infoeLevelTemp.append(project.project.name)
            #COUNTS
            if personal_query == '':
                infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.project.name)&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==True)).count())
                infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.project.name)&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==True)).count())
                infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.project.name)&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==True)).count())
            else:
                infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.project.name)&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).count())
                infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.project.name)&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).count())
                infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.project.name)&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).count())
            #INSERT PROJECT
            infoLevel.append(infoeLevelTemp)
    #PER MONTH
    elif str(request.vars['level'])=="2":
        for month in GET_MONTH_PERIOD():
            start = datetime.strptime(str(period.yearp) + '-' + str(month[0]) +'-01', "%Y-%m-%d")
            if month[2]==1:
                end = datetime.strptime(str(period.yearp+1) + '-' + str(month[2]) +'-01', "%Y-%m-%d")
            else:
                end = datetime.strptime(str(period.yearp) + '-' + str(month[2]) +'-01', "%Y-%m-%d")
            infoeLevelTemp = []
            #ID OF MONTH
            infoeLevelTemp.append(month[0])
            #NAME OF MONTH
            infoeLevelTemp.append(month[1]+' '+str(period.yearp))
            #COUNTS
            if personal_query == '':
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==True)).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==True)).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==True)).count())
            else:
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).count())
            #INSERT MONTH
            infoLevel.append(infoeLevelTemp)
    #PER ROL
    elif str(request.vars['level'])=="3":
        if len(roles) == 0:
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('teacher_reports', 'validate_laboratory_management',vars=dict(level='2', type_L = str(request.vars['type_U']), querySearch=personal_query)))

        for rollT in roles:
            roll=db(db.auth_group.role==rollT).select().first()
            if roll is None:
                roll=db(db.validate_laboratory_log.roll==rollT).select().first()
                roll=roll.roll
            else:
                roll=roll.role
            infoeLevelTemp = []
            #ID OF ROLE
            infoeLevelTemp.append(roll)
            #NAME OF ROLE
            infoeLevelTemp.append(T('Rol '+roll))
            #COUNTS
            if personal_query == '':
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==True)).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==True)).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==True)).count())
            else:
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).count())
            #INSERT ROLL
            infoLevel.append(infoeLevelTemp)
    #PER USER
    elif str(request.vars['level'])=="4":
        if len(usersProject) == 0:
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('teacher_reports', 'validate_laboratory_management',vars=dict(level='3', month = str(request.vars['month']), type_L = str(request.vars['type_U']), type_U = str(request.vars['type_U']), querySearch=personal_query)))

        for userPT in usersProject:
            userP=db(db.auth_user.username==userPT).select().first()
            if userP is None:
                userP=db(db.validate_laboratory_log.user_name==userPT).select().first()
                userP=userP.user_name
            else:
                userP=userP.username
            infoeLevelTemp = []
            #ID OF USER
            infoeLevelTemp.append(userP)
            #NAME OF USER
            infoeLevelTemp.append(userP)
            #COUNTS
            if personal_query == '':
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==True)).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==True)).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==True)).count())
            else:
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).count())
            #INSERT USER
            infoLevel.append(infoeLevelTemp)
    #DATA
    elif str(request.vars['level'])=="5":
        #COUNTS
        if personal_query == '':
            if str(request.vars['type_L'])=="all":
                allData = db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.validation_type==True)).select()
            elif str(request.vars['type_L'])=="i":
                allData = db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==True)).select()
            elif str(request.vars['type_L'])=="u":
                allData = db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==True)).select()
            elif str(request.vars['type_L'])=="d":
                allData = db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==True)).select()
        else:
            if str(request.vars['type_L'])=="all":
                allData = db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).select()
            elif str(request.vars['type_L'])=="i":
                allData = db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).select()
            elif str(request.vars['type_L'])=="u":
                allData = db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).select()
            elif str(request.vars['type_L'])=="d":
                allData = db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==True)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).select()
        grid = []
        for data in allData:
                grid.append(data.id)
        if len(grid) == 0:
            grid.append(-1)
        #GRID
        db.validate_laboratory_log.id.readable = False
        db.validate_laboratory_log.id.writable = False
        db.validate_laboratory_log.user_name.readable = False
        db.validate_laboratory_log.user_name.writable = False
        db.validate_laboratory_log.roll.readable = False
        db.validate_laboratory_log.roll.writable = False
        db.validate_laboratory_log.academic_id.readable = False
        db.validate_laboratory_log.academic_id.writable = False
        db.validate_laboratory_log.project.readable = False
        db.validate_laboratory_log.project.writable = False
        db.validate_laboratory_log.yearp.readable = False
        db.validate_laboratory_log.yearp.writable = False
        db.validate_laboratory_log.period.readable = False
        db.validate_laboratory_log.period.writable = False
        db.validate_laboratory_log.validation_type.readable = False
        db.validate_laboratory_log.validation_type.writable = False
        db.validate_laboratory_log.id_validate_laboratory.readable = False
        db.validate_laboratory_log.id_validate_laboratory.writable = False
        grid = SQLFORM.grid(db.validate_laboratory_log.id.belongs(grid), csv=False, create=False, editable=False, deletable=False, paginate=9, searchable=False)
    return dict(personal_query=personal_query, infoLevel=infoLevel, period=period, project=project, month=month, roll=roll, userP=userP, grid=grid)



#*************************************************************************************************************************************
#*************************************************************************************************************************************
#*****************************************************MANAGEMENT REPORT REPLACING*****************************************************
@auth.requires_login()
@auth.requires(auth.has_membership('Teacher'))
def laboratory_replacing_management_export():
    #****************************************************************************************************************
    #****************************************************************************************************************
    #***************************************CHECK IF THERE IS A PERSONALIZED QUERY***********************************
    import cpfecys
    period = cpfecys.current_year_period()
    from datetime import datetime
    infoLevel = []
    personal_query = ''
    if request.vars['querySearch'] is not None and str(request.vars['querySearch']) != "":
        #PERSONALIZED QUERY SURE WORK
        try:
            personal_query = int(request.vars['querySearch'])
            countI = db(db.validate_laboratory_log.academic==personal_query).count()
        except:
            personal_query = ''


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

                #CHECK IF THE PROJECT IS VALID
                project = VALIDATE_PROJECT(request.vars['project'],'validate_laboratory_log')
                if project is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))
            
            #LEVEL MORE THAN 2
            if int(request.vars['level'])>2:
                #CHECK IF THE TYPE OF REPORT IS VALID
                if request.vars['type_U'] is None or (str(request.vars['type_U'])!="all" and str(request.vars['type_U'])!="i" and str(request.vars['type_U'])!="u" and str(request.vars['type_U'])!="d"):
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))

                #CHECK IF THE MONTH IS VALID
                month = VALIDATE_MONTH(request.vars['month'])
                if month is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))
                #OBTAIN ROLES
                roles=GET_ROLES('validate_laboratory_log')
            
            #LEVEL MORE THAN 4
            if int(request.vars['level'])>3:
                #CHECK IF THE ROLE IS VALID
                roll = VALIDATE_ROLE(request.vars['roll'],'validate_laboratory_log')
                if roll is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))
                #OBTAIN USERS
                usersProject = GET_USERS(project,roll,'validate_laboratory_log')

            #LEVEL MORE THAN 5
            if int(request.vars['level'])>4:
                #CHECK IF THE USER IS VALID
                userP = VALIDATE_USER(project,roll,request.vars['userP'],'validate_laboratory_log')
                if userP is None:
                    session.flash = T('Not valid Action.')
                    redi*rect(URL('default','index'))
    except:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    
    #****************************************************************************************************************
    #****************************************************************************************************************
    #*****************************************************REPORT*****************************************************
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
    infoeLevelTemp.append(T('Report Equivalence Management Laboratory'))
    infoLevel.append(infoeLevelTemp)
    #PERIOD OF REPORT
    infoeLevelTemp=[]
    infoeLevelTemp.append(T('Period'))
    infoeLevelTemp.append(T(period.period.name)+' '+str(period.yearp))
    infoLevel.append(infoeLevelTemp)
    #ALL SEMESTERS
    if request.vars['level']=='1' or request.vars['level'] is None:
        #MIDDLE LINE OF REPORT
        infoeLevelTemp=[]
        infoLevel.append(infoeLevelTemp)
        #LABLE DETAIL OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Detail'))
        infoLevel.append(infoeLevelTemp)
        #LABELS OF DATA OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Course'))
        infoeLevelTemp.append(T('Total inserted'))
        infoeLevelTemp.append(T('Total modified'))
        infoeLevelTemp.append(T('Total out'))
        infoLevel.append(infoeLevelTemp)
        for project in db((db.user_project.assigned_user==auth.user.id)&((db.user_project.period <= period.id) & ((db.user_project.period + db.user_project.periods) > period.id))).select():
            infoeLevelTemp = []
            #NAME OF PERIOD
            infoeLevelTemp.append(project.project.name)
            #COUNTS
            if personal_query == '':
                infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.project.name)&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==False)).count())
                infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.project.name)&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==False)).count())
                infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.project.name)&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==False)).count())
            else:
                infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.project.name)&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).count())
                infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.project.name)&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).count())
                infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.project.name)&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).count())
            #INSERT PROJECT
            infoLevel.append(infoeLevelTemp)
    #PER MONTH
    elif str(request.vars['level'])=="2":
        #PROJECT OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Course'))
        infoeLevelTemp.append(project.name)
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

        for month in GET_MONTH_PERIOD():
            start = datetime.strptime(str(period.yearp) + '-' + str(month[0]) +'-01', "%Y-%m-%d")
            if month[2]==1:
                end = datetime.strptime(str(period.yearp+1) + '-' + str(month[2]) +'-01', "%Y-%m-%d")
            else:
                end = datetime.strptime(str(period.yearp) + '-' + str(month[2]) +'-01', "%Y-%m-%d")
            infoeLevelTemp = []
            #NAME OF MONTH
            infoeLevelTemp.append(month[1]+' '+str(period.yearp))
            #COUNTS
            if personal_query == '':
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==False)).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==False)).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==False)).count())
            else:
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).count())
            #INSERT MONTH
            infoLevel.append(infoeLevelTemp)
    #PER ROL
    elif str(request.vars['level'])=="3":
        #PROJECT OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Course'))
        infoeLevelTemp.append(project.name)
        infoLevel.append(infoeLevelTemp)
        #MONTH OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Month'))
        infoeLevelTemp.append(month[0])
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
                roll=db(db.validate_laboratory_log.roll==rollT).select().first()
                roll=roll.roll
            else:
                roll=roll.role
            infoeLevelTemp = []
            #NAME OF ROLE
            infoeLevelTemp.append(T('Rol '+roll))
            #COUNTS
            if personal_query == '':
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==False)).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==False)).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==False)).count())
            else:
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).count())
            #INSERT ROLL
            infoLevel.append(infoeLevelTemp)
    #PER USER
    elif str(request.vars['level'])=="4":
        #PROJECT OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Course'))
        infoeLevelTemp.append(project.name)
        infoLevel.append(infoeLevelTemp)
        #MONTH OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Month'))
        infoeLevelTemp.append(month[0])
        infoLevel.append(infoeLevelTemp)
        #ROLE OF REPORT
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
                userP=db(db.validate_laboratory_log.user_name==userPT).select().first()
                userP=userP.user_name
            else:
                userP=userP.username
            infoeLevelTemp = []
            #NAME OF USER
            infoeLevelTemp.append(userP)
            #COUNTS
            if personal_query == '':
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==False)).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==False)).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==False)).count())
            else:
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).count())
            #INSERT USER
            infoLevel.append(infoeLevelTemp)
    #DATA
    elif str(request.vars['level'])=="5":
        #PROJECT OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Course'))
        infoeLevelTemp.append(project.name)
        infoLevel.append(infoeLevelTemp)
        #MONTH OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Month'))
        infoeLevelTemp.append(month[0])
        infoLevel.append(infoeLevelTemp)
        #ROLE OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Role'))
        infoeLevelTemp.append(T('Rol '+roll))
        infoLevel.append(infoeLevelTemp)
        #ROLE OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('User'))
        infoeLevelTemp.append(userP)
        infoLevel.append(infoeLevelTemp)
        #MIDDLE LINE OF REPORT
        infoeLevelTemp=[]
        infoLevel.append(infoeLevelTemp)
        #LABLE DETAIL OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Detail'))
        infoLevel.append(infoeLevelTemp)
        #COUNTS
        if personal_query == '':
            if str(request.vars['type_L'])=="all":
                allData = db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.validation_type==False)).select()
            elif str(request.vars['type_L'])=="i":
                allData = db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==False)).select()
            elif str(request.vars['type_L'])=="u":
                allData = db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==False)).select()
            elif str(request.vars['type_L'])=="d":
                allData = db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==False)).select()
        else:
            if str(request.vars['type_L'])=="all":
                allData = db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).select()
            elif str(request.vars['type_L'])=="i":
                allData = db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).select()
            elif str(request.vars['type_L'])=="u":
                allData = db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).select()
            elif str(request.vars['type_L'])=="d":
                allData = db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).select()
        #TITLE OF TABLE
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Operation'))
        infoeLevelTemp.append(T('Academic'))
        infoeLevelTemp.append(T('Grade Before'))
        infoeLevelTemp.append(T('Grade After'))
        infoeLevelTemp.append(T('Date'))
        infoeLevelTemp.append(T('Description'))
        infoLevel.append(infoeLevelTemp)
        for operation in allData:
            infoeLevelTemp=[]
            infoeLevelTemp.append(operation.operation_log)
            infoeLevelTemp.append(operation.academic)
            infoeLevelTemp.append(operation.before_grade)
            infoeLevelTemp.append(operation.after_grade)
            infoeLevelTemp.append(operation.date_log)
            infoeLevelTemp.append(operation.description)
    return dict(filename='ReporteGestionEquivalencia', csvdata=infoLevel)
    

@auth.requires_login()
@auth.requires(auth.has_membership('Teacher'))
def laboratory_replacing_management():
    #****************************************************************************************************************
    #****************************************************************************************************************
    #***************************************CHECK IF THERE IS A PERSONALIZED QUERY***********************************
    import cpfecys
    period = cpfecys.current_year_period()
    from datetime import datetime
    infoLevel = []
    personal_query = ''
    makeRedirect = False
    project=None
    month=None
    roll=None
    userP=None
    grid=None
    if request.vars['querySearch'] is not None and str(request.vars['querySearch']) != "":
        #PERSONALIZED QUERY SURE WORK
        try:
            personal_query = int(request.vars['querySearch'])
            countI = db(db.validate_laboratory_log.academic==personal_query).count()
            if request.vars['searchT'] is not None and str(request.vars['searchT']) == 'T':
                makeRedirect = True
        except:
            response.flash = T('The query is not valid. The report is displayed without applying any query.')
            personal_query = ''
    if makeRedirect == True:
        redirect(URL('teacher_reports', 'laboratory_replacing_management',vars=dict(level = 5, project = str(request.vars['project']), month = str(request.vars['month']), roll = str(request.vars['roll']), userP = str(request.vars['userP']), type_L=request.vars['type_L'], type_U=request.vars['type_U'], querySearch=request.vars['querySearch'])))


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

                #CHECK IF THE PROJECT IS VALID
                project = VALIDATE_PROJECT(request.vars['project'],'validate_laboratory_log')
                if project is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))
            
            #LEVEL MORE THAN 2
            if int(request.vars['level'])>2:
                #CHECK IF THE TYPE OF REPORT IS VALID
                if request.vars['type_U'] is None or (str(request.vars['type_U'])!="all" and str(request.vars['type_U'])!="i" and str(request.vars['type_U'])!="u" and str(request.vars['type_U'])!="d"):
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))

                #CHECK IF THE MONTH IS VALID
                month = VALIDATE_MONTH(request.vars['month'])
                if month is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))
                #OBTAIN ROLES
                roles=GET_ROLES('validate_laboratory_log')
            
            #LEVEL MORE THAN 4
            if int(request.vars['level'])>3:
                #CHECK IF THE ROLE IS VALID
                roll = VALIDATE_ROLE(request.vars['roll'],'validate_laboratory_log')
                if roll is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))
                #OBTAIN USERS
                usersProject = GET_USERS(project,roll,'validate_laboratory_log')

            #LEVEL MORE THAN 5
            if int(request.vars['level'])>4:
                #CHECK IF THE USER IS VALID
                userP = VALIDATE_USER(project,roll,request.vars['userP'],'validate_laboratory_log')
                if userP is None:
                    session.flash = T('Not valid Action.')
                    redi*rect(URL('default','index'))
    except:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    
    #****************************************************************************************************************
    #****************************************************************************************************************
    #*****************************************************REPORT*****************************************************
    #LEVELS OF REPORT
    #ALL SEMESTERS
    if request.vars['level']=='1' or request.vars['level'] is None:
        projects = db((db.user_project.assigned_user==auth.user.id)&((db.user_project.period <= period.id) & ((db.user_project.period + db.user_project.periods) > period.id))).select()
        if projects.first() is None:
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('activity_control','courses_list'))

        for project in projects:
            infoeLevelTemp = []
            #ID OF PERIOD
            infoeLevelTemp.append(project.project.id)
            #NAME OF PERIOD
            infoeLevelTemp.append(project.project.name)
            #COUNTS
            if personal_query == '':
                infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.project.name)&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==False)).count())
                infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.project.name)&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==False)).count())
                infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.project.name)&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==False)).count())
            else:
                infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.project.name)&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).count())
                infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.project.name)&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).count())
                infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.project.name)&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).count())
            #INSERT PROJECT
            infoLevel.append(infoeLevelTemp)
    #PER MONTH
    elif str(request.vars['level'])=="2":
        for month in GET_MONTH_PERIOD():
            start = datetime.strptime(str(period.yearp) + '-' + str(month[0]) +'-01', "%Y-%m-%d")
            if month[2]==1:
                end = datetime.strptime(str(period.yearp+1) + '-' + str(month[2]) +'-01', "%Y-%m-%d")
            else:
                end = datetime.strptime(str(period.yearp) + '-' + str(month[2]) +'-01', "%Y-%m-%d")
            infoeLevelTemp = []
            #ID OF MONTH
            infoeLevelTemp.append(month[0])
            #NAME OF MONTH
            infoeLevelTemp.append(month[1]+' '+str(period.yearp))
            #COUNTS
            if personal_query == '':
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==False)).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==False)).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==False)).count())
            else:
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(start))&(db.validate_laboratory_log.date_log<str(end))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).count())
            #INSERT MONTH
            infoLevel.append(infoeLevelTemp)
    #PER ROL
    elif str(request.vars['level'])=="3":
        if len(roles) == 0:
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('teacher_reports', 'laboratory_replacing_management',vars=dict(level='2', type_L = str(request.vars['type_U']), querySearch=personal_query)))

        for rollT in roles:
            roll=db(db.auth_group.role==rollT).select().first()
            if roll is None:
                roll=db(db.validate_laboratory_log.roll==rollT).select().first()
                roll=roll.roll
            else:
                roll=roll.role
            infoeLevelTemp = []
            #ID OF ROLE
            infoeLevelTemp.append(roll)
            #NAME OF ROLE
            infoeLevelTemp.append(T('Rol '+roll))
            #COUNTS
            if personal_query == '':
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==False)).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==False)).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==False)).count())
            else:
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).count())
            #INSERT ROLL
            infoLevel.append(infoeLevelTemp)
    #PER USER
    elif str(request.vars['level'])=="4":
        if len(usersProject) == 0:
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('teacher_reports', 'laboratory_replacing_management',vars=dict(level='3', month = str(request.vars['month']), type_L = str(request.vars['type_U']), type_U = str(request.vars['type_U']), querySearch=personal_query)))

        for userPT in usersProject:
            userP=db(db.auth_user.username==userPT).select().first()
            if userP is None:
                userP=db(db.validate_laboratory_log.user_name==userPT).select().first()
                userP=userP.user_name
            else:
                userP=userP.username
            infoeLevelTemp = []
            #ID OF USER
            infoeLevelTemp.append(userP)
            #NAME OF USER
            infoeLevelTemp.append(userP)
            #COUNTS
            if personal_query == '':
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==False)).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==False)).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==False)).count())
            else:
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="i":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="u":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).count())
                if str(request.vars['type_L'])=="all" or str(request.vars['type_L'])=="d":
                    infoeLevelTemp.append(db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).count())
            #INSERT USER
            infoLevel.append(infoeLevelTemp)
    #DATA
    elif str(request.vars['level'])=="5":
        #COUNTS
        if personal_query == '':
            if str(request.vars['type_L'])=="all":
                allData = db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.validation_type==False)).select()
            elif str(request.vars['type_L'])=="i":
                allData = db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==False)).select()
            elif str(request.vars['type_L'])=="u":
                allData = db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==False)).select()
            elif str(request.vars['type_L'])=="d":
                allData = db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==False)).select()
        else:
            if str(request.vars['type_L'])=="all":
                allData = db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).select()
            elif str(request.vars['type_L'])=="i":
                allData = db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.operation_log=='insert')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).select()
            elif str(request.vars['type_L'])=="u":
                allData = db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.operation_log=='update')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).select()
            elif str(request.vars['type_L'])=="d":
                allData = db((db.validate_laboratory_log.period==T(period.period.name))&(db.validate_laboratory_log.yearp==period.yearp)&(db.validate_laboratory_log.project==project.name)&(db.validate_laboratory_log.date_log>=str(month[1]))&(db.validate_laboratory_log.date_log<str(month[2]))&(db.validate_laboratory_log.roll==str(roll))&(db.validate_laboratory_log.user_name==str(userP))&(db.validate_laboratory_log.operation_log=='delete')&(db.validate_laboratory_log.validation_type==False)&(db.validate_laboratory_log.academic.like('%'+str(personal_query)+'%'))).select()
        grid = []
        for data in allData:
                grid.append(data.id)
        if len(grid) == 0:
            grid.append(-1)
        #GRID
        db.validate_laboratory_log.id.readable = False
        db.validate_laboratory_log.id.writable = False
        db.validate_laboratory_log.user_name.readable = False
        db.validate_laboratory_log.user_name.writable = False
        db.validate_laboratory_log.roll.readable = False
        db.validate_laboratory_log.roll.writable = False
        db.validate_laboratory_log.academic_id.readable = False
        db.validate_laboratory_log.academic_id.writable = False
        db.validate_laboratory_log.project.readable = False
        db.validate_laboratory_log.project.writable = False
        db.validate_laboratory_log.yearp.readable = False
        db.validate_laboratory_log.yearp.writable = False
        db.validate_laboratory_log.period.readable = False
        db.validate_laboratory_log.period.writable = False
        db.validate_laboratory_log.validation_type.readable = False
        db.validate_laboratory_log.validation_type.writable = False
        db.validate_laboratory_log.id_validate_laboratory.readable = False
        db.validate_laboratory_log.id_validate_laboratory.writable = False
        grid = SQLFORM.grid(db.validate_laboratory_log.id.belongs(grid), csv=False, create=False, editable=False, deletable=False, paginate=9, searchable=False)
    return dict(personal_query=personal_query, infoLevel=infoLevel, period=period, project=project, month=month, roll=roll, userP=userP, grid=grid)
