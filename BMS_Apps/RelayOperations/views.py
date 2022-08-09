from BMS_Apps.RelayOperations.relay_code import RelayKeys
from BMS_Apps.BMS_Main.config import Config
from BMS_Apps.Devices.views import getAllDeviceData
from BMS_Apps.Devices.models import Device

from socket import *
from struct import pack
from BMS_PRO import urls
import logging
import binascii
import six
import time

rc = RelayKeys()
param = Config()

logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S')

# Create your views here.

# *************************************************************************************************Start function
def relay_opr(param):
    logging.info(">>->>->> Sending Operation on " + str(param['device_id']) + " on channel id " + str(param['channel_id']) + " Operation " + str(param['device_status'])+" >>->>->>")
    y = hex(int(param['channel_id']))

    if int(param['channel_id']) < 16:
        m = y.replace('0x', '0')
    else:
        m = y.replace('0x', '')
    channel_id = binascii.a2b_hex(m.encode('utf-8'))

    deviceid_hex = hex(int(param['device_id']))

    if int(param['device_id']) < 16:
        deviceid_replaced = deviceid_hex.replace('0x', '0')
    else:
        deviceid_replaced = deviceid_hex.replace('0x', '')

    device_id = binascii.a2b_hex(deviceid_replaced.encode('utf-8'))

    operation = param['device_status']

    if operation == 'true':
        b = r"\x" + '64'
        o = b.replace('\\x', '')
        opr = binascii.a2b_hex(o.encode('utf-8'))

    elif operation == 'false':
        b = r"\x" + '00'
        o = b.replace('\\x', '')
        opr = binascii.a2b_hex(o.encode('utf-8'))

    else:
        opr = pack('b', int(operation))

    get = crc16_ccitt(rc.OPERATION + device_id + channel_id + opr + rc.TRAIL, crc=0)
    crc_int = hex(get)[2:]

    if len(crc_int) == 3:
        crc_int = f'0{crc_int}'
    if len(crc_int) == 2:
        crc_int = f'00{crc_int}'

    sm = r"\x" + r"\x".join(crc_int[n : n+2] for n in range(0, len(crc_int), 2))

    a = sm.replace('\\x', '')
    a.encode('utf8')

    x = binascii.a2b_hex(a.encode('utf8'))

    udp_pack_new = rc.HEADER + rc.OPERATION + device_id + channel_id + opr + rc.TRAIL + x

    urls.UDP_SENDER.sendto(udp_pack_new, ('255.255.255.255',6000))
# *************************************************************************************************End

