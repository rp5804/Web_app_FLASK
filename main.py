from flask import Flask, redirect, url_for, request, render_template

app = Flask('__name__')

# users = []
# passwords = []


@app.route('/login', methods=['POST'])
def login():
    user = request.form['nm']
    password = request.form['pass']
    return auth(password, user)


def auth(password, user):
    if password == 'patil':
        return hello_name(user)
    # for a in users:
    #     if user == a:
    #         if password == passwords[a]:
    #             return hello_name(user)
    #         else:
    #             return ('User not found!')
    #
    else:
        return ('Authorization Failed')


def hello_name(user):
    return render_template('index.html', name=user)


@app.route('/new_user', methods=['POST', 'GET'])
def new_user():
    if request.method == 'GET':
        return render_template('new_user.html')


# def get_new_user():
#     if request.method == 'POST':
#         new_usr = request.form['username']
#         new_pass = request.form['pswrd']
#         users.append(new_usr), passwords.append(new_pass)
#         return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
