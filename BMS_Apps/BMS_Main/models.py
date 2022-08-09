from django.db import models
from django.utils.translation import ugettext as _
from django.utils import timezone
from model_utils import Choices
from django.utils.text import slugify

from BMS_Apps.Areas.models import SubArea

# from BMS_Apps.Users.models import UserBMS

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model Start 
# BMS module
class BMSModule(models.Model):
    STATUS_TYPES = Choices(
        ("Active","Active"),
        ("In-active","In-active"),
    )
    module_name = models.CharField(max_length=254)
    module_slug = models.CharField(max_length=254)
    status = models.CharField(max_length=15, choices=STATUS_TYPES)
    createdAt = models.DateTimeField(_('Date of created'), default=timezone.now)
    updatedAt = models.DateTimeField(_('Date of modified'),auto_now=True)

    def __str__ (self):
        return f'{self.module_name}'

    class Meta:
        db_table = 'bms_module_master'
    
    def save(self, *args, **kwargs):
        self.module_slug = slugify(f'{self.module_name}')
        super().save(*args,**kwargs)
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model End


# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model Start
# BMS permissions
class BMSPermissions(models.Model):
    module =models.ForeignKey(BMSModule,on_delete=models.CASCADE)
    permission_name = models.CharField(max_length=254)
    permission_slug = models.CharField(max_length=254)
    createdAt = models.DateTimeField(_('Date of created'), default=timezone.now)
    updatedAt = models.DateTimeField(_('Date of modified'),auto_now=True)
    def __str__ (self):
        return f'{self.module} = {self.permission_name}'

    class Meta:
        db_table = 'bms_permissions_master'
    
    def save(self, *args, **kwargs):
        self.permission_slug = slugify(f'{self.permission_name}')
        super().save(*args,**kwargs)
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model End


# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model Start
# BMS access control rfid master Model
class BmsAccessControlRFID(models.Model):
    CARD_TYPES = Choices(
        ("dynamic","Dynamic"),
        ("static","Static"),
        ("no-assign","No-assign"),
    )
    STATUS_TYPES = Choices(
        ("active","Active"),
        ("in-active","In-active"),
    )
    user = models.ForeignKey("Users.UserBMS",related_name='user_access',on_delete=models.CASCADE,null=True,blank=True)
    rfid_number = models.PositiveBigIntegerField()
    card_type = models.CharField(max_length=15, choices=CARD_TYPES)
    access_area = models.JSONField(default=list,null=True,blank=True)
    status = models.CharField(max_length=15, choices=STATUS_TYPES)
    access_start_time = models.TimeField(null=True,blank=True)
    access_end_time = models.TimeField(null=True,blank=True)
    def __str__ (self):
        return f'{self.rfid_number} = {self.user_id}'

    class Meta:
        db_table = 'bms_access_control_rfid_master'
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model End


# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model Start
# BMS history Model
class BMSHistory(models.Model):
    HISTORY_TYPES = Choices(
        ("new_user","New user"),
        ("visitor","Visitor"),
        ("access","Access"),
        ("conference","Conference"),
    )
    user = models.ForeignKey("Users.UserBMS",related_name='history',on_delete=models.CASCADE)
    history_type = models.CharField(max_length=15, choices=HISTORY_TYPES)
    description = models.JSONField(default=dict,null=True,blank=True)
    createdAt = models.DateTimeField(_('Date of created'), default=timezone.now)
    def __str__ (self):
        return f'{self.user}'

    class Meta:
        db_table = 'bms_history'
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model Start
# BMS settings model
class BMSSettings(models.Model):
    module = models.ForeignKey(BMSModule,on_delete=models.CASCADE)
    setting_data = models.JSONField(default=dict,null=True,blank=True)
    createdAt = models.DateTimeField(_('Date of created'), default=timezone.now)

    def __str__ (self):
        return f'{self.module_id}'

    class Meta:
        db_table = 'bms_settings'
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model Start
# BMS locker model
class BMSLocker(models.Model):
    LOCKER_TYPES = Choices(
        ("normal","Normal"),
        ("big","Big"),
     )
    LOCKER_STATUS = Choices(
        ("active","Active"),
        ("in-active","In-active"),
     )
    category = models.CharField(max_length=15, choices=LOCKER_TYPES)
    subArea = models.ForeignKey(SubArea,on_delete=models.CASCADE)
    locker_name = models.CharField(max_length=254)
    createdAt = models.DateTimeField(_('Date of created'), default=timezone.now)
    status = models.CharField(max_length=15, default="in-active",choices=LOCKER_STATUS)
    
    def __str__ (self):
        return f'{self.locker_name}'

    class Meta:
        db_table = 'bms_locker'
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model End