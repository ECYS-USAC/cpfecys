# coding: utf8
# intente algo como
@auth.requires_login()
@auth.requires_membership('Teacher')
def index():
    return dict()
   
def courses():
    cyear = get_current_year()
    year_period = request.vars['year_period']
    cyear_period = current_year_period()
    user_projects = db(db.user_project.student==auth.user.id).select()
    
    max_display = 1
    currentyear_period = db.period_year(db.period_year.id == year_period)
    if not currentyear_period:
        currentyear_period = current_year_period()
    #grid = SQLFORM.grid((db.user_project.period == currentyear_period.id))
    current_period_name = T(second_period_name)
    if currentyear_period.period == first_period.id:
        current_period_name = T(first_period_name)
    start_index = currentyear_period.id - max_display - 1
    if start_index<1:
        start_index = 0
    end_index = currentyear_period.id + max_display
    periods_before = db(db.period_year).select(limitby=(start_index, currentyear_period.id - 1))
    periods_after = db(db.period_year).select(limitby=(currentyear_period.id, cyear_period.id))
    other_periods = db(db.period_year).select()
    return locals()
    
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
