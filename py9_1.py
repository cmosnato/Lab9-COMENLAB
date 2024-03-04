from flask import Flask
app = Flask(__name__)
 
@app.route('/<opt>/<float:a>/<float:b>')
def calculate(opt, a, b):
    result = None
    if opt == 'add':
        result = a + b
    elif opt == 'sub':
        result = a - b
    elif opt == 'mul':
        result = a * b
    elif opt == 'div':
        if b != 0:
            result = a / b
        else:
            return 'Error: division by zero'
    else:
        return 'Error: invalid operator'
 
    return f'Result: {result}'
 
if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')
 