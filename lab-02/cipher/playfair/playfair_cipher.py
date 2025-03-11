class PlayfairCipher:
    def __init__(self):
        self.matrix = []

    def create_playfair_matrix(self, key):
        # Chuẩn hóa khóa: thay "J" bằng "I", chuyển thành chữ in hoa, loại bỏ ký tự trùng lặp
        key = key.replace("J", "I")
        key = key.upper()
        key_set = set(key)
        
        # Bảng chữ cái, bỏ chữ "J"
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        remainder = [letter for letter in alphabet if letter not in key_set]
        
        # Tạo chuỗi hoàn chỉnh để tạo ma trận
        matrix_key = key + "".join(remainder)
        
        # Cắt chuỗi thành ma trận 5x5
        self.matrix = []
        for i in range(0, 25):  # Chỉ lấy tối đa 25 ký tự
            if i % 5 == 0:
                self.matrix.append([])
            self.matrix[-1].append(matrix_key[i])
        
        return self.matrix

    def find_letter_coords(self, matrix, letter):
        for row in range(len(matrix)):
            for col in range(len(matrix)):
                if matrix[row][col] == letter:
                    return (row, col)
        return None

    def encrypt(self, plain_text, key):
        # Tạo ma trận dựa trên khóa
        self.create_playfair_matrix(key)
        
        # Chuẩn hóa văn bản: thay "J" bằng "I", chuyển thành chữ in hoa, loại bỏ ký tự không phải chữ cái
        plain_text = plain_text.replace("J", "I")
        plain_text = plain_text.upper()
        plain_text = "".join(c for c in plain_text if c.isalpha())
        
        # Đảm bảo độ dài chẵn bằng cách thêm "X" nếu cần
        if len(plain_text) % 2 != 0:
            plain_text += "X"
        
        encrypted_text = ""
        for i in range(0, len(plain_text), 2):
            pair = plain_text[i:i + 2]
            
            # Tìm tọa độ của hai ký tự
            row1, col1 = self.find_letter_coords(self.matrix, pair[0])
            row2, col2 = self.find_letter_coords(self.matrix, pair[1])

            if row1 == row2:  # Cùng hàng
                encrypted_text += self.matrix[row1][(col1 + 1) % 5] + self.matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:  # Cùng cột
                encrypted_text += self.matrix[(row1 + 1) % 5][col1] + self.matrix[(row2 + 1) % 5][col2]
            else:  # Khác hàng và khác cột
                encrypted_text += self.matrix[row1][col2] + self.matrix[row2][col1]

        return encrypted_text

    def decrypt(self, cipher_text, key):
        # Tạo ma trận dựa trên khóa
        self.create_playfair_matrix(key)
        
        # Chuẩn hóa văn bản: chuyển thành chữ in hoa
        cipher_text = cipher_text.upper()
        
        decrypted_text = ""
        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i + 2]
            
            # Tìm tọa độ của hai ký tự
            row1, col1 = self.find_letter_coords(self.matrix, pair[0])
            row2, col2 = self.find_letter_coords(self.matrix, pair[1])

            if row1 == row2:  # Cùng hàng
                decrypted_text += self.matrix[row1][(col1 - 1) % 5] + self.matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:  # Cùng cột
                decrypted_text += self.matrix[(row1 - 1) % 5][col1] + self.matrix[(row2 - 1) % 5][col2]
            else:  # Khác hàng và khác cột
                decrypted_text += self.matrix[row1][col2] + self.matrix[row2][col1]

        # Loại bỏ "X" bổ sung (nếu có) và trả về văn bản
        return decrypted_text.replace("X", "") if decrypted_text.endswith("X") else decrypted_text

# Ví dụ sử dụng
if __name__ == "__main__":
    cipher = PlayfairCipher()
    key = "KEYWORD"
    plain_text = "HELLO"
    encrypted = cipher.encrypt(plain_text, key)
    decrypted = cipher.decrypt(encrypted, key)
    print(f"Plain text: {plain_text}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")