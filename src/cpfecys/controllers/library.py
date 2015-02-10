@auth.requires_login()
@auth.requires(auth.has_membership('Student') or auth.has_membership('Teacher') or auth.has_membership('Academic'))
def file_managers():
    #The list of periods
    def obtainPeriods(func):
        if func == 1:
            try:
                academic_var = db.academic(db.academic.id_auth_user==auth.user.id)        
                period_list = db(db.academic_course_assignation.carnet==academic_var.id).select(db.academic_course_assignation.semester,distinct=True)
                periods = period_list
            except:
                periods = []
        else:
            periods = db( ((db.user_project.period <= db.period_year.id) & ((db.user_project.period + db.user_project.periods) > db.period_year.id)) &(db.user_project.assigned_user==auth.user.id)).select(db.period_year.id, db.period_year.yearp, db.period_year.period, distinct = True)
        return periods
    #The list of the projects
    def obtainProjects(func,period):
        if func == 1:
            try:
                academic_var = db.academic(db.academic.id_auth_user==auth.user.id)        
                rproject = db((db.academic_course_assignation.carnet==academic_var.id)&(db.academic_course_assignation.semester==period)).select()
            except:
                rproject = []
        else:
            rproject = db((db.user_project.assigned_user==auth.user.id)&((db.user_project.period <= period) & ((db.user_project.period + db.user_project.periods) > period)) ).select()
        return rproject
    #The list of the final students
    def obtainStudents(project):
        persons = db((db.user_project.project == project.project)&((db.user_project.period <= project.period) & ((db.user_project.period + db.user_project.periods) > project.period))&(db.auth_membership.user_id==db.user_project.assigned_user)&(db.auth_membership.group_id==2)).select()
        return persons
    
    #Existe alguna accion
    def existeRegistro():
        resultado=False
        if (session.library_tipo_vars != '0' and session.library_pro_vars != '0'):
            resultado = True
        return resultado

    tipo=None
    pro=None
    grid=None
    if request.vars['tipo'] ==None:
        if session.library_tipo_vars != None:
            tipo = session.library_tipo_vars
    else:
        tipo = request.vars['tipo']
        session.library_tipo_vars = tipo

    if request.vars['pro'] ==None:
        if session.library_pro_vars != None:
            pro = session.library_pro_vars
    else:
        pro = request.vars['pro']
        session.library_pro_vars = pro

    grid = None
    if tipo != None and pro != None:
        if tipo=='5':
            academic_var = db.academic(db.academic.id_auth_user==auth.user.id)        
            if request.vars['semester'] is not None:
                session.library_semester = request.vars['semester']
            project = db((db.academic_course_assignation.carnet==academic_var.id)&(db.academic_course_assignation.assignation==session.library_pro_vars)&(db.academic_course_assignation.semester==session.library_semester)).select().first()
            if project is None:
                session.flash = T('Not valid Action.')
                redirect(URL('default', 'index'))
            else:
                
                query = ((db.library.project==project.assignation)&(db.library.period==project.semester)&(db.library.visible==True))
                db.library.period.readable = False
                db.library.project.readable = False
                db.library.visible.readable = False
                db.library.owner_file.readable = False
                grid = SQLFORM.grid(query, csv=False, create=False, editable=False, deletable=False, paginate=9, searchable=False)
                nameProject = project.assignation.name
                nameSemester = project.semester.period.name
                nameYear = project.semester.yearp
                usernombre=''
        elif tipo != '0':
            project = int(pro)+0
            check = db.user_project(id = project)
            year = db.period_year(id=request.vars["semester"])
            year_semester = db.period(id=year.period)
            #Obtain the current period of year
            period = cpfecys.current_year_period()
            #Check the fields
            db.library.id.readable = False
            db.library.id.writable = False
            db.library.project.readable = False
            db.library.project.writable = False
            db.library.project.default = check.project
            db.library.period.readable = False
            db.library.period.writable = False
            db.library.period.default = year.id
            db.library.owner_file.writable = False
            db.library.owner_file.readable = False
            db.library.owner_file.default = check.assigned_user

            nameProject = check.project.name
            nameSemester = T(year_semester.name)
            nameYear = year.yearp
            
            rproject = db((db.user_project.assigned_user==auth.user.id)&((db.user_project.period <= year.id) & ((db.user_project.period + db.user_project.periods) > year.id)) ).select()
            this_project = db((db.user_project.id==pro)).select().first()
            none_access = False
            for var_project in rproject:
                if(var_project.project.id == this_project.project.id):
                    none_access = True

            if none_access == False:
                session.flash = T('Not valid Action.')
                redirect(URL('default', 'index'))

            if tipo=='1':
                usernombre=check.assigned_user.first_name
                query = ((db.library.owner_file==check.assigned_user)&(db.library.project==check.project)&(db.library.period==year.id))
                if period.id == year.id:
                    grid = SQLFORM.grid(query, csv=False, paginate=9, searchable=False)
                else:
                    links = [lambda row: A('Enlazar Semestre Actual',_href=URL("library","change_period",vars = dict(semester=request.vars["semester"]),args=[row.id]))]
                    grid = SQLFORM.grid(query, links=links, create=False, editable=False, csv=False, paginate=9, searchable=False)
            elif tipo=='2':
                db.library.owner_file.readable = True
                query = ((db.library.visible==True)&(db.library.owner_file!=check.assigned_user)&(db.library.project==check.project)&(db.library.period==year.id))
                grid = SQLFORM.grid(query, csv=False, create=False, editable=False, deletable=False, paginate=9, searchable=False)
                usernombre=T('Share')
            elif tipo=='3':
                usernombre=check.assigned_user.first_name
                query = ((db.library.owner_file==check.assigned_user)&(db.library.project==check.project)&(db.library.period==year.id))
                if period.id == year.id:
                    grid = SQLFORM.grid(query, csv=False, paginate=9, searchable=False)
                else:
                    links = [lambda row: A('Enlazar Semestre Actual',_href=URL("library","change_period",vars = dict(semester=request.vars["semester"]),args=[row.id]))]
                    grid = SQLFORM.grid(query, links=links, create=False, editable=False, csv=False, paginate=9, searchable=False)
            elif tipo=='4':
                usernombre=check.assigned_user.first_name
                query = ((db.library.owner_file==check.assigned_user)&(db.library.project==check.project)&(db.library.period==year.id))
                grid = SQLFORM.grid(query, csv=False, create=False, editable=False, deletable=False, paginate=9, searchable=False)
            else:
                session.flash = T('Not valid Action.')
                redirect(URL('default', 'index'))
        else:
            nameProject = ''
            nameSemester = ''
            nameYear = ''
            usernombre=''
    else:
        session.flash = T('Not valid Action.')
        redirect(URL('default', 'index'))

    return dict(obtainPeriods = obtainPeriods, 
                obtainProjects=obtainProjects, 
                obtainStudents=obtainStudents, 
                existeRegistro=existeRegistro, 
                grid=grid, 
                name = nameProject,
                semester=nameSemester,
                year=nameYear,
                usernombre=usernombre)

