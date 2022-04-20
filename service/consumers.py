from service.views import *
import json
import random
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from service.model import room,hosting
from getmac import get_mac_address as gma

class ChatConsumer(WebsocketConsumer):
    def websocket_connect(self,event):
        print('CONNECTED>>>>>>>>')
        # me=gma()
        # room.objects.create(host1=me,host2=me).save()
        # try:
        #     hosting.objects.get(ip=me)

        # except hosting.DoesNotExist:
        #     ip_address = hosting.objects.create(status=1,ip=me, pub_date=datetime.datetime.now())
        #     ip_address.save()

        # try:
        #     ip_list=hosting.objects.filter(status=1)
        #     if ip_list:
        #         ip_list=ip_list.exclude(ip=me)
        #         ip2=random.choice(ip_list)
        #         other_user=ip2
        #         try:
        #             room.objects.filter(host1=me).delete()
        #             room.objects.filter(host2=me).delete()
        #             room.objects.filter(host1=other_user).delete()
        #             room.objects.filter(host2=other_user).delete()
        #         except:
        #             pass
        #         room.objects.create(host1=me,host2=other_user).save()
        # except:
        #     pass
        # self.room='1'
        # self.room=str(room.objects.only('room_id').get(host1=me).room_id)
        # print(self.room)
        # self.send({
        #     "type":"websocket.accept"
        # })
        self.room='sss'
        async_to_sync(self.channel_layer.group_add)(
            self.room,
            self.channel_name
        )
        self.accept()
        # print(f'[{self.channel_layer}]','you are connected')

    def chat_message(self,event):
        message=event['message']

        self.send(text_data=json.dumps({
            'type':'chat',
            'message': message
       }))


    def receive(self,text_data):
        text_data_json=json.loads(text_data)
        message=text_data_json['message']

        print('message: ',message)
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

    # def disconnect(self, close_code):
    #     room.objects.filter(room_id=self.room).delete()