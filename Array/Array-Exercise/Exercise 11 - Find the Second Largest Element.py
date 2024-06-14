class Solution:
    
    def secondLargestElement(self, arr):  
        if len(arr) < 2:
            return None 

        if arr[0] > arr[1]:
            largest = arr[0]
            secondLargest = arr[1]
        else:
            largest = arr[1]
            secondLargest = arr[0]

        # Duyệt qua các phần tử còn lại trong mảng
        for i in range(2, len(arr)):
            element = arr[i]
            if element > largest:
                secondLargest = largest
                largest = element
            elif element > secondLargest and element != largest:
                secondLargest = element

        return secondLargest

solution = Solution() 
arr = [1, 3, 4, 5, 0, 2]
result = solution.secondLargestElement(arr)  
print("The second largest element is:", result)

