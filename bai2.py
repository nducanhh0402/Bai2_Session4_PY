# Chức năng 1: Yêu cầu người dùng nhập vào tổng số lượng hóa đơn đã xuất trong ca
n = int(input("Nhap so luong hoa don trong ca: "))

# Kiểm tra nếu số lượng hóa đơn không hợp lệ
if n <= 0:
    print("So luong hoa don khong hop le!")
else:
    max_val = None
    min_val = None

    # Chức năng 2: Lặp và nhập giá trị cho từng hóa đơn
    for i in range(1, n + 1):
        current_val = int(input(f"Nhap gia tri hoa don thu {i}: "))

        # Chức năng 3: Tìm giá trị hóa đơn lớn nhất (Max) và nhỏ nhất (Min)
        if max_val is None or current_val > max_val:
            max_val = current_val
        if min_val is None or current_val < min_val:
            min_val = current_val

    # Hiển thị kết quả đúng chuẩn theo mẫu output trong ảnh
    print("------ KET QUA KIEM TOAN CA RIKKEI STORE ------")
    print(f"Hoa don co gia tri cao nhat: {max_val} VND")
    print(f"Hoa don co gia tri thap nhat: {min_val} VND")