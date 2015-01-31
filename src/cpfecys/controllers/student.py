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
@auth.requires_membership('Student')
def index():
    import datetime
    current_date = datetime.datetime.now().date()
    assignations = db((db.user_project.assigned_user == auth.user.id)&
                      (db.user_project.assigned_user == db.auth_user.id)&
                      (db.user_project.project == db.project.id)&
                      (db.project.area_level == db.area_level.id)&
                      (db.user_project.period == db.period_year.id)).select()
    cyear_period = cpfecys.current_year_period()
    def available_reports(assignation_period):
        import datetime
        current_date = datetime.datetime.now()
        #if it is the first semester then the restriction should be:
        #start date >= January 1 year 00:00:00
        #end date >= January 1 year 00:00:00
        #start date < July 1 year 00:00:00
        #end date < July 1 year 00:00:00
        #if it is the second semester then the restriction should be:
        #start date >= July 1 year 00:00:00
        #end date >= July 1 year 00:00:00
        #start date < Jan 1 year 00:00:00
        #end date < Jan 1 year 00:00:00
        if assignation_period.period == cpfecys.first_period.id:
            date_min = datetime.datetime(assignation_period.yearp, 1, 1)
            date_max = datetime.datetime(assignation_period.yearp, 7, 1)
        else:
            the_year = assignation_period.yearp + 1
            date_min = datetime.datetime(assignation_period.yearp, 7, 1)
            date_max = datetime.datetime(the_year, 1, 1)
        return db((db.report_restriction.start_date <= current_date)&
                  (db.report_restriction.end_date >= current_date)&
                  (db.report_restriction.start_date >= date_min)&
                  (db.report_restriction.end_date >= date_min)&
                  (db.report_restriction.start_date < date_max)&
                  (db.report_restriction.end_date < date_max)&
                  (db.report_restriction.is_enabled == True))

    def available_item_restriction(period_year, user_project):
        return db(((db.item_restriction.period==period_year) |
                    (db.item_restriction.permanent==True))&
                (db.item_restriction.is_enabled==True)&
                (db.item_restriction_area.item_restriction==\
                    db.item_restriction.id)&
                (db.item_restriction_area.area_level==\
                    user_project.project.area_level.id))

    def has_disabled_items(period_year, item_restriction, assignation):
        items = db((db.item.created==period_year.id)&
            (db.item.item_restriction==item_restriction.id)&
            (db.item.assignation==assignation.user_project.id)&
            (db.item.is_active!=True))
        return items

    def restriction_project_exception(item_restriction_id, project_id):
        return db((db.item_restriction_exception.project== \
                    project_id)&
                    (db.item_restriction_exception.item_restriction \
                        ==item_restriction_id))

    def items_instance(item_restriction, assignation):
        import cpfecys
        period = cpfecys.current_year_period()
        return db((db.item.item_restriction==item_restriction.id)&
                    (db.item.created==period.id)&
                    (db.item.assignation==assignation.user_project.id)&
                    (db.item.is_active==True))

    def get_item(item_restriction, assignation):
        cperiod = cpfecys.current_year_period()
        if item_restriction.period.id < cperiod.id:
            item = db((db.item.item_restriction==item_restriction.id)&
                (db.item.assignation==assignation.user_project.id))
            return item
        return True

    def restriction_in_limit_days(item_restriction):
    	import datetime
        cdate = datetime.datetime.now()
    	cperiod = cpfecys.current_year_period()
    	year = str(cperiod.yearp)
    	if cperiod.period == cpfecys.first_period.id: month = '-01-01'
    	else: month = '-06-01'
        start = datetime.datetime.strptime(year + month, "%Y-%m-%d")
        if item_restriction.limit_days != None:
            last_date = start + datetime.timedelta( \
                days=item_restriction.limit_days)
            if cdate > last_date:
                return False
            return True
        return True

    def calculate_last_day(item_restriction):
        import datetime
        cperiod = cpfecys.current_year_period()
        year = str(cperiod.yearp)
        if cperiod.period == cpfecys.first_period.id: 
            month = '-01-01'
            last = '-06-01'
        else: 
            month = '-06-01'
            last = '-01-01'
        start = datetime.datetime.strptime(year + month, "%Y-%m-%d")
        if item_restriction.limit_days != None:
            last_date = start + datetime.timedelta( \
                days=item_restriction.limit_days-1)
        else:
            if cperiod.period == cpfecys.first_period.id: 
                last_date = datetime.datetime.strptime(year + last, "%Y-%m-%d")
            else:
                year=str(int(year)+1)
                last_date = datetime.datetime.strptime(year + last, "%Y-%m-%d")
                last_date=last_date-datetime.timedelta(days=1)
        return last_date.date()

    def assignation_range(assignation):
        cperiod = cpfecys.current_year_period()
        ends = assignation.period_year.id + assignation.user_project.periods
        period_range = db((db.period_year.id >= assignation.period_year.id)&
            (db.period_year.id < ends)&
            (db.period_year.id <= cperiod.id)).select()
        return period_range

    def is_indate_range(report):
        if report.score_date == None:
            return False
        import datetime
        current_date = datetime.datetime.now().date()
        next_date = report.score_date + datetime.timedelta(
                        days=cpfecys.get_custom_parameters().rescore_max_days)
        return current_date < next_date

    def to_be_created(available_report, assignation):
        report = db((db.report.report_restriction==available_report.id)&
            (db.user_project.id==db.report.assignation)&
            (db.user_project.id==assignation.id)&
            (db.user_project.assigned_user==auth.user.id))
        return report.count() < 1


    return dict(assignations = assignations,
                available_reports = available_reports,
                current_date = current_date,
                cyear_period = cyear_period,
                available_item_restriction = available_item_restriction,
                items_instance = items_instance,
                restriction_project_exception=restriction_project_exception,
                is_indate_range=is_indate_range,
                restriction_in_limit_days=restriction_in_limit_days,
                assignation_range=assignation_range,
                get_item=get_item,
                calculate_last_day=calculate_last_day,
                has_disabled_items=has_disabled_items,
                to_be_created=to_be_created)

@auth.requires_login()
@auth.requires_membership('Student')
def update_data():
    update_data_form = False
    if auth.user != None:
        cuser = db(db.auth_user.id==auth.user.id).select().first()
        form = FORM(
                        DIV(LABEL(T('First Name')),
                                    INPUT(_name="first_name",
                                        _type="text", _id="first_name",
                                        _value=cuser.first_name,
                                        requires=IS_NOT_EMPTY())),

                        DIV(LABEL(T('Last Name')),
                                       INPUT(_name="last_name",
                                        _type="text", _id="last_name",
                                         _value=cuser.last_name, 
                                         requires=IS_NOT_EMPTY())),

                        DIV(LABEL(T('Email')),
                                       INPUT(_name="email",
                                        _type="text", _id="email",
                                        _value=cuser.email,
                                        requires=IS_NOT_EMPTY())),

                        DIV(LABEL(T('Password (Leave the same for no \
                            change)')),
                                      INPUT(_name="password",
                                        _type="password", _id="password",
                                        _value=cuser.password,
                                        requires=IS_NOT_EMPTY())),

                        DIV(LABEL(T('Repeat password (Leave the blank for \
                            no change)')),
                                      INPUT(_name="repass",
                                        _type="password", _id="repass")),

                        DIV(LABEL(T('Phone')),
                                      INPUT(_name="phone", _type="text",
                                        _id="phone", _value=cuser.phone,
                                        requires=IS_LENGTH(minsize=8,
                                                        maxsize=12))),
                        DIV(LABEL(T('Working')),
                                      INPUT(_name="working",
                                        _type="checkbox", _id="working",
                                        _value=cuser.working)),

                        DIV(LABEL(T('Work Address')),
                                      INPUT(_name="work_address",
                                        _type="text", _id="work_address",
                                        _value=cuser.work_address)),
                        DIV(LABEL(T('Company Name')),
                                      INPUT(_name="company_name",
                                        _type="text", _id="company_name",
                                        _value=cuser.company_name)),
                        DIV(LABEL(T('Work phone')),
                                      INPUT(_name="work_phone",
                                        _type="text", _id="work_phone",
                                        _value=cuser.work_phone)),
                        DIV(LABEL(T('Home Address')),
                                      INPUT(_name="home_address",
                                        _type="text", _id="home_address",
                                        _value=cuser.home_address)),
                        DIV(LABEL(T('Photo')),
                                      INPUT(_name="photo",
                                        _class="upload",
                                        _type="file", _id="photo",
                                        requires=[IS_IMAGE(extensions =('jpeg', 'png'), maxsize=(200, 300),\
                    error_message=T('Only files are accepted with extension') +\
                    ' png|jpg'+" "+T('with 200x300px size')+".")],
                                        _value=cuser.photo)),
                        BR(),
                        DIV(INPUT(_type='submit',
                            _id="update_data",
                            _value=T('Update Profile'),
                            _class="btn-primary")),
                            _class="form-horizontal",)
        if form.process().accepted:
            first_name = request.vars['first_name']
            last_name = request.vars['last_name']
            email = request.vars['email']
            password = request.vars['password']
            repass = request.vars['repass']
            phone = request.vars['phone']
            working = request.vars['working']
            work_address = request.vars['work_address']
            company_name = request.vars['company_name']
            work_phone = request.vars['work_phone']
            home_address = request.vars['home_address']
            photo = request.vars['photo']


            #TODO analyze for aditional security steps
            cuser=db(db.auth_user.id==auth.user.id).select().first()
            if cuser != None:
                cuser.first_name = first_name
                cuser.last_name = last_name
                cuser.email = email
                cuser.phone = phone
                cuser.company_name = company_name
                cuser.work_phone = work_phone
                cuser.home_address = home_address
                cuser.photo = photo
                cuser.data_updated = True
                if password == repass and len(repass) > 0:
                    #TODO Fix password update
                    cuser.password = db.auth_user.password.validate(password)[0]
                if working:
                    cuser.working = working
                    cuser.work_address = work_address

                cuser.update_record()
                response.flash = T('User data updated!')
                redirect(URL('default', 'index'))
            else:
                response.flash = 'Error!'

        elif form.errors:
            response.flash = T('form has errors')
        else:
            response.flash = T('please fill the form')
    return dict(form=form, update_data_form=True)

