# linear search
li = [int(i) for i in input("Enter a list separated with comma:").split(",")]
item = int(input("Enter item:"))
for i in range(0, len(li) - 1, 1):# for i in li:
    if li[i] == item:
        print(f"The item is in element:{i+1} of the list")
        break
else:
    print("Not found")