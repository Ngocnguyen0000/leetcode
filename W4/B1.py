# arr = [4, 7, 8, 2, 3, 2, 1, 9]
#                             i
       


class Solution1:
    def findduplicate(self, arr):
        new_arr = set() # 4,7,8,2,3,1
        duplicate = set() # 2
        
        for i in range(len(arr)):
            if arr[i] in new_arr:
                duplicate.add(arr[i])
            else:
                new_arr.add(arr[i])
        return list(duplicate)

# [4, 7, 8, 2, 3, 2, 1]
# 4, 7, 8, 2, 3, 1


class Solution2:
    def findduplicate(self, arr):
        duplicate2 = [] # 2
        
        for i in range(len(arr)):
            if arr[i] in arr[:i]:
                if arr[i] not in duplicate2:
                    duplicate2.append(arr[i])
        
        return duplicate2


# solution = Solution1()
solution = Solution1()
arr = []
result = solution.findduplicate(arr)

if not result:
    print("None")
else:
    print(result)






# Create a dictionary
map = {
    "John": 25,
    "Jane": 30,
    "Doe": 35
}

# Adding elements to the dictionary
map["John"] = 26
print("After changing John's age:", map)

# Removing an element
del map["Doe"]
print("After removing Doe:", map)

# Checking if a key exists
key_to_check = "Jane"
if key_to_check in map:
    print(key_to_check + " is present in the dictionary")
else:
    print(key_to_check + " is not present in the dictionary")

# Retrieving a value
key_to_retrieve = "John"
johns_age = map[key_to_retrieve]
print("Age of " + key_to_retrieve + ":", johns_age)




Phương thức chính:

map[key] = value: Thêm hoặc cập nhật cặp khóa-giá trị.
map.get(key): Lấy giá trị tương ứng với khóa, trả về None nếu khóa không tồn tại.
del map[key]: Xóa mục với khóa cụ thể.
key in map: Kiểm tra xem dictionary có chứa khóa cụ thể không.
value in map.values(): Kiểm tra xem dictionary có chứa giá trị cụ thể không.