@cache.action()
@auth.requires_login()
@auth.requires_membership('Student')
def download():
    item = db(db.item.uploaded_file==request.args[0]).select().first()
    if item != None and item.assignation.assigned_user == auth.user.id:
        return response.download(request, db)
    else:
        session.flash = T('Access Forbidden')
        redirect(URL('default', 'index'))

@auth.requires_login()
@auth.requires_membership('Student')
def report_hours():
    if (request.args(0) == 'create'):
        report = request.vars['report']
        hours = request.vars['report-hours']
        ## Get the report id
        report = db.report(db.report.id == report)
        valid = not(report is None) and not(hours is None)
        ## Validate report TIMING restriction
        #if valid: valid = cpfecys.student_validation_report_restrictions(report.report_restriction.id)
        ## Validate assignation
        if valid: valid = not cpfecys.assignation_is_locked(report.assignation)
        ## Validate that the report belongs to user
        if valid: valid = cpfecys.student_validation_report_owner(report.id)
        ## Validate that the report status is editable (it is either 'Draft' or 'Recheck')
        if valid: valid = cpfecys.student_validation_report_status(report)
        if valid:
            report.hours = hours
            report.update_record()
            session.flash = T('Report updated.')
            redirect(URL('student','report/edit', vars = dict(report = report.id)))
        else:
            session.flash = T('Selected report can\'t be edited. Select a valid report.')
            redirect(URL('student','index'))
    elif (request.args(0) == 'update'):
        report = request.vars['report']
        hours = request.vars['report-hours']
        report = db.report(db.report.id == report)
        valid = not(report is None) and not(hours is None)
        ## Validate report TIMING restriction
        #if valid: valid = cpfecys.student_validation_report_restrictions(report.report_restriction.id)
        ## Validate assignation
        if valid: valid = not cpfecys.assignation_is_locked(report.assignation)
        ## Validate that the report belongs to user
        if valid: valid = cpfecys.student_validation_report_owner(report.id)
        ## Validate that the report status is editable (it is either 'Draft' or 'Recheck')
        if valid: valid = cpfecys.student_validation_report_status(report)
        if valid:
            report.hours = hours
            report.update_record()
            session.flash = T('Report updated.')
            redirect(URL('student','report/edit', vars = dict(report = report.id)))
        else:
            session.flash = T('Selected report can\'t be edited. Select a valid report.')
            redirect(URL('student','index'))
    elif (request.args(0) == 'delete'):
        report = request.vars['report']
        report = db.report(db.report.id == report)
        valid = not(report is None)
        ## Validate report TIMING restriction
        #if valid: valid = cpfecys.student_validation_report_restrictions(report.report_restriction.id)
        ## Validate assignation
        if valid: valid = not cpfecys.assignation_is_locked(report.assignation)
        ## Validate that the report belongs to user
        if valid: valid = cpfecys.student_validation_report_owner(report.id)
        ## Validate that the report status is editable (it is either 'Draft' or 'Recheck')
        if valid: valid = cpfecys.student_validation_report_status(report)
        if valid:
            report.hours = None
            report.update_record()
            session.flash = T('Report updated.')
            redirect(URL('student','report/edit', vars = dict(report = report.id)))
        else:
            session.flash = T('Selected report can\'t be edited. Select a valid report.')
            redirect(URL('student','index'))
    raise HTTP(404)

@auth.requires_login()
@auth.requires_membership('Student')
def report_header():
    if (request.args(0) == 'create'):
        report = request.vars['report']
        content = request.vars['report-content']
        ## Get the report id
        report = db.report(db.report.id == report)
        valid = not(report is None) and not(content is None)
        ## Validate report TIMING restriction
        #if valid: valid = cpfecys.student_validation_report_restrictions(report.report_restriction.id)
        ## Validate assignation
        if valid: valid = not cpfecys.assignation_is_locked(report.assignation)
        ## Validate that the report belongs to user
        if valid: valid = cpfecys.student_validation_report_owner(report.id)
        ## Validate that the report status is editable (it is either 'Draft' or 'Recheck')
        if valid: valid = cpfecys.student_validation_report_status(report)
        if valid:
            report.heading = content
            report.update_record()
            session.flash = T('Report updated.')
            redirect(URL('student','report/edit', vars = dict(report = report.id)))
        else:
            session.flash = T('Selected report can\'t be edited. Select a valid report.')
            redirect(URL('student','index'))
    elif (request.args(0) == 'update'):
        report = request.vars['report']
        content = request.vars['report-content']
        report = db.report(db.report.id == report)
        valid = not(report is None) and not(content is None)
        ## Validate report TIMING restriction
        #if valid: valid = cpfecys.student_validation_report_restrictions(report.report_restriction.id)
        ## Validate assignation
        if valid: valid = not cpfecys.assignation_is_locked(report.assignation)
        ## Validate that the report belongs to user
        if valid: valid = cpfecys.student_validation_report_owner(report.id)
        ## Validate that the report status is editable (it is either 'Draft' or 'Recheck')
        if valid: valid = cpfecys.student_validation_report_status(report)
        if valid:
            report.heading = content
            report.update_record()
            session.flash = T('Report updated.')
            redirect(URL('student','report/edit', vars = dict(report = report.id)))
        else:
            session.flash = T('Selected report can\'t be edited. Select a valid report.')
            redirect(URL('student','index'))
    elif (request.args(0) == 'delete'):
        report = request.vars['report']
        report = db.report(db.report.id == report)
        valid = not(report is None)
        ## Validate report TIMING restriction
        #if valid: valid = cpfecys.student_validation_report_restrictions(report.report_restriction.id)
        ## Validate assignation
        if valid: valid = not cpfecys.assignation_is_locked(report.assignation)
        ## Validate that the report belongs to user
        if valid: valid = cpfecys.student_validation_report_owner(report.id)
        ## Validate that the report status is editable (it is either 'Draft' or 'Recheck')
        if valid: valid = cpfecys.student_validation_report_status(report)
        if valid:
            report.heading = None
            report.update_record()
            session.flash = T('Report updated.')
            redirect(URL('student','report/edit', vars = dict(report = report.id)))
        else:
            print 5
            session.flash = T('Selected report can\'t be edited. Select a valid report.')
            redirect(URL('student','index'))
    raise HTTP(404)

@auth.requires_login()
@auth.requires_membership('Student')
def report_footer():
    if (request.args(0) == 'create'):
        report = request.vars['report']
        content = request.vars['report-content']
        ## Get the report id
        report = db.report(db.report.id == report)
        valid = not(report is None) and not(content is None)
        ## Validate report TIMING restriction
        #if valid: valid = cpfecys.student_validation_report_restrictions(report.report_restriction.id)
        ## Validate assignation
        if valid: valid = not cpfecys.assignation_is_locked(report.assignation)
        ## Validate that the report belongs to user
        if valid: valid = cpfecys.student_validation_report_owner(report.id)
        ## Validate that the report status is editable (it is either 'Draft' or 'Recheck')
        if valid: valid = cpfecys.student_validation_report_status(report)
        if valid:
            report.footer = content
            report.update_record()
            session.flash = T('Report updated.')
            redirect(URL('student','report/edit', vars = dict(report = report.id)))
        else:
            session.flash = T('Selected report can\'t be edited. Select a valid report.')
            redirect(URL('student','index'))
    elif (request.args(0) == 'update'):
        report = request.vars['report']
        content = request.vars['report-content']
        report = db.report(db.report.id == report)
        valid = not(report is None) and not(content is None)
        ## Validate report TIMING restriction
        #if valid: valid = cpfecys.student_validation_report_restrictions(report.report_restriction.id)
        ## Validate assignation
        if valid: valid = not cpfecys.assignation_is_locked(report.assignation)
        ## Validate that the report belongs to user
        if valid: valid = cpfecys.student_validation_report_owner(report.id)
        ## Validate that the report status is editable (it is either 'Draft' or 'Recheck')
        if valid: valid = cpfecys.student_validation_report_status(report)
        if valid:
            report.footer = content
            report.update_record()
            session.flash = T('Report updated.')
            redirect(URL('student','report/edit', vars = dict(report = report.id)))
        else:
            session.flash = T('Selected report can\'t be edited. Select a valid report.')
            redirect(URL('student','index'))
    elif (request.args(0) == 'delete'):
        report = request.vars['report']
        report = db.report(db.report.id == report)
        valid = not(report is None)
        ## Validate report TIMING restriction
        #if valid: valid = cpfecys.student_validation_report_restrictions(report.report_restriction.id)
        ## Validate assignation
        if valid: valid = not cpfecys.assignation_is_locked(report.assignation)
        ## Validate that the report belongs to user
        if valid: valid = cpfecys.student_validation_report_owner(report.id)
        ## Validate that the report status is editable (it is either 'Draft' or 'Recheck')
        if valid: valid = cpfecys.student_validation_report_status(report)
        if valid:
            report.footer = None
            report.update_record()
            session.flash = T('Report updated.')
            redirect(URL('student','report/edit', vars = dict(report = report.id)))
        else:
            session.flash = T('Selected report can\'t be edited. Select a valid report.')
            redirect(URL('student','index'))
    raise HTTP(404)

