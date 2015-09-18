from django.contrib import admin

from .models import Directory


@admin.register(Directory)
class DirectoryAdmin(admin.ModelAdmin):
    pass
