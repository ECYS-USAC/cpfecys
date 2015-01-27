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
def student_validation_parameters_fields():
    svp=db(db.validate_student).select().first()
    if svp is not None:
        db.validate_student_parameters.validate_student.default = svp.id
        db.validate_student_parameters.validate_student.writable = False
        db.validate_student_parameters.validate_student.readable = False
        grid = SQLFORM.grid(db.validate_student_parameters, csv=False)
        return dict(grid=grid)
    else:
        session.flash = T('Not valid Action.')
        redirect(URL('default','index'))


@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def student_validation_parameters():
    svp=db(db.validate_student).select().first()
    db.validate_student.id.writable = False
    db.validate_student.id.readable = False
    if svp is None:
        grid = SQLFORM.grid(db.validate_student, csv=False, paginate=1, searchable=False)
    else:
        links = [lambda row: A(T('Web Service Parameters'),
        _role='label',
        _href=URL('student_academic', 'student_validation_parameters_fields'),
        _title=T('Web Service Parameters'))]
        grid = SQLFORM.grid(db.validate_student, csv=False, paginate=1, create=False, searchable=False, links=links)
    return dict(grid=grid)




@auth.requires_login()
@auth.requires(auth.has_membership('Student') or auth.has_membership('Teacher') or auth.has_membership('Super-Administrator') or auth.has_membership('Ecys-Administrator'))
def check_student(check_carnet):
    svp=db(db.validate_student).select().first()
    if svp is not None:
        try:
            #CONSUME THE WEBSERVICE
            from gluon.contrib.pysimplesoap.client import SoapClient
            from gluon.contrib.pysimplesoap.client import SimpleXMLElement
            client = SoapClient(
                location = svp.supplier,
                action = svp.supplier+"/"+svp.action_service,
                namespace = svp.supplier,
                soap_ns=svp.type_service, trace = True, ns = False)

            import cpfecys
            year = cpfecys.current_year_period()
            sent="<"+svp.send+">"
            for svpf in db(db.validate_student_parameters).select():
                sent +="<"+svpf.parameter_name_validate+">"+svpf.parameter_value_validate+"</"+svpf.parameter_name_validate+">"
            sent += "<CARNET>"+str(check_carnet)+"</CARNET><CICLO>"+str(year.yearp)+"</CICLO></"+svp.send+">"
            back = client.call(svp.action_service,xmlDatos=sent)

            #PREPARE FOR RETURNED XML WEB SERVICE
            xml = back.as_xml()
            
            xml=xml.replace('&lt;','<')
            xml=xml.replace('&gt;','>')
            inicio = xml.find("<"+svp.receive+">")
            final = xml.find("</"+svp.receive+">")
            xml = xml[inicio:(final+17)]
            import xml.etree.ElementTree as ET
            root = ET.fromstring(xml)
            xml = SimpleXMLElement(xml)

            #VARIABLE TO CHECK THE CORRECT FUNCTIONING
            CARNET = xml.CARNET
            NOMBRES = xml.NOMBRES
            APELLIDOS= xml.APELLIDOS
            CORREO = xml.CORREO

            #Unicode Nombres
            try:
                str(NOMBRES)
            except:
                apellidos_var = unicode(NOMBRES).split(' ')
                appellidos_return = None
                for apellido in apellidos_var:                
                    try:
                        if appellidos_return is None:
                            appellidos_return = str(apellido)
                        else:                        
                            appellidos_return = appellidos_return + " " + str(apellido)
                    except:          
                        try:

                            temp = unicode(apellido).encode('utf-8').replace('Ã¡','á').replace('Ã©','é').replace('Ã­','í').replace('Ã³','ó').replace('Ãº','ú').replace('Ã±','ñ').replace('Ã','Á').replace('Ã‰','É').replace('Ã','Í').replace('Ã“','Ó').replace('Ãš','Ú').replace('Ã‘','Ñ').replace('Ã¼‘','ü')
                        except:
                            None

                        apellido = temp
                        if appellidos_return is None:
                            appellidos_return = str(apellido)
                        else:                        
                            appellidos_return = appellidos_return + " " + str(apellido)
                        
                NOMBRES = appellidos_return
            #Unicode APELLIDOS
            try:
                str(APELLIDOS)
            except:
                apellidos_var = unicode(APELLIDOS).split(' ')
                appellidos_return = None
                for apellido in apellidos_var:                
                    try:
                        if appellidos_return is None:
                            appellidos_return = str(apellido)
                        else:                        
                            appellidos_return = appellidos_return + " " + str(apellido)
                    except:          
                        try:

                            temp = unicode(apellido).encode('utf-8').replace('Ã¡','á').replace('Ã©','é').replace('Ã­','í').replace('Ã³','ó').replace('Ãº','ú').replace('Ã±','ñ').replace('Ã','Á').replace('Ã‰','É').replace('Ã','Í').replace('Ã“','Ó').replace('Ãš','Ú').replace('Ã‘','Ñ').replace('Ã¼‘','ü')
                        except:
                            None

                        apellido = temp
                        if appellidos_return is None:
                            appellidos_return = str(apellido)
                        else:                        
                            appellidos_return = appellidos_return + " " + str(apellido)
                        
                APELLIDOS = appellidos_return


            

            if (CARNET is None or CARNET=='') and (NOMBRES is None or NOMBRES=='') and (APELLIDOS is None or APELLIDOS=='') and (CORREO is None or CORREO==''):
                return dict(flag=False,error=False,message=T('The record was removed because the user is not registered to the academic cycle'))
            else:
                isStuden=False
                for c in root.findall('CARRERA'):
                    if c.find('UNIDAD').text=="08" and c.find('EXTENSION').text=="00" and (c.find('CARRERA').text=="05" or c.find('CARRERA').text=="09" or c.find('CARRERA').text=="07"):
                        isStuden=True

                if isStuden==False:
                    return dict(flag=False,error=False,message=T('The record was removed because students not enrolled in career allowed to use the system'))
                else:
                    return dict(flag=True, carnet=int(str(CARNET)), nombres=(NOMBRES), apellidos=(APELLIDOS), correo=str(CORREO),error=False)
        except:
            return dict(flag=False,error=True,message=T('Error with web service validation'))
    else:
        return dict(flag=False,error=True,message=T('Error with web service validation'))



