from rest_framework import serializers
from .models import AudioAnnouncements

# Manage Audio Announcements Serializers
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Serializer Start
# Serializer for Audio Announcements
class AudioAnnouncementsSerializers(serializers.ModelSerializer):
    class Meta:
        model = AudioAnnouncements
        fields = ('id', 'announcement_file','description','sub_area_ids','is_recurrence','reccurence_type','date','play_time','play_after_each_duration','status')
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Serializer End
