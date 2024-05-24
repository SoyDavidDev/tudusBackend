from django.contrib import admin

from .models import List
# Register your models here.


class ListAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'user_id')
    list_filter = ('created_at', 'updated_at', 'user_id')
    search_fields = ('title', 'user_id')
    ordering = ('-id',)



admin.site.register(List, ListAdmin)