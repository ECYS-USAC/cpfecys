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
def evaluation():
    query=db.evaluation
    import cpfecys
    cperiod = cpfecys.current_year_period()
    db.evaluation.period.default = cperiod.id
    db.evaluation.period.writable = False
    db.evaluation.period.readable = False
    grid = SQLFORM.smartgrid(query, csv=False)
    return dict(grid=grid)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def evaluation_results():
    query=db.evaluation_result
    grid = SQLFORM.smartgrid(query, csv=False)
    return dict(grid=grid)
    
@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def template():
    query=db.evaluation_template
    grid = SQLFORM.smartgrid(query, csv=False)
    return dict(grid=grid)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def evaluation_type():
    query=db.evaluation_type
    grid = SQLFORM.smartgrid(query, csv=False)
    return dict(grid=grid)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def repository_evaluation():
    query=db.repository_evaluation
    grid = SQLFORM.smartgrid(query, csv=False,create=False,editable=False,deletable=False)
    return dict(grid=grid)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def answer_type():
    query=db.answer_type
    grid = SQLFORM.smartgrid(query, csv=False)
    return dict(grid=grid)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def answer():
    query=db.answer
    grid = SQLFORM.grid(query, csv=False)
    return dict(grid=grid)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def evaluation_question():
    query=db.evaluation_question
    grid = SQLFORM.grid(query, csv=False)
    return dict(grid=grid)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def question_type():
    query=db.question_type
    grid = SQLFORM.grid(query, csv=False)
    return dict(grid=grid)

