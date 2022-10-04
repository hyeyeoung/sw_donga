from flask import Flask
from flask import Flask, render_template, request, session, redirect, url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('test.html')

if __name__ == '__main__':
    app.debug = True
    app.run(debug=True)