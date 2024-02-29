from django.contrib.auth import get_user_model
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from urllib.parse import parse_qs
from channels.db import database_sync_to_async
from rest_framework_simplejwt.tokens import AccessToken


User = get_user_model()

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        
        query_string = parse_qs(self.scope['query_string'].decode())
        token = query_string.get('token',[None])[0]
        
        
        if token :
            self.user = await self.get_user_from_jwt(token)
            if not self.user:
                await self.close()
                return
        else:
            await self.close()
            return
        
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        
    async def disconnect(self ,close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        
    async def receive(self , text_data):
        text_data_json = json.loads(text_data)
        
        
        message = text_data_json['message']
        username = self.user.username
        
        
        
        await self.channel_layer.group_send(
            
            self.room_group_name,
            {
                'type': 'chat_message',
                'username' : username,
                'message' :message
            }
        )
        
    async def chat_message(self , event):
        username = event['username']
        message = event['message']
        
        
        await self.send(text_data=json.dumps({
            'username' : username,
            'message' :message,
            
        }))
        
        
        
    @database_sync_to_async
    def get_user_from_jwt(self,token):
        try: 
            access_token = AccessToken(token)
            user_id = access_token.payload['user_id']
            return User.objects.get(id = user_id)
        except Exception as e:
            print("error" , e)
            return None
        
    