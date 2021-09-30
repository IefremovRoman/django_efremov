from django.contrib import admin

from .models import Student, Logger


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	save_on_top = True
	list_per_page = 30
	list_display = ("last_name", "first_name", "age", "phone")
	list_filter = ("age", "first_name")
	search_fields = ("last_name__startswith", )


@admin.register(Logger)
class Logging(admin.ModelAdmin):
    list_display = ['method', 'path', 'created', 'execution_time']
    list_filter = ['method', 'created']
