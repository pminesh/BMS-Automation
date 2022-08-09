from django.db import models
from django.utils.translation import ugettext as _
from django.utils import timezone
from model_utils import Choices
from BMS_Apps.Areas.models import Department,SubArea
from BMS_Apps.BMS_Main.models import BMSLocker
# from django.db.models import signals

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model Start
# User role model
class UserRole(models.Model):
    role_name = models.CharField(max_length=100)
    permission_ids = models.JSONField(default=list,blank=True,null=True)
    createdAt = models.DateTimeField(_('Date of created'), default=timezone.now)
    updatedAt = models.DateTimeField(_('Date of modified'),auto_now=True)

    def __str__ (self):
        return f'{self.role_name}'

    class Meta:
        db_table = 'bms_roles'
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model Start
# User type model
class UserType(models.Model):
    type_name = models.CharField(max_length=50)
    createdAt = models.DateTimeField(_('Date of created'), default=timezone.now)

    def __str__ (self):
        return f'{self.type_name}'

    class Meta:
        db_table = 'bms_user_types'
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model Start
# User model
class UserBMS(models.Model):
    user_type = models.ForeignKey(UserType,on_delete=models.CASCADE)
    role = models.ForeignKey(UserRole,on_delete=models.CASCADE,blank=True,null=True)    
    user_email = models.EmailField(max_length=254,unique=True,error_messages={'unique': _('A user with that email address  already exists.')})
    password = models.CharField(max_length=254)
    status = models.BooleanField(default=False)
    createdAt = models.DateTimeField(_('Date of joined'), default=timezone.now)
    updatedAt = models.DateTimeField(_('Date of modified'),auto_now=True)

    def __str__ (self):
        return f'{self.user_email}-{self.user_type}'

    class Meta:
        db_table = 'bms_users'
        verbose_name = _('User BMS')
        verbose_name_plural = _('Users BMS')
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model Start
# User staff details model
class UserStaffDetail(models.Model):
    user = models.ForeignKey(UserBMS,on_delete=models.CASCADE)
    locker = models.ForeignKey(BMSLocker,on_delete=models.SET_NULL,null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to ='images',blank=True)
    phone_no = models.CharField(max_length=16)
    birthdate = models.DateField()
    address = models.TextField()
    department = models.ForeignKey(Department,on_delete=models.SET_NULL,null=True)
    createdAt = models.DateTimeField(_('Date of created'), default=timezone.now)
    updatedAt = models.DateTimeField(_('Date of modified'),auto_now=True)

    def __str__ (self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        db_table = 'bms_staff_details'
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model Start
# User visitor model
class UserVisitorDetail(models.Model):
    user = models.ForeignKey(UserBMS,on_delete=models.CASCADE)
    locker = models.ForeignKey(BMSLocker,on_delete=models.SET_NULL,null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField()
    phone_no = models.CharField(max_length=16)
    createdAt = models.DateTimeField(_('Date of created'), default=timezone.now)
    updatedAt = models.DateTimeField(_('Date of modified'),auto_now=True)

    def __str__ (self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        db_table = 'bms_visitor_details'
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model Start
# User wallet model
class UserWallet(models.Model):
    user = models.ForeignKey(UserBMS,on_delete=models.CASCADE)
    wallet_balance = models.DecimalField(max_digits=9,decimal_places=2)
    createdAt = models.DateTimeField(_('Date of created'), default=timezone.now)
    
    def __str__ (self):
        return f'{self.user} - {self.wallet_balance}'

    class Meta:
        db_table = 'bms_user_wallet'
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model Start
# User recharge wallet model
class UserRechargeWallet(models.Model):
    user = models.ForeignKey(UserBMS,on_delete=models.CASCADE)
    recharge_amount = models.DecimalField(max_digits=9,decimal_places=2)
    wallet_balance = models.DecimalField(max_digits=9,decimal_places=2)
    createdAt = models.DateTimeField(_('Date of created'), default=timezone.now)
    
    def __str__ (self):
        return f'{self.recharge_amount} - {self.wallet_balance}'

    class Meta:
        db_table = 'bms_recharge_wallet'
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model Start
# User visitor activity
class UserVisitorActivity(models.Model):
    STATUS_TYPES = Choices(
        ("in","In"),
        ("out","Out"),
    )
    user = models.ForeignKey(UserBMS,on_delete=models.CASCADE,related_name='user')
    department = models.ForeignKey(Department,on_delete=models.SET_NULL,null=True)
    meet_person_name = models.CharField(max_length=254)
    in_time = models.TimeField()
    out_time = models.TimeField()
    reason_to_meet = models.TextField()
    out_remark = models.CharField(max_length=254)
    enter_by = models.ForeignKey(UserBMS,on_delete=models.SET_NULL,null=True,related_name='enter_by')
    rfid = models.CharField(max_length=254)
    status = models.CharField(max_length=15, choices=STATUS_TYPES)
    access_from_time = models.TimeField()
    access_to_time = models.TimeField()
    createdAt = models.DateTimeField(_('Date of created'), default=timezone.now)
    updatedAt = models.DateTimeField(_('Date of modified'),auto_now=True)

    def __str__ (self):
        return f'{self.user} - {self.status}'

    class Meta:
        db_table = 'bms_visitor_activity '
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model End

# ===================================================================================================#
# ==                                         Signals                                               ==#
# ===================================================================================================#

# def create_customer(sender, instance, created, **kwargs):
#     print(sender)
#     print(instance.id)
#     print(created)
#     print(kwargs)

# signals.post_save.connect(receiver=create_customer, sender=UserBMS)