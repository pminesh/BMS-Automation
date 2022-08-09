from django.contrib import admin
from BMS_Apps.BMS_Main.models import *

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register Start
# model BMS Module
@admin.register(BMSModule)
class BMSModuleAdmin(admin.ModelAdmin):
    list_display = ('module_name','module_slug','status')
    search_fields = ("module_name__startswith", )
    readonly_fields = ('module_slug',)

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register Start
# model Bms Access Control RFID
@admin.register(BmsAccessControlRFID)
class BmsAccessControlRFIDAdmin(admin.ModelAdmin):
    list_display = ('rfid_number','user','card_type','access_start_time','access_end_time','status')
    search_fields = ("card_type__startswith", )
    list_filter = ('card_type','status')
    list_per_page = 10
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register Start
# model BMS History
@admin.register(BMSHistory)
class BMSHistoryAdmin(admin.ModelAdmin):
    list_display = ('user','history_type','description','createdAt')
    list_filter = ('createdAt',)
    list_per_page = 10
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register Start
# model BMS Permissions
@admin.register(BMSPermissions)
class BMSHistoryAdmin(admin.ModelAdmin):
    list_display = ('module','permission_name','permission_slug','createdAt')
    list_filter = ('module',)
    readonly_fields = ('permission_slug',)
    list_per_page = 10
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register Start
# model BMS Locker
@admin.register(BMSLocker)
class BMSLockerAdmin(admin.ModelAdmin):
    list_display = ('category','subArea','locker_name','status','createdAt')
    list_filter = ('category',)
    list_per_page = 10
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register Start
# model BMS Settings
@admin.register(BMSSettings)
class BMSSettingsAdmin(admin.ModelAdmin):
    list_display = ('module','setting_data','createdAt')
    list_filter = ('module',)
    list_per_page = 10
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register End
