async def handler_reaction(client, payload):
    member = client.get_guild(payload.guild_id).get_member(payload.user_id)
    if payload.event_type == "REACTION_ADD":
        msg = await client.get_channel(payload.channel_id).fetch_message(payload.message_id)
        await msg.remove_reaction(payload.emoji, member)
