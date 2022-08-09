from django.db import models
from django.utils.translation import ugettext as _
from django.utils import timezone

# Create your models here.

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model Start
# Floor Model
class Floor(models.Model):
    name = models.CharField(max_length=150)
    createdAt = models.DateTimeField(_('Date of created'), default=timezone.now)
    updatedAt = models.DateTimeField(_('Date of modified'),auto_now=True)
    def __str__ (self):
        return f'{self.name}'

    class Meta:
        db_table = 'bms_floor_master'
        verbose_name = _('Area Floor')
        verbose_name_plural = _('Area Floors')
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model Start
# Department Model
class Department(models.Model):
    name = models.CharField(max_length=150)
    floor = models.ForeignKey(Floor,on_delete=models.CASCADE)
    createdAt = models.DateTimeField(_('Date of created'), default=timezone.now)
    updatedAt = models.DateTimeField(_('Date of modified'),auto_now=True)
    
    def __str__ (self):
        return f'{self.name} = {self.floor}'

    class Meta:
        db_table = 'bms_department_master'
        verbose_name = _('Area Department')
        verbose_name_plural = _('Area Departments')
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model Start
# Sub Area Model
class SubArea(models.Model):
    name = models.CharField(max_length=150)
    on_image_path = models.CharField(max_length=255)
    off_image_path = models.CharField(max_length=255)
    width = models.CharField(max_length=15)
    height = models.CharField(max_length=15)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    seating_capacity = models.PositiveBigIntegerField(null=True,blank=True)
    createdAt = models.DateTimeField(_('Date of created'), default=timezone.now)
    updatedAt = models.DateTimeField(_('Date of modified'),auto_now=True)
    def __str__ (self):
        return f'{self.name} = {self.department}'

    class Meta:
        db_table = 'bms_subArea_master'
        verbose_name = _('Area SubArea')
        verbose_name_plural = _('Area SubAreas')
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model End

