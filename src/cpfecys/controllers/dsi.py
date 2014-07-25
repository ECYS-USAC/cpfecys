# coding: utf8

@auth.requires_login()
@auth.requires_membership('DSI')
def index():
    admin = False
    period = cpfecys.current_year_period()
    restrictions = db(
       (db.item_restriction.item_type==db.item_type(name='Activity'))& \
       ((db.item_restriction.period==period.id) |
        ((db.item_restriction.permanent==True)&
            (db.item_restriction.period <= period.id)))&
        (db.item_restriction.is_enabled==True)).select()| \
    db((db.item_restriction.item_type==db.item_type(name='Grade Activity'))& \
       ((db.item_restriction.period==period.id) |
        ((db.item_restriction.permanent==True)&
            (db.item_restriction.period <= period.id)))&
        (db.item_restriction.is_enabled==True)).select()
    return dict(restrictions=restrictions)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def approve_all():
    restriction = request.vars['restrictions']
    period = request.vars['period']
    grade_all(restriction, period)
    redirect(URL('item_detail', vars=dict(restriction=restriction)))

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def grade_all(restriction,period):
  areas = db( \
    (db.item_restriction_area.item_restriction==restriction)&
    (db.area_level.id==db.item_restriction_area.area_level)
    ).select(db.area_level.ALL)
  for area in areas:
    projects = db((db.project.area_level==db.area_level.id)&
         (db.area_level.id==area.id)&
         (db.item_restriction.id==restriction)&
         (db.item_restriction_area.area_level==area.id)&
         (db.item_restriction_area.item_restriction==restriction)&
         (db.item_restriction_area.item_restriction==db.item_restriction.id)&
         (db.item_restriction_area.area_level==db.area_level.id)&
         (db.item_restriction_area.is_enabled==True)).select(db.project.ALL)
    for project in projects:
      exception = db((db.item_restriction_exception.project==project.id)&
         (db.item_restriction_exception.item_restriction== \
          restriction))
      if exception.count() == 0:
        assignations = db(
                    (db.auth_user.id==db.user_project.assigned_user)&
                    (db.auth_user.id==db.auth_membership.user_id)&
                    (db.auth_membership.group_id==db.auth_group.id)&
                    (db.auth_group.role=='Student')&
                    (db.user_project.project==project.id)&
                    (db.user_project.period == db.period_year.id)&
                    ((db.user_project.period <= period)&
                 ((db.user_project.period + db.user_project.periods) > \
                  period))
                    ).select(db.user_project.ALL)
        for assignation in assignations:
          item = db((db.item.assignation==assignation.id)&
         (db.item.item_restriction==restriction)&
         (db.item.item_restriction==db.item_restriction.id)&
         (db.item_restriction.is_enabled==True)&
         (db.item.created==period)).select(db.item.ALL).first()
          if item == None:
            restrictionInstance = db(
              db.item_restriction.id==restriction).select().first()
            db.item.insert(is_active=True,
            done_activity=True,
            created=period,
            item_restriction=restriction,
            assignation=assignation.id,
            score=restrictionInstance.min_score,
            min_score=restrictionInstance.min_score)
          else:
            if item.score != None:
              item.update_record(score=item.min_score)
            if item.done_activity == None:
              item.update_record(done_activity=True)
  return assignations

