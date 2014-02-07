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
                  Field('uv_token', 'string', length=64, notnull=False, \
                    writable=False, readable=False),
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
# Table to save if we are done with setup
db.define_table('setup',
                Field('done', 'boolean', unique = True))

# A project contains an description and name
db.define_table('area_level',
                Field('name', 'string', label = T('name')),
                Field('description', 'text', label = T('description')),
                format='%(name)s')

db.define_table('project',
                Field ('project_id', 'string', unique = True, length = 255, \
                    label = T('project_id')),
                Field ('name', 'string', label = T('name')),
                Field ('area_level', 'reference area_level', label = T('area_level')),
                Field ('description', 'text', label = T('description')),
                Field ('physical_location', 'text', \
                    label = T('physical_location')),
                format='%(name)s')

db.define_table('period',
                Field ('name', 'string', unique = True, length = 255, \
                    label = T('name')),
                format = '%(name)s')

db.define_table('period_year',
                Field('yearp', 'integer', label = T('yearp')),
                Field('period', 'reference period', label = T('period')),
                format = '%(yearp)s - %(period)s')

# The relationship between a user and a subproject contains
# the history of the final practice,
# it has the starting cycle and the ending cycle
# it also is the central key for all operations with interesting data
db.define_table('user_project',
                Field('assigned_user', 'reference auth_user', \
                    label = T('assigned_user')),
                Field('project', 'reference project', label = T('project')),
                Field('period', 'reference period_year', label = T('period')),
                Field('pro_bono', 'boolean', length=255, notnull=False, \
                    label = T('pro_bono')),
                Field ('periods', 'integer', notnull=False, \
                    label = T('periods')))

# This are the tables that store important links and uploaded
# files by admin.
db.define_table('link',
                Field('url', 'text', notnull=True, label = T('url/URL')),
                Field('blank', 'boolean', label = T('blank')),
                Field('url_text', 'text', notnull=True, \
                    label = T('url_text')),
                Field('visible', 'boolean', notnull=True, \
                    label = T('visible')),
                Field('is_public', 'boolean', notnull=False, 
                    label = T('is_public')),
                format='%(url_text)s')

#Frontend notification
db.define_table('front_notification',
                Field('name', 'string', notnull=True, label = T('name')),
                Field('content_text', 'text', notnull=False, \
                    label = T('content_text')),
                Field('url', 'string', notnull=False, label = T('url/URL')),
                Field('visible', 'boolean', notnull=False, label = T('visible')),
                Field('is_public', 'boolean', notnull=False, \
                    label = T('is_public')),
                Field('file_data', 'upload', default='', notnull=False, \
                    label = T('file_data')),
                Field('promoted', 'boolean', notnull=False, \
                    label = T('promoted')),
                format='%(name)s'
                )

#Published files entity
db.define_table('uploaded_file',
                Field('name', 'string', notnull=True, label = T('name')),
                Field('visible', 'boolean', label = T('visible')),
                Field('file_data', 'upload', default='', \
                    label = T('file_data')),
                Field('is_public', 'boolean', notnull=False, \
                    label = T('is_public')),
                format='%(name)s')

#User gruops relationships with files, notifications, links
db.define_table('file_access',
                Field ('user_role', 'reference auth_group', \
                    label = T('user_role')),
                Field ('uploaded_file', 'reference uploaded_file', \
                    label = T('uploaded_file')),
                )

db.define_table('link_access',
                Field ('user_role', 'reference auth_group', \
                    label = T('user_role')),
                Field ('link', 'reference link', \
                    label = T('link')),
                )

db.define_table('notification_access',
                Field ('user_role', 'reference auth_group', \
                    label = T('user_role')),
                Field ('front_notification', 'reference front_notification',\
                    label = T('front_notification')),
                )

#Reports and Activities structure
db.define_table('report_restriction',
                Field('name', 'string', notnull=False, \
                    label = T('name')),
                Field('start_date', 'date', notnull=False, \
                    label = T('start_date')),
                Field('end_date', 'date', notnull=False, \
                    label = T('end_date')),
                Field('is_enabled', 'boolean', notnull=False, \
                    label = T('is_enabled')),
                )

db.define_table('report_status',
                Field('name', 'string', notnull=True, label = T('name')),
                Field('description', 'string', notnull=True), \
                label = T('description'))

db.define_table('report',
                Field('created', 'date', \
                label = T('created')),
                Field('assignation', 'reference user_project', \
                label = T('assignation')),
                Field('report_restriction', 'reference report_restriction', \
                label = T('report_restriction')),
                Field('score', 'integer', \
                label = T('score')),
                Field('heading', 'text', \
                label = T('heading')),
                Field('footer', 'text', \
                label = T('footer')),
                Field('status', 'reference report_status', notnull=True, \
                label = T('status')),
                )

