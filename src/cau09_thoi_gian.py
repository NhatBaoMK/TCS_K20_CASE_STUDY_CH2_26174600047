from datetime import datetime

thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")

print(thoi_diem)
print(type(thoi_diem))
print(thoi_diem_text)
print(type(thoi_diem_text))



# Bo sung
bat_dau = datetime(2026, 10, 14, 13, 15)
ket_thuc = datetime(2026, 10, 14, 14, 15)
thoi_luong = ket_thuc - bat_dau
print(thoi_luong)
print(type(thoi_luong))

# datatime: lấy thời điểm hiện tại
# str: dùng để biểu diễn văn bản hoặc chữ
# timedelta: biểu diễn một khoảng thời gian
