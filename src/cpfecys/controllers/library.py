# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################
@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def academic_log():
    import cpfecys
    #assignation = request.vars['assignation']
    year_period = cpfecys.current_year_period()
    max_display = 1
    
    currentyear_period = db.period_year(db.period_year.id == year_period)
    

    query = ((db.academic_course_assignation.semester == currentyear_period.id))

    #db.academic_course_assignation.assignation.default = check.project
    db.academic_course_assignation.assignation.writable = False
    db.academic_course_assignation.assignation.readable = False
    db.academic_course_assignation.semester.default = currentyear_period.id
    db.academic_course_assignation.semester.writable = False
    db.academic_course_assignation.semester.readable = False

    grid = SQLFORM.grid(query)

    current_period_name = T(cpfecys.second_period.name)
    if currentyear_period.period == cpfecys.first_period.id:
        current_period_name = T(cpfecys.first_period.name)
    start_index = currentyear_period.id - max_display - 1
    if start_index < 1:
        start_index = 0
    end_index = currentyear_period.id + max_display
    periods_before = db(db.period_year).select(limitby=(start_index,  \
        currentyear_period.id - 1))
    periods_after = db(db.period_year).select(limitby=(currentyear_period.id, \
     end_index))
    other_periods = db(db.period_year).select()
    return dict(grid = grid,
                currentyear_period = currentyear_period,
                current_period_name = current_period_name,
                periods_before = periods_before,
                periods_after = periods_after,
                other_periods = other_periods,
                )

