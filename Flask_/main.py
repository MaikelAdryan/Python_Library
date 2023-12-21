from flask import Flask, url_for, render_template

APP = Flask(__name__)

@APP.route('/')
def ola_mundo():
  title = 'Hello'
  users = [
    {'name': 'Adryan', 'active': True},
    {'name': 'Litão', 'active': False}
  ]
  return render_template('index.html', title=title, users=users)

@APP.route('/sobre')
def pagina_sobre():
  return '''
    <h1><strong>Eu sou o Adryan Maikel</strong></h1>
  '''

APP.run(debug=True)
