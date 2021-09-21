
from django.contrib import admin

from .models import Question, Employee, Choice, Project

admin.site.register(Question)
admin.site.register(Employee)
admin.site.register(Choice)
admin.site.register(Project)