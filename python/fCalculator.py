import tkinter
from tkinter import messagebox
from math import factorial, log, exp, sin, cos, tan, radians
import sympy as sp

# کار با صفحه کلید
def handle_key(event):
    key = event.keysym
    if key in ['plus', 'minus', 'asterisk', 'slash']:
        if key == "plus":
            btnClick('+')
        elif key == "minus":
            btnClick('-')
        elif key == "asterisk":
            btnClick('*')
        elif key == "slash":
            btnClick('/')
    elif key.isdigit():
        btnClick(key)
    elif key == 'Return':
        btnEqualsInput()
    elif key == 'percent':
        btnClick('%')
    elif key == 'asciicircum':
        btnClick('**')
    elif key == 'exclam':
        btnFactorial()
    elif key == 'r':
        btnRound()
    elif key == 'l':
        btnLog()
    elif key == 'e':
        btnExponential()
    elif key == 's':
        btnSin()
    elif key == 'o':
            btnCot()
    elif key == 'c':
            btnCos()
    elif key == 't':
        btnTan()
    elif key == "BackSpace":
        btnBackSpace()
        
#دکمه صفحه کلید 
def btnBackSpace():
    global Display
    current_expression = Display
    if current_expression:
        new_expression = current_expression[:-1]
        Display = new_expression


#ایا عدد اول است یا نه
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num//2 + 1):
        if num % i == 0:
            return False
    return True


# تجزیه عدد در صورت اول بودن
# 12 = 2^2 * 3
def btnEqualsIn():
    global Display
    if is_prime(int(Display)):
        messagebox.showinfo("It is a prime number")
    else:
        factors = sp.factorint(int(Display))
        factor_str = "*".join([f"{k}^{v}" for k, v in factors.items()])
        messagebox.showinfo(factor_str)



# عدد به تابع -->is_prime
def btnCheckPrime():
    global Display
    if is_prime(int(Display)):
        messagebox.showinfo("Result", f"{Display} is a prime number")
        print("prime")
    else:
        messagebox.showinfo("Result", f"{Display} is a composite number")

# ذخیره عدد با دکمه --> m+
def btnMemStore():
    global Display
    value = Display
    memory.append(value)

# نمایش اعداد ذخیره شده در صفحه جدا   
def btnMemrecall():
    recall_window = tkinter.Toplevel(win)
    recall_window.title("Memory recall")
    for i, value in enumerate(memory):
        label = tkinter.Label(recall_window, text=f"Memory {i + 1}: {value}", font = ('arial', 16))
        label.pack()

# پاک کردن لیست حافظه --> MC
def btnMemclear():
    memory.clear()

def btnClick(A):
    global Display
    Display = Display + str(A)
    text_input.set(Display)

def btnDecimal():
    global Display
    if '.' not in Display:
        Display += '.'
        text_input.set(Display)

def btnClearDisplay():
    global Display
    Display = ""
    text_input.set("")

def btnEqualsInput(event = None):
    global Display
    result = str(eval(Display))
    text_input.set(result)
    Display = result

def btnFactorial(event = None):
    global Display
    result = factorial(int(Display))
    text_input.set(result)
    Display = result

def btnRound(event = None):
    global Display
    result = str(round(float(Display)))
    text_input.set(result)
    Display = result

def btnLog(event = None):
    global Display
    result = str(log(float(Display)))
    text_input.set(result)
    Display = result

def btnExponential(event = None):
    global Display
    result = str(exp(float(Display)))
    text_input.set(result)
    Display = result

def btnSin(event = None):
    global Display
    result = str(sin(radians(float(Display))))
    text_input.set(result)
    Display = result

def btnCos(event = None):
    global Display
    result = str(cos(radians(float(Display))))
    text_input.set(result)
    Display = result

def btnTan(event = None):
    global Display
    result = str(tan(radians(float(Display))))
    text_input.set(result)
    Display = result

def btnCot(event = None):
    global Display
    tan_value = tan(radians(float(Display)))
    result = str(1 / tan_value)
    text_input.set(result)
    Display = result


