from django.conf.urls import url
from django.contrib import admin
from complaints import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^new-complaint$', views.new_complaint, name='new_complaint'),
	url(r'^search-complaint$', views.search_complaint, name='search_complaint'),
	url(r'^update-complaint/(?P<complaint_number>[\w\-0-9]+)/$', views.update_complaint, name='update_complaint'),
	url(r'^users/$', views.users, name='users'),
	url(r'^users/add/$', views.add_user, name='add_user'),
	url(r'^users/update/(?P<username>[\w\-0-9]+)/$', views.update_user, name='update_user'),
	url(r'^platforms/$', views.platforms, name='platforms'),
	url(r'^platforms/add/$', views.add_platform, name='add_platform'),
	url(r'^platforms/update/(?P<platform_id>[\w\-0-9]+)/$', views.update_platform, name='update_platform'),
	url(r'^platforms/delete/(?P<platform_id>[\w\-0-9]+)/$', views.delete_platform, name='delete_platform'),
	url(r'^categories/$', views.categories, name='categories'),
	url(r'^categories/add/$', views.add_category, name='add_category'),
	url(r'^categories/update/(?P<category_id>[\w\-0-9]+)/$', views.update_category, name='update_category'),
	url(r'^categories/delete/(?P<category_id>[\w\-0-9]+)/$', views.delete_category, name='delete_category'),
	url(r'^offices/$', views.offices, name='offices'),
	url(r'^offices/add/$', views.add_office, name='add_office'),
	url(r'^offices/update/(?P<office_id>[\w\-0-9]+)/$', views.update_office, name='update_office'),
	url(r'^offices/delete/(?P<office_id>[\w\-0-9]+)/$', views.delete_office, name='delete_office'),
]
