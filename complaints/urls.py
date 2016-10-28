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
]
