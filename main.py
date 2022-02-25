import discord
import asyncio
from quart import Quart,request

app = Quart(__name__)
client = discord.Client()


@app.before_serving
async def before_serving():
    loop = asyncio.get_event_loop()
    await client.login("OTQ1ODQ4MTY5NTI5NDc5MjQ4.YhWHwA.HotOS0Ien-Rr4sHNBumT1nmkrUY")
    loop.create_task(client.connect())


@app.route("/send", methods=["POST"])
async def send_message():
    content = await request.get_json()
    message = content["message"]
    user_id = content["user_id"]
    # wait_until_ready and check for valid connection is missing here
    user = await client.fetch_user(user_id)
    await user.send(message)
    return 'ok'


app.run()