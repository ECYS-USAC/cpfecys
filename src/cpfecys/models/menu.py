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
response.meta.author = 'Boris Aguilar <me@borisaguilar.com> & Omar Vides <omarvides@gmail.com> & William Abdalla <wil.fuentes005@gmail.com> & Gustavo Vega <lecatavo@gmail.com>'
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
        (T('Users'), False, URL(),[
             (T('Users'), False, URL('admin', 'users'), []),
             (T('Academic'), False, URL('student_academic','academic'), []),
             (T('Roles'), False, URL('admin', 'roles'), []),
             ]),
        (T('Assignation'), False, URL(),[
             (T('Final Practices'), False, URL('admin', 'assignations'), []),
             (T('Project Leaders'), False, URL('admin', 'active_teachers'), []),
             (T('Final Practice Admin'), False, URL('admin', 'final_practice'), []),
             (T('Project Admin'), False, URL(),[
                (T('Areas'), False, URL('admin', 'areas'), []),
                (T('Projects'), False, URL('admin', 'projects'), []),
                ]),
             ]),
         (T('Academic Control'), False, URL(), [
            (T('Manage')+" "+T('Academic Control'), False, URL('activity_control','courses_list'), []),
            (T('Pending Requests'), False, URL('activity_control','courses_list_request'), []),
            ((T('Exceptions'), False, URL(), [    
                (T('Course and Laboratory Exceptions'), False, URL('activity_control','course_laboratory_exception'), []),
                (T('Course Time Limit Exception'), False, URL('activity_control','course_limit_exception'), [])
            ]))
        ]),
         (T('Practice Reports'), False, URL(),[
            ((T('Reports'), False, URL(), [ 
                (T('Reports and Restrictions'), False, URL('admin', 'report_restrictions'), []),
                (T('Report Mandatory Blocks'), False, URL('admin', 'report_requirements'), []),
                (T('Course Report Exceptions'), False, URL('admin', 'course_report_exception'), []),
                (T('Reports by status'), False, URL('admin', 'report_list'), []),
            ])),
            ((T('Items'), False, URL(), [ 
                (T('Items Manager'), False, URL('admin', 'items_manager'), []),   
                (T('Delivered Items Administrator'), False, URL('admin', 'manage_items/periods'), []),
                (T('Delivered Download'), False, URL('admin', 'delivered_download'), [])
            ])),
             (T('Anomalies per periods'), False, URL('admin', 'anomalies_list/periods'), [])
         ]),
        (T('Evaluations')+" 360", False, URL(), [
            (T('Manage Templates'), False, URL('evaluation','evaluation_template'), []),
            (T('Manage Evaluations'), False, URL('evaluation','evaluation'), []),
            (T('Evaluations Repository'), False, URL('evaluation','repository_evaluation'), []),
            ((T('Template Parameters'), False, URL(), [    
                (T('Answers'), False, URL('evaluation','answer'), []),
                (T('Templates'), False, URL('evaluation','template'), []),
                (T('Type answer'), False, URL('evaluation','answer_type'), []),
                (T('Type question'), False, URL('evaluation','question_type'), []),
                (T('Type evaluation'), False, URL('evaluation','evaluation_type'), [])
            ]))            
        ]),
         
         
         (T('Configuration'), False, URL(),[
            (T('System Parameters'), False, URL('admin', 'parameters'), []),
            ((T('Academic Control Parameters'), False, URL(), [    
                (T('Categories for weighting'), False, URL('activity_control','activity_category'), []),
                (T('Partials Management'), False, URL('activity_control','partials'), []),
                (T('Period'), False, URL('activity_control','student_control_period'), [])
            ])),
            (T('Configuration Web Service'), False, URL('student_academic', 'student_validation_parameters'), []),
            (T('Assignation Freeze Dates'), False, URL('admin', 'assignation_freeze'), []),
         ]),
         (T('Frontend'), False, URL(),[
             (T('Links'), False, URL('admin', 'links'), []),
             (T('Files'), False, URL('admin', 'files_manager'), []),
             (T('News'), False, URL('admin', 'notifications_manager'), []),
             (T('Send Mail'), False, URL('admin', 'mail_notifications'), []),
         ]),
         
         
    ])

