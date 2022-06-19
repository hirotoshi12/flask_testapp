from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def set_number():
    return "<h1>Hello World!</h1>"

# @app.route("/<number>")
# def set_numbers(number):
#     return render_template('number.html', number=number)

@app.route("/<age>")
def set_ages(age):
    # print(type(age))
    # return f'<h1>{age}</h1>'
    return render_template('number.html', age=age)