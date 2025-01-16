welcome = """Welome! you can calculate your bmi to find out
that your weight is ok or no it need your weight, height
and your age(your age must be upper than 20 or 20)"""
print(welcome)
while True :
    try:
        weight = int(input("Enter your weight(kg):"))
        height = int(input("Enter your height(cm):")) / 100
        age = int(input("Enter your age(20..):"))
        bmi = weight / (height ** 2)
    except:
        print("Error has occured!")
    if age < 20 :
        print("Error! your age must be upper than 20")
        break
    else:
        print(f"your bmi number is :{bmi}")    
        if bmi < 18.5 :
            print("your weight is too low!")
            print(f"you should gain at least {round(18.5 * (height ** 2)- weight, 2)}kilos")
        elif 18.5 <= bmi < 25 :
            print("your have a good weight for your height")
        elif 25 <= bmi < 30 :
            print("you are slightly overweight!")
            print(f"you need to lose {round(weight - (24.9 * (height ** 2)), 2)} kilos")
        else :
            print("you are overweighted!")
            print(f"you need to lose {round(weight - (24.9 * (height ** 2)), 2)} kilos \
so that your health is not compromised!you must talk to a doctor \
or a nutritional consultant")
        want = input("Do you want to find another bmi(yes/no):")
        if want.lower() == "yes":
            pass
        elif want.lower() == "no":
            print("Thanks for using us!")
            break
        else:
            print("invalid Error")
            break
