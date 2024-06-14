# Bài toán này liên quan đến việc tìm kiếm một chuỗi con (substring) trong một chuỗi lớn hơn (hay còn gọi là chuỗi mẹ)
def longest_palindromic_substring(array):
    max_length = 0

    # Kiểm tra các chuỗi con đối xứng có độ dài lẻ
    for i in range(1, len(array)):
        current_length = 0
        left, right = i - 1, i + 1
        while left >= 0 and right < len(array) and array[left] == array[right]:
            current_length += 2
            left -= 1
            right += 1
        if (current_length + 1) > max_length:
            max_length = current_length + 1

    # Kiểm tra các chuỗi con đối xứng có độ dài chẵn
    for i in range(len(array)):
        current_length = 0
        left, right = i, i + 1
        while left >= 0 and right < len(array) and array[left] == array[right]:
            current_length += 2
            left -= 1
            right += 1
        if current_length > max_length:
            max_length = current_length

    return max_length

# Ví dụ sử dụng
array = ["T", "O", "T", "K", "G", "H", "H", "O", "T", "T", "O", "O", "H", "G"]
print("Độ dài chuỗi con đối xứng dài nhất:", longest_palindromic_substring(array))

