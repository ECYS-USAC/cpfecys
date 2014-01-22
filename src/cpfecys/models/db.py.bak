# -*- coding: utf-8 -*-

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
## File is released under public domain and you can use without limitations
#########################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

if not request.env.web2py_runtime_gae:
    ## if NOT running on Google App Engine use SQLite or other DB
    db = DAL('mysql://root@localhost/cpfecys',pool_size=1,check_reserved=['all'])
else:
    ## connect to Google BigTable (optional 'google:datastore://namespace')
    db = DAL('google:datastore')
    ## store sessions and tickets there
    session.connect(request, response, db=db)
    ## or store session in Memcache, Redis, etc.
    ## from gluon.contrib.memdb import MEMDB
    ## from google.appengine.api.memcache import Client
    ## session.connect(request, response, db = MEMDB(Client()))

#Some weird web2py bug fixed here to avoid overwritting code in core
from gluon.dal import BaseAdapter
def ADD(self, first, second):
    if self.is_numerical_type(first.type) or isinstance(first, Field):
        return '(%s + %s)' % (self.expand(first),
                              self.expand(second, first.type))
    else:
        return self.CONCAT(first, second)
BaseAdapter.ADD = ADD

## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []
## (optional) optimize handling of static files
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

#########################################################################
## Here is sample code if you need for
## - email capabilities
## - authentication (registration, login, logout, ... )
## - authorization (role based authorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
## - old style crud actions
## (more options discussed in gluon/tools.py)
#########################################################################

from gluon.tools import Auth, Crud, Service, PluginManager, prettydate
auth = Auth(db)

# NOTE: length=255 is needed because a bug in mysql
# as describede here: http://goo.gl/NBG5JM
auth.settings.extra_fields['auth_user']= [
                  Field('phone', 'string', length=16, notnull=False),
                  Field('working', 'boolean', notnull=False),
                  Field('work_address', 'string',length=255, notnull=False),
                  Field('uv_token', 'string', length=64, notnull=False),
                  Field('data_updated', 'boolean', notnull=False),]

crud, service, plugins = Crud(db), Service(), PluginManager()

## create all tables needed by auth if not custom tables
auth.define_tables(username=True, signature=False, migrate=True)

## Change the display format for a user within this system.
## Carnet is our best chance for identifying users.
## db.auth_user._format = '%(carnet)s'

## configure email
mail = auth.settings.mailer
mail.settings.server = 'logging' or 'smtp.gmail.com:587'
mail.settings.sender = 'you@gmail.com'
mail.settings.login = 'username:password'

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True
## disable registration
auth.settings.actions_disabled.append('register')

## if you need to use OpenID, Facebook, MySpace, Twitter, Linkedin, etc.
## register with janrain.com, write your domain:api_key in private/janrain.key
from gluon.contrib.login_methods.rpx_account import use_janrain
use_janrain(auth, filename='private/janrain.key')

#########################################################################
## Define your tables below (or better in another model file) for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################

# A project contains an description and name
db.define_table('area_level',
                Field('name', 'string'),
                Field('description', 'text'),
                format='%(name)s')

db.define_table('project',
                Field ('project_id', 'string', unique = True, length = 255),
                Field ('name', 'string'),
                Field ('area_level', 'reference area_level'),
                Field ('description', 'text'),
                Field ('physical_location', 'text'),
                format='%(name)s')

db.define_table('period',
                Field ('name', 'string', unique = True, length = 255),
                format = '%(name)s')

db.define_table('period_year',
                Field('yearp', 'integer'),
                Field('period', 'reference period'),
                format = '%(yearp)s - %(period)s')

# The relationship between a user and a subproject contains
# the history of the final practice,
# it has the starting cycle and the ending cycle
# it also is the central key for all operations with interesting data
db.define_table('user_project',
                Field('assigned_user', 'reference auth_user'),
                Field('project', 'reference project'),
                Field('period', 'reference period_year'),
                Field('pro_bono', 'boolean', length=255, notnull=False),
                Field ('periods', 'integer', notnull=False))

first_period_name = 'First Semester'
second_period_name = 'Second Semester'

# This are the tables that store important links and uploaded
# files by admin.
db.define_table('link',
                Field('url', 'text', notnull=True),
                Field('blank', 'boolean'),
                Field('url_text', 'text', notnull=True),
                Field('visible', 'boolean', notnull=True),
                Field('is_public', 'boolean', notnull=False),
                format='%(url_text)s')

#Frontend notification
db.define_table('front_notification',
                Field('name', 'string', notnull=True),
                Field('content_text', 'text', notnull=False),
                Field('url', 'string', notnull=False),
                Field('visible', 'boolean', notnull=False),
                Field('is_public', 'boolean', notnull=False),
                Field('file_data', 'upload', default='', notnull=False),
                Field('promoted', 'boolean', notnull=False),
                format='%(name)s'
                )

