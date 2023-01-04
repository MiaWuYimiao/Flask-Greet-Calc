# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div
import operations

app = Flask(__name__)

@app.route("/add")
def do_add():
    """Add a and b and return result as the body"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    res = add(a, b)

    return str(res)

@app.route("/sub")
def do_sub():
    """Subtract a and b and return result as the body"""

    a = int(request.args["a"])
    b = int(request.args["b"])
    res = sub(a, b)

    return str(res)

@app.route("/mult")
def do_mult():
    """Multiply a and b and return result as the body"""

    a = int(request.args["a"])
    b = int(request.args["b"])
    res = mult(a, b)

    return str(res)

@app.route("/div")
def do_div():
    """Divide a and b and return result as the body"""

    a = int(request.args["a"])
    b = int(request.args["b"])
    res = div(a, b)

    return str(res)

# opr = {
#     "add" : add,
#     "sub" : sub,
#     "mult" : mult,
#     "div" : div
# }

@app.route("/math/<operation>")
def do_math(operation):
    """Add a and b and return result as the body"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    print(operation)
    print(f"a = {a} b = {b}")
    opr = getattr(operations, operation)

    return str(opr(a,b))