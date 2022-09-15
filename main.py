from flask import Flask
from chapter02 import ch02_recursion, practice_01

app = Flask('app')


@app.route('/')
def home():
    #ch02_recursion.recursion(3)
    return 'hello world'


@app.route('/recursion')
def recursion():
    ch02_recursion.recursion(3)
    return 'recursion'


@app.route('/sum-by-recursion')
def practice():
    print(practice_01.sumByRecursion(3))
    return 'practive01'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
