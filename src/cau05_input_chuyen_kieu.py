ma_may = input("Nhập mã máy:")
cong_suat_w = float(input("Nhập công suất W:"))
so_phut = int(input("Nhập số phút:"))
don_gia_kwh = float(input("Nhập đơn giá điện/kWh:"))

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("Mã máy:", ma_may)
print("Điện năng:", dien_nang_kwh, "kWh")
print("Chi phí:", chi_phi, "vnd")
