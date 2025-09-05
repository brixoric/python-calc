import os
os.system('cls')

math_numb = int(input("What math operation do you want to do? (1 = multiply, 2 = subtract, 3 = add, 4 = divide): "))
if math_numb == 1:
    os.system('python3 multiply.py')
if math_numb == 2:
    os.system('python3 subtract.py')
if math_numb == 3:
    os.system('python3 add.py')
if math_numb == 4:
    os.system('python3 divide.py')