# *************************************************************************************************Start function
# this function is used for return crc16 packet
def crc16_ccitt(data, crc=0):
   CRC16_CCITT_TAB = \
      [
        0x0000, 0x1021, 0x2042, 0x3063, 0x4084, 0x50a5, 0x60c6, 0x70e7,
        0x8108, 0x9129, 0xa14a, 0xb16b, 0xc18c, 0xd1ad, 0xe1ce, 0xf1ef,
        0x1231, 0x0210, 0x3273, 0x2252, 0x52b5, 0x4294, 0x72f7, 0x62d6,
        0x9339, 0x8318, 0xb37b, 0xa35a, 0xd3bd, 0xc39c, 0xf3ff, 0xe3de,
        0x2462, 0x3443, 0x0420, 0x1401, 0x64e6, 0x74c7, 0x44a4, 0x5485,
        0xa56a, 0xb54b, 0x8528, 0x9509, 0xe5ee, 0xf5cf, 0xc5ac, 0xd58d,
        0x3653, 0x2672, 0x1611, 0x0630, 0x76d7, 0x66f6, 0x5695, 0x46b4,
        0xb75b, 0xa77a, 0x9719, 0x8738, 0xf7df, 0xe7fe, 0xd79d, 0xc7bc,
        0x48c4, 0x58e5, 0x6886, 0x78a7, 0x0840, 0x1861, 0x2802, 0x3823,
        0xc9cc, 0xd9ed, 0xe98e, 0xf9af, 0x8948, 0x9969, 0xa90a, 0xb92b,
        0x5af5, 0x4ad4, 0x7ab7, 0x6a96, 0x1a71, 0x0a50, 0x3a33, 0x2a12,
        0xdbfd, 0xcbdc, 0xfbbf, 0xeb9e, 0x9b79, 0x8b58, 0xbb3b, 0xab1a,
        0x6ca6, 0x7c87, 0x4ce4, 0x5cc5, 0x2c22, 0x3c03, 0x0c60, 0x1c41,
        0xedae, 0xfd8f, 0xcdec, 0xddcd, 0xad2a, 0xbd0b, 0x8d68, 0x9d49,
        0x7e97, 0x6eb6, 0x5ed5, 0x4ef4, 0x3e13, 0x2e32, 0x1e51, 0x0e70,
        0xff9f, 0xefbe, 0xdfdd, 0xcffc, 0xbf1b, 0xaf3a, 0x9f59, 0x8f78,
        0x9188, 0x81a9, 0xb1ca, 0xa1eb, 0xd10c, 0xc12d, 0xf14e, 0xe16f,
        0x1080, 0x00a1, 0x30c2, 0x20e3, 0x5004, 0x4025, 0x7046, 0x6067,
        0x83b9, 0x9398, 0xa3fb, 0xb3da, 0xc33d, 0xd31c, 0xe37f, 0xf35e,
        0x02b1, 0x1290, 0x22f3, 0x32d2, 0x4235, 0x5214, 0x6277, 0x7256,
        0xb5ea, 0xa5cb, 0x95a8, 0x8589, 0xf56e, 0xe54f, 0xd52c, 0xc50d,
        0x34e2, 0x24c3, 0x14a0, 0x0481, 0x7466, 0x6447, 0x5424, 0x4405,
        0xa7db, 0xb7fa, 0x8799, 0x97b8, 0xe75f, 0xf77e, 0xc71d, 0xd73c,
        0x26d3, 0x36f2, 0x0691, 0x16b0, 0x6657, 0x7676, 0x4615, 0x5634,
        0xd94c, 0xc96d, 0xf90e, 0xe92f, 0x99c8, 0x89e9, 0xb98a, 0xa9ab,
        0x5844, 0x4865, 0x7806, 0x6827, 0x18c0, 0x08e1, 0x3882, 0x28a3,
        0xcb7d, 0xdb5c, 0xeb3f, 0xfb1e, 0x8bf9, 0x9bd8, 0xabbb, 0xbb9a,
        0x4a75, 0x5a54, 0x6a37, 0x7a16, 0x0af1, 0x1ad0, 0x2ab3, 0x3a92,
        0xfd2e, 0xed0f, 0xdd6c, 0xcd4d, 0xbdaa, 0xad8b, 0x9de8, 0x8dc9,
        0x7c26, 0x6c07, 0x5c64, 0x4c45, 0x3ca2, 0x2c83, 0x1ce0, 0x0cc1,
        0xef1f, 0xff3e, 0xcf5d, 0xdf7c, 0xaf9b, 0xbfba, 0x8fd9, 0x9ff8,
        0x6e17, 0x7e36, 0x4e55, 0x5e74, 0x2e93, 0x3eb2, 0x0ed1, 0x1ef0,
      ]

   tab = CRC16_CCITT_TAB  # minor optimization (now in locals)
   crc = 0x0000
   for byte in six.iterbytes(data):
      index = ((crc >> 8)) ^ byte
      crc = (((crc << 8) & 0xFFFF) ^ tab[index])
   return crc & 0xffff
# *************************************************************************************************End

# *************************************************************************************************Start function
# Listener of packets for UDP server
def relay_reader():
    try:
        data, sender = urls.UDP_LISTENER.recvfrom(4096)
        return data
    except (AttributeError, OSError):
        urls.UDP_LISTENER.bind(('0.0.0.0', 6000))
        return relay_reader()
# *************************************************************************************************End

# *************************************************************************************************Start function
def relay_data(m, id):
    array = []
    for cn, i in enumerate(m, start=1):
        if i == '00':
            array.append({'device_id': id, 'channel_id': str(cn), 'device_status' : 'false',})
        elif i == '64':
            array.append({'device_id': id, 'channel_id': str(cn), 'device_status' : 'true',})
    return array
# *************************************************************************************************End

# *************************************************************************************************Start function
def site_relays():
    m = []
    devices = getAllDeviceData()
    for i in devices["devices"]:
        if i['device_type'] == "RL":
            s = i["device_id"]
            if s not in m:
                m.append(s)
    return m
# *************************************************************************************************End

# *************************************************************************************************Start function
def setStatus_loop(m):
    data = getAllDeviceData()
    for n in m:
        try:
            h = next(i for i, x in enumerate(data['devices']) if x['channel_id'] == n['channel_id'] and  x['device_id'] == n['device_id'])
            data['devices'][h]['device_status'] = n['device_status']
        except Exception as e:
            print('setStatus_loop:',e)
    return data
# *************************************************************************************************End

