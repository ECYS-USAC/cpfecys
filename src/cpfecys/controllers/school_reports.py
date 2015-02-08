@auth.requires_login()
@auth.requires(auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
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



@auth.requires_login()
@auth.requires(auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
def get_name(project):
    try:
        (nameP, projectSection) = str(project.name).split('(')
        (nameS,garbage) = str(projectSection).split(')')
    except:
        nameP = project.name
    whiteSpace = 0
    for letter in reversed(xrange(len(nameP)-whiteSpace)):
        if nameP[letter]==' ':
            whiteSpace+=1
        else:
            break
    nameC = None
    for letter in xrange(len(nameP)-whiteSpace):
        if nameC is None:
            nameC=nameP[letter]
        else:
            nameC=nameC+nameP[letter]
    return nameC



@auth.requires_login()
@auth.requires(auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
def get_unique_name(project):
    nameC = db(db.project.name.like('%'+project+'%')).select().first()[db.project.name]
    #nameC = nameC.name
    try:
        (nameP, projectSection) = str(nameC).split('(')
        (nameS,garbage) = str(projectSection).split(')')
    except:
        nameP = nameC
    whiteSpace = 0
    for letter in reversed(xrange(len(nameP)-whiteSpace)):
        if nameP[letter]==' ':
            whiteSpace+=1
        else:
            break
    nameC = None
    for letter in xrange(len(nameP)-whiteSpace):
        if nameC is None:
            nameC=nameP[letter]
        else:
            nameC=nameC+nameP[letter]
    return nameC

#*************************************************************************************************************************************
#*************************************************************************************************************************************
#**************************************************REPORT INFORMATION GENERAL*********************************************************
@auth.requires_login()
@auth.requires(auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
def general_information_export():
    infoLevel = []
    groupPeriods = None
    period = None
    project = None
    try:
        #CHECK IF THE TYPE OF EXPORT IS VALID
        if request.vars['list_type'] is None or str(request.vars['list_type'])!="csv":
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))
            
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
    infoeLevelTemp.append(T('General Information'))
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
@auth.requires(auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
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



#*************************************************************************************************************************************
#*************************************************************************************************************************************
#**************************************************REPORT INFORMATION PERIOD**********************************************************
@auth.requires_login()
@auth.requires(auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
def general_period_export():
    infoLevel = []
    groupPeriods = None
    period = None
    try:
        #CHECK IF THE TYPE OF EXPORT IS VALID
        if request.vars['list_type'] is None or str(request.vars['list_type'])!="csv":
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
        #groupProjects = db(db.project.area_level==area.id).select(orderby=db.project.name)
        groupProjects = db((db.project.area_level==area.id)&
                        (db.user_project.project==db.project.id)&
                        (db.user_project.period == db.period_year.id)&
                        ((db.user_project.period <= period.id)&
                        ((db.user_project.period + db.user_project.periods) > period.id))).select(db.project.ALL, orderby=db.project.name, distinct=True)
        if len(groupProjects) == 0:
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('default','index'))

        partials = db(db.partials).select()
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
    infoeLevelTemp.append(T('Overview of semester'))
    infoLevel.append(infoeLevelTemp)
    #DESCRIPTION OF REPORT
    infoeLevelTemp=[]
    infoeLevelTemp.append(T('Description'))
    infoeLevelTemp.append(T('Report on the overview of courses per semester.'))
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
    infoeLevelTemp = []
    infoeLevelTemp.append(T('Course'))
    infoeLevelTemp.append(T('Total number of students assigned to the course'))
    for partial in partials:
        infoeLevelTemp.append(T('Average of grades of')+' '+partial.name)
    infoeLevelTemp.append(T('Average of grades of')+' Examen Final')
    infoeLevelTemp.append(T('Percentage of students who passed the')+' '+T('Laboratory'))
    infoeLevelTemp.append(T('Percentage of students who passed the')+' '+T('Course'))
    infoLevel.append(infoeLevelTemp)
    #ALL PROJECTS
    controlP = db(db.student_control_period.period_name==(T(period.period.name)+" "+str(period.yearp))).select().first()
    if controlP is not None:
        for project in groupProjects:
            infoeLevelTemp = []
            #NAME OF PROJECT
            infoeLevelTemp.append(project.name)
            #TOTAL STUDENTS
            students = db((db.academic_course_assignation.semester==period.id)&(db.academic_course_assignation.assignation==project.id)).select()
            infoeLevelTemp.append(str(len(students)))
            #PARTIALS
            for partial in partials:
                average=0
                activityPartial = db((db.course_activity.assignation==project.id)&(db.course_activity.semester==period.id)&(db.course_activity.name==partial.name)&(db.course_activity.laboratory==False)).select().first()
                if activityPartial is not None:
                    averageA = db.executesql('select avg(grade) as average from grades where activity='+str(activityPartial.id)+';',as_dict=True)
                    for d0 in averageA:
                        if d0['average']!=None:
                            average=float(round(d0['average'],2))
                infoeLevelTemp.append(str(average))
            #FINAL TEST
            average=0
            activityFinal = db((db.course_activity.assignation==project.id)&(db.course_activity.semester==period.id)&(db.course_activity.name=='Examen Final')&(db.course_activity.laboratory==False)).select().first()
            if activityFinal is not None:
                averageA = db.executesql('select avg(grade) as average from grades where activity='+str(activityFinal.id)+';',as_dict=True)
                for d0 in averageA:
                    if d0['average']!=None:
                        average=float(round(d0['average'],2))
            infoeLevelTemp.append(str(average))
            #CLASS AND LABORATORY
            totalWinLaboratory=0
            totalWinClass=0

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
                    categoriesClass.append([categories,0])

            #GRADE OF STUDENT
            for student in students:
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
                            if grade_Laboratory>=61:
                                totalWinLaboratory=totalWinLaboratory+1
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
                            grade_Laboratory=float((grade_Laboratory*float(categoryClass[0].grade))/100)
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
                    totalCarry=int(round(totalCarry,0))+int(round(grade_Laboratory,0))+totalFinal
                    totalCarry = int(round(totalCarry,0))
                    if totalCarry >=61:
                        totalWinClass=totalWinClass+1
            #LABORATORY
            studentsLab = db((db.academic_course_assignation.semester==period.id)&(db.academic_course_assignation.assignation==project.id)&(db.academic_course_assignation.laboratorio==True)).count()
            if studentsLab>0:
                totalWinLaboratory=round(((totalWinLaboratory*100)/studentsLab),2)
            infoeLevelTemp.append(totalWinLaboratory)
            #CLASS
            if len(students)>0:
                totalWinClass=round(((totalWinClass*100)/len(students)),2)
            infoeLevelTemp.append(totalWinClass)
            infoLevel.append(infoeLevelTemp)
    return dict(filename='InformacionPeriodo', csvdata=infoLevel)

@auth.requires_login()
@auth.requires(auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
def general_period():
    infoLevel = []
    groupPeriods = None
    period = None
    try:
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
        groupPeriods = db(db.period_year).select(orderby=~db.period_year.id)
        if len(groupPeriods) == 0:
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('default','index'))

        #groupProjects = db(db.project.area_level==area.id).select(orderby=db.project.name)
        groupProjects = db((db.project.area_level==area.id)&
                        (db.user_project.project==db.project.id)&
                        (db.user_project.period == db.period_year.id)&
                        ((db.user_project.period <= period.id)&
                        ((db.user_project.period + db.user_project.periods) > period.id))).select(db.project.ALL, orderby=db.project.name, distinct=True)
        if len(groupProjects) == 0:
            session.flash = T('Report no visible: There are no parameters required to display the report.')
            redirect(URL('default','index'))

        partials = db(db.partials).select()
    except:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))

    #*****************************************************REPORT*****************************************************
    infoeLevelTemp = []
    infoeLevelTemp.append(T('Course'))
    infoeLevelTemp.append(T('Total number of students assigned to the course'))
    for partial in partials:
        infoeLevelTemp.append(T('Average of grades of')+' '+partial.name)
    infoeLevelTemp.append(T('Average of grades of')+' Examen Final')
    infoeLevelTemp.append(T('Percentage of students who passed the')+' '+T('Laboratory'))
    infoeLevelTemp.append(T('Percentage of students who passed the')+' '+T('Course'))
    infoLevel.append(infoeLevelTemp)
    #ALL PROJECTS
    controlP = db(db.student_control_period.period_name==(T(period.period.name)+" "+str(period.yearp))).select().first()
    if controlP is not None:
        for project in groupProjects:
            infoeLevelTemp = []
            #NAME OF PROJECT
            infoeLevelTemp.append(project.name)
            #TOTAL STUDENTS
            students = db((db.academic_course_assignation.semester==period.id)&(db.academic_course_assignation.assignation==project.id)).select()
            infoeLevelTemp.append(str(len(students)))
            #PARTIALS
            for partial in partials:
                average=0
                activityPartial = db((db.course_activity.assignation==project.id)&(db.course_activity.semester==period.id)&(db.course_activity.name==partial.name)&(db.course_activity.laboratory==False)).select().first()
                if activityPartial is not None:
                    averageA = db.executesql('select avg(grade) as average from grades where activity='+str(activityPartial.id)+';',as_dict=True)
                    for d0 in averageA:
                        if d0['average']!=None:
                            average=float(round(d0['average'],2))
                infoeLevelTemp.append(str(average))
            #FINAL TEST
            average=0
            activityFinal = db((db.course_activity.assignation==project.id)&(db.course_activity.semester==period.id)&(db.course_activity.name=='Examen Final')&(db.course_activity.laboratory==False)).select().first()
            if activityFinal is not None:
                averageA = db.executesql('select avg(grade) as average from grades where activity='+str(activityFinal.id)+';',as_dict=True)
                for d0 in averageA:
                    if d0['average']!=None:
                        average=float(round(d0['average'],2))
            infoeLevelTemp.append(str(average))
            #CLASS AND LABORATORY
            totalWinLaboratory=0
            totalWinClass=0

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
                    categoriesClass.append([categories,0])

            #GRADE OF STUDENT
            for student in students:
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
                            if grade_Laboratory>=61:
                                totalWinLaboratory=totalWinLaboratory+1
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
                            grade_Laboratory=float((grade_Laboratory*float(categoryClass[0].grade))/100)
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
                    totalCarry=int(round(totalCarry,0))+int(round(grade_Laboratory,0))+totalFinal
                    totalCarry = int(round(totalCarry,0))
                    if totalCarry >=61:
                        totalWinClass=totalWinClass+1
            #LABORATORY
            studentsLab = db((db.academic_course_assignation.semester==period.id)&(db.academic_course_assignation.assignation==project.id)&(db.academic_course_assignation.laboratorio==True)).count()
            if studentsLab>0:
                totalWinLaboratory=round(((totalWinLaboratory*100)/studentsLab),2)
            infoeLevelTemp.append(totalWinLaboratory)
            #CLASS
            if len(students)>0:
                totalWinClass=round(((totalWinClass*100)/len(students)),2)
            infoeLevelTemp.append(totalWinClass)
            infoLevel.append(infoeLevelTemp)
    return dict(groupPeriods=groupPeriods, period=period, infoLevel=infoLevel, controlP=controlP)



#*************************************************************************************************************************************
#*************************************************************************************************************************************
#**************************************************REPORT HISTORIC COURSE*************************************************************
@auth.requires_login()
@auth.requires(auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
def historic_course_export():
    infoLevel = []
    period = None
    project = None
    try:
        #CHECK IF THE TYPE OF EXPORT IS VALID
        if request.vars['list_type'] is None or str(request.vars['list_type'])!="csv":
            session.flash = T('Not valid Action.')
            redirect(URL('default','index'))

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
            groupProjects = db((db.project.area_level==area.id)&
                        (db.user_project.project==db.project.id)&
                        (db.user_project.period == db.period_year.id)&
                        ((db.user_project.period <= period.id)&
                        ((db.user_project.period + db.user_project.periods) > period.id))).select(db.project.ALL, orderby=db.project.name, distinct=True)
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
    infoeLevelTemp.append(T('Historic per course'))
    infoLevel.append(infoeLevelTemp)
    #DESCRIPTION OF REPORT
    infoeLevelTemp=[]
    infoeLevelTemp.append(T('Description'))
    infoeLevelTemp.append(T('Report on the historic course information.'))
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
        #HEAD OF TABLE
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Course'))
        infoeLevelTemp.append(T('Total number of students assigned to the course'))
        infoeLevelTemp.append(T('Passed the course'))
        infoeLevelTemp.append(T('Reprobate the course'))
        infoeLevelTemp.append(T('Number of sections'))
        infoLevel.append(infoeLevelTemp)
        nameCourses = []
        #Fill all the courses once time
        for project in groupProjects:
            #Get only name
            nameC = get_name(project)
            #Get unique name
            nameC = get_unique_name(nameC)
            #Fill the name of the courses
            exits = False
            for iterator in nameCourses:
                if iterator==nameC:
                    exits=True
                    break
            if exits==False:
                nameCourses.append(nameC)
        #FOR COURSE
        for course in nameCourses:
            sections = db((db.project.name.like('%'+course+'%'))&
                        (db.user_project.project==db.project.id)&
                        (db.user_project.period == db.period_year.id)&
                        ((db.user_project.period <= period.id)&
                        ((db.user_project.period + db.user_project.periods) > period.id))).select(db.project.ALL, orderby=db.project.name, distinct=True)
            infoeLevelTemp=[]
            infoeLevelTemp.append(course)
            infoeLevelTemp.append(0)
            infoeLevelTemp.append(0)
            infoeLevelTemp.append(0)
            infoeLevelTemp.append(len(sections))
            for project in sections:
                #Total Students in section
                students = db((db.academic_course_assignation.semester==period.id)&(db.academic_course_assignation.assignation==project.id)).select()
                infoeLevelTemp[1]=infoeLevelTemp[1]+len(students)

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
                        categoriesClass.append([categories,0])

                #GRADE OF STUDENT
                for student in students:
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
                                grade_Laboratory=float((grade_Laboratory*float(categoryClass[0].grade))/100)
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
                        totalCarry=int(round(totalCarry,0))+int(round(grade_Laboratory,0))+totalFinal
                        totalCarry = int(round(totalCarry,0))
                        if totalCarry>=61:
                            infoeLevelTemp[2]=infoeLevelTemp[2]+1
                        else:
                            infoeLevelTemp[3]=infoeLevelTemp[3]+1
            infoLevel.append(infoeLevelTemp)
    #PROJECT
    elif request.vars['level']=='2':
        nameCourses = []
        #Get only name
        nameC = get_name(project)
        #Get unique name
        nameC = get_unique_name(nameC)
        #Fill the name of the courses
        nameCourses.append(nameC)
        #HEAD OF TABLE
        #PERIOD OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Course'))
        infoeLevelTemp.append(nameC)
        infoLevel.append(infoeLevelTemp)
        #MIDDLE LINE OF REPORT
        infoeLevelTemp=[]
        infoLevel.append(infoeLevelTemp)
        #LABLE DETAIL OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Detail'))
        infoLevel.append(infoeLevelTemp)
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Section'))
        infoeLevelTemp.append(T('Total number of students assigned to the course'))
        infoeLevelTemp.append(T('Passed the course'))
        infoeLevelTemp.append(T('Reprobate the course'))
        infoLevel.append(infoeLevelTemp)
        #FOR COURSE
        for course in nameCourses:
            sections = db((db.project.name.like('%'+course+'%'))&
                        (db.user_project.project==db.project.id)&
                        (db.user_project.period == db.period_year.id)&
                        ((db.user_project.period <= period.id)&
                        ((db.user_project.period + db.user_project.periods) > period.id))).select(db.project.ALL, orderby=db.project.name, distinct=True)
            for project in sections:
                infoeLevelTemp=[]
                infoeLevelTemp.append(project.name)
                infoeLevelTemp.append(0)
                infoeLevelTemp.append(0)
                infoeLevelTemp.append(0)
                #Total Students in section
                students = db((db.academic_course_assignation.semester==period.id)&(db.academic_course_assignation.assignation==project.id)).select()
                infoeLevelTemp[1]=infoeLevelTemp[1]+len(students)

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
                        categoriesClass.append([categories,0])

                #GRADE OF STUDENT
                for student in students:
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
                                grade_Laboratory=float((grade_Laboratory*float(categoryClass[0].grade))/100)
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
                        totalCarry=int(round(totalCarry,0))+int(round(grade_Laboratory,0))+totalFinal
                        totalCarry = int(round(totalCarry,0))
                        if totalCarry>=61:
                            infoeLevelTemp[2]=infoeLevelTemp[2]+1
                        else:
                            infoeLevelTemp[3]=infoeLevelTemp[3]+1
                infoLevel.append(infoeLevelTemp)
    return dict(filename='HistoricoPorCurso', csvdata=infoLevel)

@auth.requires_login()
@auth.requires(auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
def historic_course():
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

            #groupProjects = db(db.project.area_level==area.id).select(orderby=db.project.name)
            groupProjects = db((db.project.area_level==area.id)&
                        (db.user_project.project==db.project.id)&
                        (db.user_project.period == db.period_year.id)&
                        ((db.user_project.period <= period.id)&
                        ((db.user_project.period + db.user_project.periods) > period.id))).select(db.project.ALL, orderby=db.project.name, distinct=True)
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
        nameCourses = []
        #Fill all the courses once time
        for project in groupProjects:
            #Get only name
            nameC = get_name(project)
            #Get unique name
            nameC = get_unique_name(nameC)
            #Fill the name of the courses
            exits = False
            for iterator in nameCourses:
                if iterator==nameC:
                    exits=True
                    break
            if exits==False:
                nameCourses.append(nameC)
        #FOR COURSE
        for course in nameCourses:
            sections = db((db.project.name.like('%'+course+'%'))&
                        (db.user_project.project==db.project.id)&
                        (db.user_project.period == db.period_year.id)&
                        ((db.user_project.period <= period.id)&
                        ((db.user_project.period + db.user_project.periods) > period.id))).select(db.project.ALL, orderby=db.project.name, distinct=True)
            infoeLevelTemp=[]
            infoeLevelTemp.append(sections.first().id)
            infoeLevelTemp.append(course)
            infoeLevelTemp.append(0)
            infoeLevelTemp.append(0)
            infoeLevelTemp.append(0)
            infoeLevelTemp.append(len(sections))
            for project in sections:
                #Total Students in section
                students = db((db.academic_course_assignation.semester==period.id)&(db.academic_course_assignation.assignation==project.id)).select()
                infoeLevelTemp[2]=infoeLevelTemp[2]+len(students)

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
                        categoriesClass.append([categories,0])

                #GRADE OF STUDENT
                for student in students:
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
                                grade_Laboratory=float((grade_Laboratory*float(categoryClass[0].grade))/100)
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
                        totalCarry=int(round(totalCarry,0))+int(round(grade_Laboratory,0))+totalFinal
                        totalCarry = int(round(totalCarry,0))
                        if totalCarry>=61:
                            infoeLevelTemp[3]=infoeLevelTemp[3]+1
                        else:
                            infoeLevelTemp[4]=infoeLevelTemp[4]+1
            infoLevel.append(infoeLevelTemp)
    #PROJECT
    elif request.vars['level']=='2':
        nameCourses = []
        #Get only name
        nameC = get_name(project)
        #Get unique name
        nameC = get_unique_name(nameC)
        #Fill the name of the courses
        nameCourses.append(nameC)
        #FOR COURSE
        for course in nameCourses:
            sections = db((db.project.name.like('%'+course+'%'))&
                        (db.user_project.project==db.project.id)&
                        (db.user_project.period == db.period_year.id)&
                        ((db.user_project.period <= period.id)&
                        ((db.user_project.period + db.user_project.periods) > period.id))).select(db.project.ALL, orderby=db.project.name, distinct=True)
            for project in sections:
                infoeLevelTemp=[]
                infoeLevelTemp.append(project.name)
                infoeLevelTemp.append(0)
                infoeLevelTemp.append(0)
                infoeLevelTemp.append(0)
                #Total Students in section
                students = db((db.academic_course_assignation.semester==period.id)&(db.academic_course_assignation.assignation==project.id)).select()
                infoeLevelTemp[1]=infoeLevelTemp[1]+len(students)

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
                        categoriesClass.append([categories,0])

                #GRADE OF STUDENT
                for student in students:
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
                                grade_Laboratory=float((grade_Laboratory*float(categoryClass[0].grade))/100)
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
                        totalCarry=int(round(totalCarry,0))+int(round(grade_Laboratory,0))+totalFinal
                        totalCarry = int(round(totalCarry,0))
                        if totalCarry>=61:
                            infoeLevelTemp[2]=infoeLevelTemp[2]+1
                        else:
                            infoeLevelTemp[3]=infoeLevelTemp[3]+1
                infoLevel.append(infoeLevelTemp)
        project=nameC
    return dict(groupPeriods=groupPeriods, period=period, infoLevel=infoLevel, project=project)



#*************************************************************************************************************************************
#*************************************************************************************************************************************
#**************************************************REPORT PERCENTAGE CHANGE GRADES****************************************************
@auth.requires_login()
@auth.requires(auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
def percentage_change_grades_export():
    infoLevel = []
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
            #groupProjects = db(db.project.area_level==area.id).select(orderby=db.project.name)
            groupProjects = db((db.project.area_level==area.id)&
                        (db.user_project.project==db.project.id)&
                        (db.user_project.period == db.period_year.id)&
                        ((db.user_project.period <= period.id)&
                        ((db.user_project.period + db.user_project.periods) > period.id))).select(db.project.ALL, orderby=db.project.name, distinct=True)
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
    infoeLevelTemp.append(T('Historic per course'))
    infoLevel.append(infoeLevelTemp)
    #DESCRIPTION OF REPORT
    infoeLevelTemp=[]
    infoeLevelTemp.append(T('Description'))
    infoeLevelTemp.append(T('Report on the historic course information.'))
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
        nameCourses = []
        #HEADER
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Course'))
        infoeLevelTemp.append(T('Percent Change'))
        infoeLevelTemp.append(T('Number of sections'))
        infoLevel.append(infoeLevelTemp)
        nameCourses = []
        #Fill all the courses once time
        for project in groupProjects:
            #Get only name
            nameC = get_name(project)
            #Get unique name
            nameC = get_unique_name(nameC)
            #Fill the name of the courses
            exits = False
            for iterator in nameCourses:
                if iterator==nameC:
                    exits=True
                    break
            if exits==False:
                nameCourses.append(nameC)
        #TOTAL OF CHANGES
        totalChanges = db((db.grades_log.yearp==period.yearp)&(db.grades_log.period==T(period.period.name))&((db.grades_log.operation_log=='update')|(db.grades_log.operation_log=='delete'))).count()
        #FOR COURSE
        for course in nameCourses:
            #sections = db(db.project.name.like('%'+course+'%')).select()
            sections = db((db.project.name.like('%'+course+'%'))&
                        (db.user_project.project==db.project.id)&
                        (db.user_project.period == db.period_year.id)&
                        ((db.user_project.period <= period.id)&
                        ((db.user_project.period + db.user_project.periods) > period.id))).select(db.project.ALL, orderby=db.project.name, distinct=True)
            infoeLevelTemp=[]
            infoeLevelTemp.append(course)
            infoeLevelTemp.append(0)
            infoeLevelTemp.append(len(sections))
            if totalChanges>0:
                for project in sections:
                    infoeLevelTemp[1]+=db((db.grades_log.yearp==period.yearp)&(db.grades_log.period==T(period.period.name))&(db.grades_log.project==project.name)&((db.grades_log.operation_log=='update')|(db.grades_log.operation_log=='delete'))).count()
                infoeLevelTemp[1] = round(((float(infoeLevelTemp[1])*float(100))/float(totalChanges)),2)
            infoLevel.append(infoeLevelTemp)
    else:
        #Get only name
        nameC = get_name(project)
        #Get unique name
        nameC = get_unique_name(nameC)
        #TOTAL OF CHANGES
        totalChanges = 0
        #FOR COURSE
        rolesC=db(db.grades_log).select(db.grades_log.roll, distinct=True)
        #PROJECT OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Course'))
        infoeLevelTemp.append(nameC)
        infoLevel.append(infoeLevelTemp)
        #MIDDLE LINE OF REPORT
        infoeLevelTemp=[]
        infoLevel.append(infoeLevelTemp)
        #LABLE DETAIL OF REPORT
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Detail'))
        infoLevel.append(infoeLevelTemp)
        nameCourses = []
        #HEADER
        infoeLevelTemp=[]
        infoeLevelTemp.append(T('Section'))
        for rc in rolesC:
            infoeLevelTemp.append(T('Percent Change')+' '+T('Rol '+rc.roll))
        infoLevel.append(infoeLevelTemp)
        #sections = db(db.project.name.like('%'+nameC+'%')).select()
        sections = db((db.project.name.like('%'+nameC+'%'))&
                        (db.user_project.project==db.project.id)&
                        (db.user_project.period == db.period_year.id)&
                        ((db.user_project.period <= period.id)&
                        ((db.user_project.period + db.user_project.periods) > period.id))).select(db.project.ALL, orderby=db.project.name, distinct=True)
        for section in sections:
            totalChanges+=db((db.grades_log.yearp==period.yearp)&(db.grades_log.period==T(period.period.name))&(db.grades_log.project==section.name)&((db.grades_log.operation_log=='update')|(db.grades_log.operation_log=='delete'))).count()
        for section in sections:
            infoeLevelTemp=[]
            infoeLevelTemp.append(section.name)
            for rc in rolesC:
                infoeLevelTemp.append(0)
            if totalChanges>0:
                position=1
                for rc in rolesC:
                    infoeLevelTemp[position]+=db((db.grades_log.yearp==period.yearp)&(db.grades_log.period==T(period.period.name))&(db.grades_log.project==section.name)&(db.grades_log.roll==rc.roll)&((db.grades_log.operation_log=='update')|(db.grades_log.operation_log=='delete'))).count()
                    infoeLevelTemp[position] = round(((float(infoeLevelTemp[position])*float(100))/float(totalChanges)),2)
                    position+=1
            infoLevel.append(infoeLevelTemp)
    return dict(filename='PorcentajeCambioNotas', csvdata=infoLevel)


@auth.requires_login()
@auth.requires(auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
def percentage_change_grades():
    infoLevel = []
    groupPeriods = None
    period = None
    project = None
    rolesC=None
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

            #groupProjects = db(db.project.area_level==area.id).select(orderby=db.project.name)
            groupProjects = db((db.project.area_level==area.id)&
                        (db.user_project.project==db.project.id)&
                        (db.user_project.period == db.period_year.id)&
                        ((db.user_project.period <= period.id)&
                        ((db.user_project.period + db.user_project.periods) > period.id))).select(db.project.ALL, orderby=db.project.name, distinct=True)
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
        nameCourses = []
        #Fill all the courses once time
        for project in groupProjects:
            #Get only name
            nameC = get_name(project)
            #Get unique name
            nameC = get_unique_name(nameC)
            #Fill the name of the courses
            exits = False
            for iterator in nameCourses:
                if iterator==nameC:
                    exits=True
                    break
            if exits==False:
                nameCourses.append(nameC)
        #TOTAL OF CHANGES
        totalChanges = db((db.grades_log.yearp==period.yearp)&(db.grades_log.period==T(period.period.name))&((db.grades_log.operation_log=='update')|(db.grades_log.operation_log=='delete'))).count()
        #FOR COURSE
        for course in nameCourses:
            #sections = db(db.project.name.like('%'+course+'%')).select()
            sections = db((db.project.name.like('%'+course+'%'))&
                        (db.user_project.project==db.project.id)&
                        (db.user_project.period == db.period_year.id)&
                        ((db.user_project.period <= period.id)&
                        ((db.user_project.period + db.user_project.periods) > period.id))).select(db.project.ALL, orderby=db.project.name, distinct=True)
            infoeLevelTemp=[]
            infoeLevelTemp.append(sections.first().id)
            infoeLevelTemp.append(course)
            infoeLevelTemp.append(0)
            infoeLevelTemp.append(len(sections))
            if totalChanges>0:
                for project in sections:
                    infoeLevelTemp[2]+=db((db.grades_log.yearp==period.yearp)&(db.grades_log.period==T(period.period.name))&(db.grades_log.project==project.name)&((db.grades_log.operation_log=='update')|(db.grades_log.operation_log=='delete'))).count()
                infoeLevelTemp[2] = round(((float(infoeLevelTemp[2])*float(100))/float(totalChanges)),2)
            infoLevel.append(infoeLevelTemp)
    else:
        #Get only name
        nameC = get_name(project)
        #Get unique name
        nameC = get_unique_name(nameC)
        #TOTAL OF CHANGES
        totalChanges = 0
        #FOR COURSE
        rolesC=db(db.grades_log).select(db.grades_log.roll, distinct=True)
        #sections = db(db.project.name.like('%'+nameC+'%')).select()
        sections = db((db.project.name.like('%'+nameC+'%'))&
                        (db.user_project.project==db.project.id)&
                        (db.user_project.period == db.period_year.id)&
                        ((db.user_project.period <= period.id)&
                        ((db.user_project.period + db.user_project.periods) > period.id))).select(db.project.ALL, orderby=db.project.name, distinct=True)
        for section in sections:
            totalChanges+=db((db.grades_log.yearp==period.yearp)&(db.grades_log.period==T(period.period.name))&(db.grades_log.project==section.name)&((db.grades_log.operation_log=='update')|(db.grades_log.operation_log=='delete'))).count()
        for section in sections:
            infoeLevelTemp=[]
            infoeLevelTemp.append(section.name)
            for rc in rolesC:
                infoeLevelTemp.append(0)
            if totalChanges>0:
                position=1
                for rc in rolesC:
                    infoeLevelTemp[position]+=db((db.grades_log.yearp==period.yearp)&(db.grades_log.period==T(period.period.name))&(db.grades_log.project==section.name)&(db.grades_log.roll==rc.roll)&((db.grades_log.operation_log=='update')|(db.grades_log.operation_log=='delete'))).count()
                    infoeLevelTemp[position] = round(((float(infoeLevelTemp[position])*float(100))/float(totalChanges)),2)
                    position+=1
            infoLevel.append(infoeLevelTemp)
        project=nameC
    return dict(groupPeriods=groupPeriods, period=period, infoLevel=infoLevel, project=project, rolesC=rolesC)