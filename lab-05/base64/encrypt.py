import base64

def main():
    input_string = input("Nhập thông tin cần mã hóa: ")  # Nhận dữ liệu từ người dùng
    encoded_bytes = base64.b64encode(input_string.encode("utf-8"))  # Mã hóa dữ liệu vào base64
    encoded_string = encoded_bytes.decode("utf-8")  # Chuyển đổi từ bytes thành chuỗi
    
    # Ghi chuỗi mã hóa vào tệp
    with open("data.txt", "w") as file:
        file.write(encoded_string)
    
    print("Đã mã hóa và ghi vào tệp data.txt")  # In thông báo cho người dùng

if __name__ == "__main__":
    main()
