from django.db import models
from django.utils.translation import ugettext as _
from django.utils import timezone
from model_utils import Choices

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model Start
# audio announcements Model
class AudioAnnouncements(models.Model):
    RECCURRENCE_TYPES = Choices(
        ("daily","Daily"),
        ("weekly","Weekly"),
        ("bi-weekly","Bi-weekly"),
        ("monthly","Monthly")
    )
    STATUS_TYPES = Choices(
        ("active","Active"),
        ("in-active","In-active"),
    )
    announcement_file = models.CharField(max_length=255)
    description = models.TextField()
    sub_area_ids = models.JSONField(default=list,null=True,blank=True)
    is_recurrence = models.BooleanField()
    reccurence_type = models.CharField(max_length=15, choices=RECCURRENCE_TYPES)
    date = models.DateField()
    play_time = models.TimeField()
    play_after_each_duration = models.IntegerField()
    status = models.CharField(max_length=15, choices=STATUS_TYPES)
    createdAt = models.DateTimeField(_('Date of created'), default=timezone.now)

    def __str__ (self):
        return f'{self.description}'

    class Meta:
        db_table = 'bms_audio_announcements'
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model End
