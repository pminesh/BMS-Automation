from rest_framework.views import APIView
from .serializers import FoodCategorySerializers, FoodSerializers, FoodMenuSerializers, FoodOrderSerializers
from .models import *
from rest_framework.response import Response
from rest_framework import status
from BMS_Apps.BMS_Main.common_func import base64ConvertArea, id_generator, removeOldFile
from django.http import Http404

# ******************************************************************************************************************
# ******************************************* Manage Category ******************************************************
# ******************************************************************************************************************

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API Start
# This API is used for add category and get all category list.
# type:Web API
# form-data,raw
# add category: {"name":"Protein"}


class FoodCategoryListAdd(APIView):
    def get(self, request):
        try:
            category_data = FoodCategory.objects.all()
            serializer = FoodCategorySerializers(category_data, many=True)
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Category list",
                "response": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        try:
            serializer = FoodCategorySerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "data": "true",
                    "status_code": "200",
                    "message": "Category created successfully"
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
# This API is used for update,delete and view category
# type:Web API
# form-data,raw
# update category:{"name":"Protein"}


class FoodCategoryUpdateDeteleDetails(APIView):
    def get_object(self, pk):
        try:
            return FoodCategory.objects.get(id=pk)
        except FoodCategory.DoesNotExist as e:
            raise Http404 from e

    def get(self, request, pk, format=None):
        category_data = self.get_object(pk)
        try:
            serializer = FoodCategorySerializers(category_data)
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Category get successfully",
                "response": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        category_data = self.get_object(pk)
        try:
            serializer = FoodCategorySerializers(
                category_data, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "data": "true",
                    "status_code": "200",
                    "message": "Category updated successfully"
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
        category_data = self.get_object(pk)
        try:
            category_data.delete()
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Category deleted successfully"
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API End

# ******************************************************************************************************************
# ******************************************* Manage Food **********************************************************
# ******************************************************************************************************************

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API Start
# This API is used for add food and get all food list.
# type:Web API
# form-data,raw
# add food: {"category":2,"food_name":"vadapaw","price":20,"description":"saras"}


class FoodListAdd(APIView):
    def get(self, request):
        try:
            food_data = Food.objects.all()
            serializer = FoodSerializers(food_data, many=True)
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Food list",
                "response": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        try:
            serializer = FoodSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "data": "true",
                    "status_code": "200",
                    "message": "Food created successfully"
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
# This API is used for update,delete and view food
# type:Web API
# form-data,raw
# update food:{"category":2,"food_name":"vadapaw","price":20,"description":"saras"}


class FoodUpdateDeteleDetails(APIView):
    def get_object(self, pk):
        try:
            return Food.objects.get(id=pk)
        except Food.DoesNotExist as e:
            raise Http404 from e

    def get(self, request, pk, format=None):
        food_data = self.get_object(pk)
        try:
            serializer = FoodSerializers(food_data)
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Food get successfully",
                "response": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        food_data = self.get_object(pk)
        try:
            serializer = FoodSerializers(
                food_data, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "data": "true",
                    "status_code": "200",
                    "message": "Food updated successfully"
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
        food_data = self.get_object(pk)
        try:
            food_data.delete()
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Food deleted successfully"
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API End

# ******************************************************************************************************************
# ******************************************* Manage Food Menu *****************************************************
# ******************************************************************************************************************

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API Start
# This API is used for add food-menu and get all food-menu list.
# type:Web API
# form-data,raw
# add food-menu: {"food_ids":[1,2,3,4],"menu_name":"last day","image_base64":"base64 string","price":100}


class FoodMenuListAdd(APIView):
    def get(self, request):
        try:
            food_menu_data = FoodMenu.objects.all()
            serializer = FoodMenuSerializers(food_menu_data, many=True)
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Food menu list",
                "response": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        try:
            menu_name = request.data['menu_name'].replace(" ", "_")
            rand_string = str(id_generator())
            menuBase64 = request.data['image_base64']
            Imagepath = base64ConvertArea(
                menuBase64, f"menu_{menu_name}_{rand_string}", ".jpg",'img')
            request.data['image'] = Imagepath[0]
            serializer = FoodMenuSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "data": "true",
                    "status_code": "200",
                    "message": "Food menu created successfully"
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
# This API is used for update,delete and view food-menu
# type:Web API
# form-data,raw
# update food:{"food_ids":[1,2,3,4],"menu_name":"last day","image_base64":"base64 string","price":100}


class FoodMenuUpdateDeteleDetails(APIView):
    def get_object(self, pk):
        try:
            return FoodMenu.objects.get(id=pk)
        except FoodMenu.DoesNotExist as e:
            raise Http404 from e

    def get(self, request, pk, format=None):
        food_menu_data = self.get_object(pk)
        try:
            serializer = FoodMenuSerializers(food_menu_data)
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Food menu get successfully",
                "response": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        try:
            menu_name = request.data['menu_name'].replace(" ", "_")
            rand_string = str(id_generator())
            menuBase64 = request.data['image_base64']
            Imagepath = base64ConvertArea(
                menuBase64, f"menu_{menu_name}_{rand_string}", ".jpg",'img')
            food_menu_data = self.get_object(pk)
            request.data['image'] = Imagepath[0]
            removeOldFile(food_menu_data.image, "",'img')
            serializer = FoodMenuSerializers(
                food_menu_data, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "data": "true",
                    "status_code": "200",
                    "message": "Food menu updated successfully"
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
        food_menu_data = self.get_object(pk)
        try:
            removeOldFile(food_menu_data.image, "",'img')
            food_menu_data.delete()
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Food menu deleted successfully"
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API End


# ******************************************************************************************************************
# ******************************************* Manage Food Order ****************************************************
# ******************************************************************************************************************

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API Start
# This API is used for add food-menu and get all food-order list.
# type:Web API
# form-data,raw
# add food-order: {"user":3,"from_sub_area":1,"menu":3,"quantity":5,"price":100,"status":"pending"}

class FoodOrderListAdd(APIView):
    def get(self, request):
        try:
            food_order_data = FoodOrderDetails.objects.all()
            serializer = FoodOrderSerializers(food_order_data, many=True)
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Food order list",
                "response": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        try:
            serializer = FoodOrderSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "data": "true",
                    "status_code": "200",
                    "message": "Food order created successfully"
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
# This API is used for update,delete and view food-order
# type:Web API
# form-data,raw
# update food:{"user":3,"from_sub_area":1,"menu":3,"quantity":5,"price":100,"status":"pending"}


class FoodOrderUpdateDeteleDetails(APIView):
    def get_object(self, pk):
        try:
            return FoodOrderDetails.objects.get(id=pk)
        except FoodOrderDetails.DoesNotExist as e:
            raise Http404 from e

    def get(self, request, pk, format=None):
        food_order_data = self.get_object(pk)
        try:
            serializer = FoodOrderSerializers(food_order_data)
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Food order get successfully",
                "response": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        food_order_data = self.get_object(pk)
        try:
            serializer = FoodOrderSerializers(
                food_order_data, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "data": "true",
                    "status_code": "200",
                    "message": "Food order updated successfully"
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
        food_order_data = self.get_object(pk)
        try:
            food_order_data.delete()
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Food order deleted successfully"
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API Start
# This API is used for update food order status
# type:Web API
# form-data,raw
# update food:{"status":"completed"}


class FoodOrderStatusUpdate(APIView):
    def put(self, request, pk, format=None):
        try:
            food_order_data = FoodOrderDetails.objects.get(id=pk)
            food_order_data.status = request.data["status"]
            food_order_data.save()
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Food order status updated successfully"
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API End
