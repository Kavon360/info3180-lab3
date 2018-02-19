from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretpass'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '2525'
app.config['MAIL_USERNAME'] = 'insert usr name'
app.config['MAIL_PASSWORD'] = 'insert password'

mail = Mail(app)
from app import views
