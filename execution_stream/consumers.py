# execution_stream/consumers.py

import asyncio
import subprocess
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ExecutionConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        command = data['command']

        try:
            process = await asyncio.create_subprocess_shell(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            while True:
                output = await process.stdout.readline()
                if not output:
                    break

                await self.send(text_data=json.dumps({'output': output.decode()}))
        except asyncio.CancelledError:
            process.terminate()
            raise
