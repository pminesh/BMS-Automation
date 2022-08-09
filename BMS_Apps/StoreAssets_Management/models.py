from model_utils import Choices
from django.db import models
from django.utils.translation import ugettext as _
from django.utils import timezone
from BMS_Apps.Areas.models import SubArea
from BMS_Apps.Users.models import UserBMS
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model Start
# Assets Type
class AssetsType(models.Model):
    type_name = models.CharField(max_length=254)
    description = models.TextField()
    createdAt = models.DateTimeField(_('Date of created'), default=timezone.now)

    def __str__ (self):
        return f'{self.type_name}'

    class Meta:
        db_table = 'bms_assets_type'
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model Start
# Assets Details
class AssetsDetails(models.Model):
    assets_type = models.ForeignKey(AssetsType,on_delete=models.CASCADE)
    name = models.CharField(max_length=254)
    purchase_description = models.TextField()
    purchase_date = models.DateField()
    expiry_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock_quantity = models.PositiveSmallIntegerField(_('number of quantity'),default=1)
    createdAt = models.DateTimeField(_('Date of created'), default=timezone.now)

    def __str__ (self):
        return f'{self.name}'

    class Meta:
        db_table = 'bms_assets_details'
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model Start
# Manage Assets
class ManageAssets(models.Model):
    assets = models.ForeignKey(AssetsDetails,on_delete=models.CASCADE)
    sub_area = models.ForeignKey(SubArea,on_delete=models.SET_NULL,null=True)
    user = models.ForeignKey(UserBMS,on_delete=models.SET_NULL,null=True)
    stock_quantity = models.PositiveSmallIntegerField(_('number of quantity'),default=1)
    alert_message = models.CharField(max_length=254)
    createdAt = models.DateTimeField(_('Date of created'), default=timezone.now)

    def __str__ (self):
        return f'{self.assets} = {self.stock_quantity}'

    class Meta:
        db_table = 'bms_manage_assets'
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model Start
# Assets Service
class AssetsService (models.Model):
    service_name = models.CharField(max_length=254)
    provider_details = models.JSONField(default=dict,blank=True,null=True)
    createdAt = models.DateTimeField(_('Date of created'), default=timezone.now)

    def __str__ (self):
        return f'{self.service_name}'

    class Meta:
        db_table = 'bms_assets_service'
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model Start
# Service For Assets
class ServiceForAssets(models.Model):
    STATUS_TYPES = Choices(
        ("active","Active"),
        ("in-active","In-active"),
    )
    assets = models.ForeignKey(AssetsDetails,on_delete=models.CASCADE)
    service = models.ForeignKey(AssetsService,on_delete=models.CASCADE)
    service_information = models.JSONField(default=dict,blank=True,null=True)
    status = models.CharField(max_length=15, choices=STATUS_TYPES)

    def __str__ (self):
        return f'{self.assets} = {self.service}'

    class Meta:
        db_table = 'bms_service_for_assets'
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model End