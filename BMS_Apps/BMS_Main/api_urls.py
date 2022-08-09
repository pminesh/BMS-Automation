from django.urls import path, include
from BMS_Apps.BMS_Main import views

app_name = 'bms_operations'

urlpatterns = [
    # Manage Modules
    path('user-module-add-list',views.ModuleAddAndList.as_view(),name='module_add_list'),
    path('user-module-update-delete-details/<int:pk>/',views.ModuleUpdateDeteleDetails.as_view(),name='module_update_delete_details'),

    # Manage Locker
    path('locker-add-list',views.LockerAddAndList.as_view(),name='locker_add_list'),
    path('locker-update-delete-details/<int:pk>/',views.LockerUpdateDeteleDetails.as_view(),name='locker_update_delete_details'),
    path('locker-update-status',views.LockerStatusUpdate.as_view(),name='locker_update_status'),

]

