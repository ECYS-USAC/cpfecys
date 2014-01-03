# coding: utf8
if not request.env.web2py_runtime_gae:
    ## if NOT running on Google App Engine use SQLite or other DB
    db2 = DAL('mysql://root@localhost/chamilo4',pool_size=1,check_reserved=['all'], migrate=False)
else:
    ## connect to Google BigTable (optional 'google:datastore://namespace')
    db2 = DAL('google:datastore')
    ## store sessions and tickets there
    session.connect(request, response, db2=db2)
    ## or store session in Memcache, Redis, etc.
    ## from gluon.contrib.memdb import MEMDB
    ## from google.appengine.api.memcache import Client
    ## session.connect(request, response, db = MEMDB(Client()))

db2.define_table('user_user',
                Field('lastname'),
                Field('firstname'),
                Field('username'),
                Field('password'),
                Field('phone'),
                Field('email'),
                Field('external_uid'))
