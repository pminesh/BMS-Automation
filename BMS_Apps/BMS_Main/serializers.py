from rest_framework import serializers
from .models import BMSLocker, BMSModule
from BMS_Apps.Areas.models import SubArea

# Manage Roles Serializers
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Serializer Start
# Serializer for role
class ModuleSerializers(serializers.ModelSerializer):
    class Meta:
        model = BMSModule
        fields = ('id', 'module_name','module_slug','status')
        extra_kwargs = {
            'module_slug':{'required':False},
        }
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Serializer End

# Manage locker Serializers
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Serializer Start
# Serializer for locker
class LockerSerializers(serializers.ModelSerializer):
    subArea_name = serializers.SerializerMethodField()
    class Meta:
        model = BMSLocker
        fields = ('id', 'category','subArea','subArea_name','locker_name','status')

    def get_subArea_name(self,obj):
        try:
            sub_area_data = SubArea.objects.get(id=obj.subArea.id)
            return sub_area_data.name
        except Exception as e:
            return None
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Serializer End