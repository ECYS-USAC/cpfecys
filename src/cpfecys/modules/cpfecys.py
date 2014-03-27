#!/usr/bin/env python
# coding: utf8
from gluon import *

#Variable Definitions
_db = None
_auth = None
_scheduler = None
_auto_daily = None
first_period = None
second_period = None
first_period_name = None
second_period_name = None

def setup(db, auth, scheduler, auto_daily):
    global _db, _auth, _scheduler, _auto_daily
    _db = db
    _auth = auth
    _auto_daily = auto_daily
    _scheduler = scheduler
    _database_setup()
    _module_variables_setup()
    _period_setup()

def force_student_data_update(path, ignore_paths):
    #User updated data validation
    if _auth.user != None:
        groups = _db((_db.auth_membership.user_id==_auth.user.id)& \
                        (_db.auth_group.role=='Student')& \
                        (_db.auth_group.id==_db.auth_membership.group_id)). \
                        select().first()
        if (groups is None):
            return
        data_updated = _db.auth_user(_db.auth_user.id==_auth.user.id).data_updated
        if data_updated:
            return
        if any(s in path for s in ignore_paths):
            return
        redirect(URL('student','update_data'))

def current_year_period():
    db = _db
    import datetime
    cdate = datetime.datetime.now()
    cyear = cdate.year
    cmonth = cdate.month
    period = second_period
    #current period depends if we are in dates between jan-jun and jul-dec
    if cmonth < 7 :
        period = first_period
    return db.period_year((db.period_year.yearp == cyear)&
                          (db.period_year.period == period))

def get_markmin():
    LATEX = '<img src="http://chart.apis.google.com/chart?cht=tx&chl=%s" align="center"/>'
    markmin_settings = {
            'latex':lambda code: LATEX % code.replace('"','"'),
            'code_cpp':lambda text: CODE(text,language='cpp').xml(),
            'code_java':lambda text: CODE(text,language='java').xml(),
            'code_python':lambda text: CODE(text,language='python').xml(),
            'code_html':lambda text: CODE(text,language='html').xml()}
    return markmin_settings

## Validate the assignation is unlocked and accepts modifications or not
def assignation_is_locked(assignation):
    return not assignation.assignation_status is None

## Validate that the report date restriction and is_enabled restriction apply to current date
def student_validation_report_restrictions(report_restriction):
    db = _db
    import datetime
    current_date = datetime.datetime.now()
    rep_restr = db((db.report_restriction.id == report_restriction)&
        (db.report_restriction.start_date <= current_date)&
        (db.report_restriction.end_date >= current_date)&
        (db.report_restriction.is_enabled == True)).select().first()
    return rep_restr != None

## Validate that the report status is editable (it is either 'Draft' or 'Recheck')
def student_validation_report_status(report):
    db = _db
    return (report.status == db.report_status(db.report_status.name == 'Draft').id) or \
            (report.status == db.report_status(db.report_status.name == 'Recheck').id)

def student_validation_report_owner(report):
    db = _db
    auth = _auth
    usr_rep = db((db.report.id == report)&
            (db.report.assignation == db.user_project.id)&
            (db.user_project.assigned_user == auth.user.id)).select().first()
    return usr_rep != None

def teacher_validation_report_access(report):
    db = _db
    auth = _auth
    report = db(db.report.id==report).select().first()
    if report == None or report.assignation.project == None:
        return False
    project = report.assignation.project
    assignation = db((db.user_project.assigned_user==auth.user.id)&
                (db.user_project.project==project.id))
    return assignation != None

#
# automatically tries to create the next period in may and november respectively
# Using the following logic:
# - In May..Dec the second period of current year is created.
# - In Nov the first period of next year is created.
# - In Jan..Apr the first period of current year is created.
#
def _period_setup():
    db = _db
    import datetime
    now = datetime.datetime.now()
    year = now.year
    if now.month >= 5:
        #check and create second semester of current year
        pery = db.period_year((db.period_year.yearp == year)&
                              (db.period_year.period == second_period))
        if not pery:
            db.period_year.insert(yearp = year, period = second_period)
    else:
        #check and create first semester of current year
        pery = db.period_year((db.period_year.yearp == year)&
                              (db.period_year.period == first_period))
        if not pery:
            db.period_year.insert(yearp = year, period = first_period)
    if now.month >= 11:
        #check and create first semester of next year
        pery = db.period_year((db.period_year.yearp == (year + 1))&
                              (db.period_year.period == first_period))
        if not pery:
            db.period_year.insert(yearp = (year + 1), period = first_period)

