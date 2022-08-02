from django.contrib import admin

# Register your models here.

from .models import Questions
from .models import Student
admin.site.register(Questions)
admin.site.register(Student)