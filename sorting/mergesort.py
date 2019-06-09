def mergeSort(arr):
	if len(arr)>1:
		left, right = 0, len(arr)
		mid = left + (right-left)//2
		leftArr = arr[:mid]
		rightArr = arr[mid:]
		mergeSort(leftArr)
		mergeSort(rightArr)
		leftI = rightI = arrI = 0
		while len(leftArr)>leftI and len(rightArr)>rightI:
			if leftArr[leftI] < rightArr[rightI]:
				arr[arrI] = leftArr[leftI]
				arrI += 1
				leftI += 1
			else:
				arr[arrI] = rightArr[rightI]
				arrI += 1
				rightI += 1
		while leftI < len(leftArr):
			arr[arrI] = leftArr[leftI]
			arrI += 1
			leftI += 1
		while rightI < len(rightArr):
			arr[arrI] = rightArr[rightI]
			arrI += 1
			rightI += 1

from random import randint

if __name__ == "__main__":
	print("Length of the list:", end="")
	listLength = int(input())
	arr = [randint(0, 100) for _ in range(listLength)]
	print(arr)
	mergeSort(arr)
	print(arr)
