from flask import Flask, request, render_template
from mainscript import transfer,showdata
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def submit():
    return render_template('output2.html',output=transfer(request.form['text']))

@app.route('/<name>')
def my_view_func(name):
    return render_template('output.html',output=showdata(name))



if __name__ == '__main__':
    app.run(host="0.0.0.0")
