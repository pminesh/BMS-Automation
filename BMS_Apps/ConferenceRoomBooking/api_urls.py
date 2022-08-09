from django.urls import path, include
from BMS_Apps.ConferenceRoomBooking import views

app_name = 'bms_conference_room_booking'

urlpatterns = [
    # Manage Conference Room Booking
    path('conference_room_booking-add-list',views.ConferenceRoomBookingAddList.as_view(),name='conference_room_booking_add_list'),
    path('conference_room_booking-update-delete-details/<int:pk>/',views.ConferenceRoomBookingUpdateDeleteDetails.as_view(),name='conference_room_booking_update_delete_details'),
    path('conference_room_booking-status-update',views.ConferenceRoomBookingUpdateStatus.as_view(),name='conference_room_booking_status_update'),
]

