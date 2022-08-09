import json
import logging
from channels.generic.websocket import AsyncJsonWebsocketConsumer

live_users = []

class UserDashConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.role_id = self.scope['url_route']['kwargs']['role_id']
        self.user_id = self.scope['url_route']['kwargs']['user_id']
        self.user_type = self.scope['url_route']['kwargs']['user_type']

        self.user_group = f'user_{self.user_id}_{self.role_id}_{self.user_type}'

        # Join room group
        await self.channel_layer.group_add(
            self.user_group,
            self.channel_name
        )
        
        await self.accept()
        if self.user_group not in live_users:
            live_users.append({"user_id" : self.user_id,"role_id": self.role_id, "user_type": self.user_type, "user_group" : self.user_group})
            logging.info(f"Connected Users Are : {str(live_users)}")

        # await self.channel_layer.group_send(self.user_group, {
        #     'type': 'card_config',
        #     'response': user_dashboard(self.user_id),
        # })

        # await self.channel_layer.group_send(self.user_group, {
        #     'type': 'cards_type_config',
        #     'response': card_opr.card_types(),
        # })

        # await self.channel_layer.group_send(self.user_group, {
        #     'type': 'site_config',
        #     'response': user_site_config(self.user_id, self.role_id, self.user_type),
        # })

    async def disconnect(self, close_code):
        logging.info('User Disconnecting...')
        self.channel_layer.group_discard(self.user_group, self.channel_name)
        for user in live_users:
            if self.user_group in user['user_group']:
                live_users.remove(user)
                logging.info(f"Disconnectin User : {self.user_group}")
                logging.info(f"Now Connected Users Are : {str(live_users)}")


    
    async def receive(self, text_data):
        logging.info(text_data)
        """
        Receive message from WebSocket.
        Get the event and send the appropriate event
        """
        response = json.loads(text_data)
        
        

    # async def card_config(self, res):
    #     """ Receive message from room group """
    #     # Send message to WebSocket
    #     await self.send(text_data=json.dumps({
    #         "status_code": 200,
    #         "payload": res,
    #     }))
    
    # async def site_config(self, res):
    #     """ Receive message from room group """
    #     # Send message to WebSocket
    #     await self.send(text_data=json.dumps({
    #         "status_code": 200,
    #         "payload": res,
    #     }))

    # async def cards_type_config(self, res):
    #     """ Receive message from room group """
    #     # Send message to WebSocket
    #     await self.send(text_data=json.dumps({
    #         "status_code": 200,
    #         "payload": res,
    #     }))

    async def device_json(self, res):
        """ Receive message from room group """
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            "status_code": 200,
            "payload": res,
        }))

    async def dataSender(self, data):
        logging.info("++++++++++++")
        self.channel_layer.group_send(self.user_group, {
            'type': 'send_message',
            'response': data,
        })


# // CRC00003 16:22:23:883 : 0F 01 FE FF FE 00 31 01 3E 03 64 00 00 12 02
# // CRC00004 16:22:30:229 : 0F 01 FE FF FE 00 31 01 3E 02 00 00 00 23 1D
# // CRC00005 16:22:32:890 : 0F 01 FE FF FE 00 31 01 3E 03 00 00 00 55 A9
# // CRC00006 16:22:34:935 : 0F 01 FE FF FE 00 31 01 3E 04 00 00 00 04 84
# // CRC00007 16:22:40:976 : 0F 01 FE FF FE 00 31 01 3E 01 00 00 00 B8 C1
# // CRC00005 16:25:02:398 : 0F 01 FE FF FE 00 31 01 3E 02 64 00 00 64 B6
# // CRC00004 16:26:11:161 : 0F 01 FE FF FE 00 31 01 3E 03 64 00 00 12 02