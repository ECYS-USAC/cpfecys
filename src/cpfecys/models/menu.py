# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = A(B('web',SPAN(2),'py'),XML('&trade;&nbsp;'),
                  _class="brand",_href="http://www.web2py.com/")
response.title = request.application.replace('_',' ').title()
response.subtitle = ''

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Boris Aguilar <me@borisaguilar.com> & Omar Vides <omarvides@gmail.com>'
response.meta.description = T('Application to manage Final Practice in USAC')
response.meta.keywords = 'usac'
#response.meta.generator = ''

## your http://google.com/analytics id
response.google_analytics_id = 'UA-50474874-1'

def current_year_period():
    import datetime
    cdate = datetime.datetime.now()
    cyear = cdate.year
    cmonth = cdate.month
    period = db.period(name = 'Second Semester')
    #current period depends if we are in dates between jan-jun and jul-dec
    if cmonth < 6 :
        period = db.period(name = 'First Semester')
    return db((db.period_year.yearp == cyear)&
                          (db.period_year.period == period)).select().first()

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################
response.menu = [(T('Home'), False, URL('default', 'index'), [])]
if auth.has_membership(role="Super-Administrator"):
    response.menu.extend([
        (T('Users Administration'), False, URL(),[
             (T('Final Practice Admin'), False, URL('admin', 'final_practice'), []),
             (T('Users'), False, URL('admin', 'users'), []),
             (T('Roles'), False, URL('admin', 'roles'), []),
             ]),
        (T('Assignation Administration'), False, URL(),[
             (T('Assignation By Semester'), False, URL('admin', 'assignations'), []),
             (T('Assignation Freeze Dates'), False, URL('admin', 'assignation_freeze'), []),
             ]),
         (T('Projects Administration'), False, URL(),[
            (T('Areas'), False, URL('admin', 'areas'), []),
            (T('Projects'), False, URL('admin', 'projects'), []),
            ]),
         (T('Frontend Administration'), False, URL(),[
             (T('Links Manager'), False, URL('admin', 'links'), []),
             (T('Files Manager'), False, URL('admin', 'files_manager'), []),
             (T('News'), False, URL('admin', 'notifications_manager'), []),
             (T('Mail Notifications Manager'), False, URL(), [
                (T('Send Mail'), False, URL('admin', 'mail_notifications'), []),
                (T('Mail Log'), False, URL('admin', 'mail_log'), []),]),
             ]),
         (T('Reports Administration'), False, URL(),[
             (T('Report Mandatory Blocks'), False, URL('admin', 'report_requirements'), []),
             (T('Reports and Restrictions'), False, URL('admin', 'report_restrictions'), []),
             (T('Items Manager'), False, URL('admin', 'items_manager'), []),
             (T('Reports by status'), False, URL('admin', 'report_list'), []),
             (T('Anomalies per periods'), False, URL('admin', 'anomalies_list/periods'), []),
             (T('Delivered Items Administrator'), False, URL('admin', 'manage_items/periods'), []),
             (T('Delivered Download'), False, URL('admin', 'delivered_download'), []),
             ]),
         (T('System Configuration'), False, URL(),[
             (T('Parameters configuration'), False, URL('admin', 'parameters'), []),
             (T('Configuration Web Service'), False, URL('student_academic', 'student_validation_parameters'), []),
             ]),
         (T('Reports'), False, URL(),[
             (T('Courses reports'), False, URL('admin', 'courses_report/areas'), []),
             (T('Project Leaders'), False, URL('admin', 'active_teachers'), []),
             (T('General Report'), False, URL('admin', 'general_report'), []),
             (T('System-wide Mail Logs'), False, URL('mailer', 'index'), []),
             (T('Scheduler Report'), False, URL('admin', 'scheduler_activity'), []),
             ]),
    ])


