from django.contrib import admin
from BMS_Apps.Devices.models import *

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register Start
# model Device Type
@admin.register(DeviceType)
class DeviceTypeAdmin(admin.ModelAdmin):
    list_display = ('name','createdAt')
    list_per_page = 10
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register Start
# model App Type
@admin.register(AppType)
class AppTypeAdmin(admin.ModelAdmin):
    list_display = ('name','device_type','createdAt')
    list_filter = ('device_type',)
    list_per_page = 10
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register Start
# model Device
@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('device_name','app_type','is_used','status','subArea','createdAt')
    list_filter = ('app_type','is_used')
    list_per_page = 10
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register Start
# model Device Has User
@admin.register(DeviceHasUser)
class DeviceHasUserAdmin(admin.ModelAdmin):
    list_display = ('device','user')
    list_filter = ('user',)
    list_per_page = 10
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register Start
# model Device Status
@admin.register(DeviceStatus)
class DeviceStatusAdmin(admin.ModelAdmin):
    list_display = ('user','device','device_status','createdAt')
    list_filter = ('user','device_status')
    list_per_page = 10
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register End