@auth.requires_login()
@auth.requires(auth.has_membership('Student') or auth.has_membership('Teacher'))
def attendance_list():
    if request.vars['list'] != None:
        academic_var = db.auth_group(db.auth_group.role=='Academic')
        academic_list = db((db.academic_course_assignation.semester == request.vars['period']) & (db.academic_course_assignation.assignation==request.vars['project'])).select()
        for academic_temp in academic_list:
            user_var = db.auth_user(db.auth_user.username==academic_temp.carnet.carnet)

            if user_var is None:
                #WEBSERVICE
                web_service = check_student(academic_temp.carnet.carnet)
                
                if web_service['flag'] == True:
                    id_user = db.auth_user.insert(first_name = web_service['nombres'],
                                last_name =  web_service['apellidos'],
                                email = web_service['correo'],
                                username = academic_temp.carnet.carnet,
                                phone = '12345678',
                                home_address = T('Enter your address'))
                    #Add the id_auth_user to academic.
                    db(db.academic.id == academic_temp.carnet.id).update(id_auth_user = id_user.id)
                    #Create membership to academic
                    db.auth_membership.insert(user_id = id_user.id, group_id =  academic_var.id)
                    message = [] 
                    message.append(academic_temp.carnet.carnet)
                    message.append(T('Profile was created successfully'))
                    if session.assignation_message is None:
                        session.assignation_message = []
                        session.assignation_message.append(message)
                    else:
                        session.assignation_message.append(message)  
                else:
                    message = [] 
                    message.append(academic_temp.carnet.carnet)
                    message.append(web_service['message'])
                    if session.assignation_error is None:
                        session.assignation_error = []
                        session.assignation_error.append(message)
                    else:
                        session.assignation_error.append(message)

                    if web_service['error'] == False:
                        db(db.academic.id == academic_temp.carnet.id).delete()

                        result = db(db.auth_membership.user_id==auth.user.id).select()
                        roll_var = ''
                        i = 0;
                        for a in result:
                            if i == 0:
                                roll_var = a.group_id.role
                                i = i+1
                            else:
                               roll_var = roll_var + ',' + a.group_id.role
                        import cpfecys
                        currentyear_period = cpfecys.current_year_period()
                        db.academic_log.insert(user_name = auth.user.username, 
                                    roll =  str(roll_var), 
                                    operation_log = 'delete', 
                                    before_carnet = academic_temp.carnet.carnet, 
                                    before_email = academic_temp.carnet.email, 
                                    id_period = str(currentyear_period.id),
                                    description = T('The record was removed because it failed the webservice validation'))

            else:
                message = [] 
                message.append(academic_temp.carnet.carnet)
                message.append(T('The student profile was already created'))
                if session.assignation_message is None:
                    session.assignation_message = []
                    session.assignation_message.append(message)
                else:
                    session.assignation_message.append(message)

                membership_var = db.auth_membership((db.auth_membership.user_id==user_var.id) & (db.auth_membership.group_id==academic_var.id))
                if membership_var is None:
                    #Create membership to academic
                    db.auth_membership.insert(user_id = user_var.id, group_id =  academic_var.id) 

                #Add the id_auth_user to academic. And update academic inforamtion  
                db(db.academic.id == academic_temp.carnet.id).update(id_auth_user = user_var.id,
                                                        email = user_var.email,
                                                        carnet = user_var.username)
                #academic_LOG 
                import cpfecys
                cperiod = cpfecys.current_year_period()
                db.academic_log.insert(user_name = 'system',
                                    roll = 'system',
                                    operation_log = 'update', 
                                    before_carnet = academic_temp.carnet.carnet, 
                                    before_email = academic_temp.carnet.email, 
                                    after_carnet = user_var.username, 
                                    after_email = user_var.email, 
                                    id_academic = academic_temp.carnet.id, 
                                    id_period = cperiod,
                                    description = T('Registration data was updated, set with the information entered by ')+str(auth.user.username))
        session.flash = T('Profiles created')
        redirect(URL('student_academic','academic_assignation',vars=dict(assignation=str(request.vars['project']))))
    else:
        def get_name(id_auth):
            var_return = db(db.auth_user.id == id_auth).select().first()
            if var_return is None:
                return ""
            else:
                return var_return.first_name + " " + var_return.last_name
        if request.vars['usuario_proyecto'] != None:
            check = db.user_project(id=request.vars['usuario_proyecto'], assigned_user = auth.user.id)
            project = db(db.project.id==check.project).select().first()
            periodo = db(db.period_year.id==check.period).select().first()
            alumnos = db((db.academic.id==db.academic_course_assignation.carnet)&(db.academic_course_assignation.assignation==project.id)&(db.academic_course_assignation.semester==periodo.id)).select()
            l=[]
            t=[]
            t.append(T('Assistance List'))
            l.append(t)

            t=[]
            t.append(project.project_id)
            t.append(project.name)
            p = T(periodo.period.name)+' '+str(periodo.yearp)
            t.append(p)
            l.append(t)
            t=[]
            t.append(None)
            l.append(t)
            
            t=[]
            t.append(T('Carnet'))
            t.append(T('Name'))
            t.append(T('Email'))
            t.append(T('Laboratory'))
            t.append(T('Signature'))
            l.append(t)
            for i in alumnos:
                t=[]
                t.append(i.academic.carnet)
                t.append(get_name(db(db.academic.id==int(i.academic.id)).select(db.academic.id_auth_user).first().id_auth_user))
                t.append(i.academic.email)
                if i.academic_course_assignation.laboratorio==True:
                    t.append(T('Yes'))
                else:
                    t.append('No')
                l.append(t)
            nombre='Listado '+project.name
            return dict(filename=nombre, csvdata=l)
        else:
            redirect(URL('default','index'))

