from django.contrib import admin

from .models import Group


# ["title", "start_year", "finish_year", "student_quantity"]
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    save_on_top = True
    list_per_page = 30
    list_display = ("title", "start_year", "finish_year", "student_quantity", "teacher_of_group")
    list_filter = ("start_year", "student_quantity")
    search_fields = ("title__startswith",)

    def teacher_of_group(self, obj):
        from teachers.models import Teacher
        teacher = Teacher.objects.filter(id=obj.teacher_id_id).values()[0]
        return f"Name: {teacher.get('first_name')} " \
               f"{teacher.get('last_name')} " \
               f"Id: {teacher.get('id')}"
