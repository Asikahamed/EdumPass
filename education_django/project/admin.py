from django.contrib import admin

# Register your models here.
from .models import Category, Project, Lesson

admin.site.register(Category)
admin.site.register(Project)
admin.site.register(Lesson)