@auth.requires_login()
@auth.requires(auth.has_membership('Student') or auth.has_membership('Teacher'))
def academic_assignation():
    #requires parameter year_period if no one is provided then it is 
    #automatically detected
    #and shows the current period
    assignation = request.vars['assignation']
    year_period = request.vars['year_period']
    max_display = 1
    import cpfecys
    currentyear_period = db.period_year(db.period_year.id == year_period)
    check = db.user_project(id=assignation, assigned_user = auth.user.id)
    if not currentyear_period:
        currentyear_period = cpfecys.current_year_period()
        changid = currentyear_period.id
    if (check is None):
        #check if there is no assignation or if it is locked (shouldn't be touched)
        if (session.last_assignation is None):
            redirect(URL('default','index'))
            return
        else:
            check = db.user_project(id = session.last_assignation)
            if cpfecys.assignation_is_locked(check):
                redirect(URL('default','index'))
                return
    else:
        session.last_assignation = check.id
    cyearperiod = cpfecys.current_year_period()

    #Temporal---------------------------------------------------------------------------------------------
    if request.vars['listado'] =='True':
        redirect(URL('student_academic','attendance_list',vars=dict(usuario_proyecto=str(check.id))))

    
    #Temporal---------------------------------------------------------------------------------------------



    if request.vars['search_var'] is None:
        query = ((db.academic_course_assignation.semester == currentyear_period.id) & (db.academic_course_assignation.assignation==check.project))
    else:
        query2 = db((db.academic_course_assignation.carnet == db.academic.id) & (db.academic_course_assignation.semester == currentyear_period.id) & (db.academic_course_assignation.assignation==check.project) & (db.academic.carnet.like('%'+request.vars['search_var']+'%')) ).select()
        dest = []
        query = None
        for q in query2:
            dest.append(q.academic.id)
            #consultar a la base de datos para obtener a los usuarios a los que enviaremos
        query = (db.academic_course_assignation.carnet.belongs(dest) & (db.academic_course_assignation.semester == currentyear_period.id) & (db.academic_course_assignation.assignation==check.project))
        
    
    fields = (db.academic_course_assignation.carnet, db.academic_course_assignation.laboratorio)

    db.academic_course_assignation.assignation.default = check.project
    db.academic_course_assignation.assignation.writable = False
    db.academic_course_assignation.assignation.readable = False
    db.academic_course_assignation.semester.default = currentyear_period.id
    db.academic_course_assignation.semester.writable = False
    db.academic_course_assignation.semester.readable = False
    db.academic_course_assignation.carnet.readable = False
    db.academic_course_assignation.laboratorio.readable = False

    #update form start
    update_form = FORM(INPUT(_name='academic_carnet',_type='text'),
                        INPUT(_name='laboratory_check',_type='checkbox'),
                        INPUT(_name='assignation_id',_type='text'),
                        INPUT(_name='laboratory_before',_type='text'),                        
                        INPUT(_name='delete_check',_type='checkbox'))

    if update_form.accepts(request.vars,formname='update_form'):
        try:
            #Search for user roles
            result = db(db.auth_membership.user_id==auth.user.id).select()
            roll_var = ''
            i = 0;
            for a in result:
                if i == 0:
                    roll_var = a.group_id.role
                    i = i+1
                else:
                   roll_var = roll_var + ',' + a.group_id.role

            if update_form.vars.laboratory_check == 'on':
                var_labo =  True
            else:
                var_labo =  False

            if update_form.vars.delete_check:
                var_aca = db(db.academic_course_assignation.id==update_form.vars.assignation_id).select().first()
                if db(db.grades.academic_assignation==update_form.vars.assignation_id).select().first() is None:
                    db(db.academic_course_assignation.id==update_form.vars.assignation_id).delete()
                    
                    db.academic_course_assignation_log.insert(user_name = auth.user.username, 
                                                            roll =  str(roll_var), 
                                                            operation_log = 'delete', 
                                                            before_carnet = update_form.vars.academic_carnet, 
                                                            before_course = var_aca.assignation.name,
                                                            before_year = var_aca.semester.yearp,
                                                            before_semester = var_aca.semester.period.name,
                                                            before_laboratory = str(var_labo),
                                                            id_period = str(currentyear_period.id),
                                                            description = T('Registration is removed from the page students'))
                    response.flash = T('Deleted register.')
                else:
                    response.flash = T('Can not be deleted because it has grades associated')
            else:
                if update_form.vars.laboratory_before != str(var_labo):
                    var_aca = db(db.academic_course_assignation.id==update_form.vars.assignation_id).select().first()

                    dont_delete = False

                    if var_labo == False:
                        grades = db(db.grades.academic_assignation==var_aca.id).select()
                        for g in grades:
                            if g.activity.laboratory == True:
                                dont_delete = True

                    if dont_delete == False:
                        db(db.academic_course_assignation.id==update_form.vars.assignation_id).update(laboratorio=var_labo)

                        db.academic_course_assignation_log.insert(user_name = auth.user.username, 
                                                roll =  roll_var, 
                                                operation_log = 'update', 
                                                before_carnet = str(var_aca.carnet.carnet), 
                                                before_course = var_aca.assignation.name,
                                                before_year = str(var_aca.semester.yearp),
                                                before_semester = var_aca.semester.period.name,
                                                before_laboratory = update_form.vars.laboratory_before,
                                                after_carnet = str(var_aca.carnet.carnet), 
                                                after_course = var_aca.assignation.name,
                                                after_year = str(var_aca.semester.yearp) ,
                                                after_semester = var_aca.semester.period.name,
                                                after_laboratory = str(var_labo),
                                                id_academic_course_assignation = update_form.vars.assignation_id,
                                                id_period = str(currentyear_period.id),
                                                description = T('Registration modified from the page from students')) 
    
                        response.flash = T('Updated register.')
                    else:
                        response.flash = T('Can not be modify because it has grades associated')
        except:
            response.flash = T('Error.')
    #update form finish

    def get_button_clas(carnet_pa):
        try:
            review = db((db.photo_review.user_id == str(db(db.academic.id==int(carnet_pa)).select(db.academic.id_auth_user).first().id_auth_user))).select().first()
            if review is None:
                class_button = 'btn btn-info'
            else:
                if review.accepted == True:
                    class_button = 'btn btn-success'
                else:
                    class_button = 'btn btn-danger'
            return class_button
        except:
            return 'btn'

    def get_auth_user(id_auth):
        var_return = db(db.auth_user.id == id_auth).select().first()
        if var_return is None:
            class temp:
                photo = ''
                first_name = ''
                last_name = ''
            return temp
        else:
            return var_return
    
    def get_photo_state(id_auth):
        review = db((db.photo_review.user_id == id_auth)).select().first()
        if review is None:
            class temp:
                result = T('Pending')
                color = 'blue'
            return temp
        else:
            if review.accepted == True:
                class temp:
                    result = T('Accepted')
                    color = 'green'
                return temp
            else:
                class temp:
                    result = T('rejected')
                    color = 'red'
                return temp
            pass
        pass

    def has_foto(id_auth):
        var_return = db(db.auth_user.id == id_auth).select().first()
        if var_return is None:
            return -1
        else:
            if var_return.photo is None:
                return -1
            else:
                return id_auth
        
    
    links = [{'header':T('Photo'), 
                'body':lambda row: A(IMG(_src= URL('default/download', get_auth_user((db(db.academic.id==int(row.carnet)).select(db.academic.id_auth_user).first().id_auth_user)).photo ), 
                    _width=50, _height=40, _id='image'), 
        _style="cursor:pointer;"        ,
        _onclick='set_photo("'+str(db(db.academic.id==int(row.carnet)).select(db.academic.id_auth_user).first().id_auth_user)+'");', 
        _title=T('View photo') ,**{"_data-toggle":"modal", "_data-target": "#picModal"}) 
                

                }]

    links += [{'header':T('Carnet'), 
                'body':lambda row:  str(db(db.academic.id==int(row.carnet)).select(db.academic.carnet).first().carnet)}]

    links += [{'header':T('Name'), 
                'body':lambda row:  str(get_auth_user((db(db.academic.id==int(row.carnet)).select(db.academic.id_auth_user).first().id_auth_user)).first_name) + " " + str(get_auth_user((db(db.academic.id==int(row.carnet)).select(db.academic.id_auth_user).first().id_auth_user)).last_name )}]


    links += [{'header':T('Email'), 
                'body':lambda row: (str( db(db.academic.id==int(row.carnet)).select(db.academic.email).first().email ))}]

    links += [{'header':T('Laboratory'), 
                'body':lambda row: T(str(row.laboratorio))}] 

    links += [{'header':T('Photo State'), 
                'body':lambda row: A(get_photo_state((db(db.academic.id==int(row.carnet)).select(db.academic.id_auth_user).first().id_auth_user)).result,
                    _id="label_"+str(db(db.academic.id==int(row.carnet)).select(db.academic.id_auth_user).first().id_auth_user),
                    _style="cursor:pointer; color:"+get_photo_state((db(db.academic.id==int(row.carnet)).select(db.academic.id_auth_user).first().id_auth_user)).color+";",
                    _onclick='set_photo("'+str(db(db.academic.id==int(row.carnet)).select(db.academic.id_auth_user).first().id_auth_user)+'");',**{"_data-toggle":"modal", "_data-target": "#picModal"} ) }] 


        

    if (request.vars['year_period'] is None) or (str(request.vars['year_period']) == str(cpfecys.current_year_period().id)):
        links += [{'header':T('Assignation'), 
                'body':lambda row: A(T('Edit'), 
            _role='button', 
            _class='btn', 
            _onclick='set_values('+str(row.id)+','\
                +str( db(db.academic.id==int(row.carnet)).select(db.academic.carnet).first().carnet )+','\
                +'"'+str( db(db.academic.id==int(row.carnet)).select(db.academic.email).first().email )+'",'\
                +'"'+str(row.laboratorio)+'")', 
            _title=T('Edit academic assignation')+' '+str( db(db.academic.id==int(row.carnet)).select(db.academic.carnet).first().carnet ) ,**{"_data-toggle":"modal", "_data-target": "#attachModal"})}]
    
    links += [lambda row: A(T('Accept Photo'),
                _class="btn btn-success",
                _onclick="click_acept_photo("+str(has_foto(db(db.academic.id==int(row.carnet)).select(db.academic.id_auth_user).first().id_auth_user))+")")]

    links += [lambda row: A(T('Reject Photo'),
                _class="btn btn-danger",
                _onclick="click_reject_photo("+str(has_foto(db(db.academic.id==int(row.carnet)).select(db.academic.id_auth_user).first().id_auth_user))+")")]
   
   
    if (currentyear_period.id == cpfecys.current_year_period().id):
        grid = SQLFORM.grid(query, orderby=db.academic_course_assignation.carnet,details=False, fields=fields, links=links, oncreate=oncreate_academic_assignation, onupdate=onupdate_academic_assignation, ondelete=ondelete_academic_assignation, csv=False, deletable=False, editable=False, paginate=100)
    else:
        checkProject = db((db.user_project.assigned_user==auth.user.id)&\
                        (db.user_project.project == check.project)&\
                        ((db.user_project.period <= currentyear_period.id) & \
                        ((db.user_project.period + db.user_project.periods) > currentyear_period.id))).select(db.user_project.ALL)
        b=0
        for a in checkProject:
            b=b+1
        if b!=0:
            grid = SQLFORM.grid(query, details=False , fields=fields, links=links, deletable=False, editable=False, create=False,csv=False, paginate=100)
        else:
            session.flash  =T('Not authorized')
            redirect(URL('default','index'))

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
                name = check.project.name,
                check = check,
                assignation = check.id)

