from django.urls import path, include
from BMS_Apps.Areas import views

app_name = 'bms_area'

urlpatterns = [
    # Manage Area
    path('floor-add-list',views.FloorAddList.as_view(),name='floor_add_list'),
    path('floor-delete-update-details/<int:pk>/',views.FloorUpdateDeleteDetails.as_view(),name='floor_delete_update_details'),

    # Manage Department
    path('dept-add-list',views.DepartmentAddList.as_view(),name='dept_add_list'),
    path('dept-delete-update-details/<int:pk>/',views.DepartmentUpdateDeleteDetails.as_view(),name='dept_delete_update_details'),

    # Manage Sub Area
    path('subArea-add-list',views.SubAreaAddList.as_view(),name='subArea_add_list'),
    path('subArea-delete-update-details/<int:pk>/',views.SubAreaUpdateDeleteDetails.as_view(),name='subArea_delete_update_details'),

]