@auth.requires_login()
@auth.requires(auth.has_membership('Student') or auth.has_membership('Teacher') or auth.has_membership('Academic'))
def evaluation_reply():
    import cpfecys
    cperiod = cpfecys.current_year_period()

    project = request.vars['project']
    period = request.vars['period']
    evaluation = request.vars['evaluation']
    evaluated = request.vars['evaluated']

    if db((db.auth_user.id==auth.user.id) & (db.user_project.project==project) & \
        ((db.user_project.period <= period) & ((db.user_project.period + db.user_project.periods) > period))).select().first() is None:
        session.flash  =T('Not authorized')
        redirect(URL('default','index'))

    evaluated = db((db.auth_user.id==evaluated) & (db.user_project.project==project) & \
        ((db.user_project.period <= period) & ((db.user_project.period + db.user_project.periods) > period))).select().first() 
    if evaluated is None:
        session.flash  =T('Not authorized')
        redirect(URL('default','index'))

    var_evaluation = db((db.evaluation.id == evaluation)).select().first()

    if (str(period) != str(cperiod.id)):
        session.flash  =T('Not authorized')
        redirect(URL('default','index'))

    user_role = None
    if auth.has_membership('Student') or auth.has_membership('Teacher'):
        try:
            if db((db.user_project.assigned_user == auth.user.id) & \
                ((db.user_project.period <= period) & ((db.user_project.period + db.user_project.periods) > period))).select().first() is not None:
                if auth.has_membership('Student'):
                    user_role = 2
                else:
                    user_role = 3
        except:
            None
    if auth.has_membership('Academic'):
        try:
            academic_var = db.academic(db.academic.id_auth_user==auth.user.id)
            if db((db.academic_course_assignation.carnet==academic_var.id)&(db.academic_course_assignation.semester==period)).select().first() is not None:
                user_role = 5
        except:
            None

    if var_evaluation.repository_evaluation.user_type_evaluator != user_role:
        session.flash  =T('Not authorized')
        redirect(URL('default','index'))

    var_repository_evaluation = db(db.repository_evaluation.id == var_evaluation.repository_evaluation).select().first()
    question_category = db(db.question_repository.repository_evaluation == var_evaluation.repository_evaluation).select(db.question_repository.question_type_name,distinct=True) 
    
    evaluation_result = db((db.evaluation_result.repository_evaluation == var_evaluation.repository_evaluation) &\
                                (db.evaluation_result.evaluated == evaluated.auth_user.id) & \
                                (db.evaluation_result.period == period) & \
                                (db.evaluation_result.project == project) ).select().first()
                             
    if (evaluation_result is not None) and \
        (db((db.evaluation_auth_user.evaluation_result == evaluation_result.id) &\
        (db.evaluation_auth_user.evaluator == auth.user.id) ).select().first() is not None):
        session.flash  =T('Not authorized')
        redirect(URL('default','index'))

    if (request.args(0) == 'send'):
        
        if evaluation_result is None:
            evaluation_result_id = db.evaluation_result.insert(repository_evaluation = var_evaluation.repository_evaluation,
                                        evaluated = evaluated.auth_user.id,
                                        period = period,
                                        project = project)
        else:
            evaluation_result_id = evaluation_result.id

        evaluation_auth_user = db((db.evaluation_auth_user.evaluation_result == evaluation_result_id) &\
                                (db.evaluation_auth_user.evaluator == auth.user.id) ).select().first()
        if evaluation_auth_user is None:
            db.evaluation_auth_user.insert(evaluation_result = evaluation_result_id,
                                        evaluator = auth.user.id)

        question_query = db((db.question_repository.repository_evaluation == var_evaluation.repository_evaluation)).select()
        for question in question_query:
            answer_query = db((db.repository_answer.question_repository == question.id) ).select()
            if len(answer_query) == 0:
                if (request.vars['group_'+str(question.id)] is not None) & (request.vars['group_'+str(question.id)] != ""):
                    db.evaluation_solve_text.insert(evaluation_result = evaluation_result_id,
                                                question_repository = question.id,
                                                answer = request.vars['group_'+str(question.id)])
            else:
                for answer in answer_query:
                    if answer.exclusive_one_answer ==  True:
                        if request.vars['group_'+str(question.id)] is not None:
                            if str(request.vars['group_'+str(question.id)]) == str(answer.id):
                                evaluation_solve_detail = db((db.evaluation_solve_detail.evaluation_result == evaluation_result_id) &\
                                    (db.evaluation_solve_detail.question_repository == question.id) & \
                                    (db.evaluation_solve_detail.repository_answer == answer.id)).select().first()
                                if evaluation_solve_detail is None:
                                    db.evaluation_solve_detail.insert(evaluation_result = evaluation_result_id,
                                                            question_repository = question.id,
                                                            repository_answer = answer.id,
                                                            total_count = 1)
                                else:
                                    db(db.evaluation_solve_detail.id == evaluation_solve_detail.id).update(total_count = (evaluation_solve_detail.total_count + 1) )

        
        session.flash = T('The evaluation has been sent')            
        redirect(URL('evaluation','evaluation_list', vars=dict(period=period,project=project) ))

    return dict(var_evaluation = var_evaluation,
                var_repository_evaluation = var_repository_evaluation,
                question_category = question_category,
                evaluated = evaluated)
    

@auth.requires_login()
@auth.requires(auth.has_membership('Student') or auth.has_membership('Teacher') or auth.has_membership('Academic'))
def evaluation_list():
    project = request.vars['project']
    period = request.vars['period']
    user = db((db.auth_user.id==auth.user.id) & (db.user_project.project==project) & \
        ((db.user_project.period <= period) & ((db.user_project.period + db.user_project.periods) > period))).select().first()
    
    if user is None:
        session.flash  =T('Not authorized')
        redirect(URL('default','index'))

    from datetime import date
    users_project =  db((db.user_project.project==project) & \
        ((db.user_project.period <= period) & ((db.user_project.period + db.user_project.periods) > period))).select()
    
    user_role = None
    if auth.has_membership('Student') or auth.has_membership('Teacher'):
        try:
            if db((db.user_project.assigned_user == auth.user.id) & \
                ((db.user_project.period <= period) & ((db.user_project.period + db.user_project.periods) > period)) ).select().first() is not None:
                if auth.has_membership('Student'):
                    user_role = 2
                else:
                    user_role = 3
        except:
            None
    if auth.has_membership('Academic'):
        try:
            academic_var = db.academic(db.academic.id_auth_user==auth.user.id)
            if db((db.academic_course_assignation.carnet==academic_var.id)&(db.academic_course_assignation.semester==period)).select().first() is not None:
                user_role = 5
        except:
            None


    evaluations = db(db.evaluation.period == period).select()
    return dict(evaluations=evaluations,
                users_project=users_project,
                project=project,
                user_role=user_role,
                period=period)