@auth.requires_login()
@auth.requires_membership('Student')
def item():
    cyear_period = cpfecys.current_year_period()
    item_restriction = request.vars['restriction']
    user_project = request.vars['assignation']
    period = request.vars['period']
    if period == None:
        session.flash = T('Action not allowed')
        redirect(URL('student', 'index'))
    period = int(period)
    area = request.vars['area']
    assignation = db((db.user_project.id==user_project)&
            (db.user_project.assigned_user==auth.user.id)
            ).select().first()
    item_query = db((db.item.created==cyear_period)&
                (db.item.item_restriction==item_restriction)&
                (db.item.assignation==user_project)&
                (db.item.is_active==True))
    item_restriction = db(db.item_restriction.id==\
            item_restriction).select().first()

    if(request.args(0) == 'create'):
        if assignation == None:
            session.flash = T('This item can\'t be\
                edited, permissions problem')
            redirect(URL('student', 'index'))

        if cpfecys.assignation_is_locked(assignation):
            session.flash = T('This item can\'t be\
                edited, its assignation is locked')
            redirect(URL('student', 'index'))
        if cyear_period.id != period:
            session.flash = T('This item can\'t be\
                edited, item edition for this item is out of time')
            redirect(URL('student', 'index'))
        itm_res_area = db(
            (db.item_restriction_area.area_level==area)&
            (db.item_restriction_area.item_restriction== \
                item_restriction)&
            (db.item_restriction_area.is_enabled==True)
            )._select()

        if itm_res_area == None:
            session.flash = T('This item can\'t be\
                edited, doesn\'t belongs to this project')
            redirect(URL('student', 'index'))
        if item_restriction.limit_days != None:
            import datetime
            cdate = datetime.datetime.now()
            cperiod = cpfecys.current_year_period()
            year = str(cperiod.yearp)
            if cperiod.period == cpfecys.first_period.id: 
                month = '-01-01'
            else: 
                month = '-06-01'
            start = \
                datetime.datetime.strptime(year + month, "%Y-%m-%d")
            if item_restriction.limit_days != None:
                last_date = start + datetime.timedelta( \
                    days=item_restriction.limit_days)
                if cdate > last_date:
                    session.flash = T('This item can\'t be\
                    edited, out of date, last date was' +\
                    last_date)
                    redirect(URL('student', 'index'))
        if item_query.select().first() == None:
            if item_restriction.item_type.name == 'File':
                form = FORM(
                            DIV(LABEL(T('Upload '+item_restriction.name+' \
                            File:')),
                            INPUT(_name="upload", 
                                _type="file", _id="first_name", 
                                requires=[IS_NOT_EMPTY(), \
                                            IS_UPLOAD_FILENAME( \
                                            extension='^(pdf|doc|docx)$',\
                                            error_message=T('Invalid Format, \
                                            Please upload only PDF, DOC or \
                                            DOCX files files'))])),
                            BR(),
                            DIV(INPUT(_type='submit',
                                            _value=T('Upload File'),
                                            _class="btn-primary")),
                                            _class="form-horizontal",)
                if form.process().accepted:
                    if request.vars.upload != None:
                        item = db.item.uploaded_file.store( \
                            request.vars.upload.file,  \
                            request.vars.upload.filename)
                        db.item.insert(uploaded_file=item,
                            is_active=True,
                            created=cyear_period,
                            item_restriction=item_restriction.id,
                            assignation=user_project)
                        db.commit()
                        session.flash = T('Item created!')
                        redirect(URL('student', 'index'))
                    else:
                        session.flash = T('Form Errors')
                        redirect(URL('student', 'index'))
                #elif form.errors:
                    #session.flash = form.errors
                    #redirect(URL('student', 'index'))
                #else:
                    #session.flash = T('please fill the form')
                return  dict(form=form, action='create')
            elif item_restriction.item_type.name == 'Schedule':
                # TODO: Finish up schedule views and controller
                #this thing is meant to allow students to create an item that 
                #is a schedule for something
                #schedule? yep like the hours where they are busy somewhere
                #Example: Course Schedule: Mon (0900-0930) Tue (1500-1530)
                #or DSI Attention: Tue (1000 - 1230)
                #or basically anything :P
                #we need the id of the created deliverable item
                item = db.item.insert(is_active=True,
                                      created=cyear_period,
                                      item_restriction=item_restriction.id,
                                      assignation=user_project)
                session.flash = T('Item Created')
                redirect(URL('student', 'item',  args=['edit'],\
                    vars = dict(restriction=item_restriction.id, \
                        assignation=user_project, \
                        period=period,
                        item=item.id)))
                #return
        else:
            session.flash = T('Action not allowed')
            redirect(URL('student', 'index'))
    elif(request.args(0) == 'view'):
        item_upload = request.vars['file']
        item = db((db.item.item_restriction==item_restriction)&
            (db.item.assignation==user_project)&
            (db.item.uploaded_file==item_upload)).select().first()
        if item != None and item_restriction.teacher_only != True \
                and item.is_active == True \
                and item.assignation.assigned_user == auth.user.id:
            return dict(item=item, name=item_restriction.name, action='view')
        else:
            session.flash = T('Access Forbidden')
            redirect(URL('student', 'index'))

    elif(request.args(0) == 'edit'):
        item_id = request.vars['item']
        if assignation == None:
            session.flash = T('This item can\'t be\
                edited, permissions problem')
            redirect(URL('student', 'index'))

        if cpfecys.assignation_is_locked(assignation):
            session.flash = T('This item can\'t be\
                edited, its assignation is locked')
            redirect(URL('student', 'index'))
        if cyear_period.id != period:
            session.flash = T('This item can\'t be\
                edited, item edition for this item is out of time')
            redirect(URL('student', 'index'))

        can_edit = db((db.item_restriction.id==item_restriction)&
            (db.item.item_restriction==db.item_restriction.id)&
            (db.item.id==item_id)&
            (db.item.assignation==db.user_project.id)&
            (db.item.assignation==user_project)&
            (db.item.created==db.period_year.id)&
            (db.period_year.id==period))

        if can_edit == None:
            session.flash = T('This item can\'t be\
                edited, doesn\'t belongs to this project')
            redirect(URL('student', 'index'))
        if item_restriction.limit_days != None:
            import datetime
            cdate = datetime.datetime.now()
            cperiod = cpfecys.current_year_period()
            year = str(cperiod.yearp)
            if cperiod.period == cpfecys.first_period.id: 
                month = '-01-01'
            else: 
                month = '-06-01'
            start = \
                datetime.datetime.strptime(year + month, "%Y-%m-%d")
            if item_restriction.limit_days != None:
                last_date = start + datetime.timedelta( \
                    days=item_restriction.limit_days)
                if cdate > last_date:
                    session.flash = T('This item can\'t be\
                    edited, doesn\'t out of date, last date was: ')  +\
                    str(last_date)
                    redirect(URL('student', 'index'))

        item = db(db.item.id==item_id).select().first()
        if item == None or item.is_active != True:
            session.flash = ('This item can\'t be\
                    edited, doesn\'t exists or is not active')
            redirect(URL('student', 'index'))
        if item.item_restriction.item_type.name == 'File':
            form = FORM(
                    DIV(LABEL(T('Upload '+item_restriction.name+' \
                        File:')),
                                INPUT(_name="upload", 
                                    _type="file", _id="first_name", 
                                    requires=[IS_NOT_EMPTY(), \
                                            IS_UPLOAD_FILENAME( \
                                            extension='^(pdf|doc|docx)$',\
                                            error_message=T('Invalid Format, \
                                            Please upload only PDF, DOC or \
                                            DOCX files files'))])),
                    BR(),
                    DIV(INPUT(_type='submit',
                        _value=T('Upload File'),
                        _class="btn-primary")),
                        _class="form-horizontal",)
            if form.process().accepted:
                if request.vars.upload != None:
                    uploaded = db.item.uploaded_file.store(request.vars.upload.file, request.vars.upload.filename)
                    item = db((db.item.created==cyear_period)&
                    (db.item.item_restriction==item_restriction)&
                    (db.item.assignation==user_project)).select().first()
                    if item != None:
                        item.update_record(uploaded_file = uploaded)
                        db.commit()
                        redirect(URL('student', 'index'))
                    elif form.errors:
                        response.flash = "Errors"
                    else:
                        response.flash = "please fill the form"
            return  dict(form=form, action='edit')
        elif item.item_restriction.item_type.name == 'Schedule':
            db.item_schedule.item.writable = False
            db.item_schedule.item.default = item.id
            response.view = 'student/schedule.html'
            grid = SQLFORM.grid((db.item_schedule.item == item.id), args=request.args)
            return dict(schedule_name = item.item_restriction.name, grid = grid)
    else:
        response.view = 'student/schedule.html'
        grid = SQLFORM.grid(db.item_schedule)
        return dict(schedule_name = 'Horario de Curso', grid = grid)

