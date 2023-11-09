'''
Написать программу, которая скачивает изображения с заданных URL-адресов и
сохраняет их на диск. Каждое изображение должно сохраняться в отдельном
файле, название которого соответствует названию изображения в URL-адресе.
Например URL-адрес: https://example/images/image1.jpg -> файл на диске:
image1.jpg
Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
Программа должна иметь возможность задавать список URL-адресов через
аргументы командной строки.
Программа должна выводить в консоль информацию о времени скачивания
каждого изображения и общем времени выполнения программы.
'''

import sys
import argparse
import threading
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
    with open(f'Download_thread/{filename}', 'wb') as f:
        f.write(response.content)


if __name__ == '__main__':
    te=0
    threads = []
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    if namespace.url_parser:
        urls = namespace.url_parser

        for url in urls:
            ts = time.time()
            t = threading.Thread(target=get_url, args=(url,))
            t.start()
            tf = time.time()
            te += (tf - ts)
            print(f'Прошло времени: {tf - ts}')

    for tread in threads:
        tread.join()
print(f'Всего времени прошло: {te}')
