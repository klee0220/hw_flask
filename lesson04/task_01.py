import asyncio
import sys
import multiprocessing
import threading
import requests
import time
import aiohttp



def get_url(url: str):
    response = requests.get(url).content
    with open(f'{url.split("/")[-1]}', "wb") as f:
        f.write(response)


def start_thread(urls: list):
    tm = time.time()
    threads = []
    for i in urls:
        t = threading.Thread(target=get_url, args=i)
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()
    td = time.time()
    print(f'Download time {td - tm}')


def get_url_multi(url: str):
    response = requests.get(url).content
    with open(f'{url.split("/")[-1]}', "wb") as f:
        f.write(response)


def start_multiproc(urls: list):
    tm = time.time()
    proces = []
    for i in urls:
        t = multiprocessing.Process(target=get_url_multi, args=i)
        proces.append(t)
        t.start()

    for i in proces:
        i.join()
    td = time.time()
    print(f'Download time {td - tm}')


async def get_url_a(url: str):
    async with aiohttp.ClientSession() as s:
        async with s.get(url) as resp:
            async with s.get(url) as responce:
                with open(f'{url.split("/")[-1]}', "wb") as f:
                    content = await responce.content.read()
                    f.write(content)


async def main():
    tasks = []
    for url in urls:
        tasks.append(get_url_a(url))
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    urls = sys.argv[1:]
    a = int(input("How to download file?: 1 - Multithreaded, 2 - Multiprocessor, 3 - Asynchronously :"))
    if a in [1, 2, 3]:
        if a == 3:
            tm = time.time()
            asyncio.run(main())
            td = time.time()
            print(f'Time need for: {td - tm}')
        elif a == 1:
            start_thread(urls)
        elif a == 2:
            start_multiproc(urls)
    else:
        print("You should more careful!!")
