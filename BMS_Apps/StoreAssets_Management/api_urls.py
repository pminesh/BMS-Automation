from django.urls import path, include
from BMS_Apps.StoreAssets_Management import views

app_name = 'bms_store_assets_management'

urlpatterns = [
    # Manage assets type
    path('assets-type-add-list', views.AssetsTypeAddList.as_view(),
         name='assets_type_add_list'),
    path('assets-type-delete-update-details/<int:pk>/',
         views.AssetsTypeUpdateDeleteDetails.as_view(), name='assets_type_delete_update_details'),

    # Manage assets details
    path('assets-details-add-list', views.AssetsDetailsAddList.as_view(),
         name='assets_details_add_list'),
    path('assets-details-delete-update/<int:pk>/',
         views.AssetsDetailsUpdateDelete.as_view(), name='assets_details_delete_update'),

    # Manage assets
    path('assets-manage-add-list', views.AssetsManageAddList.as_view(),
         name='assets_details_add_list'),
    path('assets-manage-delete-update-details/<int:pk>/',
         views.AssetsManageUpdateDeleteDetails.as_view(), name='assets_manage_delete_update_details'),

    # Manage assets service
    path('assets-service-add-list', views.AssetsServiceAddList.as_view(),
         name='assets_service_add_list'),
    path('assets-service-delete-update-details/<int:pk>/',
         views.AssetsServiceUpdateDeleteDetails.as_view(), name='assets_service_delete_update_details'),

    # Manage service for assets
    path('serviceforassets-add-list', views.ServiceForAssetsAddList.as_view(),
         name='serviceforassets_add_list'),
    path('serviceforassets-delete-update-details/<int:pk>/',
         views.ServiceForAssetsUpdateDeleteDetails.as_view(), name='serviceforassets_delete_update_details'),

]
