from datetime import datetime
import pandas
"""This code is about management of a simple shop that you can put shop supples\
in your inventory and sell them when you sell a product .the sum_cost of selling\
was shown to you if you want to see the inventory you should choose number 3\
and finally in financial balance sector you can compare the buy with your\
profit from selling products and both will be shown to you
note: you must first choose buy to put some supplies in your shop then go to \
other options and you can go out from this program with exit option :)"""
menu = """1)buy
2)sell
3)inventory
4)financial balance
5)exit\n"""
print(menu)
products = {}
li = []
value_sell = 0
cost_buy = 0
current_date = datetime.now()
data_format = "%d/%m/%y"
print(current_date.strftime(data_format))
while True:
    option = int(input("Choose your option:"))
    if option == 1:
        while True:
            product = input("Enter the product clearly with its brand:")
            cost = int(input("Enter the cost(Toman):"))
            count = int(input("Enter the count of your product:"))
            if product in products:
                products[product][1] += count
                if cost < products[product][0]:
                    pass
                else:
                    products[product][0] = cost
            else:
                products[product] = [cost, count]
            cost_buy += count * cost
            con = input("anything else(y/n)? ")
            if con.lower() == "n" :
                break
            elif con.lower() == "y":
                pass
            else:
                print("Value Error!!")
                break
        print("*" * 20)
        df = pandas.DataFrame(products, index= ["cost","count"])
        print(df)
    elif option == 2:
        while True:
            sell_product = input("which product do you want to sell:")
            sell_count = int(input("Enter the number of products that you sent:"))
            value_sell += products[sell_product][0] * sell_count
            print("\nThe sum cost of the product:", value_sell)
            products[sell_product][1] -= sell_count
            con = input("anything else(y/n)? ")
            if con.lower() == "n" :
                break
            elif con.lower() == "y":
                pass
            else:
                print("Value Error!!")
                break
        print("*" * 20)
        df = pandas.DataFrame(products, index= ["cost","count"])
        print(df)
    elif option == 3:
        print("*" * 20)
        df = pandas.DataFrame(products, index= ["cost","count"])
        print(df)
        print("*" * 20)
    elif option == 4:
        level = value_sell - cost_buy
        print(f"in this date :{current_date.strftime(data_format)}")
        print(f"you buy : {cost_buy}\nyou sell : {value_sell}\nyour level :\
{level}")
        if level < 0 :
            print("your financial balance is negative")
        elif level > 0 :
            print("your financial balance is positive")
        else:
            print("toy do not have any profit")
    elif option == 5:
        print("Have a good life :)))))")
        break
    else:
        print("Invalid value!!!")