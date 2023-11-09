import sys
import argparse
import multiprocessing
import requests
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


def get_url(url):
    response = requests.get(url)
    filename = url.split('/')[-1]
    with open(f'Download_multi/{filename}', 'wb') as f:
        f.write(response.content)


if __name__ == '__main__':
    te=0
    proces = []
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    if namespace.url_parser:
        urls = namespace.url_parser

        for url in urls:
            ts = time.time()
            t = multiprocessing.Process(target=get_url, args=(url,))
            proces.append(t)
            t.start()
            tf = time.time()
            te += (tf - ts)
            print(f'Прошло времени: {tf - ts}')

    for i in proces:
        i.join()
    print(f'Всего времени прошло: {te}')