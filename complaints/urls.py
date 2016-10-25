from django.conf.urls import url
from django.contrib import admin
from complaints import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^login/$', views.user_login, name='login')
]
