# coding: utf8
# intente algo como
@auth.requires_login()
def index():
    #Get the assignations of the current user!
    response.title = u"Constancia de Entrega de Reportes y Cumplimiento de requisitos de Práctica Final"
    #assignations = db((db.user_project.assigned_user == auth.user.id)&
    #                  (db.user_project.assignation_ignored == False)&(db.user_project.assignation_status == db.assignation_status.id) & (db.assignation_status.name == 'Successful')).select(db.user_project.ALL)
    #assignations_html = DIV()

    def get_body(assignation):
        assignations_html = DIV()
    #for assignation in assignations:
        assignation_finished = True
        report_average = 0

        if (assignation.assignation_status == None) or \
           (assignation.assignation_status.name == 'Failed'):
                session.flash = T('Invalid Action')
                return dict()
        #Get the assigned user that is a teacher withing same user_project
        dude_in_charge = db((db.user_project.project == assignation.project)&
                        (db.user_project.assigned_user == db.auth_user.id)&
                        (db.auth_membership.user_id == db.auth_user.id)&
                        (db.auth_membership.group_id == db.auth_group.id)&
                        (db.auth_group.role == 'Teacher')).select().first()
        if not dude_in_charge is None:
            dude_in_charge = dude_in_charge.auth_user.first_name + ' ' + dude_in_charge.auth_user.last_name
        else:
            dude_in_charge = "Sin Asignar"
        #Get the reports of the assignation
        #Get the items for the assignation
        reports = db(db.report.assignation == assignation.id).select()
        report_body = TBODY()
        total_reports = 0
        acum_score = 0
        for report in reports:
            total_reports += 1
            created_date = report.created
            if report.never_delivered:
                created_date = 'Nunca Entregado'
            score = str(report.score)
            score_date = report.score_date
            if report.dtt_approval == False:
                score = (str(report.score) or '0') + ', reprobado DTT.'
                acum_score += 0
            if report.dtt_approval == None:
                score = (str(report.score) or '0') + ', pendiente DTT.'
                acum_score += 0
            if not report.admin_score is None:
                score_date = 'Calificado por DTT'
                acum_score += ((report.admin_score) or 0)
                score = str(report.admin_score)
            else:
                acum_score += (report.score or 0)
            report_body.append(TR(TD(report.report_restriction.name),
                                  TD("  "),
                                  TD(report.created),
                                  
                                  TD(score_date or 'Nunca Calificado'),
                                  TD("     "),
                                  TD(score or '0')))
        rows_report = [THEAD(TR(TH("Reporte",_width="25%"),
                                TH("     ",_width="15%"),
                                TH("Fecha Entrega",_width="15%"),
                                
                                TH("Fecha Calificación",_width="20%"),
                                TH("  ",_width="5%"),
                                TH("Nota",_width="5%"))),
                       report_body]

        items_head = TBODY()
        items = db((db.item.assignation == assignation)&
                   (db.item.is_active == True)).select()
        items_total = 0
        for item in items:
            items_total += 1
            item_type = 'Desconocido'
            if item.item_restriction.item_type == db.item_type(name = 'File'):
                item_type = 'Archivo'
            elif item.item_restriction.item_type == db.item_type(name = 'Activity'):
                item_type = 'Requisito'
            elif item.item_restriction.item_type == db.item_type(name = 'Grade Activity'):
                item_type = 'Con Nota: ' + str(item.score)
            elif item.item_restriction.item_type == db.item_type(name = 'Schedule'):
                item_type = 'Horario'
            items_head.append(TR(TD(item.item_restriction.name),
                                 TD(T(item.created.period.name) + ' - ' + str(item.created.year)),
                                 TD()))
            pass
        rows_items = [THEAD(TR(TH("Entregable",_width="33%"),
                        TH("Fecha Entrega",_width="33%"),
                        TH("Tipo Entregable",_width="33%"))),
                      items_head]

        table_items = TABLE(*rows_items, _border="0", _align="center", _width="100%")

        table_reports = TABLE(*rows_report, _border="0", _align="center", _width="100%")
        if total_reports > 0:
            report_average = float(acum_score)/float(total_reports)
        reports = DIV(H3('Resumen de Reportes'), table_reports, B('Promedio: '), SPAN(report_average or '0'))
        items = DIV(H3('Resumen de Entregables'), table_items)
        s = T(assignation.period.period.name) + str(" - ") + str(assignation.period.yearp)
        rows = [THEAD(TR(TH("",_width="25%"),
                         TH("",_width="40%"),
                         TH("",_width="25%"),
                         TH("",_width="10%"))),
                TBODY(TR(TD(B(u"Inicio de Asignación:")),TD(s),
                         TD(B(u"Duración de Asignación:")), TD(str(assignation.periods) + " Semestres")),
                      #TR(),
                      TR(TD(B(u"Código Área:")),TD(assignation.project.area_level.id)),
                      TR(TD(B(u"Código Proyecto:")),TD(assignation.project.project_id)),
                      TR(TD(B(u"Área:")),TD(str(assignation.project.area_level.name))),
                      TR(TD(B(u"Proyecto:")),TD(assignation.project.name)),
                      TR(TD(B(u"Encargado(a):")),TD(dude_in_charge)),
                      #TR(),
                      TR(TD(B(u"Carnet:")),TD(assignation.assigned_user.username)),
                      TR(TD(B(u"Nombre del Practicante:")),
                         TD(assignation.assigned_user.first_name + ' ' + assignation.assigned_user.last_name)),
                      TR(),
                      TR(TD(B(u"Total de Reportes:")),TD(total_reports),
                         TD(B(u"Promedio de Reportes:")),TD(report_average)),
                      TR(TD(B(u"Total de Entregables:")),TD(items_total)))]
        table_assignation = TABLE(*rows, _border="0", _align="center", _width="100%")
        assignations_html.append(SPAN(H3('Resumen de Asignación'),table_assignation,reports,
                                #HR(),
                                #HR()
                                ))
        return DIV(H2(u'Asignaciones a Proyectos'),assignations_html)
    #placeholder = DIV(H2(u'Asignaciones a Proyectos'),assignations_html)
    if request.extension == 'pdf':
        from gluon.contrib.pyfpdf import FPDF, HTMLMixin
        # create a custom class with the required functionalities 
        class MyFPDF(FPDF, HTMLMixin):
            def header(self):
                "hook to draw custom page header (logo and title)"
                import os
                import cpfecys
                logo = cpfecys.get_custom_parameters().clearance_logo
                if (logo is None) or (logo == ' ') or (logo == ''):
                    logo=os.path.join(request.folder,'static/logo-usac.png')
                else:
                    logo = os.path.join(request.folder, 'uploads', logo)
                #self.image(logo,10,8,33)
                self.set_font('Times','B',18)
                self.cell(35) # padding
                self.cell(155,7,"UNIVERSIDAD DE SAN CARLOS DE GUATEMALA",0,1,'L')
                self.set_font('Times','',16)
                self.cell(35) # padding
                self.cell(155,7,u"FACULTAD DE INGENIERÍA",0,1,'L')
                self.cell(35) # padding
                self.cell(155,8,u"Escuela de Ciencias y Sistemas",0,1,'L')
                self.cell(35) # padding
                self.cell(155,7,u"Desarrollo de Transferencia Tecnológica (DTT)",0,1,'L')
                self.ln(5)
                self.cell(190,0,'',1,1,'L')
                self.ln(5)
                
                #self.cell(35) # padding
                #self.set_font('Times','B',18)
                #self.cell(190,7,"Constancia de Entrega de Reportes y Cumplimiento",0,1,'C')
                #self.cell(35) # padding
                #self.cell(190,7,"de",0,1,'C')
                #self.cell(35) # padding
                #self.cell(190,7,u"Requisitos de Práctica Final",0,1,'C')
                self.ln(1)

            def footer(self):
                "hook to draw custom page footer (printing page numbers)"
                self.set_y(-25)
                self.set_font('Arial','I',8)
                txt = u'Página %s de %s' % (self.page_no(), self.alias_nb_pages())
                self.ln(2)
                self.cell(0,5,u'Firma:_______________________', 0, 1, 'C')
                import cpfecys
                cparams = cpfecys.get_custom_parameters()
                self.cell(0,4,unicode(cparams.coordinator_name,"utf-8"), 0, 1, 'C')
                #print "cparams.coordinator_title:"+str(cparams.coordinator_name)
                self.cell(0,4,unicode(cparams.coordinator_title,"utf-8"), 0, 1, 'C')
                import datetime
                self.cell(0,5,'Generado: ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),0,0,'L')
                self.cell(0,5,txt,0,1,'R')
        pdf=MyFPDF()
        # create a page and serialize/render HTML objects
        
        assignations = db((db.user_project.assigned_user == request.vars['user'])&
                          (db.user_project.assignation_ignored == False)&(db.user_project.assignation_status == db.assignation_status.id) & (db.assignation_status.name == 'Successful')).select(db.user_project.ALL)
        for x in assignations:
            pdf.add_page()
            pdf.write_html(unicode(str(XML(SPAN(B(CENTER('Solvencia de Entrega de Reportes y Cumplimiento ')),B(CENTER("de")),B(CENTER("Requisitos de Práctica Final")),DIV(get_body(x))),
                                       sanitize=False)), "utf-8"))
        #pdf.write_html(str(XML(CENTER(chart), sanitize=False)))
        # prepare PDF to download:
        response.headers['Content-Type']='application/pdf'
        return pdf.output(dest='S')
    else:
        return dict(message="hello from certificate.py")
