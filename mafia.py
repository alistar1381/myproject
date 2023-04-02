from random import choice
number_role = {}
l_role = ["godfather", "dealer", "mafia", "doctor", "detective", "armored", "reporter", "citizen", "citizen", "sniper"]
for i in range(1, 11):
    role = choice(l_role)
    print(f"player {i} your role is : {role}")
    number_role[i] = role
    l_role.remove(role)
print(number_role)
