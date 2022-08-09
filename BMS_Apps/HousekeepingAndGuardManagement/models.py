from django.db import models
from model_utils import Choices
from django.utils import timezone
from BMS_Apps.Users.models import UserBMS
from BMS_Apps.Areas.models import SubArea
from django.utils.translation import ugettext as _

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model Start
# User Housekeeping Guard Service
class HousekeepingGuardService(models.Model):
    STATUS_TYPES = Choices(
        ("active","Active"),
        ("in-active","In-active"),
    )
    service_name = models.CharField(max_length=254)
    status = models.CharField(max_length=15, choices=STATUS_TYPES)
    createdAt = models.DateTimeField(_('Date of created'), default=timezone.now)

    def __str__ (self):
        return f'{self.service_name}'

    class Meta:
        db_table = 'bms_housekeeping_guard_service_master'
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model Start
# User Housekeeping Guard Details
class HousekeepingGuardDetails(models.Model):
    STATUS_TYPES = Choices(
        ("pending","Pending"),
        ("completed","Completed"),
    )
    sub_area = models.ForeignKey(SubArea,on_delete=models.CASCADE)
    service = models.ForeignKey(HousekeepingGuardService,on_delete=models.CASCADE)
    user = models.ForeignKey(UserBMS,on_delete=models.CASCADE)
    start_time = models.TextField()
    end_time = models.TimeField()
    status = models.CharField(max_length=15, choices=STATUS_TYPES)
    createdAt = models.DateTimeField(_('Date of created'), default=timezone.now)

    def __str__ (self):
        return f'{self.service_name}'

    class Meta:
        db_table = 'bms_housekeeping_guard_details'
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model End
