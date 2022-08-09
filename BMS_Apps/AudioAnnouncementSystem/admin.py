from django.contrib import admin
from BMS_Apps.AudioAnnouncementSystem.models import *

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register Start
# model Audio Announcements
@admin.register(AudioAnnouncements)
class AudioAnnouncementsAdmin(admin.ModelAdmin):
    list_display = ('description','sub_area_ids','is_recurrence','reccurence_type','date','play_time','play_after_each_duration','status')
    list_filter = ('status','reccurence_type')
    list_per_page = 10
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register End