@auth.requires_login()
@auth.requires_membership('DSI')
def item_detail():
    period = cpfecys.current_year_period()
    if request.vars['period'] != None:
        period = request.vars['period']
        period = db.period_year(db.period_year.id==period)
    admin_role = db((db.auth_user.id==auth.user.id)&
                      (db.auth_membership.user_id == db.auth_user.id)&
                      (db.auth_membership.group_id == db.auth_group.id)&
                      (db.auth_group.role == 'Super-Administrator'))
    admin = admin_role.count() != 0
    periods = False
    if admin:
        periods = db(db.period_year).select()
    if (request.args(0) == 'update'):
       valid = False
       score = request.vars['score']
       done = request.vars['done'] or False
       user = request.vars['user']
       project = request.vars['project']
       restriction = request.vars['restriction']
       done_activity = (done=='on' or False)
       restriction = db(db.item_restriction.id==restriction).select().first()
       if restriction.item_type.name == 'Grade Activity':
         valid = not(score and user and restriction)
         if not isinstance(score, int):
          session.flash = T('Value must be numeric.')
          redirect(URL('dsi','item_detail', 
            vars=dict(restriction=restriction.id)))
       else:
         valid = not(user and restriction)
       if valid:
         session.flash = T('Not permited action.')
         redirect(URL('dsi', 'index'))
       #Validate if current user assignation is active
       assignations = db(
                        (db.auth_user.id==db.user_project.assigned_user)&
                        (db.auth_user.id==db.auth_membership.user_id)&
                        (db.auth_user.id==user)&
                        (db.auth_membership.group_id==db.auth_group.id)&
                        (db.auth_group.role=='Student')&
                        (db.user_project.project==project)&
                        (db.user_project.period==db.period_year.id)&
                        ((db.user_project.period <= period.id)&
                       ((db.user_project.period + db.user_project.periods) > \
                        period.id))
                        )
       if assignations.count() != 1:
         session.flash = T('Not permited action.')
         redirect(URL('dsi', 'index'))
       assignation = assignations.select(db.user_project.ALL).first()
       item = db((db.item.created==period.id)&
         (db.item.item_restriction==restriction.id)&
         (db.item.item_restriction==db.item_restriction.id)&
         (db.item_restriction.is_enabled==True)&
         (db.item.assignation==assignation.id)).select(db.item.ALL).first()

       if item == None:
         import datetime
         cdate = datetime.datetime.now()
         db.item.insert(is_active=True,
          done_activity=done_activity,
          created=period.id,
          item_restriction=restriction.id,
          assignation=assignation.id,
          score=score,
          min_score=restriction.min_score)
       else:
         item.update_record(is_active=True,
          done_activity=done_activity,
          created=period.id,
          item_restriction=restriction.id,
          assignation=assignation.id,
          score=score,
          min_score=restriction.min_score)

       redirect(URL('dsi','item_detail', vars=dict(restriction=restriction.id)))
    
    restriction = request.vars['restriction']
    valid = restriction != None and restriction != ''
    if not valid:
       session.flash = T('Not valid item list select a valid item list.')
       redirect(URL('dsi', 'index'))
    restrictions = db(
       (db.item_restriction.item_type==db.item_type(name='Activity'))& \
       (db.item_restriction.period==period.id)&
       (db.item_restriction.id==restriction)&
       (db.item_restriction.is_enabled==True)).select() | \
    db((db.item_restriction.item_type==db.item_type(name='Grade Activity'))& \
       (db.item_restriction.period==period.id)&
       (db.item_restriction.id==restriction)&
       (db.item_restriction.is_enabled==True)).select()| \
    db((db.item_restriction.item_type==db.item_type(name='Activity'))& \
       (db.item_restriction.id==restriction)&
       (db.item_restriction.is_enabled==True)&
       (db.item_restriction.permanent==True)).select()| \
    db((db.item_restriction.item_type==db.item_type(name='Grade Activity'))& \
       (db.item_restriction.id==restriction)&
       (db.item_restriction.is_enabled==True)&
       (db.item_restriction.permanent==True)).select()
    def get_areas(restriction):
       areas = db((db.item_restriction_area.item_restriction==restriction.id)&
         (db.area_level.id==db.item_restriction_area.area_level))
       return areas
    def get_projects(area,restriction):
       projects = db((db.project.area_level==db.area_level.id)&
         (db.area_level.id==area.id)&
         (db.item_restriction.id==restriction.id)&
         (db.item_restriction_area.area_level==area.id)&
         (db.item_restriction_area.item_restriction==restriction.id)&
         (db.item_restriction_area.item_restriction==db.item_restriction.id)&
         (db.item_restriction_area.area_level==db.area_level.id)&
         (db.item_restriction_area.is_enabled==True))
       return projects
    def is_exception(project, restriction):
       exception = db((db.item_restriction_exception.project==project.id)&
         (db.item_restriction_exception.item_restriction== \
          restriction.id))
       return exception.count() != 0
    def get_students(project):
       assignations = db(
                    (db.auth_user.id==db.user_project.assigned_user)&
                    (db.auth_user.id==db.auth_membership.user_id)&
                    (db.auth_membership.group_id==db.auth_group.id)&
                    (db.auth_group.role=='Student')&
                    (db.user_project.project==project.id)&
                    (db.user_project.period == db.period_year.id)&
                    ((db.user_project.period <= period.id)&
                 ((db.user_project.period + db.user_project.periods) > \
                  period.id))
                    ).select(db.user_project.ALL)
       return assignations
    def get_item(restriction, assignation):
       item = db((db.item.assignation==assignation.id)&
         (db.item.item_restriction==restriction.id)&
         (db.item.item_restriction==db.item_restriction.id)&
         (db.item_restriction.is_enabled==True)&
         (db.item.is_active==True)&
         (db.item.created==period.id)).select(db.item.ALL).first()
       return item
    return dict(restrictions=restrictions,
       get_areas=get_areas,
       get_projects=get_projects,
       is_exception=is_exception,
       get_students=get_students,
       get_item=get_item,
       admin=admin,
       periods=periods,
       period=period)
