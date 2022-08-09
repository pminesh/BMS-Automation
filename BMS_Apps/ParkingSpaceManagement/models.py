# from django.db import models
# from django.utils import timezone
# from django.utils.translation import ugettext as _
# from model_utils import Choices

# # *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model Start
# # Vehicles Type
# class VehiclesType(models.Model):
#     # vehicle_type = 
#     # vehicle_image
#     # status
#     # createdAt
#     def __str__ (self):
#         return f'{self.supplier_name}'

#     class Meta:
#         db_table = 'bms_vehicles_type'
# # *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model End

# # *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model Start
# # Parking Zone
# class ParkingZone(models.Model):
#     # floor
#     # zone_name
#     # parking_slots
#     def __str__ (self):
#         return f'{self.supplier_name}'

#     class Meta:
#         db_table = 'bms_parking_zone'
# # *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model End

# # *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model Start
# # Parking Booking
# class ParkingBooking(models.Model):
#     # user
#     # owner_name
#     # vehicle_no
#     # vehicle_type
#     # pricing
#     # parking_slot
#     # check_in
#     # check_out
#     # duration
#     # payable_amount
#     def __str__ (self):
#         return f'{self.supplier_name}'

#     class Meta:
#         db_table = 'bms_parking_booking'
# # *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model End

# # *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model Start
# # Available Parking Slot
# class AvailableParkingSlot(models.Model):
#     # zone
#     # slot_no
#     # is_occupied
#     def __str__ (self):
#         return f'{self.supplier_name}'

#     class Meta:
#         db_table = 'bms_available_parking_slots'
# # *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model End

# # *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model Start
# # Parking Pricing
# class ParkingPricing(models.Model):
#     # vehicle_type
#     # floor
#     # zone
#     # duration_type
#     # standard_price
#     # standard_hours
#     # additional_price
#     # additional_duration
#     def __str__ (self):
#         return f'{self.supplier_name}'

#     class Meta:
#         db_table = 'bms_parking_pricing_master'
# # *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model End

# # *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model Start
# # Parking Payment
# class ParkingPayment(models.Model):
#     # parking_booking
#     # total_amount
#     # wallet
#     def __str__ (self):
#         return f'{self.supplier_name}'

#     class Meta:
#         db_table = 'bms_parking_payment'
# # *--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*Model End
