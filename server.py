from flask import Flask,redirect,request, render_template,url_for
from mainscript import transfer,showdata
app = Flask(__name__)

@app.route('/')
def index():
    times = ['10 Minutes', '15 Minutes', '30 Minutes', '60 Minutes']
    return render_template('home.html',times=times)

@app.route('/submit', methods=['POST'])
def submit():
    if len(request.form.get('bakra'))>1:

        return render_template('output2.html',output=transfer(request.form.get('bakra'),request.form.get('ttt')))
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
