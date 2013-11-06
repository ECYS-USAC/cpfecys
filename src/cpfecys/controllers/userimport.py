# coding: utf8
# try something like
import csv
@auth.requires_login()
def index():
    newUsrs = {}
    errUsrs = {}
    UsrIndx = 0
    errIndx = 0
    success = False
    if request.vars.csvfile != None:
        file = request.vars.csvfile.file
        cr = csv.reader(file, delimiter=',', quotechar='|')
        success = True
        
        for row in cr:    
            user = None
            user = db2(db2.user_user.username==row[0]).select().first()
            
            if user is None:
                newUsrs[UsrIndx] = row[0]
                UsrIndx = UsrIndx + 1
            else:
                errUsrs[errIndx] = row[0]
                errIndx = errIndx + 1
        
        response.flash = T('Data uploaded')
        return dict(success=success, data=newUsrs, errors=errUsrs)
    else:
        return dict(success=False, file=False)