#Published files entity
db.define_table('uploaded_file',
                Field('name', 'string', notnull=True),
                Field('visible', 'boolean'),
                Field('file_data', 'upload', default=''),
                Field('is_public', 'boolean', notnull=False),
                format='%(name)s')

#User gruops relationships with files, notifications, links
db.define_table('file_access',
                Field ('user_role', 'reference auth_group'),
                Field ('uploaded_file', 'reference uploaded_file'),
                )

db.define_table('link_access',
                Field ('user_role', 'reference auth_group'),
                Field ('link', 'reference link'),
                )

db.define_table('notification_access',
                Field ('user_role', 'reference auth_group'),
                Field ('front_notification', 'reference front_notification'),
                )

#Reports and Activities structure
db.define_table('report_restriction',
                Field('name', 'string', notnull=False),
                Field('start_date', 'date', notnull=False),
                Field('end_date', 'date', notnull=False),
                Field('is_enabled', 'boolean', notnull=False),
                )

db.define_table('report_status',
                Field('name', 'string', notnull=True),
                Field('description', 'string', notnull=True))

db.define_table('report',
                Field('created', 'date'),
                Field('assignation', 'reference user_project'),
                Field('report_restriction', 'reference report_restriction'),
                Field('score', 'integer'),
                Field('status', 'reference report_status', notnull=True),
                )

db.define_table('report_detail',
                Field('created', 'datetime', notnull=True),
                Field('report', 'reference report'),
                )

db.define_table('log_type',
                Field('name', 'string', notnull=True),
                format='%(entry_date)s'
                )

db.define_table('log_entry',
                Field('log_type', 'reference log_type'),
                Field('entry_date', 'date', notnull=True),
                Field('description', 'text', notnull=True),
                Field('report', 'reference report'),
                format='%(entry_date)s'
                )
#Project item requirements structure
db.define_table('item_type',
                Field('name', 'string', notnull=True),
                format='%(name)s'
                )

db.define_table('item_restriction',
                Field('name', 'string', notnull=False),
                Field('start_date', 'date', notnull=False),
                Field('end_date', 'date', notnull=False),
                Field('is_enabled', 'boolean', notnull=False),
                Field('permanent', 'boolean', notnull=False),
                Field('teacher_only', 'boolean', notnull=True),
                Field('item_type', 'reference item_type'),
                Field('period', 'reference period_year'),
                format='%(name)s'
                )

db.define_table('item_restriction_area', 
                Field('area_level', 'reference area_level'),
                Field('item_restriction', 'reference item_restriction'),
                Field('is_enabled', 'boolean', notnull=False),
                )

db.define_table('item',
                Field('is_active', 'boolean', notnull=False),
                Field('description', 'text', notnull=False),
                Field('uploaded_file', 'upload', default='', notnull=False),
                Field('done_activity', 'boolean', notnull=False),
                Field('created', 'reference period_year'),
                Field('item_restriction', 'reference item_restriction'),
                Field('assignation', 'reference user_project'),
                format='%(name)s'
                )

#User updated data validation
if auth.user != None:
    groups = db((db.auth_membership.user_id==auth.user.id)& \
                    (db.auth_group.role=='Student')& \
                    (db.auth_group.id==db.auth_membership.group_id)). \
                    select().first()
    if groups != None:
        path  = request.env.path_info
        update_url = '/cpfecys/student/update_data'
        logout_url = '/default/user/logout'
        if not db(db.auth_user.id==auth.user.id).select().first().data_updated:
                if path != update_url and not logout_url in path:
                    redirect(URL('student','update_data'))
# User Roles
## Super-Administrator:
setup = db.auth_user(db.auth_user.username == 'admin')
if setup is None:
    ## Report Status Types
    db.report_status.insert(name="Draft", description="")
    db.report_status.insert(name="Grading", description="")
    db.report_status.insert(name="Recheck", description="")
    db.report_status.insert(name="Acceptance", description="")
    #Default item types
    db.item_type.insert(name='File')
    db.item_type.insert(name='Activity')

    #Default log types
    db.log_type.insert(name='Activity')
    db.log_type.insert(name='Anomaly')

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
    ## Would be a good idea to at least join courses with UV here
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
#
# automatically tries to create the next period in may and november respectively
# Using the following logic:
# - In May..Dec the second period of current year is created.
# - In Nov the first period of next year is created.
# - In Jan..Apr the first period of current year is created.
#
first_period = db.period(db.period.name == first_period_name)
second_period = db.period(db.period.name == second_period_name)
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
## after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)
