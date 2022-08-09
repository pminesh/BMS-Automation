from rest_framework.response import Response
from .serializers import AudioAnnouncementsSerializers
from rest_framework import status
from rest_framework.views import APIView
from .models import AudioAnnouncements
from django.http import Http404
from BMS_Apps.BMS_Main.common_func import base64ConvertArea,id_generator,removeOldFile

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API Start
# This API is used for add audio announcement and get all audio announcement list.
# type:Web API
# form-data,raw
# add audio announcement::> {"announcement_file_base64":"base64","description": "every day play","sub_area_ids": [1,3],"is_recurrence": True,"reccurence_type": "daily","date": "2022-07-27",    "play_time": "06:50", "play_after_each_duration": 5,"status": "in-active"}

class AudioAnnouncementAddList(APIView):
    def get(self, request):
        try:
            dept_data = AudioAnnouncements.objects.all()
            serializer = AudioAnnouncementsSerializers(dept_data, many=True)
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Audio announcements list",
                "response": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        try:
            announcement_file_base64 = request.data['announcement_file_base64']
            rand_string = str(id_generator())
            reccurence_type = request.data['reccurence_type'].replace(" ", "_")
            announcement_file = base64ConvertArea(
                announcement_file_base64, f"audio_{reccurence_type}_{rand_string}", ".mp3",'mp3')
            request.data['announcement_file'] = announcement_file
            serializer = AudioAnnouncementsSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "data": "true",
                    "status_code": "200",
                    "message": "Audio announcements created successfully"
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "data": "false",
                    "status_code": "400",
                    "message": "Invalid data"
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API Start
# This API is used for update,delete and view audio announcement.
# type:Web API
# form-data,raw
# update audio announcement::>request raw:{"announcement_file_base64":"base64","description": "every day play","sub_area_ids": [1,3],"is_recurrence": True,"reccurence_type": "daily","date": "2022-07-27",    "play_time": "06:50", "play_after_each_duration": 5,"status": "in-active"}

class AudioAnnouncementUpdateDeleteDetails(APIView):    
    def get_object(self, pk):
        try:
            return AudioAnnouncements.objects.get(id=pk)
        except AudioAnnouncements.DoesNotExist as e:
            raise Http404 from e

    def get(self, request, pk, format=None):
        audio_data = self.get_object(pk)
        try:
            serializer = AudioAnnouncementsSerializers(audio_data)
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Audio announcements details",
                "response": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        audio_data = self.get_object(pk)
        try:
            announcement_file_base64 = request.data['announcement_file_base64']
            rand_string = str(id_generator())
            reccurence_type = request.data['reccurence_type'].replace(" ", "_")
            announcement_file = base64ConvertArea(
                announcement_file_base64, f"audio_{reccurence_type}_{rand_string}", ".mp3",'mp3')
            request.data['announcement_file'] = announcement_file
            serializer = AudioAnnouncementsSerializers(audio_data, data=request.data)
            removeOldFile(audio_data.announcement_file,"",'mp3')
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "data": "true",
                    "status_code": "200",
                    "message": "Audio announcements updated successfully"
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "data": "false",
                    "status_code": "400",
                    "message": "Invalid data"
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        audio_data = self.get_object(pk)
        try:
            removeOldFile(audio_data.announcement_file,"",'mp3')
            audio_data.delete()
            return Response({
                "data": "true",
                "status_code": "200",
                "message": "Audio announcements delete successfully"
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API Start
# This API is used for update,delete and view audio announcement.
# type:Web API
# form-data,raw

class ActiveInactiveStatus(APIView):
    def get_object(self, pk):
        try:
            return AudioAnnouncements.objects.get(id=pk)
        except AudioAnnouncements.DoesNotExist as e:
            raise Http404 from e

    def put(self, request, pk, format=None):
        audio_data = self.get_object(pk)
        try:
            audio_data.status = request.data['status']
            audio_data.save()
            return Response({
                    "data": "true",
                    "status_code": "200",
                    "message": "Status updated successfully"
                }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": "false", "status_code": "404", "message": e}, status=status.HTTP_404_NOT_FOUND)
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*API End