cont_news = 0
if auth.has_membership(role="Teacher") or auth.has_membership(role="Student"):
    var_count = 0
    var_count_report = 0

    projects = db(db.user_project.assigned_user == auth.user.id).select(db.user_project.project,distinct=True)
    for project in projects:
        
        mails = db((db.academic_send_mail_log.course==project.project.name)).select()
        for a in mails:
            var_query = db.academic_send_mail_detail((db.academic_send_mail_detail.academic_send_mail_log==a.id) & (db.academic_send_mail_detail.username==auth.user.username))
                            
            if var_query != None:
                if db((db.read_mail_student.id_auth_user == auth.user.id) & (db.read_mail_student.id_mail == a.id) ).select().first() == None:
                    cont_news = cont_news + 1
                pass
            pass
        pass

        for a in db((db.notification_general_log4.course==project.project.name)).select():
            var_query = db.notification_log4((db.notification_log4.register==a.id) & (db.notification_log4.username==auth.user.username))
            if var_query != None:
                if db((db.read_mail.id_auth_user == auth.user.id) & (db.read_mail.id_mail == a.id) ).select().first() == None:
                    cont_news = cont_news + 1
                pass
            pass
        pass

        if auth.has_membership(role="Teacher"):
            var_count = var_count + db((db.request_change_weighting.status=='pending')&(db.request_change_weighting.period==current_year_period().id)&(db.request_change_weighting.project==project.project)).count()
            var_count = var_count + db((db.requestchange_activity.status=='pending')&(db.requestchange_activity.semester==current_year_period().id)&(db.requestchange_activity.course==project.project)).count()
            var_count = var_count + db((db.request_change_grades.status=='pending')&(db.request_change_grades.period==current_year_period().id)&(db.request_change_grades.project==project.project)).count()

    pass

    if auth.has_membership(role="Teacher"):
        my_projects = db((db.user_project.assigned_user == auth.user.id)&(db.project.id == db.user_project.project)).select()
        for project in my_projects:
            for assignation in project.project.user_project.select():
                q=((assignation.report((db.report.status == db.report_status.id)&((db.report_status.name == 'Grading')|(db.report_status.name == 'EnabledForTeacher')))))
                var_count_report = var_count_report + q.count()


if auth.has_membership(role="Academic"):
    academic_var = db.academic(db.academic.id_auth_user==auth.user.id)
    if academic_var is not None:
        assignation_var = db((db.academic_course_assignation.carnet==academic_var.id)).select(db.academic_course_assignation.assignation,distinct=True)
        for assignation in assignation_var:
            for a in db((db.notification_general_log4.course==assignation.assignation.name)).select():
                var_query = db.notification_log4((db.notification_log4.register==a.id) & (db.notification_log4.username==auth.user.username))
                
                if var_query != None:
                    if db((db.read_mail.id_auth_user == auth.user.id) & (db.read_mail.id_mail == a.id) ).select().first() == None:
                        cont_news = cont_news + 1
                    pass
                pass
            pass
        
if auth.has_membership(role="Ecys-Administrator"):
    response.menu.extend([(T('Manage')+" "+T('Academic Control'), False, URL('activity_control','courses_list'), [])
    ])

if auth.has_membership(role="Student"):
    response.menu.extend([(T('Final Practice'), False,  URL('student', 'index'), [])
    ])

if auth.has_membership(role="Academic") or auth.has_membership(role="Student") or auth.has_membership(role="Teacher"):
    response.menu.extend([
        (T('My Courses')+"", False, URL('activity_control','courses_list'), [])
        ])


if auth.has_membership(role="Student") or auth.has_membership(role="Academic") or auth.has_membership(role="Teacher"):
    response.menu.extend([
        (T('Inbox')+" ("+str(cont_news)+")", False, URL('notification_student','inbox'), [])
    ])

