from django.contrib import admin
from . import models


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'sub_title',
        'thumbnail',
        'description',
        'icon',
        'period_start',
        'period_end',
        'tag',
        'position',
    )
    list_editable = (
        'sub_title',
        'thumbnail',
        'description',
        'icon',
        'period_start',
        'period_end',
        'tag',
        'position',
    )


admin.site.register(models.ProjectDetail, ProjectAdmin)
