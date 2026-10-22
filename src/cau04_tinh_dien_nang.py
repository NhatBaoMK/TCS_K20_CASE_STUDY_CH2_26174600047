cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("Điện năng tiêu thụ", dien_nang_kwh, "kWh")
print("Chi phí điện", chi_phi, "vnd")




so_phut = 60

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("Sau khi đổi thời gian")
print("Điện năng", dien_nang_kwh, "kWh")
print("Chi phí", chi_phi, "vnd")


#    DU DOAN KET QUA:

# Điện năng tiêu thụ 0.375 kWh
# Chi phí điện 1125.0 vnd
# Sau khi đổi thời gian
# Điện năng 0.25 kWh
# Chi phí 750.0 vnd