if auth.has_membership(role="Teacher"):
    response.menu.extend([(T('Requests')+" ("+str(var_count + var_count_report)+")", False, URL(), [
                (T('Reports Pending Grading')+ " ("+str(var_count_report)+")", False, URL('teacher', 'todo_reports'), []),
                (T('Request control')+" ("+str(var_count)+")", False, URL('activity_control','courses_list_request'), []),]),
        
    ])

if auth.has_membership(role="DSI") and \
 not auth.has_membership(role="Super-Administrator"):
    response.menu.extend([(T('DSI tasks'), False, URL('dsi', 'index'), [])])
elif auth.has_membership(role="Super-Administrator"):
    response.menu.extend([(T('DSI tasks'), False, URL('admin', 'delivered'), [])])
user_menu = []
if not (auth.is_logged_in()):
    user_menu.append((T('View Events'), False, URL('default','events'), []))
if (auth.is_logged_in()):
    user_menu.append((T('View Events'), False, URL('default','events'), []))
        

if auth.has_membership(role="Super-Administrator"):
    user_menu.append((T('Academic'), False, URL(), [
    (T('General List of Academic'), False, URL('student_academic','academic'), []),    
    ]))

if auth.has_membership(role="Super-Administrator"):
    user_menu.append((T('Academic Control'), False, URL(), [
        (T('Manage')+" "+T('Academic Control'), False, URL('activity_control','courses_list'), []),
        (T('Pending Requests'), False, URL('activity_control','courses_list_request'), []),
        ((T('Parameters'), False, URL(), [    
            (T('Categories for weighting'), False, URL('activity_control','activity_category'), []),
            (T('Partials Management'), False, URL('activity_control','partials'), []),
            (T('Period'), False, URL('activity_control','student_control_period'), [])
        ])),
        ((T('Exceptions'), False, URL(), [    
            (T('Course and Laboratory Exceptions'), False, URL('activity_control','course_laboratory_exception'), []),
            (T('Course Time Limit Exception'), False, URL('activity_control','course_limit_exception'), [])
        ]))
    ]))
    user_menu.append((T('Evaluations'), False, URL(), [
        (T('Manage Templates'), False, URL('evaluation','evaluation_template'), []),
        (T('Manage Evaluations'), False, URL('evaluation','evaluation'), []),
        (T('History Evaluations'), False, URL('evaluation','evaluation_history'), []),

        ((T('Template Parameters'), False, URL(), [    
            (T('Answers'), False, URL('evaluation','answer'), []),
            (T('Type answer'), False, URL('evaluation','answer_type'), []),
            (T('Type question'), False, URL('evaluation','question_type'), []),
            (T('Type evaluation'), False, URL('evaluation','evaluation_type'), [])
        ]))
        
    ]))

if auth.has_membership(role="Super-Administrator"):
    user_menu.append((T('Audit'), False, URL(), [
    (T('Teacher notices'), False, URL('audit','audit_teacher_mail_notifications_areas'), []),
    (T('Student notices'), False, URL('audit', 'audit_student_mail_notifications_areas'), []),
    (T('Log academic'), False, URL('audit', 'audit_academic'), []),
    (T('Log academic assignation'), False, URL('audit', 'audit_academic_assignation_areas'), []),
    ]))
response.menu.extend(user_menu)
DEVELOPMENT_MENU = False

#########################################################################
## provide shortcuts for development. remove in production
#########################################################################

