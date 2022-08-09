from django.urls import path, include
from BMS_Apps.Users import views

app_name = 'user_operations'

urlpatterns = [
    # Manage Users
    path('user-login',views.UserLogin.as_view(),name='user_login'),
    path('user-add-list',views.UserAddAndList.as_view(),name='user_add_list'),
    path('user-update-delete-details/<int:pk>/',views.UserUpdateDeleteDetails.as_view(),name='user_update_delete_details'),
    path('user-change-password',views.UserChangePassword.as_view(),name='user_change_password'),
    path('user-add-profile',views.UserAddProfile.as_view(),name='user_add_profile'),
    path('user-update-profile/<int:pk>/',views.UserUpdateProfile.as_view(),name='user_update_profile'),
    path('user-active-inactive',views.UserActiveInactive.as_view(),name='user_active_inactive'),
    path('user-visitor-list-update-status',views.VisitorList.as_view(),name='user_visitor_list'),

    # Manage Roles & Modules
    path('user-role-add-list',views.RoleAddAndList.as_view(),name='role_add_list'),
    path('user-role-update-delete-details/<int:pk>/',views.RoleUpdateDeteleDetails.as_view(),name='role_update_delete_details'),

]

