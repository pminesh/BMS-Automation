from rest_framework.views import APIView
from .models import *
from .serializers import AssetsTypeSerializers, AssetsDetailsSerializers, ManageAssetsSerializers, AssetsServiceSerializers, ServiceForAssetsSerializers
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from rest_framework.schemas.openapi import AutoSchema

# ******************************************************************************************************************
# ******************************************* Manage Assets ********************************************************
# ******************************************************************************************************************

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API Start
# This API is used for add Assets type and get all Assets type list.
# type:Web API
# form-data,raw
# add Assets type: request raw:{ "type_name":"Machinery","description":"Machinery description"}


class AssetsTypeAddList(APIView):
    def get(self, request):
        try:
            assets_data = AssetsType.objects.all()
            serializer = AssetsTypeSerializers(assets_data, many=True)
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Assets type list",
                "response": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        try:
            serializer = AssetsTypeSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "data": "true",
                    "status_code": "200",
                    "message": "Assets type created successfully"
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "data": "false",
                    "status_code": "400",
                    "message": "Invalid data"
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API Start
# This API is used for update, delete and view Assets type.
# type:Web API
# form-data,raw
# update Assets type::>request raw:{ "type_name":"Machinery","description":"Machinery description"}


class AssetsTypeUpdateDeleteDetails(APIView):
    def get_object(self, pk):
        try:
            return AssetsType.objects.get(id=pk)
        except AssetsType.DoesNotExist as e:
            raise Http404 from e

    def get(self, request, pk, format=None):
        assetsType_data = self.get_object(pk)
        try:
            serializer = AssetsTypeSerializers(assetsType_data)
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Assets type details",
                "response": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        assetsType_data = self.get_object(pk)
        try:
            serializer = AssetsTypeSerializers(
                assetsType_data, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "data": "true",
                    "status_code": "200",
                    "message": "Assets type updated successfully"
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "data": "false",
                    "status_code": "400",
                    "message": "Invalid data"
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        assetsType_data = self.get_object(pk)
        try:
            assetsType_data.delete()
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Assets type delete successfully"
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API Start
# This API is used for add Assets type and get all Assets type list.
# type:Web API
# form-data,raw
# add Assets type: request raw:{"assets_type": 3,"name": "drill presses","purchase_description": "machinery", "purchase_date": "2022-07-20", "expiry_date": "2022-07-26", "price": "2000.00", "stock_quantity": 2}


class AssetsDetailsAddList(APIView):
    def get(self, request):
        try:
            assets_details_data = AssetsDetails.objects.all()
            serializer = AssetsDetailsSerializers(
                assets_details_data, many=True)
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Assets details list",
                "response": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        try:
            serializer = AssetsDetailsSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "data": "true",
                    "status_code": "200",
                    "message": "Assets details created successfully"
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "data": "false",
                    "status_code": "400",
                    "message": "Invalid data"
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API Start
# This API is used for update, delete and view Assets details.
# type:Web API
# form-data,raw
# update Assets details::>request raw:{"assets_type": 3,"name": "drill presses","purchase_description": "machinery", "purchase_date": "2022-07-20", "expiry_date": "2022-07-26", "price": "2000.00", "stock_quantity": 2}


class AssetsDetailsUpdateDelete(APIView):
    def get_object(self, pk):
        try:
            return AssetsDetails.objects.get(id=pk)
        except AssetsDetails.DoesNotExist as e:
            raise Http404 from e

    def get(self, request, pk, format=None):
        assets_details_data = self.get_object(pk)
        try:
            serializer = AssetsDetailsSerializers(assets_details_data)
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Assets details details",
                "response": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        assets_details_data = self.get_object(pk)
        try:
            serializer = AssetsDetailsSerializers(
                assets_details_data, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "data": "true",
                    "status_code": "200",
                    "message": "Assets details updated successfully"
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "data": "false",
                    "status_code": "400",
                    "message": "Invalid data"
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        assets_details_data = self.get_object(pk)
        try:
            assets_details_data.delete()
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Assets details delete successfully"
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API Start
# This API is used for add Assets manage and get all Assets manage list.
# type:Web API
# form-data,raw
# add Assets manage: request raw:{"assets": 1,"sub_area": 1,"user": 3,"stock_quantity": 100,"alert_message": "Good Morning"}


class AssetsManageAddList(APIView):
    def get(self, request):
        try:
            assets_manage_data = ManageAssets.objects.all()
            serializer = ManageAssetsSerializers(assets_manage_data, many=True)
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Assets manage list",
                "response": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        try:
            serializer = ManageAssetsSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "data": "true",
                    "status_code": "200",
                    "message": "Assets manage created successfully"
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "data": "false",
                    "status_code": "400",
                    "message": "Invalid data"
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API Start
# This API is used for update, delete and view Assets manage.
# type:Web API
# form-data,raw
# update Assets manage::>request raw:{"assets": 1,"sub_area": 1,"user": 3,"stock_quantity": 100,"alert_message": "Good Morning"}


class AssetsManageUpdateDeleteDetails(APIView):
    def get_object(self, pk):
        try:
            return ManageAssets.objects.get(id=pk)
        except ManageAssets.DoesNotExist as e:
            raise Http404 from e

    def get(self, request, pk, format=None):
        assets_manage_data = self.get_object(pk)
        try:
            serializer = ManageAssetsSerializers(assets_manage_data)
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Assets manage details",
                "response": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        assets_manage_data = self.get_object(pk)
        try:
            serializer = ManageAssetsSerializers(
                assets_manage_data, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "data": "true",
                    "status_code": "200",
                    "message": "Assets manage updated successfully"
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "data": "false",
                    "status_code": "400",
                    "message": "Invalid data"
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        assets_manage_data = self.get_object(pk)
        try:
            assets_manage_data.delete()
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Assets manage delete successfully"
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API Start
# This API is used for add Assets service and get all Assets service list.
# type:Web API
# form-data,raw
# add Assets service: request raw:{"service_name": "PUC","provider_details": {"name": "mayur","age": 24}}


class AssetsServiceAddList(APIView):
    def get(self, request):
        try:
            assets_service_data = AssetsService.objects.all()
            serializer = AssetsServiceSerializers(
                assets_service_data, many=True)
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Assets service list",
                "response": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        try:
            serializer = AssetsServiceSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "data": "true",
                    "status_code": "200",
                    "message": "Assets service created successfully"
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "data": "false",
                    "status_code": "400",
                    "message": "Invalid data"
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API Start
# This API is used for update, delete and view Assets service.
# type:Web API
# form-data,raw
# update Assets service::>request raw:{"service_name": "PUC","provider_details": {"name": "mayur","age": 24}}


class AssetsServiceUpdateDeleteDetails(APIView):
    def get_object(self, pk):
        try:
            return AssetsService.objects.get(id=pk)
        except AssetsService.DoesNotExist as e:
            raise Http404 from e

    def get(self, request, pk, format=None):
        try:
            assets_service_data = self.get_object(pk)
            serializer = AssetsServiceSerializers(assets_service_data)
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Assets service details",
                "response": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        try:
            assets_service_data = self.get_object(pk)
            serializer = AssetsServiceSerializers(
                assets_service_data, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "data": "true",
                    "status_code": "200",
                    "message": "Assets service updated successfully"
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "data": "false",
                    "status_code": "400",
                    "message": "Invalid data"
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        try:
            assets_service_data = self.get_object(pk)
            assets_service_data.delete()
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Assets service delete successfully"
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API Start
# This API is used for add service for assets and get all service for assets list.
# type:Web API
# form-data,raw
# add service for assets: request raw:{"assets": 3,"service": 1,"service_information": {"expiry_date": "28/09/2022","price": 20000},"status": "in-active"}


class ServiceForAssetsAddList(APIView):
    def get(self, request):
        try:
            serviceforassets_data = ServiceForAssets.objects.all()
            serializer = ServiceForAssetsSerializers(
                serviceforassets_data, many=True)
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Service for assets list",
                "response": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        try:
            serializer = ServiceForAssetsSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "data": "true",
                    "status_code": "200",
                    "message": "Service for assets created successfully"
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "data": "false",
                    "status_code": "400",
                    "message": "Invalid data"
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API Start
# This API is used for update, delete and view service for assets.
# type:Web API
# form-data,raw
# add service for assets: request raw:{"assets": 3,"service": 1,"service_information": {"expiry_date": "28/09/2022","price": 20000},"status": "in-active"}


class ServiceForAssetsUpdateDeleteDetails(APIView):
    def get_object(self, pk):
        try:
            return ServiceForAssets.objects.get(id=pk)
        except ServiceForAssets.DoesNotExist as e:
            raise Http404 from e

    def get(self, request, pk, format=None):
        serviceforassets_data = self.get_object(pk)
        try:
            serializer = ServiceForAssetsSerializers(serviceforassets_data)
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Service for assets details",
                "response": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        serviceforassets_data = self.get_object(pk)
        try:
            serializer = ServiceForAssetsSerializers(
                serviceforassets_data, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "data": "true",
                    "status_code": "200",
                    "message": "Service for assets updated successfully"
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "data": "false",
                    "status_code": "400",
                    "message": "Invalid data"
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        serviceforassets_data = self.get_object(pk)
        try:
            serviceforassets_data.delete()
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Service for assets delete successfully"
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API End
