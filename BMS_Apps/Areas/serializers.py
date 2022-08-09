from rest_framework import serializers
from .models import *
# Manage Area Serializers
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Serializer Start
# Serializer for Floor
class FloorSerializers(serializers.ModelSerializer):
     class Meta:
        model = Floor
        fields = ('id', 'name')
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Serializer End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Serializer Start
# Serializer for Department
class DepartmentSerializers(serializers.ModelSerializer):
    floor_name = serializers.SerializerMethodField()
    class Meta:
        model = Department
        fields = ('id', 'name','floor','floor_name')

    def get_floor_name(self, obj):
        try:
            floor_data = Floor.objects.get(id=int(obj.floor.id))
            return floor_data.name
        except Exception:
            return None
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Serializer End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Serializer Start
# Serializer for Sub Area
class SubAreaSerializers(serializers.ModelSerializer):
    dept_name = serializers.SerializerMethodField()
    class Meta:
        model = SubArea
        fields = ('id', 'name','on_image_path','off_image_path','width','height','department','dept_name','seating_capacity')

    def get_dept_name(self, obj):
        try:
            dept_data = Department.objects.get(id=int(obj.department.id))
            return dept_data.name
        except Exception:
            return None
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Serializer End