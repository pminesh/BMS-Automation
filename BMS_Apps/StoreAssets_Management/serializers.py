from rest_framework import serializers
from .models import *

# Manage Store/Assets Serializers
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Serializer Start
# Serializer for Assets Type
class AssetsTypeSerializers(serializers.ModelSerializer):
     class Meta:
        model = AssetsType
        fields = ('id', 'type_name','description')
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Serializer End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Serializer Start
# Serializer for Assets Details
class AssetsDetailsSerializers(serializers.ModelSerializer):
     class Meta:
        model = AssetsDetails
        fields = ('id', 'assets_type','name', 'purchase_description','purchase_date', 'expiry_date','price','stock_quantity')
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Serializer End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Serializer Start
# Serializer for Assets Manage
class ManageAssetsSerializers(serializers.ModelSerializer):
     class Meta:
        model = ManageAssets
        fields = ('id','assets','sub_area','user','stock_quantity','alert_message')
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Serializer End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Serializer Start
# Serializer for Assets Service
class AssetsServiceSerializers(serializers.ModelSerializer):
     class Meta:
        model = AssetsService
        fields = ('id','service_name','provider_details')
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Serializer End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Serializer Start
# Serializer for Service For Assets
class ServiceForAssetsSerializers(serializers.ModelSerializer):
     class Meta:
        model = ServiceForAssets
        fields = ('id','assets','service','service_information','status')
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Serializer End