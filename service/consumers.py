from service.views import *
from email import message
import imp
import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from service.model import room,Thread

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        me=''
        other_user=''
        thread_obj=Thread.objects.get_or_create_personal_thread(me,other_user)
        self.room='str(room_id)'

        async_to_sync(self.channel_layer.group_add)(
            self.room,
            self.channel_name
        )
        self.accept()
        r=room.objects.create(room_id=self.room,host1=ip1,host2=ip2)
        # room.objects.create(room_id=self.channel_name)

        # self.send(text_data=json.dumps({
        #     'type':'Connection Complete',
        #     'message': 'You are now connected'
        # }))
    
    def chat_message(self,event):
        message=event['message']

        self.send(text_data=json.dumps({
            'type':'chat',
            'message': message
        }))


    def receive(self,text_data):
        text_data_json=json.loads(text_data)
        message=text_data_json['message']

        # print('message: ',message)
        # self.send(text_data=json.dumps({
        #     'type':'chat',
        #     'message':message,
        # }))

        async_to_sync(self.channel_layer.group_send)(
            self.room,
            {
                'type':'chat_message',
                'message':message
            }
        )

    def disconnect(self, close_code):
        room.objects.filter(room_id=self.channel_name).delete() 