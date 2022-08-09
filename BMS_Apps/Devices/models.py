from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _
from model_utils import Choices
from BMS_Apps.Areas.models import SubArea
from BMS_Apps.Users.models import UserBMS

# Create your models here.

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model Start
# Device Type
class DeviceType(models.Model):
    name = models.CharField(max_length=254)
    createdAt = models.DateTimeField(_('Date of created'), default=timezone.now)

    def __str__ (self):
        return f'{self.name}'

    class Meta:
        db_table = 'bms_device_type'
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model Start
# App Type
class AppType(models.Model):
    name = models.CharField(max_length=254)
    device_type = models.ForeignKey(DeviceType,on_delete=models.CASCADE)
    createdAt = models.DateTimeField(_('Date of created'), default=timezone.now)

    def __str__ (self):
        return f'{self.name}-{self.device_type}'

    class Meta:
        db_table = 'bms_app_type'
        verbose_name = _('Device App Type')
        verbose_name_plural = _('Devices App Type')
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model Start
# Device
class Device(models.Model):#[ Automations ]
    IS_USED_TYPES = Choices(
        ("yes","Yes"),
        ("no","No"),
    )
    device_name = models.CharField(max_length=254)
    app_type = models.ForeignKey(AppType,on_delete=models.CASCADE)
    is_used =  models.CharField(max_length=15, choices=IS_USED_TYPES)
    device_information = models.JSONField(default=list,null=True,blank=True)
    status = models.CharField(max_length=10)
    subArea = models.ForeignKey(SubArea,on_delete=models.CASCADE)
    createdAt = models.DateTimeField(_('Date of created'), default=timezone.now)
    updatedAt = models.DateTimeField(_('Date of modified'),auto_now=True)
    
    def __str__ (self):
        return f'{self.device_name}'

    class Meta:
        db_table = 'bms_devices'
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model Start
# Device HasUser
class DeviceHasUser(models.Model):
    device =  models.ForeignKey(Device,on_delete=models.CASCADE)
    user =  models.ForeignKey(UserBMS,on_delete=models.CASCADE)
    createdAt = models.DateTimeField(_('Date of created'), default=timezone.now)

    def __str__ (self):
        return f'{self.device}-{self.user}'

    class Meta:
        db_table = 'bms_devices_has_users'
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model Start
# Device Status
class DeviceStatus(models.Model):
    user = models.ForeignKey(UserBMS,on_delete=models.CASCADE)
    device =  models.ForeignKey(Device,on_delete=models.CASCADE)
    device_status =  models.CharField(max_length=10)
    createdAt = models.DateTimeField(_('Date of created'), default=timezone.now)
    def __str__ (self):
        return f'{self.user}-{self.device}-{self.device_status}'

    class Meta:
        db_table = 'bms_device_status'
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model End

