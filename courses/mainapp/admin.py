from django.contrib import admin
from .models import *

admin.site.register(Teacher)
admin.site.register(Courses)
admin.site.register(Student)
admin.site.register(Toolbox)
admin.site.register(WorkDay)
admin.site.register(WorkTime)
admin.site.register(Timetable)

