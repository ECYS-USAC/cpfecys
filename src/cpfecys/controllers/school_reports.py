@auth.requires_login()
@auth.requires_membership('Ecys-Administrator')
def get_assignations(project, period, role):
    assignations = db(
                    (db.auth_user.id==db.user_project.assigned_user)&
                    (db.auth_user.id==db.auth_membership.user_id)&
                    (db.auth_membership.group_id==db.auth_group.id)&
                    (db.auth_group.role==role)&
                    (project==False or (db.user_project.project==project))&
                    (db.project.area_level==db.area_level.id)&
                    (db.user_project.project==db.project.id)&
                    (db.user_project.period == db.period_year.id)&
                    ((db.user_project.period <= period.id)&
                 ((db.user_project.period + db.user_project.periods) > \
                  period.id))
                    )
    return assignations




#*************************************************************************************************************************************
#*************************************************************************************************************************************
#**************************************************MANAGEMENT REPORT PERFORMANCE OF STUDENTS******************************************
@auth.requires_login()
@auth.requires_membership('Ecys-Administrator')
def general_information_export():
    infoLevel = []
    groupPeriods = None
    period = None
    project = None
    try:
        #CHECK THAT THE LEVEL OF REPORT IS VALID
        if request.vars['level'] is not None and (int(request.vars['level'])<1 or int(request.vars['level'])>2):
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
            period = db(db.period_year.id==int(request.vars['period'])).select().first()
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
            project = db((db.project.id==int(request.vars['project']))&(db.project.area_level==area.id)).select().first()
            if project is None:
                session.flash = T('Not valid Action.')
                redirect(URL('default','index'))
    except:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))

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
    infoeLevelTemp.append(T('Performance of students'))
    infoLevel.append(infoeLevelTemp)
    #DESCRIPTION OF REPORT
    infoeLevelTemp=[]
    infoeLevelTemp.append(T('Description'))
    infoeLevelTemp.append(T('Report on the overview of the courses registered in the system.'))
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
        infoeLevelTemp.append(T('Active professors'))
        infoeLevelTemp.append(T('Academic Tutors Assets'))
        infoeLevelTemp.append(T('State of Course'))
        infoLevel.append(infoeLevelTemp)
        #ALL PROJECTS
        for project in groupProjects:
            infoeLevelTemp = []
            #NAME OF PROJECT
            infoeLevelTemp.append(project.name)
            #COUNT TEACHERS
            infoeLevelTemp.append(get_assignations(project, period, 'Teacher').count())
            #ACADEMIC TUTORS COUNT
            infoeLevelTemp.append(get_assignations(project, period, 'Student').count())
            #STATUS OF COURSE
            if infoeLevelTemp[1]+infoeLevelTemp[2]>0:
                infoeLevelTemp.append(T('Active'))
            else:
                infoeLevelTemp.append(T('Inactive'))
            infoLevel.append(infoeLevelTemp)
    else:
        infoLevel2=[]
        infoLevel2.append(get_assignations(project, period, 'Teacher').select(db.user_project.ALL))
        infoLevel2.append(get_assignations(project, period, 'Student').select(db.user_project.ALL))

        sc = db(db.item_restriction.name=='Horario Clase').select().first()
        infoLevel2.append([])
        if sc is not None and len(infoLevel2[1])>0:       
            for assignation in infoLevel2[1]:
                r_hl = db((db.item.item_restriction==sc.id)&(db.item.created==period.id)&(db.item.assignation==assignation.id)).select().first()
                if r_hl is not None and len(infoLevel2[2])<r_hl.item_schedule.count():
                    infoLevel2[2]=r_hl.item_schedule.select()

        sc = db(db.item_restriction.name=='Horario Laboratorio').select().first()
        infoLevel2.append([])
        if sc is not None and len(infoLevel2[1])>0:       
            for assignation in infoLevel2[1]:
                r_hl = db((db.item.item_restriction==sc.id)&(db.item.created==period.id)&(db.item.assignation==assignation.id)).select().first()
                if r_hl is not None and len(infoLevel2[3])<r_hl.item_schedule.count():
                    infoLevel2[3]=r_hl.item_schedule.select()

        #PROJECT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Course'))
        infoeLevelTemp.append(project.name)
        infoLevel.append(infoeLevelTemp)
        #MIDDLE LINE OF REPORT
        infoeLevelTemp=[]
        infoLevel.append(infoeLevelTemp)
        #LABLE DETAIL OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Course Information'))
        infoLevel.append(infoeLevelTemp)

        #Current Teacher
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Current Teacher'))
        infoLevel.append(infoeLevelTemp)
        if len(infoLevel2[0])<=0:
            infoeLevelTemp=[]
            infoeLevelTemp.append('')
            infoeLevelTemp.append(T('Not assigned'))
            infoLevel.append(infoeLevelTemp)
        else:
            for student in infoLevel2[0]:
                infoeLevelTemp=[]
                infoeLevelTemp.append('')
                infoeLevelTemp.append(T('Username'))
                infoeLevelTemp.append(student.assigned_user.username)
                infoLevel.append(infoeLevelTemp)
                infoeLevelTemp=[]
                infoeLevelTemp.append('')
                infoeLevelTemp.append(T('Name'))
                infoeLevelTemp.append(student.assigned_user.first_name+' '+student.assigned_user.last_name)
                infoLevel.append(infoeLevelTemp)
                infoeLevelTemp=[]
                infoeLevelTemp.append('')
                infoeLevelTemp.append(T('Email'))
                infoeLevelTemp.append(student.assigned_user.email)
                infoLevel.append(infoeLevelTemp)
                infoeLevelTemp=[]
                infoeLevelTemp.append('')
                infoeLevelTemp.append(T('Phone'))
                infoeLevelTemp.append(student.assigned_user.phone)
                infoLevel.append(infoeLevelTemp)
                infoeLevelTemp=[]
                infoeLevelTemp.append('')
                infoLevel.append(infoeLevelTemp)

        infoeLevelTemp=[]
        infoeLevelTemp.append('')
        infoLevel.append(infoeLevelTemp)
        infoeLevelTemp=[]
        infoeLevelTemp.append('')
        infoLevel.append(infoeLevelTemp)

        #Assigned Tutor
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Assigned Tutor'))
        infoLevel.append(infoeLevelTemp)
        if len(infoLevel2[1])<=0:
            infoeLevelTemp=[]
            infoeLevelTemp.append('')
            infoeLevelTemp.append(T('Not assigned'))
            infoLevel.append(infoeLevelTemp)
        else:
            for student in infoLevel2[1]:
                infoeLevelTemp=[]
                infoeLevelTemp.append('')
                infoeLevelTemp.append(T('Username'))
                infoeLevelTemp.append(student.assigned_user.username)
                infoLevel.append(infoeLevelTemp)
                infoeLevelTemp=[]
                infoeLevelTemp.append('')
                infoeLevelTemp.append(T('Name'))
                infoeLevelTemp.append(student.assigned_user.first_name+' '+student.assigned_user.last_name)
                infoLevel.append(infoeLevelTemp)
                infoeLevelTemp=[]
                infoeLevelTemp.append('')
                infoeLevelTemp.append(T('Email'))
                infoeLevelTemp.append(student.assigned_user.email)
                infoLevel.append(infoeLevelTemp)
                infoeLevelTemp=[]
                infoeLevelTemp.append('')
                infoeLevelTemp.append(T('Phone'))
                infoeLevelTemp.append(student.assigned_user.phone)
                infoLevel.append(infoeLevelTemp)
                infoeLevelTemp=[]
                infoeLevelTemp.append('')
                infoLevel.append(infoeLevelTemp)

        infoeLevelTemp=[]
        infoeLevelTemp.append('')
        infoLevel.append(infoeLevelTemp)
        infoeLevelTemp=[]
        infoeLevelTemp.append('')
        infoLevel.append(infoeLevelTemp)

        #Assigned Tutor
        infoeLevelTemp=[]
        infoeLevelTemp.append('Horario Clase:')
        infoLevel.append(infoeLevelTemp)
        if len(infoLevel2[2])<=0:
            infoeLevelTemp=[]
            infoeLevelTemp.append('')
            infoeLevelTemp.append(T('Not assigned'))
            infoLevel.append(infoeLevelTemp)
        else:
            for student in infoLevel2[2]:
                infoeLevelTemp=[]
                infoeLevelTemp.append('')
                infoeLevelTemp.append(T('Location'))
                infoeLevelTemp.append(student.physical_location)
                infoLevel.append(infoeLevelTemp)
                infoeLevelTemp=[]
                infoeLevelTemp.append('')
                infoeLevelTemp.append(T('Day'))
                infoeLevelTemp.append(db(db.day_of_week.id==student.day_of_week).select().first()['name'])
                infoLevel.append(infoeLevelTemp)
                infoeLevelTemp=[]
                infoeLevelTemp.append('')
                infoeLevelTemp.append(T('Start Hour'))
                infoeLevelTemp.append(student.start_time)
                infoLevel.append(infoeLevelTemp)
                infoeLevelTemp=[]
                infoeLevelTemp.append('')
                infoeLevelTemp.append(T('End Hour'))
                infoeLevelTemp.append(student.end_time)
                infoLevel.append(infoeLevelTemp)
                infoeLevelTemp=[]
                infoeLevelTemp.append('')
                infoLevel.append(infoeLevelTemp)
        
        infoeLevelTemp=[]
        infoeLevelTemp.append('')
        infoLevel.append(infoeLevelTemp)
        infoeLevelTemp=[]
        infoeLevelTemp.append('')
        infoLevel.append(infoeLevelTemp)

        #Assigned Tutor
        infoeLevelTemp=[]
        infoeLevelTemp.append('Horario Laboratorio:')
        infoLevel.append(infoeLevelTemp)
        if len(infoLevel2[3])<=0:
            infoeLevelTemp=[]
            infoeLevelTemp.append('')
            infoeLevelTemp.append(T('Not assigned'))
            infoLevel.append(infoeLevelTemp)
        else:
            for student in infoLevel2[3]:
                infoeLevelTemp=[]
                infoeLevelTemp.append('')
                infoeLevelTemp.append(T('Location'))
                infoeLevelTemp.append(student.physical_location)
                infoLevel.append(infoeLevelTemp)
                infoeLevelTemp=[]
                infoeLevelTemp.append('')
                infoeLevelTemp.append(T('Day'))
                infoeLevelTemp.append(db(db.day_of_week.id==student.day_of_week).select().first()['name'])
                infoLevel.append(infoeLevelTemp)
                infoeLevelTemp=[]
                infoeLevelTemp.append('')
                infoeLevelTemp.append(T('Start Hour'))
                infoeLevelTemp.append(student.start_time)
                infoLevel.append(infoeLevelTemp)
                infoeLevelTemp=[]
                infoeLevelTemp.append('')
                infoeLevelTemp.append(T('End Hour'))
                infoeLevelTemp.append(student.end_time)
                infoLevel.append(infoeLevelTemp)
                infoeLevelTemp=[]
                infoeLevelTemp.append('')
                infoLevel.append(infoeLevelTemp)

    return dict(filename='InformacionGeneral', csvdata=infoLevel)
    
