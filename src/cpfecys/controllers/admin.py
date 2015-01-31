#***********************************************************************************************************************
#******************************************************PHASE 2 DTT******************************************************
def obtainPeriodReport(report):
    #Get the minimum and maximum date of the report
    tmp_period=1
    tmp_year=report.report_restriction.start_date.year
    if report.report_restriction.start_date.month >= 6:
        tmp_period=2
    return db((db.period_year.yearp==tmp_year)&(db.period_year.period==tmp_period)).select().first()


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


def activities_report_tutor(report):
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
                if activities_M_Real is None:
                    activities_M_Real=[]
                activities_M_Real.append(metric_statistics(report,1,None))


            #students_second_recovery
            try:
                srt = int(db((db.course_second_recovery_test.semester==cperiod.id)&(db.course_second_recovery_test.project==report.assignation.project)).count())
            except:
                srt = int(0)
            if srt>0:
                if activities_M_Real is None:
                    activities_M_Real=[]
                activities_M_Real.append(metric_statistics(report,2,None))

    if activities_M is None:
        activities_M=[]
    if activities_WM is None:
        activities_WM=[]
    if activities_F is None:
        activities_F=[]
    return dict(activities_F=activities_F, activities_WM=activities_WM, activities_M=activities_M)


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



@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def course_report_exception():
    query = db.course_report_exception
    grid = SQLFORM.grid(query, maxtextlength=100,csv=False)
    return dict(grid=grid)
#***********************************************************************************************************************
#******************************************************PHASE 2 DTT******************************************************

