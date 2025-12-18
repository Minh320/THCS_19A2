a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tong_chan = 0
tong_le = 0
for x in a:
    if x % 2 == 0:
        tong_chan += x
    else:
        tong_le += x
print(f"Tổng số chẵn: {tong_chan}")
print(f"Tổng số lẻ: {tong_le}")