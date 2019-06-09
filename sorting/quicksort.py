def partition(arr, low, high):
	pivot = arr[high]
	i = low - 1
	for j in range(low, high):
		if arr[j] <= pivot:
			i+=1
			arr[j], arr[i] = arr[i], arr[j]
	arr[i+1], arr[high] = arr[high], arr[i+1]
	return i+1

def quicksort(arr, low, high):
	if low<high:
		pivotIndex = partition(arr, low, high)
		quicksort(arr, low, pivotIndex-1)
		quicksort(arr, pivotIndex+1, high)

from random import randint

if __name__ == "__main__":
	print("List length: ", end="")
	listLength = int(input())
	begin, end = 0, 100
	arr = [randint(begin, end) for _ in range(listLength)]
	print("Array:", arr)
	quicksort(arr, 0, len(arr)-1)
	print("Sorted:", arr)
