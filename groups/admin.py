from django.contrib import admin

from .models import Group

# ["title", "start_year", "finish_year", "student_quantity"]
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
	save_on_top = True
	list_per_page = 30
	list_display = ("title", "start_year", "finish_year", "student_quantity")
	list_filter = ("start_year", "student_quantity")
	search_fields = ("title__startswith", )
