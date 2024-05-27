from flask import Flask, render_template, request, redirect, url_for, abort, flash, make_response

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/welcome/', methods=['POST'])
def welcome():
    name = request.form.get('name')
    email = request.form.get('email')
    response = make_response(redirect('/greet'))
    response.set_cookie('user_name', name)
    response.set_cookie('user_email', email)
    return response


@app.route('/greet')
def greet():
    user_name = request.cookies.get('user_name')
    if user_name:
        return render_template('greet.html', name=user_name)
    return redirect('/')


@app.route('/logout/')
def logout():
    response = make_response(redirect('/'))
    response.delete_cookie('name')
    response.delete_cookie('email')
    return response


if __name__ == '__main__':
    app.run(debug=True)
