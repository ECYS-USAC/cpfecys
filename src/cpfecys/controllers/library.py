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
            periods = db((db.period_year.id == db.user_project.period)&(db.user_project.assigned_user==auth.user.id)).select(db.period_year.id, db.period_year.yearp, db.period_year.period, distinct = True)
        return periods
    #The list of the projects
    def obtainProjects(period):
        rproject = db((db.user_project.assigned_user==auth.user.id)&(db.user_project.period==period)).select()
        return rproject
    #The list of the final students
    def obtainStudents(project):
        persons = db((db.user_project.project == project.project)&(db.user_project.period==project.period)&(db.auth_membership.user_id==db.user_project.assigned_user)&(db.auth_membership.group_id==2)).select()
        return persons
    #Type of rol
    def obtenerRol():
        try:
            rol = db(db.auth_membership.user_id==auth.user.id).select()
            nrol = 0
            for s in rol:
                nrol = s.group_id
        except:
            session.flash = T('Not valid Action.')
            redirect(URL('default', 'index'))
        return nrol
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
        if tipo != '0':
            project = int(pro)+0
            check = db.user_project(id = project)
            year = db.period_year(id=check.period)
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
            db.library.period.default = check.period
            db.library.owner_file.writable = False
            db.library.owner_file.readable = False
            db.library.owner_file.default = check.assigned_user

            nameProject = check.project.name
            nameSemester = T(year_semester.name)
            nameYear = year.yearp

            if tipo=='1':
                usernombre=check.assigned_user.first_name
                query = ((db.library.owner_file==check.assigned_user)&(db.library.project==check.project)&(db.library.period==check.period))
                if period.id == year.id:
                    grid = SQLFORM.grid(query, csv=False, paginate=5)
                else:
                    links = [lambda row: A('Enlazar Semestre Actual',_href=URL("library","change_period",args=[row.id]))]
                    grid = SQLFORM.grid(query, links=links, csv=False, paginate=5)
            elif tipo=='2':
                db.library.owner_file.readable = True
                query = ((db.library.visible==True)&(db.library.owner_file!=check.assigned_user)&(db.library.project==check.project)&(db.library.period==check.period))
                grid = SQLFORM.grid(query, csv=False, create=False, editable=False, deletable=False, paginate=5)
                usernombre=T('Share')
            elif tipo=='3':
                usernombre=check.assigned_user.first_name
                query = ((db.library.owner_file==check.assigned_user)&(db.library.project==check.project)&(db.library.period==check.period))
                if period.id == year.id:
                    grid = SQLFORM.grid(query, csv=False, paginate=5)
                else:
                    links = [lambda row: A('Enlazar Semestre Actual',_href=URL("library","change_period",args=[row.id]))]
                    grid = SQLFORM.grid(query, links=links, csv=False, paginate=5)
            elif tipo=='4':
                usernombre=check.assigned_user.first_name
                query = ((db.library.owner_file==check.assigned_user)&(db.library.project==check.project)&(db.library.period==check.period))
                grid = SQLFORM.grid(query, csv=False, create=False, editable=False, deletable=False, paginate=5)
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

    return dict(obtainPeriods = obtainPeriods, obtainProjects=obtainProjects, obtainStudents=obtainStudents, obtenerRol=obtenerRol, existeRegistro=existeRegistro, grid=grid, name = nameProject,semester=nameSemester,year=nameYear,usernombre=usernombre)

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
            project2 = db((db.user_project.project==f.project)&(db.user_project.assigned_user==f.owner_file)&(db.user_project.period==period)).select(count2)
            total2=2
            for s2 in project2:
                total2 = s2[count2]
            if total2 == 1:
                db.library.insert(name=f.name,file_data=f.file_data,description=f.description,visible=f.visible,period=period,project=f.project,owner_file=f.owner_file)
                session.flash  =T('The file was copy to the actual semester')
            else:
                session.flash  ='El archivo no se puede copiar, ya que no tiene asignado el curso en el semestre actual'
            redirect(URL('library','file_managers'))
        else:
            session.flash  =T('The file already exists')
            redirect(URL('library','file_managers'))