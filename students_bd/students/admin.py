from django.contrib import admin
from students.models import Group, Student

class StudentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Group)
admin.site.register(Student)
