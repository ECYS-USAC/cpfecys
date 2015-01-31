#***********************************************************************************************************************
#******************************************************PHASE 2 DTT******************************************************
import math
def metric_statistics(actTempo, recovery, dataIncoming):
    activity=[]
    if dataIncoming is None:
        if recovery==1 or recovery==2:
            if recovery==1:
                #Description of Activity
                description = 'Nombre: "PRIMERA RETRASADA"'
                tempData = db((db.course_first_recovery_test.semester==obtainPeriodReport(actTempo).id)&(db.course_first_recovery_test.project==actTempo.assignation.project)).select(db.course_first_recovery_test.grade, orderby=db.course_first_recovery_test.grade)
            else:
                #Description of Activity
                description = 'Nombre: "SEGUNDA RETRASADA"'
                tempData = db((db.course_second_recovery_test.semester==obtainPeriodReport(actTempo).id)&(db.course_second_recovery_test.project==actTempo.assignation.project)).select(db.course_second_recovery_test.grade, orderby=db.course_second_recovery_test.grade)
            data=[]
            Sum_Data=float(0)
            Sum_Data_Squared=float(0)
            totalReprobate=0
            totalApproved=0
            for d1 in tempData:
                if d1.grade is None:
                    data.append(float(0))
                    totalReprobate+=1
                else:
                    data.append(float(d1.grade))
                    Sum_Data+=float(d1.grade)
                    Sum_Data_Squared+=(float(d1.grade)*float(d1.grade))
                    if float(d1.grade)>=float(61):
                        totalApproved+=1
                    else:
                        totalReprobate+=1
        else:
            #Description of Activity
            description = 'Nombre: "'+actTempo.name+'" Descripción: "'+actTempo.description+'"'
            
            #*********************************************Statistics Activity*********************************************
            #Get the data
            tempData = db(db.grades.activity == actTempo.id).select(db.grades.grade, orderby=db.grades.grade)
            #tempData=[40,60,75,75,75,75,80,80,85,85,85,85,85,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100]
            data=[]
            Sum_Data=float(0)
            Sum_Data_Squared=float(0)
            totalReprobate=0
            totalApproved=0
            for d1 in tempData:
                if d1.grade is None:
                    data.append(float(0))
                    totalReprobate+=1
                else:
                    data.append(float(d1.grade))
                    Sum_Data+=float(d1.grade)
                    Sum_Data_Squared+=(float(d1.grade)*float(d1.grade))
                    if float(d1.grade)>=float(61):
                        totalApproved+=1
                    else:
                        totalReprobate+=1
    else:
        data=[]
        Sum_Data=float(0)
        Sum_Data_Squared=float(0)
        totalReprobate=0
        totalApproved=0
        for d1 in dataIncoming:
            if d1 is None:
                data.append(float(0))
                totalReprobate+=1
            else:
                data.append(float(d1))
                Sum_Data+=float(d1)
                Sum_Data_Squared+=(float(d1)*float(d1))
                if float(d1)>=float(61):
                    totalApproved+=1
                else:
                    totalReprobate+=1
    


    #*********************************************
    #Total Students
    totalStudents = int(len(data))
    


    #*********************************************
    #Mean
    mean = float(Sum_Data/totalStudents)
    #Variance
    try:
        variance=((Sum_Data_Squared/totalStudents)-(mean*mean))
    except:
        variance=float(0)
    #Standard Deviation
    try:
        standard_deviation=math.sqrt(variance)
    except:
        standard_deviation=float(0)
    #Standard Error
    try:
        standard_error=standard_deviation/math.sqrt(totalStudents)
    except:
        standard_error=float(0)
    #Kurtosis
    try:
        #Numerator
        numerator=0
        for i in data:
            numerator+=(i-mean)*(i-mean)*(i-mean)*(i-mean)
        numerator=numerator*totalStudents
        #Denominator
        denominator=0
        for i in data:
            denominator+=(i-mean)*(i-mean)
        denominator=denominator*denominator
        #Fraction
        kurtosis=(numerator/denominator)-3
    except:
        kurtosis=float(0)
    #Minimum
    minimum=float(data[0])
    if totalStudents==1:
        #Maximum
        maximum=float(data[0])
        #Rank
        rank=float(0)
        #Median
        median=float(Sum_Data)
        #Mode
        mode=float(Sum_Data)
    else:
        #Maximum
        maximum=float(data[totalStudents-1])
        #Rank
        rank=float(data[totalStudents-1] - data[0])
        #Median
        if totalStudents%2 == 1:
            median = float(data[totalStudents//2])
        else:
            i = totalStudents//2
            median = float((data[i - 1] + data[i])/2)
        #Mode
        try:
            table = collections.Counter(iter(data)).most_common()
            maxfreq = table[0][1]
            for i in range(1, len(table)):
                if table[i][1] != maxfreq:
                    table = table[:i]
                    break
            mode=float(table[0][0])
        except:
            mode=minimum
    #Skewness
    try:
        skewness=float((3*(mean-median))/standard_error)
    except:
        skewness=float(0)
    


    #**********************************************
    #Metric Type
    if dataIncoming is None:
        if recovery==1 or recovery==2:
            if recovery==1:
                metricType=db(db.metrics_type.name=='PRIMERA RETRASADA').select(db.metrics_type.id).first()[db.metrics_type.id]
            else:
                metricType=db(db.metrics_type.name=='SEGUNDA RETRASADA').select(db.metrics_type.id).first()[db.metrics_type.id]
        else:
            category = actTempo.course_activity_category.category.category.upper()
            metricType=None
            if category=='TAREAS':
                metricType=db(db.metrics_type.name=='TAREA').select(db.metrics_type.id).first()[db.metrics_type.id]
            elif category=='EXAMEN CORTO':
                metricType=db(db.metrics_type.name=='EXAMEN CORTO').select(db.metrics_type.id).first()[db.metrics_type.id]
            elif category=='HOJAS DE TRABAJO':
                metricType=db(db.metrics_type.name=='HOJA DE TRABAJO').select(db.metrics_type.id).first()[db.metrics_type.id]
            elif category=='PARCIALES':
                metricType=db(db.metrics_type.name==actTempo.name.upper()).select(db.metrics_type.id).first()[db.metrics_type.id]
            elif category=='EXAMEN FINAL':
                metricType=db(db.metrics_type.name=='EXAMEN FINAL').select(db.metrics_type.id).first()[db.metrics_type.id]
            elif category=='PRACTICAS':
                metricType=db(db.metrics_type.name=='PRACTICA').select(db.metrics_type.id).first()[db.metrics_type.id]
            elif category=='PROYECTOS':
                name_search = actTempo.name.upper()
                if "FASE FINAL" in name_search:
                    metricType=db(db.metrics_type.name=='FASE FINAL').select(db.metrics_type.id).first()[db.metrics_type.id]
                elif "FASE" in name_search:
                    metricType=db(db.metrics_type.name=='FASE DE PROYECTO').select(db.metrics_type.id).first()[db.metrics_type.id]
                elif "PRIMER PROYECTO" in name_search or "1ER PROYECTO" in name_search  or "1ER. PROYECTO" in name_search or "PROYECTO1" in name_search or "PROYECTO 1" in name_search or "PROYECTO NO.1" in name_search or "PROYECTO NO1" in name_search   or "PROYECTO NUMERO 1" in name_search or "PROYECTO NUMERO1" in name_search or "PROYECTO #1" in name_search or "PROYECTO#1" in name_search:
                    metricType=db(db.metrics_type.name=='PROYECTO 1').select(db.metrics_type.id).first()[db.metrics_type.id]
                elif "SEGUNDO PROYECTO" in name_search or "1DO PROYECTO" in name_search  or "2DO. PROYECTO" in name_search or "PROYECTO2" in name_search or "PROYECTO 2" in name_search or "PROYECTO NO.2" in name_search or "PROYECTO NO2" in name_search   or "PROYECTO NUMERO 2" in name_search or "PROYECTO NUMERO2" in name_search or "PROYECTO #2" in name_search or "PROYECTO#2" in name_search:
                    metricType=db(db.metrics_type.name=='PROYECTO 2').select(db.metrics_type.id).first()[db.metrics_type.id]
            if metricType is None:
                metricType=db(db.metrics_type.name=='OTRA ACTIVIDAD').select(db.metrics_type.id).first()[db.metrics_type.id]



    #******************************************************
    #Fill the activity
    if dataIncoming is None:
        if recovery==1 or recovery==2:
            import datetime
            activity.append(datetime.datetime.now().date())
        else:
            activity.append(actTempo.date_start)
        activity.append(description)
    activity.append(mean)
    activity.append(standard_error)
    activity.append(median)
    activity.append(mode)
    activity.append(standard_deviation)
    activity.append(variance)
    activity.append(kurtosis)
    activity.append(skewness)
    activity.append(rank)
    activity.append(minimum)
    activity.append(maximum)
    #Total Students
    activity.append(totalStudents)
    #Total Reprobate
    activity.append(totalReprobate)
    #Total Approved
    activity.append(totalApproved)
    #Metric Type
    if dataIncoming is None:
        activity.append(int(metricType))
        if recovery==1:
            activity.append(-1)
        elif recovery==2:
            activity.append(-2)
        else:
            activity.append(actTempo.id)

    #Activity to return
    return activity

def final_metric(cperiod, report):
    final_stats_vec=[]

    #***********************************************************************************************
    #********************************Attendance and dropout in exams********************************
    #students_minutes
    try:
        final_stats_vec.append(int(db((db.academic_course_assignation.semester==cperiod.id)&(db.academic_course_assignation.assignation==report.assignation.project)).count()))
    except:
        final_stats_vec.append(int(0))

    #students_partial
    try:
        Partials = db(db.activity_category.category=='Parciales').select().first()
        catPartials = db((db.course_activity_category.category==Partials.id)&(db.course_activity_category.semester==cperiod.id)&(db.course_activity_category.assignation==report.assignation.project)&(db.course_activity_category.laboratory==False)).select().first()
        Partials = db((db.course_activity.course_activity_category==catPartials.id)&(db.course_activity.semester==cperiod.id)&(db.course_activity.assignation==report.assignation.project)&(db.course_activity.laboratory==False)).select(db.course_activity.id)
        final_stats_vec.append(int(db(db.grades.activity.belongs(Partials)).count()/db((db.course_activity.course_activity_category==catPartials.id)&(db.course_activity.semester==cperiod.id)&(db.course_activity.assignation==report.assignation.project)&(db.course_activity.laboratory==False)).count()))
    except:
        final_stats_vec.append(int(0))

    #students_final
    try:
        Final = db(db.activity_category.category=='Examen Final').select().first()
        catFinal = db((db.course_activity_category.category==Final.id)&(db.course_activity_category.semester==cperiod.id)&(db.course_activity_category.assignation==report.assignation.project)&(db.course_activity_category.laboratory==False)).select().first()
        Final = db((db.course_activity.course_activity_category==catFinal.id)&(db.course_activity.semester==cperiod.id)&(db.course_activity.assignation==report.assignation.project)&(db.course_activity.laboratory==False)).select(db.course_activity.id)
        final_stats_vec.append(int(db(db.grades.activity.belongs(Final)).count()))
    except:
        final_stats_vec.append(int(0))

    #students_first_recovery
    try:
        final_stats_vec.append(int(db((db.course_first_recovery_test.semester==cperiod.id)&(db.course_first_recovery_test.project==report.assignation.project)).count()))
    except:
        final_stats_vec.append(int(0))

    #students_second_recovery
    try:
        final_stats_vec.append(int(db((db.course_second_recovery_test.semester==cperiod.id)&(db.course_second_recovery_test.project==report.assignation.project)).count()))
    except:
        final_stats_vec.append(int(0))


    #Students
    students = db((db.academic_course_assignation.semester == cperiod.id) & (db.academic_course_assignation.assignation==report.assignation.project)).select()


    #***********************************************************************************************
    #********************************FINAL RESULTS OF LABORATORY************************************
    #students_in_lab
    existLab=False
    totalClass=float(0)
    totalLab=float(0)
    totalFinalLab=float(0)
    totalW=float(0)
    try:
        CourseCategory = db((db.course_activity_category.semester==cperiod.id)&(db.course_activity_category.assignation==report.assignation.project)&(db.course_activity_category.laboratory==False)).select()
        catCourseTemp=None
        catVecCourseTemp=[]
        CourseActivities = []
        for categoryC in CourseCategory:
            totalW=totalW+float(categoryC.grade)
            if categoryC.category.category=="Laboratorio":
                existLab=True
                totalLab=float(categoryC.grade)
                catVecCourseTemp.append(categoryC)
            elif categoryC.category.category=="Examen Final":
                var_final_grade = categoryC.grade
                catCourseTemp=categoryC
            else:
                catVecCourseTemp.append(categoryC)
                CourseActivities.append(db((db.course_activity.semester==cperiod.id)&(db.course_activity.assignation==report.assignation.project)&(db.course_activity.laboratory==False)&(db.course_activity.course_activity_category==categoryC.id)).select())
        if catCourseTemp != None:
            catVecCourseTemp.append(catCourseTemp)
            CourseActivities.append(db((db.course_activity.semester==cperiod.id)&(db.course_activity.assignation==report.assignation.project)&(db.course_activity.laboratory==False)&(db.course_activity.course_activity_category==catCourseTemp.id)).select())
        CourseCategory=catVecCourseTemp
        totalClass=totalW


        totalW=float(0)
        LabCategory=None
        catLabTemp=None
        catVecLabTemp=[]
        LabActivities = None
        validateLaboratory=None
        LabCategory = db((db.course_activity_category.semester==cperiod.id)&(db.course_activity_category.assignation==report.assignation.project)&(db.course_activity_category.laboratory==True)).select()
        if LabCategory.first() is not None:
            validateLaboratory = db((db.validate_laboratory.semester==cperiod.id)&(db.validate_laboratory.project==report.assignation.project)).select()
            LabCategory = db((db.course_activity_category.semester==cperiod.id)&(db.course_activity_category.assignation==report.assignation.project)&(db.course_activity_category.laboratory==True)).select()
            LabActivities = []
            for categoryL in LabCategory:
                if categoryL.category.category=="Examen Final":
                    totalW=totalW+float(categoryL.grade)
                    catLabTemp=categoryL
                else:
                    catVecLabTemp.append(categoryL)
                    totalW=totalW+float(categoryL.grade)
                    LabActivities.append(db((db.course_activity.semester==cperiod.id)&(db.course_activity.assignation==report.assignation.project)&(db.course_activity.laboratory==True)&(db.course_activity.course_activity_category==categoryL.id)).select())
            if catLabTemp != None:
                catVecLabTemp.append(catLabTemp)
                LabActivities.append(db((db.course_activity.semester==cperiod.id)&(db.course_activity.assignation==report.assignation.project)&(db.course_activity.laboratory==True)&(db.course_activity.course_activity_category==catLabTemp.id)).select())
            LabCategory=catVecLabTemp
            totalFinalLab=totalW


        requirement = db((db.course_requirement.semester==cperiod.id)&(db.course_requirement.project==report.assignation.project)).select().first()
    except:
        totalClass=float(0)
        totalFinalLab=float(0)

    #COMPUTING LABORATORY NOTES
    students_in_lab=[]
    temp_students_in_lab=[]
    approved=0
    reprobate=0
    sum_laboratory_grades=0
    try:
        if totalFinalLab==float(100):
            for t1 in students:
                tempData=[]
                totalCategory=float(0)
                isValidate=False
                #<!--Revalidation of laboratory-->
                for validate in validateLaboratory:
                    if validate.carnet==t1.carnet:
                        isValidate=True
                        tempData.append(t1.carnet.carnet)
                        tempData.append(int(round(validate.grade,0)))
                        students_in_lab.append(tempData)


                #<!--Doesnt has a revalidation-->
                if isValidate==False:
                    #<!--Position in the vector of activities-->
                    posVCC_Lab=0
                    #<!--Vars to the control of grade of the student-->
                    totalCategory_Lab=float(0)
                    totalActivities_Lab=0
                    totalCarry_Lab=float(0)

                    #<!--****************************************FILL THE GRADES OF THE STUDENT****************************************-->
                    #<!--LAB ACTIVITIES-->
                    for category_Lab in LabCategory:
                        totalCategory_Lab=float(0)
                        totalActivities_Lab=0
                        for c_Lab in LabActivities[posVCC_Lab]:
                            studentGrade = db((db.grades.activity==c_Lab.id)&(db.grades.academic_assignation==t1.id)).select().first()
                            if studentGrade is None or studentGrade.grade is None:
                                totalCategory_Lab=totalCategory_Lab+float(0)
                            else:
                                if category_Lab.specific_grade==True:
                                    totalCategory_Lab=totalCategory_Lab+float((studentGrade.grade*c_Lab.grade)/100)
                                else:
                                    totalCategory_Lab=totalCategory_Lab+float(studentGrade.grade)
                            totalActivities_Lab=totalActivities_Lab+1
                        

                        if category_Lab.specific_grade==False:
                            if totalActivities_Lab==0:
                                totalActivities_Lab=1
                            totalActivities_Lab=totalActivities_Lab*100
                            totalCategory_Lab=float((totalCategory_Lab*float(category_Lab.grade))/float(totalActivities_Lab))
                        totalCarry_Lab=totalCarry_Lab+totalCategory_Lab
                        posVCC_Lab=posVCC_Lab+1
                    tempData.append(t1.carnet.carnet)
                    tempData.append(int(round(totalCarry_Lab,0)))
                    students_in_lab.append(tempData)
                    temp_students_in_lab.append(tempData)
                    sum_laboratory_grades+=int(round(totalCarry_Lab,0))
                    if int(round(totalCarry_Lab,0))<61:
                        reprobate+=1
                    else:
                        approved+=1

            #APPROVED
            final_stats_vec.append(approved)
            #FAILED
            final_stats_vec.append(reprobate)
            #MEAN
            final_stats_vec.append(float(sum_laboratory_grades)/float(len(temp_students_in_lab)))
            #AVERAGE
            final_stats_vec.append(float((float(approved)/float(len(temp_students_in_lab)))*float(100)))
        else:
            #APPROVED
            final_stats_vec.append(int(0))
            #FAILED
            final_stats_vec.append(int(0))
            #MEAN
            final_stats_vec.append(int(0))
            #AVERAGE
            final_stats_vec.append(int(0))
    except:
        countFail=int(len(final_stats_vec))
        for countFail in range(9):
            final_stats_vec.append(int(0))
    

    #Class Final Results
    dataFinalClass=[]
    try:
        if totalClass==100:
            for t1 in students:
                posStudent=0
                posVCC=0
                totalCategory=float(0)
                totalActivities=0
                totalCarry=float(0)
                for category in CourseCategory:
                    if category.category.category!="Laboratorio" and category.category.category!="Examen Final":
                        totalCategory=float(0)
                        totalActivities=0
                        for c in CourseActivities[posVCC]:
                            studentGrade = db((db.grades.activity==c.id)&(db.grades.academic_assignation==t1.id)).select().first()
                            if studentGrade is None or studentGrade.grade is None:
                                totalCategory=totalCategory+float(0)
                            else:
                                if category.specific_grade==True:
                                    totalCategory=totalCategory+float((studentGrade.grade*c.grade)/100)
                                else:
                                    totalCategory=totalCategory+float(studentGrade.grade)
                            totalActivities=totalActivities+1

                        if category.specific_grade==True:
                            None
                        else:
                            if totalActivities==0:
                                totalActivities=1
                            totalActivities=totalActivities*100
                            totalCategory=float((totalCategory*float(category.grade))/float(totalActivities))
                        totalCarry=totalCarry+totalCategory
                        posVCC=posVCC+1
                    elif category.category.category=="Examen Final":
                        totalCarry=int(round(totalCarry,0))
                        totalCategory=float(0)
                        totalActivities=0
                        for c in CourseActivities[posVCC]:
                            studentGrade = db((db.grades.activity==c.id)&(db.grades.academic_assignation==t1.id)).select().first()
                            if studentGrade is None or studentGrade.grade is None:
                                totalCategory=totalCategory+float(0)
                            else:
                                if category.specific_grade==True:
                                    totalCategory=totalCategory+float((studentGrade.grade*c.grade)/100)
                                else:
                                    totalCategory=totalCategory+float(studentGrade.grade)
                            totalActivities=totalActivities+1

                        if category.specific_grade==True:
                            None
                        else:
                            if totalActivities==0:
                                totalActivities=1
                            totalActivities=totalActivities*100
                            totalCategory=float((totalCategory*float(category.grade))/float(totalActivities))
                        totalCategory=int(round(totalCategory,0))
                        totalCarry=totalCarry+totalCategory
                        posVCC=posVCC+1
                
                #Make
                if existLab==True:
                    totalCategory=float((int(students_in_lab[posStudent][1])*totalLab)/100)
                    totalCarry=totalCarry+totalCategory

                if requirement is not None:
                    if db((db.course_requirement_student.carnet==t1.carnet)&(db.course_requirement_student.requirement==requirement.id)).select().first() is not None:
                        dataFinalClass.append(int(round(totalCarry,0)))
                    else:
                        dataFinalClass.append(int(0))
                else:
                    dataFinalClass.append(int(round(totalCarry,0)))
                posStudent+=1

            #Calculate metric_statistics
            dataFinalClass=sorted(dataFinalClass)
            dataFinalClass = metric_statistics(None, 0, dataFinalClass)
            for posFinal in dataFinalClass:
                final_stats_vec.append(posFinal)
        else:
            countFailFinal=int(len(final_stats_vec))
            for countFailFinal in range(23):
                final_stats_vec.append(int(0))
    except:
        countFailFinal=int(len(final_stats_vec))
        for countFailFinal in range(23):
                final_stats_vec.append(int(0))

    return final_stats_vec


def obtainPeriodReport(report):
    #Get the minimum and maximum date of the report
    tmp_period=1
    tmp_year=report.report_restriction.start_date.year
    if report.report_restriction.start_date.month >= 6:
        tmp_period=2
    return db((db.period_year.yearp==tmp_year)&(db.period_year.period==tmp_period)).select().first()
#***********************************************************************************************************************
#******************************************************PHASE 2 DTT******************************************************


# coding: utf8
# intente algo como
@auth.requires_login()
@auth.requires_membership('Teacher')
def index():
    return dict()

@auth.requires_login()
@auth.requires_membership('Teacher')
def todo_reports():
    #show the reports that haven't already been checked based on current assignations of the teacher
    data = db((db.report.status == db.report_status.id)&
       ((db.report_status.name == 'Grading')|(db.report_status.name == 'EnabledForTeacher'))&
       (db.report.assignation == db.user_project.id)&
       (db.user_project.assigned_user == auth.user.id)).select()
    return dict(my_projects = db((db.user_project.assigned_user == auth.user.id)&
                                 (db.project.id == db.user_project.project)).select())

@auth.requires_login()
@auth.requires_membership('Teacher')
def final_practice():
    def assignation_range(assignation):
        cperiod = cpfecys.current_year_period()
        ends = assignation.period.id + assignation.periods
        period_range = db((db.period_year.id >= assignation.period.id)&
            (db.period_year.id < ends)&
            (db.period_year.id <= cperiod.id)).select()
        return period_range

    def available_item_restriction(period_year, user_project):
        return db(((db.item_restriction.period==period_year) |
                    (db.item_restriction.permanent==True))&
                (db.item_restriction.is_enabled==True)&
                (db.item_restriction.hidden_from_teacher!=True)&
                (db.item_restriction_area.item_restriction==\
                    db.item_restriction.id)&
                (db.item_restriction_area.area_level==\
                    user_project.project.area_level.id))

    def restriction_project_exception(item_restriction_id, project_id):
        return db((db.item_restriction_exception.project== \
                    project_id)&
                    (db.item_restriction_exception.item_restriction \
                        ==item_restriction_id))

    def items_instance(item_restriction, assignation):
        return db((db.item.item_restriction==item_restriction.id)&
                    (db.item.assignation==assignation.id)&
                    (db.item.is_active==True))

    def get_items(period, assignation):
        restrictions = db((db.item_restriction.id== \
            db.item_restriction_exception.item_restriction)& \
            (db.item_restriction_exception.project==final_practice.project.id) \
            ).select(db.item_restriction.ALL)
        items = db((db.item.created==period.id)&
            (db.item.assignation==assignation.id)&
            (~db.item.item_restriction.belongs(restrictions)))
        return items.select(db.item.ALL)

    assignation = request.vars['assignation']
    if not assignation: redirect(URL('courses'))
    assignation = db(db.user_project.id==assignation).select().first()
    final_practice = db((db.user_project.id == assignation)&
                        (db.user_project.assigned_user == db.auth_user.id)&
                        (db.user_project.project == db.project.id)&
                        (db.project.area_level == db.area_level.id)&
                        (db.user_project.period == db.period_year.id)).select()
    if not final_practice: redirect(URL('courses'))
    final_practice = final_practice.first()
    #TODO evaluate if available_periods is really necessary
    available_periods = db((db.period_year.id >= \
                            final_practice.user_project.period)&
                        (db.period_year.id < \
                            (final_practice.user_project.period + \
                            final_practice.user_project.periods))).select()

    items = db((db.item.created==cpfecys.current_year_period())& \
                        (db.item.assignation==final_practice.user_project.id) \
                        ).select()
    total_items = db((db.item.created==cpfecys.current_year_period())).select()

    def compare_last_day(last_day):
        from datetime import datetime
        cdate = datetime.now()
        last_day = datetime.strptime(str(last_day), "%Y-%m-%d")
        if cdate > last_day:
            return True
        return False

    def get_current_reports(period):
        from datetime import datetime
        import cpfecys
        cperiod = cpfecys.current_year_period()
        year = str(cperiod.yearp)
        if period.period == 1:
            start = datetime.strptime(year + '-01-01', "%Y-%m-%d")
            end = datetime.strptime(year + '-06-01', "%Y-%m-%d")
        else:
            start = datetime.strptime(year + '-06-01', "%Y-%m-%d")
            end = datetime.strptime(year + '-12-31', "%Y-%m-%d")

        reports = db((db.report.assignation == final_practice.user_project.id)&
                        (db.report.status.name!='Grading')&
                        (db.report.created >= start)&
                        (db.report.created <= end))
        avg = reports.select((db.report.score.sum()/db.report.score.count()).\
                        with_alias('avg')).first()['avg'] or 0
        reports = reports.select(), avg
        return reports
    return dict(final_practice=final_practice,
                available_periods=available_periods,
                items=items,
                total_items=total_items,
                get_items=get_items,
                assignation_range=assignation_range,
                available_item_restriction=available_item_restriction,
                assignation=assignation,
                restriction_project_exception=restriction_project_exception,
                items_instance=items_instance,
                get_current_reports=get_current_reports,
                compare_last_day=compare_last_day)

@cache.action()
@auth.requires_login()
@auth.requires_membership('Teacher')
def download():
    item = db(db.item.uploaded_file==request.args[0]).select().first()
    project =  item.assignation.project
    t_assignation = db((db.user_project.project==project.id)&
        (db.user_project.assigned_user==auth.user.id))
    if item != None and t_assignation != None:
        return response.download(request, db)
    else:
        session.flash = T('Access Forbidden')
        redirect(URL('default', 'index'))

@auth.requires_login()
@auth.requires_membership('Teacher')
def report():
    import datetime
    cdate = datetime.datetime.now()
    report = request.vars['report']
    report = db.report(db.report.id == report)
    import cpfecys
    parameters = cpfecys.get_custom_parameters()
    valid = not(report is None)
    next_date = None
    if valid:
        valid = cpfecys.teacher_validation_report_access(report.id)

    if (request.args(0) == 'view'):
        if valid:
            if report.score_date:
                next_date = report.score_date + datetime.timedelta(
                    days=parameters.rescore_max_days)
            response.view = 'teacher/report_view.html'
            assignation_reports = db(db.report.assignation== \
                report.assignation).select()
            teacher = db(db.auth_user.id==auth.user.id).select().first()


            #***********************************************************************************************************************
            #******************************************************PHASE 2 DTT******************************************************
            activities_WM=None
            activities_M=None
            activities_F=None
            if report.assignation.project.area_level.name=='DTT Tutor Académico' and (report.status.name=='Draft' or report.status.name=='Recheck'):
                #Get the minimum and maximum date of the report
                cperiod = obtainPeriodReport(report)
                parameters_period = db(db.student_control_period.period_name==(T(cperiod.period.name)+' '+str(cperiod.yearp))).select().first()
                endDateActivity=None
                initSemester=None
                if cperiod.period == 1:
                    initSemester = datetime.datetime.strptime(str(cperiod.yearp) + '-' + '01-01', "%Y-%m-%d")
                    if report.report_restriction.is_final==False:
                        activities_F=[]
                        nameReportSplit = report.report_restriction.name.upper()
                        nameReportSplit = nameReportSplit.split(' ')
                        for word in nameReportSplit:
                            if word=='ENERO':
                                endDateActivity = datetime.datetime.strptime(str(cperiod.yearp) + '-' + '02-01', "%Y-%m-%d")
                            elif word=='FEBRERO':
                                endDateActivity = datetime.datetime.strptime(str(cperiod.yearp) + '-' + '03-01', "%Y-%m-%d")
                            elif word=='MARZO':
                                endDateActivity = datetime.datetime.strptime(str(cperiod.yearp) + '-' + '04-01', "%Y-%m-%d")
                            elif word=='ABRIL':
                                endDateActivity = datetime.datetime.strptime(str(cperiod.yearp) + '-' + '05-01', "%Y-%m-%d")
                            elif word=='MAYO':
                                endDateActivity = datetime.datetime.strptime(str(cperiod.yearp) + '-' + '06-01', "%Y-%m-%d")
                    else:
                        endDateActivity = datetime.datetime.strptime(str(cperiod.yearp) + '-' + '06-01', "%Y-%m-%d")
                else:
                    initSemester = datetime.datetime.strptime(str(cperiod.yearp) + '-' + '06-01', "%Y-%m-%d")
                    if report.report_restriction.is_final==False:
                        activities_F=[]
                        nameReportSplit = report.report_restriction.name.upper()
                        nameReportSplit = nameReportSplit.split(' ')
                        for word in nameReportSplit:
                            if word=='JUNIO':
                                endDateActivity = datetime.datetime.strptime(str(cperiod.yearp) + '-' + '07-01', "%Y-%m-%d")
                            elif word=='JULIO':
                                endDateActivity = datetime.datetime.strptime(str(cperiod.yearp) + '-' + '08-01', "%Y-%m-%d")
                            elif word=='AGOSTO':
                                endDateActivity = datetime.datetime.strptime(str(cperiod.yearp) + '-' + '09-01', "%Y-%m-%d")
                            elif word=='SEPTIEMBRE':
                                endDateActivity = datetime.datetime.strptime(str(cperiod.yearp) + '-' + '10-01', "%Y-%m-%d")
                            elif word=='OCTUBRE':
                                endDateActivity = datetime.datetime.strptime(str(cperiod.yearp) + '-' + '11-01', "%Y-%m-%d")
                            elif word=='NOVIEMBRE':
                                endDateActivity = datetime.datetime.strptime(str(cperiod.yearp) + '-' + '12-01', "%Y-%m-%d")
                            elif word=='DICIEMBRE':
                                endDateActivity = datetime.datetime.strptime(str(cperiod.yearp+1) + '-' + '01-01', "%Y-%m-%d")
                    else:
                        endDateActivity = datetime.datetime.strptime(str(cperiod.yearp+1) + '-' + '01-01', "%Y-%m-%d")

                #Verify that the date range of the period and the parameters are defined
                if initSemester is  None or endDateActivity is None or parameters_period is None:
                    session.flash = T('Error. Is not defined date range of the report or do not have the required parameters. --- Contact the system administrator.')
                    redirect(URL('student','index'))
                else:
                    #Get the latest reports and are of this semester
                    beforeReportsRestriction = db((db.report_restriction.id<report.report_restriction)&(db.report_restriction.start_date>=initSemester)).select(db.report_restriction.id)
                    if beforeReportsRestriction.first() is None:
                        beforeReports=[]
                        beforeReports.append(-1)
                    else:
                        beforeReports = db((db.report.assignation==report.assignation)&(db.report.report_restriction.belongs(beforeReportsRestriction))).select(db.report.id)
                        if beforeReports.first() is None:
                            beforeReports=[]
                            beforeReports.append(-1)

                #Check the id of the log type thtat is activity
                temp_logType = db(db.log_type.name=='Activity').select().first()

                #Verify that there is a category activity report
                if temp_logType is None:
                    session.flash = T('Error. Is not defined date range of the report or do not have the required parameters. --- Contact the system administrator.')
                    redirect(URL('student','index'))
                else:
                    #*******************Activities to record activities unless already recorded in previous reports
                    #Activities without metric
                    activitiesWMBefore = db((db.log_entry.log_type==temp_logType)&(db.log_entry.period==cperiod.id)&(db.log_entry.tActivity==False)&(db.log_entry.report.belongs(beforeReports))).select(db.log_entry.idActivity.with_alias('id'))
                    if activitiesWMBefore.first() is None:
                        activities_WM = db((db.course_activity_without_metric.semester == cperiod.id)&(db.course_activity_without_metric.assignation == report.assignation.project)&(db.course_activity_without_metric.date_start < endDateActivity)).select()
                        #Future activities without metric
                        if report.report_restriction.is_final==False:
                            activities_F_temp = db((db.course_activity_without_metric.semester == cperiod.id)&(db.course_activity_without_metric.assignation == report.assignation.project)&(db.course_activity_without_metric.date_start >= endDateActivity)).select()
                            for awmt in activities_F_temp:
                                activities_F.append(awmt)
                    else:
                        activities_WM = db((db.course_activity_without_metric.semester == cperiod.id)&(db.course_activity_without_metric.assignation == report.assignation.project)&(~db.course_activity_without_metric.id.belongs(activitiesWMBefore))&(db.course_activity_without_metric.date_start < endDateActivity)).select()
                        #Future activities without metric
                        if report.report_restriction.is_final==False:
                            activities_F_temp = db((db.course_activity_without_metric.semester == cperiod.id)&(db.course_activity_without_metric.assignation == report.assignation.project)&(~db.course_activity_without_metric.id.belongs(activitiesWMBefore))&(db.course_activity_without_metric.date_start >= endDateActivity)).select()
                            for awmt in activities_F_temp:
                                activities_F.append(awmt)

                    #Activities with metric
                    activitiesMBefore = db((db.log_entry.log_type==temp_logType)&(db.log_entry.period==cperiod.id)&(db.log_entry.tActivity==True)&(db.log_entry.report.belongs(beforeReports))).select(db.log_entry.idActivity.with_alias('id'))
                    activitiesGrades = db((db.grades.academic_assignation==db.academic_course_assignation.id)&(db.academic_course_assignation.semester==cperiod.id)&(db.academic_course_assignation.assignation==report.assignation.project)).select(db.grades.activity.with_alias('id'), distinct=True)
                    if activitiesGrades.first() is not None:
                        activities_M_Real=[]
                        if activitiesMBefore.first() is None:
                            #Complete with measuring activities
                            activities_M = db((db.course_activity.semester == cperiod.id)&(db.course_activity.assignation == report.assignation.project)&(db.course_activity.date_start < endDateActivity)&(db.course_activity.id.belongs(activitiesGrades))).select()
                            for actTempo in activities_M:
                                if report.report_restriction.is_final==False:
                                    tempEndAct = actTempo.date_finish + datetime.timedelta(days=parameters_period.timeout_income_notes)
                                    tempEndAct = datetime.datetime(tempEndAct.year, tempEndAct.month, tempEndAct.day)
                                    endDateActivityt1 = datetime.datetime(endDateActivity.year, endDateActivity.month, endDateActivity.day)
                                    if tempEndAct<endDateActivityt1:
                                        #Check if you have the minimum of notes recorded in the activity amount that you are worth in the report
                                        if (((int(db((db.grades_log.activity_id == actTempo.id)&(db.grades_log.operation_log=='insert')&(db.grades_log.user_name==report.assignation.assigned_user.username)).count())*100)/int(db(db.grades.activity == actTempo.id).count()))>=int(parameters_period.percentage_income_activity)):
                                            activities_M_Real.append(metric_statistics(actTempo,0,None))
                                    else:
                                        #Future activities with metric
                                        activities_F.append(actTempo)
                                else:
                                    #Check if you have the minimum of notes recorded in the activity amount that you are worth in the report
                                    if (((int(db((db.grades_log.activity_id == actTempo.id)&(db.grades_log.operation_log=='insert')&(db.grades_log.user_name==report.assignation.assigned_user.username)).count())*100)/int(db(db.grades.activity == actTempo.id).count()))>=int(parameters_period.percentage_income_activity)):
                                        activities_M_Real.append(metric_statistics(actTempo,0,None))
                            activities_M = activities_M_Real
                            #Complete with measuring future activities
                            if report.report_restriction.is_final==False:
                                activities_F_temp = db((db.course_activity.semester == cperiod.id)&(db.course_activity.assignation == report.assignation.project)&(db.course_activity.date_start >= endDateActivity)).select()
                                for awmt in activities_F_temp:
                                    activities_F.append(awmt)
                        else:
                            #Complete with measuring activities
                            activities_M = db((db.course_activity.semester == cperiod.id)&(db.course_activity.assignation == report.assignation.project)&(db.course_activity.date_start < endDateActivity)&(~db.course_activity.id.belongs(activitiesMBefore))&(db.course_activity.id.belongs(activitiesGrades))).select()
                            for actTempo in activities_M:
                                if report.report_restriction.is_final==False:
                                    tempEndAct = actTempo.date_finish + datetime.timedelta(days=parameters_period.timeout_income_notes)
                                    tempEndAct = datetime.datetime(tempEndAct.year, tempEndAct.month, tempEndAct.day)
                                    endDateActivityt1 = datetime.datetime(endDateActivity.year, endDateActivity.month, endDateActivity.day)
                                    if tempEndAct<endDateActivityt1:
                                        #Check if you have the minimum of notes recorded in the activity amount that you are worth in the report
                                        if (((int(db((db.grades_log.activity_id == actTempo.id)&(db.grades_log.operation_log=='insert')&(db.grades_log.user_name==report.assignation.assigned_user.username)).count())*100)/int(db(db.grades.activity == actTempo.id).count()))>=int(parameters_period.percentage_income_activity)):
                                            activities_M_Real.append(metric_statistics(actTempo,0,None))
                                    else:
                                        #Future activities with metric
                                        activities_F.append(actTempo)
                                else:
                                    #Check if you have the minimum of notes recorded in the activity amount that you are worth in the report
                                    if (((int(db((db.grades_log.activity_id == actTempo.id)&(db.grades_log.operation_log=='insert')&(db.grades_log.user_name==report.assignation.assigned_user.username)).count())*100)/int(db(db.grades.activity == actTempo.id).count()))>=int(parameters_period.percentage_income_activity)):
                                        activities_M_Real.append(metric_statistics(actTempo,0,None))
                            activities_M = activities_M_Real
                            #Complete with measuring future activities
                            if report.report_restriction.is_final==False:
                                activities_F_temp = db((db.course_activity.semester == cperiod.id)&(db.course_activity.assignation == report.assignation.project)&(db.course_activity.date_start >= endDateActivity)&(~db.course_activity.id.belongs(activitiesMBefore))).select()
                                for awmt in activities_F_temp:
                                    activities_F.append(awmt)
            
                #RECOVERY 1 y 2
                if report.report_restriction.is_final==True:
                    #students_first_recovery
                    try:
                        frt = int(db((db.course_first_recovery_test.semester==cperiod.id)&(db.course_first_recovery_test.project==report.assignation.project)).count())
                    except:
                        frt = int(0)
                    if frt>0:
                        if activities_M is None:
                            activities_M=[]
                        activities_M.append(metric_statistics(report,1,None))


                    #students_second_recovery
                    try:
                        srt = int(db((db.course_second_recovery_test.semester==cperiod.id)&(db.course_second_recovery_test.project==report.assignation.project)).count())
                    except:
                        srt = int(0)
                    if srt>0:
                        if activities_M is None:
                            activities_M=[]
                        activities_M.append(metric_statistics(report,2,None))

            if activities_M is None:
                activities_M=[]
            if activities_WM is None:
                activities_WM=[]
            if activities_F is None:
                activities_F=[]
            #***********************************************************************************************************************
            #******************************************************PHASE 2 DTT******************************************************



            return dict(
                log_types=db(db.log_type.id > 0).select(),
                assignation_reports = assignation_reports,
                logs=db((db.log_entry.report == report.id)).select(),
                parameters=parameters,
                metrics=db((db.log_metrics.report == report.id)).select(),
                final_r = db(db.log_final.report == report.id).select(),
                anomalies=db((db.log_type.name == 'Anomaly')&
                           (db.log_entry.log_type == db.log_type.id)&
                           (db.log_entry.report == report.id)).count(),
                markmin_settings=cpfecys.get_markmin,
                report=report,
                next_date=next_date,
                teacher=teacher,
                activities_M=activities_M,
                activities_WM=activities_WM,
                activities_F=activities_F)
        else:
            session.flash = T('Selected report can\'t be viewed. \
                                Select a valid report.')
            redirect(URL('teacher', 'index'))
    elif (request.args(0) == 'grade'):
        if valid:
            score = request.vars['score']
            comment = request.vars['comment']
            if score != None:
                score = int(score)
                if request.vars['improve'] != None:
                    if report.times_graded >= parameters.rescore_max_count and \
                            report.status.name!='EnabledForTeacher':
                        session.flash = T('This report can\'t be sent to \
                            rechecked anymore')
                        redirect(URL('teacher', 'report/view', \
                            vars=dict(report=report.id)))

                    if comment != None:
                        #***********************************************************************************************************************
                        #******************************************************PHASE 2 DTT******************************************************
                        if report.assignation.project.area_level.name=='DTT Tutor Académico':
                            try:
                                temp_logType = db(db.log_type.name=='Activity').select().first()
                                db((db.log_entry.report==report.id)&(db.log_entry.log_type==temp_logType.id)).delete()
                            except:
                                db(db.log_entry.report==report.id).delete()
                            db(db.log_metrics.report==report.id).delete()
                            db(db.log_future.report==report.id).delete()

                            if report.report_restriction.is_final==True:
                                if db(db.log_final.report==report.id).select().first() is None:
                                    #CREATE THE FINAL METRICS
                                    cperiod = obtainPeriodReport(report)
                                    final_metrics = final_metric(cperiod,report)
                                    try:
                                        average=float((final_metrics[22]*100)/final_metrics[20])
                                    except:
                                        average=float(0)
                                    db.log_final.insert(curso_asignados_actas=int(final_metrics[0]),
                                                        curso_en_parciales=int(final_metrics[1]),
                                                        curso_en_final=int(final_metrics[2]),
                                                        curso_en_primera_restrasada=int(final_metrics[3]),
                                                        curso_en_segunda_restrasada=int(final_metrics[4]),
                                                        lab_aprobados=int(final_metrics[5]),
                                                        lab_reprobados=int(final_metrics[6]),
                                                        lab_media=final_metrics[7],
                                                        lab_promedio=final_metrics[8],
                                                        curso_media=final_metrics[9],
                                                        curso_error=final_metrics[10],
                                                        curso_mediana=final_metrics[11],
                                                        curso_moda=final_metrics[12],
                                                        curso_desviacion=final_metrics[13],
                                                        curso_varianza=final_metrics[14],
                                                        curso_curtosis=final_metrics[15],
                                                        curso_coeficiente=final_metrics[16],
                                                        curso_rango=final_metrics[17],
                                                        curso_minimo=final_metrics[18],
                                                        curso_maximo=final_metrics[19],
                                                        curso_total=int(final_metrics[20]),
                                                        curso_reprobados=int(final_metrics[21]),
                                                        curso_aprobados=int(final_metrics[22]),
                                                        curso_promedio=average,
                                                        curso_created=report.created,
                                                        report=report.id
                                                        )


                        #***********************************************************************************************************************
                        #******************************************************PHASE 2 DTT******************************************************

                        report.update_record(
                            score=score,
                            min_score=cpfecys.get_custom_parameters().min_score,
                            teacher_comment=comment,
                            status=db.report_status(name='Recheck'),
                            score_date=cdate,
                            times_graded=(report.times_graded or 0)+1)
                        session.flash = T('The report has been sent to recheck \
                            you will be notified via email when rechecked')
                        # Notification Message
                        import cpfecys
                        signature = (cpfecys.get_custom_parameters().email_signature or '')
                        me_the_user = db.auth_user(db.auth_user.id == auth.user.id)
                        row = db.user_project(db.user_project.id == report.assignation)
                        message = '<html>' + T('The report') + ' ' \
                        + '<b>' + XML(report.report_restriction['name']) + '</b><br/>' \
                        + T('sent by student: ') + XML(row.assigned_user['username']) + ' ' \
                        + XML(row.assigned_user['first_name']) + ' ' + XML(row.assigned_user['last_name']) \
                        + '<br/>' \
                        + T('Score: ') + XML(report.score) + ' ' \
                        + '<br/>' \
                        + T('Scored by: ') + XML(me_the_user.username) + ' ' \
                        + XML(me_the_user.first_name) + ' ' + XML(me_the_user.last_name) \
                        + '<br/>' \
                        + T('Comment: ') + XML(comment) + ' ' \
                        + '<br/>' \
                        + T('Was checked, but sent back to be fixed.') + '<br/>' \
                        + T('You have:') + ' ' + str(db(db.custom_parameters.id > 0).select().first().rescore_max_days) + ' '  + T('days to fix the report.') + '<br/>' \
                        + T('If report is not fixed within given time, then last valid score is taken.') + '<br/>' \
                        + T('Fix the report on:') \
                        + ' ' + cpfecys.get_domain() + '<br />' + signature + '</html>'
                        # send mail to teacher and student notifying change.
                        mails = []
                        # retrieve teacher's email
                        teacher = me_the_user.email
                        mails.append(teacher)
                        # retrieve student's email
                        student_mail = row.assigned_user['email']
                        mails.append(student_mail)
                        was_sent = mail.send(to=mails,
                                  subject=T('[DTT]Automatic Notification - Report needs improvement.'),
                                  # If reply_to is omitted, then mail.settings.sender is used
                                  reply_to = teacher,
                                  message=message)
                        #MAILER LOG
                        db.mailer_log.insert(sent_message = message,
                             destination = ','.join(mails),
                             result_log = str(mail.error or '') + ':' + str(mail.result),
                             success = was_sent)
                        redirect(URL('teacher', 'report/view', \
                            vars=dict(report=report.id)))
                else:
                    if score >= 0  and score <= 100:
                        report.update_record(
                            score=score,
                            min_score=cpfecys.get_custom_parameters().min_score,
                            teacher_comment=comment,
                            status=db.report_status(name='Acceptance'),
                            score_date=cdate,
                            times_graded=(report.times_graded or 0)+1)
                        session.flash = T('The report has been scored \
                            successfully')
                        # Notification Message
                        import cpfecys
                        signature = (cpfecys.get_custom_parameters().email_signature or '')
                        me_the_user = db.auth_user(db.auth_user.id == auth.user.id)
                        row = db.user_project(db.user_project.id == report.assignation)
                        message = '<html>' + T('The report') + ' ' \
                        + '<b>' + XML(report.report_restriction['name']) + '</b><br/>' \
                        + T('sent by student: ') + XML(row.assigned_user['username']) + ' ' \
                        + XML(row.assigned_user['first_name']) + ' ' + XML(row.assigned_user['last_name']) \
                        + '<br/>' \
                        + T('Score: ') + XML(report.score) + ' ' \
                        + '<br/>' \
                        + T('Scored by: ') + XML(me_the_user.username) + ' ' \
                        + XML(me_the_user.first_name) + ' ' + XML(me_the_user.last_name) \
                        + '<br/>' \
                        + T('Comment: ') + XML(comment) + ' ' \
                        + '<br/>' \
                        + T('Was checked. No further actions are needed.') + '<br/>' \
                        + T('DTT-ECYS') \
                        + ' ' + cpfecys.get_domain() + '<br />' + signature + '</html>'
                        # send mail to teacher and student notifying change.
                        mails = []
                        # retrieve teacher's email
                        teacher = me_the_user.email
                        mails.append(teacher)
                        # retrieve student's email
                        student_mail = row.assigned_user['email']
                        mails.append(student_mail)
                        was_sent = mail.send(to=mails,
                                  subject=T('[DTT]Automatic Notification - Report Done.'),
                                  # If reply_to is omitted, then mail.settings.sender is used
                                  reply_to = teacher,
                                  message=message)
                        #MAILER LOG
                        db.mailer_log.insert(sent_message = message,
                             destination = ','.join(mails),
                             result_log = str(mail.error or '') + ':' + str(mail.result),
                             success = was_sent)
                        redirect(URL('teacher', 'report/view', \
                            vars=dict(report=report.id)))

        session.flash = T('Selected report can\'t be viewed. \
                            Select a valid report.')
        redirect(URL('teacher', 'index'))

@auth.requires_login()
@auth.requires_membership('Teacher')
def graphs():
    #requires parameter of project if none is provided then redirected to courses
    project_id = request.vars['project']
    #This also validates the current user is assigned in the project
    if not project_id: redirect(URL('courses'))
    current_project = db((db.user_project.assigned_user == auth.user.id)&
                         (db.project.id == project_id)).select().first()
    if not current_project: redirect(URL('courses'))
    #requires parameter year_period if no one is provided then it is automatically detected
    #and shows the current period
    year_period = request.vars['year_period']
    max_display = 1
    currentyear_period = db.period_year(db.period_year.id == year_period)
    if not currentyear_period:
        import cpfecys
        currentyear_period = cpfecys.current_year_period()
    current_data = db((db.user_project.period <= currentyear_period.id)&
              ((db.user_project.period + db.user_project.periods) > currentyear_period.id)&
              (db.user_project.project == current_project.project.id)&
              (db.auth_group.role == 'Student')&
              (db.auth_membership.group_id == db.auth_group.id)&
              (db.user_project.assigned_user == db.auth_membership.user_id)).select()
    import cpfecys
    current_period_name = T(cpfecys.second_period_name)
    #if we are second semester then start is 1st july
    import datetime
    start_date = datetime.date(currentyear_period.yearp, 7, 7)
    end_date = datetime.date(currentyear_period.yearp, 12, 31)
    if currentyear_period.period == cpfecys.first_period.id:
        current_period_name = T(cpfecys.first_period_name)
        #else we are on first semester, start jan 1st
        start_date = datetime.date(currentyear_period.yearp, 1, 1)
        end_date = datetime.date(currentyear_period.yearp, 6, 30)
    # i need all reports delivered by students for this semester
    reports = db((db.user_project.period <= currentyear_period.id)&
              ((db.user_project.period + db.user_project.periods) > currentyear_period.id)&
              (db.user_project.project == current_project.project.id)&
              (db.auth_group.role == 'Student')&
              (db.auth_membership.group_id == db.auth_group.id)&
              (db.user_project.assigned_user == db.auth_membership.user_id)&
              (db.report_restriction.start_date >= start_date)&
              (db.report_restriction.start_date <= end_date)).select(db.report.ALL, db.report_restriction.ALL, db.user_project.ALL, db.auth_group.ALL, db.auth_membership.ALL, orderby=db.user_project.assigned_user|db.report_restriction.start_date|db.report_restriction.name, left=[db.report.on(db.user_project.id == db.report.assignation), db.report_restriction.on(db.report.report_restriction == db.report_restriction.id)])
    report_activities = db((db.user_project.period <= currentyear_period.id)&
              ((db.user_project.period + db.user_project.periods) > currentyear_period.id)&
              (db.user_project.project == current_project.project.id)&
              (db.auth_group.role == 'Student')&
              (db.auth_membership.group_id == db.auth_group.id)&
              (db.user_project.assigned_user == db.auth_membership.user_id)&
              (db.report_restriction.start_date >= start_date)&
              (db.report_restriction.start_date <= end_date)&
              (db.report.id == db.log_metrics.report)).select(db.log_metrics.ALL, db.report.ALL, db.report_restriction.ALL, db.user_project.ALL, db.auth_group.ALL, db.auth_membership.ALL, orderby=db.user_project.assigned_user|db.report_restriction.start_date|db.report_restriction.name|db.log_metrics.created, left=[db.report.on(db.user_project.id == db.report.assignation), db.report_restriction.on(db.report.report_restriction == db.report_restriction.id)])
    # A helper to display this code within js stuff
    def values_display(values):
        result = "["
        old_user = None
        for item in values:
            if old_user != item.user_project.assigned_user.username:
                if old_user is not None:
                    result += "]},"
                old_user = item.user_project.assigned_user.username
                result += "{ name: '" + item.user_project.assigned_user.username + " - " + item.user_project.assigned_user.first_name +"',"
                result += "data: ["
            #categories.add(item.report.report_restriction)
            result += str(item.report.desertion_continued or 0) + ','
        result += "]}]"
        return XML(result)
    # A helper to display this code within js stuff
    def values_display_activities(values):
        result = "["
        old_user = None
        for item in values:
            if old_user != item.user_project.assigned_user.username:
                if old_user is not None:
                    result += "]},"
                old_user = item.user_project.assigned_user.username
                result += "{ name: '" + item.user_project.assigned_user.username + " - " + item.user_project.assigned_user.first_name +"',"
                result += "data: ["
            #categories.add(item.report.report_restriction)
            result += str(item.log_metrics.mediana or 0) + ','
        result += "]}]"
        return XML(result)
    start_index = currentyear_period.id - max_display - 1
    if start_index < 1:
        start_index = 0
    end_index = currentyear_period.id + max_display
    periods_before = db(db.period_year).select(limitby=(start_index, currentyear_period.id - 1))
    periods_after = db(db.period_year).select(limitby=(currentyear_period.id, end_index))
    other_periods = db(db.period_year).select()
    return dict(current_project = current_project,
                current_data = current_data,
                currentyear_period = currentyear_period,
                current_period_name = current_period_name,
                current_reports = reports,
                values_display = values_display,
                values_display_activities = values_display_activities,
                report_activities = report_activities,
                periods_before = periods_before,
                periods_after = periods_after,
                other_periods = other_periods)

@auth.requires_login()
@auth.requires_membership('Teacher')
def students():
    #requires parameter of project if none is provided then redirected to courses
    project_id = request.vars['project']
    #This also validates the current user is assigned in the project
    if not project_id: redirect(URL('courses'))
    current_project = db((db.user_project.assigned_user == auth.user.id)&
                         (db.project.id == project_id)).select().first()
    if not current_project: redirect(URL('courses'))
    #requires parameter year_period if no one is provided then it is automatically detected
    #and shows the current period
    year_period = request.vars['year_period']
    max_display = 1
    currentyear_period = db.period_year(db.period_year.id == year_period)
    if not currentyear_period:
        currentyear_period = current_year_period()
    current_data = db((db.user_project.period <= currentyear_period.id)&
              ((db.user_project.period + db.user_project.periods) > currentyear_period.id)&
              (db.user_project.project == current_project.project.id)&
              (db.auth_group.role == 'Student')&
              (db.auth_membership.group_id == db.auth_group.id)&
              (db.user_project.assigned_user == db.auth_membership.user_id)).select()
    current_period_name = T(cpfecys.second_period_name)
    #if we are second semester then start is 1st july
    import datetime
    start_date = datetime.date(currentyear_period.yearp, 7, 7)
    end_date = datetime.date(currentyear_period.yearp, 12, 31)
    if currentyear_period.period == cpfecys.first_period.id:
        current_period_name = T(cpfecys.first_period_name)
        #else we are on first semester, start jan 1st
        start_date = datetime.date(currentyear_period.yearp, 1, 1)
        end_date = datetime.date(currentyear_period.yearp, 6, 30)
    # i need all reports delivered by students for this semester
    reports = db((db.user_project.period <= currentyear_period.id)&
              ((db.user_project.period + db.user_project.periods) > currentyear_period.id)&
              (db.user_project.project == current_project.project.id)&
              (db.auth_group.role == 'Student')&
              (db.auth_membership.group_id == db.auth_group.id)&
              (db.user_project.assigned_user == db.auth_membership.user_id)&
              (db.report_restriction.start_date >= start_date)&
              (db.report_restriction.start_date <= end_date)).select(db.report.ALL, db.report_restriction.ALL, db.user_project.ALL, db.auth_group.ALL, db.auth_membership.ALL, orderby=db.user_project.assigned_user|db.report_restriction.start_date|db.report_restriction.name, left=[db.report.on(db.user_project.id == db.report.assignation), db.report_restriction.on(db.report.report_restriction == db.report_restriction.id)])
    report_activities = db((db.user_project.period <= currentyear_period.id)&
              ((db.user_project.period + db.user_project.periods) > currentyear_period.id)&
              (db.user_project.project == current_project.project.id)&
              (db.auth_group.role == 'Student')&
              (db.auth_membership.group_id == db.auth_group.id)&
              (db.user_project.assigned_user == db.auth_membership.user_id)&
              (db.report_restriction.start_date >= start_date)&
              (db.report_restriction.start_date <= end_date)&
              (db.report.id == db.log_metrics.report)).select(db.log_metrics.ALL, db.report.ALL, db.report_restriction.ALL, db.user_project.ALL, db.auth_group.ALL, db.auth_membership.ALL, orderby=db.user_project.assigned_user|db.report_restriction.start_date|db.report_restriction.name, left=[db.report.on(db.user_project.id == db.report.assignation), db.report_restriction.on(db.report.report_restriction == db.report_restriction.id)])
    # A helper to display this code within js stuff
    start_index = currentyear_period.id - max_display - 1
    if start_index < 1:
        start_index = 0
    end_index = currentyear_period.id + max_display
    periods_before = db(db.period_year).select(limitby=(start_index, currentyear_period.id - 1))
    periods_after = db(db.period_year).select(limitby=(currentyear_period.id, end_index))
    other_periods = db(db.period_year).select()
    return dict(current_project = current_project,
                current_data = current_data,
                currentyear_period = currentyear_period,
                current_period_name = current_period_name,
                current_reports = reports,
                report_activities = report_activities,
                periods_before = periods_before,
                periods_after = periods_after,
                other_periods = other_periods)

@auth.requires_login()
@auth.requires_membership('Teacher')
def courses():
    #requires parameter year_period if no one is provided then it is automatically detected
    #and shows the current period
    year_period = request.vars['year_period']
    max_display = 1
    currentyear_period = db.period_year(db.period_year.id == year_period)
    if not currentyear_period:
        import cpfecys
        currentyear_period = cpfecys.current_year_period()
    current_data = db((db.user_project.period <= currentyear_period.id)&
              ((db.user_project.period + db.user_project.periods) > currentyear_period.id)&
              (db.user_project.assigned_user == auth.user.id)).select()
    current_period_name = T(cpfecys.second_period_name)
    if currentyear_period.period == cpfecys.first_period.id:
        current_period_name = T(cpfecys.first_period_name)
    start_index = currentyear_period.id - max_display - 1
    if start_index < 1:
        start_index = 0
    end_index = currentyear_period.id + max_display
    periods_before = db(db.period_year).select(limitby=(start_index, currentyear_period.id - 1))
    periods_after = db(db.period_year).select(limitby=(currentyear_period.id, end_index))
    other_periods = db(db.period_year).select()
    return dict(current_data = current_data,
                currentyear_period = currentyear_period,
                current_period_name = current_period_name,
                periods_before = periods_before,
                periods_after = periods_after,
                other_periods = other_periods)

def find_max_cycles(user_projects):
    cycles = [0]
    for item in user_projects:
        cycles.extend([item.periods])
    return max(cycles)

def get_current_year():
    from datetime import datetime
    return datetime.now().year

def current_year_period():
    #this should be a module's method
    import datetime
    cdate = datetime.datetime.now()
    cyear = cdate.year
    cmonth = cdate.month
    period = cpfecys.second_period
    #current period depends if we are in dates between jan-jun and jul-dec
    if cmonth < 7 :
        period = cpfecys.first_period
    return db.period_year((db.period_year.yearp == cyear)&
                          (db.period_year.period == period))

def grading():
    return locals()
