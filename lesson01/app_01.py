'''
Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню, подвал),
и дочерние шаблоны для страниц категорий товаров и отдельных товаров. Например, создать страницы «Одежда»,
«Обувь» и «Куртка», используя базовый шаблон.
'''
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def magazine():
    return render_template('base.html')


@app.route('/odejda/')
def odejda():
    odejda = [{'name_odejda': 'vetrovka'},
              {'text_odejda': 'ot vetra'},
              {'date_odejda': 'osen'}
              ]
    return render_template('odejda.html', odejda=odejda)


@app.route('/obuv/')
def obuv():
    obuv = [{'name_obuv': 'galoshi'},
            {'text_obuv': 'tanki gryazi ne boyatsya'},
            {'date_obuv': 'all seazon'}
            ]
    return render_template('obuv.html', obuv=obuv)


@app.route('/kurtka/')
def Kurtka():
    kurtka = [{'name_kurtka': 'shuba'},
            {'text_kurtka': 'norkovaya'},
            {'date_kurtka': 'dlya viebona'}
            ]
    return render_template('kurtka.html', kurtka=kurtka)



if __name__ == '__main__':
    app.run(debug=True)

