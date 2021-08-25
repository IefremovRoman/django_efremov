from django.contrib import admin

from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	save_on_top = True
	list_per_page = 30
	list_display = ("last_name", "first_name", "age", "phone")
	list_filter = ("age", "first_name")
	search_fields = ("last_name__startswith", )
