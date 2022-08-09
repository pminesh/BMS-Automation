import logging
from BMS_Apps.RelayOperations.views import relay_opr
from BMS_Apps.Devices.views import getAllDeviceData

class Operations():
    def check_opr(self, res):
        device = getAllDeviceData()
        if res['opr'] == "service" and res['opr_type'] == 'service_opr' and res['record']['device_type'] == 'RL':
            my_gen =  next((x for x in device["devices"] if x["record_id"] == int(res['record']["record_id"])), None)
            logging.info("Relay operation received")
            
            # Light
            if res['record']['app_type'] == 'L':
                my_gen["device_status"] = res['record']["device_status"]
                relay_opr(res['record'])
                
            # Speaker
            if res['record']['app_type'] == 'S':
                my_gen["device_status"] = res['record']["device_status"]
                relay_opr(res['record'])
                
            # AC
            if res['record']['app_type'] == 'AC':
                my_gen["device_status"] = res['record']["device_status"]
                # ac_panel_opr.pannel_ac_control(res['record'])

            # Curtain
            if res['record']['app_type'] == 'C':
                my_gen["device_status"] = res['record']["device_status"]
                # curtain_opr.curtain_opr(res['record'], res['opr_param'])

            return True