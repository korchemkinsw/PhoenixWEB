from django.contrib import admin

from .models import Advancesearchtemplates

class AdvancesearchtemplatesAdmin(admin.ModelAdmin):
  list_display = ('id', 'typeoptions', 'templatename', 'sqlstring')

admin.site.register(Advancesearchtemplates, AdvancesearchtemplatesAdmin)
