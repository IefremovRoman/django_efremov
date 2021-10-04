from django.contrib import admin

from .models import Student, Logger


# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    save_on_top = True
    list_per_page = 30
    list_display = (
        "last_name",
        "first_name",
        "age",
        "phone",
        "group_name_and_id",
        "group_teacher")
    list_filter = ("age", "first_name", "group_id")
    search_fields = ("last_name__startswith",)

    def group_name_and_id(self, obj):
        from groups.models import Group
        group = Group.objects.filter(id=obj.group_id_id).values()[0]
        return f"Title: {group.get('title')} " \
               f"Id: {group.get('id')}"

    def group_teacher(self, obj):
        from groups.models import Group
        from teachers.models import Teacher
        teacher_id = Group.objects.filter(id=obj.group_id_id).values()[0].get('teacher_id_id')
        teacher = Teacher.objects.filter(id=teacher_id).values()[0]
        return f"Name: {teacher.get('first_name')} " \
               f"{teacher.get('last_name')} " \
               f"Id: {teacher.get('id')}"


# def category_post_count(self, obj):
# 	return obj.post_set.count()


@admin.register(Logger)
class Logging(admin.ModelAdmin):
    list_display = ['method', 'path', 'created', 'execution_time']
    list_filter = ['method', 'created']
