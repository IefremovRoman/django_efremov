from django.contrib import admin

from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    save_on_top = True
    list_per_page = 30
    list_display = ("last_name", "first_name", "age", "subject", "phone", "group_attached")
    list_filter = ("age", "subject")
    search_fields = ("last_name__startswith",)

    def group_attached(self, obj):
        from groups.models import Group
        group = Group.objects.filter(teacher_id_id=obj.id).values()
        if group.exists():
            group = group[0]
            return f"Title: {group.get('title')} " \
                   f"Id: {group.get('id')}"
        else:
            return '-'
