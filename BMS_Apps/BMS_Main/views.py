from rest_framework.response import Response
from .serializers import ModuleSerializers,LockerSerializers
from rest_framework import status
from rest_framework.views import APIView
from .models import BMSModule,BMSLocker
import contextlib
from django.http import Http404

# ******************************************************************************************************************
# ******************************************* Manage Modules *******************************************************
# ******************************************************************************************************************

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API Start
# This API is used for add module and get all module list.
# type:Web API
# form-data,raw
# add module: request raw:{"module_name": "Conference Booking","status":"Active"}


class ModuleAddAndList(APIView):
    def get(self, request):
        try:
            module_data = BMSModule.objects.all()
            serializer = ModuleSerializers(module_data, many=True)
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Modules list",
                "response": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        try:
            serializer = ModuleSerializers(data=request.data)
            if serializer.is_valid():
                with contextlib.suppress(Exception):
                    serializer.save()
                    return Response({
                        "data": "true",
                        "status_code": "200",
                        "message": "Module created successfully"
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
# This API is used for update,delete and view module.
# type:Web API
# form-data,raw
# update module::>request raw:{"module_name": "Conference Booking","status":"Active"}


class ModuleUpdateDeteleDetails(APIView):
    def get_object(self, pk):
        try:
            return BMSModule.objects.get(id=pk)
        except BMSModule.DoesNotExist as e:
            raise Http404 from e

    def get(self, request, pk, format=None):
        module_data = self.get_object(pk)
        try:
            serializer = ModuleSerializers(module_data)
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Module get successfully",
                "response": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        module_data = self.get_object(pk)
        try:
            serializer = ModuleSerializers(module_data, data=request.data)
            if serializer.is_valid():
                with contextlib.suppress(Exception):
                    serializer.save()
                    return Response({
                        "data": "true",
                        "status_code": "200",
                        "message": "Module updated successfully"
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
        module_data = self.get_object(pk)
        try:
            module_data.delete()
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Module deleted successfully"
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API End

# ******************************************************************************************************************
# ******************************************* Manage Locker ********************************************************
# ******************************************************************************************************************

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API Start
# This API is used for add locker and get all locker list.
# type:Web API
# form-data,raw
# add locker: request raw:{"category":"normal","subArea":1,"locker_name":"Locker Big 555"}

class LockerAddAndList(APIView):
    def get(self, request):
        try:
            locker_data = BMSLocker.objects.all()
            serializer = LockerSerializers(locker_data, many=True)
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Lockers list",
                "response": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        try:
            serializer = LockerSerializers(data=request.data)
            if serializer.is_valid():
                with contextlib.suppress(Exception):
                    serializer.save()
                    return Response({
                        "data": "true",
                        "status_code": "200",
                        "message": "locker created successfully"
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
# This API is used for update,delete and view locker.
# type:Web API
# form-data,raw
# update locker::>request raw:{"category":"big","subArea":2,"locker_name":"Locker Normal 555"}


class LockerUpdateDeteleDetails(APIView):
    def get_object(self, pk):
        try:
            return BMSLocker.objects.get(id=pk)
        except BMSLocker.DoesNotExist as e:
            raise Http404 from e

    def get(self, request, pk, format=None):
        locker_data = self.get_object(pk)
        try:
            serializer = LockerSerializers(locker_data)
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Locker get successfully",
                "response": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        locker_data = self.get_object(pk)
        try:
            serializer = LockerSerializers(locker_data, data=request.data)
            if serializer.is_valid():
                with contextlib.suppress(Exception):
                    serializer.save()
                    return Response({
                        "data": "true",
                        "status_code": "200",
                        "message": "locker updated successfully"
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
        locker_data = self.get_object(pk)
        try:
            locker_data.delete()
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Locker deleted successfully"
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API Start
# This API is used for update locker status.
# type:Web API
# form-data,raw
# update locker status: request raw:

class LockerStatusUpdate(APIView):
    def put(self,request):
        try:
            locker_id = request.data["locker_id"]
            locker_data = BMSLocker.objects.get(id=locker_id)
            locker_data.status = request.data["status"]
            locker_data.save()
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Locker status update successfully"
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API End
