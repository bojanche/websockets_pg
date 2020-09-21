# chat/consumers.py
import json
from channels.generic.websocket import WebsocketConsumer
import psutil


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        cpu = psutil.cpu_percent()
        message = text_data_json['message']
        print(message)
        self.send(text_data=json.dumps({
            'message': message, 'cpu': cpu
        }))