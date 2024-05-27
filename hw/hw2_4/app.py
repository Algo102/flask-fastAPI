from flask import Flask, render_template, request, redirect, url_for, abort, flash, make_response, session

app = Flask(__name__)
app.secret_key = b'e236e8d5008cf89ac35084b84f7389a248c7062b4c62c50bf2b6aa5eb6474b26'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form.get('username', 'email')
        return redirect(url_for('index'))
    return render_template('login.html')


@app.route('/logout/')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
