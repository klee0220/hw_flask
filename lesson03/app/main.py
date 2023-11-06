from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegistrationForm
from models import db, User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///mydatabase.db'
db.init_app(app)
csrf = CSRFProtect(app)


@app.route('/')
def hello():
    return 'Hi!'


@app.cli.command("init-db")
def init_db():
   db.create_all()


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        firstname = form.firstname.data
        secondname = form.secondname.data
        email = form.email.data
        password = form.password.data
        hash = generate_password_hash(password)
        print(firstname,secondname,email,hash)
        print(check_password_hash(hash, password))

        new_user = User(
            firstname=firstname,
            secondname=secondname,
            email=email,
            password=hash
         )
        db.session.add(new_user)
        db.session.commit()
        success_msg = 'Поздравляю вы зарегестрированы!'
        return success_msg
    return render_template('register.html', form=form)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)