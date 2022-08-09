from django.urls import path, include
from BMS_Apps.InventoryManagement import views

app_name = 'bms_inventory_management'

urlpatterns = [
    # Manage Inventory Category
    path('inventory-category-add-list', views.InventoryCategoryAddList.as_view(),
         name='inventory_category_add_list'),
    path('inventory-category-delete-update-details/<int:pk>/',
         views.InventoryCategoryUpdateDeleteDetails.as_view(), name='inventory_category_delete_update_details'),

    # Manage Item Detail
    path('item-add-list', views.ItemDetailAddList.as_view(),
         name='item_add_list'),
    path('item-delete-update-details/<int:pk>/',
         views.ItemUpdateDeleteDetails.as_view(), name='item_delete_update_details'),

    # Manage Inventory
    path('manageInventoryStock-add-list', views.ManageInventoryStockAddList.as_view(),
         name='manageInventoryStock_add_list'),
    path('manageInventoryStock-delete-update-details/<int:pk>/',
         views.ManageInventoryStockUpdateDeleteDetails.as_view(), name='manageInventoryStock_delete_update_details'),
]