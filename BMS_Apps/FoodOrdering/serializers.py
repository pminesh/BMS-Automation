from tkinter import N
from rest_framework import serializers
from .models import *
from BMS_Apps.Areas.models import SubArea

# Manage Pentry Serializers
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Serializer Start
# Serializer for Food Category
class FoodCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = FoodCategory
        fields = ('id', 'name')
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Serializer End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Serializer Start
# Serializer for Food 
class FoodSerializers(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    class Meta:
        model = Food
        fields = ('id', 'category','category_name','food_name','price','description')
    
    def get_category_name(self,obj):
        try:
            category_data = FoodCategory.objects.get(id=obj.category.id)
            return category_data.name
        except Exception as e:
            return None
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Serializer End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Serializer Start
# Serializer for Food Menu
class FoodMenuSerializers(serializers.ModelSerializer):
    class Meta:
        model = FoodMenu
        fields = ('id', 'food_ids','menu_name','image','price')
    
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Serializer End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Serializer Start
# Serializer for Food Order
class FoodOrderSerializers(serializers.ModelSerializer):
    sub_area_name = serializers.SerializerMethodField()
    menu_name = serializers.SerializerMethodField()

    class Meta:
        model = FoodOrderDetails
        fields = ('id', 'user','from_sub_area','sub_area_name','menu','menu_name','quantity','price','status')
    
    def get_sub_area_name(self,obj):
        try:
            subArea_data = SubArea.objects.get(id=obj.from_sub_area.id)
            return subArea_data.name
        except Exception as e:
            return None
    
    def get_menu_name(self,obj):
        try:
            menu_data = FoodMenu.objects.get(id=obj.menu.id)
            return menu_data.menu_name
        except Exception as e:
            return None
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Serializer End