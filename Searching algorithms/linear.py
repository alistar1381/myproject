# linear search
li = input("Enter the list separated with comma:").split(",")
item = input("Enter the item:")
for i in range(0, len(li) - 1, 1):# for i in li:
    if li[i] == item:
        print(f"The item is in element:{i+1} of the list")
        break
else:
    print("Not found")