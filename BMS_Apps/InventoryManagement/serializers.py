from rest_framework import serializers
from .models import *

# Manage Store/Assets Serializers
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Serializer Start
# Serializer for Inventory Category
class InventoryCategorySerializers(serializers.ModelSerializer):
     class Meta:
        model = InventoryCategory
        fields = ('id', 'category_name','category_image','status')
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Serializer End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Serializer Start
# Serializer for Item Detail
class ItemDetailSerializers(serializers.ModelSerializer):
     class Meta:
        model = ItemDetail
        fields = ('id', 'category','item_name', 'item_description','item_image', 'price','unit','quantity','minimum_quantity','status')
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Serializer End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Serializer Start
# Serializer for Manage Inventory Stock
class ManageInventoryStockSerializers(serializers.ModelSerializer):
     class Meta:
        model = ManageInventoryStock
        fields = ('id','item','supplier_name','stock_quantity','unit','price','discount','total','tax','grand_total')
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Serializer End
