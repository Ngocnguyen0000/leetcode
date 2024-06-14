from collections import defaultdict

def freqSort(arr):
    # Bước 1: Đếm tần suất xuất hiện của các phần tử
    frq = defaultdict(int)
    for e in arr:
        frq[e] += 1

    # Bước 2: Sắp xếp lại mảng dựa trên tần suất và giá trị
    # - Đầu tiên sắp xếp theo tần suất giảm dần
    # - Nếu tần suất bằng nhau thì sắp xếp theo giá trị tăng dần
    def custom_sort(x):
        return (-frq[x], x)

    arr.sort(key=custom_sort)  # Dòng lệnh sắp xếp được di chuyển ra khỏi hàm custom_sort

    return arr

if __name__ == '__main__':
    T = int(input("Nhập số lượng bộ thử nghiệm: "))

    for _ in range(T):
        n = int(input("Nhập kích thước mảng: "))
        arr = [int(x) for x in input("Nhập các phần tử mảng: ").split()]
        sorted_arr = freqSort(arr)
        print(*sorted_arr)