# coding: utf8
# intente algo como

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def scheduler_activity():
    auto_daily()
    return dict(data = db3(db3.scheduler_run.id>0).select())

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def dtt_general_approval():
    from datetime import datetime
    cperiod = cpfecys.current_year_period()
    year = str(cperiod.yearp)
    if cperiod.period == 1:
        start = datetime.strptime(year + '-01-01', "%Y-%m-%d")
        end = datetime.strptime(year + '-06-01', "%Y-%m-%d")
    else:
        start = datetime.strptime(year + '-06-01', "%Y-%m-%d")
        end = datetime.strptime(year + '-12-31', "%Y-%m-%d")
    status = request.vars['status']
    period = request.vars['period']
    approve = request.vars['approve']
    # Get the coincident reports
    if status == 'None':
        reports = db((db.report.created>start)&
                     (db.report.created<end)).select()
        for report in reports:
            entries = count_log_entries(report)
            metrics = count_metrics_report(report)
            anomalies = count_anomalies(report)[0]['COUNT(log_entry.id)']
            if entries != 0 or metrics!= 0 or anomalies != 0:
                report.update_record(dtt_approval = approve)
    elif int(status) == -1:
        reports = db((db.report.created>start)&
            (db.report.created<end)&
            (db.report.score>=db.report.min_score)&
            (db.report.min_score!=None)&
            (db.report.min_score!=0)).select()
        for report in reports:
            entries = count_log_entries(report)
            metrics = count_metrics_report(report)
            anomalies = count_anomalies(report)[0]['COUNT(log_entry.id)']
            if entries != 0 or metrics!= 0 or anomalies != 0:
                report.update_record(dtt_approval = approve)
    else:
        reports = db((db.report.created>start)&
            (db.report.created<end)&
            (db.report.status==status)).select()
        for report in reports:
            entries = count_log_entries(report)
            metrics = count_metrics_report(report)
            anomalies = count_anomalies(report)[0]['COUNT(log_entry.id)']
            if entries != 0 or metrics!= 0 or anomalies != 0:
                report.update_record(dtt_approval = approve)
    if request.env.http_referer is None:
        redirect(URL('admin','report_filter'))
    else:
        redirect(request.env.http_referer)
    return

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def roles():
    grid = SQLFORM.smartgrid(
        db.auth_group, linked_tables=['auth_membership'])
    return dict(grid=grid)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def general_report():
    period = cpfecys.current_year_period()
    if request.vars['period'] != None:
        period = request.vars['period']
        period = db(db.period_year.id==period).select().first()
        if not period:
            session.flash = T('Not valid Action.')
            redirect(URL('default', 'index'))
    periods = db(db.period_year).select()
    areas = db(db.area_level).select()
    def get_projects(area):
        projects = db(db.project.area_level==area).select()
        return projects
    def get_teacher(project):
        assignations = get_assignations(project, period, 'Teacher' \
                ).select(db.user_project.ALL)
        return assignations
    def get_final_report(project_id,period):
        from datetime import datetime
        log_final = None
        parcial_1 = None
        parcial_2 = None
        parcial_3 = None
        cperiod = period
        year = str(cperiod.yearp)
        start = datetime.strptime(year + '-06-01', "%Y-%m-%d")
        end = datetime.strptime(year + '-12-31', "%Y-%m-%d")
        if cperiod.period == 1:
            start = datetime.strptime(year + '-01-01', "%Y-%m-%d")
            end = datetime.strptime(year + '-06-01', "%Y-%m-%d")

        final_report = db((db.report.created>start)&
                     (db.report.created<end)&
                     ((db.report_restriction.is_enabled!=None) &
                        (db.report_restriction.is_enabled!=False))&
                     (db.report.assignation==db.user_project.id)&
                     (db.user_project.project==project_id)&
                     (db.report.report_restriction==db.report_restriction.id)&
                     ((db.report_restriction.is_final!=None)&
                        (db.report_restriction.is_final!=False))
                      ).select(db.report.ALL).first()

        project_reports = db((db.report.created>start)&
                     (db.report.created<end)&
                     ((db.report_restriction.is_enabled!=None) &
                        (db.report_restriction.is_enabled!=False))&
                     (db.report.assignation==db.user_project.id)&
                     (db.user_project.project==project_id)
                      )._select(db.report.id)
        parcial_1 = db((db.log_metrics.metrics_type== \
                        db.metrics_type(name='PRIMER PARCIAL'))&
                        (db.log_metrics.report.belongs(project_reports))
                        ).select(db.log_metrics.ALL).first()
        parcial_2 = db((db.log_metrics.metrics_type== \
                        db.metrics_type(name='SEGUNDO PARCIAL'))&
                        (db.log_metrics.report.belongs(project_reports))
                        ).select(db.log_metrics.ALL).first()
        parcial_3 = db((db.log_metrics.metrics_type== \
                        db.metrics_type(name='TERCER PARCIAL'))&
                        (db.log_metrics.report.belongs(project_reports))
                        ).select(db.log_metrics.ALL).first()
        final = db((db.log_metrics.metrics_type== \
                        db.metrics_type(name='EXAMEN FINAL'))&
                        (db.log_metrics.report.belongs(project_reports))
                        ).select(db.log_metrics.ALL).first()
        primera_r = db((db.log_metrics.metrics_type== \
                        db.metrics_type(name='PRIMERA RETRASADA'))&
                        (db.log_metrics.report.belongs(project_reports))
                        ).select(db.log_metrics.ALL).first()
        segunda_r = db((db.log_metrics.metrics_type== \
                        db.metrics_type(name='SEGUNDA RETRASADA'))&
                        (db.log_metrics.report.belongs(project_reports))
                        ).select(db.log_metrics.ALL).first()
        if final_report != None:
            log_final = db(db.log_final.report== \
                final_report.id).select().first()
        return final_report, log_final, parcial_1, parcial_2, parcial_3, \
                final, primera_r, segunda_r
    periods = db(db.period_year).select()
    return dict(areas=areas, get_projects=get_projects, 
        get_teacher=get_teacher,get_final_report=get_final_report,
        actual_period=period, periods=periods)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def count_log_entries(report):
    #***********************************************************************************************************************
    #******************************************************PHASE 2 DTT******************************************************
    if report.assignation.project.area_level.name=='DTT Tutor Académico' and (report.status.name=='Draft' or report.status.name=='Recheck'):
        activitiesTutor = activities_report_tutor(report)
        log_entries=len(activitiesTutor['activities_WM'])+len(activitiesTutor['activities_M'])
    else:
        log_entries = db((db.log_entry.report==report.id)).select(db.log_entry.id.count())[0]['COUNT(log_entry.id)']
    return log_entries
    #***********************************************************************************************************************
    #******************************************************PHASE 2 DTT******************************************************

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def count_metrics_report(report):
    #***********************************************************************************************************************
    #******************************************************PHASE 2 DTT******************************************************
    if report.assignation.project.area_level.name=='DTT Tutor Académico' and (report.status.name=='Draft' or report.status.name=='Recheck'):
        activitiesTutor = activities_report_tutor(report)
        log_metrics=len(activitiesTutor['activities_M'])
    else:
        log_metrics = db((db.log_metrics.report== report.id)).select(db.log_metrics.id.count())[0]['COUNT(log_metrics.id)']
    return log_metrics
    #***********************************************************************************************************************
    #******************************************************PHASE 2 DTT******************************************************

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def count_anomalies(report):
    log_entries = db((db.log_entry.report== \
        report)&
    (db.log_entry.log_type==db.log_type(name='Anomaly')) \
    ).select(db.log_entry.id.count())
    return log_entries

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def delivered():
    periods = db(db.period_year).select()
    period = cpfecys.current_year_period()
    area_list = []
    if request.vars['period'] != None:
        period = request.vars['period']
        period = db.period_year(db.period_year.id==period)
    admin = False
    restrictions = db(
       (db.item_restriction.item_type==db.item_type(name='Activity'))& \
       ((db.item_restriction.period==period.id) |
        ((db.item_restriction.permanent==True)&
            (db.item_restriction.period <= period.id)))&
        (db.item_restriction.is_enabled==True)).select()| \
    db((db.item_restriction.item_type==db.item_type(name='Grade Activity'))& \
       ((db.item_restriction.period==period.id) |
        ((db.item_restriction.permanent==True)&
            (db.item_restriction.period <= period.id)))&
        (db.item_restriction.is_enabled==True)).select()
    def calculate_by_restriction(restriction):
        pending = 0
        graded = 0
        total = 0
        approved = 0
        failed = 0
        restriction_instance = db(
           (db.item_restriction.item_type==db.item_type(name='Activity'))& \
           (db.item_restriction.id==restriction)&
           (db.item_restriction.is_enabled==True)).select() | \
            db((db.item_restriction.item_type==db.item_type( \
                name='Grade Activity'))& \
           (db.item_restriction.id==restriction)&
           (db.item_restriction.is_enabled==True)
                ).select(db.item_restriction.ALL)

        areas = db((db.item_restriction_area.item_restriction== \
            restriction_instance[0].id)&
            (db.area_level.id==db.item_restriction_area.area_level)
                ).select(db.area_level.ALL)
        for area in areas:
            area_list.append(area.id)
        projects = db((db.project.area_level==db.area_level.id)&
         (db.item_restriction.id==restriction)&
         (db.item_restriction_area.area_level.belongs(area_list))&
         (db.item_restriction_area.item_restriction==restriction)&
         (db.item_restriction_area.item_restriction==db.item_restriction.id)&
         (db.item_restriction_area.area_level==db.area_level.id)&
         (db.item_restriction_area.is_enabled==True)).select(db.project.ALL)

        for project in projects:
            exception = db((db.item_restriction_exception.project== \
                project.id)&
                (db.item_restriction_exception.item_restriction== \
                restriction))
            if exception.count() == 0:
                assignations = db(
                    (db.auth_user.id==db.user_project.assigned_user)&
                    (db.auth_user.id==db.auth_membership.user_id)&
                    (db.auth_membership.group_id==db.auth_group.id)&
                    (db.auth_group.role=='Student')&
                    (db.user_project.project==project.id)&
                    (db.user_project.period == db.period_year.id)&
                    ((db.user_project.period <= period.id)&
                 ((db.user_project.period + db.user_project.periods) > \
                  period.id))
                    ).select(db.user_project.ALL)
                for assignation in assignations:
                    item = db((db.item.assignation==assignation.id)&
                     (db.item.item_restriction==restriction)&
                     (db.item.item_restriction==db.item_restriction.id)&
                     (db.item_restriction.is_enabled==True)&
                     (db.item.is_active==True)&
                     (db.item.created==period.id)).select(db.item.ALL).first()
                    if item == None:
                        pending += 1
                        total += 1
                    elif item.item_restriction.item_type.name=='Grade Activity':
                        if item.min_score == None:
                            pending += 1
                            total += 1
                        elif item.score >= item.min_score:
                            graded += 1
                            approved += 1
                            total += 1
                    elif item.item_restriction.item_type.name=='Activity':
                        if item.done_activity == None:
                            pending += 1
                            total += 1
                        elif item.done_activity == True:
                            graded += 1
                            approved += 1
                            total += 1
                        elif item.done_activity == False:
                            graded += 1
                            failed += 1
                            total += 1
        return pending, graded, total, approved, failed
    return dict(restrictions=restrictions, periods=periods,
        calculate_by_restriction=calculate_by_restriction,
        period=period)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def dtt_approval():
    # get report id
    report = request.vars['report']
    # get the approval value
    approve = request.vars['approve']
    # get the report
    report = db.report(id = report)
    # toggle report dtt_approval flag
    report.dtt_approval = approve
    report.update_record()
    if request.env.http_referer is None:
        redirect(URL('admin','report_filter'))
    else:
        redirect(request.env.http_referer)
    return

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def assignation_freeze():
    grid = SQLFORM.grid(db.assignation_freeze)
    return dict(grid = grid)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def assignation_ignore_toggle():
    # get assignation id
    assignation = request.vars['id']
    # get the assignation
    assignation = db.user_project(id = assignation)
    # toggle assignation_ignored flag
    assignation.assignation_ignored = not assignation.assignation_ignored
    assignation.update_record()
    if request.env.http_referer:
        redirect(request.env.http_referer)
    else:
        redirect(URL('admin','assignations'))
    return

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def force_assignation_active():
    # get assignation id
    assignation = request.vars['id']
    # get assignation comment
    comment = request.vars['comment']
    # get the assignation
    assignation = db.user_project(id = assignation)
    # set the assignation as active
    assignation.assignation_status = None
    assignation.assignation_status_comment = comment
    assignation.update_record()
    if request.env.http_referer:
        redirect(request.env.http_referer)
    else:
        redirect(URL('admin','assignations'))
    return

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def force_assignation_failed():
    # get assignation id
    assignation = request.vars['id']
    # get assignation comment
    comment = request.vars['comment']
    # get the assignation
    assignation = db.user_project(id = assignation)
    # set the assignation as failed
    assignation.assignation_status = db.assignation_status(name="Failed")
    assignation.assignation_status_comment = comment
    assignation.update_record()
    if request.env.http_referer:
        redirect(request.env.http_referer)
    else:
        redirect(URL('admin','assignations'))
    return

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def force_assignation_successful():
    # get assignation id
    assignation = request.vars['id']
    # get assignation comment
    comment = request.vars['comment']
    # get the assignation
    assignation = db.user_project(id = assignation)
    # set the assignation as successful
    assignation.assignation_status = db.assignation_status(name="Successful")
    assignation.assignation_status_comment = comment
    assignation.update_record()
    if request.env.http_referer:
        redirect(request.env.http_referer)
    else:
        redirect(URL('admin','assignations'))
    return

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def assignations():
    #requires parameter year_period if no one is provided then it is automatically detected
    #and shows the current period
    year_period = request.vars['year_period']
    max_display = 1
    import cpfecys
    currentyear_period = db.period_year(db.period_year.id == year_period)
    if not currentyear_period:
        currentyear_period = cpfecys.current_year_period()
        changid = currentyear_period.id
    q_selected_period_assignations = ((db.user_project.period <= \
        currentyear_period.id)&
              ((db.user_project.period + db.user_project.periods) > \
                currentyear_period.id))
    q2 = (db.user_project.assigned_user == db.auth_user.id)
    q3 = (db.user_project.project == db.project.id)
    q4 = (db.user_project.period == db.period_year.id)
    q5 = (db.project.area_level == db.area_level.id)
    q6 = (db.auth_user.id==db.user_project.assigned_user)
    q7 = (db.auth_user.id==db.auth_membership.user_id)
    q8 = (db.auth_membership.group_id==db.auth_group.id)
    q9 = (db.auth_group.role!='Teacher')
    orderby =  db.area_level.name
    orderby2 = db.project.name
    orderby3 = db.auth_user.username
    orderby4 = db.auth_user.first_name
    data = db(q_selected_period_assignations&q2&q3&q4&q5&q6&q7&q8&q9\
        ).select(orderby=orderby|orderby2|orderby3|orderby4,groupby=db.user_project.id)
    current_period_name = T(cpfecys.second_period.name)
    if currentyear_period.period == cpfecys.first_period.id:
        current_period_name = T(cpfecys.first_period.name)
    start_index = currentyear_period.id - max_display - 1
    if start_index < 1:
        start_index = 0
    end_index = currentyear_period.id + max_display
    periods_before = db(db.period_year \
        ).select(limitby=(start_index, currentyear_period.id - 1))
    periods_after = db(db.period_year \
        ).select(limitby=(currentyear_period.id, end_index))
    other_periods = db(db.period_year).select()

    if request.args(0) == 'toggle':
        enabled = ''
        user = request.vars['user']
        user = db(db.auth_user.id==user).select().first()
        if user == None:
            session.flash = T("No existing user")
            redirect(URL('admin', 'assignations', \
            vars=dict(year_period = currentyear_period)))
        if user.registration_key != 'blocked':
            enabled = 'blocked'
        user.update_record(
                registration_key=enabled)
        redirect(URL('admin', 'assignations', \
            vars=dict(year_period = currentyear_period.id)))

    return dict(data = data,
                currentyear_period = currentyear_period,
                current_period_name = current_period_name,
                periods_before = periods_before,
                periods_after = periods_after,
                other_periods = other_periods)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def periods():
    grid = SQLFORM.grid(db.period_year)
    return locals()

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def report_requirements():
    grid = SQLFORM.grid(db.area_report_requirement)
    return locals()

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def report_restrictions():
    grid = SQLFORM.grid(db.report_restriction)
    return locals()

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def projects():
    grid = SQLFORM.grid(db.project)
    return locals()

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def parameters():
    grid = SQLFORM.grid(db.custom_parameters)
    return dict(grid=grid)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def report():
    import datetime
    import cpfecys
    cdate = datetime.datetime.now()
    report = request.vars['report']
    report = db.report(db.report.id == report)
    parameters = cpfecys.get_custom_parameters()
    valid = not(report is None)
    next_date = None
    if (request.args(0) == 'view'):
        report = request.vars['report']
        report = db.report(db.report.id == report)
        valid = not(report is None)
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
            def add_timing(status):
                if status == 'Acceptance':
                    return status
                elif status == 'Recheck':
                    return status + ' (' + str(parameters.rescore_max_days) + \
                        ' days)'
                else:
                    return status + ' (24 hours)'
            if report.score_date:
                next_date = report.score_date + datetime.timedelta(
                    days=parameters.rescore_max_days)
            response.view = 'admin/report_view.html'
            assignation_reports = db(db.report.assignation== \
                report.assignation).select()
            #***********************************************************************************************************************
            #******************************************************PHASE 2 DTT******************************************************
            activitiesTutor=None
            if report.assignation.project.area_level.name=='DTT Tutor Académico' and (report.status.name=='Draft' or report.status.name=='Recheck'):
                activitiesTutor = activities_report_tutor(report)
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
                status_list=db(db.report_status).select(),
                add_timing=add_timing,
                teacher=teacher,
                activitiesTutor=activitiesTutor)
            #***********************************************************************************************************************
            #******************************************************PHASE 2 DTT******************************************************
        else:
            session.flash = T('Selected report can\'t be viewed. \
                                Select a valid report.')
            redirect(URL('admin', 'index'))
    elif (request.args(0) == 'approve'):
        report.update_record(dtt_approval=True)
        session.flash = T('The report has been approved')
        redirect(URL('admin', 'report/view', \
            vars=dict(report=report.id)))
    elif (request.args(0) == 'fail'):
        report.update_record(dtt_approval=False)
        session.flash = T('The report has been failed')
        redirect(URL('admin', 'report/view', \
            vars=dict(report=report.id)))
    elif (request.args(0) == 'pending'):
        report.update_record(dtt_approval=None)
        session.flash = T('The report has been set to pending')
        redirect(URL('admin', 'report/view', \
            vars=dict(report=report.id)))
    elif (request.args(0) == 'grade'):
        if valid:
            score = request.vars['score']
            comment = request.vars['comment']
            status = request.vars['status']
            sendmail = request.vars['send_mail']
            if sendmail != None: sendmail = True
            else: sendmail = False
            if score != '': score = int(score)
            else: score = report.score
            if comment == '': comment = report.teacher_comment
            status =db.report_status(id=status)
            if status.id != report.status:
                #***********************************************************************************************************************
                #******************************************************PHASE 2 DTT******************************************************
                if report.assignation.project.area_level.name=='DTT Tutor Académico' and (status.name=='Draft' or status.name=='Recheck'):
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
                    admin_score=score,
                    min_score=cpfecys.get_custom_parameters().min_score,
                    admin_comment=comment,
                    score_date=cdate,
                    status=status.id,
                    dtt_approval=True,
                    never_delivered=False)
            elif score >= 0  and score <= 100:
                report.update_record(
                    admin_score=score,
                    min_score=cpfecys.get_custom_parameters().min_score,
                    admin_comment=comment,
                    score_date=cdate,
                    status=db.report_status(name='Acceptance'),
                    dtt_approval=True,
                    never_delivered=False)

            if sendmail:
                user = report.assignation.assigned_user
                subject = T('[DTT]Automatic Notification - Report graded ') \
                +T('BY ADMIN USER')
                signat = cpfecys.get_custom_parameters().email_signature or ''
                cstatus = db(db.report_status.id==report.status).select().first()
                message = '<html>' + T('The report') + ' ' \
                + '<b>' + XML(report.report_restriction.name) + '</b><br/>' \
                + T('sent by student: ') + XML(user.username) + ' ' \
                + XML(user.first_name) + ' ' \
                + XML(user.last_name) \
                + '<br/>' \
                + T('Score: ') + XML(report.admin_score) + ' ' \
                + '<br/>' \
                + T('Scored by: ') + XML('Admin User') + ' ' \
                + '<br/>' \
                + T('Comment: ') + XML(comment) + ' ' \
                + '<br/>' \
                + T('Current status is: ') \
                + XML(T(cstatus.name)) +'<br/>' \
                + T('DTT-ECYS') \
                + ' ' + cpfecys.get_domain() + '<br />' + signat + '</html>'
                was_sent = mail.send(to=user.email,
                  subject=subject,
                  message=message)
                #MAILER LOG
                db.mailer_log.insert(sent_message = message,
                             destination = str(user.email),
                             result_log = str(mail.error or '') + ':' + str(mail.result),
                             success = was_sent)
            session.flash = T('The report has been scored \
                successfully')
            redirect(URL('admin', 'report/view', \
                vars=dict(report=report.id)))

        session.flash = T('Not valid Action.')
        redirect(URL('admin', 'report/view', \
                    vars=dict(report=report.id)))

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def courses_report():
    period = cpfecys.current_year_period()
    periods = db(db.period_year).select()
    area = None
    if request.vars['period'] != None:
        period = request.vars['period']
        period = db(db.period_year.id==period).select().first()
        if not period:
            session.flash = T('Not valid Action.')
            redirect(URL('default', 'index'))
    if request.args(0) == 'areas':
        areas = db(db.area_level).select()
        return dict(areas=areas)
    elif request.args(0) == 'list':
        area = request.vars['area']
        response.view = 'admin/courses_list.html'
        projects = db(db.project.area_level==area).select()
        def count_assigned(project):
            assignations = get_assignations(project, period, 'Student' \
                ).count()
            return assignations
        def obtainPeriodReport(report):
            #Get the minimum and maximum date of the report
            tmp_period=1
            tmp_year=report.report_restriction.start_date.year
            if report.report_restriction.start_date.month >= 6:
               tmp_period=2
            return db((db.period_year.yearp==tmp_year)&(db.period_year.period==tmp_period)).select().first()
        def count_assigned_students(project):
            assigned = []
            desertion = []
            assignations = get_assignations(project, period, 'Student' \
                ).select(db.user_project.ALL)
            for assignation in assignations:                
                reports = db(db.report.assignation==assignation.id
                    ).select()
                for report in reports:
                    if obtainPeriodReport(report) == period:
                        assigned.append(report.desertion_started)
            if assignations.first() != None:
                desertion_assignation = assignations.first()
                desertion_reports = db(
                    db.report.assignation==desertion_assignation.id).select()
                for report in desertion_reports:
                    if obtainPeriodReport(report) == period:
                        if report.desertion_gone != None:
                            if report.desertion_gone:
                                desertion.append(report.desertion_gone)
            if len(assigned) > 0:
                assigned = max(assigned)
            else:
                assigned = T('Pending')
            if len(desertion) > 0:
                desertion = sum(desertion)
            else:
                desertion = T('Pending')
            return desertion, assigned
        def count_student_hours(project):
            resp = []
            assignations = get_assignations(project, period, 'Student' \
                ).select(db.user_project.ALL)
            for assignation in assignations:
                hours = 0
                reports = db(db.report.assignation==assignation.id
                    ).select()
                for report in reports:
                    if report.hours != None:
                        hours += report.hours
                sub_response = [assignation.assigned_user.first_name +\
                    ' ' + assignation.assigned_user.last_name + \
                    ', ' + assignation.assigned_user.username, hours]
                resp.append(sub_response)
            return resp

        def current_teacher(project):
            teacher = get_assignations(project, period, 'Teacher'
                ).select(db.auth_user.ALL).first()
            name = T('Pending')
            if teacher != None:
                name = teacher.first_name + ' ' + teacher.last_name
            return name

        return dict(projects=projects, count_assigned=count_assigned,
            current_teacher=current_teacher, 
            count_assigned_students=count_assigned_students,
            count_student_hours=count_student_hours,
            periods=periods,
            area=area, period=period)
    else:
        session.flash = "Action not allowed"
        redirect(URL('default','index'))

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def active_teachers():
    period = cpfecys.current_year_period()
    if request.vars['period'] != None:
            period = request.vars['period']
            period = db(db.period_year.id==period).select().first()
            if not period:
                session.flash = T('Not valid Action.')
                redirect(URL('default', 'index'))
    if (request.args(0) == 'toggle'):
        enabled = ''
        user = request.vars['user']
        user = db(db.auth_user.id==user).select().first()
        if user == None:
            session.flash = T("No existing user")
            redirect(URL('admin','active_teachers'))
        if user.registration_key != 'blocked':
            enabled = 'blocked'
        user.update_record(
                registration_key=enabled)
        redirect(URL('admin','active_teachers'))
    elif request.args(0) == 'mail':
        user = request.vars['user']
        if user == None:
            session.flash = T("No existing user")
            redirect(URL('admin','active_teachers'))
        user = db(db.auth_user.id==user).select().first()
        if user == None:
            session.flash = T("No existing user")
            redirect(URL('admin','active_teachers'))
        recovery = cpfecys.get_domain() + \
            'default/user/request_reset_password?_next=/cpfecys/default/index'
        message = "Bienvenido a CPFECYS, su usuario es " + user.username + \
        ' para generar su contraseña puede visitar el siguiente enlace e ' +\
        'ingresar su usuario ' + recovery
        subject = 'DTT-ECYS Bienvenido'
        send_mail_to_users([user], message, None, None, subject)
        user.update_record(load_alerted=True)
    elif request.args(0) == 'notifyall':
        users = get_assignations(False, period, 'Teacher'
                ).select(db.auth_user.ALL, distinct=True)
        recovery = cpfecys.get_domain() + \
            'default/user/request_reset_password?_next=/cpfecys/default/index'
        for user in users:
            message = "Bienvenido a CPFECYS, su usuario es " + user.username + \
            ' para generar su contraseña puede visitar el siguiente enlace e ' +\
            'ingresar su usuario ' + recovery
            subject = 'DTT-ECYS Bienvenido'
            send_mail_to_users([user], message, None, None, subject)
            user.update_record(load_alerted=True)
    elif request.args(0) == 'notifypending':
        project = False
        users = db(
            (db.auth_user.id==db.user_project.assigned_user)&
            (db.auth_user.id==db.auth_membership.user_id)&
            (db.auth_user.load_alerted==None)&
            (db.auth_membership.group_id==db.auth_group.id)&
            (db.auth_group.role=='Teacher')&
            (project==False or (db.user_project.project==project))&
            (db.project.area_level==db.area_level.id)&
            (db.user_project.project==db.project.id)&
            (db.user_project.period == db.period_year.id)&
            ((db.user_project.period <= period.id)&
         ((db.user_project.period + db.user_project.periods) > \
          period.id))
            ).select(db.auth_user.ALL, distinct=True)
        recovery = cpfecys.get_domain() + \
            'default/user/retrieve_username?_next=/cpfecys/default/index'
        for user in users:
            message = "Bienvenido a CPFECYS, su usuario es " + user.username + \
            ' para generar su contraseña puede visitar el siguiente enlace e ' +\
            'ingresar su usuario ' + recovery
            subject = 'DTT-ECYS Bienvenido'
            send_mail_to_users([user], message, None, None, subject)
            user.update_record(load_alerted=True)

    assignations = get_assignations(False, period, 'Teacher' \
                ).select(db.user_project.ALL,
                orderby=db.area_level.name|\
                db.project.name|\
                db.auth_user.last_name|\
                db.auth_user.first_name)
    periods = db(db.period_year).select()
    return dict(periods=periods, assignations=assignations,
        actual_period=period)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def get_assignations(project, period, role):
    assignations = db(
                    (db.auth_user.id==db.user_project.assigned_user)&
                    (db.auth_user.id==db.auth_membership.user_id)&
                    (db.auth_membership.group_id==db.auth_group.id)&
                    (db.auth_group.role==role)&
                    (project==False or (db.user_project.project==project))&
                    (db.project.area_level==db.area_level.id)&
                    (db.user_project.project==db.project.id)&
                    (db.user_project.period == db.period_year.id)&
                    ((db.user_project.period <= period.id)&
                 ((db.user_project.period + db.user_project.periods) > \
                  period.id))
                    )
    return assignations

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def courses_report_detail():
    period = cpfecys.current_year_period()
    periods = db(db.period_year).select()
    if request.vars['period'] != None:
        period = request.vars['period']
        period = db(db.year_period.id==period).select().first()
    if request.vars['project'] == None:
        session.flash = "Action not allowed"
        redirect(URL('admin','courses_report/areas'))
    project = request.vars['project']
    assignations = db(
                    (db.auth_user.id==db.user_project.assigned_user)&
                    (db.auth_user.id==db.auth_membership.user_id)&
                    (db.auth_membership.group_id==db.auth_group.id)&
                    (db.auth_group.role=='Student')&
                    (db.user_project.project==project)&
                    (db.user_project.period == db.period_year.id)&
                    ((db.user_project.period <= period)&
                 ((db.user_project.period + db.user_project.periods) > \
                  period))
                    )._select()
    return assignations
    return dict(periods=periods, project=project,
        period=period)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def mail_notifications():
    period = cpfecys.current_year_period()
    if (request.args(0) == 'send'):
        roles = request.vars['role']
        projects = request.vars['project']
        message = request.vars['message']
        subject = request.vars['subject']

        if isinstance(roles, str):
            roles = [roles]

        if projects != None and isinstance(projects, str):
            projects = [projects]

        if projects  != None  and roles != None:
            for role in request.vars['role']:
                role = db(db.auth_group.id==role).select().first()

                if role.role == 'DSI':
                    users = db(
                        (db.auth_user.id==db.auth_membership.user_id)&
                        (db.auth_membership.group_id==db.auth_group.id)&
                        (db.auth_group.role=='DSI'))
                    group_id = users.select().first().auth_group.id
                    dsi_role = [group_id]
                    send_mail_to_users(users.select(db.auth_user.ALL), 
                        message, dsi_role, projects,
                        subject)

                users = db(
                    (db.auth_user.id==db.auth_membership.user_id)&
                    (db.auth_membership.group_id==db.auth_group.id)&
                    (db.auth_group.id.belongs(roles))&
                    #Until here we get users from role
                    (db.user_project.project.belongs(projects))&
                    (db.auth_user.id==db.user_project.assigned_user)&
                    #Until here we get users from role assigned to projects
                    (db.user_project.period==db.period_year.id)&
                    ((db.user_project.period <= period.id)&
                    ((db.user_project.period + db.user_project.periods) > \
                     period.id))
                    )
                #return users._select(db.auth_user.ALL, distinct=True)
                users = users.select(db.auth_user.ALL, distinct=True)
                #return users
                send_mail_to_users(users, message, \
                    roles, projects, subject, True)

            session.flash = T('Mail successfully sent')
            redirect(URL('admin', 'mail_notifications'))
        elif (roles != None) and (len(roles) == 1):
            for role in roles:
                role = db(db.auth_group.id==role).select().first()
                if role.role == 'DSI':
                    users = db(
                        (db.auth_user.id==db.auth_membership.user_id)&
                        (db.auth_membership.group_id==db.auth_group.id)&
                        (db.auth_group.role=='DSI'))
                    group_id = users.select().first().auth_group.id
                    dsi_role = [group_id]
                    send_mail_to_users(users.select(db.auth_user.ALL), 
                        message, dsi_role, projects,
                        subject)
        else:
            session.flash = T('At least a project and a role must be selected')
            redirect(URL('admin', 'mail_notifications'))

    groups = db(db.auth_group.role!='Super-Administrator').select()
    areas = db(db.area_level).select()
    def get_projects(area):
        courses = db(db.project.area_level==area.id)
        return courses
    def prepare_name(name):
        name = name.lower()
        name = name.replace(' ', '-')
        return name
    return dict(groups=groups,
        areas=areas,
        get_projects=get_projects,
        prepare_name=prepare_name,
        markmin_settings = cpfecys.get_markmin)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def mail_log():
    logs = db(db.mail_log).select()
    return dict(logs=logs)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def send_mail_to_users(users, message, roles, projects, subject, log=False):
    if log:
        import datetime
        cdate = datetime.datetime.now()
        roles = db(db.auth_group.id.belongs(roles)).select()
        projects = db(db.project.id.belongs(projects)).select()
        roles_text = ''
        projects_text = ''
        for role in roles:
            roles_text = roles_text + ',' + role.role
            pass
        for project in projects:
            projects_text = projects_text + ', ' + project.name
            pass
        db.mail_log.insert(sent_message=message,
            roles=roles_text[1:],
            projects=projects_text[1:],
            sent=cdate)


    import cpfecys
    message = message.replace("\n","<br>")
    message = '<html>' + message + '<br>'+ (cpfecys.get_custom_parameters().email_signature or '') + '</html>'

    userList= []
    for user in users:
        #print user.email
        if user.email != None and user.email != '':
            userList.append(user.email)

    if userList != '':
        was_sent = mail.send(to='dtt.ecys@dtt-ecys.org',
          subject=subject,
          message=message,
          bcc=userList)
        #MAILER LOG
        db.mailer_log.insert(sent_message = message,
                     destination = str(userList),
                     result_log = str(mail.error or '') + ':' + \
                     str(mail.result),
                     success = was_sent)


