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

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################
response.menu = [(T('Home'), False, URL('default', 'index'), [])]
if auth.has_membership(role="Super-Administrator"):
    response.menu.extend([
        (T('Users Administration'), False, URL(),[
             (T('Final Practice Admin'), False, URL('admin', 'assignation'), []),
             (T('Users'), False, URL('admin', 'users'), []),
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
             (T('Notifications Manager'), False, URL('admin', 'notifications_manager'), []),
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
             ]),
         (T('System Configuration'), False, URL(),[
             (T('Parameters configuration'), False, URL('admin', 'parameters'), []),
             ]),
         (T('Reports'), False, URL(),[
             (T('Courses reports'), False, URL('admin', 'courses_report/areas'), []),
             (T('Active Teachers'), False, URL('admin', 'active_teachers'), []),
             ]),
    ])
if auth.has_membership(role="Teacher"):
    response.menu.extend([(T('Courses'), False, URL('teacher', 'courses'), []),
    (T('Reports Pending Grading'), False, URL('teacher', 'todo_reports'), []),
    ])
if auth.has_membership(role="Student"):
    response.menu.extend([(T('Final Practice'), False, URL('student', 'index'), [])])
if auth.has_membership(role="DSI") and \
 not auth.has_membership(role="Super-Administrator"):
    response.menu.extend([(T('Delivered Items'), False, URL('dsi', 'index'), [])])
else:
    response.menu.extend([(T('Delivered Items'), False, URL('admin', 'delivered'), [])])

if auth.is_logged_in():
    user_menu = []
    user_menu.append((T('Edit Schedules'), False, URL('default', 'event_edition'), []))
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
