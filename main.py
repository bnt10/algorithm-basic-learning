from flask import Flask

app = Flask('app')
#from chapter03 import practice03
from chapter04 import graph_dfs


@app.route('/')
def debugAlgorithm():

    #practice03.selectionSort([1, 5, 3, 2])
    # stack.checkPalindrome('Madam, I am Adam.')
    return 'debugAlgorithm'


app.run(host='0.0.0.0', port=8080)
