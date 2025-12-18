def tong_duong_cheo_phu(a):
    n = len(a)
    tong = 0
    for i in range(n):
        for j in range(n):
            if i + j == n - 1:
                tong = tong + a[i][j]
    return tong
ma_tran = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
tong = tong_duong_cheo_phu(ma_tran)
print(f"Tổng đường chéo phụ: {tong}")