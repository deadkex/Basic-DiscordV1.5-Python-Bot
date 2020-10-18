import asyncio


async def handler_loop(client):
    await client.wait_until_ready()
    while True:
        # do smth over and over as background task
        await asyncio.sleep(60)
