from heapq import heapify, heappop

def heapsort(arr):
	copy = [num for num in arr]
	heapify(copy)
	for i in range(len(arr)):
		arr[i] = heappop(copy)

from random import randint

if __name__ == "__main__":
	print("Length of the list:", end="")
	listLength = int(input())
	arr = [randint(0, 100) for _ in range(listLength)]
	print(arr)
	heapsort(arr)
	print(arr)
