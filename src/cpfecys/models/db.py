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
                  Field('work_address', 'string', unique=True, length=255, notnull=False),
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
                Field('student', 'reference auth_user'),
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

db.define_table('uploaded_file',
                Field('name', 'string', notnull=True),
                Field('visible', 'boolean'),
                Field('file_data', 'upload', default=''),
                Field('is_public', 'boolean', notnull=False),
                format='%(name)s')

db.define_table('file_access',
                Field ('user_role', 'reference auth_group'),
                Field ('uploaded_file', 'reference uploaded_file'),
                )

db.define_table('link_access',
                Field ('user_role', 'reference auth_group'),
                Field ('link', 'reference link'),
                )
                
#Student report

# User Roles
## Super-Administrator:
setup = db.auth_user(db.auth_user.username == 'admin')
if setup is None:
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
# automatically creates the two periods of the current year and the next year
# when the year changes so automatically new periods are created
# example: we are in year 2013; automatically first semester and second semester are created for this year
#  and the next one (2014)
#
first_period = db.period(db.period.name == first_period_name)
second_period = db.period(db.period.name == second_period_name)
import datetime
now = datetime.datetime.now()
year = now.year
next_year = year + 1
pery = db.period_year(db.period_year.yearp == year)
if not pery:
    db.period_year.insert(yearp = year, period = first_period)
    db.period_year.insert(yearp = year, period = second_period)
pery = db.period_year(db.period_year.yearp == next_year)
if not pery:
    db.period_year.insert(yearp = next_year, period = first_period)
    db.period_year.insert(yearp = next_year, period = second_period)
## after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)