def oncreate_academic_assignation(form):
    import datetime
    import cpfecys

    cdate = datetime.datetime.now()
    assignation = request.vars['assignation']
    
    
    currentyear_period = cpfecys.current_year_period()

    check = db.user_project(id=assignation, assigned_user = auth.user.id)
    if (check is None):
        #check if there is no assignation or if it is locked (shouldn't be touched)
        if (session.last_assignation is None):
            redirect(URL('default','index'))
            return
        else:
            check = db.user_project(id = session.last_assignation)
            if cpfecys.assignation_is_locked(check):
                redirect(URL('default','index'))
                return
    else:
        session.last_assignation = check.id
    #Search for user roles
    result = db(db.auth_membership.user_id==auth.user.id).select()
    roll_var = ''
    i = 0;
    for a in result:
        if i == 0:
            roll_var = a.group_id.role
            i = i+1
        else:
           roll_var = roll_var + ',' + a.group_id.role

    
    student_var = db(db.academic.id == form.vars.carnet).select()
    carnet_var = ''
    for a in student_var:
        carnet_var = a.carnet

    #Check that there is not an assignation
    usr2 = db((db.academic_course_assignation.id != form.vars.id) & (db.academic_course_assignation.semester == currentyear_period.id) & (db.academic_course_assignation.assignation == check.project) & (db.academic_course_assignation.carnet == form.vars.carnet)).select()
    i = 0;
    for a in usr2:
        i = i+1

    if i == 0: 
        #If there is not an assignation update the log
        session.flash = T('Se realizó la asignación')
        db.academic_course_assignation_log.insert(user_name = auth.user.username, 
                                                roll =  roll_var, 
                                                operation_log = 'insert', 
                                                after_carnet = carnet_var, 
                                                after_course = check.project.name,
                                                after_year = str(currentyear_period.yearp) ,
                                                after_semester = str(currentyear_period.period),
                                                after_laboratory = form.vars.laboratorio,
                                                id_academic_course_assignation = form.vars.id,
                                                id_period = str(currentyear_period.id),
                                                description = 'Se creo el registro desde la pagina Asignar Estudiantes')
    else:
        #If there is an assignation delete the last record
        db(db.academic_course_assignation.id==form.vars.id).delete()
        session.flash = T('Error: Ya existe la asignacion')


