import pyrebase
from flask import *
from flask import render_template, request, redirect, session
app = Flask(__name__)
import os

config = {
    "apiKey": "AIzaSyDv1uJ42TwjTDJm0_-kCtiAqq6h305JmJM",
    "authDomain": "motor-f93e9.firebaseapp.com",
    "databaseURL": "https://motor-f93e9.firebaseio.com",
    "projectId": "motor-f93e9",
    "storageBucket": "motor-f93e9.appspot.com",
    "messagingSenderId": "58141624646",
    "appId": "1:58141624646:web:a2c6ab6314646485633d47"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    if (request.method == 'POST'):
            email = request.form['name']
            password = request.form['password']
            try:
                auth.sign_in_with_email_and_password(email, password)
                #user_id = auth.get_account_info(user['idToken'])
                #session['usr'] = user_id
                return render_template('home.html')
            except:
                unsuccessful = 'Please check your credentials'
                return render_template('index.html', umessage=unsuccessful)
    return render_template('index.html')

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if (request.method == 'POST'):
            email = request.form['name']
            password = request.form['password']
            auth.create_user_with_email_and_password(email, password)
            return render_template('index.html')
    return render_template('create_account.html')

@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if (request.method == 'POST'):
            email = request.form['name']
            auth.send_password_reset_email(email)
            return render_template('index.html')
    return render_template('forgot_password.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run()
