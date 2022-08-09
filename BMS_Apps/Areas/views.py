from rest_framework.views import APIView
from .models import *
from .serializers import FloorSerializers, DepartmentSerializers, SubAreaSerializers
from rest_framework import status
from rest_framework.response import Response
from BMS_Apps.BMS_Main.common_func import base64ConvertArea,id_generator,removeOldFile
from django.http import Http404

# ******************************************************************************************************************
# *******************************************Manage Floor **********************************************************
# ******************************************************************************************************************

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API Start
# This API is used for add floor and get all floor list.
# type:Web API
# form-data,raw
# add floor: request raw:{"name":"Second Floor"}


class FloorAddList(APIView):    
    def get(self, request):
        try:
            floor_data = Floor.objects.all()
            serializer = FloorSerializers(floor_data, many=True)
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Floor list",
                "response": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        try:
            serializer = FloorSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "data": "true",
                    "status_code": "200",
                    "message": "Floor created successfully"
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
# This API is used for update,delete and view floor.
# type:Web API
# form-data,raw
# update floor::>request raw:{"name":"Second Floor"}


class FloorUpdateDeleteDetails(APIView):    
    def get_object(self, pk):
        try:
            return Floor.objects.get(id=pk)
        except Floor.DoesNotExist as e:
            raise Http404 from e

    def get(self, request, pk, format=None):
        floor_data = self.get_object(pk)
        try:
            serializer = FloorSerializers(floor_data)
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Floor details",
                "response": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        floor_data = self.get_object(pk)
        try:
            serializer = FloorSerializers(floor_data, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "data": "true",
                    "status_code": "200",
                    "message": "Floor updated successfully"
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
        floor_data = self.get_object(pk)
        try:
            floor_data.delete()
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Floor delete successfully"
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API End


# ******************************************************************************************************************
# ******************************************* Manage Department ****************************************************
# ******************************************************************************************************************

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API Start
# This API is used for add department and get all department list.
# type:Web API
# form-data,raw
# add department: request raw:{"name":"test area","floor":1}

class DepartmentAddList(APIView):    
    def get(self, request):
        try:
            dept_data = Department.objects.all()
            serializer = DepartmentSerializers(dept_data, many=True)
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Department list",
                "response": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        try:
            serializer = DepartmentSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "data": "true",
                    "status_code": "200",
                    "message": "Department created successfully"
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
# This API is used for update,delete and view Department.
# type:Web API
# form-data,raw
# update Department::>request raw:{"name":"test area","floor":1}


class DepartmentUpdateDeleteDetails(APIView):    
    def get_object(self, pk):
        try:
            return Department.objects.get(id=pk)
        except Department.DoesNotExist as e:
            raise Http404 from e

    def get(self, request, pk, format=None):
        dept_data = self.get_object(pk)
        try:
            serializer = DepartmentSerializers(dept_data)
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Department details",
                "response": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        dept_data = self.get_object(pk)
        try:
            serializer = DepartmentSerializers(dept_data, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "data": "true",
                    "status_code": "200",
                    "message": "Department updated successfully"
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
        dept_data = self.get_object(pk)
        try:
            dept_data.delete()
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Department delete successfully"
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API End


# ******************************************************************************************************************
# ******************************************* Manage Sub Area ******************************************************
# ******************************************************************************************************************


# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API Start
# This API is used for add Sub Area and get all Sub Area list.
# type:Web API
# form-data,raw
# add Sub Area: request raw:{"name":"new area", "on_image_base64":"base64 string", "off_image_base64":"base64 string", "department":1, "seating_capacity":100}

class SubAreaAddList(APIView):    
    def get(self, request):
        try:
            dept_data = SubArea.objects.all()
            serializer = SubAreaSerializers(dept_data, many=True)
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "SubArea list",
                "response": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        try:
            sub_area_name = request.data['name'].replace(" ", "_")
            rand_string = str(id_generator())
            onImageBase64 = request.data['on_image_base64']
            offImageBase64 = request.data['off_image_base64']
            onImagepath = base64ConvertArea(
                onImageBase64, f"on_{sub_area_name}_{rand_string}", ".jpg",'img')
            offImagepath = base64ConvertArea(
                offImageBase64, f"off_{sub_area_name}_{rand_string}", ".jpg",'img')
            request.data['on_image_path'] = onImagepath[0]
            request.data['off_image_path'] = offImagepath[0]

            request.data['width'] = str(onImagepath[1])
            request.data['height'] = str(onImagepath[2])
            serializer = SubAreaSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "data": "true",
                            "status_code": "200",
                            "message": "Sub-area created successfully"
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "data": "false",
                    "status_code": "400",
                    "message": "Invalid data"
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API Start
# This API is used for update,delete and view Sub-Area.
# type:Web API
# form-data,raw
# update Sub-Area::>{"name":"new area", "on_image_base64":"base64 string", "off_image_base64":"base64 string", "department":1, "seating_capacity":100}

class SubAreaUpdateDeleteDetails(APIView):    
    def get_object(self, pk):
        try:
            return SubArea.objects.get(id=pk)
        except SubArea.DoesNotExist as e:
            raise Http404 from e

    def get(self, request, pk, format=None):
        dept_data = self.get_object(pk)
        try:
            serializer = SubAreaSerializers(dept_data)
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "SubArea details",
                "response": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        try:
            sub_area_name = request.data['name'].replace(" ", "_")
            rand_string = str(id_generator())
            onImageBase64 = request.data['on_image_base64']
            offImageBase64 = request.data['off_image_base64']
            onImagepath = base64ConvertArea(
                onImageBase64, f"on_{sub_area_name}_{rand_string}", ".jpg",'img')
            offImagepath = base64ConvertArea(
                offImageBase64, f"off_{sub_area_name}_{rand_string}", ".jpg",'img')
            request.data['on_image_path'] = onImagepath[0]
            request.data['off_image_path'] = offImagepath[0]

            request.data['width'] = str(onImagepath[1])
            request.data['height'] = str(onImagepath[2])
            sub_area_data = self.get_object(pk)

            removeOldFile(sub_area_data.on_image_path,sub_area_data.off_image_path,'img')
            serializer = SubAreaSerializers(sub_area_data, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "data": "true",
                            "status_code": "200",
                            "message": "Sub-area updated successfully"
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
        sub_area_data = self.get_object(pk)
        try:
            removeOldFile(sub_area_data.on_image_path,sub_area_data.off_image_path,'img')
            sub_area_data.delete()
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Sub-area delete successfully"
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API End