@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def question_template():
    question_type = request.vars['question_type']
    answer_type = request.vars['answer_type']
    template_id = request.vars['template_id']
    question_var = request.vars['question']
    answer_obligate = request.vars['answer_obligate']

    if str(answer_obligate).lower() == "true":
        answer_obligate_var = True
    else:
        answer_obligate_var = False

    message_var = None
    if request.vars['operation'] == 'add_question':
        if (question_var is None) or (question_var == ""):
            message_var = T('The question can not be empty.')
        else:
            
            var_answer_type = db((db.answer_type.id == answer_type)).select().first()
            var_answer = db((db.answer.answer_type == answer_type)).select()

            add_question_bol = True
            #if var_answer is not None:
                #if var_answer_type.exclusive_one_answer == True:
                    #total_grade = 0
                    #for answer in var_answer:
                    #    total_grade = total_grade + answer.grade
                    #pass

                    #if total_grade != 100:
                    #    message_var = T("No question was not added because the responses in this type of response does not sum up to 100. The sum of the responses are: ")+str(total_grade)
                    #    add_question_bol = False

            if add_question_bol == True:
                var_question = db((db.evaluation_question.question == question_var)).select().first()
                if var_question is None:
                    db.evaluation_question.insert(question = question_var)
                    var_question = db((db.evaluation_question.question == question_var)).select().first()
                
                var_question_temp = db((db.evaluation_template_detail.evaluation_template == template_id)&(db.evaluation_template_detail.evaluation_question == var_question.id)&(db.evaluation_template_detail.question_type == question_type)).select().first()
                if var_question_temp is None:
                    db.evaluation_template_detail.insert(evaluation_template = template_id,
                                                    evaluation_question = var_question.id,
                                                    question_type = question_type,
                                                    obligatory = answer_obligate_var,
                                                    answer_type = answer_type)
                    message_var = T('Question has been added.')
                else:
                    message_var = "Error!!! " + T('The question has already been added.')

    return dict(question_type = question_type,
                template_id = template_id,
                answer_type = answer_type,
                message_var = message_var)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def evaluation_template_detail():
    template_id = request.vars['template_id']
    if str(template_id) != str('None'):
        list_evaluation_template_detail = db(db.evaluation_template_detail.evaluation_template == template_id).select(db.evaluation_template_detail.question_type,distinct=True) 
        temp_list = []
        for temporal_var in list_evaluation_template_detail:
            if temporal_var is not None:
                temp_list.append(temporal_var.question_type)
        list_evaluation_template_detail = temp_list
    else:
        list_evaluation_template_detail = []
    return dict(list_evaluation_template_detail = list_evaluation_template_detail,
                template_id = template_id)