def onupdate_academic_assignation(form):
    import datetime
    import cpfecys

    cdate = datetime.datetime.now()
    assignation = request.vars['assignation']
    
    
    currentyear_period = cpfecys.current_year_period()

    check = db.user_project(id=assignation, assigned_user = auth.user.id)
    if (check is None):
        #check if there is no assignation or if it is locked (shouldn't be touched)
        if (session.last_assignation is None):
            redirect(URL('default','index'))
            return
        else:
            check = db.user_project(id = session.last_assignation)
            if cpfecys.assignation_is_locked(check):
                redirect(URL('default','index'))
                return
    else:
        session.last_assignation = check.id

    #Search for user roles
    result = db(db.auth_membership.user_id==auth.user.id).select()
    roll_var = ''
    i = 0;
    for a in result:
        if i == 0:
            roll_var = a.group_id.role
            i = i+1
        else:
            roll_var = roll_var + ',' + a.group_id.role

    #Search for carnet
    student_var = db(db.academic.id == form.vars.carnet).select()
    carnet_var = ''
    for a in student_var:
        carnet_var = a.carnet

    #Search for before values
    student_var2 = db(db.academic_course_assignation_log.id_academic_course_assignation == form.vars.id).select(orderby=db.academic_course_assignation_log.id)
    bef_carnet_var = ''
    course_var = ''
    year_var = ''
    semester_var = ''
    laboratory_var = ''
    for a in student_var2:
        bef_carnet_var = a.after_carnet
        course_var = a.after_course
        year_var = a.after_year
        semester_var = a.after_semester
        laboratory_var = a.after_laboratory
    if form.vars.delete_this_record != None:
        db.academic_course_assignation_log.insert(user_name = auth.user.username, 
                                                roll =  roll_var, 
                                                operation_log = 'delete', 
                                                before_carnet = bef_carnet_var, 
                                                before_course = course_var,
                                                before_year = year_var,
                                                before_semester = semester_var,
                                                before_laboratory = laboratory_var,
                                                id_period = str(currentyear_period.id),
                                                description = 'Se elimino el registro desde la pagina Asignar Estudiantes')
    else:
        #Check that there is not an assignation
        usr2 = db((db.academic_course_assignation.id != form.vars.id) & (db.academic_course_assignation.semester == currentyear_period.id) & (db.academic_course_assignation.assignation == check.project) & (db.academic_course_assignation.carnet == form.vars.carnet)).select()
        i = 0;
        for a in usr2:
            i = i+1

        if i == 0: 
            #If there is not an assignation update the log
            session.flash = T('Se realizó la modificacion')
            db.academic_course_assignation_log.insert(user_name = auth.user.username, 
                                                roll =  roll_var, 
                                                operation_log = 'update', 
                                                before_carnet = bef_carnet_var, 
                                                before_course = course_var,
                                                before_year = year_var,
                                                before_semester = semester_var,
                                                before_laboratory = laboratory_var,
                                                after_carnet = carnet_var, 
                                                after_course = check.project.name,
                                                after_year = str(currentyear_period.yearp) ,
                                                after_semester = str(currentyear_period.period),
                                                after_laboratory = form.vars.laboratorio,
                                                id_academic_course_assignation = form.vars.id,
                                                id_period = str(currentyear_period.id),
                                                description = 'Se modifico el registro desde la pagina Asignar Estudiantes')
        else:
            #If there is an assignation delete the last record
            #db(db.academic_course_assignation.id==form.vars.id).delete()
            temp_academic = db(db.academic.carnet==bef_carnet_var).select()
            id_academic = ''
            for a in temp_academic:
                id_academic = a.id
            db(db.academic_course_assignation.id==form.vars.id).update(carnet=id_academic,laboratorio=laboratory_var)
            session.flash = T('Error: Ya existe la asignacion, no se modifico el estudiante')
        

