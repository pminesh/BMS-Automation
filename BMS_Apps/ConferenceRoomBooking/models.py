from django.db import models
from BMS_Apps.Areas.models import SubArea
from BMS_Apps.Users.models import UserBMS
from django.utils import timezone
from django.utils.translation import ugettext as _
from model_utils import Choices

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model Start
# Conference Room Booking Model
class ConferenceRoomBooking(models.Model):
    STATUS_TYPES = Choices(
        ("pending","Pending"),
        ("confirm","Confirm"),
        ("cancelled","Cancelled"),
        ("rejected","Rejected"),
    )
    BOOKING_TYPES = Choices(
        ("new","New"),
        ("re-schedule","Re-schedule"),
    )
    meeting_room = models.ForeignKey(SubArea,on_delete=models.CASCADE)
    host = models.ForeignKey(UserBMS,on_delete=models.SET_NULL,null=True)
    attendees = models.JSONField(default=list,blank=True,null=True,help_text=('store data like [1,2,3]'))
    no_of_attendees = models.PositiveBigIntegerField()
    amenities = models.TextField()
    meeting_agenda = models.TextField()
    meeting_link = models.CharField(max_length=255)
    meeting_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    booking_status = models.CharField(max_length=15, choices=STATUS_TYPES)
    booking_type = models.CharField(max_length=15, choices=BOOKING_TYPES)
    createdAt = models.DateTimeField(_('Date of created'), default=timezone.now)
    updatedAt = models.DateTimeField(_('Date of modified'),auto_now=True)

    def __str__ (self):
        return f'{self.meeting_agenda}'

    class Meta:
        db_table = 'bms_conference_room_booking'
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model End
