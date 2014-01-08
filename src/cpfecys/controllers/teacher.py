# coding: utf8
# intente algo como
@auth.requires_login()
@auth.requires_membership('Teacher')
def index():
    return dict()

@auth.requires_login()
@auth.requires_membership('Teacher')
def final_practice():
    assignation = request.vars['assignation']
    if not assignation: redirect(URL('courses'))
    final_practice = db((db.user_project.id == assignation)&
                        (db.user_project.assigned_user == db.auth_user.id)&
                        (db.user_project.project == db.project.id)&
                        (db.project.area_level == db.area_level.id)&
                        (db.user_project.period == db.period_year.id)).select()
    if not final_practice: redirect(URL('courses'))
    final_practice = final_practice.first()
    #TODO evaluate if available_periods is really necessary
    available_periods = db((db.period_year.id >= final_practice.user_project.period)&
                           (db.period_year.id < (final_practice.user_project.period + final_practice.user_project.periods))).select()
    #TODO Only show reports with status of != 'Draft'
    #TODO (in view) Only allow to grade the ones with status of Grading
    reports = db(db.report.assignation == final_practice.user_project.id).select()
    return dict(final_practice = final_practice,
                available_periods = available_periods,
                reports = reports)

@auth.requires_login()
@auth.requires_membership('Teacher')
def students():
    #requires parameter of project if none is provided then redirected to courses
    project_id = request.vars['project']
    #This also validates the current user is assigned in the project
    if not project_id: redirect(URL('courses'))
    current_project = db((db.user_project.assigned_user == auth.user.id)&
                         (db.project.id == project_id)).select().first()
    if not current_project: redirect(URL('courses'))
    #requires parameter year_period if no one is provided then it is automatically detected
    #and shows the current period
    year_period = request.vars['year_period']
    max_display = 1
    currentyear_period = db.period_year(db.period_year.id == year_period)
    if not currentyear_period:
        currentyear_period = current_year_period()
    current_data = db((db.user_project.period <= currentyear_period.id)&
              ((db.user_project.period + db.user_project.periods) > currentyear_period.id)&
              (db.user_project.project == current_project.project.id)&
              (db.auth_group.role == 'Student')&
              (db.auth_membership.group_id == db.auth_group.id)&
              (db.user_project.assigned_user == db.auth_membership.user_id)).select()
    current_period_name = T(second_period_name)
    if currentyear_period.period == first_period.id:
        current_period_name = T(first_period_name)
    start_index = currentyear_period.id - max_display - 1
    if start_index < 1:
        start_index = 0
    end_index = currentyear_period.id + max_display
    periods_before = db(db.period_year).select(limitby=(start_index, currentyear_period.id - 1))
    periods_after = db(db.period_year).select(limitby=(currentyear_period.id, end_index))
    other_periods = db(db.period_year).select()
    return dict(current_project = current_project,
                current_data = current_data,
                currentyear_period = currentyear_period,
                current_period_name = current_period_name,
                periods_before = periods_before,
                periods_after = periods_after,
                other_periods = other_periods)

@auth.requires_login()
@auth.requires_membership('Teacher')
def courses():
    #requires parameter year_period if no one is provided then it is automatically detected
    #and shows the current period
    year_period = request.vars['year_period']
    max_display = 1
    currentyear_period = db.period_year(db.period_year.id == year_period)
    if not currentyear_period:
        currentyear_period = current_year_period()
    current_data = db((db.user_project.period <= currentyear_period.id)&
              ((db.user_project.period + db.user_project.periods) > currentyear_period.id)&
              (db.user_project.assigned_user == auth.user.id)).select()
    current_period_name = T(second_period_name)
    if currentyear_period.period == first_period.id:
        current_period_name = T(first_period_name)
    start_index = currentyear_period.id - max_display - 1
    if start_index < 1:
        start_index = 0
    end_index = currentyear_period.id + max_display
    periods_before = db(db.period_year).select(limitby=(start_index, currentyear_period.id - 1))
    periods_after = db(db.period_year).select(limitby=(currentyear_period.id, end_index))
    other_periods = db(db.period_year).select()
    return dict(current_data = current_data,
                currentyear_period = currentyear_period,
                current_period_name = current_period_name,
                periods_before = periods_before,
                periods_after = periods_after,
                other_periods = other_periods)

def find_max_cycles(user_projects):
    cycles = [0]
    for item in user_projects:
        cycles.extend([item.periods])
    return max(cycles)

def get_current_year():
    from datetime import datetime
    return datetime.now().year

def current_year_period():
    #this should be a module's method
    import datetime
    cdate = datetime.datetime.now()
    cyear = cdate.year
    cmonth = cdate.month
    period = second_period
    #current period depends if we are in dates between jan-jun and jul-dec
    if cmonth < 7 :
        period = first_period
    return db.period_year((db.period_year.yearp == cyear)&
                          (db.period_year.period == period))

def grading():
    return locals()
