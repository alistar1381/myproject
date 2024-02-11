from math import sqrt


li = [int(i) for i in input("Enter the list separated by comma:").split(",")]
li.sort()
item = int(input("Enter the item:"))
jump = int(sqrt(len(li)))
con = False
i = 0
while i <= (len(li)) - 1:  
    if li[i] > item:
        pre = i - jump
        for j in range(pre, i + 1):
            if li[j] == item:
                print(f"The item is in element:{j + 1} of the list")
                con = True
                break
    if con:
        break
    i += jump 
else:
    print("Not found")
