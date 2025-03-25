import base64

def main():
    try:
        with open("data.txt", "r") as file:
            encoded_string = file.read().strip()  # Đọc dữ liệu từ tệp và loại bỏ các ký tự thừa
            decoded_bytes = base64.b64decode(encoded_string)  # Giải mã từ base64
            decoded_string = decoded_bytes.decode("utf-8")  # Chuyển đổi từ bytes sang chuỗi UTF-8
            
            print("Chuỗi sau khi giải mã:", decoded_string)  # In ra chuỗi đã giải mã
    except Exception as e:
        print("Lỗi:", e)  # Xử lý các lỗi nếu có

if __name__ == "__main__":
    main()
