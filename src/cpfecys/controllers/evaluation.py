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
def evaluation_history():
    query=db.evaluation_history
    grid = SQLFORM.smartgrid(query, csv=False,editable=False,deletable=False)
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
def evaluation_list():
    query=db.evaluation
    grid = SQLFORM.grid(query, csv=False)
    return dict(grid=grid)


@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def question_template():
    question_type = request.vars['question_type']
    answer_type = request.vars['answer_type']
    template_id = request.vars['template_id']
    question_var = request.vars['question']
    message_var = None
    if request.vars['operation'] == 'add_question':
        if (question_var is None) or (question_var == ""):
            message_var = T('The question can not be empty.')
        else:
            var_question = db((db.evaluation_question.question == question_var)).select().first()
            if var_question is None:
                db.evaluation_question.insert(question = question_var,
                                            answer_type = answer_type)
                var_question = db((db.evaluation_question.question == question_var)).select().first()
            
            var_question_temp = db((db.evaluation_template_detail.evaluation_template == template_id)&(db.evaluation_template_detail.evaluation_question == var_question.id)&(db.evaluation_template_detail.question_type == question_type)).select().first()
            if var_question_temp is None:
                db.evaluation_template_detail.insert(evaluation_template = template_id,
                                                evaluation_question = var_question.id,
                                                question_type = question_type)
                message_var = T('Question has been added.')
            else:
                message_var = T('The question has already been added.')

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
                eval_h_id = db.evaluation_history.insert(name = add_to_history.vars.hitory_name,
                                            template_name = var_template.name,
                                            evaluation_type_name = var_template.evaluation_type.name,
                                            user_type_evaluated = var_template.evaluation_type.user_type_evaluated,
                                            user_type_evaluator = var_template.evaluation_type.user_type_evaluator)

                
                var_template_detail = db(db.evaluation_template_detail.evaluation_template == template_id).select()
                for v_t_d in var_template_detail:
                    question_h_id = db.question_history.insert(question = v_t_d.evaluation_question.question,
                                            question_type_name = v_t_d.question_type.name,
                                            evaluation_history = eval_h_id)

                    var_answer_type = db(db.answer.answer_type == v_t_d.evaluation_question.answer_type).select()
                    for v_a_t in var_answer_type:
                        db.answer_history.insert(answer = v_a_t.answer,
                                                answer_type_name = v_a_t.answer_type.name,
                                                question_history = question_h_id)
            
                response.flash = T('Evaluation has been added to the evaluation history')
            except:
                response.flash = "Error! " + T('An assessment already exists in the history of evaluations with that name')

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

    