# *************************************************************************************************Start function
def main_update():  # sourcery skip: low-code-quality
    while True:
        devices = site_relays()
        # devices_data = getAllDeviceData()
        packets = param.received_packets
        param.received_packets = []
        obj ={}
        for data in packets:
            if data.hex().find('3401fe') != -1:
                device_id = data.hex()[36:]
                device_id = device_id[:2]
                device_id = int(device_id, 16)
                for deviceId in devices:
                    if data.hex().find('3401fe') != -1 and str(device_id) == deviceId:
                        logging.info(f"Receieved status of : {deviceId}")
                        res = data
                        sample_str = res.hex()
                        newstr = ''
                        if len(sample_str) == 104:
                            newstr = sample_str[-52:]
                        elif len(sample_str) == 80:
                            newstr = sample_str[-28:]
                        elif len(sample_str) == 68:
                            newstr = sample_str[-16:]

                        get = newstr[:-4]
                        n = 2
                        arr = [(get[i:i+n]) for i in range(0, len(get), n)]
                        resp = relay_data(arr, deviceId)
                        # devices_data = setStatus_loop(resp)
                        logging.info(f"Saving status of : {deviceId}")

            # Relay opertaions change receiver
            if data.hex().find('32ffff') != -1:
                device_id = getter(data.hex(), "D")
                channel_id = getter(data.hex(), "C")
                operation = getter(data.hex(), "O")
                obj["device_id"]=device_id
                obj["channel_id"]=channel_id
                obj["operation"]=operation

            if len(obj) != 0:
                try:
                    dev = Device.objects.filter(device_information__device_id__contains = obj)
                    dev = Device.objects.filter(device_information__0__device_id=str(obj["device_id"]),device_information__0__channel_id=str(obj["channel_id"]))
                    if len(dev) != 0:
                        dev[0].device_status = obj['operation']
                        dev[0].save()
                    obj ={}
                    # sendUpdateStatus()
                except Exception as e:
                    print("Error: ",e)
# *************************************************************************************************End

# *************************************************************************************************Start function
# Getter for devices parameter from UDP packet
def getter(packet, detail):
    if detail == "D":
        device_id = packet[36:]
        device_id = device_id[:2]
        return int(device_id, 16)
        
    if detail == "C":
        channel_id = packet[50:]
        channel_id = channel_id[:2]
        return int(channel_id, 16)
        
    if detail == "O":  
        channel_id = packet[54:]
        if channel_id[:2] == '64':
            return "true"
        elif channel_id[:2] == '00':
            return "false"
        else:
            return int(channel_id[:2], 16)
    
    if detail == "R":  
        rndom = packet[32:]
        logging.info(rndom[:2])
        return int(rndom, 16)
        
    return "Something is wrong"
# *************************************************************************************************End

# *************************************************************************************************Start function
def site_relay_devices():
    m = []
    devices = Device.objects.all()
    for i in devices:
        main_dict = {
            "record_id":i.id,
            "device_name":i.device_name,
            "device_type":i.device_type,
            "app_type":i.app_type,
            "device_status":i.device_status
        }
        device_object = main_dict | i.device_object[0]
        if device_object['device_type'] == "RL":
            if device_object['app_type'] == "L":
                s = {"device_type" : device_object["device_type"], "device_id" : device_object["device_id"], "app_type": device_object["app_type"]}
                if s not in m:
                    m.append(s)

            if device_object['app_type'] == "S":
                s = {"device_type" : device_object["device_type"], "device_id" : device_object["device_id"], "app_type": device_object["app_type"]}
                if s not in m:
                    m.append(s)
    return m
# *************************************************************************************************End

# *************************************************************************************************Start function
# Getting relay status
def get_relay_status(deviceId):
    dId = pack("B", int(deviceId))

    get = crc16_ccitt(rc.GET_STATUS + dId, crc=0)
    crc_int = hex(get)[2:]
    if len(crc_int) < 4:
        crc_int = f'0{crc_int}'
    sm = r"\x" + r"\x".join(crc_int[n : n+2] for n in range(0, len(crc_int), 2))
    a = sm.replace('\\x', '')
    x = binascii.a2b_hex(a.encode('utf8'))
    udp_pack_new = rc.HEADER + rc.GET_STATUS + dId + x
    urls.UDP_SENDER.sendto(udp_pack_new, ('255.255.255.255',6000))
    time.sleep(0.1)
# *************************************************************************************************End

# *************************************************************************************************Start function    
def get_devices_status():
    logging.info('Getting Status of Devices')
    devices = site_relay_devices()
    urls.no_of_devices = urls.no_of_devices + len(devices)
    for i in devices:
        if i['device_type'] == "RL":
            if i['app_type'] == "L":
                logging.info("Getting Status of Relay : " + i['device_id'])
                # param.logUpdate("Sending request for status of Relay" + i['device_id'])
                get_relay_status(i['device_id'])

            if i['app_type'] == "S":
                logging.info("Getting Status of Relay : " + i['device_id'])
                # param.logUpdate("Sending request for status of Relay" + i['device_id'])
                get_relay_status(i['device_id'])

        #     if i['app_type'] == "AC":
        #         logging.info("Getting Status of AC Panel : " + i['device_id'])
        #         param.logUpdate("Sending request for status of AC Panel" + i['device_id'])

        #         value = {
        #             "device_id" : i['device_id'],
        #             "ac_no" : i['channel_id']
        #         }                
        #         ac_panel_opr.panel_ac_status(value)
        # if i['device_type'] == "AC":
        #     logging.info("No AC device is connected")
        # if i['device_type'] == "AVR":
        #     logging.info("No AVR device is connected")
        # if i['device_type'] == "TV":
        #     logging.info("No TV device is connected")
# *************************************************************************************************End

# *************************************************************************************************Start function   
# Listener for relay 
def device_listener():
    while True:
        data = relay_reader()
        # checkSwitchInput(data)
        param.received_packets.append(data)