def tao_tuple_tu_list(lst):
    return tuple(lst)

# Nhập danh sách từ người dùng
input_list = input("Nhập danh sách các số, cách nhau bằng dấu cách: ")

# Chuyển chuỗi nhập vào thành danh sách số nguyên
numbers = list(map(int, input_list.split()))

# Tạo tuple từ danh sách
my_tuple = tao_tuple_tu_list(numbers)

# In kết quả
print("List:", numbers)
print("Tuple từ list:", my_tuple)