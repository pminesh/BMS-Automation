from django.shortcuts import render
from .models import Device

# Create your views here.

# common function for get all device details
def getAllDeviceData():
    device = {
        "devices": []
    }
    all_devices = Device.objects.all()
    for md in all_devices:
        main_dict = {
            "record_id":md.id,
            "device_name":md.device_name,
            "device_type":md.app_type.device_type.name,
            "app_type":md.app_type.name,
            "is_used":md.is_used,
            "device_status":md.status
        }
        device_object = main_dict | md.device_information[0]
        device["devices"].append(device_object)
    return device