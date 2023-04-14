"""This code is about a different calculator that do some mathematical calculations like plus ,
minus,divide and so on"""
print(__doc__)
page = "1\t2\t3 |\t+\t-\t*\n4\t5\t6 |\t/\t//\t^\n7\t8\t9 |\t_\t%\t_\nce\t0\t. |"
print(page)
number_1 = float(input("Enter your number:"))
result = number_1
while True:
    operand = input("Enter operand:")
    if operand == "=":
        print("Finished!!")
        break
    number_2 = float(input("Enter number again:"))
    if operand == "+":
        result = result + number_2
        print(result)
    elif operand == "*":
        result = result * number_2
        print(result)
    elif operand == "/":
        result = result / number_2
        print(result)
    elif operand == "//":
        result = result // number_2
    elif operand == "%":
        result = result % number_2
        print(result)
    elif operand == "^":
        result = pow(result, number_2)
        print(result)
    elif operand.lower() == "ce":
        result = 0
    else:
        print("Error!!")
print("Have a good night:)")
