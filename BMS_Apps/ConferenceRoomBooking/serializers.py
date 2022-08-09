from rest_framework import serializers
from .models import *
from BMS_Apps.Users.models import UserBMS
# Manage Conference Room Booking Serializers
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Serializer Start
# Serializer for Conference Room Booking


class ConferenceRoomBookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = ConferenceRoomBooking
        fields = ('id','meeting_room', 'host', 'attendees', 'no_of_attendees', 'amenities', 'meeting_agenda', 'meeting_link', 'meeting_date', 'start_time',
                  'end_time', 'booking_status', 'booking_type')
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Serializer End
