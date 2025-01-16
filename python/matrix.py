"""Well , In this code we will do somthing with matrix like calculating determinant , multiply two matrix , division two matrix\
ading matrixs together and low-off two matrix with numpy"""
import numpy as np


# define matrix
def mat(rows, cols, x):
    for i in range(rows):
        row = input(f"row elements: {i+1}\nseperate with space:")
        if len(row.split()) == cols:
            row = list(map(int, row.split()))
        else:
            print("your value is too low!!")
            break
        x.append(row)


#calculating determinant
def determinal(x):
    try:
        matrix = np.array(x)
        detetminant = np.linalg.det(matrix)
        print(f"The determinant of this matrix: {round(detetminant)}")
    except np.linalg.LinAlgError:
        print("Last 2 dimensions of the array must be square")


# multiplication a matrix to a number put it to A
def mul_scaler(a, scaler):
    matrix = np.array(a)
    result = matrix * scaler
    return result


# multiplication two matrix and put it to A
def multiplication(a, b):
    try:
        m1 = np.array(a)
        m2 = np.array(b)
        result = np.dot(m1, m2)
        return result
    except ValueError:
        print("The number of columns in the first matrix must be equal to the number of rows in the second matrix!!Try again")


# adding two matrix and put it to A
def add(a, b):
    try:
        m1 = np.array(a)
        m2 = np.array(b)
        result = np.add(m1, m2)
        return result
    except ValueError:
        print("They need to have the same dimensions")
        

# dividing two matrix and put it to A
def divide(a, b):
    try:
        m1 = np.array(a)
        m2 = np.array(b)
        result = np.round(np.divide(m1, m2), decimals= 2)
        return result
    except ValueError:
        print("The number of columns in the first matrix must be equal to the number of rows in the second matrix!!Try again")
    except ZeroDivisionError:
        print("Division by zero")


# subtraction of two matrix
def minus(a, b):
    try:
        m1 = np.array(a)
        m2 = np.array(b)
        result = np.subtract(m1, m2)
        return result
    except ValueError:
        print("They need to have the same dimensions")


print("*" * 40)
print(menu := "1)receive matrix A\n2)receive matrix B\n3)simultaneous transfer between A&B\n4)Transfer from A to B\n5)Transfer from B to A\
\n5)A=A*B\n6)A=A/b\n7)A=A+B\n8)A=A-B\n9)A=a*A\n10)Determinal A\n11)Determinal B\n12)Print A\n13)Print B\n14)exit")
print("*" * 40)
while True:
    choice = int(input("Choose a number:"))
    if choice == 1:
        rows = int(input("Enter rows:"))
        cols = int(input("Enter columns:"))
        a = []
        if rows * cols <= 100:
            mat(rows, cols, a)
        else:
            print("your elements must be lower than 100")
    elif choice == 2:
        rows = int(input("Enter rows:"))
        cols = int(input("Enter columns:"))
        b = []
        if rows * cols <= 100:
            mat(rows, cols, b)
        else:
            print("your elements must be lower than 100")
    elif choice == 3:
        a, b = b, a
        print("Tranfer was successful!!")
    elif choice == 4:
        a = b.copy()
        b.clear()
        print("Tranfer was successful!!")
    elif choice == 5:
        b = a.copy()
        a.clear()
        print("Tranfer was successful!!")
    elif choice == 6:
        a = multiplication(a, b)
        for sublist in a:
            print(sublist)
    elif choice == 7:
        a = divide(a, b)
        for sublist in a:
            print(sublist)
    elif choice == 8:
        a = add(a, b)
        for sublist in a:
            print(sublist)
    elif choice == 9:
        a = minus(a, b)
        for sublist in a:
            print(sublist)
    elif choice == 10:
        scaler = int(input("Enter the number you want to multiply it to matrix A:"))
        a = mul_scaler(a, scaler)
        for sublist in a:
            print(sublist)
    elif choice == 11:
        determinal(a)
    elif choice == 12:
        determinal(b)
    elif choice == 13:
        print("*" * 40)
        for sublist in a:
            print(sublist)
        print("*" * 40)
    elif choice == 14:
        print("*" * 40)
        for sublist in b:
            print(sublist)
        print("*" * 40)
    elif choice == 15:
        print("Good luck")
        break
    else:
        print("Error!!Try again...")
