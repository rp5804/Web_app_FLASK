from flask import Flask, redirect, url_for, request, render_template
import databse

app = Flask('__name__')


@app.route('/login', methods=['GET', 'POST'])
def login():

    user_id = request.form['nm']
    password = request.form['pass']
    return is_auth(databse.authenticate(user_id, password), user_id)


def is_auth(auth, user_id):
    if auth == 2:
        return render_template('new_user.html')
    if auth == 1:
        return hello_name(user_id)
    else:
        return ('Authorization Failed')


@app.route('/hello_name', methods=['POST'])
def hello_name(user_id):
    return render_template('index.html', name=user_id)


@app.route('/logout', methods=['POST'])
def logout():
    if request.method == 'POST':
        return render_template('login.html')


@app.route('/new_user', methods=['POST', 'GET'])
def new_user():
    if request.method == 'GET':
        return render_template('new_user.html')
    if request.method == 'POST':
        user_id = request.form['username']
        passwd = request.form['pswrd']
        if user_id or passwd == '' or '':
            return render_template('new_user.html')
        else:
            databse.insert_user(user_id, passwd)
            return render_template('login.html')



if __name__ == '__main__':
    app.run(debug=True)
