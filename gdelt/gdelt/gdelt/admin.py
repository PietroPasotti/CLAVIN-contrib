from django.contrib import admin
from models import GDELT 

class GDELTAdmin(admin.ModelAdmin):
    search_fields = ('SQLDATE', 'MonthYear', 'Year', 'Actor1Code', 'Actor2Code', 'QuadClass', 'EventCode', 'ActionGeo_CountryCode')
    list_display = ('SQLDATE', 'MonthYear', 'Year', 'Actor1Code', 'Actor2Code', 'QuadClass', 'EventCode', 'ActionGeo_CountryCode')

admin.site.register(GDELT, GDELTAdmin)
