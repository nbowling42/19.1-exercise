from flask import Flask, request
import operations

app = Flask(__name__)

@app.route('/add')
def addition():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"{operations.add(a,b)}"

@app.route('/sub')
def subtract():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"{operations.sub(a,b)}"

@app.route('/mult')
def multiply():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"{operations.mult(a,b)}"

@app.route('/div')
def divide():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"{operations.div(a,b)}"

oper = {
    'add': operations.add,
    'sub': operations.sub,
    'mult': operations.mult,
    'div': operations.div
}

@app.route('/math/<operation>')
def math(operation):
    a = int(request.args['a'])
    b = int(request.args['b'])
    func = oper[operation]
    res = func(a,b)

    return str(res)
    
