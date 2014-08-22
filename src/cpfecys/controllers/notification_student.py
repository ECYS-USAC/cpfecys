#***************************************************************
#***************************************************************
#***************************************************************
#***************************************************************
@auth.requires_login()
@auth.requires_membership('Academic')
def inbox():
    import cpfecys
    cperiod = cpfecys.current_year_period()

    academic_var = db.academic(db.academic.id_auth_user==auth.user.id)        
    period_list = db(db.academic_course_assignation.carnet==academic_var.id).select(db.academic_course_assignation.semester,distinct=True)

    select_form = FORM(INPUT(_name='semester_id',_type='text'))

    if select_form.accepts(request.vars,formname='select_form'):
        assignations = db((db.academic_course_assignation.semester==str(select_form.vars.semester_id)) & (db.academic_course_assignation.carnet==academic_var.id)).select()
        period_id = str(select_form.vars.semester_id)
    else:
        assignations = db((db.academic_course_assignation.semester==cperiod.id) & (db.academic_course_assignation.carnet==academic_var.id)).select()
        period_id = str(cperiod.id)

    return dict(assignations=assignations,email=auth.user.email,period_id=period_id,period_list=period_list,cperiod=cperiod.id)

def inbox_mails_load():
    import cpfecys
    #request.vars['email']
    #If emisor username change... error of reload
    try:
        if request.vars['operation'] == "mails_list":
            year_var = db.period_year(db.period_year.id==request.vars['period_id'])
            period_var = db.period(db.period.id==year_var.period)
            project_var = db.project(db.project.id==request.vars['project_id'])
                        
            mails = db((db.notification_general_log4.yearp==year_var.yearp) & (db.notification_general_log4.period==period_var.name) & (db.notification_general_log4.course==project_var.name)).select()
            
            return dict(mails = mails)    

        if request.vars['operation'] == "view_mail":

            mail_var = db.notification_general_log4(db.notification_general_log4.id==request.vars['mail_id'])
            user_var = db.auth_user(db.auth_user.username==mail_var.emisor)
        return dict(mail = mail_var, emisor = user_var)
    except:
        return dict(mail = "", emisor = "")

        


