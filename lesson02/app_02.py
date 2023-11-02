'''
Создать страницу, на которой будет форма для ввода имени и электронной почты,
при отправке которой будет создан cookie-файл с данными пользователя,
а также будет произведено перенаправление на страницу приветствия, где будет отображаться имя пользователя.
На странице приветствия должна быть кнопка «Выйти»,
при нажатии на которую будет удалён cookie-файл с данными пользователя и
произведено перенаправление на страницу ввода имени и электронной почты.
'''

from flask import Flask, render_template, request, redirect, url_for, make_response


app = Flask(__name__)



@app.route('/music/', methods=['GET', 'POST'])
def music_cook():
    if request.method == 'POST':
        name = request.form.get('name')
        mail = request.form.get('music')
        response = make_response(render_template('hw.html'))
        response.set_cookie(key='name',value='name',max_age=0)
        return response
    return render_template('hw.html')

@app.route('/set/', methods=['GET', 'POST'])
def set_cookie():
    if request.method == 'POST':
        name = request.form.get('name')
        response = make_response(render_template('HW_mail_2.html',name=name)) #объект ответа
        response.set_cookie(key='name',value=name)
        return response
    return redirect(url_for('music_cook'))



if __name__ == '__main__':
    app.run(debug=False)
