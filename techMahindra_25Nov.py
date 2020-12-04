def findTotalDistance(arr, l):
	new_arr = []
	for i in range(l-1):
		diff = abs(arr[i] - arr[i+1])
		new_arr.append(diff)
	addition = sum(new_arr)
	return addition


arr = [10, 11, 7, 12, 14]
l = 5
findTotalDistance(arr, l)