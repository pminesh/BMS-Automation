from django.urls import path
from BMS_Apps.FoodOrdering import views

app_name = 'bms_pantry_food_manage'

urlpatterns = [
    # Manage Category
    path('category-add-list',views.FoodCategoryListAdd.as_view(),name='category_add_list'),
    path('category-update-delete-details/<int:pk>/',views.FoodCategoryUpdateDeteleDetails.as_view(),name='category_update_delete_details'),

    # Manage Food
    path('food-add-list',views.FoodListAdd.as_view(),name='food_add_list'),
    path('food-update-delete-details/<int:pk>/',views.FoodUpdateDeteleDetails.as_view(),name='food_update_delete_details'),

    # Manage Food-menu
    path('food-menu-add-list',views.FoodMenuListAdd.as_view(),name='food_menu_add_list'),
    path('food-menu-update-delete-details/<int:pk>/',views.FoodMenuUpdateDeteleDetails.as_view(),name='food_menu_update_delete_details'),

    # Manage Food-order
    path('food-order-add-list',views.FoodOrderListAdd.as_view(),name='food_order_add_list'),
    path('food-order-update-delete-details/<int:pk>/',views.FoodOrderUpdateDeteleDetails.as_view(),name='food_order_update_delete_details'),
    path('food-order-status-update/<int:pk>/',views.FoodOrderStatusUpdate.as_view(),name='food_order_status_update'),

]
