from django.contrib import admin
from .models import *

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register Start
# model Assets Type

@admin.register(AssetsType)
class AssetsTypeAdmin(admin.ModelAdmin):
    list_display = ('type_name', 'description', 'createdAt')
    list_per_page = 10
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register Start
# model Assets Details

@admin.register(AssetsDetails)
class AssetsDetailsAdmin(admin.ModelAdmin):
    list_display = ('assets_type', 'name', 'purchase_description','purchase_date','expiry_date','price','stock_quantity','createdAt')
    search_fields = ("assets_type", )
    list_per_page = 10
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register Start
# model Manage Assets

@admin.register(ManageAssets)
class ManageAssetsAdmin(admin.ModelAdmin):
    list_display = ('assets', 'sub_area', 'user', 'stock_quantity','alert_message','createdAt')
    list_per_page = 10
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register Start
# model Assets Service

@admin.register(AssetsService)
class AssetsServiceAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'provider_details', 'createdAt')
    list_per_page = 10
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register Start
# model Service For Assets

@admin.register(ServiceForAssets)
class ServiceForAssetsAdmin(admin.ModelAdmin):
    list_display = ('assets', 'service', 'service_information','status')
    search_fields = ("status", )
    list_per_page = 10
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register End