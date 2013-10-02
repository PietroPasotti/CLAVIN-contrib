from django.contrib import admin
from models import GDELT 

class GDELTAdmin(admin.ModelAdmin):
    pass

admin.site.register(GDELT, GDELTAdmin)
