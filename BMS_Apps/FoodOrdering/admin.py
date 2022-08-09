from django.contrib import admin
from BMS_Apps.FoodOrdering.models import *

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register Start
# model Food Category
@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    # list_filter = ('date','meeting_room')
    readonly_fields = ('slug',)
    list_per_page = 10
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register Start
# model Food
@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('category','food_name','price','slug','description')
    list_filter = ('category',)
    readonly_fields = ('slug',)
    list_per_page = 10
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register Start
# model Food Menu
@admin.register(FoodMenu)
class FoodMenuAdmin(admin.ModelAdmin):
    list_display = ('food_ids','menu_name','image','price')
    # list_filter = ('category',)
    list_per_page = 10
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register Start
# model Food Order Details
@admin.register(FoodOrderDetails)
class FoodOrderDetailsAdmin(admin.ModelAdmin):
    list_display = ('user','from_sub_area','menu','quantity','price','status')
    list_filter = ('status',)
    list_per_page = 10
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register Start
# model Food Order Payment
@admin.register(FoodOrderPayment)
class FoodOrderPaymentAdmin(admin.ModelAdmin):
    list_display = ('order','order_amount','wallet','status')
    list_filter = ('wallet','status')
    list_per_page = 10
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register Start
