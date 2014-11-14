# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################

def events():
    cyearperiod = cpfecys.current_year_period()
    return dict(year = cyearperiod.yearp, semester = cyearperiod.period.name,
                 thing = db((db.public_event.semester == cyearperiod.id)&
                            (db.public_event.assignation != None)&
                            (db.public_event.assignation == db.user_project.id)&
                            (db.user_project.project == db.project.id) \
                            ).select(orderby=db.project.name))
@auth.requires_login()
def event_edition():
    #show all assignations of current user
    return dict(assignations = db((db.user_project.assigned_user == auth.user.id) & (db.user_project.period == cpfecys.current_year_period().id)).select())

@auth.requires_login()
def event_editor():
    assignation = request.vars['assignation']
    #check assignation belongs to this user
    import cpfecys
    check = db.user_project(id = assignation, assigned_user = auth.user.id)
    if (check is None):
        #check if there is no assignation or if it is locked (shouldn't be touched)
        if (session.last_assignation is None):
            redirect(URL('default','index'))
            return
        else:
            check = db.user_project(id = session.last_assignation)
            if cpfecys.assignation_is_locked(check):
                redirect(URL('default','index'))
                return
    else:
        session.last_assignation = check.id
    cyearperiod = cpfecys.current_year_period()
    db.public_event.semester.default = cyearperiod.id
    db.public_event.semester.writable = False
    db.public_event.semester.readable = False
    db.public_event.assignation.default = check.id
    db.public_event.assignation.writable = False
    db.public_event.assignation.readable = False
    db.public_event_schedule.public_event.readable = False
    db.public_event_schedule.public_event.writable = False
    query = (db.public_event.assignation == check.id)
    return dict(year = cyearperiod.yearp, semester = cyearperiod.period.name,name = check.project.name,grid = SQLFORM.smartgrid(db.public_event, constraints = {'public_event' : query}))

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
    links = []
    if auth.user != None:
        links = db(db.link).select()
        groups = db((db.auth_membership.user_id==auth.user.id)& \
                        (db.auth_group.id==db.auth_membership.group_id)). \
                        select(db.auth_group.ALL)
        links = db((db.link.id == db.link_access.link)& \
                   (db.link_access.user_role.belongs(groups))).select(db.link.ALL)
    public_links = db(db.link.is_public == True).select()
    return dict(links=links, public_links=public_links)

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
    if request.args(0) == 'profile':
        if auth.has_membership('Super-Administrator') == False:
            db.auth_user.username.writable = False
    pass
    return dict(form=auth())

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)

def download_file():
    the_file = db(db.uploaded_file.file_data==request.args[0]).select().first()
    if the_file != None and the_file.visible == True and the_file.is_public == True:
        return response.download(request, db)
    else:
        session.flash = T('Access Forbidden')
        redirect(URL('default', 'index'))


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
    def teachers_on_project(project_id):
        return db((db.project.id == project_id)&\
                (db.user_project.project == db.project.id)&\
                (db.auth_user.id == db.user_project.assigned_user)&\
                (db.user_project.assignation_status == None)&\
                (db.auth_membership.user_id == db.auth_user.id)&\
                (db.auth_membership.group_id == db.auth_group.id)&\
                (db.auth_group.role == 'Teacher')).select()
    def aux_in_courses(project_id):
        return db((db.project.id == project_id)&\
                (db.user_project.project == db.project.id)&\
                (db.auth_user.id == db.user_project.assigned_user)&\
                (db.user_project.assignation_status == None)&\
                (db.auth_membership.user_id == db.auth_user.id)&\
                (db.auth_membership.group_id == db.auth_group.id)&\
                (db.auth_group.role == 'Student')).select()
    return dict(teachers_on_project = teachers_on_project,
                aux_in_courses = aux_in_courses,
                semester = period,
                data = db((db.item.item_restriction == item_restriction_id)&
                          (db.item.item_restriction == db.item_restriction.id)&
                          (db.item_restriction.is_public == True)&
                          (db.item_restriction.period == period)&
                          (db.item.assignation == db.user_project.id)&
                          (db.user_project.project == db.project.id)&
                          (db.user_project.project == db.project.id)&\
                        (db.auth_user.id == db.user_project.assigned_user)&\
                        (db.user_project.assignation_status == None)&\
                        (db.auth_membership.user_id == db.auth_user.id)&\
                        (db.auth_membership.group_id == db.auth_group.id)&\
                        (db.auth_group.role == 'Student')&
                          (db.item.id > 0)).select(orderby=db.project.name))
