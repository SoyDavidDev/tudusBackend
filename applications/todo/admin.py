from django.contrib import admin

from .models import Todo
# Register your models here.


class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed', 'created_at', 'updated_at', 'list_id', 'user_id')
    list_filter = ('completed', 'created_at', 'updated_at')
    search_fields = ('title', 'description', 'list_id', 'user_id')
    ordering = ('-id',)


admin.site.register(Todo, TodoAdmin)