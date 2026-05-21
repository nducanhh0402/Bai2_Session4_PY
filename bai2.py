# Khởi tạo các biến tích lũy ban đầu
tong_doanh_thu = 0
so_ngay_dat_muc_tieu = 0
MUC_TIEU_CAO = 5000000

# Chức năng 1: Sử dụng vòng lặp chạy đúng 7 lần để nhập doanh thu
for ngay in range(1, 8):
    # Yêu cầu người dùng nhập doanh thu cho từng ngày
    doanh_thu_ngay = float(input(f"Nhập doanh thu Ngày {ngay}: "))
    
    # Chức năng 2: Tích lũy tổng doanh thu của cả tuần
    tong_doanh_thu += doanh_thu_ngay
    
    # Chức năng 3: Kiểm tra và đếm số ngày đạt mục tiêu doanh thu cao
    if doanh_thu_ngay >= MUC_TIEU_CAO:
        so_ngay_dat_muc_tieu += 1

# Tính doanh thu trung bình mỗi ngày trong tuần
doanh_thu_trung_binh = tong_doanh_thu / 7

# Xuất báo cáo kết quả ra màn hình theo định dạng yêu cầu
print("\n--- BÁO CÁO DOANH THU TUẦN RIKKEI STORE ---")
print(f"Tổng doanh thu cả tuần: {tong_doanh_thu:.0f} VND")
print(f"Doanh thu trung bình mỗi ngày: {doanh_thu_trung_binh:.0f} VND")
print(f"Số ngày đạt doanh thu mục tiêu (>= 5,000,000 VND): {so_ngay_dat_muc_tieu} ngày")