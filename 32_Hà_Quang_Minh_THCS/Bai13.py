def la_ma_tran_don_vi(a):
    n = len(a)
    # Kiểm tra ma trận vuông
    for i in range(n):
        if len(a[i]) != n:
            return False
    # Kiểm tra ma trận đơn vị
    for i in range(n):
        for j in range(n):
            if i == j:
                if a[i][j] != 1:
                    return False
            else:
                if a[i][j] != 0:
                    return False
    return True
ma_tran = [[1,0,0], [0,1,0], [0,0,1]]
if la_ma_tran_don_vi(ma_tran):
    print("Ma trận là ma trận đơn vị")
else:
    print("Ma trận KHÔNG phải là ma trận đơn vị")

