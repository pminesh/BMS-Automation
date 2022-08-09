from django.contrib import admin
from BMS_Apps.HousekeepingAndGuardManagement.models import *

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register Start
# model Housekeeping Guard Service
@admin.register(HousekeepingGuardService)
class HousekeepingGuardServiceAdmin(admin.ModelAdmin):
    list_display = ('service_name','status')
    list_filter = ('status',)
    list_per_page = 10
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register Start
# model Housekeeping Guard Details
@admin.register(HousekeepingGuardDetails)
class HousekeepingGuardDetailsAdmin(admin.ModelAdmin):
    list_display = ('sub_area','service','user','start_time','end_time','status')
    list_filter = ('status',)
    list_per_page = 10
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register End

