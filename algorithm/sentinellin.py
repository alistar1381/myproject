# sentinel linear search
li = input("Enter the list separated with comma:").split(",")
item = input("Enter the item you want to find:")
last, li[-1] = li[-1], item
i = 0
while li[i] != item: 
    i += 1
li[-1] = last
if (i < (len(li) - 1)) or (li[i] == item):
    print(f"The item is in element:{i+1} of the list")
else:
    print("Not found")
