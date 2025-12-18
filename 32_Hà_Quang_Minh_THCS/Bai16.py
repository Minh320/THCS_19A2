def dem_tan_suat_ky_tu(s):
    tan_suat = {}
    for i in s:
        if i in tan_suat:
            tan_suat[i] = tan_suat[i] + 1
        else:
            tan_suat[i] = 1
    return tan_suat

ds = input("Nhập chuỗi: ")
ket_qua = dem_tan_suat_ky_tu(ds)
print("Tần suất xuất hiện của các ký tự:", ket_qua)