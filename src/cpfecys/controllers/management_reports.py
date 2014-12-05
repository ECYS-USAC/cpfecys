@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def grades_management():
    #****************************************************************************************************************
    #****************************************************************************************************************
    #*****************************************************SEARCH*****************************************************
    #Options to compare fields against the values entered
    def filtered_by(flag):
        fsearch_Option=[]
        fsearch_Option_Temp=[]
        fsearch_Option_Temp.append('=')
        fsearch_Option_Temp.append('=')
        fsearch_Option.append(fsearch_Option_Temp)
        fsearch_Option_Temp=[]
        fsearch_Option_Temp.append('!=')
        fsearch_Option_Temp.append('!=')
        fsearch_Option.append(fsearch_Option_Temp)
        fsearch_Option_Temp=[]
        fsearch_Option_Temp.append('&lt;')
        fsearch_Option_Temp.append('<')
        fsearch_Option.append(fsearch_Option_Temp)
        fsearch_Option_Temp=[]
        fsearch_Option_Temp.append('&gt;')
        fsearch_Option_Temp.append('>')
        fsearch_Option.append(fsearch_Option_Temp)
        fsearch_Option_Temp=[]
        fsearch_Option_Temp.append('&lt;=')
        fsearch_Option_Temp.append('<=')
        fsearch_Option.append(fsearch_Option_Temp)
        fsearch_Option_Temp=[]
        fsearch_Option_Temp.append('&gt;=')
        fsearch_Option_Temp.append('>=')
        fsearch_Option.append(fsearch_Option_Temp)
        if flag==True:
            fsearch_Option_Temp=[]
            fsearch_Option_Temp.append('starts with')
            fsearch_Option_Temp.append('inicia cón')
            fsearch_Option.append(fsearch_Option_Temp)
            fsearch_Option_Temp=[]
            fsearch_Option_Temp.append('contains')
            fsearch_Option_Temp.append('contiene')
            fsearch_Option.append(fsearch_Option_Temp)
            fsearch_Option_Temp=[]
            fsearch_Option_Temp.append('in')
            fsearch_Option_Temp.append('en')
            fsearch_Option.append(fsearch_Option_Temp)
            fsearch_Option_Temp=[]
            fsearch_Option_Temp.append('not in')
            fsearch_Option_Temp.append('no esta en')
            fsearch_Option.append(fsearch_Option_Temp)
        return fsearch_Option
    
    #ALL INFORMATION OF SEARCH
    fsearch = []
    #
    fsearch_Temp=[]
    fsearch_Temp.append('user_name')
    fsearch_Temp.append('Usuario Registro')
    fsearch_Temp.append(True)
    fsearch_Values=[]
    fsearch_Values.append(1)
    fsearch_Temp.append(fsearch_Values)
    fsearch.append(fsearch_Temp)

    fsearch_Temp=[]
    fsearch_Temp.append('roll')
    fsearch_Temp.append('Rol')
    fsearch_Temp.append(True)
    fsearch_Values=[]
    fsearch_Values.append(1)
    fsearch_Temp.append(fsearch_Values)
    fsearch.append(fsearch_Temp)

    fsearch_Temp=[]
    fsearch_Temp.append('operation_log')
    fsearch_Temp.append('Operación Registrada')
    fsearch_Temp.append(True)
    fsearch_Values=[]
    fsearch_Values.append(1)
    fsearch_Temp.append(fsearch_Values)
    fsearch.append(fsearch_Temp)

    fsearch_Temp=[]
    fsearch_Temp.append('academic_assignation_id')
    fsearch_Temp.append('ID Asignación Estudiante')
    fsearch_Temp.append(True)
    fsearch_Values=[]
    fsearch_Values.append(1)
    fsearch_Temp.append(fsearch_Values)
    fsearch.append(fsearch_Temp)

    fsearch_Temp=[]
    fsearch_Temp.append('academic')
    fsearch_Temp.append('Estudiante')
    fsearch_Temp.append(True)
    fsearch_Values=[]
    fsearch_Values.append(1)
    fsearch_Temp.append(fsearch_Values)
    fsearch.append(fsearch_Temp)

    fsearch_Temp=[]
    fsearch_Temp.append('activity')
    fsearch_Temp.append('Actividad')
    fsearch_Temp.append(True)
    fsearch_Values=[]
    fsearch_Values.append(1)
    fsearch_Temp.append(fsearch_Values)
    fsearch.append(fsearch_Temp)

    fsearch_Temp=[]
    fsearch_Temp.append('activity_id')
    fsearch_Temp.append('ID Actividad')
    fsearch_Temp.append(True)
    fsearch_Values=[]
    fsearch_Values.append(1)
    fsearch_Temp.append(fsearch_Values)
    fsearch.append(fsearch_Temp)

    fsearch_Temp=[]
    fsearch_Temp.append('category')
    fsearch_Temp.append('Categoria')
    fsearch_Temp.append(True)
    fsearch_Values=[]
    fsearch_Values.append(1)
    fsearch_Temp.append(fsearch_Values)
    fsearch.append(fsearch_Temp)

    fsearch_Temp=[]
    fsearch_Temp.append('project')
    fsearch_Temp.append('Curso')
    fsearch_Temp.append(True)
    fsearch_Values=[]
    fsearch_Values.append(1)
    fsearch_Temp.append(fsearch_Values)
    fsearch.append(fsearch_Temp)

    fsearch_Temp=[]
    fsearch_Temp.append('yearp')
    fsearch_Temp.append('Año')
    fsearch_Temp.append(True)
    fsearch_Values=[]
    fsearch_Values.append(1)
    fsearch_Temp.append(fsearch_Values)
    fsearch.append(fsearch_Temp)

    fsearch_Temp=[]
    fsearch_Temp.append('period')
    fsearch_Temp.append('Periodo')
    fsearch_Temp.append(True)
    fsearch_Values=[]
    fsearch_Values.append(1)
    fsearch_Temp.append(fsearch_Values)
    fsearch.append(fsearch_Temp)

    fsearch_Temp=[]
    fsearch_Temp.append('before_grade')
    fsearch_Temp.append('Nota Historica')
    fsearch_Temp.append(False)
    fsearch_Values=[]
    fsearch_Values.append(1)
    fsearch_Temp.append(fsearch_Values)
    fsearch.append(fsearch_Temp)

    fsearch_Temp=[]
    fsearch_Temp.append('after_grade')
    fsearch_Temp.append('Nota Oficial')
    fsearch_Temp.append(False)
    fsearch_Values=[]
    fsearch_Values.append(1)
    fsearch_Temp.append(fsearch_Values)
    fsearch.append(fsearch_Temp)

    fsearch_Temp=[]
    fsearch_Temp.append('description')
    fsearch_Temp.append('Descripción')
    fsearch_Temp.append(True)
    fsearch_Values=[]
    fsearch_Values.append(1)
    fsearch_Temp.append(fsearch_Values)
    fsearch.append(fsearch_Temp)

    fsearch_Temp=[]
    fsearch_Temp.append('date_log')
    fsearch_Temp.append('Fecha')
    fsearch_Temp.append(False)
    fsearch_Values=[]
    fsearch_Values.append(2)
    fsearch_Temp.append(fsearch_Values)
    fsearch.append(fsearch_Temp)
    #****************************************************************************************************************
    #****************************************************************************************************************
    #*****************************************************SEARCH*****************************************************

    personal_query = ''


    return dict(fsearch=fsearch, filtered_by=filtered_by, personal_query=personal_query)
