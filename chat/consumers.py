from django.contrib.auth import get_user_model
import json
from channels.generic.websocket import AsyncWebsocketConsumer


User = get_user_model()

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        
        