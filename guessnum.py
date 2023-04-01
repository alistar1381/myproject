"""Welcome to the game. you should guest the number dependent on the modes of this game:1)easy2)medium3)hard"""
from random import randint


def easy_mode():
    save_num = randint(1, 10)
    for i in range(5):
        guess = int(input("Guess the number(1,10):"))
        if guess == save_num:
            print(f"Congratulations!!, You can guess that number:{save_num}")
            break
        else:
            print("Not correct!")
    else:
        print(f"Sorry for you :| you can not guess the number. the number:{save_num}")


def med_mode():
    save_num = randint(1, 100)
    for i in range(10):
        guess = int(input("Guess the number(1,100):"))
        if guess == save_num:
            print("*" * 40)
            print(f"Congratulations!!You can guess that number:{save_num}")
            break
        elif guess > save_num:
            print("No!!That number is lower")
            print("*" * 40)
        elif guess < save_num:
            print("No!! That number is higher")
            print("*" * 40)
    else:
        print(f"Sorry for you :| you could not guess the number. the number:{save_num}")


def hard_mod():
    save_num = randint(1, 1000)
    for i in range(15):
        guess = int(input("Guess the number(1, 1000):"))
        if guess == save_num:
            print("*" * 40)
            print(f"Congratulations!!You can guess that number:{save_num}")
            break
        elif guess > save_num:
            print("No!!That number is lower")
            print("*" * 40)
        elif guess < save_num:
            print("No!! That number is higher")
            print("*" * 40)
    else:
        print(f"Sorry for you :| you could not guess the number. the number:{save_num}")


def help_game():
    print(__doc__)


li = """1)Easy
2)Medium
3)Hard
4)Help
5)Exit
"""
print(li)
while True:
    begin = int(input("Choose your option:"))
    if begin == 1:
        easy_mode()
    elif begin == 2:
        med_mode()
    elif begin == 3:
        hard_mod()
    elif begin == 4:
        help_game()
    elif begin == 5:
        print("Have a nice time!!")
    else:
        print("Error!!!")
    want = input("Do you want to play(y/n):")
    if want.lower() == "n":
        print("have a nice time:)")
        break
    elif want.lower() == "y":
        pass
    else:
        print("Error!")
        break
