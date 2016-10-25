from django.contrib import admin
from complaints.models import Office, Category, Platform, Complaint

admin.site.register(Office)
admin.site.register(Category)
admin.site.register(Platform)
admin.site.register(Complaint)