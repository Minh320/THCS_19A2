x = input("Nhập chuỗi: ")
chu_cai = 0
chu_so = 0
dac_biet = 0
for i in x:
    if ('a' <= i <= 'z') or ('A' <= i <= 'Z'):
        chu_cai += 1
    elif '0' <= i <= '9':
        chu_so += 1
    else:
        dac_biet += 1
print(f"Số chữ cái: {chu_cai}")
print(f"Số chữ số: {chu_so}")
print(f"Số ký tự đặc biệt: {dac_biet}")