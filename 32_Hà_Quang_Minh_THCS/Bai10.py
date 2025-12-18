def hang_co_tong_lon_nhat(a):
    so_hang = len(a)
    so_cot = len(a[0])
    max_tong = None
    vi_tri = 0
    for i in range(so_hang):
        tong = 0
        for j in range(so_cot):
            tong = tong + a[i][j]
        if max_tong is None or tong > max_tong:
            max_tong = tong
            vi_tri = i
    return vi_tri, max_tong
ma_tran = [[1,3,4], [2,6,5], [3,8,4]]
hang_max, tong_max = hang_co_tong_lon_nhat(ma_tran)
print("Hàng có tổng lớn nhất là hàng:", hang_max)
print("Tổng lớn nhất là:", tong_max)