def _database_setup():
    global first_period_name, second_period_name
    first_period_name = 'First Semester'
    second_period_name = 'Second Semester'
    db = _db
    ## Super-Administrator:
    setup = db.setup(done = True)
    if setup is None:
        _days_of_week_setup()
        _report_status_setup()
        _item_type_setup()
        _log_type_setup()
        _projects_setup()
        _roles_setup()
        _setup_parameters()
        _report_requirements()
        _assignation_status()
        _start_scheduler()
        db.setup.insert(done = True)

def _days_of_week_setup():
    db.day_of_week.insert(name = T('Monday'))
    db.day_of_week.insert(name = T('Tuesday'))
    db.day_of_week.insert(name = T('Wednesday'))
    db.day_of_week.insert(name = T('Thursday'))
    db.day_of_week.insert(name = T('Friday'))
    db.day_of_week.insert(name = T('Saturday'))
    db.day_of_week.insert(name = T('Sunday'))

def _assignation_status():
    db = _db
    db.assignation_status.insert(name = 'Failed')
    db.assignation_status.insert(name = 'Successful')

# Scheduler automatically triggered when setting up the system. Daily at midnight
def _start_scheduler():
    scheduler = _scheduler
    auto_daily = _auto_daily
    import datetime
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    tomorrow = datetime.datetime(tomorrow.year, tomorrow.month, tomorrow.day)
    scheduler.queue_task(auto_daily, start_time = tomorrow, period = (3600)*24, repeats = 0, timeout=600)

def _report_requirements():
    db = _db
    #default requirements
    heading = db.report_requirement.insert(name = 'Encabezado')
    footer = db.report_requirement.insert(name = 'Pie de Reporte')
    activity = db.report_requirement.insert(name = 'Registrar Actividad')
    metrics = db.report_requirement.insert(name = 'Registrar Actividad con Metricas')
    desertions = db.report_requirement.insert(name = 'Registrar Deserciones')
    hours = db.report_requirement.insert(name = 'Registrar Horas Completadas')
    final_r = db.report_requirement.insert(name = 'Registrar Estadisticas Finales de Curso')
    #levels
    lvl_1 = db.area_level(name = "DTT Tutor Académico")
    lvl_2 = db.area_level(name = "DTT Tutor de Comunicación")
    lvl_3 = db.area_level(name = "DTT Tutor de Desarrollo")
    lvl_4 = db.area_level(name = "DTT Tutor de Innovación")
    lvl_5 = db.area_level(name = "DTT Tutor de Investigación")
    lvl_6 = db.area_level(name = "DTT Tutor de Infraestructura")
    #area_report_requirement
    db.area_report_requirement.insert(report_requirement = heading, area_level = lvl_1)
    db.area_report_requirement.insert(report_requirement = heading, area_level = lvl_2)
    db.area_report_requirement.insert(report_requirement = heading, area_level = lvl_3)
    db.area_report_requirement.insert(report_requirement = heading, area_level = lvl_4)
    db.area_report_requirement.insert(report_requirement = heading, area_level = lvl_5)
    db.area_report_requirement.insert(report_requirement = heading, area_level = lvl_6)
    db.area_report_requirement.insert(report_requirement = footer, area_level = lvl_1)
    db.area_report_requirement.insert(report_requirement = footer, area_level = lvl_2)
    db.area_report_requirement.insert(report_requirement = footer, area_level = lvl_3)
    db.area_report_requirement.insert(report_requirement = footer, area_level = lvl_4)
    db.area_report_requirement.insert(report_requirement = footer, area_level = lvl_5)
    db.area_report_requirement.insert(report_requirement = footer, area_level = lvl_6)
    db.area_report_requirement.insert(report_requirement = activity, area_level = lvl_1)
    db.area_report_requirement.insert(report_requirement = activity, area_level = lvl_2)
    db.area_report_requirement.insert(report_requirement = activity, area_level = lvl_3)
    db.area_report_requirement.insert(report_requirement = activity, area_level = lvl_4)
    db.area_report_requirement.insert(report_requirement = activity, area_level = lvl_5)
    db.area_report_requirement.insert(report_requirement = activity, area_level = lvl_6)
    db.area_report_requirement.insert(report_requirement = metrics, area_level = lvl_1)
    db.area_report_requirement.insert(report_requirement = desertions, area_level = lvl_1)
    db.area_report_requirement.insert(report_requirement = final_r, area_level = lvl_1)
    db.area_report_requirement.insert(report_requirement = hours, area_level = lvl_2)
    db.area_report_requirement.insert(report_requirement = hours, area_level = lvl_3)
    db.area_report_requirement.insert(report_requirement = hours, area_level = lvl_4)
    db.area_report_requirement.insert(report_requirement = hours, area_level = lvl_5)
    db.area_report_requirement.insert(report_requirement = hours, area_level = lvl_6)
    return

