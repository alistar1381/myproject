def binary_search(begin, end, item, li):
    mid = (begin + end) // 2
    if begin <= end:
        if li[mid] == item:
            print(f"The item is in element:{mid + 1} of the list")
        elif li[mid] > item:
            binary_search(begin, mid -1, item, li)
        elif li[mid] < item:
            binary_search(mid + 1, end, item, li)
    else:
        print("Not Found")
    

li = input("Enter the list separated by comma:").split(",")
li.sort()
begin = 0
end = len(li) - 1
item = input("Enter item:")
binary_search(begin, end, item, li)
