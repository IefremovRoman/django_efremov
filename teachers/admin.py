from django.contrib import admin

from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
	save_on_top = True
	list_per_page = 30
	list_display = ("last_name", "first_name", "age", "subject")
	list_filter = ("age", "subject")
	search_fields = ("last_name__startswith", )
