"""In this code ,we want to perform a series of operations with students. We want to add them to a table\
,remove them from it , or even edit their information and display them"""
import pandas

# Create class student
class Student():
    """This class has a series of methods and attributes . The class attributes include a list of student ID and the last\
student number, which is incremented each time a new student is added to table. The behaviors of this class incluide\
showing,adding,deleting and editing the details of the student"""
    list_id = []
    last_number = 40017299999999
    # create the std ID and add it to list_id 
    def __init__(self):
        Student.last_number += 1
        self.Student_number = Student.last_number
        Student.list_id.append(self.Student_number)

    #show students
    def show(cls):
        cls.df = pandas.read_csv("student.csv", index_col= 0)
        print(cls.df)


    # adding new student
    @classmethod
    def add(cls, li_first_name, li_last_name, li_age, li_phone_number):
        if len(li_first_name) == len(li_last_name) == len(li_age):
            cls.df = pandas.read_csv("student.csv", index_col= 0)
            data = {"name": li_first_name, "surname": li_last_name, "age": li_age, "phone":li_phone_number, "ID": Student.list_id}
            cls.df = pandas.DataFrame(data, index= range(len(Student.list_id)))
            cls.df.to_csv("student.csv")
            print(cls.df)
        else:
            raise ValueError("length of lists does not match")
    
    # delete a student
    @classmethod
    def delete(cls, del_first_name, del_last_name, del_phone_number, del_age, del_stu_id):
        cls.df = pandas.read_csv("student.csv", index_col= 0)
        li_first_name.pop(li_first_name.index(del_first_name))
        li_last_name.pop(li_last_name.index(del_last_name))
        li_phone_number.pop(li_phone_number.index(del_phone_number))
        li_age.pop(li_age.index(del_age))
        cls.df.drop(Student.list_id.index(del_stu_id), inplace= True)
        Student.list_id.pop(Student.list_id.index(del_stu_id))
        cls.df.reset_index(drop= True, inplace= True)
        cls.df.to_csv("student.csv")
        print(cls.df)
    
    # edit details of a student
    @classmethod
    def edit(cls, pre, new):
        cls.df = pandas.read_csv("student.csv", index_col= 0)
        cls.df.replace(to_replace= pre, value= new, inplace= True)
        cls.df.to_csv("student.csv")
        print(cls.df)

# list of first name, last name, telephone number and age of students
li_phone_number = []
li_first_name = []
li_last_name = []
li_age = []
while True:
    # menu
    print("*" * 40)
    print(menu := "1)show\n2)Add st\n3)Delete st\n4)Edit st\n5)Exit")
    print("*" * 40)
    start = int(input("What do you want to do(Enter a number):"))
    if start == 1:
        try:
            obj.show()
        except:
            print("No data to display")
    elif start == 2:
        while True:
            try:
                first_name = input("Enter first name :")
                last_name = input("Enter last name :")
                phone_number = input("Enter phone number:")
                age = int(input("Enter age :"))
                li_first_name.append(first_name.capitalize())
                li_last_name.append(last_name.capitalize())
                li_phone_number.append(phone_number)
                if  0 < len(first_name) <= 15 and not first_name.isnumeric():
                    pass
                else: 
                    raise ValueError()
                if  0 < len(last_name) <= 20 and not last_name.isnumeric():
                    pass
                else:
                    raise ValueError
                if len(phone_number) == 11 and phone_number.isnumeric() and phone_number.startswith("09"):
                    pass
                else:
                    raise ValueError()
                if age >= 17: 
                    li_age.append(age)
                else:
                    raise ValueError()
                obj = Student()
            except:
                li_first_name.pop(li_first_name.index(first_name.capitalize()))
                li_last_name.pop(li_last_name.index(last_name.capitalize()))
                li_phone_number.pop(li_phone_number.index(phone_number))
                print("Invalid value")
            try:
                con = input("Anything else(y/n):")
                if con.lower() == "n":
                    obj.add(li_first_name,li_last_name, li_age, li_phone_number)
                    break
                elif con.lower() == "y":
                    obj.add(li_first_name,li_last_name, li_age, li_phone_number)
                    pass
                else:
                    print("Invalid Value!!")
            except NameError:
                print("No data to print. Try again")


    elif start == 3:
        j = 0
        while j <= len(li_first_name):
            try:
                deleting = input("Do you want me to delete a name(y/n):")
                if deleting.lower() == "y":
                    del_first_name = input("Enter first name :")
                    del_last_name = input("Enter last name :")
                    del_phone_number = input("Enter phone number:")
                    del_age = int(input("Enter age :"))
                    del_stu_id = int(input("Enter student ID:"))
                    obj.delete(del_first_name.capitalize(), del_last_name.capitalize(), del_phone_number, del_age, del_stu_id)
                    j += 1
                elif deleting.lower() == "n":
                    break
                else:
                    print("Try again!!")
            except:
                print("Try again...")
        else:
            print("No data to print:((")

            
    elif start == 4 :
        try:
            stu_id = int(input("Enter Student_id:"))
            while True:
                print(edit_menu := "1)Edit first name\n2)Edit last name\n3)Edit phone num\n4)Edit age\n5)Exit")
                editing = int(input("Choose your option:"))
                if editing == 1:
                    try:
                        pre_first_name = input("Enter previous first name:")
                        new_first_name = input("Enter new first name:")
                        li_first_name[li_first_name.index(pre_first_name.capitalize())] = new_first_name.capitalize()
                        obj.edit(pre_first_name.capitalize(), new_first_name.capitalize())
                    except:
                        print("Error!!!Try again ...")
                elif editing == 2:
                    try:
                        pre_last_name = input("Enter previous last name:")
                        new_last_name = input("Enter new last name:")
                        li_last_name[li_last_name.index(pre_last_name.capitalize())] = new_last_name.capitalize()
                        obj.edit(pre_last_name.capitalize(), new_last_name.capitalize())
                    except:
                        print("Error!!!Try again ...")
                elif editing == 3:
                    try:
                        pre_phone = input("Enter previous phone number:")
                        new_phone = input("Enter new phone number:")
                        li_phone_number[li_phone_number.index(pre_phone)] = new_phone
                        obj.edit(pre_phone, new_phone)
                    except:
                        print("Error!!!Try again ...")
                elif editing == 4 :
                    try:
                        pre_age= int(input("Enter previous age:"))
                        new_age= int(input("Enter new age:"))
                        li_age[li_age.index(pre_age)] = new_age
                        obj.edit(pre_age, new_age)
                    except:
                        print("Error!!!Try again ...")
                elif editing == 5:
                    print("That's ok ...")
                    break
                else:
                    print("Invalid value!!Try again")
        except:
            print("Enter a valid value:(((")
                   

    elif start == 5:
        print("Best wishes for you :))))") 
        break
    else:
        print("Invalid value. Try again ...")




