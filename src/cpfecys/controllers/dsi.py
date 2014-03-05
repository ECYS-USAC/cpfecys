# coding: utf8

@auth.requires_login()
@auth.requires_membership('DSI')
def index():
	period = cpfecys.current_year_period()
	restrictions = db(
		(db.item_restriction.item_type==db.item_type(name='Activity'))& \
		(db.item_restriction.period==period.id)).select()
	return dict(restrictions=restrictions)

def item_detail():
	period = cpfecys.current_year_period()
	restriction = request.vars['restriction']
	valid = restriction != None and restriction != ''
	if not valid:
		session.flash = T('Not valid item list select a valid item list.')
		redirect(URL('dsi', 'index'))
	restrictions = db(
		(db.item_restriction.item_type==db.item_type(name='Activity'))& \
		(db.item_restriction.period==period.id)&
		(db.item_restriction.id==restriction))
	def get_areas(restriction):
		areas = db((db.item_restriction_area.item_restriction==restriction.id)&
			(db.area_level.id==db.item_restriction_area.area_level))
		return areas
	def get_projects(area,restriction):
		projects = db((db.project.area_level==db.area_level.id)&
			(db.area_level.id==area.id)&
			(db.item_restriction.id==restriction.id)&
			(db.item_restriction_area.area_level==area.id)&
			(db.item_restriction_area.item_restriction==restriction.id)&
			(db.item_restriction_area.item_restriction==db.item_restriction.id)&
			(db.item_restriction_area.area_level==db.area_level.id)&
			(db.item_restriction_area.is_enabled==True))
		return projects
	def is_exception(project, restriction):
		restriction = db((db.item_restriction_exception.project==project.id)&
			(db.item_restriction_exception.item_restriction== \
				restriction.id))
		return restriction.count() != 0
	def get_students(project):
		target_period = period.id + 1
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
		return assignations
		return 'uno'
	return dict(restrictions=restrictions,
		get_areas=get_areas,
		get_projects=get_projects,
		is_exception=is_exception,
		get_students=get_students)