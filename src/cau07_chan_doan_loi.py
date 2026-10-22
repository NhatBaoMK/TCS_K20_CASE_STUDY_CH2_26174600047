ma_may = input("Nhập mã máy: ")
#cong_suat_w = input("Nhập công suất W: ")
cong_suat_w = float(input("Nhập công suất W: "))
so_phut = int(input("Nhập số phút: "))

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print(f"Máy: {ma_may}")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")


# Nhapj PC12, 250, 90 -> Chương trình sẽ báo lỗi vì cong_suat_w đang là chuỗi không phải số
# Lỗi kiểu dữ liệu TypeError, phép chia không thực hiện được vì giá trị trung gian là chuỗi



# Sua loi
# cong_suat_w = float(input("Nhập công suất W: "))
