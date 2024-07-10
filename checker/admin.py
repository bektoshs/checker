import re

from django.contrib import admin
from import_export import resources
from import_export.formats.base_formats import XLSX
from import_export.admin import ImportExportMixin
from .models import Website
import re


def clean_address(address):
    # Regex pattern to match 'http://' or 'https://'
    pattern = re.compile(r'^https?://')
    # Replace 'http://' or 'https://' with an empty string
    cleaned_address = pattern.sub('', address)
    return cleaned_address

class WebsiteResource(resources.ModelResource):
    class Meta:
        model = Website
        fields = ('address', 'status')

    def before_import_row(self, row, row_number=None, **kwargs):
        address = row.get('address')
        if address:
            # Clean the address
            address = clean_address(address)
            row['address'] = address
        if Website.objects.filter(address=address).exists():
            row['id'] = Website.objects.get(address=address).id

    def before_save_instance(self, instance, using_transactions, dry_run):
        # Clean the address before saving the instance
        instance.address = clean_address(instance.address)
        return super().before_save_instance(instance, using_transactions, dry_run)

class WebsiteAdmin(ImportExportMixin, admin.ModelAdmin):
    resources = WebsiteResource
    formats = [XLSX]
    list_display = ['address', 'status']


admin.site.register(Website, WebsiteAdmin)
