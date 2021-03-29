from flask import Flask, request, flash
from flask.globals import session
from flask.helpers import make_response, url_for
from flask.templating import render_template
from werkzeug.utils import redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import unittest


app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'SUPER SECRETO'

todos = ['Comprar Café', 'Enviar cuenta de cobro', 'Entregar página al cliente', 'Comprar cervezas']

class LoginForm(FlaskForm):
    username = StringField('Nombre del usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Enviar')

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def not_found(error):
    return render_template('500.html', error=error)

@app.route('/')
def index():
    # raise(Exception('500 error'))
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip

    return response


@app.route('/hello', methods=['GET','Post'])
def hello():
    user_ip = session.get('user_ip')
    login_form = LoginForm()
    username = session.get('username')
  
    context = {
        'user_ip': user_ip,
        'todos': todos,
        'login_form': login_form,
        'username' : username
       
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username

        flash('Nombre de usuario registrado con éxito')

        return redirect(url_for('index'))
    


    return render_template('hello.html', **context)
    # El doble asterisco permite extender diccionarios en python y evitar el uso de context=contex
    # ya que esto implicaria el uso de más código al llamar variables (context.user_ip o context.todos)
    # return 'Hello Work Dante, su ip es {}' .format(user_ip)