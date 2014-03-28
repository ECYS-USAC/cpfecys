# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################


def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simple replace the two lines below with:
    return auth.wiki()
    """
    if auth.user != None:
        groups = db((db.auth_membership.user_id==auth.user.id)& \
                        (db.auth_group.id==db.auth_membership.group_id)). \
                        select(db.auth_group.ALL)
        front_notification = \
        db(db.front_notification.is_public==True).select()| \
        db((db.front_notification.id== \
            db.notification_access.front_notification)& \
        (db.notification_access.user_role.belongs(groups))
            ).select(db.front_notification.ALL) 
    else:
        front_notification = db(db.front_notification.is_public == True).select()
    return dict(front_notification=front_notification,
        markmin_settings = cpfecys.get_markmin,)

def links():
    """ This url shows all important links published by admin
    user. 
    """
    if auth.user != None:
        links = db(db.link).select()
        groups = db((db.auth_membership.user_id==auth.user.id)& \
                        (db.auth_group.id==db.auth_membership.group_id)). \
                        select(db.auth_group.ALL)
        links = db((db.link.id == db.link_access.link)& \
                   (db.link_access.user_role.belongs(groups))).select(db.link.ALL)
    else:
        links = db(db.link.is_public == True).select()
    return dict(links=links)

def files():
    """ This url shows all published files published by admin"""
    if auth.user != None:
        groups = db((db.auth_membership.user_id==auth.user.id)&\
                        (db.auth_group.id==db.auth_membership.group_id)).\
                        select(db.auth_group.ALL)
        files = db((db.uploaded_file.id == db.file_access.uploaded_file)&\
                   (db.file_access.user_role.belongs(groups)))\
                       .select(db.uploaded_file.ALL)
    else:
        files = db(db.uploaded_file.is_public == True).select()
    return dict(files=files)


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())

def zip():
    files = ['item.uploaded_file.bd4592bbb798c7c6.3235363035372e706466.pdf']
    return response.zip(request, files, db)

def resources():
    #Get the selected item_restriction id from parameter
    item_restriction_id = request.vars['r']
    #Get the items that belong to current semester
    import cpfecys
    period = cpfecys.current_year_period()
    return dict(semester = period,
                data = db((db.item.item_restriction == item_restriction_id)&
                          (db.item.item_restriction == db.item_restriction.id)&
                          (db.item_restriction.is_public == True)&
                          (db.item_restriction.period == period)&
                          (db.item.assignation == db.user_project.id)&
                          (db.user_project.project == db.project.id)&
                          (db.item.id > 0)).select(groupby=db.project.name, orderby=db.project.name))