@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def anomalies_list():
    from datetime import datetime
    cperiod = cpfecys.current_year_period()
    year = str(cperiod.yearp)
    if cperiod.period == 1:
        start = datetime.strptime(year + '-01-01', "%Y-%m-%d")
        end = datetime.strptime(year + '-06-01', "%Y-%m-%d")
    else:
        start = datetime.strptime(year + '-06-01', "%Y-%m-%d")
        end = datetime.strptime(year + '-12-31', "%Y-%m-%d")
    def get_month_name(date):
        import datetime
        return date.strftime("%B")
    count = db.log_entry.id.count()
    if (request.args(0) == 'view'):
        period = request.vars['period']
        valid = period != None
        if not valid:
            session.flash = T('Incomplete Information')
            redirect(URL('default', 'index'))
        cperiod = db(db.period_year.id==period).select().first()
        if cperiod.period == 1:
            start = datetime.strptime(year + '-01-01', "%Y-%m-%d")
            end = datetime.strptime(year + '-06-01', "%Y-%m-%d")
        else:
            start = datetime.strptime(year + '-06-01', "%Y-%m-%d")
            end = datetime.strptime(year + '-12-31', "%Y-%m-%d")
        anomalies = db((db.log_entry.report==db.report.id)&
            (db.log_entry.log_type==db.log_type(name='Anomaly'))&
            (db.report.created>start)&
            (db.report.created<end)&
            (db.report.assignation==db.user_project.id)&
            (db.user_project.project==db.project.id) \
            ).select(db.log_entry.entry_date, \
            count, db.log_entry.log_type, \
            db.project.ALL, groupby=db.project.name)
        return dict(anomalies=anomalies,
            get_month_name=get_month_name,
            period=period)

    elif (request.args(0) == 'periods'):
        response.view = 'admin/anomaly_periods.html'
        periods = db(db.period_year).select()
        def count_by_period(period):
            cperiod = db(db.period_year.id==period).select().first()
            if cperiod.period == 1:
                start = datetime.strptime(year + '-01-01', "%Y-%m-%d")
                end = datetime.strptime(year + '-06-01', "%Y-%m-%d")
            else:
                start = datetime.strptime(year + '-06-01', "%Y-%m-%d")
                end = datetime.strptime(year + '-12-31', "%Y-%m-%d")
            anomalies_total = db((db.log_entry.report==db.report.id)&
            (db.log_entry.log_type==db.log_type(name='Anomaly'))&
            (db.report.created>start)&
            (db.report.created<end)&
            (db.report.assignation==db.user_project.id)&
            (db.user_project.project==db.project.id) \
            ).count()
            return anomalies_total
        return dict(periods=periods,
            count_by_period=count_by_period)

    elif (request.args(0) == 'show'):
        project = request.vars['project']
        period = request.vars['period']
        valid = project != None
        if not valid:
            session.flash = T('Incomplete Information')
            redirect(URL('default', 'index'))
        project = db(db.project.id==project).select().first()
        anomalies = db((db.log_entry.report==db.report.id)&
            (db.log_entry.log_type==db.log_type(name='Anomaly'))&
            (db.report.created>start)&
            (db.report.created<end)&
            (db.report.assignation==db.user_project.id)&
            (db.user_project.project==db.project.id)&
            (db.project.id==project) \
            ).select(db.log_entry.ALL, \
            db.user_project.ALL,
            db.project.ALL)
        response.view = 'admin/anomaly_show.html'
        return dict(anomalies=anomalies)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def report_list():
    response.view = 'admin/report_list.html'
    period_year = db(db.period_year).select(orderby=~db.period_year.id)
    def count_reproved(pyear):
        from datetime import datetime
        year = str(pyear.yearp)
        if pyear.period == 1:
            start = datetime.strptime(year + '-01-01', "%Y-%m-%d")
            end = datetime.strptime(year + '-06-01', "%Y-%m-%d")
        else:
            start = datetime.strptime(year + '-06-01', "%Y-%m-%d")
            end = datetime.strptime(year + '-12-31', "%Y-%m-%d")
        reports = db((db.report.created>start)&
            (db.report.created<end)&
            (db.report.score < db.report.min_score)&
            (db.report.never_delivered==None 
                or db.report.never_delivered==False))
        return reports.count()

    def count_approved(pyear):
        from datetime import datetime
        year = str(pyear.yearp)
        if pyear.period == 1:
            start = datetime.strptime(year + '-01-01', "%Y-%m-%d")
            end = datetime.strptime(year + '-06-01', "%Y-%m-%d")
        else:
            start = datetime.strptime(year + '-06-01', "%Y-%m-%d")
            end = datetime.strptime(year + '-12-31', "%Y-%m-%d")
        reports = db((db.report.created<end)&
            (db.report.created>start)&
            ((db.report.score>=db.report.min_score) |
                (db.report.admin_score>=db.report.min_score))&
            (db.report.min_score!=None)&
            (db.report.min_score!=0))
        return reports.count()

    def count_no_created(pyear):
        from datetime import datetime
        year = str(pyear.yearp)
        if pyear.period == 1:
            start = datetime.strptime(year + '-01-01', "%Y-%m-%d")
            end = datetime.strptime(year + '-06-01', "%Y-%m-%d")
        else:
            start = datetime.strptime(year + '-06-01', "%Y-%m-%d")
            end = datetime.strptime(year + '-12-31', "%Y-%m-%d")
        cperiod = cpfecys.current_year_period()
        restrictions = db((db.report_restriction.start_date>=start)&
            (db.report_restriction.end_date<=end)&
            (db.report_restriction.is_enabled==True)).select()
        pending = 0
        assignations = get_assignations(False, cperiod, 'Student').select()
        for assignation in assignations:
            for restriction in restrictions:
                report = db(
                    (db.report.assignation==assignation.user_project.id)&
                    (db.report.report_restriction==restriction.id)&
                    (db.report.report_restriction==db.report_restriction.id)
                    ).select(db.report.ALL).first()
                if report == None:
                    pending += 1
                #esto es para no ver drafts en no_created del report_filter
                #else:
                #    hours = report.hours
                #    entries = count_log_entries(\
                #        report.id)[0]['COUNT(log_entry.id)']
                #    metrics = count_metrics_report(\
                #        report.id)[0]['COUNT(log_metrics.id)']
                #    anomalies = count_anomalies(\
                #        report)[0]['COUNT(log_entry.id)']
                #    if assignation.user_project.project.area_level.name == \
                #            'DTT Tutor Académico':
                #        if entries == 0 and metrics == 0 and anomalies == 0:
                #            pending += 1
                #    else:
                #        if hours == None and hours == 0:
                #            pending += 1

        return pending

    def count_acceptance(pyear):
        from datetime import datetime
        year = str(pyear.yearp)
        total = 0
        string = ''
        if pyear.period == 1:
            start = datetime.strptime(year + '-01-01', "%Y-%m-%d")
            end = datetime.strptime(year + '-06-01', "%Y-%m-%d")
        else:
            start = datetime.strptime(year + '-06-01', "%Y-%m-%d")
            end = datetime.strptime(year + '-12-31', "%Y-%m-%d")
        reports = db((db.report.created>= start)&
            (db.report.created<=end)&
            (db.report.status==db.report_status(name='Acceptance'))).select()
        array = []
        for report in reports:
            hours = report.hours
            entries = count_log_entries(report)
            metrics = count_metrics_report(report)
            anomalies = count_anomalies(\
                report)[0]['COUNT(log_entry.id)']
            string = string + str(entries) + ' ' + str(metrics) + ' ' +str(anomalies) + '<br/>'
            if report.assignation.project.area_level.name == \
                    'DTT Tutor Académico':
                if entries != 0 or metrics != 0 or anomalies != 0:
                    total += 1
            else:
                if hours != None:
                    total += 1
        return total

    def count_draft(pyear):
        from datetime import datetime
        year = str(pyear.yearp)
        total = 0
        string = ''
        if pyear.period == 1:
            start = datetime.strptime(year + '-01-01', "%Y-%m-%d")
            end = datetime.strptime(year + '-06-01', "%Y-%m-%d")
        else:
            start = datetime.strptime(year + '-06-01', "%Y-%m-%d")
            end = datetime.strptime(year + '-12-31', "%Y-%m-%d")
        reports = db((db.report.created>= start)&
            (db.report.created<=end)&
            (db.report.status==db.report_status(name='Draft'))).select()
        for report in reports:
            hours = report.hours
            #***********************************************************************************************************************
            #******************************************************PHASE 2 DTT******************************************************
            entries = count_log_entries(report)
            metrics = count_metrics_report(report)
            anomalies = count_anomalies(\
                report)[0]['COUNT(log_entry.id)']
            string = string + str(entries) + ' ' + str(metrics) + ' ' +str(anomalies) + '<br/>'
            if report.assignation.project.area_level.name == \
                    'DTT Tutor Académico':
                if entries != 0 or metrics != 0 or anomalies != 0:
                            total += 1
            #***********************************************************************************************************************
            #******************************************************PHASE 2 DTT******************************************************
            else:
                if hours != None and hours != 0:
                    total += 1
        return total

    def count_no_delivered(pyear):
        from datetime import datetime
        year = str(pyear.yearp)
        if pyear.period == 1:
            start = datetime.strptime(year + '-01-01', "%Y-%m-%d")
            end = datetime.strptime(year + '-06-01', "%Y-%m-%d")
        else:
            start = datetime.strptime(year + '-06-01', "%Y-%m-%d")
            end = datetime.strptime(year + '-12-31', "%Y-%m-%d")
        reports = db((db.report_restriction.start_date>=start)&
            (db.report_restriction.end_date<=end)&
            (db.report.report_restriction==db.report_restriction.id)&
            (db.report.never_delivered == True))
        return reports.count()
    def count_reports(pyear, status, exclude):
        from datetime import datetime
        year = str(pyear.yearp)
        if pyear.period == 1:
            start = datetime.strptime(year + '-01-01', "%Y-%m-%d")
            end = datetime.strptime(year + '-06-01', "%Y-%m-%d")
        else:
            start = datetime.strptime(year + '-06-01', "%Y-%m-%d")
            end = datetime.strptime(year + '-12-31', "%Y-%m-%d")
        count = db.report.id.count()
        report_total = db().select(
            db.report_status.ALL, count, 
            left=db.report.on((db.report.status==db.report_status.id)&
                (db.report.created < end)&
                (db.report.created > start)&
                ((status==False) or (db.report_status.name==status))), 
            groupby=db.report_status.name,
            orderby=db.report_status.order_number)
        return report_total

    count = db.report.id.count()
    report_total = db().select(
        db.report_status.ALL, count, 
        left=db.report.on((db.report.status==db.report_status.id)), 
        groupby=db.report_status.name,
        orderby=db.report_status.order_number)
    return dict(period_year=period_year,
        report_total=report_total,
        count_reproved=count_reproved,
        count_approved=count_approved,
        count_no_created=count_no_created,
        count_reports=count_reports,
        count_draft=count_draft,
        count_no_delivered=count_no_delivered,
        count_acceptance=count_acceptance)
                

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def report_filter():
    from datetime import datetime
    cperiod = cpfecys.current_year_period()
    if request.vars['period'] != None:
        cperiod = db(db.period_year.id==\
            request.vars['period']).select().first()
    year = str(cperiod.yearp)
    if cperiod.period == 1:
        start = datetime.strptime(year + '-01-01', "%Y-%m-%d")
        end = datetime.strptime(year + '-06-01', "%Y-%m-%d")
    else:
        start = datetime.strptime(year + '-06-01', "%Y-%m-%d")
        end = datetime.strptime(year + '-12-31', "%Y-%m-%d")
    status = request.vars['status']
    period = request.vars['period']
    valid = period != None
    def count_log_entries(report):
        #***********************************************************************************************************************
        #******************************************************PHASE 2 DTT******************************************************
        if report.assignation.project.area_level.name=='DTT Tutor Académico' and (report.status.name=='Draft' or report.status.name=='Recheck'):
            activitiesTutor = activities_report_tutor(report)
            log_entries=len(activitiesTutor['activities_WM'])+len(activitiesTutor['activities_M'])
        else:
            log_entries = db((db.log_entry.report==report.id)).select(db.log_entry.id.count())[0]['COUNT(log_entry.id)']
        return log_entries
        #***********************************************************************************************************************
        #******************************************************PHASE 2 DTT******************************************************
    def count_metrics_report(report):
        #***********************************************************************************************************************
        #******************************************************PHASE 2 DTT******************************************************
        if report.assignation.project.area_level.name=='DTT Tutor Académico' and (report.status.name=='Draft' or report.status.name=='Recheck'):
            activitiesTutor = activities_report_tutor(report)
            log_metrics=len(activitiesTutor['activities_M'])
        else:
            log_metrics = db((db.log_metrics.report== report.id)).select(db.log_metrics.id.count())[0]['COUNT(log_metrics.id)']
        return log_metrics
        #***********************************************************************************************************************
        #******************************************************PHASE 2 DTT******************************************************
    def count_anomalies(report):
        log_entries = db((db.log_entry.report== \
            report.id)&
        (db.log_entry.log_type==db.log_type(name='Anomaly')) \
        ).select(db.log_entry.id.count())
        return log_entries
    def calculate_ending_date(report):
        from datetime import date, datetime, timedelta
        someday = date.today()
        otherday = someday + timedelta(days=8)
        date = datetime.strptime(str(report.assignation.period.yearp) + \
                '-01-01', "%Y-%m-%d")
        date += timedelta(days=(30*6)*report.assignation.periods)
        semester =''
        fecha = ''
        if report.assignation.period.period.id == 1:
            if report.assignation.periods % 2 == 0:
                semester = T('Second Semester')
            else:
                semester = T('First Semester')
            fecha = str(date.year) + '-' + str(semester)
        else:
            if report.assignation.periods % 2 == 0:
                semester = T('First Semester')
                fecha = str(date.year+1) + '-' + str(semester)
            else:
                semester = T('Second Semester')
                fecha = str(date.year) + '-' + str(semester)
        return fecha
    if not valid:
        session.flash = T('Incomplete Information')
        redirect(URL('default', 'index'))
    if not status:
        reports = db((db.report.created>start)&
            (db.report.created<end)).select(db.report.ALL)
        status_instance = False
    elif int(status) == -1:#Aprobados
        reports = db((db.report.created>start)&
            (db.report.created<end)&
            ((db.report.admin_score>=db.report.min_score) |\
             (db.report.score>=db.report.min_score))&
            (db.report.min_score!=None)&
            (db.report.min_score!=0)).select()
        status_instance = db(db.report_status.id==status).select().first()
    elif int(status) == -2:#Reprobados
        reports = db((db.report.created>start)&
            (db.report.created<end)&
            (db.report.score<=db.report.min_score)&
            (db.report.min_score!=None)&
            (db.report.min_score!=0)&
            (db.report.never_delivered==None or
                db.report.never_delivered==False)).select()
        status_instance = db(db.report_status.id==status).select().first()
    elif int(status) == -3:#Pendientes
        #***********************************************************************************************************************
        #******************************************************PHASE 2 DTT******************************************************    
        #INIT Check if there is a pending report has created
        if request.vars['report'] != None and request.vars['assignation'] != None:
            #Check for restriction exists and is valid
            rr_ID = db((db.report_restriction.start_date>=start)&
                (db.report_restriction.end_date<=end)&
                (db.report_restriction.is_enabled==True)&
                (db.report_restriction.id==int(request.vars['report']))).select().first()
            if rr_ID is None:
                session.flash = T('Incomplete Information')
                redirect(URL('admin', 'report_filter',vars=dict(status = request.vars['status'], period = request.vars['period'])))

            #Verify that the user exists and is student specific period
            assignations_ID = db(
                    (db.auth_user.id==db.user_project.assigned_user)&
                    (db.auth_user.id==db.auth_membership.user_id)&
                    (db.auth_membership.group_id==db.auth_group.id)&
                    (db.auth_group.role=='Student')&
                    (db.user_project.id==int(request.vars['assignation']))&
                    (db.user_project.period == db.period_year.id)&
                    ((db.user_project.period <= cperiod.id)&
                 ((db.user_project.period + db.user_project.periods) > \
                  cperiod.id))
                    ).select().first()
            if assignations_ID is None:
                session.flash = T('Incomplete Information')
                redirect(URL('admin', 'report_filter',vars=dict(status = request.vars['status'], period = request.vars['period'])))

            #Verify that the specified user does not have a report from the constraint specified
            report_delivered = db((db.report.report_restriction==int(request.vars['report']))&(db.report.assignation==int(request.vars['assignation']))).select().first()
            if report_delivered is not None:
                session.flash = T('Incomplete Information')
                redirect(URL('admin', 'report_filter',vars=dict(status = request.vars['status'], period = request.vars['period'])))    

            #Create the report and place it in draft status so that you can edit the student
            status_draft = db.report_status(db.report_status.name == 'Draft')
            current_date = datetime.now().date()
            new_Report = db.report.insert(created = rr_ID.end_date,
                                 assignation = int(request.vars['assignation']),
                                 report_restriction = rr_ID.id,
                                 admin_score = cpfecys.get_custom_parameters().min_score,
                                 min_score = cpfecys.get_custom_parameters().min_score,
                                 status = status_draft,
                                 admin_comment =  T('Created by admin'),
                                 score_date=current_date,
                                 dtt_approval=True,
                                 never_delivered=False)
            if new_Report.assignation.project.area_level.name=='DTT Tutor Académico' and new_Report.report_restriction.is_final==True:
                #CREATE THE FINAL METRICS
                cperiod = obtainPeriodReport(new_Report)
                final_metrics = final_metric(cperiod,new_Report)
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
                                    report=new_Report.id
                                    )
            
            #Report by email to the academic tutor who can edit your report
            user = new_Report.assignation.assigned_user
            subject = T('[DTT]Automatic Notification - Report created ') \
            +T('BY ADMIN USER')
            signat = cpfecys.get_custom_parameters().email_signature or ''
            cstatus = db(db.report_status.id==new_Report.status).select().first()
            message = '<html>' + T('You have created the report') + ' ' \
            + '<b>' + XML(new_Report.report_restriction.name) + '</b>.<br/>' \
            + T('The report is set to Draft status. You can proceed to edit the report.') \
            +'<br/>' \
            + T('DTT-ECYS') \
            + ' ' + cpfecys.get_domain() + '<br />' + signat + '</html>'
            print message
            was_sent = mail.send(to=user.email,
              subject=subject,
              message=message)
            #MAILER LOG
            db.mailer_log.insert(sent_message = message,
                         destination = str(user.email),
                         result_log = str(mail.error or '') + ':' + str(mail.result),
                         success = was_sent)
            


            session.flash = T('You have created the report and has notified the academic tutor by email')
            redirect(URL('admin', 'report/view',vars=dict(report = new_Report.id)))
        elif request.vars['report'] != None or request.vars['assignation'] != None:
            session.flash = T('Incomplete Information')
            redirect(URL('admin', 'report_filter',vars=dict(status = request.vars['status'], period = request.vars['period'])))
        #END Check if there is a pending report has created
        #***********************************************************************************************************************
        #******************************************************PHASE 2 DTT******************************************************

        result = []
        existing = []
        restrictions = db((db.report_restriction.start_date>=start)&
            (db.report_restriction.end_date<=end)&
            (db.report_restriction.is_enabled==True)).select()
        pending = 0
        assignations = get_assignations(False, cperiod, 'Student').select()
        for assignation in assignations:
            for restriction in restrictions:
                report = db(
                    (db.report.assignation==assignation.user_project.id)&
                    (db.report.report_restriction==restriction.id)&
                    (db.report.report_restriction==db.report_restriction.id)
                    ).select(db.report.ALL).first()
                if report == None:
                    temp = dict(assignation=assignation, 
                        restriction=restriction)
                    result.append(temp)
                else:
                    hours = report.hours
                    entries = count_log_entries(report)
                    metrics = count_metrics_report(report)
                    anomalies = count_anomalies(report)[0]['COUNT(log_entry.id)']
                    temp = dict(assignation=assignation, 
                            restriction=restriction,
                            report=report)
                    if assignation.user_project.project.area_level.name == \
                            'DTT Tutor Académico':
                        if entries == 0 and metrics == 0 and anomalies == 0:
                            existing.append(temp)
                    else:
                        if hours == None:
                            existing.append(temp)
        response.view = 'admin/report_filter_pending.html'      
        return dict(result=result, existing=existing,
            count_log_entries=count_log_entries,
            count_metrics_report=count_metrics_report,
            count_anomalies=count_anomalies,)
    elif int(status) == -4:#No entregados
        reports = db((db.report_restriction.start_date>=start)&
            (db.report_restriction.end_date<=end)&
            (db.report.report_restriction==db.report_restriction.id)&
            (db.user_project.id==db.report.assignation)&
            (db.auth_user.id==db.user_project.assigned_user)&
            (db.project.id==db.user_project.project)&
            (db.report.never_delivered == True))
        status_instance = reports.select()
        response.view = 'admin/report_filter_never_delivered.html'
        return dict(status_instance=status_instance,
            count_log_entries=count_log_entries,
            count_metrics_report=count_metrics_report,
            count_anomalies=count_anomalies,
            status=status,
            period=period)
    else:
        reports = db((db.report.created>start)&
            (db.report.created<end)&
            (db.report.status==status)).select(db.report.ALL)
        status_instance = db(db.report_status.id==status).select().first()
    return dict(reports=reports,
        count_log_entries=count_log_entries,
        count_metrics_report=count_metrics_report,
        count_anomalies=count_anomalies,
        calculate_ending_date=calculate_ending_date,
        status = status,
        status_instance = status_instance,
        period = period)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def links():
    user = db(db.auth_membership.user_id== \
        auth.user.id).select(db.auth_group.ALL)
    grid = SQLFORM.smartgrid(db.link, linked_tables=['link_access'])
    return locals()

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def areas():
    grid = SQLFORM.grid(db.area_level)
    return locals()

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def files_manager():
    user = db(db.auth_membership.user_id==auth.user.id \
        ).select(db.auth_group.ALL)
    grid = SQLFORM.smartgrid(db.uploaded_file, linked_tables=['file_access'])
    return locals()

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def notifications_manager():
    user = db(db.auth_membership.user_id == auth.user.id \
        ).select(db.auth_group.ALL)
    grid = SQLFORM.smartgrid(db.front_notification,  \
        linked_tables=['notification_access'])
    return locals()

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def items_manager():
    from datetime import datetime
    cperiod = cpfecys.current_year_period()
    year = str(cperiod.yearp)
        
    if request.function == 'new':
        db.item.created.writable=db.item.created.readable=False
    grid = SQLFORM.smartgrid(db.item_restriction,  \
        linked_tables=['item_restriction_area', 'item_restriction_exception'])
    return dict(grid=grid, year=year)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def manage_items():
    if (request.args(0) == 'periods'):
        response.view = 'admin/manage_items_periods.html'
        periods = db(db.period_year).select()
        return dict(periods=periods)
    elif (request.args(0) == 'area'):
        def count_items(area, period, disabled=False, enabled=False):
            if not(area and period):
                assignations = db(
                    (db.auth_user.id==db.user_project.assigned_user)&
                    (db.auth_user.id==db.auth_membership.user_id)&
                    (db.auth_membership.group_id==db.auth_group.id)&
                    (db.auth_group.role!='Teacher')).select(db.user_project.ALL)
                items = db((db.item.assignation.belongs(assignations))&
                    ((disabled==False)or(db.item.is_active==False))&
                    ((enabled==False)or(db.item.is_active==True)))
                return items
            else:
                projects = db(db.project.area_level==area).select()
                assignations = db((db.user_project.project.belongs(projects))&
                    (db.auth_user.id==db.user_project.assigned_user)&
                    (db.auth_user.id==db.auth_membership.user_id)&
                    (db.auth_membership.group_id==db.auth_group.id)&
                    (db.auth_group.role!='Teacher')).select(db.user_project.ALL)
                items = db((db.item.assignation.belongs(assignations))&
                    (db.item.created==period)&
                    ((disabled==False)or(db.item.is_active==False))&
                    ((enabled==False)or(db.item.is_active==True)))
                return items
        period = request.vars['period']
        areas = db(db.area_level).select()
        response.view = 'admin/manage_items_areas.html'
        return dict(areas=areas,
            period=period,
            count_items=count_items)        

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def delivered_download():
    if request.args(0) == 'type':
        period = request.vars['period']
        restrictions = db((db.item_restriction.period==period)&
            (db.item_restriction.is_enabled==True)&
            (db.item_restriction.item_type==db.item_type(name='File')))
        restrictions = restrictions.select(db.item_restriction.ALL)
        response.view = 'admin/delivered_download_restrictions.html'
        return dict(restrictions=restrictions)

    elif request.args(0) == 'zip':
        import datetime
        period = request.vars['period']
        cdate = datetime.datetime.now().date()
        restriction = request.vars['restriction']
        r_instance = db(db.item_restriction.id==1
            ).select(db.item_restriction.ALL)
        file_name = cdate + T('Deliverable Items')
        items = db((db.item.item_restriction==restriction)&
            (db.item.uploaded_file!=None)&
            (db.item.uploaded_file!='')).select()
        files = []
        for item in items:
            files.append(item.uploaded_file)
        if len(files) > 0:
            return response.zip(request, files, db)
        session.flash = T('No files to download.')
        redirect(URL('admin', 'delivered_download/type', 
            vars=dict(period=period)))

    periods = db(db.period_year).select()
    return dict(periods=periods)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def send_item_mail():
    user = request.vars['user']
    item = request.vars['item']
    success = False
    if not (not item and not user):
        user = db(db.auth_user.id==user).select().first()
        item = db(db.item.id==item).select().first()
        comment = item.admin_comment or T('No comment')
        subject = T('Item rejected by admin, please take action.')
        message = T('An item you created has been rejected by admin,') \
            + T('the reason is ') + comment \
            + T('please proceed to replace the item, if you don\'t take\
                any action the item will remain disabled.')
        import cpfecys
        message += (cpfecys.get_custom_parameters().email_signature or '')
        was_sent = mail.send(to=user.email,
                  subject=subject,
                  message=message)
        #MAILER LOG
        db.mailer_log.insert(sent_message = message,
                             destination = str(user.email),
                             result_log = str(mail.error or '') + ':' + str(mail.result),
                             success = was_sent)
        item.update_record(
            notified_mail = True)
        success = True
    return success
