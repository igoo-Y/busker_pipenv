# consumers.py 는 사용자가 서버에 연결하기 위한 views.py 와 같음. 웹소켓을 사용하여 consumers.py 에 연결됨.
# channels 가 websocket 연결을 받아들이면 root routing configuration 을 통해 consumers.py 를 찾은 후에 이벤트를 처리하기 위한 함수를 호출함.

import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer  #
from django.dispatch.dispatcher import receiver


class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.room_group_name = "Test-Room"

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

        print("Disconnected")

    async def receive(self, text_data):
        receive_dict = json.loads(text_data)
        message = receive_dict["message"]
        action = receive_dict["action"]

        if (action == "new-offer") or (action == "new-answer"):
            receiver_channel_name = receive_dict["message"][
                "receiver_channel_name"
            ] = self.channel_name

            await self.channel_layer.send(
                receiver_channel_name,
                {"type": "send.sdp", "receive_dict": receive_dict},
            )

            return

        receive_dict["message"]["receiver_channel_name"] = self.channel_name

        await self.channel_layer.group_send(
            self.room_group_name, {"type": "send.sdp", "receive_dict": receive_dict}
        )

    async def send_sdp(self, event):
        receive_dict = event["receive_dict"]

        await self.send(text_data=json.dumps(receive_dict))
