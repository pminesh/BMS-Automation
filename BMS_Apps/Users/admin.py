from django.contrib import admin
from BMS_Apps.Users.models import *

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register Start
# model UserBMS

@admin.register(UserBMS)
class UserBMSAdmin(admin.ModelAdmin):
    list_display = ('user_email', 'status', 'user_type', 'role')
    search_fields = ("last_name__startswith", )
    list_per_page = 10
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register Start
# model UserStaffDetail

@admin.register(UserStaffDetail)
class UserStaffDetailAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'user',
                    'phone_no', 'birthdate', 'address', 'department', 'locker')
    list_filter = ('birthdate',)
    list_per_page = 10
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register Start
# model UserVisitorDetail

@admin.register(UserVisitorDetail)
class UserVisitorDetailAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name',
                    'user', 'address', 'phone_no', 'locker')
    search_fields = ("address__startswith", )
    list_per_page = 10
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register Start
# model UserType

@admin.register(UserType)
class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('type_name',)
    list_per_page = 10
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register Start
# model UserRole

@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('role_name', 'permission_ids')
    search_fields = ("role_name__startswith", )
    list_per_page = 10
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register Start
# model UserWallet

@admin.register(UserWallet)
class UserWalletAdmin(admin.ModelAdmin):
    list_display = ('user', 'wallet_balance')
    list_per_page = 10
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register Start
# model UserRechargeWallet

@admin.register(UserRechargeWallet)
class UserRechargeWalletAdmin(admin.ModelAdmin):
    list_display = ('user', 'recharge_amount', 'wallet_balance')
    list_per_page = 10
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register End

# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model Start
# model UserVisitorActivity

@admin.register(UserVisitorActivity)
class UserVisitorActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'meet_person_name', 'in_time', 'out_time', 'reason_to_meet',
                    'out_remark', 'enter_by', 'rfid', 'status', 'access_from_time', 'access_to_time', 'createdAt')
    search_fields = ("status", )
    list_per_page = 10
# *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*admin model register End
