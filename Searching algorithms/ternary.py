# Ternary search
li = [int(i) for i in input("Enter a list separated with comma:").split(",")]
li.sort()
item = int(input("Enter item:"))
left = 0
right = len(li) - 1
while left <= right:
    mid1 = left + (right - left) // 3 
    mid2 = right - (right - left) // 3
    if li[mid1] == item:
        print(f"The item is in element:{mid1} of the list")
        break
    elif li[mid2] == item:
        print(f"The item is in element:{mid2} of the list")
        break
    elif li[mid1] > item:
        right = mid1 - 1
    elif li[mid2] < item:
        left = mid2 + 1
    elif li[mid1] < item < li[mid2]:
        left = mid1 + 1
        right = mid2 -1
else:
    print("Not found")
