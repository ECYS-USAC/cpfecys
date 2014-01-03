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
                  Field('pro_bono', 'boolean', length=255, notnull=False),
                  Field('uv_token', 'string', length=64, notnull=False),]

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
                Field ('area_level', 'reference area_level'),
                Field ('name', 'string'),
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
db.define_table('enabled_date',
                Field('name', 'string', notnull=False),
                Field('start_date', 'date', notnull=False),
                Field('end_date', 'date', notnull=False),
                Field('is_eanbled', 'boolean', notnull=False),
                )

db.define_table('report_head',
                Field('created', 'date'),
                Field('repor_user', 'reference auth_user'),
                Field('project', 'reference project'),
                Field('enabled_date', 'reference enabled_date'),
                )

db.define_table('report',
                Field('created', 'datetime', notnull=True),
                Field('project', 'reference project'),
                Field('head', 'reference report_head'),
                )              
                  
db.define_table('log_type',
                Field('name', 'string', notnull=True),
                format='%(entry_date)s'
                )  
                                
db.define_table('log_entry',
                Field('log_type', 'reference log_type'),
                Field('entry_date', 'date', notnull=True),
                Field('description', 'text', notnull=True),
                Field('entry_user', 'reference auth_user'),
                Field('project', 'reference project'),
                Field('head', 'reference report_head'),
                format='%(entry_date)s'
                )              
#Project item requirements structure
db.define_table('item_type',
                Field('name', 'string', notnull=True),
                format='%(name)s'
                )
                
db.define_table('item',
                Field('name', 'string', notnull=True),
                Field('is_active', 'boolean', notnull=False),
                Field('permanent', 'boolean', notnull=False),
                Field('description', 'text', notnull=False),
                Field('item_type', 'reference item_type'),
                Field('teacher_only', 'boolean', notnull=True),
                Field('created', 'reference period_year'),
                format='%(name)s'
                )

db.define_table('item_project',
                Field('assigned_project', 'reference project'),
                Field('item', 'reference item'),
                Field('gkey', 'string', notnull=True),
                Field('assigned_date', 'reference period_year'),
                Field('is_active', 'boolean', notnull=True),
                Field('available_periods' , 'integer')
                )

db.define_table('file_item',
                Field('file_name', 'upload', default='', notnull=True),
                Field('uploaded', 'datetime', notnull=True),
                Field('owner_user', 'reference auth_user'),
                Field('gkey', 'string', notnull=True),
                format='%(file_name)s'
                )

db.define_table('activity_item',
                Field('done', 'boolean', notnull=True),
                Field('completed', 'datetime', notnull=True),
                Field('owner_user', 'reference auth_user'),
                Field('gkey', 'string', notnull=True),
                format='%(done)s'
                )

# User Roles
## Super-Administrator:
setup = db.auth_user(db.auth_user.username == 'admin')
if setup is None:
    #Default item types
    db.item_type.insert(name='File')
    db.item_type.insert(name='Activity')
    
    #Default log types
    db.log_type.insert(name='Activity')
    db.log_type.insert(name='Anomaly')

    semester1 = db.period.insert(name = first_period_name)
    semester2 = db.period.insert(name = second_period_name)
    ## Final Practice Areas of DTT
    db.area_level.insert(name = "DTT Tutor Académico", description = "")
    db.area_level.insert(name = "DTT Tutor de Comunicación", description = "")
    db.area_level.insert(name = "DTT Tutor de Desarrollo", description = "")
    db.area_level.insert(name = "DTT Tutor de Innovación", description = "")
    db.area_level.insert(name = "DTT Tutor de Investigación", description = "")
    db.area_level.insert(name = "DTT Tutor de Infraestructura", description = "")
    ## Would be a good idea to at least join courses with UV here
    ## User Roles Setup:
    super = db.auth_user.insert(email = 'admin@admin.com', first_name = 'Super',
                                         last_name = 'Administrator', username = 'admin',
                                         password = db.auth_user.password.validate('superadmin')[0])
    superadmins = auth.add_group(role = 'Super-Administrator',
                                 description = 'In charge of the whole system administration.')
    auth.add_membership(superadmins, super)
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
    #check and create second semester of current year
    pery = db.period_year((db.period_year.yearp == year)&
                          (db.period_year.period == second_period))
    if not pery:
        db.period_year.insert(yearp = year, period = second_period)
if now.month >= 11:
    #check and create first semester of next year
    pery = db.period_year((db.period_year.yearp == (year + 1))&
                          (db.period_year.period == first_period))
    if not pery:
        db.period_year.insert(yearp = (year + 1), period = first_period)
## after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)
