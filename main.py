from app.forms import LoginForm
from flask import request
from flask.globals import session
from flask.helpers import make_response
from flask.templating import render_template
from werkzeug.utils import redirect

import unittest

from app import create_app
from app.forms import LoginForm

app = create_app()

todos = ['Comprar Café', 'Enviar cuenta de cobro', 'Entregar página al cliente', 'Comprar cervezas']



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


@app.route('/hello', methods=['GET'])
def hello():
    user_ip = session.get('user_ip')
    # login_form = LoginForm()
    username = session.get('username')
  
    context = {
        'user_ip': user_ip,
        'todos': todos,
        # 'login_form': login_form,
        'username' : username
       
    }

    return render_template('hello.html', **context)
    # El doble asterisco permite extender diccionarios en python y evitar el uso de context=contex
    # ya que esto implicaria el uso de más código al llamar variables (context.user_ip o context.todos)
    # return 'Hello Work Dante, su ip es {}' .format(user_ip)