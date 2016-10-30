from django.conf.urls import url
from django.contrib import admin
from reports import views

urlpatterns = [
	url(r'^$', views.reports, name='reports'),
	url(r'^monthly-detail/(?P<report_type>[\w\-0-9]+)/$', views.monthly_detail, name='monthly_detail'),
]