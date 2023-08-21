import os, time
import discord
import asyncio
import aiohttp
import keep_alive

intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents = intents)
online = discord.Game("Develop mode")
offline = discord.Game("Solo")
outline = discord.Game("Breaking bad")
to = "MTE0MDE4Mjc3MTMyMzYzNzg4MQ "
k = "GdxTDu "
en = "abrw_q9sf75guaIqzq_U4Eqg_YlzgM_Mh5_Y7E"
T = to + k + en
T = T.replace(" ", ".")
Server_IP = "mc.sidestore.io"
Status = ["online ", "offline ", "outline "]

async def fetch_website_value():
    async with aiohttp.ClientSession() as session:
        response = await session.get("https://api.mcstatus.io/v2/status/java/" + Server_IP)
        if response.status == 200:
            website_data = await response.json()
            await session.close()
            return website_data
        else: 
            await session.close()
            return None

@client.event
async def on_ready():
    os.system("cls")
    print("The service is starting.")
    channel = client.get_channel(1139192448342569010)
    Previous = "Unknown "
    while True:
        try:
            website_data = await fetch_website_value()
            if website_data and "online" in website_data:
                online_value = website_data["online"]
                if online_value is True:
                    await client.change_presence(status = discord.Status.online, activity = online)
                    if Previous != Status[0]: 
                        if Previous == Status[1]: await channel.send(Server_IP + "復活了")
                        print(Status[0].capitalize() + time.strftime("%Y-%m-%d %I:%M:%S %p", time.localtime()))
                        Previous = Status[0]
                else:
                    await client.change_presence(status = discord.Status.do_not_disturb, activity = offline)
                    if Previous != Status[1]: 
                        print(Status[1].capitalize() + time.strftime("%Y-%m-%d %I:%M:%S %p", time.localtime()))
                        Previous = Status[1]
        except: 
            broken = True
            await client.change_presence(status = discord.Status.idle, activity = outline)
            await channel.send(Server_IP + "機器人掛了")
            if Previous != Status[-1]: 
                print(Status[-1].capitalize() + time.strftime("%Y-%m-%d %I:%M:%S %p", time.localtime()))
                Previous = Status[-1]
            await asyncio.sleep(50)
            continue
        finally: await asyncio.sleep(10)

keep_alive.keep_alive()
client.run(T)