def ondelete_academic_assignation(table_involved, id_of_the_deleted_record):
    import datetime
    cdate = datetime.datetime.now()
    student_assignation_var = db.academic_course_assignation(id_of_the_deleted_record)  
    import cpfecys  
    currentyear_period = cpfecys.current_year_period()

    #Search for user roles
    result = db(db.auth_membership.user_id==auth.user.id).select()
    roll_var = ''
    i = 0;
    for a in result:
        if i == 0:
            roll_var = a.group_id.role
            i = i+1
        else:
            roll_var = roll_var + ',' + a.group_id.role

    project_name_var = ''
    project_var = db(db.project.id == student_assignation_var.assignation).select()
    for a in project_var:
        project_name_var = a.name

    db.academic_course_assignation_log.insert(user_name = auth.user.username, 
                                                roll =  roll_var, 
                                                operation_log = 'delete', 
                                                before_carnet = student_assignation_var.carnet.carnet, 
                                                before_course = student_assignation_var.assignation.name,
                                                before_year = str(student_assignation_var.semester.yearp) ,
                                                before_semester = str(student_assignation_var.semester.period),
                                                before_laboratory = student_assignation_var.laboratorio,
                                                id_period = str(currentyear_period.id),
                                                description = 'Se elimino el registro desde la pagina Asignar Estudiantes')

@auth.requires_login()
@auth.requires(auth.has_membership('Student') or auth.has_membership('Teacher'))
def periods():
    grid = SQLFORM.grid(db.period_year)
    return locals()