def _():
    # shortcuts
    app = request.application
    ctr = request.controller
    # useful links to internal and external resources
    response.menu += [
        (SPAN('web2py', _class='highlighted'), False, 'http://web2py.com', [
        (T('My Sites'), False, URL('admin', 'default', 'site')),
        (T('This App'), False, URL('admin', 'default', 'design/%s' % app), [
        (T('Controller'), False,
         URL(
         'admin', 'default', 'edit/%s/controllers/%s.py' % (app, ctr))),
        (T('View'), False,
         URL(
         'admin', 'default', 'edit/%s/views/%s' % (app, response.view))),
        (T('Layout'), False,
         URL(
         'admin', 'default', 'edit/%s/views/layout.html' % app)),
        (T('Stylesheet'), False,
         URL(
         'admin', 'default', 'edit/%s/static/css/web2py.css' % app)),
        (T('DB Model'), False,
         URL(
         'admin', 'default', 'edit/%s/models/db.py' % app)),
        (T('Menu Model'), False,
         URL(
         'admin', 'default', 'edit/%s/models/menu.py' % app)),
        (T('Database'), False, URL(app, 'appadmin', 'index')),
        (T('Errors'), False, URL(
         'admin', 'default', 'errors/' + app)),
        (T('About'), False, URL(
         'admin', 'default', 'about/' + app)),
        ]),
            ('web2py.com', False, 'http://www.web2py.com', [
             (T('Download'), False,
              'http://www.web2py.com/examples/default/download'),
             (T('Support'), False,
              'http://www.web2py.com/examples/default/support'),
             (T('Demo'), False, 'http://web2py.com/demo_admin'),
             (T('Quick Examples'), False,
              'http://web2py.com/examples/default/examples'),
             (T('FAQ'), False, 'http://web2py.com/AlterEgo'),
             (T('Videos'), False,
              'http://www.web2py.com/examples/default/videos/'),
             (T('Free Applications'),
              False, 'http://web2py.com/appliances'),
             (T('Plugins'), False, 'http://web2py.com/plugins'),
             (T('Layouts'), False, 'http://web2py.com/layouts'),
             (T('Recipes'), False, 'http://web2pyslices.com/'),
             (T('Semantic'), False, 'http://web2py.com/semantic'),
             ]),
            (T('Documentation'), False, 'http://www.web2py.com/book', [
             (T('Preface'), False,
              'http://www.web2py.com/book/default/chapter/00'),
             (T('Introduction'), False,
              'http://www.web2py.com/book/default/chapter/01'),
             (T('Python'), False,
              'http://www.web2py.com/book/default/chapter/02'),
             (T('Overview'), False,
              'http://www.web2py.com/book/default/chapter/03'),
             (T('The Core'), False,
              'http://www.web2py.com/book/default/chapter/04'),
             (T('The Views'), False,
              'http://www.web2py.com/book/default/chapter/05'),
             (T('Database'), False,
              'http://www.web2py.com/book/default/chapter/06'),
             (T('Forms and Validators'), False,
              'http://www.web2py.com/book/default/chapter/07'),
             (T('Email and SMS'), False,
              'http://www.web2py.com/book/default/chapter/08'),
             (T('Access Control'), False,
              'http://www.web2py.com/book/default/chapter/09'),
             (T('Services'), False,
              'http://www.web2py.com/book/default/chapter/10'),
             (T('Ajax Recipes'), False,
              'http://www.web2py.com/book/default/chapter/11'),
             (T('Components and Plugins'), False,
              'http://www.web2py.com/book/default/chapter/12'),
             (T('Deployment Recipes'), False,
              'http://www.web2py.com/book/default/chapter/13'),
             (T('Other Recipes'), False,
              'http://www.web2py.com/book/default/chapter/14'),
             (T('Buy this book'), False,
              'http://stores.lulu.com/web2py'),
             ]),
            (T('Community'), False, None, [
             (T('Groups'), False,
              'http://www.web2py.com/examples/default/usergroups'),
                        (T('Twitter'), False, 'http://twitter.com/web2py'),
                        (T('Live Chat'), False,
                         'http://webchat.freenode.net/?channels=web2py'),
                        ]),
                (T('Plugins'), False, None, [
                        ('plugin_wiki', False,
                         'http://web2py.com/examples/default/download'),
                        (T('Other Plugins'), False,
                         'http://web2py.com/plugins'),
                        (T('Layout Plugins'),
                         False, 'http://web2py.com/layouts'),
                        ])
                ]
         )]
if DEVELOPMENT_MENU: _()

if "auth" in locals(): auth.wikimenu()

