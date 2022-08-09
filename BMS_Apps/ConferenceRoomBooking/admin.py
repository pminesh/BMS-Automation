from django.contrib import admin
from BMS_Apps.ConferenceRoomBooking.models import ConferenceRoomBooking


# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register Start
# model Conference Room Booking
@admin.register(ConferenceRoomBooking)
class ConferenceRoomBookingAdmin(admin.ModelAdmin):
    list_display = ('meeting_room','host','no_of_attendees','amenities','meeting_link','meeting_date','start_time','end_time','booking_status','booking_type')
    list_filter = ('booking_status','booking_type')
    list_per_page = 10
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register End
