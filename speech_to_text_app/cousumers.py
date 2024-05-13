# from channels.generic.websocket import AsyncWebsocketConsumer

# class SpeechConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         print('connected')
#         await self.accept()

#     async def disconnect(self, close_code):
#         print('disconnected')
#         pass

#     async def receive(self, text_data):
#         print('received')
#         # Process incoming messages from the client
#         pass

from channels.generic.websocket import AsyncWebsocketConsumer

class AudioConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        # Process incoming audio data and convert it to text
        # Send the transcription back to the client