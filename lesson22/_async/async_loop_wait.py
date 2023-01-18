import asyncio
import random


async def print_number(number):
    delay = random.randint(1, 3)
    await asyncio.sleep(delay)
    print(f"Completed {number} delay - {delay}")


async def main():
    tasks = [asyncio.create_task(print_number(number)) for number in range(10)]
    for task in tasks:
        await task

if __name__ == "__main__":
    # # asyncio.wait
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(
    #    asyncio.wait([
    #        print_number(number)
    #        for number in range(10)
    #    ])
    # )
    # loop.close()
    asyncio.run(main())

