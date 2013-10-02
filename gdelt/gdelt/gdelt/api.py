from tastypie.resources import ModelResource
from models import GDELT


class GDELTResource(ModelResource):
    class Meta:
        queryset = GDELT.objects.all()
        resource_name = 'gdelt'