memory = []
# ایجاد صفحه
win = tkinter.Tk()
win.title("ماشين حساب")
Display = ""
#ایجاد دکمه ها
text_input = tkinter.StringVar()
txtDisplay = tkinter.Entry(win, font=('arial', 20, 'bold'), textvariable=text_input, bd=8, insertwidth=2, bg='powder blue', fg='#000000', justify='right').grid(columnspan=4)
btn7 = tkinter.Button(win, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='7', command=lambda: btnClick(7)).grid(row=1, column=0)
btn8 = tkinter.Button(win, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='8', command=lambda: btnClick(8)).grid(row=1, column=1)
btn9 = tkinter.Button(win, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='9', command=lambda: btnClick(9)).grid(row=1, column=2)
add = tkinter.Button(win, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='+', command=lambda: btnClick('+')).grid(row=1, column=3)
btn4 = tkinter.Button(win, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='4', command=lambda: btnClick(4)).grid(row=2, column=0)
btn5 = tkinter.Button(win, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='5', command=lambda: btnClick(5)).grid(row=2, column=1)
btn6 = tkinter.Button(win, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='6', command=lambda: btnClick(6)).grid(row=2, column=2)
subt = tkinter.Button(win, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='-', command=lambda: btnClick('-')).grid(row=2, column=3)
btn1 = tkinter.Button(win, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='1', command=lambda: btnClick(1)).grid(row=3, column=0)
btn2 = tkinter.Button(win, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='2', command=lambda: btnClick(2)).grid(row=3, column=1)
btn3 = tkinter.Button(win, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='3', command=lambda: btnClick(3)).grid(row=3, column=2)
mult = tkinter.Button(win, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='*', command=lambda: btnClick('*')).grid(row=3, column=3)
btn0 = tkinter.Button(win, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='0', command=lambda: btnClick(0)).grid(row=4, column=0)
btndecimal = tkinter.Button(win, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='.', command=btnDecimal).grid(row=4, column=1)
btnC = tkinter.Button(win, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='C', command=btnClearDisplay).grid(row=4, column=2)
btnE = tkinter.Button(win, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='=', command=btnEqualsInput).grid(row=4, column=3)
btnMod = tkinter.Button(win, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='%', command=lambda: btnClick('%')).grid(row=5, column=0)
btnExp = tkinter.Button(win, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='^', command=lambda: btnClick('**')).grid(row=5, column=1)
btnFact = tkinter.Button(win, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='!', command=btnFactorial).grid(row=5, column=2)
btnround = tkinter.Button(win, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='round', command=btnRound).grid(row=5, column=3)
btnlog = tkinter.Button(win, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='log', command=btnLog).grid(row=6, column=0)
btnExpFunc = tkinter.Button(win, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='exp', command=btnExponential).grid(row=6, column=1)
btnsin = tkinter.Button(win, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='sin', command=btnSin).grid(row=7, column=0)
btncos = tkinter.Button(win, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='cos', command=btnCos).grid(row=7, column=1)
btntan = tkinter.Button(win, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='tan', command=btnTan).grid(row=7, column=2)
btncot = tkinter.Button(win, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='cot', command=btnCot).grid(row=7, column=3)
btnmemstore = tkinter.Button(win, padx=16, pady=16, bd=8, fg="black",font=('arial', 20, 'bold'), text="M+", command=btnMemStore).grid(row=4, column=0)
btnmemrecall = tkinter.Button(win, padx=16, pady=16, bd=8, fg="black",font=('arial', 20, 'bold'), text="MR", command=btnMemrecall).grid(row=4, column=1)
btnmemreclear = tkinter.Button(win, padx=16, pady=16, bd=8, fg="black",font=('arial', 20, 'bold'), text="MC", command=btnMemclear).grid(row=4, column=3)
btncheckprime = tkinter.Button(win, padx=16, pady=16, bd=8, fg="black",font=('arial', 20, 'bold'), text="Check Prime", command=btnCheckPrime).grid(row=6, column=3)
btnequal = tkinter.Button(win, padx=16, pady=16, bd=8, fg="black",font=('arial', 20, 'bold'), text="Eq in", command=btnEqualsIn).grid(row=6, column=2)
#کار با صفحه کلید با فراخوانی تابع --> handle_key
win.bind('<Key>', handle_key)


win.mainloop()
