from flask import Flask,jsonify,Response
from app.services.services import function_a, calculate_sum, sub_numbers, diff_numbers

app = Flask(__name__)
app.debug = True 
app.config['SECRET_KEY'] = "everyone-can-see-this"

@app.route("/code-smell")
def code_smell():
    # print(A)
    A = 10
    return jsonify({
        "A": A
    })

 
@app.route("/code-smell/again")
def code_smell_again():   
    a = 10
    b = 20
    c = 30
    d = 40
    
    result = 0
    
    if  a >1:
        result= a+b+c+d
    elif b > 1:
        result= a+b+c+d
    elif c > "1":
        result= a+b+c+d
    else:
        result = a +b +c +d
        
    return jsonify({
        "reult": result
    })
@app.route("/code-smell/again/again")
def code_smell_again_again():  
    function_a()
    
    return "function is over"

@app.route("/security")
def security():
    response = Response()
    response.set_cookie('key', 'value') # Sensitive
    return response
    
    
@app.route("/sum")
def calculate():
    out = calculate_sum(5,6)
    return jsonify({
        "result": 11,
    })
    
@app.route("/dif")
def calculate_dif():
    outA = sub_numbers(5,6)
    outB = diff_numbers(5,6)
    return jsonify({
        "result": outA,
    })