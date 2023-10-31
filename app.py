from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def calculator_page():
    return render_template('index.html')

@app.route('/math', methods= ['POST'])
def calculator_operation():
    ops = request.form['operation']
    first_number = int(request.form['num1'])
    second_number = int(request.form['num2'])

    if (ops == 'add'):
        result = first_number + second_number
        return f"Sum of {first_number} and {second_number} is {result}"

    if (ops == 'subtract'):
        result = first_number - second_number
        return f"Difference of {first_number} and {second_number} is {result}"
    
    if (ops == 'multiply'):
        result = first_number * second_number
        return f"Multiplication of {first_number} and {second_number} is {result}"       

    if (ops == 'divide'):
        if second_number == 0:
            return "Division by zero is not possible"
        else:
            result = first_number / second_number
            return f"Division of {first_number} and {second_number} is {result}"   

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5001)