@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def items_grid():
    import datetime
    cdate = datetime.datetime.now().date()
    period = request.vars['period']
    area = request.vars['area']
    context_string = T('All')
    period_entity = db(db.period_year.id==period).select().first()
    if period_entity:
        period_name = period_entity.period.name
        period_year = period_entity.yearp
        context_string = T(str(period_name)) + ' ' + str(period_entity.yearp)
    school_id = request.vars['school_id']
    if not(area=='' or area==None):
        projects = db(db.project.area_level==area).select()    
    else:
        projects = db(db.project).select()
    assignations = db((db.user_project.project.belongs(projects))&
            (db.auth_user.id==db.user_project.assigned_user)&
            (db.auth_user.id==db.auth_membership.user_id)&
            ((school_id=='' or school_id==None) or \
                (db.auth_user.username==school_id))&
            (db.auth_membership.group_id==db.auth_group.id)&
            (db.auth_group.role!='Teacher')).select(db.user_project.ALL)
    items = db((db.item.assignation.belongs(assignations))&
        ((period=='' or period==None) or (db.item.created==period))
        ).select(orderby=db.item.item_restriction.name)
    if request.args(0) == 'zip':
        files = []
        for item in items:
            files.append(item.uploaded_file)
        if len(files) > 0:
            return response.zip(request, files, db)
        response.flash = T('No files to download.')
    return dict(items=items,
        area=area,
        period=period,
        context_string=context_string,
        cdate=str(cdate))

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def toggle_active_item():
    item = request.vars['item']
    comment = request.vars['comment'] or None
    if item != None:
        item = db(db.item.id==item).select().first()
    if item != None:
        item.update_record(
            is_active = not item.is_active,
            admin_comment=comment)
    return True

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def assign_items():
    filter = 1
    if request.vars['filter'] != None:
        filter = int(request.vars['filter'])
    if filter == 1:
        pass
    dct = {}
    items = db((db.item.is_active==True)).select()
    rows=db().select(db.item.ALL, db.item_project.ALL,
         left=db.item_project.on(db.item.id==db.item_project.item))
    for item in items:
        dct.update({item.name:[]})
    for row in rows:
        dct[row.item.name].append(row)
    return locals()

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def teacher_assignation_upload():
    import csv
    error_users = []
    warning_users = []
    uv_off = request.vars['uv_off'] or False
    success = False
    import cpfecys
    current_period = cpfecys.current_year_period()
    if request.vars.csvfile != None:
        try:
            file = request.vars.csvfile.file
        except AttributeError:
            response.flash = T('Please upload a file.')
            return dict(success = False,
                file = False,
                periods = periods)
        try:
            cr = csv.reader(file, delimiter=',', quotechar='"')
            success = True
            header = next(cr)
            for row in cr:
                ## parameters
                rusername = row[2] or ''
                rproject = row[0]
                rassignation_length = row[7]
                rpro_bono = (row[8] == 'Si') or (row[8] == 'si')
                rhours = row[9]
                remail = row[5]
                rphone = row[6] or ''
                rlast_name = row[3]
                rfirst_name = row[4]
                ## check if user exists
                usr = db.auth_user(db.auth_user.username == rusername)
                project = db.project(db.project.project_id == rproject)
                if usr is None:
                    ## find it on chamilo (db2)
                    if not uv_off:
                        usr = db2.user_user(db2.user_user.username == rusername)
                        if usr is None:
                            # report error and get on to next row
                            row.append(T('Error: ') + T('User is not valid. \
                                User doesn\'t exist in UV.'))
                            error_users.append(row)
                            continue
                        else:
                            # insert the new user
                            usr = db.auth_user.insert(username = usr.username,
                                                    password = usr.password,
                                                    phone = usr.phone,
                                                    last_name = usr.lastname,
                                                    first_name = usr.firstname,
                                                    email = usr.email)
                            #add user to role 'Teacher'
                            auth.add_membership('Teacher', usr)
                    else:
                        #insert a new user with csv data
                        usr = db.auth_user.insert(username = rusername,
                                                  email = remail,
                                                  first_name=rfirst_name,
                                                  last_name=rlast_name,
                                                  phone=rphone)
                        #add user to role 'Teacher'
                        auth.add_membership('Teacher', usr)
                else:
                    assignation = db.user_project(
                        (db.user_project.assigned_user == usr.id)&
                        (db.user_project.project == project)&
                        (db.user_project.period == current_period)&
                        (db.user_project.assignation_status == None))
                    if assignation != None:
                        row.append(T('Error: ') + T('User \
                         was already assigned, Please Manually Assign Him.'))
                        error_users.append(row)
                        continue
                if project != None:
                    db.user_project.insert(assigned_user = usr,
                                            project = project,
                                            period = current_period,
                                            periods = rassignation_length,
                                            pro_bono = rpro_bono,
                                            hours = rhours)
                else:
                    # project_id is not valid
                    row.append('Error: ' + T('Project code is not valid. \
                     Check please.'))
                    error_users.append(row)
                    continue
        except csv.Error:
            response.flash = T('File doesn\'t seem properly encoded.')
            return dict(success = False,
                file = False,
                periods = periods,
                current_period = current_period)
        response.flash = T('Data uploaded')
        return dict(success = success,
                    errors = error_users,
                    warnings = warning_users,
                    periods = periods,
                    current_period = current_period)
    return dict(success = False,
                file = False,
                periods = periods,
                current_period = current_period)


