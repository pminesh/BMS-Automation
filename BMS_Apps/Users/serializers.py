from rest_framework import serializers
from .models import *
from BMS_Apps.Areas.models import Department
from BMS_Apps.BMS_Main.models import BMSModule

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Serializer Start
# Serializer for user details
class UserSerializer(serializers.ModelSerializer):
    user_type_name = serializers.SerializerMethodField()
    role_name = serializers.SerializerMethodField()
    class Meta:
        model = UserBMS
        fields = ('id', 'user_type','user_type_name','password','role', 'role_name', 'user_email','status')
        
    def get_user_type_name(self, obj):
        try:
            UserTypeObj = UserType.objects.get(id=int(obj.user_type.id))
            return UserTypeObj.type_name
        except Exception:
            return None

    def get_role_name(self, obj):
        try:
            UserRoleObj = UserRole.objects.get(id=int(obj.role.id))
            return UserRoleObj.role_name
        except Exception:
            return None
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Serializer End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Serializer Start
# Serializer for visitor profile details
class VisitorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserVisitorDetail
        fields = ('id', 'user', 'first_name', 'last_name', 'address','phone_no')
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Serializer End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Serializer Start
# Serializer for staff profile details
class StaffProfileSerializer(serializers.ModelSerializer):
    department_name = serializers.SerializerMethodField()
    class Meta:
        model = UserStaffDetail
        fields = ('id', 'user', 'first_name', 'last_name', 'image', 'birthdate', 'department','department_name','address','phone_no')

    def get_department_name(self, obj):
        try:
            deptObj = Department.objects.get(id=int(obj.department.id))
            return deptObj.name
        except Exception:
            return None
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Serializer End


# Manage Roles Serializers
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Serializer Start
# Serializer for role
class RoleSerializers(serializers.ModelSerializer):
     class Meta:
        model = UserRole
        fields = ('id', 'role_name','permission_ids')
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Serializer End