cont_news = 0
project_list = []
if auth.has_membership(role="Teacher") or auth.has_membership(role="Student"):
    var_count = 0
    var_count_report = 0

    projects = db(db.user_project.assigned_user == auth.user.id).select(db.user_project.project,distinct=True)
    for project in projects:
        project_list.append(project.project.name)
        mails = db((db.academic_send_mail_log.course==project.project.name)).select()
        for a in mails:
            var_query = db.academic_send_mail_detail((db.academic_send_mail_detail.academic_send_mail_log==a.id) & (db.academic_send_mail_detail.username==auth.user.username))
                            
            if var_query != None:
                if db((db.read_mail_student.id_auth_user == auth.user.id) & (db.read_mail_student.id_mail == a.id) ).select().first() == None:
                    cont_news = cont_news + 1
                pass
            pass
        pass

        for a in db((db.notification_general_log4.course==project.project.name)).select(db.notification_general_log4.id,distinct=True):
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
        tempReports=[]
        my_projects = db((db.user_project.assigned_user == auth.user.id)&(db.project.id == db.user_project.project)).select()
        for project in my_projects:
            for assignation in project.project.user_project.select():
                teacher_var =db((db.user_project.project == assignation.project)&
                        (db.user_project.assigned_user == db.auth_user.id)&
                        (db.auth_membership.user_id == db.auth_user.id)&
                        (db.auth_membership.group_id == db.auth_group.id)&
                        (db.auth_group.role == 'Teacher')).select().first()
                if teacher_var is not None:
                    if teacher_var.user_project.assigned_user == auth.user.id:
                        q=((assignation.report((db.report.status == db.report_status.id)&((db.report_status.name == 'Grading')|(db.report_status.name == 'EnabledForTeacher')))))
                        for report in q.select():
                            tempReports.append(report.report.id)
        for report in db(db.report.id.belongs(tempReports)).select():
            var_count_report+=1



if auth.has_membership(role="Academic"):
    academic_var = db.academic(db.academic.id_auth_user==auth.user.id)
    if academic_var is not None:
        assignation_var = db((db.academic_course_assignation.carnet==academic_var.id)).select(db.academic_course_assignation.assignation,distinct=True)
        if len(project_list) == 0:
            project_list.append("-1")
            
        for assignation in assignation_var:
            for a in db((db.notification_general_log4.course==assignation.assignation.name)&(~db.notification_general_log4.course.belongs(project_list) )).select():
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

    response.menu.extend([(T('Management Reports'), False, URL(), [
        (T('Change Request Grades'), False, URL('management_reports','change_request_grades_management'), []),
        (T('Performance of students'), False, URL('management_reports','performance_students'), []),
        (T('History Evaluations'), False, URL('management_reports','evaluation_result'), [])
        ]),
    ])

    response.menu.extend([(T('School Reports'), False, URL(), [
        (T('General Information'), False, URL('school_reports','general_information'), []),
        (T('Overview of semester'), False, URL('school_reports','general_period'), []),
        (T('Historic per course'), False, URL('school_reports','historic_course'), []),
        (T('Percentage change of notes'), False, URL('school_reports','percentage_change_grades'), [])
        ]),
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
        


response.menu.extend(user_menu)
DEVELOPMENT_MENU = False

if auth.has_membership(role="Super-Administrator"):
    response.menu.extend([ (T('Reports'), False, URL(),[
            ((T('Summary Information of Practitioners'), False, URL(), [
                (T('Courses reports'), False, URL('admin', 'courses_report/areas'), []),
                (T('Summary of Semester'), False, URL('admin', 'general_report'), []),
            ])),
            ((T('Management in Real Time'), False, URL(), [
                (T('Management Academic'), False, URL('management_reports','student_management'), []),
                (T('Student Assignment'), False, URL('management_reports','student_assignment_management'), []),
                (T('Management Grades'), False, URL('management_reports','grades_management'), []),
                (T('Activities Metric'), False, URL('management_reports','activities_withmetric_management'), []),
                (T('Change Request Activities with Metric'), False, URL('management_reports','change_request_activities_with_metric_management'), []),
                (T('Change Request Grades'), False, URL('management_reports','change_request_grades_management'), []),
                (T('Performance of students'), False, URL('management_reports','performance_students'), []),
                (T('Evaluations'), False, URL('management_reports','evaluation_result'), [])
            ])),
            ((T('Notifications'), False, URL(), [
                (T('Teacher notices'), False, URL('audit','audit_teacher_mail_notifications_areas'), []),
                (T('Student notices'), False, URL('audit', 'audit_student_mail_notifications_areas'), []),
                (T('Mail Log'), False, URL('admin', 'mail_log'), []),
                (T('System-wide Mail Logs'), False, URL('mailer', 'index'), []),
            ])),             
             (T('Scheduler Report'), False, URL('admin', 'scheduler_activity'), []),
         ]),
    ])
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

