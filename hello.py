from flask import Flask
from flask import render_template

app = Flask(__name__)

# items = [
#     'アイテム1',
#     'アイテム2',
#     'アイテム3',
#     'アイテム4',
#     'アイテム5',
#     'アイテム6',
# ]

di = [
    {"name1": 'Miura', "name2": 'Junya'},
    {"name1": 'Tanaka', "name2": 'Taro'},
]

@app.route("/")
def hello_world():
    # return "Hello,World"
    # return render_template('hello.html')
    # return render_template('hello.html', items=items)
    return render_template('hello.html', di=di)

# @app.route("/Miura")
# def hello_miura():
#     return "Hello,Miura"

# @app.route("/Tanaka")
# def hello_tanaka():
#     return "Hello,Tanaka"

@app.route("/<name>")
def hello_user(name): # Pythonファイル内で扱う変数
    return render_template('hello.html', name=name) # HTMLテンプレートファイル内で扱う変数

    