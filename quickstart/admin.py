from django.contrib import admin
from quickstart.models import Student
# Register your models here.
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('id','last_name','first_name',)
admin.site.register(Student, StudentsAdmin)