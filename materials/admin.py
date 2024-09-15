from django.contrib import admin
from materials.models import Course, Lesson

@admin.register(Course)
class Course(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'owner',)
    list_filter = ('id', 'title', 'owner',)

@admin.register(Lesson)
class Lesson(admin.ModelAdmin):
    list_display = ('id', 'course', 'title', 'description', 'owner',)
    list_filter = ('id', 'title', 'owner',)

# Register your models here.
