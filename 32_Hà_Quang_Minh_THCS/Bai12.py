def nhan_ma_tran(A, B):
    m = len(A)
    n = len(A[0])
    p = len(B[0])
    C = []
    for i in range(m): # Tạo ma trận kết quả C toàn số 0
        hang = []
        for j in range(p):
            hang.append(0)
        C.append(hang)
    for i in range(m): # Nhân ma trận
        for j in range(p):
            tong = 0
            for k in range(n):
                tong = tong + A[i][k] * B[k][j]
            C[i][j] = tong

    return C
A = [[1,2,3], [3,4,1], [2,5,3]]
B = [[2,4,3], [6,4,3], [2,4,5]]
C = nhan_ma_tran(A, B)
print(f"Ma trận kết quả C: {C}")

