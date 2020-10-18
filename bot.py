import discord
import os
import traceback
from handler import bot_handler_cmd
from handler import bot_handler_loop
from handler import bot_handler_reaction
from handler import bot_handler_voice
from basics import bot_defines

channel_id_data = bot_defines.channel_id_data

intents = discord.Intents.all()
intents.typing = False
intents.presences = False
client = discord.Client(intents=intents)


async def errorHandler(e, loc):
    await client.get_channel(channel_id_data["bottest"]).send(loc + ": " + str(e))
    traceback.print_exc()


async def createTask():
    client.bg_task1 = client.loop.create_task(bot_handler_loop.handler_loop(client))


@client.event
async def on_ready():
    await createTask()
    print("Bot is Online!")


@client.event
async def on_message(message):
    try:
        if message.author == client.user:
            return
        elif message.content.startswith("!"):
            await bot_handler_cmd.handler_cmd(client=client, message=message)
    except Exception as e:
        await errorHandler(e, "On message")


@client.event
async def on_raw_reaction_add(payload):
    try:
        if payload.user_id == client.user.id:
            return
        await bot_handler_reaction.handler_reaction(client=client, payload=payload)
    except Exception as e:
        await errorHandler(e, "On reaction add")


@client.event
async def on_raw_reaction_remove(payload):
    try:
        if payload.user_id == client.user.id:
            return
        await bot_handler_reaction.handler_reaction(client=client, payload=payload)
    except Exception as e:
        await errorHandler(e, "On reaction remove")


@client.event
async def on_voice_state_update(member, before, state):
    try:
        if state.channel is None:
            state = before
        await bot_handler_voice.handler_voice(client, member, state)
    except Exception as e:
        await errorHandler(e, "Voice handler")


@client.event
async def on_member_join(member):
    try:
        pass
        # await bot_handler_onjoin.handler_onjoin(client, member)
    except Exception as e:
        await errorHandler(e, "On member join")


@client.event
async def on_member_remove(member):
    try:
        pass
        # await bot_handler_onleave.handler_onleave(client, member)
    except Exception as e:
        await errorHandler(e, "On member remove/leave")


client.run(bot_defines.token)
print("-----------------------------------------------------------------------------")
os.system("python3 basics/BotStarter.py")
