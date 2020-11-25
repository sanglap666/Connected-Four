from channels.consumer import AsyncConsumer
import asyncio
from channels.db import database_sync_to_async
import json
from accounts.models import thread

from django.contrib.auth import get_user_model

model = get_user_model()



class ChatConsumer(AsyncConsumer):

    async def websocket_connect(self,event):
        chat_room = "thread1"
        
        threads = await self.get_all_threads(event)
        
        for user_threads in threads:
            
            chat_room = f"thread_{user_threads.id}"                        # creating chat rooms,for current channel, using all threads for a particular user
                                                                            
            await self.channel_layer.group_add(
                chat_room,self.channel_name
            )
        await self.send(
            {
                'type':'websocket.accept',
            }
        )
        print("connected",event)
        

    async def websocket_receive(self,event):
        print("received",event)
        firstuser,seconduser = await self.get_socket_users(event)
        currentthread = await self.get_current_thread(firstuser,seconduser)
        chat_room = f"thread_{currentthread.id}"
                                                                                    #sending connect request to particular user using connected chat_room
        await self.channel_layer.group_send(
            chat_room,
            {
                "type":"chat_message",
                "text":"connect"
            }
        )
    
    async def chat_message(self,event):
        await self.send(
            {
                "type":"websocket.send",
                "text":event['text']
            }
        )
    async def websocket_disconnect(self,event):
        print("disconnected",event)        

    @database_sync_to_async
    def get_socket_users(self,event):

        first = self.scope['user']
        second = model.objects.get(username=event['text'])
        return first,second

    @database_sync_to_async
    def get_current_thread(self,firstuser,seconduser):

        return  thread.objects.get_thread(firstuser,seconduser)

    @database_sync_to_async
    def get_all_threads(self,event):
        
        user = self.scope['user']
        threads = []
               
        for thrd in thread.objects.filter(first=user):
            threads.append(thrd)
        for thrd in thread.objects.filter(second=user):
            threads.append(thrd)     
        print(threads)
        return  threads   