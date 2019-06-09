def insertionSort(arr):
	for i in range(0, len(arr)):
		key = arr[i]
		j = i-1
		while j>=0 and arr[j]>key:
			arr[j+1] = arr[j]
			j-=1
		arr[j+1] = key 

if __name__ == "__main__":
	arr = [4,3,2,1]
	print(arr)
	insertionSort(arr)
	print(arr)
