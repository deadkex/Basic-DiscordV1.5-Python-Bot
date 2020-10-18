import discord
from basics import bot_defines

role_names = bot_defines.role_names


async def handler_cmd(client, message):
    msg = message.content.split('!', 1)[1]
    cmd = msg.split(' ')[0].lower()

    if str(message.channel.type) != "private":
        if role_names["owner"] in str(message.author.roles):
            await message.channel.send("Hi! " + message.author.mention)

    if cmd == "restart":
        await case_restart(client=client, message=message)


async def case_restart(**kwargs):
    client = kwargs.get("client"); message = kwargs.get("message")
    try:
        await message.delete()
    except discord.errors.NotFound:
        pass
    try:
        client.bg_task1.cancel()
    except RuntimeError:
        pass
    await client.logout()
