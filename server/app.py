from flask import Flask, abort

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:text>')
def print_string(text):
    print(text)
    return text

@app.route('/count/<int:number>')
def count(number):
    if number < 0:
        abort(400, "Number must be non-negative")
    numbers = range(number + 1)
    numbers_text = '\n'.join(str(num) for num in numbers)
    return numbers_text

@app.route('/math/<float:num1>/<operation>/<float:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return 'Error: Division by zero', 400
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Error: Invalid operation', 400

    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
