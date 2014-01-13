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
    update_data_form = False
    if not user_updated_data():
        if auth.user != None:
            cuser = db(db.auth_user.id==auth.user.id).select().first()
            form = FORM(
                            DIV(LABEL(T('First Name:')),
                                        INPUT(_name="first_name", 
                                            _type="text", _id="first_name", 
                                            _value=cuser.first_name,
                                            requires=IS_NOT_EMPTY())),

                            DIV(LABEL(T('Last Name:')),
                                           INPUT(_name="last_name", 
                                            _type="text", _id="last_name", 
                                             _value=cuser.last_name, 
                                             requires=IS_NOT_EMPTY())),

                            DIV(LABEL(T('Email:')),
                                           INPUT(_name="email", 
                                            _type="text", _id="email", 
                                            _value=cuser.email, 
                                            requires=IS_NOT_EMPTY())),

                            DIV(LABEL(T('Password: (Leave the same for no \
                                change)')),
                                          INPUT(_name="password", 
                                            _type="password", _id="password", 
                                            _value=cuser.password, 
                                            requires=IS_NOT_EMPTY())),

                            DIV(LABEL(T('Repeat password: (Leave the blank for \
                                no change)')),
                                          INPUT(_name="repass", 
                                            _type="password", _id="repass")),

                            DIV(LABEL(T('Phone:')),
                                          INPUT(_name="phone", _type="text", 
                                            _id="phone", _value=cuser.phone, 
                                            requires=IS_LENGTH(minsize=8, 
                                                            maxsize=12))),

                            DIV(LABEL(T('Working:')),
                                          INPUT(_name="working", 
                                            _type="checkbox", _id="working", 
                                            _value=cuser.working)),

                            DIV(LABEL(T('Work Address:')),
                                          INPUT(_name="work_address", 
                                            _type="text", _id="work_address", 
                                            _value=cuser.work_address)),
                            BR(),
                            DIV(INPUT(_type='submit', 
                                _value=T('Update Profile'), 
                                _class="btn-primary")),
                                _class="form-horizontal",)
            if form.process().accepted:
                first_name = request.vars['first_name']
                last_name = request.vars['last_name']
                email = request.vars['email']
                password = request.vars['password']
                repass = request.vars['repass']
                phone = request.vars['phone']
                working = request.vars['working']
                work_address = request.vars['work_address']

                #TODO analyze for aditional security steps
                cuser=db(db.auth_user.id==auth.user.id).select().first()
                if cuser != None:
                    cuser.first_name = first_name
                    cuser.last_name = last_name
                    cuser.email = email
                    cuser.phone = phone
                    cuser.data_updated = True
                    if password == repass and len(repass) > 0:
                        #TODO Fix password update
                        cuser.password = db.auth_user.password.validate(password)
                    if working:
                        cuser.working = working
                        cuser.work_address = work_address

                    cuser.update_record()
                    response.flash = 'User data updated!'
                    redirect(URL('default', 'index'))
                else:
                    response.flash = 'Error!'

            elif form.errors:
                response.flash = 'form has errors'
            else:
                response.flash = 'please fill the form'    

            return dict(form=form, update_data_form=True)
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simple replace the two lines below with:
    return auth.wiki()
    """
    if auth.user != None:
        notifications = db(db.front_notification).select()
        groups = db((db.auth_membership.user_id==auth.user.id)& \
                        (db.auth_group.id==db.auth_membership.group_id)). \
                        select(db.auth_group.ALL)
        front_notification = db((db.front_notification.id == db.notification_access.front_notification)& \
                   (db.notification_access.user_role.belongs(groups))).select(db.front_notification.ALL)
    else:
        notifications = db(db.front_notification.is_public == True).select()
    return locals()
    return dict(message=T('Hello World'), update_data_form=False)

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