@auth.requires_login()
@auth.requires(auth.has_membership('Student') or auth.has_membership('Teacher') or auth.has_membership('Academic'))
def change_period():
    idFile = request.args(0)
    period = cpfecys.current_year_period()

    newFile = db(db.library.id==idFile).select()
    for f in newFile:
        count = db.library.id.count()
        notices  = db((db.library.name==f.name)&(db.library.file_data==f.file_data)&(db.library.description==f.description)&(db.library.visible==f.visible)&(db.library.period==period)&(db.library.project==f.project)&(db.library.owner_file==f.owner_file)).select(count)
        total = 0
        for s in notices:
            total = s[count]

        if total == 0:
            count2 = db.user_project.id.count()
            project2 = db((db.user_project.project==f.project)&(db.user_project.assigned_user==f.owner_file)&((db.user_project.period <= period) & ((db.user_project.period + db.user_project.periods) > period))).select(count2)
            total2=2
            for s2 in project2:
                total2 = s2[count2]
            if total2 == 1:
                db.library.insert(name=f.name,file_data=f.file_data,description=f.description,visible=f.visible,period=period,project=f.project,owner_file=f.owner_file)
                session.flash  =T('The file was copy to the actual semester')
            else:
                session.flash  ='El archivo no se puede copiar, ya que no tiene asignado el curso en el semestre actual'
            redirect(URL('library','file_managers',vars = dict(semester=request.vars["semester"])))
        else:
            session.flash  =T('The file already exists')
            redirect(URL('library','file_managers',vars = dict(semester=request.vars["semester"])))