db.define_table('log_type',
                Field('name', 'string', notnull=True, label = T('name')),
                format='%(entry_date)s'
                )

db.define_table('log_entry',
                Field('log_type', 'reference log_type', label = T('log_type')),
                Field('entry_date', 'date', notnull=True, \
                    label = T('entry_date')),
                Field('description', 'text', notnull=True, \
                    label = T('description')),
                Field('report', 'reference report', label = T('report')),
                format='%(entry_date)s'
                )

db.define_table('metrics_type',
                Field('name', 'string', notnull=True, label = T('name')),
                format='%(entry_date)s'
                )

db.define_table('log_metrics',
                Field('media', 'decimal(8,2)', notnull=True, \
                    label = T('media')),
                Field('error', 'decimal(8,2)', notnull=True, \
                    label = T('error')),
                Field('mediana', 'decimal(8,2)', notnull=True, \
                    label = T('mediana')),
                Field('moda', 'decimal(8,2)', notnull=True, \
                    label = T('moda')),
                Field('desviacion', 'decimal(8,2)', notnull=True, \
                    label = T('desviacion')),
                Field('varianza', 'decimal(8,2)', notnull=True, \
                    label = T('varianza')),
                Field('curtosis', 'decimal(8,2)', notnull=True, \
                    label = T('curtosis')),
                Field('coeficiente', 'decimal(8,2)', notnull=True, \
                    label = T('coeficiente')),
                Field('rango', 'decimal(8,2)', notnull=True, \
                    label = T('rango')),
                Field('minimo', 'decimal(8,2)', notnull=True, \
                    label = T('minimo')),
                Field('maximo', 'decimal(8,2)', notnull=True, \
                    label = T('maximo')),
                Field('total', 'integer', notnull=True, \
                    label = T('total')),
                Field('reprobados', 'integer', notnull=True, \
                    label = T('reprobados')),
                Field('aprobados', 'integer', notnull=True, \
                    label = T('aprobados')),
                Field('created', 'date', notnull=True, label = T('entry_date')),
                Field('report', 'reference report', label = T('report')),
                Field('metrics_type', 'reference metrics_type', label = T('type')),
                format='%(created)s'
                )

db.define_table('log_desertion',
                Field('started', 'integer',notnull=True, label=T('started')),
                Field('gone', 'integer',notnull=True, label=T('gone')),
                Field('continued', 'integer',notnull=True, label=T('continued')),
                Field('created', 'date', notnull=True, \
                    label = T('entry_date')),
                Field('report', 'reference report', \
                    label = T('report')),
                format='%(created)s'
                )
#Project item requirements structure
db.define_table('item_type',
                Field('name', 'string', notnull=True, label = T('name')),
                format='%(name)s'
                )

db.define_table('item_restriction',
                Field('name', 'string', notnull=False, label = T('name')),
                Field('is_enabled', 'boolean', notnull=False, \
                    label = T('is_enabled')),
                Field('permanent', 'boolean', notnull=False, \
                    label = T('permanent')),
                Field('teacher_only', 'boolean', notnull=True, \
                    label = T('teacher_only')),
                Field('admin_only', 'boolean', notnull=True, \
                    label = T('admin_only')),
                Field('item_type', 'reference item_type', \
                    label = T('item_type')),
                Field('period', 'reference period_year', \
                    label = T('period')),
                format='%(name)s'
                )

db.define_table('item_restriction_area',
                Field('area_level', 'reference area_level', \
                    label = T('area_level')),
                Field('item_restriction', 'reference item_restriction', \
                    label = T('item_restriction')),
                Field('is_enabled', 'boolean', notnull=False, \
                    label = T('is_enabled')),
                )

db.define_table('item_restriction_exception', 
                Field('project', 'reference project', \
                    label = T('project')),
                Field('item_restriction', 'reference item_restriction', \
                    label = T('item_restriction')),
                )

db.define_table('item',
                Field('is_active', 'boolean', notnull=False, \
                    label = T('is_active')),
                Field('description', 'text', notnull=False, \
                    label = T('description')),
                Field('uploaded_file', 'upload', default='', notnull=False, \
                    label = T('uploaded_file')),
                Field('done_activity', 'boolean', notnull=False, \
                    label = T('done_activity')),
                Field('created', 'reference period_year', \
                    label = T('created')),
                Field('item_restriction', 'reference item_restriction', \
                    label = T('item_restriction')),
                Field('assignation', 'reference user_project', \
                    label = T('assignation')),
                format='%(name)s'
                )
import cpfecys
cpfecys.setup(db, auth)
cpfecys.force_student_data_update(request.env.path_info,
                                  ['/student/update_data',
                                   '/default/user/logout'])

## after defining tables, uncomment below to enable auditing
    # auth.enable_record_versioning(db)