@auth.requires_login()
@auth.requires_membership('Student')
def final():
    if(request.args(0) == 'save'):
        # validate the user owns this report
        report = request.vars['report']
        report = db.report(db.report.id == report)
        valid_report = report != None
        ## Validate assignation
        if valid_report: valid_report = not cpfecys.assignation_is_locked(report.assignation)
        if valid_report: valid_report = cpfecys.student_validation_report_owner(report.id)
        # validate report is editable
        #if valid_report: valid_report = cpfecys.student_validation_report_restrictions \
            #(report.report_restriction)
        # validate report is 'Draft' or 'Recheck'
        if valid_report: valid_report = cpfecys.student_validation_report_status(report)
        # validate we receive log-date, log-type, log-content
        aprobados_metrics = request.vars['aprobados-metrics']
        coeficiente_metrics = request.vars['coeficiente-metrics']
        curso_asignados_actas = request.vars['curso-asignados-actas']
        curso_en_final = request.vars['curso-en-final']
        curso_en_parciales = request.vars['curso-en-parciales']
        curso_en_primera_retrasada = request.vars['curso-en-primera-retrasada']
        curso_en_segunda_retrasada = request.vars['curso-en-segunda-retrasada']
        curtosis_metrics = request.vars['curtosis-metrics']
        desviacion_estandar_metrics = request.vars['desviacion-estandar-metrics']
        error_tipico_metrics = request.vars['error-tipico-metrics']
        lab_aprobados = request.vars['lab-aprobados']
        lab_media = request.vars['lab-media']
        lab_promedios = request.vars['lab-promedio']
        lab_reprobados = request.vars['lab-reprobados']
        log_date = request.vars['log-date']
        maximo_metrics = request.vars['maximo-metrics']
        media_metrics = request.vars['media-metrics']
        mediana_metrics = request.vars['mediana-metrics']
        minimo_metrics = request.vars['minimo-metrics']
        moda_metrics = request.vars['moda-metrics']
        promedio_metrics = request.vars['promedio-metrics']
        rango_metrics = request.vars['rango-metrics']
        reprobados_metrics = request.vars['reprobados-metrics']
        total_metrics = request.vars['total-metrics']
        varianza_metrics = request.vars['varianza-metrics']
        if valid_report:
            valid_report = (aprobados_metrics and coeficiente_metrics and curso_asignados_actas \
                                         and curso_en_final and curso_en_parciales  
                                         and curso_en_primera_retrasada and curso_en_segunda_retrasada \
                                         and curtosis_metrics and desviacion_estandar_metrics \
                                         and error_tipico_metrics and lab_aprobados and lab_media \
                                         and lab_promedios and lab_reprobados \
                                         and media_metrics and mediana_metrics \
                                         and minimo_metrics and moda_metrics \
                                         and promedio_metrics and rango_metrics \
                                         and reprobados_metrics and total_metrics \
                                         and varianza_metrics \
                                         and log_date and maximo_metrics)

        if valid_report:
            db.log_final.insert(curso_asignados_actas = curso_asignados_actas,
                                curso_en_parciales = curso_en_parciales,
                                curso_en_final = curso_en_final,
                                curso_en_primera_restrasada = curso_en_primera_retrasada,
                                curso_en_segunda_restrasada = curso_en_segunda_retrasada,
                                lab_aprobados = lab_aprobados,
                                lab_reprobados = lab_reprobados,
                                lab_media = lab_media,
                                lab_promedio = lab_promedios,
                                curso_media = media_metrics,
                                curso_error = error_tipico_metrics,
                                curso_mediana = mediana_metrics,
                                curso_moda = moda_metrics,
                                curso_desviacion = desviacion_estandar_metrics,
                                curso_varianza = varianza_metrics,
                                curso_curtosis = curtosis_metrics,
                                curso_coeficiente = coeficiente_metrics,
                                curso_rango = rango_metrics,
                                curso_minimo = minimo_metrics,
                                curso_maximo = maximo_metrics,
                                curso_total = total_metrics,
                                curso_reprobados = reprobados_metrics,
                                curso_aprobados = aprobados_metrics,
                                curso_promedio = promedio_metrics,
                                curso_created = log_date,
                                report = report)
            session.flash = T('Log added')
            redirect(URL('student', 'report/edit', vars=dict(report=report.id)))
    elif(request.args(0) == 'update'):
        # validate the requested metric
        final = request.vars['final']
        final = db.log_final(db.log_final.id == final)
        valid_final = final != None
        ## Validate assignation
        if valid_final: valid_final = not cpfecys.assignation_is_locked(final.report.assignation)
        # validate metric report owner is valid
        if valid_final: valid_final = cpfecys.student_validation_report_owner(final.report)
        # validate report is editable
        #if valid_final: valid_final = cpfecys.student_validation_report_restrictions \
        #    (final.report['report_restriction'])
        # validate report is 'Draft' or 'Recheck'
        if valid_final: valid_final = cpfecys.student_validation_report_status \
            (db.report(db.report.id == final.report))
        # validate we receive log-date, log-type, log-content

        aprobados_metrics = request.vars['aprobados-metrics']
        coeficiente_metrics = request.vars['coeficiente-metrics']
        curso_asignados_actas = request.vars['curso-asignados-actas']
        curso_en_final = request.vars['curso-en-final']
        curso_en_parciales = request.vars['curso-en-parciales']
        curso_en_primera_retrasada = request.vars['curso-en-primera-retrasada']
        curso_en_segunda_retrasada = request.vars['curso-en-segunda-retrasada']
        curtosis_metrics = request.vars['curtosis-metrics']
        desviacion_estandar_metrics = request.vars['desviacion-estandar-metrics']
        error_tipico_metrics = request.vars['error-tipico-metrics']
        lab_aprobados = request.vars['lab-aprobados']
        lab_media = request.vars['lab-media']
        lab_promedios = request.vars['lab-promedio']
        lab_reprobados = request.vars['lab-reprobados']
        log_date = request.vars['log-date']
        maximo_metrics = request.vars['maximo-metrics']
        media_metrics = request.vars['media-metrics']
        mediana_metrics = request.vars['mediana-metrics']
        minimo_metrics = request.vars['minimo-metrics']
        moda_metrics = request.vars['moda-metrics']
        promedio_metrics = request.vars['promedio-metrics']
        rango_metrics = request.vars['rango-metrics']
        reprobados_metrics = request.vars['reprobados-metrics']
        total_metrics = request.vars['total-metrics']
        varianza_metrics = request.vars['varianza-metrics']
        if valid_final:
            valid_final = (aprobados_metrics and coeficiente_metrics and curso_asignados_actas \
                                         and curso_en_final and curso_en_parciales  
                                         and curso_en_primera_retrasada and curso_en_segunda_retrasada \
                                         and curtosis_metrics and desviacion_estandar_metrics \
                                         and error_tipico_metrics and lab_aprobados and lab_media \
                                         and lab_promedios and lab_reprobados \
                                         and media_metrics and mediana_metrics \
                                         and minimo_metrics and moda_metrics \
                                         and promedio_metrics and rango_metrics \
                                         and reprobados_metrics and total_metrics \
                                         and varianza_metrics \
                                         and log_date and maximo_metrics)
        if valid_final:
            final.update_record(curso_asignados_actas = curso_asignados_actas,
                                curso_en_parciales = curso_en_parciales,
                                curso_en_final = curso_en_final,
                                curso_en_primera_restrasada = curso_en_primera_retrasada,
                                curso_en_segunda_restrasada = curso_en_segunda_retrasada,
                                lab_aprobados = lab_aprobados,
                                lab_reprobados = lab_reprobados,
                                lab_media = lab_media,
                                lab_promedio = lab_promedios,
                                curso_media = media_metrics,
                                curso_error = error_tipico_metrics,
                                curso_mediana = mediana_metrics,
                                curso_moda = moda_metrics,
                                curso_desviacion = desviacion_estandar_metrics,
                                curso_varianza = varianza_metrics,
                                curso_curtosis = curtosis_metrics,
                                curso_coeficiente = coeficiente_metrics,
                                curso_rango = rango_metrics,
                                curso_minimo = minimo_metrics,
                                curso_maximo = maximo_metrics,
                                curso_total = total_metrics,
                                curso_reprobados = reprobados_metrics,
                                curso_aprobados = aprobados_metrics,
                                curso_promedio = promedio_metrics,
                                curso_created = log_date)
            session.flash = T('Updated')
            redirect(URL('student', 'report/edit', vars=dict(report=final.report)))
    elif(request.args(0) == 'delete'):
        # validate the requested log
        final = request.vars['final']
        final = db.log_final(db.log_final.id == final)
        valid_final = final != None
        # validate log report owner is valid
        if valid_final: valid_final = cpfecys.student_validation_report_owner(final.report)
        ## Validate assignation
        if valid_final: valid_final = not cpfecys.assignation_is_locked(final.report.assignation)
        # validate report is editable
        #if valid_final: valid_final = cpfecys.student_validation_report_restrictions \
        #    (final.report['report_restriction'])
        # validate report is 'Draft' or 'Recheck'
        if valid_final: valid_final = cpfecys.student_validation_report_status \
            (db.report(db.report.id == final.report))
        if valid_final:
            final.delete_record()
            session.flash = T('Log Deleted')
            redirect(URL('student', 'report/edit', vars=dict(report=final.report)))
        else:
            session.flash = T('Operation not allowed.')
            redirect(URL('student', 'index'))
    #session.flash = T('Error')
    #redirect(URL('student', 'index'))
    return