@auth.requires_login()
@auth.requires(auth.has_membership('Student') or auth.has_membership('Teacher'))
def academic_assignation_upload():
    def files():
        f = db(db.uploaded_file.name=='CargaEstudiantes_TutoresAcademicos').select()
        nameP = ''
        for p2 in f:
            nameP=p2.file_data
        return nameP
        return dict(nameP=nameP)

    assignation = request.vars['assignation']
    check = db.user_project(id=assignation, assigned_user = auth.user.id)
    name = check.project.name
    import csv
    error_users = []
    aviso_users = []
    success = False
    import cpfecys
    import datetime
    cdate = datetime.datetime.now()
    current_period = cpfecys.current_year_period()
    if request.vars.csvfile != None:
        try:
            file = request.vars.csvfile.file
        except AttributeError:
            response.flash = T('Please upload a file.')
            return dict(success = False,
                file = False,
                periods = periods,
                current_period = current_period,
                name=name, files=files)
        try:
            cr = csv.reader(file, delimiter=',', quotechar='"')
            success = True
            header = next(cr)
            for row in cr:
                ## parameters
                rcarnet = row[0]
                rlaboratorio = row[1]
                rlaboratorio = rlaboratorio.upper()
                ## check if user exists                
                check = db.user_project(id =assignation, assigned_user = auth.user.id)                      
                usr = db.academic(db.academic.carnet == rcarnet)        
                if usr is None:
                    #Email validation        
                    if rcarnet == '':
                        row.append(T('Error: ') + T('The id is a required field.'))
                        error_users.append(row)
                    else:            
                        #T o F validation
                        if rlaboratorio == 'TRUE':
                            rlaboratorio = 'T'
                        if rlaboratorio == 'FALSE':
                            rlaboratorio = 'F'

                        if rlaboratorio != 'T' and rlaboratorio != 'F':
                            row.append(T('Error: ') + T('The type of laboratory entered is incorrect. This must be T or F.'))
                            error_users.append(row)
                        else:
                            #insert a new user with csv data
                            session.academic_update = True
                            
                            usr = db.academic.insert(carnet = rcarnet,
                                                          email = "email@email.com")
                            #Add log
                            db.academic_log.insert(user_name = auth.user.username, 
                                                    roll =  'Student', 
                                                    operation_log = 'insert', 
                                                    after_carnet = rcarnet, 
                                                    after_email = "email@email.com", 
                                                    id_academic = usr.id,
                                                    id_period = current_period.id,
                                                    description = T('Inserted from CSV file.'))
                            #add user to the course
                            ingresado = db.academic_course_assignation.insert(carnet = usr.id, semester = current_period, assignation = check.project, laboratorio = rlaboratorio)
                            #Add to log
                            lab_var = ''
                            if rlaboratorio == 'T':
                                lab_var = 'True'
                            else:
                                lab_var = 'False'
                            #Search for user roles
                            result = db(db.auth_membership.user_id==auth.user.id).select()
                            roll_var = ''
                            i = 0;
                            for a in result:
                                if i == 0:
                                    roll_var = a.group_id.role
                                    i = i+1
                                else:
                                    roll_var = roll_var + ',' + a.group_id.role
                            db.academic_course_assignation_log.insert(user_name = auth.user.username, roll =  roll_var, 
                                                    operation_log = 'insert', 
                                                    after_carnet = rcarnet, 
                                                    after_course = str(check.project.name), 
                                                    after_year = str(current_period.yearp) ,
                                                    after_semester = str(current_period.period),
                                                    after_laboratory = lab_var,
                                                    id_academic_course_assignation = str(ingresado.id),
                                                    id_period = current_period.id,
                                                    description = T('Inserted from CSV file.'))
                            
                            try:
                                for var_error in session.assignation_error:
                                    var_ac = db(db.academic.carnet == var_error[0]).select().first()
                                    db(db.academic.carnet == var_error[0]).delete()
                                    result = db(db.auth_membership.user_id==auth.user.id).select()
                                    roll_var = ''
                                    i = 0;
                                    for a in result:
                                        if i == 0:
                                            roll_var = a.group_id.role
                                            i = i+1
                                        else:
                                           roll_var = roll_var + ',' + a.group_id.role
                                    

                                    db.academic_log.insert(user_name = auth.user.username, 
                                                roll =  str(roll_var), 
                                                operation_log = 'delete', 
                                                before_carnet = str(var_error[0]), 
                                                before_email = str(var_ac.email), 
                                                id_period = str(current_period.id),
                                                description = T('The record was removed because it failed the webservice validation'))
                            except:
                                None
                            if session.assignation_error == None:
                                #Agregar la advertencia que el usuario ya se encuentra registrado en el sistema
                                row.append(T('Aviso: ') + T('Successful assignment to the course'))
                                aviso_users.append(row)
                            else:
                                for var_error in session.assignation_error:
                                    row.append(T('Error: ') + ' '+ str(var_error[1]))
                                    error_users.append(row)
                            session.academic_update = None
                            session.assignation_error = None                                
                else:
                    
                    usr2 = db.academic_course_assignation((db.academic_course_assignation.semester == current_period) & (db.academic_course_assignation.assignation == check.project) & (db.academic_course_assignation.carnet == usr.id))
                    if usr2 is None:
                        #T o F validation
                        if rlaboratorio == 'TRUE':
                                rlaboratorio = 'T'
                        if rlaboratorio == 'FALSE':
                                rlaboratorio = 'F'
                            
                        if rlaboratorio != 'T' and rlaboratorio != 'F':
                            row.append(T('Error: ') + T('The type of laboratory entered is incorrect. This must be T or F.'))
                            error_users.append(row)
                        else:
                            lab_var = ''
                            if rlaboratorio == 'T':
                                lab_var = 'True'
                            else:
                                lab_var = 'False'

                            #Search for user roles
                            result = db(db.auth_membership.user_id==auth.user.id).select()
                            roll_var = ''
                            i = 0;
                            for a in result:
                                if i == 0:
                                    roll_var = a.group_id.role
                                    i = i+1
                                else:
                                    roll_var = roll_var + ',' + a.group_id.role
                            #Agregar la advertencia que el usuario ya se encuentra registrado en el sistema
                            row.append(T('Aviso: ') + T('Successful assignment to the course, the student is already registered in the system'))

                            ingresado = db.academic_course_assignation.insert(carnet = usr.id, semester = current_period, assignation = check.project, laboratorio = rlaboratorio)
                            db.academic_course_assignation_log.insert(user_name = auth.user.username, roll =  roll_var, 
                                                        operation_log = 'insert', 
                                                        after_carnet = rcarnet, 
                                                        after_course = str(check.project.name), 
                                                        after_year = str(current_period.yearp) ,
                                                        after_semester = str(current_period.period),
                                                        after_laboratory = lab_var,
                                                        id_academic_course_assignation = str(ingresado.id),
                                                        id_period = current_period.id,
                                                        description = T('Inserted from CSV file.'))
                            aviso_users.append(row)
                    else:
                        try:
                            row.remove(T('Aviso: ') + T('The student is already registered in the system'))
                        except:
                            None
                        row.append(T('Error: ') + T('The student is already registered in the system and assigned to the course'))
                        error_users.append(row)
                    continue
        except:
            response.flash = T('File doesn\'t seem properly encoded.')
            return dict(success = False,
                file = False,
                periods = periods,
                current_period = current_period,
                name=name, files=files)
        response.flash = T('Data uploaded')
        return dict(success = success,
                    errors = error_users,
                    avisos = aviso_users,
                    periods = periods,
                    current_period = current_period,
                    name=name, files=files)
    return dict(success = False,
                file = False,
                periods = periods,
                current_period = current_period,
                name=name, files=files)


