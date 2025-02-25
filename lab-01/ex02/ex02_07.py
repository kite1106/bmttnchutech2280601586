print(" nhập văn bản (nhap done de ket thuc): ")
lines =[]
while True:
    line =input()
    if line.lower() == 'done':
        break
    lines.append(line)
print("\n các dòng đã nhập sau khi chuyển thành chữ hoá: ")
for line in lines:
    print(line.upper())