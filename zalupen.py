import asyncio
from aiocryptopay import AioCryptoPay, Networks

crypto = AioCryptoPay(token='19233:AA0pnalXO6w39fhV3TExZf9A7p3jB4x0vQl', network=Networks.TEST_NET)

async def get_last_transfers(asset='USDT'):
    transfers = await crypto.get_transfers(asset=asset, count=50000)
    for transfer in transfers:
        print(transfer)

# Создаем событийный цикл
loop = asyncio.get_event_loop()
# Запускаем функцию get_last_transfers в событийном цикле
loop.run_until_complete(get_last_transfers())