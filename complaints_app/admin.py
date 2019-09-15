from django.contrib import admin
from complaints_app.models import Grievant,Department,Complaint
# Register your models here.
admin.site.register(Grievant)
admin.site.register(Complaint)
admin.site.register(Department)
