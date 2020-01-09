def sortTheColor(arr):
    currentpos = firstpos = 0
    lastpos = len(arr) -1
    while currentpos <= lastpos:
        if arr[currentpos] == 0:
            arr[currentpos], arr[firstpos] = arr[firstpos], arr[currentpos]
            currentpos += 1
            firstpos += 1
        elif arr[currentpos] == 2:
            arr[currentpos], arr[lastpos] = arr[lastpos], arr[currentpos]
            lastpos -= 1
        else:
            currentpos += 1
    return arr


arr = [2, 0, 2, 1, 1, 0]
print(sortTheColor(arr))