# exponential search
def expobin(li, item):
    if li[0] == item:
        return "The item is in element:%i in the list"%(1)
    i = 1
    while i < len(li) and li[i] <= item: 
        i *= 2
    start = i // 2
    end = min(i, len(li) - 1)
    mid = (end + start) // 2
    while start <= end:
        if li[mid] == item:
            return "This item is in element:{} of the list".format(mid + 1)
        elif li[mid] < item:
            start = mid + 1
        elif li[mid] > item:
            end = mid - 1
        mid = (start + end) // 2
    else:
        return "Not found"
        

li = [int(i) for i in input("Enter the list separated with comma:").split(",")]
li.sort()
item = int(input("Enter the item:"))
print(expobin(li, item))
