# coding: utf8
# try something like
import csv
@auth.requires_login()
def loadcsv():
    string = ''
    if request.vars.csvfile != None:
        file = request.vars.csvfile.file
        response.flash = T('Data uploaded')
        content = file.read()
        return dict(file=content)
    else:
        return dict(file=False)