@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def evaluation_template():
    template_id = request.vars['template_id']
    op_select = request.vars['op_select']
    ev_type = request.vars['ev_type']

    if (ev_type is not None) and (template_id is not None):
        db(db.evaluation_template.id == template_id).update(evaluation_type = ev_type)


    select_form = FORM(INPUT(_name='ev_te_de_id',_type='text'))
   
    if select_form.accepts(request.vars,formname='remove_question'):
        db(db.evaluation_template_detail.id==select_form.vars.ev_te_de_id).delete()
        response.flash = T('Question removed')

    add_to_history = FORM(INPUT(_name='hitory_name',_type='text'))    
    if add_to_history.accepts(request.vars,formname='add_to_history'):
        if add_to_history.vars.hitory_name == "":
            response.flash = "Error! " + T('You must enter a name')
        else:
            try:
                var_template = db(db.evaluation_template.id == template_id).select().first()
                eval_h_id = db.repository_evaluation.insert(name = add_to_history.vars.hitory_name,
                                            template_name = var_template.name,
                                            evaluation_type_name = var_template.evaluation_type.name,
                                            user_type_evaluated = var_template.evaluation_type.user_type_evaluated,
                                            user_type_evaluator = var_template.evaluation_type.user_type_evaluator)

                
                var_template_detail = db(db.evaluation_template_detail.evaluation_template == template_id).select()
                for v_t_d in var_template_detail:
                    question_h_id = db.question_repository.insert(question = v_t_d.evaluation_question.question,
                                            question_type_name = v_t_d.question_type.name,
                                            obligatory = v_t_d.obligatory,
                                            repository_evaluation = eval_h_id)
                    var_answer_type = db(db.answer.answer_type == v_t_d.answer_type).select()
                    for v_a_t in var_answer_type:
                        db.repository_answer.insert(answer = v_a_t.answer,
                                                answer_type_name = v_a_t.answer_type.name,
                                                grade = v_a_t.grade,
                                                exclusive_one_answer = v_a_t.answer_type.exclusive_one_answer,
                                                question_repository = question_h_id)
            
                response.flash = T('Evaluation has been added to the repository evaluation')
            except:
                response.flash = "Error! " + T('An assessment already exists in the repository of evaluations with that name')

    add_question_form = FORM(INPUT(_name='question_id',_type='text'))
   
    if add_question_form.accepts(request.vars,formname='add_question'):
        question_id = request.vars['question_id']
        if question_id is not None:
            var_question_temp = db((db.evaluation_template_detail.evaluation_template == template_id)&(db.evaluation_template_detail.evaluation_question == question_id)).select().first()
            if var_question_temp is None:
                db.evaluation_template_detail.insert(evaluation_template = template_id,
                                                evaluation_question = question_id)
                response.flash = T('Question has been added.')
            else:
                response.flash = T('The question has already been added.')

    evaluation_template_list=db(db.evaluation_template).select()
    db.evaluation_template.date_created.writable = False
    
    form=crud.create(db.evaluation_template, next=URL('evaluation','evaluation_template',vars=dict(op_select = 2) ),message=T("Template has been created"))
    if form.errors:
        op_select = '2'
        response.flash = T('Error')

    form_answer_create = crud.create(db.answer, next=URL('evaluation','evaluation_template',vars=dict(op_select = 3) ),message=T("Answer has been created"))
    if form_answer_create.errors:
        op_select = '3'
        response.flash = T('Error')

    form_answer_type_create = crud.create(db.answer_type, next=URL('evaluation','evaluation_template',vars=dict(op_select = 4) ),message=T("Type answer has been created"))
    if form_answer_type_create.errors:
        op_select = '4'
        response.flash = T('Error')

    form_question_type_create = crud.create(db.question_type, next=URL('evaluation','evaluation_template',vars=dict(op_select = 5) ),message=T("Type question has been created"))
    if form_question_type_create.errors:
        op_select = '5'
        response.flash = T('Error')

    form_evaluation_type_create = crud.create(db.evaluation_type, next=URL('evaluation','evaluation_template',vars=dict(op_select = 6) ),message=T("Type evaluation has been created"))
    if form_evaluation_type_create.errors:
        op_select = '6'
        response.flash = T('Error')
    
    return dict(evaluation_template_list = evaluation_template_list,
                form = form,
                form_answer_create = form_answer_create,
                form_answer_type_create = form_answer_type_create,
                form_question_type_create = form_question_type_create,
                form_evaluation_type_create = form_evaluation_type_create,
                op_select = op_select,
                template_id = template_id)

    