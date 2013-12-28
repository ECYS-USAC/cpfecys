# coding: utf8
# intente algo como
@auth.requires_login()
@auth.requires_membership('Student')
def index():
    assignations = db((db.user_project.assigned_user == auth.user.id)&
                      (db.user_project.assigned_user == db.auth_user.id)&
                      (db.user_project.project == db.project.id)&
                      (db.project.area_level == db.area_level.id)&
                      (db.user_project.period == db.period_year.id)).select()
    return dict(assignations = assignations)

def report_list():
    assignation = request.vars['assignation']
    #TODO: security statement goes here
    if not assignation: redirect(URL('index'))
    final_practice = db((db.user_project.id == assignation)&
                        (db.user_project.assigned_user == db.auth_user.id)&
                        (db.user_project.project == db.project.id)&
                        (db.project.area_level == db.area_level.id)&
                        (db.user_project.period == db.period_year.id)).select()
    if not final_practice: redirect(URL('index'))
    final_practice = final_practice.first()
    available_periods = db((db.period_year.id >= final_practice.user_project.period)&
                           (db.period_year.id < (final_practice.user_project.period + final_practice.user_project.periods))).select()
    return dict(final_practice = final_practice,
                available_periods = available_periods)
