from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _
from BMS_Apps.Areas.models import SubArea
from BMS_Apps.Users.models import UserBMS
from model_utils import Choices
from django.utils.text import slugify

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model Start 
# BMS Food Category
class FoodCategory(models.Model):
    name = models.CharField(max_length=254)
    slug = models.CharField(max_length=254)
    createdAt = models.DateTimeField(_('Date of created'), default=timezone.now)

    def __str__ (self):
        return f'{self.name}'

    class Meta:
        db_table = 'bms_food_category'

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.name}')
        super().save(*args,**kwargs)
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model End


# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model Start
# BMS Food
class Food(models.Model):
    category = models.ForeignKey(FoodCategory,on_delete=models.CASCADE)
    food_name = models.CharField(max_length=254)
    price = models.PositiveBigIntegerField(_('food price'))
    slug = models.CharField(max_length=254)
    description = models.TextField()
    createdAt = models.DateTimeField(_('Date of created'), default=timezone.now)

    def __str__ (self):
        return f'{self.food_name}'

    class Meta:
        db_table = 'bms_food_products'
    
    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.food_name}')
        super().save(*args,**kwargs)
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model End


# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model Start
# BMS Food Menu
class FoodMenu(models.Model):
    food_ids = models.JSONField(default=list,blank=True,null=True)
    menu_name = models.CharField(max_length=254)
    image = models.CharField(max_length=255)
    price = models.PositiveBigIntegerField(_('menu price'))
    createdAt = models.DateTimeField(_('Date of created'), default=timezone.now)

    def __str__ (self):
        return f'{self.menu_name}'

    class Meta:
        db_table = 'bms_food_menu'
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model End


# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model Start
# BMS Food Order Details
class FoodOrderDetails(models.Model):
    STATUS_TYPES = Choices(
        ("pending","Pending"),
        ("in-process","In-process"),
        ("completed","Completed"),
        ("cancel","Cancel"),
    )
    user = models.ForeignKey(UserBMS,on_delete=models.CASCADE)
    from_sub_area = models.ForeignKey(SubArea,on_delete=models.SET_NULL,null=True)
    menu = models.ForeignKey(FoodMenu,on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(_('quantity'))
    price = models.PositiveBigIntegerField(_('order amount'))
    status = models.CharField(max_length=15, default='pending',choices=STATUS_TYPES)
    createdAt = models.DateTimeField(_('Date of created'), default=timezone.now)
    updatedAt = models.DateTimeField(_('Date of modified'),auto_now=True)

    def __str__ (self):
        return f'{self.user} = {self.menu} = {self.status}'

    class Meta:
        db_table = 'bms_food_order_details'
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model End


# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model Start
# BMS Food Order Payment
class FoodOrderPayment(models.Model):
    STATUS_TYPES = Choices(
        ("paid","Paid"),
        ("unpaid","Unpaid"),
    )
    order = models.ForeignKey(FoodOrderDetails,on_delete=models.CASCADE)
    order_amount = models.PositiveBigIntegerField(_('payment net amount'))
    wallet = models.PositiveBigIntegerField()#change: foreignkey with wallet table
    status = models.CharField(max_length=15, choices=STATUS_TYPES)
    createdAt = models.DateTimeField(_('Date of created'), default=timezone.now)

    def __str__ (self):
        return f'{self.order}'

    class Meta:
        db_table = 'bms_food_payment_details'
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model End
