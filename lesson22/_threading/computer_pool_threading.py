import time
from queue import Empty, Queue
from threading import Thread

import requests

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
THREAD_POOL_SIZE = 5


def fetch_computers(page):
    url = URL.format(page)
    response = requests.get(url)
    response.raise_for_status()
    for item in response.json()["data"]["products"]:
        show_name = item['name'][:16] + '...'
        result = f"{show_name:20} {item['brand']:20} {item['salePriceU'] / 100}"
        print(result)


def worker(work_queue):
    while not work_queue.empty():
        try:
            item = work_queue.get(block=False)
        except Empty:
            break
        else:
            fetch_computers(item)
            work_queue.task_done()


def main():
    work_queue = Queue()

    for page in range(1, PAGES + 1):
        work_queue.put(page)

    threads = [
        Thread(target=worker, args=(work_queue,))
        for _ in range(THREAD_POOL_SIZE)
    ]

    for thread in threads:
        thread.start()

    work_queue.join()

    while threads:
        threads.pop().join()



if __name__ == '__main__':
    started = time.time()
    main()
    elapsed = time.time() - started

    print()
    print("Время выполнения: {:.2f}s".format(elapsed))