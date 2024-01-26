# binary search
#  s          mid          e
# [1, 2, 3, 4, 5, 6, 7, 8, 9] , item = 6
#                 s        e
# item > mid >>> [6, 7, 8, 9]
li = input("Enter a list separated with comma:").split(",")
li.sort()
start = 0
end = len(li) - 1
mid = (end + start) // 2
item = input("Enter item:")
while start <= end:
    if li[mid] == item:
        print(f"This item is in element:{li.index(item)+1} of the list")
        break
    elif li[mid] < item:
            start = mid + 1
    elif li[mid] > item:
            end = mid - 1
    mid = (start + end) // 2
else:
    print("Not found")


