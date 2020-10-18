async def handler_voice(client, member, state):
    if member.voice is not None and member.voice.mute:
        await member.edit(mute=False)
