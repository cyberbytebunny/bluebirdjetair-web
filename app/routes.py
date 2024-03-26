from flask import Blueprint, render_template, request, redirect, session, current_app
import secrets
from hashlib import md5

main = Blueprint('main', __name__)

@main.before_request
def make_session_permanent():
    session.permanent = True

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/login', methods=['GET'])
def loginPage():
    if 'username' in session:
        return redirect('/flag')
    return render_template('login.html')

@main.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    session['username'] = username
    session['id'] = md5(str((password + secrets.token_hex(8))).encode()).hexdigest()
    return redirect('/flag') # Redirect to a dashboard view upon successful login

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')

@main.route('/flag')
def flag():
    if 'username' not in session:
        return redirect('/login')

    username = session.get('username')
    if session.get('id') == current_app.config['ADMIN_ID']:
        show_flag = True
        flag_content = current_app.config['FLAG']
    else:
        show_flag = False
        flag_content = ''

    return render_template('flag.html', username=username, show_flag=show_flag, flag_content=flag_content)

#Testing to see if username can be rendered from URL
@main.route('/test', methods=['GET'])
def test_session():
    username = request.args.get('username', 'Anonymous')
    return render_template('flag.html', username=username, show_flag=False, flag_content="NOT-A-REAL-FLAG")

@main.route('/signout')
def signout():
    session.clear()
    return redirect('/login')