@auth.requires_login()
@auth.requires_membership('Student')
def report():
    import cpfecys
    import datetime
    if (request.args(0) == 'create'):
        #get the data & save the report
        assignation = request.vars['assignation']
        report_restriction = request.vars['report_restriction']
        # Validate DB report_restriction to obey TIMING rules
        import cpfecys
        #valid_rep_restr = cpfecys.student_validation_report_restrictions(report_restriction)
        # Validate report_restriction
        report_restrict = db.report_restriction(\
            db.report_restriction.id == report_restriction)
        valid_report = report_restrict != None
        # Validate assignation belongs to this user
        assign = db.user_project((db.user_project.id == assignation)&
                                (db.user_project.assigned_user == auth.user.id))
        valid_assignation = assign != None
        ## Validate assignation
        if valid_assignation: valid_assignation = \
            not cpfecys.assignation_is_locked(assign)
        # Validate there is not an already inserted report
        valid = db.report((db.report.assignation == assignation)&
                  (db.report.report_restriction == report_restriction)) is None
        if not(assignation and report_restriction and valid \
                and valid_assignation and valid_report):
            session.flash = T('Invalid selected assignation \
                                and report. Select a valid one.') + 'INV001'
            redirect(URL('student','index'))
        import datetime
        current_date = datetime.datetime.now()
        report = db.report.insert(created = current_date,
                             assignation = assignation,
                             report_restriction = report_restriction,
                             status = db.report_status(name = 'Draft'))


        #***********************************************************************************************************************
        #******************************************************PHASE 2 DTT******************************************************
        if report.assignation.project.area_level.name=='DTT Tutor Académico' and report.report_restriction.is_final==True:
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
                                curso_created=current_date,
                                report=report.id
                                )
        #***********************************************************************************************************************
        #******************************************************PHASE 2 DTT******************************************************


        session.flash = T('Report is now a draft.')
        redirect(URL('student','report/edit', vars = dict(report = report.id)))
    elif (request.args(0) == 'edit'):
        ## Get the report id
        report = request.vars['report']
        ## Retrieve report data
        report = db.report(db.report.id == report)
        if not(report):
            session.flash = T('Selected report can\'t be edited. \
                Select a valid report.')
            redirect(URL('student','index'))
        ## Validate assignation
        import cpfecys
        if cpfecys.assignation_is_locked(report.assignation):
            session.flash = T('Selected report can\'t be edited. \
                Select a valid report.')
            redirect(URL('student','index'))
        ## Validate report TIMING restriction
        #valid_rep_restr = cpfecys.student_validation_report_restrictions(report.report_restriction.id)
        #if not(valid_rep_restr):
        #    session.flash = T('Selected report can\'t be edited. Select a valid report.')
        #    redirect(URL('student','index'))
        ## Validate that the report belongs to user
        valid_report_owner = cpfecys.student_validation_report_owner(report.id)
        if not(valid_report_owner):
            session.flash = T('Selected report can\'t be edited. \
                Select a valid report.')
            redirect(URL('student','index'))
        ## Validate that the report status is editable (it is either 'Draft' or 'Recheck')
        if not(cpfecys.student_validation_report_status(report)):
            session.flash = T('Selected report can\'t be edited. \
                Is not in a editable state.')
            redirect(URL('student','index'))
        ## Validate that the administrator of DTT has not failed the student
        if report.dtt_approval is not None and report.dtt_approval==False:
            session.flash = T('Selected report can\'t be edited. \
                Select a valid report.')
            redirect(URL('student','index'))
        ## Markmin formatting of reports
        response.view = 'student/report_edit.html'
        assignation_reports = db(db.report.assignation == \
            report.assignation).select()
        # check minimun requirements
        reqs = db(db.area_report_requirement.area_level == \
            report.assignation.project.area_level).select()
        minimal_requirements = True
        

        #***********************************************************************************************************************
        #******************************************************PHASE 2 DTT******************************************************
        activities_count = db(db.log_entry.report == report.id).count()
        metrics_count = db(db.log_metrics.report == report.id).count()
        final_stats = db(db.log_final.report == report.id).count()


        activities_WM=None
        activities_M=None
        activities_F=None
        final_stats_flag=False
        #if (T(cpfecys.current_year_period().period.name) + ' ' +str(cpfecys.current_year_period().yearp)).upper()!='SEGUNDO SEMESTRE 2014':
        if report.assignation.project.area_level.name=='DTT Tutor Académico':
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
                                    if (((int(db((db.grades_log.activity_id == actTempo.id)&(db.grades_log.operation_log=='insert')&(db.grades_log.user_name==auth.user.username)).count())*100)/int(db(db.grades.activity == actTempo.id).count()))>=int(parameters_period.percentage_income_activity)):
                                        activities_M_Real.append(metric_statistics(actTempo,0,None))
                                else:
                                    #Future activities with metric
                                    activities_F.append(actTempo)
                            else:
                                #Check if you have the minimum of notes recorded in the activity amount that you are worth in the report
                                if (((int(db((db.grades_log.activity_id == actTempo.id)&(db.grades_log.operation_log=='insert')&(db.grades_log.user_name==auth.user.username)).count())*100)/int(db(db.grades.activity == actTempo.id).count()))>=int(parameters_period.percentage_income_activity)):
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
                                    if (((int(db((db.grades_log.activity_id == actTempo.id)&(db.grades_log.operation_log=='insert')&(db.grades_log.user_name==auth.user.username)).count())*100)/int(db(db.grades.activity == actTempo.id).count()))>=int(parameters_period.percentage_income_activity)):
                                        activities_M_Real.append(metric_statistics(actTempo,0,None))
                                else:
                                    #Future activities with metric
                                    activities_F.append(actTempo)
                            else:
                                #Check if you have the minimum of notes recorded in the activity amount that you are worth in the report
                                if (((int(db((db.grades_log.activity_id == actTempo.id)&(db.grades_log.operation_log=='insert')&(db.grades_log.user_name==auth.user.username)).count())*100)/int(db(db.grades.activity == actTempo.id).count()))>=int(parameters_period.percentage_income_activity)):
                                    activities_M_Real.append(metric_statistics(actTempo,0,None))
                        activities_M = activities_M_Real
                        #Complete with measuring future activities
                        if report.report_restriction.is_final==False:
                            activities_F_temp = db((db.course_activity.semester == cperiod.id)&(db.course_activity.assignation == report.assignation.project)&(db.course_activity.date_start >= endDateActivity)&(~db.course_activity.id.belongs(activitiesMBefore))).select()
                            for awmt in activities_F_temp:
                                activities_F.append(awmt)

            if db(db.course_report_exception.project==report.assignation.project).select().first() is not None:
                final_stats_flag=True

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

        activities_count = activities_count+len(activities_WM)+len(activities_M)
        metrics_count = metrics_count+len(activities_M)
        #***********************************************************************************************************************
        #******************************************************PHASE 2 DTT******************************************************

        

        for req in reqs:
            if (req.report_requirement.name == 'Registrar Estadisticas Finales de Curso') \
            and (report.report_restriction.is_final) \
            and (final_stats == 0):
                minimal_requirements = False
                break
            if (req.report_requirement.name == 'Encabezado') and (report.heading is None):
                minimal_requirements = False
                break
            if (req.report_requirement.name == 'Pie de Reporte') and (report.footer is None):
                minimal_requirements = False
                break
            if (req.report_requirement.name == 'Registrar Actividad') and (activities_count == 0):
                minimal_requirements = False
                break
            if (req.report_requirement.name == 'Registrar Actividad con Metricas') and (metrics_count == 0):
                minimal_requirements = False
                break
            if (req.report_requirement.name == 'Registrar Deserciones') and (report.desertion_started is None):
                minimal_requirements = False
                break
            if (req.report_requirement.name == 'Registrar Horas Completadas') and (report.hours is None):
                minimal_requirements = False
                break
        mandatory_requirements = ''
        for req in reqs:
            mandatory_requirements += req.report_requirement.name  + ', '


        return dict(log_types = db(db.log_type.id > 0).select(),
                    mandatory_requirements = mandatory_requirements,
                    minimal_requirements = minimal_requirements,
                    assignation_reports = assignation_reports,
                    logs = db((db.log_entry.report == report.id)).select(),
                    metrics = db((db.log_metrics.report == report.id)).select(),
                    final_r = db(db.log_final.report == report.id).select(),
                    metrics_type = db(db.metrics_type).select(),
                    anomalies = db((db.log_type.name == 'Anomaly')&
                                   (db.log_entry.log_type == db.log_type.id)&
                                   (db.log_entry.report == report.id)).count(),
                    markmin_settings = cpfecys.get_markmin,
                    report = report,
                    activities_WM=activities_WM,#Phase2 DTT
                    activities_M=activities_M,#Phase2 DTT
                    activities_F=activities_F,#Phase2 DTT
                    final_stats_flag=final_stats_flag)#Phase2 DTT
    elif (request.args(0) == 'acceptance'):
        #get the data & save the report
        report = request.vars['report']
        report = db.report(db.report.id == report)
        # Check minimun requirements
        reqs = db(db.area_report_requirement.area_level == report.assignation.project.area_level).select()
        minimal_requirements = True


        #***********************************************************************************************************************
        #******************************************************PHASE 2 DTT******************************************************
        activities_count = db(db.log_entry.report == report.id).count()
        metrics_count = db(db.log_metrics.report == report.id).count()
        final_stats = db(db.log_final.report == report.id).count()


        activities_WM=None
        activities_M=None
        activities_F=None
        final_stats_flag=False
        if report.assignation.project.area_level.name=='DTT Tutor Académico':
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
                                    if (((int(db((db.grades_log.activity_id == actTempo.id)&(db.grades_log.operation_log=='insert')&(db.grades_log.user_name==auth.user.username)).count())*100)/int(db(db.grades.activity == actTempo.id).count()))>=int(parameters_period.percentage_income_activity)):
                                        activities_M_Real.append(metric_statistics(actTempo,0,None))
                                else:
                                    #Future activities with metric
                                    activities_F.append(actTempo)
                            else:
                                #Check if you have the minimum of notes recorded in the activity amount that you are worth in the report
                                if (((int(db((db.grades_log.activity_id == actTempo.id)&(db.grades_log.operation_log=='insert')&(db.grades_log.user_name==auth.user.username)).count())*100)/int(db(db.grades.activity == actTempo.id).count()))>=int(parameters_period.percentage_income_activity)):
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
                                    if (((int(db((db.grades_log.activity_id == actTempo.id)&(db.grades_log.operation_log=='insert')&(db.grades_log.user_name==auth.user.username)).count())*100)/int(db(db.grades.activity == actTempo.id).count()))>=int(parameters_period.percentage_income_activity)):
                                        activities_M_Real.append(metric_statistics(actTempo,0,None))
                                else:
                                    #Future activities with metric
                                    activities_F.append(actTempo)
                            else:
                                #Check if you have the minimum of notes recorded in the activity amount that you are worth in the report
                                if (((int(db((db.grades_log.activity_id == actTempo.id)&(db.grades_log.operation_log=='insert')&(db.grades_log.user_name==auth.user.username)).count())*100)/int(db(db.grades.activity == actTempo.id).count()))>=int(parameters_period.percentage_income_activity)):
                                    activities_M_Real.append(metric_statistics(actTempo,0,None))
                        activities_M = activities_M_Real
                        #Complete with measuring future activities
                        if report.report_restriction.is_final==False:
                            activities_F_temp = db((db.course_activity.semester == cperiod.id)&(db.course_activity.assignation == report.assignation.project)&(db.course_activity.date_start >= endDateActivity)&(~db.course_activity.id.belongs(activitiesMBefore))).select()
                            for awmt in activities_F_temp:
                                activities_F.append(awmt)

            if db(db.course_report_exception.project==report.assignation.project).select().first() is not None:
                final_stats_flag=True

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

        activities_count = activities_count+len(activities_WM)+len(activities_M)
        metrics_count = metrics_count+len(activities_M)
        #***********************************************************************************************************************
        #******************************************************PHASE 2 DTT******************************************************


        for req in reqs:
            if (req.report_requirement.name == 'Registrar Estadisticas Finales de Curso') \
            and (report.report_restriction.is_final) \
            and (final_stats == 0):
                minimal_requirements = False
                break
            if (req.report_requirement.name == 'Encabezado') and \
                        (report.heading is None):
                minimal_requirements = False
                break
            if (req.report_requirement.name == 'Pie de Reporte') and \
                        (report.footer is None):
                minimal_requirements = False
                break
            if (req.report_requirement.name == 'Registrar Actividad') and \
                        (activities_count == 0):
                minimal_requirements = False
                break
            if (req.report_requirement.name == 'Registrar Actividad con Metricas') and \
                        (metrics_count == 0):
                minimal_requirements = False
                break
            if (req.report_requirement.name == 'Registrar Deserciones') and \
                        (report.desertion_started is None):
                minimal_requirements = False
                break
            if (req.report_requirement.name == 'Registrar Horas Completadas') and \
                        (report.hours is None):
                minimal_requirements = False
                break
        if not minimal_requirements:
            session.flash = T('Selected report can\'t be accepted, it lacks mandatory blocks.')
            redirect(URL('student','index'))
        # Validate DB report_restriction to obey TIMING rules
        import cpfecys
        #valid_rep_restr = cpfecys.student_validation_report_restrictions(report.report_restriction.id)
        ## Validate that the report status is editable (it is either 'Draft' or 'Recheck')
        if not(cpfecys.student_validation_report_status(report)):
            session.flash = T('Invalid selected assignation \
                                and report. Select a valid one.') + 'INV002'
            redirect(URL('student','index'))
        ## Validate assignation
        if cpfecys.assignation_is_locked(report.assignation):
            session.flash = T('Selected report can\'t be edited. Select a valid report.')
            redirect(URL('student','index'))
        # Validate assignation belongs to this user
        assign = db.user_project((db.user_project.id == report.assignation)&
                                (db.user_project.assigned_user == auth.user.id))
        valid_assignation = assign != None
        if not(report and valid_assignation):
            session.flash = T('Invalid selected assignation \
                                and report. Select a valid one.') + 'INV003'
            redirect(URL('student','index'))
        import datetime
        current_date = datetime.datetime.now()
        if(report.status.name=='Recheck'):
            import datetime
            dated = datetime.datetime.now().date()
            next_date = report.score_date + datetime.timedelta(
                            days=cpfecys.get_custom_parameters().rescore_max_days)
            if not(dated < next_date):
                session.flash = T('Selected report can\'t be edited. Select a valid report.')
                redirect(URL('student','index'))

        ## Validate that the administrator of DTT has not failed the student
        if report.dtt_approval is not None and report.dtt_approval==False:
            session.flash = T('Selected report can\'t be edited. \
                Select a valid report.')
            redirect(URL('student','index'))
            
        report.update_record(created = current_date,
                      status = db.report_status(name = 'Grading'))



        #***********************************************************************************************************************
        #******************************************************PHASE 2 DTT******************************************************
        if report.assignation.project.area_level.name=='DTT Tutor Académico':
            cperiod = obtainPeriodReport(report)
            for awm in activities_WM:
                db.log_entry.insert(log_type=temp_logType.id,
                                    entry_date=current_date,
                                    description='Nombre: "'+awm.name+'"      Descripción: "'+awm.description+'"',
                                    report=report.id,
                                    period=cperiod.id,
                                    tActivity='F',
                                    idActivity=awm.id
                                    )

            for awm in activities_M:
                db.log_entry.insert(log_type=temp_logType.id,
                                    entry_date=current_date,
                                    description=awm[1],
                                    report=report.id,
                                    period=cperiod.id,
                                    tActivity='T',
                                    idActivity=awm[17]
                                    )
                db.log_metrics.insert(description=awm[1],
                                        media=awm[2],
                                        error=awm[3],
                                        mediana=awm[4],
                                        moda=awm[5],
                                        desviacion=awm[6],
                                        varianza=awm[7],
                                        curtosis=awm[8],
                                        coeficiente=awm[9],
                                        rango=awm[10],
                                        minimo=awm[11],
                                        maximo=awm[12],
                                        total=awm[13],
                                        reprobados=awm[14],
                                        aprobados=awm[15],
                                        created=awm[0],
                                        report=report.id,
                                        metrics_type=awm[16]
                                    )
            for awm in activities_F:
                db.log_future.insert(entry_date=current_date,
                                    description='Nombre: "'+awm.name+'"      Descripción: "'+awm.description+'"',
                                    report=report.id,
                                    period=cperiod.id
                                    )
        #***********************************************************************************************************************
        #******************************************************PHASE 2 DTT******************************************************



        session.flash = T('Report sent to Grading.')
        # Notification Message
        import cpfecys
        signature = (cpfecys.get_custom_parameters().email_signature or '')
        me_the_user = db.auth_user(db.auth_user.id == auth.user.id)
        message = '<html>' + T('The report') + ' ' \
        + '<b>' + XML(report.report_restriction['name']) + '</b><br/>' \
        + T('sent by student: ') + XML(me_the_user.username) + ' ' \
        + XML(me_the_user.first_name) + ' ' + XML(me_the_user.last_name) \
        + '<br/>' \
        + T('was sent to be checked.') + '<br/>' + T('Checking can be done in:') \
        + ' ' + cpfecys.get_domain() + '<br />' + signature + '</html>'
        # send mail to teacher and student notifying change.
        mails = []
        # retrieve teacher's email
        teachers = db((db.project.id == assign.project)&
                      (db.user_project.project == db.project.id)&
                      (db.user_project.assigned_user == db.auth_user.id)&
                      (db.auth_membership.user_id == db.auth_user.id)&
                      (db.auth_membership.group_id == db.auth_group.id)&
                      (db.auth_group.role == 'Teacher')).select()
        for teacher in teachers:
            mails.append(teacher.auth_user.email)
        # retrieve student's email
        student_mail = me_the_user.email
        mails.append(student_mail)
        was_sent = mail.send(to=mails,
                  subject=T('[DTT]Automatic Notification - Report ready to be checked.'),
                  # If reply_to is omitted, then mail.settings.sender is used
                  reply_to = student_mail,
                  message=message)
        #MAILER LOG
        db.mailer_log.insert(sent_message = message,
                             destination = ','.join(mails),
                             result_log = str(mail.error or '') + ':' + str(mail.result),
                             success = was_sent)
        redirect(URL('student','index'))
    elif (request.args(0) == 'view'):
        #Get the report id
        report = request.vars['report']
        # Validate that the report exists
        report = db.report(db.report.id == report)
        valid = not(report is None)
        ## Validate assignation
        import cpfecys
        if valid: valid = not cpfecys.assignation_is_locked(report.assignation)
        # Validate that the report belongs to user
        if valid: valid = cpfecys.student_validation_report_owner(report.id)
        if valid:
            semester = cpfecys.first_period.id
            if report.created.month >= 7:
                semester = cpfecys.second_period.id

            period = db((db.period_year.yearp==int(report.created.year))&
                (db.period_year.period==semester)).select().first()
            teacher = db(
                        (db.auth_user.id==db.user_project.assigned_user)&
                        (db.auth_user.id==db.auth_membership.user_id)&
                        (db.auth_membership.group_id==db.auth_group.id)&
                        (db.auth_group.role=='Teacher')&
                        (db.user_project.project==report.assignation.project)&
                        (db.user_project.period==db.period_year.id)&
                        ((db.user_project.period <= period.id)&
                       ((db.user_project.period + db.user_project.periods) > \
                        period.id))
                        ).select(db.auth_user.ALL).first()
            student = db(db.auth_user.id==auth.user.id).select().first()
            response.view = 'student/report_view.html'
            assignation_reports = db(db.report.assignation == report.assignation).select()

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
                                        if (((int(db((db.grades_log.activity_id == actTempo.id)&(db.grades_log.operation_log=='insert')&(db.grades_log.user_name==auth.user.username)).count())*100)/int(db(db.grades.activity == actTempo.id).count()))>=int(parameters_period.percentage_income_activity)):
                                            activities_M_Real.append(metric_statistics(actTempo,0,None))
                                    else:
                                        #Future activities with metric
                                        activities_F.append(actTempo)
                                else:
                                    #Check if you have the minimum of notes recorded in the activity amount that you are worth in the report
                                    if (((int(db((db.grades_log.activity_id == actTempo.id)&(db.grades_log.operation_log=='insert')&(db.grades_log.user_name==auth.user.username)).count())*100)/int(db(db.grades.activity == actTempo.id).count()))>=int(parameters_period.percentage_income_activity)):
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
                                        if (((int(db((db.grades_log.activity_id == actTempo.id)&(db.grades_log.operation_log=='insert')&(db.grades_log.user_name==auth.user.username)).count())*100)/int(db(db.grades.activity == actTempo.id).count()))>=int(parameters_period.percentage_income_activity)):
                                            activities_M_Real.append(metric_statistics(actTempo,0,None))
                                    else:
                                        #Future activities with metric
                                        activities_F.append(actTempo)
                                else:
                                    #Check if you have the minimum of notes recorded in the activity amount that you are worth in the report
                                    if (((int(db((db.grades_log.activity_id == actTempo.id)&(db.grades_log.operation_log=='insert')&(db.grades_log.user_name==auth.user.username)).count())*100)/int(db(db.grades.activity == actTempo.id).count()))>=int(parameters_period.percentage_income_activity)):
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
            return dict(log_types = db(db.log_type.id > 0).select(),
                        assignation_reports = assignation_reports,
                        logs = db((db.log_entry.report == report.id)).select(),
                        activities_WM=activities_WM,
                        metrics = db((db.log_metrics.report == report.id)).select(),
                        activities_M=activities_M,
                        final_r = db(db.log_final.report == report.id).select(),
                        anomalies = db((db.log_type.name == 'Anomaly')&
                                   (db.log_entry.log_type == db.log_type.id)&
                                   (db.log_entry.report == report.id)).count(),
                        activities_F=activities_F,
                        markmin_settings = cpfecys.get_markmin,
                        report = report,
                        student = student,
                        teacher = teacher)
        else:
            session.flash = T('Selected report can\'t be viewed. Select a valid report.')
            redirect(URL('student', 'index'))
    else:
        redirect(URL('student', 'index'))
    raise HTTP(404)

