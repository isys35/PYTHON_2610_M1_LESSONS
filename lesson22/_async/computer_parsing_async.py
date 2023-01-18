import time

import aiohttp
import asyncio

URL = "https://catalog.wb.ru/catalog/electronic15/" \
      "catalog" \
      "?__tmp=by" \
      "&appType=1" \
      "&couponsGeo=12,7,3,21" \
      "&curr=byn" \
      "&dest=12358386,12358403,-70563,-8139704" \
      "&emp=0" \
      "&lang=ru" \
      "&locale=by" \
      "&page={}" \
      "&pricemarginCoeff=1" \
      "&reg=0" \
      "&regions=80,83,4,33,70,69,86,30,40,48,1,66,31,68,22" \
      "&sort=popular" \
      "&spp=0" \
      "&subject=2872;2875" \
      "&xsubject=2875"

PAGES = 10


async def get_computers(session: aiohttp.ClientSession, page: str):
    async with session.get(URL.format(page)) as response:
        computers = (await response.json(content_type=None))["data"]["products"]
        return computers


async def print_results(results_corutine):
    results = (await results_corutine)
    for item in results:
        show_name = item['name'][:16] + '...'
        result_print = f"{show_name:20} {item['brand']:20} {item['salePriceU'] / 100}"
        print(result_print)


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [
            asyncio.create_task(print_results(get_computers(session, page)))
            for page in range(1, PAGES + 1)
        ]
        for task in tasks:
            await task


if __name__ == '__main__':
    started = time.time()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
    elapsed = time.time() - started
    print()
    print("Время выполнения: {:.2f}s".format(elapsed))
