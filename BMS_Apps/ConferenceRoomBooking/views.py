from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import ConferenceRoomBookingSerializers
from .models import ConferenceRoomBooking
from django.http import Http404

# ******************************************************************************************************************
# ******************************************* Manage Conference Room Booking ***************************************
# ******************************************************************************************************************

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API Start
# This API is used for add Conference Room Booking and get all Conference Room Booking list.
# type:Web API
# form-data,raw
# add Conference Room Booking: request raw:{"module_name": {"meeting_room": 1, "host": 3,"attendees": [],   "no_of_attendees": 2,  "amenities": "",  "meeting_agenda": "",   "meeting_link": "",    "meeting_date": "2022-07-19",  "start_time": "12:37",  "end_time": "12", "booking_status": "pending",   "booking_type": "new"}


class ConferenceRoomBookingAddList(APIView):
    def get(self, request):
        try:
            crb_data = ConferenceRoomBooking.objects.all()
            serializer = ConferenceRoomBookingSerializers(
                crb_data, many=True)
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "All booking list",
                "response": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        try:
            serializer = ConferenceRoomBookingSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "data": "true",
                    "status_code": "200",
                    "message": "Conference room booking successfully"
                }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API Start
# This API is used for update,delete and view Conference Room Booking.
# type:Web API
# form-data,raw
# update Conference Room Booking: request raw:{"module_name": {"meeting_room": 1, "host": 3,"attendees": [],   "no_of_attendees": 2,  "amenities": "",  "meeting_agenda": "",   "meeting_link": "",    "meeting_date": "2022-07-19",  "start_time": "12:37",  "end_time": "12", "booking_status": "pending",   "booking_type": "new"}

class ConferenceRoomBookingUpdateDeleteDetails(APIView):
    def get_object(self, pk):
        try:
            return ConferenceRoomBooking.objects.get(id=pk)
        except ConferenceRoomBooking.DoesNotExist as e:
            raise Http404 from e

    def get(self, request, pk, format=None):
        crb_data = self.get_object(pk)
        try:
            serializer = ConferenceRoomBookingSerializers(crb_data)
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Get conference room booking details successfully",
                "response": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        try:
            pass
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        crb_data = self.get_object(pk)
        try:
            crb_data.delete()
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Conference room booking deleted successfully"
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API Start
# This API is used for update status Conference Room Booking.
# type:Web API
# form-data,raw
# Conference Room Booking status update: request raw:{"crb_id":2,"status":"confirm"}

class ConferenceRoomBookingUpdateStatus(APIView):
    def put(self,request):
        try:
            crb_id = request.data["crb_id"]
            crb_data = ConferenceRoomBooking.objects.get(id=crb_id)
            crb_data.booking_status = request.data["status"]
            crb_data.save()
            return Response({"data": "true", "status_code": "200", "message": "Status update successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API End