@auth.requires_login()
@auth.requires_membership('Student')
def log_future():
    if (request.args(0) == 'save'):
        # validate the user owns this report
        report = request.vars['report']
        report = db.report(db.report.id == report)
        valid_report = report != None
        ## Validate assignation
        if valid_report: valid_report = not cpfecys.assignation_is_locked(report.assignation)
        if valid_report: valid_report = cpfecys.student_validation_report_owner(report.id)
        # validate report is editable
        #if valid_report: valid_report = cpfecys.student_validation_report_restrictions \
        #    (report.report_restriction)
        # validate report is 'Draft' or 'Recheck'
        if valid_report: valid_report = cpfecys.student_validation_report_status(report)
        # validate we receive log-date, log-type, log-content
        log_date = request.vars['log-date']
        log_content = request.vars['log-content']
        if valid_report: valid_report = (log_date and log_content)
        if valid_report:
            db.log_future.insert(entry_date = log_date,
                                description = log_content,
                                report = report.id,
                                period=cpfecys.current_year_period())
            session.flash = T('Log added')
            redirect(URL('student', 'report/edit', vars=dict(report=report.id)))
        else:
            session.flash = T('Operation not allowed.')
            redirect(URL('student', 'index'))
    elif (request.args(0) == 'update'):
        # validate the requested log
        log = request.vars['log']
        log = db.log_future(db.log_future.id == log)
        valid_log = log != None
        # validate log report owner is valid
        if valid_log: valid_log = cpfecys.student_validation_report_owner(log.report)
        ## Validate assignation
        if valid_log: valid_log = not cpfecys.assignation_is_locked(log.report.assignation)
        # validate report is editable
        #if valid_log: valid_log = cpfecys.student_validation_report_restrictions \
        #    (log.report['report_restriction'])
        # validate report is 'Draft' or 'Recheck'
        if valid_log: valid_log = cpfecys.student_validation_report_status \
            (db.report(db.report.id == log.report))
        # validate we receive log-date, log-type, log-content
        log_date = request.vars['log-date']
        log_content = request.vars['log-content']
        if valid_log: valid_log = (log_date and log_content)
        if valid_log:
            log.update_record(entry_date = log_date,
                              description = log_content)
            session.flash = T('Log Updated')
            redirect(URL('student', 'report/edit', vars=dict(report=log.report)))
        else:
            session.flash = T('Operation not allowed.')
            redirect(URL('student', 'index'))
    elif (request.args(0) == 'delete'):
        # validate the requested log
        log = request.vars['log']
        log = db.log_future(db.log_future.id == log)
        valid_log = log != None
        # validate log report owner is valid
        if valid_log: valid_log = cpfecys.student_validation_report_owner(log.report)
        ## Validate assignation
        if valid_log: valid_log = not cpfecys.assignation_is_locked(log.report.assignation)
        # validate report is editable
        #if valid_log: valid_log = cpfecys.student_validation_report_restrictions \
        #    (log.report['report_restriction'])
        # validate report is 'Draft' or 'Recheck'
        if valid_log: valid_log = cpfecys.student_validation_report_status \
            (db.report(db.report.id == log.report))
        if valid_log:
            log.delete_record()
            session.flash = T('Log Deleted')
            redirect(URL('student', 'report/edit', vars=dict(report=log.report)))
        else:
            session.flash = T('Operation not allowed.')
            redirect(URL('student', 'index'))
    raise HTTP(404)

