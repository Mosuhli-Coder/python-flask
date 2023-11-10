from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Tiger!'

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name

@app.route('/admin')
def hello_admin():
    return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest!' % guest

@app.route('/user/<name>')
def hello_user(name):
    if name=='admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))


@app.route('/welcome/<name>')
def welcome(name):
    return 'Welcome to my website! %s' % name

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        # handle the form data submitted by user
        user=request.form['name']
        return redirect(url_for('welcome', name=user)) 
    else:
        user=request.args.get('name')
        return redirect(url_for('welcome', name=user))
    


if __name__ == "__main__":
    app.run(debug=True)