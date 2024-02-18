# fibonacci search
def fibo(x):
    f2 = 0
    f1 = 1
    f = f1 + f2
    while f <= x:
        f2 = f1
        f1 = f
        f = f1 + f2
    return f, f1, f2

li = [int(i) for i in input("Enter the list:").split(",")]
li.sort()
f, f1, f2 = fibo(len(li))
item = int(input("Enter the item:"))
offset = -1
while f > 1:
    index = min((offset + f2), len(li) - 1)
    if li[index] == item:
        print(f"The item is in element:{index + 1} of the list")
        break
    elif li[index] < item:
        f = f1
        f1 = f2
        f2 = f - f1
        offset = index
    else:
        f = f2
        f1 = f1 - f2
        f2 = f - f1
else:
    print("Not Found")

