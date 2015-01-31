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
        if len(infoLevel[0])<=0 and len(infoLevel[1])<=0:
            session.flash = T('Report no visible: There is no assignment in the selected project within six months.')
            redirect(URL('school_reports', 'general_information',vars=dict(period = period.id)))
    return dict(groupPeriods=groupPeriods, period=period, infoLevel=infoLevel, project=project)