def _roles_setup():
    db = _db
    auth = _auth
    ## User Roles Setup:
    supersu = db.auth_user.insert(email = 'admin@admin.com', first_name = 'Super',
                                         last_name = 'Administrator', username = 'admin',
                                         password = db.auth_user.password.validate('superadmin')[0])
    superadmins = auth.add_group(role = 'Super-Administrator',description = 'In charge of the whole system administration.')
    auth.add_membership(superadmins, supersu)
    ## Student:
    students = auth.add_group('Student',
                              'User that is enrolled in some practice. Limited access.')
    ## Teacher:
    teachers = auth.add_group('Teacher',
                              'User that evaluates students in some courses. When final practice is teaching.')
    ##  DSI User:
    dsi = auth.add_group('DSI',
                              'User that has some responsabilities related to some control over student activities.')
    auth.add_membership(dsi, supersu)

def _projects_setup():
    db = _db
    semester1 = db.period.insert(name = first_period_name)
    semester2 = db.period.insert(name = second_period_name)
    ## Final Practice Areas of DTT
    lvl_1 = db.area_level.insert(name = "DTT Tutor Académico", description = "")
    lvl_2 = db.area_level.insert(name = "DTT Tutor de Comunicación", description = "")
    lvl_3 = db.area_level.insert(name = "DTT Tutor de Desarrollo", description = "")
    lvl_4 = db.area_level.insert(name = "DTT Tutor de Innovación", description = "")
    lvl_5 = db.area_level.insert(name = "DTT Tutor de Investigación", description = "")
    lvl_6 = db.area_level.insert(name = "DTT Tutor de Infraestructura", description = "")
    ## Creation of standard 'Projects'
    db.project.insert(project_id = '0283A', area_level = lvl_1, name = 'Análisis y Diseño de Sistemas 1 (Sección A)', description = '', physical_location = '')
    db.project.insert(project_id = '0785A', area_level = lvl_1, name = 'Análisis y Diseño de Sistemas 2 (Sección A)', description = '', physical_location = '')
    db.project.insert(project_id = '0785B', area_level = lvl_1, name = 'Análisis y Diseño de Sistemas 2 (Sección B)', description = '', physical_location = '')
    db.project.insert(project_id = '0778A', area_level = lvl_1, name = 'Arquitectura de Computadoras y Ensambladores 1 (Sección A)', description = '', physical_location = '')
    db.project.insert(project_id = '0778B', area_level = lvl_1, name = 'Arquitectura de Computadoras y Ensambladores 1 (Sección B)', description = '', physical_location = '')
    db.project.insert(project_id = '0779A', area_level = lvl_1, name = 'Arquitectura de Computadoras y Ensambladores 2 (Sección A)', description = '', physical_location = '')
    db.project.insert(project_id = '0774A', area_level = lvl_1, name = 'Bases de Datos 1 (Sección A)', description = '', physical_location = '')
    db.project.insert(project_id = '0774B', area_level = lvl_1, name = 'Bases de Datos 1 (Sección B)', description = '', physical_location = '')
    db.project.insert(project_id = '0775A', area_level = lvl_1, name = 'Bases de Datos 2 (Sección A)', description = '', physical_location = '')
    db.project.insert(project_id = '0775B', area_level = lvl_1, name = 'Bases de Datos 2 (Sección B)', description = '', physical_location = '')
    db.project.insert(project_id = '0738A', area_level = lvl_1, name = 'Bases de Datos Avanzadas (Sección A)', description = '', physical_location = '')
    db.project.insert(project_id = '0014A+', area_level = lvl_1, name = 'Economía (Sección A+)', description = '', physical_location = '')
    db.project.insert(project_id = '0014A-', area_level = lvl_1, name = 'Economía (Sección A-)', description = '', physical_location = '')
    db.project.insert(project_id = '0790A', area_level = lvl_1, name = 'Emprendedores de Negocios Informáticos	 (Sección A)', description = '', physical_location = '')
    db.project.insert(project_id = '0772A', area_level = lvl_1, name = 'Estructura de Datos (Sección A)', description = '', physical_location = '')
    db.project.insert(project_id = '0772B', area_level = lvl_1, name = 'Estructura de Datos (Sección B)', description = '', physical_location = '')
    db.project.insert(project_id = '0786N', area_level = lvl_1, name = 'Gerenciales 1 (Sección N)', description = '', physical_location = '')
    db.project.insert(project_id = '0786P', area_level = lvl_1, name = 'Gerenciales 1 (Sección P)', description = '', physical_location = '')
    db.project.insert(project_id = '0787A', area_level = lvl_1, name = 'Gerenciales 2 (Sección A)', description = '', physical_location = '')
    db.project.insert(project_id = '0972A', area_level = lvl_1, name = 'Inteligencia Artificial 1 (Sección A)', description = '', physical_location = '')
    db.project.insert(project_id = '0972B', area_level = lvl_1, name = 'Inteligencia Artificial 1 (Sección B)', description = '', physical_location = '')
    db.project.insert(project_id = '0770A', area_level = lvl_1, name = 'Introducción a la Programación y Computación 1 (Sección A)', description = '', physical_location = '')
    db.project.insert(project_id = '0770B', area_level = lvl_1, name = 'Introducción a la Programación y Computación 1 (Sección B)', description = '', physical_location = '')
    db.project.insert(project_id = '0770C', area_level = lvl_1, name = 'Introducción a la Programación y Computación 1 (Sección C)', description = '', physical_location = '')
    db.project.insert(project_id = '0770D', area_level = lvl_1, name = 'Introducción a la Programación y Computación 1 (Sección D)', description = '', physical_location = '')
    db.project.insert(project_id = '0770E', area_level = lvl_1, name = 'Introducción a la Programación y Computación 1 (Sección E)', description = '', physical_location = '')
    db.project.insert(project_id = '0771A', area_level = lvl_1, name = 'Introducción a la Programación y Computación 2 (Sección A)', description = '', physical_location = '')
    db.project.insert(project_id = '0771B', area_level = lvl_1, name = 'Introducción a la Programación y Computación 2 (Sección B)', description = '', physical_location = '')
    db.project.insert(project_id = '0771C', area_level = lvl_1, name = 'Introducción a la Programación y Computación 2 (Sección C)', description = '', physical_location = '')
    db.project.insert(project_id = '0771D', area_level = lvl_1, name = 'Introducción a la Programación y Computación 2 (Sección D)', description = '', physical_location = '')
    db.project.insert(project_id = '0771E', area_level = lvl_1, name = 'Introducción a la Programación y Computación 2 (Sección E)', description = '', physical_location = '')
    db.project.insert(project_id = '0796A+', area_level = lvl_1, name = 'Lenguajes Formales y de Programación (Sección A+)', description = '', physical_location = '')
    db.project.insert(project_id = '0796A-', area_level = lvl_1, name = 'Lenguajes Formales y de Programación (Sección A-)', description = '', physical_location = '')
    db.project.insert(project_id = '0796B+', area_level = lvl_1, name = 'Lenguajes Formales y de Programación (Sección B+)', description = '', physical_location = '')
    db.project.insert(project_id = '0796B-', area_level = lvl_1, name = 'Lenguajes Formales y de Programación (Sección B-)', description = '', physical_location = '')
    db.project.insert(project_id = '0795A+', area_level = lvl_1, name = 'Lógica de Sistemas (Sección A+)', description = '', physical_location = '')
    db.project.insert(project_id = '0795A-', area_level = lvl_1, name = 'Lógica de Sistemas (Sección A-)', description = '', physical_location = '')
    db.project.insert(project_id = '0773A+', area_level = lvl_1, name = 'Manejo e Implementación de Archivos (Sección A+)', description = '', physical_location = '')
    db.project.insert(project_id = '0773A-', area_level = lvl_1, name = 'Manejo e Implementación de Archivos (Sección A-)', description = '', physical_location = '')
    db.project.insert(project_id = '0729A', area_level = lvl_1, name = 'Modelación y Simulación 1 (Sección A)', description = '', physical_location = '')
    db.project.insert(project_id = '0730A', area_level = lvl_1, name = 'Modelación y Simulación 2 (Sección A)', description = '', physical_location = '')
    db.project.insert(project_id = '0964A', area_level = lvl_1, name = 'Organización Comptuacional (Sección A)', description = '', physical_location = '')
    db.project.insert(project_id = '0964B', area_level = lvl_1, name = 'Organización Comptuacional (Sección B)', description = '', physical_location = '')
    db.project.insert(project_id = '0777A', area_level = lvl_1, name = 'Organización Lenguajes y Compiladores 1 (Sección A)', description = '', physical_location = '')
    db.project.insert(project_id = '0777B', area_level = lvl_1, name = 'Organización Lenguajes y Compiladores 1 (Sección B)', description = '', physical_location = '')
    db.project.insert(project_id = '0777C', area_level = lvl_1, name = 'Organización Lenguajes y Compiladores 1 (Sección C)', description = '', physical_location = '')
    db.project.insert(project_id = '0777D', area_level = lvl_1, name = 'Organización Lenguajes y Compiladores 1 (Sección D)', description = '', physical_location = '')
    db.project.insert(project_id = '0781A+', area_level = lvl_1, name = 'Organización Lenguajes y Compiladores 2 (Sección A+)', description = '', physical_location = '')
    db.project.insert(project_id = '0781A-', area_level = lvl_1, name = 'Organización Lenguajes y Compiladores 2 (Sección A+)', description = '', physical_location = '')
    db.project.insert(project_id = '2025A', area_level = lvl_1, name = 'Prácticas Iniciales (Sección A)', description = '', physical_location = '')
    db.project.insert(project_id = '2036A', area_level = lvl_1, name = 'Prácticas Intermedias (Sección A)', description = '', physical_location = '')
    db.project.insert(project_id = '0667P', area_level = lvl_1, name = 'Programación Comercial 1 (Sección P)', description = '', physical_location = '')
    db.project.insert(project_id = '0090A', area_level = lvl_1, name = 'Programación de Computadoras 1 (090 Sección A)', description = '', physical_location = '')
    db.project.insert(project_id = '0092N', area_level = lvl_1, name = 'Programación de Computadoras 2 (Sección N)', description = '', physical_location = '')
    db.project.insert(project_id = '0092P', area_level = lvl_1, name = 'Programación de Computadoras 2 (Sección P)', description = '', physical_location = '')
    db.project.insert(project_id = '0092Q', area_level = lvl_1, name = 'Programación de Computadoras 2 (Sección Q)', description = '', physical_location = '')
    db.project.insert(project_id = '0970A', area_level = lvl_1, name = 'Redes de Computadoras 1 (Sección A)', description = '', physical_location = '')
    db.project.insert(project_id = '0975A', area_level = lvl_1, name = 'Redes de Computadoras 2 (Sección A)', description = '', physical_location = '')
    db.project.insert(project_id = '0966A', area_level = lvl_1, name = 'Seguridad y Auditoria de Redes (Sección A)', description = '', physical_location = '')
    db.project.insert(project_id = '0799A', area_level = lvl_1, name = 'Seminario de Investigación (Sección A)', description = '', physical_location = '')
    db.project.insert(project_id = '0797A', area_level = lvl_1, name = 'Seminario de Sistemas 1 (Sección A)', description = '', physical_location = '')
    db.project.insert(project_id = '0798A', area_level = lvl_1, name = 'Seminario de Sistemas 2 (Sección A)', description = '', physical_location = '')
    db.project.insert(project_id = '0281A', area_level = lvl_1, name = 'Sistemas Operativos 1 (Sección A)', description = '', physical_location = '')
    db.project.insert(project_id = '0285A', area_level = lvl_1, name = 'Sistemas Operativos 2 (Sección A)', description = '', physical_location = '')
    db.project.insert(project_id = '0780A', area_level = lvl_1, name = 'Software Avanzado (Sección A)', description = '', physical_location = '')
    db.project.insert(project_id = '0722A', area_level = lvl_1, name = 'Teoria de Sistemas 1 (Sección A)', description = '', physical_location = '')
    db.project.insert(project_id = '0721A', area_level = lvl_1, name = 'Teoria de Sistemas 2 (Sección A)', description = '', physical_location = '')
    # Various Projects
    db.project.insert(project_id = 'PV001', area_level = lvl_6, name = 'COECYS', description = 'Congreso de Estudiantes de Ingeniería en Ciencias y Sistemas', physical_location = 'Oficina de Congresos Estudiantiles Ingeniería USAC, Edificio T-1, tercer nivel')
    db.project.insert(project_id = 'PV002', area_level = lvl_1, name = 'DSI', description = 'Departamento de Soporte Informático', physical_location = 'Edificio T3, Salon 104; Universidad de San Carlos de Guatemala.')
    db.project.insert(project_id = 'PV003', area_level = lvl_4, name = 'SAE-SAP', description = '', physical_location = '')
    db.project.insert(project_id = 'PV004', area_level = lvl_4, name = 'ITCoE', description = '', physical_location = '')
    db.project.insert(project_id = 'PV005', area_level = lvl_3, name = 'Centro de Cálculo FIUSAC', description = '', physical_location = 'Centro de Cálculo Facultad de Ingeniería USAC.')
    db.project.insert(project_id = 'PV006', area_level = lvl_4, name = 'Rectoría (Infraestructura)', description = 'Proyecto de Infraestructura en Rectoría Universidad de San Carlos de Guatemala', physical_location = 'Rectoría USAC.')
    db.project.insert(project_id = 'PV007', area_level = lvl_3, name = 'Centro de Investigación FIUSAC', description = '', physical_location = 'Centro de Investigación Facultad de Ingeniería USAC.')
    db.project.insert(project_id = 'PV008', area_level = lvl_3, name = 'Escuela de Ciencias y Sistemas FIUSAC', description = 'Desarrollo de aplicaciones y utilidades para la Escuela de Ciencias y Sistemas FIUSAC.', physical_location = 'Escuela de Ciencias y Sistemas, Edificio T3.')

