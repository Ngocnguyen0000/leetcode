# Python3 program to find element
# closest to given target using binary search.

# Returns element closest to target in arr[]
def findClosest(arr, n, target):

	# Corner cases: Điều kiện đặc biệt
	if (target <= arr[0]):
		return arr[0]
	if (target >= arr[n - 1]):
		return arr[n - 1]

	# Doing binary search: Tìm kiếm nhị phân
	i = 0; j = n; mid = 0
	while (i < j): 
		mid = (i + j) // 2

		if (arr[mid] == target):
			return arr[mid]

		# If target is less than array 
		# element, then search in left
		if (target < arr[mid]) :

			# If target is greater than previous
			# to mid, return closest of two
			if (mid > 0 and target > arr[mid - 1]):
				return getClosest(arr[mid - 1], arr[mid], target)

			# Repeat for left half 
			j = mid
		
		# If target is greater than mid
		else :
			if (mid < n - 1 and target < arr[mid + 1]):
				return getClosest(arr[mid], arr[mid + 1], target)
				
			# update i
			i = mid + 1
		
	# Only single element left after search
	return arr[mid]


# Method to compare which one is the more close.
# We find the closest by taking the difference
# between the target and both values. It assumes
# that val2 is greater than val1 and target lies
# between these two.
def getClosest(val1, val2, target):

	if (target - val1 >= val2 - target):
		return val2
	else:
		return val1

# Driver code
arr = [1, 2, 4, 5, 6, 6, 8, 9] 
n = len(arr)
target = 11
print(findClosest(arr, n, target))


