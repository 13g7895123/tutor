from flask import Flask, render_template
# from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html') # jinja2

# int、float
@app.route('/calculation/<float:num>')
def calculation(num):

    temp = 3.14159

    return f'''
        <label>加總結果: {num * temp}</label></br>

    '''

# @app.route('/form', method=['GET', 'POST'])

app.debug = True
app.run()