@auth.requires_login()
@auth.requires_membership('Student')
def log():
    if (request.args(0) == 'save'):
        # validate the user owns this report
        report = request.vars['report']
        report = db.report(db.report.id == report)
        valid_report = report != None
        ## Validate assignation
        if valid_report: valid_report = not cpfecys.assignation_is_locked(report.assignation)
        if valid_report: valid_report = cpfecys.student_validation_report_owner(report.id)
        # validate report is editable
        #if valid_report: valid_report = cpfecys.student_validation_report_restrictions \
        #    (report.report_restriction)
        # validate report is 'Draft' or 'Recheck'
        if valid_report: valid_report = cpfecys.student_validation_report_status(report)
        # validate we receive log-date, log-type, log-content
        log_type = request.vars['log-type']
        log_date = request.vars['log-date']
        log_content = request.vars['log-content']
        if valid_report: valid_report = (log_type and log_date and log_content)
        if valid_report:
            db.log_entry.insert(log_type = log_type,
                                entry_date = log_date,
                                description = log_content,
                                report = report.id,
                                period=cpfecys.current_year_period())
            session.flash = T('Log added')
            redirect(URL('student', 'report/edit', vars=dict(report=report.id)))
        else:
            session.flash = T('Operation not allowed.')
            redirect(URL('student', 'index'))
    elif (request.args(0) == 'update'):
        # validate the requested log
        log = request.vars['log']
        log = db.log_entry(db.log_entry.id == log)
        valid_log = log != None
        # validate log report owner is valid
        if valid_log: valid_log = cpfecys.student_validation_report_owner(log.report)
        ## Validate assignation
        if valid_log: valid_log = not cpfecys.assignation_is_locked(log.report.assignation)
        # validate report is editable
        #if valid_log: valid_log = cpfecys.student_validation_report_restrictions \
        #    (log.report['report_restriction'])
        # validate report is 'Draft' or 'Recheck'
        if valid_log: valid_log = cpfecys.student_validation_report_status \
            (db.report(db.report.id == log.report))
        # validate we receive log-date, log-type, log-content
        log_type = request.vars['log-type']
        log_date = request.vars['log-date']
        log_content = request.vars['log-content']
        if valid_log: valid_log = (log_type and log_date and log_content)
        if valid_log:
            log.update_record(log_type = log_type,
                              entry_date = log_date,
                              description = log_content)
            session.flash = T('Log Updated')
            redirect(URL('student', 'report/edit', vars=dict(report=log.report)))
        else:
            session.flash = T('Operation not allowed.')
            redirect(URL('student', 'index'))
    elif (request.args(0) == 'delete'):
        # validate the requested log
        log = request.vars['log']
        log = db.log_entry(db.log_entry.id == log)
        valid_log = log != None
        # validate log report owner is valid
        if valid_log: valid_log = cpfecys.student_validation_report_owner(log.report)
        ## Validate assignation
        if valid_log: valid_log = not cpfecys.assignation_is_locked(log.report.assignation)
        # validate report is editable
        #if valid_log: valid_log = cpfecys.student_validation_report_restrictions \
        #    (log.report['report_restriction'])
        # validate report is 'Draft' or 'Recheck'
        if valid_log: valid_log = cpfecys.student_validation_report_status \
            (db.report(db.report.id == log.report))
        if valid_log:
            log.delete_record()
            session.flash = T('Log Deleted')
            redirect(URL('student', 'report/edit', vars=dict(report=log.report)))
        else:
            session.flash = T('Operation not allowed.')
            redirect(URL('student', 'index'))
    raise HTTP(404)


