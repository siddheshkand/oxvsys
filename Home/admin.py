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


class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'contact_nos',
        'message',
        'requirements',
    )


admin.site.register(models.ProjectDetail, ProjectAdmin)
admin.site.register(models.CustomerDetail, CustomerAdmin)