@auth.requires_login()
@auth.requires_membership('Ecys-Administrator')
def general_information():
    infoLevel = []
    groupPeriods = None
    period = None
    project = None
    try:
        #CHECK THAT THE LEVEL OF REPORT IS VALID
        if request.vars['level'] is not None and (int(request.vars['level'])<1 or int(request.vars['level'])>2):
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
            period = db(db.period_year.id==int(request.vars['period'])).select().first()
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
            project = db((db.project.id==int(request.vars['project']))&(db.project.area_level==area.id)).select().first()
            if project is None:
                session.flash = T('Not valid Action.')
                redirect(URL('default','index'))
    except:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))

    #*****************************************************REPORT*****************************************************
    #ALL SEMESTERS
    if request.vars['level']=='1' or request.vars['level'] is None:
        #ALL PROJECTS
        for project in groupProjects:
            infoeLevelTemp = []
            #ID OF PROJECT
            infoeLevelTemp.append(project.id)
            #NAME OF PROJECT
            infoeLevelTemp.append(project.name)
            #COUNT TEACHERS
            infoeLevelTemp.append(get_assignations(project, period, 'Teacher').count())
            #ACADEMIC TUTORS COUNT
            infoeLevelTemp.append(get_assignations(project, period, 'Student').count())
            infoLevel.append(infoeLevelTemp)
    else:
        infoLevel.append(get_assignations(project, period, 'Teacher').select(db.user_project.ALL))
        infoLevel.append(get_assignations(project, period, 'Student').select(db.user_project.ALL))

        sc = db(db.item_restriction.name=='Horario Clase').select().first()
        infoLevel.append([])
        if sc is not None and len(infoLevel[1])>0:       
            for assignation in infoLevel[1]:
                r_hl = db((db.item.item_restriction==sc.id)&(db.item.created==period.id)&(db.item.assignation==assignation.id)).select().first()
                if r_hl is not None and len(infoLevel[2])<r_hl.item_schedule.count():
                    infoLevel[2]=r_hl.item_schedule.select()

        sc = db(db.item_restriction.name=='Horario Laboratorio').select().first()
        infoLevel.append([])
        if sc is not None and len(infoLevel[1])>0:       
            for assignation in infoLevel[1]:
                r_hl = db((db.item.item_restriction==sc.id)&(db.item.created==period.id)&(db.item.assignation==assignation.id)).select().first()
                if r_hl is not None and len(infoLevel[3])<r_hl.item_schedule.count():
                    infoLevel[3]=r_hl.item_schedule.select()
    return dict(groupPeriods=groupPeriods, period=period, infoLevel=infoLevel, project=project)
