# Ubiquitous binary search
li = [int(i) for i in input("Enter the list separated by comma:").split(",")]
li.sort()
item = int(input("Enter your number:"))
start = 0
end = len(li) - 1
mid = start + (end - start) // 2
while end - start > 1:
    if li[mid] <= item:
        start = mid
    else:
        end = mid
    mid = start + (end - start) // 2

if li[end] == item or li[start] == item:
    print(f"The item is in element:{li.index(item) + 1} of the list")
else:
    print("Not Found")
