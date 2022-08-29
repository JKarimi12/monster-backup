from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from backup.models import Backup


@admin.register(Backup)
class BackupAdmin(ModelAdmin):
    list_display = (
        'dir_path',
        'crontab',
        'dest_dir_path',
    )

    fields = list_display
