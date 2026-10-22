from datetime import datetime

# Nhap
ma_phien = input("Nhap ma phien: ")
ma_may = input("Nhap ma may: ")
cong_suat = float(input("Nhap cong suat thiet bi: "))
thoi_luong = int(input("Nhap thoi gian su dung: "))
don_gia = float(input("Nhap don gia dien: "))

dien_nang = cong_suat * thoi_luong / 60 / 1000
chi_phi = dien_nang * don_gia
tren_60 = thoi_luong > 60

# Thoi gian
thoi_diem = datetime.now()
thoi_diem_dinh_dang = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")

# Xuat
print(f"Ma phien: {ma_phien}")
print(f"May: {ma_may}")
print(f"Cong suat: {cong_suat:.2f} W")
print(f"Thoi luong: {thoi_luong} phut")
print(f"Dien nang: {dien_nang:.3f} kWh")
print(f"Chi phi: {chi_phi:.2f} VND")
print(f"Tren 60 phut: {tren_60}")
print(f"Ghi nhan luc: {thoi_diem_dinh_dang}")


#Gia su co loi va can sua loi