@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def assignation_upload():
    import csv
    error_users = []
    warning_users = []
    uv_off = request.vars['uv_off'] or False
    success = False
    import cpfecys
    current_period = cpfecys.current_year_period()
    if request.vars.csvfile != None:
        try:
            file = request.vars.csvfile.file
        except AttributeError:
            response.flash = T('Please upload a file.')
            return dict(success = False,
                file = False,
                periods = periods)
        try:
            cr = csv.reader(file, delimiter=',', quotechar='"')
            success = True
            header = next(cr)
            for row in cr:
                ## parameters
                rusername = row[1]
                rproject = row[3]
                rassignation_length = row[4]
                rpro_bono = (row[5] == 'Si') or (row[5] == 'si')
                rhours = row[6]
                remail = row[7]
                ## check if user exists
                usr = db.auth_user(db.auth_user.username == rusername)
                project = db.project(db.project.project_id == rproject)
                if usr is None:
                    ## find it on chamilo (db2)
                    if not uv_off:
                        usr = db2.user_user(db2.user_user.username == rusername)
                        if usr is None:
                            # report error and get on to next row
                            row.append(T('Error: ') + T('User is not valid. \
                                User doesn\'t exist in UV.'))
                            error_users.append(row)
                            continue
                        else:
                            # insert the new user
                            usr = db.auth_user.insert(username = usr.username,
                                                    password = usr.password,
                                                    phone = usr.phone,
                                                    last_name = usr.lastname,
                                                    first_name = usr.firstname,
                                                    email = usr.email)
                            #add user to role 'student'
                            auth.add_membership('Student', usr)
                    else:
                        #insert a new user with csv data
                        usr = db.auth_user.insert(username = rusername,
                                                  email = remail)
                        #add user to role 'student'
                        auth.add_membership('Student', usr)
                else:
                    assignation = db.user_project(
                        (db.user_project.assigned_user == usr.id)&
                        (db.user_project.project == project)&
                        (db.user_project.assignation_status == None))
                    if assignation != None:
                        row.append(T('Error: ') + T('User \
                         was already assigned, Please Manually Assign Him.'))
                        error_users.append(row)
                        #assignation.update_record(periods = \
                            #rassignation_length, pro_bono = \
                            #rpro_bono)
                        continue
                if project != None:
                    db.user_project.insert(assigned_user = usr,
                                            project = project,
                                            period = current_period,
                                            periods = rassignation_length,
                                            pro_bono = rpro_bono,
                                            hours = rhours)
                else:
                    # project_id is not valid
                    row.append('Error: ' + T('Project code is not valid. \
                     Check please.'))
                    error_users.append(row)
                    continue
        except csv.Error:
            response.flash = T('File doesn\'t seem properly encoded.')
            return dict(success = False,
                file = False,
                periods = periods,
                current_period = current_period)
        response.flash = T('Data uploaded')
        return dict(success = success,
                    errors = error_users,
                    warnings = warning_users,
                    periods = periods,
                    current_period = current_period)
    return dict(success = False,
                file = False,
                periods = periods,
                current_period = current_period)

@cache.action()
@auth.requires_login()
@auth.requires_membership('Super-Administrator')
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
@auth.requires_membership('Super-Administrator')
def final_practice():
    #requires parameter year_period if no one is provided then it is 
    #automatically detected
    #and shows the current period
    year_period = request.vars['year_period']
    max_display = 1
    import cpfecys
    currentyear_period = db.period_year(db.period_year.id == year_period)
    if not currentyear_period:
        currentyear_period = cpfecys.current_year_period()
        changid = currentyear_period.id
    grid = SQLFORM.grid((db.user_project.period <= currentyear_period.id)&
              ((db.user_project.period + db.user_project.periods) >  \
                currentyear_period.id))
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
                other_periods = other_periods)

@auth.requires_login()
@auth.requires_membership('Super-Administrator')
def users():
    orderby = dict(auth_user=[db.auth_user.first_name, \
                db.auth_user.username])
    grid = SQLFORM.smartgrid(db.auth_user,linked_tables=['auth_membership','auth_event','auth_cas','user_project'], orderby=orderby)
    return dict(grid = grid)
