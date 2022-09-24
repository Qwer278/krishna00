from service.views import *
import json
from ipware import get_client_ip
import random
import time

from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from service.model import room,hosting
from getmac import get_mac_address as gma
import datetime
import socket

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        print('CONNECTED>>>>>>>>')
        self.accept()
        # hn=socket.gethostname()
        # ip=socket.gethostbyname(hn)
        # me=ip
        # print(ip)
        # room.objects.create(host1=me,host2=me).save()
        # try:
        #     hosting.objects.get(ip=me)

        # except hosting.DoesNotExist:
        #     ip_address = hosting.objects.create(status=1,ip=me, pub_date=datetime.datetime.now())
        #     ip_address.save()

        # try:
        #     ip_list=hosting.objects.filter(status=1)
        #     ip_list=ip_list.exclude(ip=me)
        #     if not ip_list:
        #         time.sleep(5)
        #     if ip_list:
                
        #         ip2=random.choice(ip_list)
        #         # print('other user >>>>>>>>>>>>>>>>>>>>>>',ip2.ip)
        #         other_user=ip2
        #         try:
        #             room.objects.filter(host1=me).delete()
        #             room.objects.filter(host2=me).delete()
        #             room.objects.filter(host1=other_user).delete()
        #             room.objects.filter(host2=other_user).delete()
        #         except:
        #             print('Not USER Found>>>>>>')
            
        #         room.objects.create(host1=me,host2=ip2.ip).save()
        # except:
        #     pass
        # # self.room='1'
        # self.room=str(room.objects.only('room_id').get(host1=me).room_id)
        # # print(self.room)
        # # self.send({
        # #     "type":"websocket.accept"
        # # })
        # # self.room='sss'

        # async_to_sync(self.channel_layer.group_add)(
        #     self.room,
        #     self.channel_name)
        # self.accept()
        # print(f'[{self.channel_layer}]','you are connected')
    
    # def chat_message(self,event):
    #     message=event['message']
    #     print('mesage',event)
    #     self.send(text_data=json.dumps({
    #         'type':'chat',
    #         'message': event['message']
    #     }))

    

    # def receive(self,text_data):
    #     print('Message Received...',text_data)
        
    #     text_data_json=json.loads(text_data)
    #     message=text_data_json['message']

    #     print('message: ',message)
    #     self.send(text_data=json.dumps({
    #         'type':'chat',
    #         'message':message,
    #     }))
    #     async_to_sync(self.channel_layer.group_send)(
    #         'programmers',
    #         {
    #             'type':'chat.message',
    #             'message':message
    #         }
    #     )

    # def disconnect(self, close_code):
        
    #     room.objects.filter(room_id=self.room).delete()