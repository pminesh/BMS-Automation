from django.contrib import admin
from .models import *

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register Start
# model Inventory Category

@admin.register(InventoryCategory)
class InventoryCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'category_image', 'status','createdAt')
    search_fields = ("status", )
    list_per_page = 10
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register Start
# model Item Detail

@admin.register(ItemDetail)
class ItemDetailAdmin(admin.ModelAdmin):
    list_display = ('category', 'item_name', 'item_description', 'item_image', 'price', 'unit', 'quantity', 'minimum_quantity', 'status','createdAt')
    search_fields = ("status", )
    list_per_page = 10
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register Start
# model Manage Inventory Stock

@admin.register(ManageInventoryStock)
class ManageInventoryStockAdmin(admin.ModelAdmin):
    list_display = ('item', 'supplier_name', 'stock_quantity', 'unit', 'price', 'discount', 'total', 'tax', 'grand_total','createdAt')
    list_per_page = 10
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register End
