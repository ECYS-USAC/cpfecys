# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

@auth.requires_login()
@auth.requires_membership('Magazine')
def management_magazine():
	query = db.magazine
	grid = SQLFORM.smartgrid(query)
	return dict(grid=grid)