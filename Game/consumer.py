from channels.consumer import AsyncConsumer
import asyncio



class ChatConsumer(AsyncConsumer):

    async def websocket_connect(self,event):

        await self.send(
            {
                'type':'websocket.accept',
            }
        )
        print("connected",event)

    async def websocket_receive(self,event):
        print("received",event)

    async def websocket_disconnect(self,event):
        print("disconnected",event)        

class HomeConsumer(AsyncConsumer):

    async def websocket_connect(self,event):

        await self.send(
            {
                'type':'websocket.accept',
            }
        )
        print("connected",event)

    async def websocket_receive(self,event):
        print("received",event)

    async def websocket_disconnect(self,event):
        print("disconnected",event)