@auth.requires_login()
@auth.requires(auth.has_membership('Student') or auth.has_membership('Teacher'))
def student_courses():
    #show all assignations of current user
    import cpfecys
    def split_name(project):
        try:
            (nameP, projectSection) = str(project).split('(')
        except:
            nameP = project
        return nameP

    def split_section(project):
        try:
            projectSection = None
            nameS = None
            (nameP, projectSection) = str(project).split('(')
            (nameS,garbage) = str(projectSection).split(')')
        except:
            nameS = '--------'
        return nameS
    year = cpfecys.current_year_period()
    assignation = db((db.user_project.assigned_user==auth.user.id)&\
                        ((db.user_project.period <= year.id) & \
                        ((db.user_project.period + db.user_project.periods) > year.id))).select(db.user_project.ALL).first()
    return dict(assignations = assignation, split_name=split_name, split_section=split_section)

#Mostrar el listado de estudiantes que han sido registrados en el sistema
@auth.requires_login()
@auth.requires(auth.has_membership('Student') or auth.has_membership('Teacher') or auth.has_membership('Super-Administrator'))
def academic():
    if request.vars['search_var'] is None:
        query = db.academic
    else:
        query = db.academic.carnet.like('%'+request.vars['search_var']+'%')

    db.academic.id.writable = False
    db.academic.id.readable = False
    #db.academic.email.writable = False
    db.academic.email.readable = False
    db.academic.id_auth_user.readable = False
    db.academic.id_auth_user.writable = False

           

    if auth.has_membership('Super-Administrator'):
        
        db.academic.email.readable = True        
        #Modal photo
        def get_button_clas(carnet_pa):
            review = db((db.photo_review.user_id == carnet_pa)).select().first()
            if review is None:
                class_button = 'btn btn-info'
            else:
                if review.accepted == True:
                    class_button = 'btn btn-success'
                else:
                    class_button = 'btn btn-danger'
            return class_button

        links = [lambda row: A(T('View photo'),
        _role='button', 
        _class= get_button_clas(row.id_auth_user), 
        _onclick='set_values("'+str(row.id_auth_user)+'");', 
        _title=T('Edit academic information') ,**{"_data-toggle":"modal", "_data-target": "#picModal"})]   
        
        grid = SQLFORM.grid(
        query, oncreate=oncreate_academic,links=links, editable=False, onupdate=onupdate_academic, ondelete=ondelete_academic,  maxtextlength=100,csv=False)
    else:
        grid = SQLFORM.grid(
        query, oncreate=oncreate_academic, onupdate=onupdate_academic, ondelete=ondelete_academic,  maxtextlength=100,csv=False,editable=False,deletable=False,details=False)
    return dict(grid=grid)

def photo():
    return dict(var="")

def oncreate_academic(form):
    import datetime
    cdate = datetime.datetime.now()
    import cpfecys  
    currentyear_period = cpfecys.current_year_period()

    #Search for user roles
    result = db(db.auth_membership.user_id==auth.user.id).select()
    roll_var = ''
    i = 0;
    for a in result:
        if i == 0:
            roll_var = a.group_id.role
            i = i+1
        else:
            roll_var = roll_var + ',' + a.group_id.role  

    db.academic_log.insert(user_name = auth.user.username, 
                                roll =  roll_var, 
                                operation_log = 'insert', 
                                after_carnet = form.vars.carnet, 
                                after_email = form.vars.email, 
                                id_academic = form.vars.id, 
                                id_period = str(currentyear_period.id),
                                description = 'Se agrego registro desde la pagina agregar estudiantes.')

    





     


def onupdate_academic(form):
    import datetime
    import cpfecys  
    currentyear_period = cpfecys.current_year_period()
    cdate = datetime.datetime.now()
    
    #Search for user roles
    result = db(db.auth_membership.user_id==auth.user.id).select()
    roll_var = ''
    i = 0;
    for a in result:
        if i == 0:
            roll_var = a.group_id.role
            i = i+1
        else:
            roll_var = roll_var + ',' + a.group_id.role    

    student_var = db(db.academic_log.id_academic == form.vars.id).select(orderby=db.academic_log.id)
    carnet_var = ''
    email_var = ''
    for a in student_var:
        carnet_var = a.after_carnet
        email_var = a.after_email
    if form.vars.delete_this_record == None:
        db.academic_log.insert(user_name = auth.user.username, 
                                roll =  roll_var, 
                                operation_log = 'update', 
                                before_carnet = carnet_var, 
                                before_email = email_var, 
                                after_carnet = form.vars.carnet, 
                                after_email = form.vars.email, 
                                id_academic = form.vars.id, 
                                id_period = str(currentyear_period.id),
                                description = T('Registration modified from the page from students'))
    else:
        db.academic_log.insert(user_name = auth.user.username, 
                                roll =  str(roll_var), 
                                operation_log = 'delete', 
                                before_carnet = carnet_var, 
                                before_email = email_var, 
                                id_period = str(currentyear_period.id),
                                description = T('Registration is removed from the page students'))


def ondelete_academic(table_involved, id_of_the_deleted_record):
    import datetime
    import cpfecys  
    currentyear_period = cpfecys.current_year_period()

    cdate = datetime.datetime.now()
    student_var = db.academic(id_of_the_deleted_record)    

    #Search for user roles
    result = db(db.auth_membership.user_id==auth.user.id).select()
    roll_var = ''
    i = 0;
    for a in result:
        if i == 0:
            roll_var = a.group_id.role
            i = i+1
        else:
            roll_var = roll_var + ',' + a.group_id.role        

    db.academic_log.insert(user_name = auth.user.username, 
                                roll =  str(roll_var), 
                                operation_log = 'delete', 
                                before_carnet = student_var.carnet, 
                                before_email = student_var.email, 
                                id_period = str(currentyear_period.id),
                                description = T('Registration is removed from the page students'))




