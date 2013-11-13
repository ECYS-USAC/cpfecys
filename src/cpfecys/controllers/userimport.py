# coding: utf8
# try something like
import csv
@auth.requires_login()
def index():
    newUsrs = {}
    errUsrs = {}
    existUsers ={}
    exisIndex = 0
    UsrIndx = 0
    errIndx = 0
    success = False
    if request.vars.csvfile != None:
        file = request.vars.csvfile.file
        cr = csv.reader(file, delimiter=',', quotechar='|')
        success = True
        header = next(cr)
        for row in cr:   
            user = None
            user = db2(db2.user_user.username==row[1]).select().first()
            if user is None:
                errUsrs[errIndx] = row[1]
                errIndx = errIndx + 1
            else:
                currentUser = None
                currentUser = db(db.auth_user.username==user.username).select().first()
                if currentUser is None:
                    phone = ''
                    area = None
                    first_name = ''
                    first_name = row[2]
                    phone = row[3]
                    email = row[4]                    
                    areacode = row[10]
                    pro_bono = row[8]
                    cycles = row[9]
                    area = db(db.project_area.id==row[10]).select().first()
                    
                    if area:
                        tempUser = db.auth_user.insert(username=user.username, \
                        first_name=first_name, email=email, pro_bono=pro_bono, \
                        phone=phone)
                        db.user_area.insert(student=tempUser, project_area=area)
                    
                    newUsrs[UsrIndx] = first_name + ' :' + area.name
                    UsrIndx = UsrIndx + 1
                else:
                    existUsers[exisIndex] = row[1]
                    exisIndex = exisIndex + 1
        
        response.flash = T('Data uploaded')
        return dict(success=success, data=newUsrs, errors=errUsrs, existUsers=existUsers)
    else:
        return dict(success=False, file=False)
