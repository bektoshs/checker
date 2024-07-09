from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Website
from .resources import WebsiteResource


@admin.register(Website)
class WebsiteAdmin(ImportExportModelAdmin):
    resource_class = WebsiteResource
    list_display = ('address', 'status')
