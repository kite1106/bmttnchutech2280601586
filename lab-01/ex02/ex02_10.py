def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]
intput_string = input("mời nhập chuỗi cần đảo ngược: ")
print("chuỗi đã đảo ngược là: ",dao_nguoc_chuoi(intput_string))