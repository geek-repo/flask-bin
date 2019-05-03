from flask import Flask,redirect,request, render_template,url_for
from mainscript import transfer,showdata
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def submit():
    if len(request.form['text'])>1:

        return render_template('output2.html',output=transfer(request.form['text']))
    else:
        return redirect('/')

@app.route('/<name>')
def my_view_func(name):
    if name=="favicon.ico":
        return redirect(url_for('static', filename='favicon.ico'), code=302)
    else:

        return render_template('output.html',output=showdata(name))



if __name__ == '__main__':
    app.run(host="0.0.0.0")
