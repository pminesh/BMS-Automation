from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _
from model_utils import Choices

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model Start
# Inventory Category
class InventoryCategory(models.Model):
    STATUS_TYPES = Choices(
        ("active","Active"),
        ("in-active","In-active"),
    )
    category_name = models.CharField(max_length=255)
    category_image = models.CharField(max_length=255)
    status =  models.CharField(max_length=15, choices=STATUS_TYPES)
    createdAt = models.DateTimeField(_('Date of created'), default=timezone.now)

    def __str__ (self):
        return f'{self.category_name}'

    class Meta:
        db_table = 'bms_inventory_category'

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model Start
# Item Detail
class ItemDetail(models.Model):
    STATUS_TYPES = Choices(
        ("active","Active"),
        ("in-active","In-active"),
    )
    category = models.ForeignKey(InventoryCategory,on_delete=models.CASCADE)
    item_name =  models.CharField(max_length=255)
    item_description = models.TextField()
    item_image = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    unit =  models.CharField(max_length=255)
    quantity = models.IntegerField()
    minimum_quantity = models.IntegerField()
    status =  models.CharField(max_length=15, choices=STATUS_TYPES)
    createdAt = models.DateTimeField(_('Date of created'), default=timezone.now)

    def __str__ (self):
        return f'{self.item_name}'

    class Meta:
        db_table = 'bms_item_details'
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model Start
# Manage Inventory Stock
class ManageInventoryStock(models.Model):
    item = models.ForeignKey(ItemDetail,on_delete=models.CASCADE)
    supplier_name = models.CharField(max_length=255)
    stock_quantity = models.IntegerField()
    unit = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount = models.DecimalField(max_digits=6, decimal_places=2)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    tax = models.DecimalField(max_digits=6, decimal_places=2)
    grand_total = models.DecimalField(max_digits=6, decimal_places=2)
    createdAt = models.DateTimeField(_('Date of created'), default=timezone.now)

    def __str__ (self):
        return f'{self.supplier_name}'

    class Meta:
        db_table = 'bms_manage_inventory_stock'
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model End