@auth.requires_login()
@auth.requires_membership('Student')
def metrics():
    import datetime
    cdate = datetime.datetime.now()
    if (request.args(0) == 'save'):
        # validate the user owns this report
        report = request.vars['report']
        report = db.report(db.report.id == report)
        valid_report = report != None
        ## Validate assignation
        if valid_report: valid_report = not cpfecys.assignation_is_locked(report.assignation)
        if valid_report: valid_report = cpfecys.student_validation_report_owner(report.id)
        # validate report is editable
        #if valid_report: valid_report = cpfecys.student_validation_report_restrictions \
        #    (report.report_restriction)
        # validate report is 'Draft' or 'Recheck'
        if valid_report: valid_report = cpfecys.student_validation_report_status(report)
        # validate we receive log-date, log-type, log-content
        description = request.vars['description']
        media = request.vars['media-metrics']
        error_tipico = request.vars['error-tipico-metrics']
        mediana = request.vars['mediana-metrics']
        moda = request.vars['moda-metrics']
        desviacion_estandar = request.vars['desviacion-estandar-metrics']
        varianza = request.vars['varianza-metrics']
        curtosis = request.vars['curtosis-metrics']
        coeficiente = request.vars['coeficiente-metrics']
        rango = request.vars['rango-metrics']
        minimo = request.vars['minimo-metrics']
        maximo = request.vars['maximo-metrics']
        total = request.vars['total-metrics']
        reprobados = request.vars['reprobados-metrics']
        aprobados = request.vars['aprobados-metrics']
        metric_type = request.vars['metric-type']
        log_date = request.vars['log-date']

        if valid_report: valid_report = (media and error_tipico and mediana \
                                         and moda and desviacion_estandar  
                                         and varianza and curtosis \
                                         and coeficiente and rango \
                                         and minimo and maximo and total \
                                         and reprobados and aprobados \
                                         and metric_type and log_date
                                         and description)

        if valid_report:
            db.log_metrics.insert(report = report.id,
                                  description = description,
                                media = media,
                                error = error_tipico,
                                mediana = mediana,
                                moda = moda,
                                desviacion = desviacion_estandar,
                                varianza = varianza,
                                curtosis = curtosis,
                                coeficiente = coeficiente,
                                rango = rango,
                                minimo = minimo,
                                maximo = maximo,
                                total = total,
                                reprobados = reprobados,
                                aprobados = aprobados,
                                created = log_date,
                                metrics_type = metric_type)
            session.flash = T('Log added')
            redirect(URL('student', 'report/edit', vars=dict(report=report.id)))
        else:
            session.flash = T('Operation not allowed.')
            redirect(URL('student', 'index'))
    elif (request.args(0) == 'update'):
        # validate the requested metric
        metric = request.vars['metric']
        metric = db.log_metrics(db.log_metrics.id == metric)
        valid_metric = metric != None
        ## Validate assignation
        if valid_metric: valid_metric = not cpfecys.assignation_is_locked(metric.report.assignation)
        # validate metric report owner is valid
        if valid_metric: valid_metric = cpfecys.student_validation_report_owner(metric.report)
        # validate report is editable
        #if valid_metric: valid_metric = cpfecys.student_validation_report_restrictions \
        #    (metric.report['report_restriction'])
        # validate report is 'Draft' or 'Recheck'
        if valid_metric: valid_metric = cpfecys.student_validation_report_status \
            (db.report(db.report.id == metric.report))
        # validate we receive log-date, log-type, log-content
        description = request.vars['description']
        media = request.vars['media-metrics']
        error_tipico = request.vars['error-tipico-metrics']
        mediana = request.vars['mediana-metrics']
        moda = request.vars['moda-metrics']
        desviacion_estandar = request.vars['desviacion-estandar-metrics']
        varianza = request.vars['varianza-metrics']
        curtosis = request.vars['curtosis-metrics']
        coeficiente = request.vars['coeficiente-metrics']
        rango = request.vars['rango-metrics']
        minimo = request.vars['minimo-metrics']
        maximo = request.vars['maximo-metrics']
        total = request.vars['total-metrics']
        reprobados = request.vars['reprobados-metrics']
        aprobados = request.vars['aprobados-metrics']
        metric_type = request.vars['metric-type']
        log_date = request.vars['log-date']
        if valid_metric: valid_metric = (media and error_tipico and mediana \
                                         and moda and desviacion_estandar \
                                         and varianza and curtosis \
                                         and coeficiente and rango \
                                         and minimo and maximo and total \
                                         and reprobados and aprobados \
                                         and metric_type and log_date and description)
        if valid_metric:
            metric.update_record(report = metric.report.id,
                                 description = description,
                                media = media,
                                error = error_tipico,
                                mediana = mediana,
                                moda = moda,
                                desviacion = desviacion_estandar,
                                varianza = varianza,
                                curtosis = curtosis,
                                coeficiente = coeficiente,
                                rango = rango,
                                minimo = minimo,
                                maximo = maximo,
                                total = total,
                                reprobados = reprobados,
                                aprobados = aprobados,
                                created = log_date,
                                metrics_type = metric_type)
            session.flash = T('Metric Updated')
            redirect(URL('student', 'report/edit', vars=dict(report=metric.report)))
        else:
            session.flash = T('Operation not allowed.')
            redirect(URL('student', 'index'))
    elif (request.args(0) == 'delete'):
        # validate the requested metric
        metric = request.vars['metric']
        metric = db.log_metrics(db.log_metrics.id == metric)
        valid_metric = metric != None
        ## Validate assignation
        if valid_metric: valid_metric = not cpfecys.assignation_is_locked(metric.report.assignation)
        # validate metric report owner is valid
        if valid_metric: valid_metric = cpfecys.student_validation_report_owner(metric.report)
        # validate report is editable
        #if valid_metric: valid_metric = cpfecys.student_validation_report_restrictions \
        #    (metric.report['report_restriction'])
        # validate report is 'Draft' or 'Recheck'
        if valid_metric: valid_metric = cpfecys.student_validation_report_status \
            (db.report(db.report.id == metric.report))
        if valid_metric:
            metric.delete_record()
            session.flash = T('Log Deleted')
            redirect(URL('student', 'report/edit', vars=dict(report=metric.report)))
        else:
            session.flash = T('Operation not allowed.')
            redirect(URL('student', 'index'))
    raise HTTP(404)

@auth.requires_login()
@auth.requires_membership('Student')
def desertions():
    if (request.args(0) == 'save'):
        # validate the user owns this report
        report = request.vars['report']
        report = db.report(db.report.id == report)
        valid_report = report != None
        ## Validate assignation
        if valid_report: valid_report = not cpfecys.assignation_is_locked(report.assignation)
        if valid_report: valid_report = cpfecys.student_validation_report_owner(report.id)
        # validate report is editable
        #if valid_report: valid_report = cpfecys.student_validation_report_restrictions \
        #    (report.report_restriction)
        # validate report is 'Draft' or 'Recheck'
        if valid_report: valid_report = cpfecys.student_validation_report_status(report)
        # validate we receive log-date, log-type, log-content
        desertion_started = request.vars['desertion-started']
        desertion_gone = request.vars['desertion-gone']
        desertion_continued = request.vars['desertion-continued']
        if valid_report: valid_report = (desertion_started and desertion_gone
                                         and desertion_continued)
        if valid_report:
            report.desertion_started = desertion_started
            report.desertion_gone = desertion_gone
            report.desertion_continued = desertion_continued
            report.update_record()
            session.flash = T('Desertion log added')
            redirect(URL('student', 'report/edit', vars=dict(report=report.id)))
        else:
            session.flash = T('Operation not allowed.')
            redirect(URL('student', 'index'))
    elif (request.args(0) == 'update'):
        # validate the user owns this report
        report = request.vars['report']
        report = db.report(db.report.id == report)
        valid_report = report != None
        ## Validate assignation
        if valid_report: valid_report = not cpfecys.assignation_is_locked(report.assignation)
        if valid_report: valid_report = cpfecys.student_validation_report_owner(report.id)
        # validate report is editable
        #if valid_report: valid_report = cpfecys.student_validation_report_restrictions \
        #    (report.report_restriction)
        # validate report is 'Draft' or 'Recheck'
        if valid_report: valid_report = cpfecys.student_validation_report_status(report)
        # validate we receive log-date, log-type, log-content
        desertion_started = request.vars['desertion-started']
        desertion_gone = request.vars['desertion-gone']
        desertion_continued = request.vars['desertion-continued']
        if valid_report: valid_report = (desertion_started and desertion_gone
                                         and desertion_continued)
        if valid_report:
            report.desertion_started = desertion_started
            report.desertion_gone = desertion_gone
            report.desertion_continued = desertion_continued
            report.update_record()
            session.flash = T('Desertion log updated')
            redirect(URL('student', 'report/edit', vars=dict(report=report.id)))
        else:
            session.flash = T('Operation not allowed.')
            redirect(URL('student', 'index'))
    elif (request.args(0) == 'delete'):
        # validate the user owns this report
        report = request.vars['report']
        report = db.report(db.report.id == report)
        valid_report = report != None
        ## Validate assignation
        if valid_report: valid_report = not cpfecys.assignation_is_locked(report.assignation)
        if valid_report: valid_report = cpfecys.student_validation_report_owner(report.id)
        # validate report is editable
        #if valid_report: valid_report = cpfecys.student_validation_report_restrictions \
        #    (report.report_restriction)
        # validate report is 'Draft' or 'Recheck'
        if valid_report: valid_report = cpfecys.student_validation_report_status(report)
        # validate we receive log-date, log-type, log-content
        desertion_started = request.vars['desertion-started']
        desertion_gone = request.vars['desertion-gone']
        desertion_continued = request.vars['desertion-continued']
        if valid_report: valid_report = (desertion_started and desertion_gone
                                         and desertion_continued)
        if valid_report:
            report.desertion_started = None
            report.desertion_gone = None
            report.desertion_continued = None
            report.update_record()
            session.flash = T('Desertion log removed')
            redirect(URL('student', 'report/edit', vars=dict(report=report.id)))
        else:
            session.flash = T('Operation not allowed.')
            redirect(URL('student', 'index'))
    raise HTTP(404)