def _log_type_setup():
    db = _db
    #Default log types
    db.log_type.insert(name='Activity')
    db.log_type.insert(name='Anomaly')
    #Metrics log default types
    db.metrics_type.insert(name="PRIMER PARCIAL")
    db.metrics_type.insert(name="SEGUNDO PARCIAL")
    db.metrics_type.insert(name="TERCER PARCIAL")
    db.metrics_type.insert(name="EXAMEN FINAL")
    db.metrics_type.insert(name="PRIMERA RETRASADA")
    db.metrics_type.insert(name="SEGUNDA RETRASADA")
    db.metrics_type.insert(name="HOJA DE TRABAJO")
    db.metrics_type.insert(name="EXAMEN CORTO")
    db.metrics_type.insert(name="FASE DE PROYECTO")
    db.metrics_type.insert(name="FASE FINAL")
    db.metrics_type.insert(name="OTRA ACTIVIDAD")
    db.metrics_type.insert(name="TAREA")
    db.metrics_type.insert(name="PRACTICA")
    db.metrics_type.insert(name="PROYECTO 1")
    db.metrics_type.insert(name="PROYECTO 2")

def _item_type_setup():
    db = _db
    #Default item types
    db.item_type.insert(name='File')
    db.item_type.insert(name='Activity')
    db.item_type.insert(name='Grade Activity')
    db.item_type.insert(name='Schedule')


def _report_status_setup():
    db = _db
    ## Report Status Types
    db.report_status.insert(name="Draft", \
        description="Student is working on report, can be viewed by teacher \
        but can't be graded", icon="icon-pencil")
    db.report_status.insert(name="Grading", description="Report is ready \
        to be graded by teacher", icon="icon-inbox")
    db.report_status.insert(name="Recheck", description="Report has been sent \
        to be improved by student", icon="icon-time")
    db.report_status.insert(name="Acceptance", description="This report has \
        been already graded", icon="icon-edit")
    db.report_status.insert(name="EnabledForTeacher", description="This report \
        has been reactivated for teacher to grade", icon="icon-repeat")

def _module_variables_setup():
    global first_period, second_period
    first_period = _db.period(name = first_period_name)
    second_period = _db.period(name = second_period_name)

def _setup_parameters():
    db = _db
    db.custom_parameters.insert(min_score=65, rescore_max_count=2, \
        rescore_max_days=7)

def get_custom_parameters():
    db = _db
    return db(db.custom_parameters).select().first()
