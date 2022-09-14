from flask import Flask
from chapter02 import ch02_recursion
app = Flask('app')

@app.route('/')
def home():
    #ch02_recursion.recursion(3)
    return 'hello world'


@app.route('/recursion')
def recursion():
    ch02_recursion.recursion(3)
    return 'recursion'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
