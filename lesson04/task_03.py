import sys
import argparse
import asyncio
import aiohttp
import time

# Вводим URL откуда будем скачивать файлы !
urls = ['https://',
        'https://',
        'https://',
        ]


# парсер
def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument("url_parser", nargs='*', help="Путь", type=str,
                        default=urls)
    return parser


async def get_url(url):
    async with aiohttp.ClientSession() as s:
        async with s.get(url) as responce:
            filename = url.split('/')[-1]
            with open(f'Download_async/{filename}', 'wb') as f:
                txt = await responce.read()
                f.write(txt)
                print(f"Downloaded {url} in {time.time() - ts:.2f} seconds")


async def main():
    tasks = []
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    if namespace.url_parser:
        urls = namespace.url_parser

        for url in urls:
            tasks.append(get_url(url, ))
    await asyncio.gather(*tasks)


ts = time.time()
if __name__ == '__main__':
    asyncio.run(main())
    tf = time.time()
    print(f'Время выполнения: {tf - ts}')
