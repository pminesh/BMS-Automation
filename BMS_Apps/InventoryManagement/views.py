from rest_framework.views import APIView
from .models import *
from .serializers import InventoryCategorySerializers,ItemDetailSerializers,ManageInventoryStockSerializers
from rest_framework import status
from rest_framework.response import Response
from BMS_Apps.BMS_Main.common_func import base64ConvertArea, id_generator, removeOldFile
from django.http import Http404

# ******************************************************************************************************************
# ******************************************* Manage Inventory *****************************************************
# ******************************************************************************************************************

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API Start
# This API is used for add Inventory category and get all Inventory category list.
# type:Web API
# form-data,raw
# add Inventory category: request raw:{"category_name": "Grocery", "base64_image": "base64", "status":"active/in-active"}

class InventoryCategoryAddList(APIView):
    def get(self, request):
        try:
            category_data = InventoryCategory.objects.all()
            serializer = InventoryCategorySerializers(category_data, many=True)
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Inventory category list",
                "response": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        try:
            category_name = request.data['category_name'].replace(" ", "_")
            rand_string = str(id_generator())
            categoryBase64 = request.data['base64_image']
            Imagepath = base64ConvertArea(
                categoryBase64, f"inventoryCategory_{category_name}_{rand_string}", ".jpg",'img')
            request.data['category_image'] = Imagepath[0]
            serializer = InventoryCategorySerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "data": "true",
                    "status_code": "200",
                    "message": "Inventory category created successfully"
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
# This API is used for update, delete and view Inventory category.
# type:Web API
# form-data,raw
# update Inventory category::>request raw:{"category_name": "Grocery", "base64_image": "base64", "status":"active/in-active"}

class InventoryCategoryUpdateDeleteDetails(APIView):
    def get_object(self, pk):
        try:
            return InventoryCategory.objects.get(id=pk)
        except InventoryCategory.DoesNotExist as e:
            raise Http404 from e

    def get(self, request, pk, format=None):
            category_data = self.get_object(pk)
            try:
                serializer = InventoryCategorySerializers(category_data)
                return Response({
                    "data": "true",
                    "status_code": "200",
                    "message": "Inventory category details",
                    "response": serializer.data
                }, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        category_data = self.get_object(pk)
        try:
            category_name = request.data['category_name'].replace(" ", "_")
            rand_string = str(id_generator())
            menuBase64 = request.data['base64_image']
            Imagepath = base64ConvertArea(
                menuBase64, f"inventoryCategory_{category_name}_{rand_string}", ".jpg",'img')
            request.data['category_image'] = Imagepath[0]
            removeOldFile(category_data.category_image, "",'img')
            serializer = InventoryCategorySerializers(category_data, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "data": "true",
                    "status_code": "200",
                    "message": "Inventory category updated successfully"
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
            removeOldFile(category_data.category_image, "",'img')
            category_data.delete()
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Inventory category delete successfully"
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API Start
# This API is used for add Item detail and get all Item detail list.
# type:Web API
# form-data,raw
# add Item detail: request raw:{"category": 4, "item_name": "Maida", "item_description": "500grams (every 2nd month)", "item_image_base64": "base64", "price": "100.00", "unit": "11", "quantity": 10, "minimum_quantity": 12, "status": "active"}

class ItemDetailAddList(APIView):
    def get(self, request):
        try:
            item_data = ItemDetail.objects.all()
            serializer = ItemDetailSerializers(item_data, many=True)
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Item detail list",
                "response": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        try:
            item_name = request.data['item_name'].replace(" ", "_")
            rand_string = str(id_generator())
            itemBase64 = request.data['item_image_base64']
            Imagepath = base64ConvertArea(
                itemBase64, f"ItemDetail_{item_name}_{rand_string}", ".jpg",'img')
            request.data['item_image'] = Imagepath[0]
            serializer = ItemDetailSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "data": "true",
                    "status_code": "200",
                    "message": "Item detail created successfully"
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
# This API is used for update, delete and view Item detail.
# type:Web API
# form-data,raw
# update Item detail::>request raw:{"category": 4, "item_name": "Maida", "item_description": "500grams (every 2nd month)", "item_image_base64": "base64", "price": "100.00", "unit": "11", "quantity": 10, "minimum_quantity": 12, "status": "active"}

class ItemUpdateDeleteDetails(APIView):
    def get_object(self, pk):
        try:
            return ItemDetail.objects.get(id=pk)
        except ItemDetail.DoesNotExist as e:
            raise Http404 from e

    def get(self, request, pk, format=None):
        item_data = self.get_object(pk)
        try:
            serializer = ItemDetailSerializers(item_data)
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Item detail details",
                "response": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        item_data = self.get_object(pk)
        try:
            item_name = request.data['item_name'].replace(" ", "_")
            rand_string = str(id_generator())
            itemBase64 = request.data['item_image_base64']
            Imagepath = base64ConvertArea(
                itemBase64, f"ItemDetail_{item_name}_{rand_string}", ".jpg",'img')
            request.data['item_image'] = Imagepath[0]
            removeOldFile(item_data.item_image, "",'img')
            serializer = ItemDetailSerializers(item_data, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "data": "true",
                    "status_code": "200",
                    "message": "Item detail updated successfully"
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
        item_data = self.get_object(pk)
        try:
            removeOldFile(item_data.item_image, "",'img')
            item_data.delete()
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Item detail delete successfully"
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API Start
# This API is used for add Manage inventory stock and get all Manage inventory stock list.
# type:Web API
# form-data,raw
# add Manage inventory stock: request raw:{"item": 1, "supplier_name": "Rahul", "stock_quantity": 100, "unit": "12", "price": "1000.00", "discount": "100.00", "total": "1000.00", "tax": "50.00","grand_total": "1000.00"}

class ManageInventoryStockAddList(APIView):
    def get(self, request):
        try:
            manageInventoryStock_data = ManageInventoryStock.objects.all()
            serializer = ManageInventoryStockSerializers(manageInventoryStock_data, many=True)
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Manage inventory stock list",
                "response": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        try:
            serializer = ManageInventoryStockSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "data": "true",
                    "status_code": "200",
                    "message": "Manage inventory stock created successfully"
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
# This API is used for update, delete and view Manage inventory stock.
# type:Web API
# form-data,raw
# update Manage inventory stock::>request raw:{"item": 1, "supplier_name": "Rahul", "stock_quantity": 100, "unit": "12", "price": "1000.00", "discount": "100.00", "total": "1000.00", "tax": "50.00","grand_total": "1000.00"}

class ManageInventoryStockUpdateDeleteDetails(APIView):
    def get_object(self, pk):
        try:
            return ManageInventoryStock.objects.get(id=pk)
        except ManageInventoryStock.DoesNotExist as e:
            raise Http404 from e

    def get(self, request, pk, format=None):
        
        manageInventoryStock_data = self.get_object(pk)
        try:
            serializer = ManageInventoryStockSerializers(manageInventoryStock_data)
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Manage inventory stock details",
                "response": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        manageInventoryStock_data = self.get_object(pk)
        try:
            serializer = ManageInventoryStockSerializers(manageInventoryStock_data, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "data": "true",
                    "status_code": "200",
                    "message": "Manage inventory stock updated successfully"
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
        manageInventoryStock_data = self.get_object(pk)
        try:
            manageInventoryStock_data.delete()
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Manage inventory stock delete successfully"
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API End
