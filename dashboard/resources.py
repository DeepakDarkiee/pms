from import_export import resources
from .models import Lic

class LicResource(resources.ModelResource):
    class Meta:
        model = Lic
