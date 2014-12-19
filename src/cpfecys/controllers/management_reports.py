#*************************************************************************************************************************************
#*************************************************************************************************************************************
#*****************************************************FEATURES EXTRAS FOR REPORTS*****************************************************
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
def EXIST_MONTH(month, period):
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


#*****************************************************FEATURES EXTRAS FOR REPORTS*****************************************************
#*************************************************************************************************************************************
#*************************************************************************************************************************************


@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def grades_management_export():
    #CHECK IF THE TYPE OF EXPORT IS VALID
    if request.vars['list_type'] is None or str(request.vars['list_type'])!="csv":
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
    #LEVELS OF REPORT
    from datetime import datetime
    infoLevel = []
    top5=[]
    if request.vars['level'] is None or str(request.vars['level'])=="1":#ALL SEMESTERS
        if db(db.period_year).select().first() is None:
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('default','index'))
        
        #TITLE
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

        for period in db(db.period_year).select():
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
    elif str(request.vars['level'])=="2":#PER MONTH
        #CHECK IF THE TYPE OF REPORT IS VALID
        if request.vars['type_L'] is None or (str(request.vars['type_L'])!="all" and str(request.vars['type_L'])!="i" and str(request.vars['type_L'])!="u" and str(request.vars['type_L'])!="d"):
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #CHECK IF THE PERIOD IS VALID
        try:
            period = db(db.period_year.id==int(request.vars['period'])).select().first()
            if period is None:
                session.flash = T('Not valid Action.')
                redirect(URL('default','index'))
        except:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #TITLE
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
    elif str(request.vars['level'])=="3":#PER PROJECT
        #CHECK IF THE TYPE OF REPORT IS VALID
        if request.vars['type_U'] is None or (str(request.vars['type_U'])!="all" and str(request.vars['type_U'])!="i" and str(request.vars['type_U'])!="u" and str(request.vars['type_U'])!="d"):
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #CHECK IF THE TYPE OF REPORT IS VALID
        if request.vars['type_L'] is None or (str(request.vars['type_L'])!="all" and str(request.vars['type_L'])!="i" and str(request.vars['type_L'])!="u" and str(request.vars['type_L'])!="d"):
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #CHECK IF THE PERIOD IS VALID
        try:
            period = db(db.period_year.id==int(request.vars['period'])).select().first()
            if period is None:
                session.flash = T('Not valid Action.')
                redirect(URL('default','index'))
        except:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #CHECK IF THE MONTH IS VALID
        month = EXIST_MONTH(request.vars['month'],period)
        if month is None:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #PROJECTS
        area = db(db.area_level.name=='DTT Tutor Académico').select().first()
        projects=[]
        if area is not None:
            projectsTemp = db(db.project.area_level==area.id).select(db.project.name.with_alias('name'), distinct=True)
            if projectsTemp.first() is not None:
                for project in projectsTemp:
                    projects.append(project.name)
                for project in db(~db.grades_log.project.belongs(projects)).select(db.grades_log.project.with_alias('name'), distinct=True):
                    projects.append(project.name)
            else:
                for project in db(db.grades_log).select(db.grades_log.project.with_alias('name'), distinct=True):
                    projects.append(project.name)
        else:
            for project in db(db.grades_log).select(db.grades_log.project.with_alias('name'), distinct=True):
                projects.append(project.name)
        if len(projects) == 0:
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('management_reports', 'grades_management',vars=dict(list='level',level='2',period = str(request.vars['period']), type_L = str(request.vars['type_U']), querySearch=personal_query)))
        projects=sorted(projects)

        #TITLE
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
    elif str(request.vars['level'])=="4":#PER ROL
        #CHECK IF THE TYPE OF REPORT IS VALID
        if request.vars['type_U'] is None or (str(request.vars['type_U'])!="all" and str(request.vars['type_U'])!="i" and str(request.vars['type_U'])!="u" and str(request.vars['type_U'])!="d"):
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #CHECK IF THE TYPE OF REPORT IS VALID
        if request.vars['type_L'] is None or (str(request.vars['type_L'])!="all" and str(request.vars['type_L'])!="i" and str(request.vars['type_L'])!="u" and str(request.vars['type_L'])!="d"):
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #CHECK IF THE PERIOD IS VALID
        try:
            period = db(db.period_year.id==int(request.vars['period'])).select().first()
            if period is None:
                session.flash = T('Not valid Action.')
                redirect(URL('default','index'))
        except:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #CHECK IF THE MONTH IS VALID
        month = EXIST_MONTH(request.vars['month'],period)
        if month is None:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #PROJECTS
        try:
            project=db(db.grades_log.project==request.vars['project']).select().first()
            if project is None:
                area = db(db.area_level.name=='DTT Tutor Académico').select().first()
                project = db((db.project.name==request.vars['project'])&(db.project.area_level==area.id)).select().first()
                if project is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))
                else:
                    project=project.name
            else:
                project=project.project
        except:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #ROLES
        roles=[]
        rolesTemp = db((db.auth_group.role!='Academic')&(db.auth_group.role!='DSI')).select(db.auth_group.role.with_alias('roll'), distinct=True)
        if rolesTemp.first() is not None:
            for roll in rolesTemp:
                roles.append(roll.roll)
            for roll in db(~db.grades_log.roll.belongs(roles)&(db.grades_log.roll!='Academic')&(db.grades_log.roll!='DSI')).select(db.grades_log.roll.with_alias('roll'), distinct=True):
                roles.append(roll.roll)
        else:
            for roll in db((db.grades_log.roll!='Academic')&(db.grades_log.roll!='DSI')).select(db.grades_log.roll.with_alias('roll'), distinct=True):
                roles.append(roll.roll)
        if len(roles) == 0:
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('management_reports', 'grades_management',vars=dict(list='level',level='3', period = str(request.vars['period']), month = str(request.vars['month']), type_L = str(request.vars['type_U']), type_U = str(request.vars['type_U']), querySearch=personal_query)))

        #TITLE
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
    elif str(request.vars['level'])=="5":#PER USER
        #CHECK IF THE TYPE OF REPORT IS VALID
        if request.vars['type_U'] is None or (str(request.vars['type_U'])!="all" and str(request.vars['type_U'])!="i" and str(request.vars['type_U'])!="u" and str(request.vars['type_U'])!="d"):
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #CHECK IF THE TYPE OF REPORT IS VALID
        if request.vars['type_L'] is None or (str(request.vars['type_L'])!="all" and str(request.vars['type_L'])!="i" and str(request.vars['type_L'])!="u" and str(request.vars['type_L'])!="d"):
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #CHECK IF THE PERIOD IS VALID
        try:
            period = db(db.period_year.id==int(request.vars['period'])).select().first()
            if period is None:
                session.flash = T('Not valid Action.')
                redirect(URL('default','index'))
        except:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #CHECK IF THE MONTH IS VALID
        month = EXIST_MONTH(request.vars['month'],period)
        if month is None:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #PROJECTS
        try:
            project=db(db.grades_log.project==request.vars['project']).select().first()
            if project is None:
                area = db(db.area_level.name=='DTT Tutor Académico').select().first()
                project = db((db.project.name==request.vars['project'])&(db.project.area_level==area.id)).select().first()
                if project is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))
                else:
                    project=project.name
            else:
                project=project.project
        except:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #ROLE
        try:
            roll = db((db.auth_group.role==request.vars['roll'])&(db.auth_group.role!='Academic')&(db.auth_group.role!='DSI')).select().first()
            if roll is None:
                roll = db((db.grades_log.roll==request.vars['roll'])&(db.grades_log.roll!='Academic')&(db.grades_log.roll!='DSI')).select().first()
                if roll is not None:
                    roll=roll.roll
                else:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))
            else:
                roll=roll.role
        except:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #USERS
        usersProject=[]
        rollT = db((db.auth_group.role==request.vars['roll'])&(db.auth_group.role!='Academic')&(db.auth_group.role!='DSI')).select().first()
        if rollT is not None:
            if roll=='Super-Administrator' or roll=='Ecys-Administrator':
                usersProjectT = db((db.auth_user.id==db.auth_membership.user_id)&(db.auth_membership.group_id==rollT.id)).select(db.auth_user.ALL)
                if usersProjectT.first() is not None:
                    for userT in usersProjectT:
                        usersProject.append(userT.username)
                    for userT in db((db.grades_log.project==project)&(db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.roll==roll)&(~db.grades_log.user_name.belongs(usersProject))).select(db.grades_log.user_name, distinct=True):
                        usersProject.append(userT.user_name)
                else:
                    for userT in db((db.grades_log.project==project)&(db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.roll==roll)).select(db.grades_log.user_name, distinct=True):
                        usersProject.append(userT.user_name)
            else:
                projectT = db(db.project.name==request.vars['project']).select().first()
                if projectT is not None:
                    usersProjectT=db((db.auth_membership.group_id==rollT.id)&(db.auth_membership.user_id==db.auth_user.id)&(db.auth_user.id==db.user_project.assigned_user)&(db.user_project.project==projectT.id)&(db.user_project.period == db.period_year.id)&((db.user_project.period <= period.id) & ((db.user_project.period + db.user_project.periods) > period.id))).select(db.auth_user.ALL)
                    if usersProjectT.first() is not None:
                        for userT in usersProjectT:
                            usersProject.append(userT.username)
                        for userT in db((db.grades_log.project==project)&(db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.roll==roll)&(~db.grades_log.user_name.belongs(usersProject))).select(db.grades_log.user_name, distinct=True):
                            usersProject.append(userT.user_name)
                    else:
                        for userT in db((db.grades_log.project==project)&(db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.roll==roll)).select(db.grades_log.user_name, distinct=True):
                            usersProject.append(userT.user_name)
                else:
                    for userT in db((db.grades_log.project==project)&(db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.roll==roll)).select(db.grades_log.user_name, distinct=True):
                        usersProject.append(userT.user_name)
        else:
            for userT in db((db.grades_log.project==project)&(db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.roll==roll)).select(db.grades_log.user_name, distinct=True):
                usersProject.append(userT.user_name)

        #VERIFY THAT CAN SHOW THE LEVEL OF THE REPORT
        if len(usersProject) == 0:
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('management_reports', 'grades_management',vars=dict(list='level',level='4', period = str(request.vars['period']), month = str(request.vars['month']), project = str(request.vars['project']), type_L = str(request.vars['type_U']), type_U = str(request.vars['type_U']), querySearch=personal_query)))
        #TITLE
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
    elif str(request.vars['level'])=="6":
        #CHECK IF THE TYPE OF REPORT IS VALID
        if request.vars['type_U'] is None or (str(request.vars['type_U'])!="all" and str(request.vars['type_U'])!="i" and str(request.vars['type_U'])!="u" and str(request.vars['type_U'])!="d"):
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #CHECK IF THE TYPE OF REPORT IS VALID
        if request.vars['type_L'] is None or (str(request.vars['type_L'])!="all" and str(request.vars['type_L'])!="i" and str(request.vars['type_L'])!="u" and str(request.vars['type_L'])!="d"):
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #CHECK IF THE PERIOD IS VALID
        try:
            period = db(db.period_year.id==int(request.vars['period'])).select().first()
            if period is None:
                session.flash = T('Not valid Action.')
                redirect(URL('default','index'))
        except:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #CHECK IF THE MONTH IS VALID
        month = EXIST_MONTH(request.vars['month'],period)
        if month is None:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #PROJECTS
        try:
            project=db(db.grades_log.project==request.vars['project']).select().first()
            if project is None:
                area = db(db.area_level.name=='DTT Tutor Académico').select().first()
                project = db((db.project.name==request.vars['project'])&(db.project.area_level==area.id)).select().first()
                if project is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))
                else:
                    project=project.name
            else:
                project=project.project
        except:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #ROLE
        try:
            roll = db((db.auth_group.role==request.vars['roll'])&(db.auth_group.role!='Academic')&(db.auth_group.role!='DSI')).select().first()
            if roll is None:
                roll = db((db.grades_log.roll==request.vars['roll'])&(db.grades_log.roll!='Academic')&(db.grades_log.roll!='DSI')).select().first()
                if roll is not None:
                    roll=roll.roll
                else:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))
            else:
                roll=roll.role
        except:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #USER
        try:
            rollT = db((db.auth_group.role==request.vars['roll'])&(db.auth_group.role!='Academic')&(db.auth_group.role!='DSI')).select().first()
            if rollT is not None:
                if roll=='Super-Administrator' or roll=='Ecys-Administrator':
                    userP = db((db.auth_user.username==request.vars['userP'])&(db.auth_user.id==db.auth_membership.user_id)&(db.auth_membership.group_id==rollT.id)).select(db.auth_user.ALL).first()
                    if userP is not None:
                        userP=userP.username
                    else:
                        userP = db((db.grades_log.project==project)&(db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.roll==roll)&(db.grades_log.user_name==request.vars['userP'])).select().first()
                        if userP is None:
                            session.flash = T('Not valid Action.')
                            redirect(URL('default','index'))
                        else:
                            userP=userP.user_name
                else:
                    projectT = db(db.project.name==request.vars['project']).select().first()
                    if projectT is not None:
                        userP=db((db.auth_membership.group_id==rollT.id)&(db.auth_membership.user_id==db.auth_user.id)&(db.auth_user.username==request.vars['userP'])&(db.auth_user.id==db.user_project.assigned_user)&(db.user_project.project==projectT.id)&(db.user_project.period == db.period_year.id)&((db.user_project.period <= period.id) & ((db.user_project.period + db.user_project.periods) > period.id))).select(db.auth_user.ALL).first()
                        if userP is not None:
                            userP=userP.username
                        else:
                            userP = db((db.grades_log.project==project)&(db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.roll==roll)&(db.grades_log.user_name==request.vars['userP'])).select().first()
                            if userP is None:
                                session.flash = T('Not valid Action.')
                                redirect(URL('default','index'))
                            else:
                                userP=userP.user_name
                    else:
                        userP = db((db.grades_log.project==project)&(db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.roll==roll)&(db.grades_log.user_name==request.vars['userP'])).select().first()
                        if userP is None:
                            session.flash = T('Not valid Action.')
                            redirect(URL('default','index'))
                        else:
                            userP=userP.user_name
            else:
                userP = db((db.grades_log.project==project)&(db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.roll==roll)&(db.grades_log.user_name==request.vars['userP'])).select().first()
                if userP is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))
                else:
                    userP=userP.user_name
        except:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

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
        #TITLE OF REPORT
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
    else:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    #*****************************************************REPORT*****************************************************
    #****************************************************************************************************************
    #****************************************************************************************************************
    return dict(filename='ReporteGestionNotas', csvdata=infoLevel)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def grades_management():
    #****************************************************************************************************************
    #****************************************************************************************************************
    #*****************************************************SEARCH*****************************************************
    #Options to compare fields against the values entered
    def filtered_by(flag):
        fsearch_Option=[]
        fsearch_Option_Temp=[]
        fsearch_Option_Temp.append('=')
        fsearch_Option_Temp.append('=')
        fsearch_Option.append(fsearch_Option_Temp)
        fsearch_Option_Temp=[]
        fsearch_Option_Temp.append('!=')
        fsearch_Option_Temp.append('!=')
        fsearch_Option.append(fsearch_Option_Temp)
        fsearch_Option_Temp=[]
        fsearch_Option_Temp.append('<')
        fsearch_Option_Temp.append('<')
        fsearch_Option.append(fsearch_Option_Temp)
        fsearch_Option_Temp=[]
        fsearch_Option_Temp.append('>')
        fsearch_Option_Temp.append('>')
        fsearch_Option.append(fsearch_Option_Temp)
        fsearch_Option_Temp=[]
        fsearch_Option_Temp.append('<=')
        fsearch_Option_Temp.append('<=')
        fsearch_Option.append(fsearch_Option_Temp)
        fsearch_Option_Temp=[]
        fsearch_Option_Temp.append('>=')
        fsearch_Option_Temp.append('>=')
        fsearch_Option.append(fsearch_Option_Temp)
        if flag==True:
            fsearch_Option_Temp=[]
            fsearch_Option_Temp.append('starts with')
            fsearch_Option_Temp.append('inicia cón')
            fsearch_Option.append(fsearch_Option_Temp)
            fsearch_Option_Temp=[]
            fsearch_Option_Temp.append('contains')
            fsearch_Option_Temp.append('contiene')
            fsearch_Option.append(fsearch_Option_Temp)
            fsearch_Option_Temp=[]
            fsearch_Option_Temp.append('in')
            fsearch_Option_Temp.append('en')
            fsearch_Option.append(fsearch_Option_Temp)
            fsearch_Option_Temp=[]
            fsearch_Option_Temp.append('not in')
            fsearch_Option_Temp.append('no esta en')
            fsearch_Option.append(fsearch_Option_Temp)
        return fsearch_Option
    
    #ALL INFORMATION OF SEARCH
    if True:
        fsearch = []
        #
        fsearch_Temp=[]
        fsearch_Temp.append('user_name')
        fsearch_Temp.append('Usuario Registro')
        fsearch_Temp.append(True)
        fsearch_Values=[]
        fsearch_Values.append(1)
        fsearch_Temp.append(fsearch_Values)
        fsearch.append(fsearch_Temp)

        fsearch_Temp=[]
        fsearch_Temp.append('roll')
        fsearch_Temp.append('Rol')
        fsearch_Temp.append(True)
        fsearch_Values=[]
        fsearch_Values.append(1)
        fsearch_Temp.append(fsearch_Values)
        fsearch.append(fsearch_Temp)

        fsearch_Temp=[]
        fsearch_Temp.append('operation_log')
        fsearch_Temp.append('Operación Registrada')
        fsearch_Temp.append(True)
        fsearch_Values=[]
        fsearch_Values.append(1)
        fsearch_Temp.append(fsearch_Values)
        fsearch.append(fsearch_Temp)

        fsearch_Temp=[]
        fsearch_Temp.append('academic_assignation_id')
        fsearch_Temp.append('ID Asignación Estudiante')
        fsearch_Temp.append(True)
        fsearch_Values=[]
        fsearch_Values.append(1)
        fsearch_Temp.append(fsearch_Values)
        fsearch.append(fsearch_Temp)

        fsearch_Temp=[]
        fsearch_Temp.append('academic')
        fsearch_Temp.append('Estudiante')
        fsearch_Temp.append(True)
        fsearch_Values=[]
        fsearch_Values.append(1)
        fsearch_Temp.append(fsearch_Values)
        fsearch.append(fsearch_Temp)

        fsearch_Temp=[]
        fsearch_Temp.append('activity')
        fsearch_Temp.append('Actividad')
        fsearch_Temp.append(True)
        fsearch_Values=[]
        fsearch_Values.append(1)
        fsearch_Temp.append(fsearch_Values)
        fsearch.append(fsearch_Temp)

        fsearch_Temp=[]
        fsearch_Temp.append('activity_id')
        fsearch_Temp.append('ID Actividad')
        fsearch_Temp.append(True)
        fsearch_Values=[]
        fsearch_Values.append(1)
        fsearch_Temp.append(fsearch_Values)
        fsearch.append(fsearch_Temp)

        fsearch_Temp=[]
        fsearch_Temp.append('category')
        fsearch_Temp.append('Categoria')
        fsearch_Temp.append(True)
        fsearch_Values=[]
        fsearch_Values.append(1)
        fsearch_Temp.append(fsearch_Values)
        fsearch.append(fsearch_Temp)

        fsearch_Temp=[]
        fsearch_Temp.append('project')
        fsearch_Temp.append('Curso')
        fsearch_Temp.append(True)
        fsearch_Values=[]
        fsearch_Values.append(1)
        fsearch_Temp.append(fsearch_Values)
        fsearch.append(fsearch_Temp)

        fsearch_Temp=[]
        fsearch_Temp.append('yearp')
        fsearch_Temp.append('Año')
        fsearch_Temp.append(True)
        fsearch_Values=[]
        fsearch_Values.append(1)
        fsearch_Temp.append(fsearch_Values)
        fsearch.append(fsearch_Temp)

        fsearch_Temp=[]
        fsearch_Temp.append('period')
        fsearch_Temp.append('Periodo')
        fsearch_Temp.append(True)
        fsearch_Values=[]
        fsearch_Values.append(1)
        fsearch_Temp.append(fsearch_Values)
        fsearch.append(fsearch_Temp)

        fsearch_Temp=[]
        fsearch_Temp.append('before_grade')
        fsearch_Temp.append('Nota Historica')
        fsearch_Temp.append(False)
        fsearch_Values=[]
        fsearch_Values.append(1)
        fsearch_Temp.append(fsearch_Values)
        fsearch.append(fsearch_Temp)

        fsearch_Temp=[]
        fsearch_Temp.append('after_grade')
        fsearch_Temp.append('Nota Oficial')
        fsearch_Temp.append(False)
        fsearch_Values=[]
        fsearch_Values.append(1)
        fsearch_Temp.append(fsearch_Values)
        fsearch.append(fsearch_Temp)

        fsearch_Temp=[]
        fsearch_Temp.append('description')
        fsearch_Temp.append('Descripción')
        fsearch_Temp.append(True)
        fsearch_Values=[]
        fsearch_Values.append(1)
        fsearch_Temp.append(fsearch_Values)
        fsearch.append(fsearch_Temp)

        fsearch_Temp=[]
        fsearch_Temp.append('date_log')
        fsearch_Temp.append('Fecha')
        fsearch_Temp.append(False)
        fsearch_Values=[]
        fsearch_Values.append(2)
        fsearch_Temp.append(fsearch_Values)
        fsearch.append(fsearch_Temp)
    
    #CHECK IF THERE IS A PERSONALIZED QUERY
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
    #*****************************************************SEARCH*****************************************************



    #****************************************************************************************************************
    #****************************************************************************************************************
    #*****************************************************REPORT*****************************************************
    #LEVELS OF REPORT
    from datetime import datetime
    infoLevel = []
    top5=[]
    dataFinal = []
    grid=None
    if request.vars['level'] is None or str(request.vars['level'])=="1":#ALL SEMESTERS
        if db(db.period_year).select().first() is None:
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('default','index'))
            

        for period in db(db.period_year).select():
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
        search='grades_log.id != "-1"'
        top5 = db.smart_query(db.grades_log,search).select(db.grades_log.period, db.grades_log.yearp, db.grades_log.id.count(), orderby=~db.grades_log.id.count(), limitby=(0, 5), groupby=[db.grades_log.period, db.grades_log.yearp])
    elif str(request.vars['level'])=="2":#PER MONTH
        #CHECK IF THE TYPE OF REPORT IS VALID
        if request.vars['type_L'] is None or (str(request.vars['type_L'])!="all" and str(request.vars['type_L'])!="i" and str(request.vars['type_L'])!="u" and str(request.vars['type_L'])!="d"):
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #CHECK IF THE PERIOD IS VALID
        try:
            period = db(db.period_year.id==int(request.vars['period'])).select().first()
            if period is None:
                session.flash = T('Not valid Action.')
                redirect(URL('default','index'))
        except:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))


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
    elif str(request.vars['level'])=="3":#PER PROJECT
        #CHECK IF THE TYPE OF REPORT IS VALID
        if request.vars['type_U'] is None or (str(request.vars['type_U'])!="all" and str(request.vars['type_U'])!="i" and str(request.vars['type_U'])!="u" and str(request.vars['type_U'])!="d"):
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #CHECK IF THE TYPE OF REPORT IS VALID
        if request.vars['type_L'] is None or (str(request.vars['type_L'])!="all" and str(request.vars['type_L'])!="i" and str(request.vars['type_L'])!="u" and str(request.vars['type_L'])!="d"):
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #CHECK IF THE PERIOD IS VALID
        try:
            period = db(db.period_year.id==int(request.vars['period'])).select().first()
            if period is None:
                session.flash = T('Not valid Action.')
                redirect(URL('default','index'))
        except:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #CHECK IF THE MONTH IS VALID
        month = EXIST_MONTH(request.vars['month'],period)
        if month is None:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #PROJECTS
        area = db(db.area_level.name=='DTT Tutor Académico').select().first()
        projects=[]
        if area is not None:
            projectsTemp = db(db.project.area_level==area.id).select(db.project.name.with_alias('name'), distinct=True)
            if projectsTemp.first() is not None:
                for project in projectsTemp:
                    projects.append(project.name)
                for project in db(~db.grades_log.project.belongs(projects)).select(db.grades_log.project.with_alias('name'), distinct=True):
                    projects.append(project.name)
            else:
                for project in db(db.grades_log).select(db.grades_log.project.with_alias('name'), distinct=True):
                    projects.append(project.name)
        else:
            for project in db(db.grades_log).select(db.grades_log.project.with_alias('name'), distinct=True):
                projects.append(project.name)
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
    elif str(request.vars['level'])=="4":#PER ROL
        #CHECK IF THE TYPE OF REPORT IS VALID
        if request.vars['type_U'] is None or (str(request.vars['type_U'])!="all" and str(request.vars['type_U'])!="i" and str(request.vars['type_U'])!="u" and str(request.vars['type_U'])!="d"):
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #CHECK IF THE TYPE OF REPORT IS VALID
        if request.vars['type_L'] is None or (str(request.vars['type_L'])!="all" and str(request.vars['type_L'])!="i" and str(request.vars['type_L'])!="u" and str(request.vars['type_L'])!="d"):
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #CHECK IF THE PERIOD IS VALID
        try:
            period = db(db.period_year.id==int(request.vars['period'])).select().first()
            if period is None:
                session.flash = T('Not valid Action.')
                redirect(URL('default','index'))
        except:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #CHECK IF THE MONTH IS VALID
        month = EXIST_MONTH(request.vars['month'],period)
        if month is None:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #PROJECTS
        try:
            project=db(db.grades_log.project==request.vars['project']).select().first()
            if project is None:
                area = db(db.area_level.name=='DTT Tutor Académico').select().first()
                project = db((db.project.name==request.vars['project'])&(db.project.area_level==area.id)).select().first()
                if project is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))
                else:
                    project=project.name
            else:
                project=project.project
        except:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #ROLES
        roles=[]
        rolesTemp = db((db.auth_group.role!='Academic')&(db.auth_group.role!='DSI')).select(db.auth_group.role.with_alias('roll'), distinct=True)
        if rolesTemp.first() is not None:
            for roll in rolesTemp:
                roles.append(roll.roll)
            for roll in db(~db.grades_log.roll.belongs(roles)&(db.grades_log.roll!='Academic')&(db.grades_log.roll!='DSI')).select(db.grades_log.roll.with_alias('roll'), distinct=True):
                roles.append(roll.roll)
        else:
            for roll in db((db.grades_log.roll!='Academic')&(db.grades_log.roll!='DSI')).select(db.grades_log.roll.with_alias('roll'), distinct=True):
                roles.append(roll.roll)
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
    elif str(request.vars['level'])=="5":#PER USER
        #CHECK IF THE TYPE OF REPORT IS VALID
        if request.vars['type_U'] is None or (str(request.vars['type_U'])!="all" and str(request.vars['type_U'])!="i" and str(request.vars['type_U'])!="u" and str(request.vars['type_U'])!="d"):
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #CHECK IF THE TYPE OF REPORT IS VALID
        if request.vars['type_L'] is None or (str(request.vars['type_L'])!="all" and str(request.vars['type_L'])!="i" and str(request.vars['type_L'])!="u" and str(request.vars['type_L'])!="d"):
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #CHECK IF THE PERIOD IS VALID
        try:
            period = db(db.period_year.id==int(request.vars['period'])).select().first()
            if period is None:
                session.flash = T('Not valid Action.')
                redirect(URL('default','index'))
        except:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #CHECK IF THE MONTH IS VALID
        month = EXIST_MONTH(request.vars['month'],period)
        if month is None:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #PROJECTS
        try:
            project=db(db.grades_log.project==request.vars['project']).select().first()
            if project is None:
                area = db(db.area_level.name=='DTT Tutor Académico').select().first()
                project = db((db.project.name==request.vars['project'])&(db.project.area_level==area.id)).select().first()
                if project is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))
                else:
                    project=project.name
            else:
                project=project.project
        except:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #ROLE
        try:
            roll = db((db.auth_group.role==request.vars['roll'])&(db.auth_group.role!='Academic')&(db.auth_group.role!='DSI')).select().first()
            if roll is None:
                roll = db((db.grades_log.roll==request.vars['roll'])&(db.grades_log.roll!='Academic')&(db.grades_log.roll!='DSI')).select().first()
                if roll is not None:
                    roll=roll.roll
                else:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))
            else:
                roll=roll.role
        except:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #USERS
        usersProject=[]
        rollT = db((db.auth_group.role==request.vars['roll'])&(db.auth_group.role!='Academic')&(db.auth_group.role!='DSI')).select().first()
        if rollT is not None:
            if roll=='Super-Administrator' or roll=='Ecys-Administrator':
                usersProjectT = db((db.auth_user.id==db.auth_membership.user_id)&(db.auth_membership.group_id==rollT.id)).select(db.auth_user.ALL)
                if usersProjectT.first() is not None:
                    for userT in usersProjectT:
                        usersProject.append(userT.username)
                    for userT in db((db.grades_log.project==project)&(db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.roll==roll)&(~db.grades_log.user_name.belongs(usersProject))).select(db.grades_log.user_name, distinct=True):
                        usersProject.append(userT.user_name)
                else:
                    for userT in db((db.grades_log.project==project)&(db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.roll==roll)).select(db.grades_log.user_name, distinct=True):
                        usersProject.append(userT.user_name)
            else:
                projectT = db(db.project.name==request.vars['project']).select().first()
                if projectT is not None:
                    usersProjectT=db((db.auth_membership.group_id==rollT.id)&(db.auth_membership.user_id==db.auth_user.id)&(db.auth_user.id==db.user_project.assigned_user)&(db.user_project.project==projectT.id)&(db.user_project.period == db.period_year.id)&((db.user_project.period <= period.id) & ((db.user_project.period + db.user_project.periods) > period.id))).select(db.auth_user.ALL)
                    if usersProjectT.first() is not None:
                        for userT in usersProjectT:
                            usersProject.append(userT.username)
                        for userT in db((db.grades_log.project==project)&(db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.roll==roll)&(~db.grades_log.user_name.belongs(usersProject))).select(db.grades_log.user_name, distinct=True):
                            usersProject.append(userT.user_name)
                    else:
                        for userT in db((db.grades_log.project==project)&(db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.roll==roll)).select(db.grades_log.user_name, distinct=True):
                            usersProject.append(userT.user_name)
                else:
                    for userT in db((db.grades_log.project==project)&(db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.roll==roll)).select(db.grades_log.user_name, distinct=True):
                        usersProject.append(userT.user_name)
        else:
            for userT in db((db.grades_log.project==project)&(db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.roll==roll)).select(db.grades_log.user_name, distinct=True):
                usersProject.append(userT.user_name)

        #VERIFY THAT CAN SHOW THE LEVEL OF THE REPORT
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
    elif str(request.vars['level'])=="6":
        #CHECK IF THE TYPE OF REPORT IS VALID
        if request.vars['type_U'] is None or (str(request.vars['type_U'])!="all" and str(request.vars['type_U'])!="i" and str(request.vars['type_U'])!="u" and str(request.vars['type_U'])!="d"):
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #CHECK IF THE TYPE OF REPORT IS VALID
        if request.vars['type_L'] is None or (str(request.vars['type_L'])!="all" and str(request.vars['type_L'])!="i" and str(request.vars['type_L'])!="u" and str(request.vars['type_L'])!="d"):
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #CHECK IF THE PERIOD IS VALID
        try:
            period = db(db.period_year.id==int(request.vars['period'])).select().first()
            if period is None:
                session.flash = T('Not valid Action.')
                redirect(URL('default','index'))
        except:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #CHECK IF THE MONTH IS VALID
        month = EXIST_MONTH(request.vars['month'],period)
        if month is None:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #PROJECTS
        try:
            project=db(db.grades_log.project==request.vars['project']).select().first()
            if project is None:
                area = db(db.area_level.name=='DTT Tutor Académico').select().first()
                project = db((db.project.name==request.vars['project'])&(db.project.area_level==area.id)).select().first()
                if project is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))
                else:
                    project=project.name
            else:
                project=project.project
        except:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #ROLE
        try:
            roll = db((db.auth_group.role==request.vars['roll'])&(db.auth_group.role!='Academic')&(db.auth_group.role!='DSI')).select().first()
            if roll is None:
                roll = db((db.grades_log.roll==request.vars['roll'])&(db.grades_log.roll!='Academic')&(db.grades_log.roll!='DSI')).select().first()
                if roll is not None:
                    roll=roll.roll
                else:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))
            else:
                roll=roll.role
        except:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

        #USER
        try:
            rollT = db((db.auth_group.role==request.vars['roll'])&(db.auth_group.role!='Academic')&(db.auth_group.role!='DSI')).select().first()
            if rollT is not None:
                if roll=='Super-Administrator' or roll=='Ecys-Administrator':
                    userP = db((db.auth_user.username==request.vars['userP'])&(db.auth_user.id==db.auth_membership.user_id)&(db.auth_membership.group_id==rollT.id)).select(db.auth_user.ALL).first()
                    if userP is not None:
                        userP=userP.username
                    else:
                        userP = db((db.grades_log.project==project)&(db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.roll==roll)&(db.grades_log.user_name==request.vars['userP'])).select().first()
                        if userP is None:
                            session.flash = T('Not valid Action.')
                            redirect(URL('default','index'))
                        else:
                            userP=userP.user_name
                else:
                    projectT = db(db.project.name==request.vars['project']).select().first()
                    if projectT is not None:
                        userP=db((db.auth_membership.group_id==rollT.id)&(db.auth_membership.user_id==db.auth_user.id)&(db.auth_user.username==request.vars['userP'])&(db.auth_user.id==db.user_project.assigned_user)&(db.user_project.project==projectT.id)&(db.user_project.period == db.period_year.id)&((db.user_project.period <= period.id) & ((db.user_project.period + db.user_project.periods) > period.id))).select(db.auth_user.ALL).first()
                        if userP is not None:
                            userP=userP.username
                        else:
                            userP = db((db.grades_log.project==project)&(db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.roll==roll)&(db.grades_log.user_name==request.vars['userP'])).select().first()
                            if userP is None:
                                session.flash = T('Not valid Action.')
                                redirect(URL('default','index'))
                            else:
                                userP=userP.user_name
                    else:
                        userP = db((db.grades_log.project==project)&(db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.roll==roll)&(db.grades_log.user_name==request.vars['userP'])).select().first()
                        if userP is None:
                            session.flash = T('Not valid Action.')
                            redirect(URL('default','index'))
                        else:
                            userP=userP.user_name
            else:
                userP = db((db.grades_log.project==project)&(db.grades_log.period==T(period.period.name))&(db.grades_log.yearp==period.yearp)&(db.grades_log.roll==roll)&(db.grades_log.user_name==request.vars['userP'])).select().first()
                if userP is None:
                    session.flash = T('Not valid Action.')
                    redirect(URL('default','index'))
                else:
                    userP=userP.user_name
        except:
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

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
        #TOP 5 OF CATEGORY
        top5 = db.smart_query(db.grades_log,search).select(db.grades_log.category, db.grades_log.id.count(), orderby=~db.grades_log.id.count(), limitby=(0, 5), groupby=db.grades_log.category)
        #DATA
        dataFinal = db.smart_query(db.grades_log,search).select()
    else:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))
    #*****************************************************REPORT*****************************************************
    #****************************************************************************************************************
    #****************************************************************************************************************
    return dict(fsearch=fsearch, filtered_by=filtered_by, personal_query=personal_query, infoLevel=infoLevel, top5=top5, grid=grid, dataFinal=dataFinal)
