from channels.generic.websocket import AsyncJsonWebsocketConsumer
from BMS_Apps.Devices.operations import Operations,getAllDeviceData
import json
import logging

dev_oprs_obj= Operations()
class BmsConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            "wss",
            self.channel_name
        )
        await self.accept()
        data= getAllDeviceData()
        
        await self.channel_layer.group_send("wss", {
                'type': 'bms_main',
                'response': data,
            })

    async def disconnect(self, close_code):
        logging.info('User Disconnecting...')
        self.channel_layer.group_discard("wss", self.channel_name)
    
    async def receive(self, text_data):
        """
        Receive message from WebSocket.
        Get the event and send the appropriate event
        """
        response = json.loads(text_data)
        logging.info("received data")
        dev_oprs_obj.check_opr(response)

    async def bms_main(self, res):
        """ Receive message from room group """
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            "payload": res,
        }))

    async def dataSender(self, data):
        self.channel_layer.group_send("wss", {
            'type': 'bms_main',
            'response': data,
        })