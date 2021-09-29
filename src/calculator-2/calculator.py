"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, add_cubes, add_mult)


# Replace this with your code
while True:
    user_input = input('Enter equation: ')
    token = user_input.split(' ')

    if token == 'q':
        print('You quit the game')
        break
    
    num1 = token[1]
    if len(token) < 3:
        num2 = "0"
    else:
        num2 = token[2]
    if len(token) > 3:
        num3 = token[3]

    result = None

    if token[0] == "+":
        result = add(float(num1), float(num2))

    elif token[0] == "-":
        result = subtract(float(num1), float(num2))
    
    elif token[0] == "*":
        result = multiply(float(num1), float(num2))
    
    elif token[0] == "/":
        result = divide(float(num1), float(num2))

    elif token[0] == "square":
        result = square(float(num1))
   
    elif token[0] == "cube":
       result = cube(float(num1))

    elif token[0] == "pow":
        result = power(float(num1), float(num2))
    
    elif token[0] == "mod":
        result = mod(float(num1), float(num2))
    
    elif token[0] == "x+":
        result = add_mult(float(num1), float(num2), float(num3))
    
    elif token[0] == "cubes+":
        result = add_cubes(float(num1),float(num2))
    
    else:
        result = 'Please enter something else'
        
    print(result)