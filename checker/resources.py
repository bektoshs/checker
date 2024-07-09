from import_export import resources
from .models import Website

class WebsiteResource(resources.ModelResource):
    class Meta:
        model = Website
        import_id_fields = ('address',)
        fields = ('id', 'address', 'status')

    def before_import_row(self, row, **kwargs):
        address = row('address')
        if Website.objects.filter(address=address).exists():
            row['status'] = 'update'  # already exists

    def before_import(self, dataset, dry_run, **kwargs):
        for row in dataset.dict:
            self.before_import_row(row)