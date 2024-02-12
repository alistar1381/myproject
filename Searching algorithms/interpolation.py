li = [int(i) for i in input("Enter the list separated by comma:").split(",")]
li.sort()
item = int(input("Enter the item:"))
low = 0
high = len(li) - 1
while low <= high and li[low] <= item <= li[high]:
    po = int(low + ((item - li[low]) * (high - low)/(li[high] - li[low])))
    if li[po] == item:
        print(f"The item is in element:{po + 1} of the list")
        break
    elif li[po] > item:
        high = po - 1
    else:
        low = po + 1
else:
    print("Not found")
