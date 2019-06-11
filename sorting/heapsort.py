def heapify(arr, currentIndex, boundary):
    leftChildIndex = currentIndex*2 + 1
    rightChildIndex = currentIndex*2 + 2
    leftChild = float("-inf") if leftChildIndex>=len(arr) or leftChildIndex>boundary else arr[leftChildIndex]
    rightChild = float("-inf") if rightChildIndex>=len(arr) or rightChildIndex>boundary else arr[rightChildIndex]
    largest = max(leftChild, rightChild)
    largestIndex = leftChildIndex if leftChild == largest else rightChildIndex
    if largest != float("-inf") and largest > arr[currentIndex]:
        arr[currentIndex], arr[largestIndex] = arr[largestIndex], arr[currentIndex]
        buildMaxHeap(arr, largestIndex, boundary)

def buildMaxHeap(arr, begin, end):
    heapSize = end-begin
    for i in range(heapSize//2, -1, -1):
        heapify(arr, i, end)

def heapsort(arr):
    for i in range(len(arr)-1, -1, -1):
        buildMaxHeap(arr, 0, i)
        arr[0], arr[i] = arr[i], arr[0]
    return arr

from random import randint

if __name__ == "__main__":
	print("Length of the list:", end="")
	listLength = int(input())
	arr = [randint(0, 100) for _ in range(listLength)]
	print(arr)
	heapsort(arr)
	print(arr)
