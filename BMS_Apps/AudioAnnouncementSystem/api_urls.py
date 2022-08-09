from django.urls import path, include
from BMS_Apps.AudioAnnouncementSystem import views

app_name = 'bms_audioAnnouncementSystem'

urlpatterns = [
    # Manage Audio announcements
     path('audio-announcements-add-list', views.AudioAnnouncementAddList.as_view(),
          name='audio_announcements_add_list'),
     path('audio-announcements-delete-update-details/<int:pk>/',
         views.AudioAnnouncementUpdateDeleteDetails.as_view(), name='audio_announcements_delete_update_details'),
     path('status-update/<int:pk>/', views.ActiveInactiveStatus.as_view(),
         name='status-update'),
]