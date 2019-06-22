from collections import OrderedDict
def mergeSort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    mergeSort(left)
    mergeSort(right)
    i, j, k = [0]*3
    while len(left) > i and len(right) > j:
        if left[i][1] <= right[j][1]:
            arr[k] = left[i]
            k += 1
            i += 1
        else:
            arr[k] = right[j]
            k += 1
            j += 1
    while i < len(left):
        arr[k] = left[i]
        k += 1
        i += 1
    while j < len(right):
        arr[k] = right[j]
        k += 1
        j += 1
    return arr
def countingSort(arr, k = None):
    k = k if k != None else max(arr, key = lambda index_val: index_val[1])
    k = k[1]
    trackerArr = [0 for _ in range(k+1)]
    for index_val in arr:
        index, val = index_val
        trackerArr[val] += 1
    for index in range(1, len(trackerArr)):
        trackerArr[index] += trackerArr[index-1]
    copy = [num for num in arr]
    for index_num  in copy:
        index, num = index_num
        arr[trackerArr[num]-1] = index_num
        trackerArr[num] -= 1
def radixSort(arr):
    nums = {arr[index]: index for index in range(len(arr))}
    maxlen = max([len(str(num)) for num in arr])
    for i in range(maxlen):
        toSort = OrderedDict()
        for index in range(len(arr)):
            stringed = str(arr[index])
            toSort[index] = int(str(arr[index])[len(stringed)-1-i]) if len(stringed)-1-i >=0 else 0
        result = list(toSort.items())
        #mergeSort(result)
        countingSort(result)
        arrcopy = [num for num in arr]
        for index in range(len(result)):
            pair = result[index]
            ind, _ = pair
            arr[index] = arrcopy[ind]

from random import randint

if __name__ == "__main__":
    print("Enter the list length:", end='')
    listlen = int(input())
    arr = [randint(0, 1000) for _ in range(listlen)]
    print(arr)
    radixSort(arr)
    print(arr)
