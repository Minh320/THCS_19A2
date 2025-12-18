def kiem_tra_doi_xung(a):
    n = len(a)
    for i in range(n):
        for j in range(n):
            if a[i][j] != a[j][i]:
                return False
    return True
ma_tran = [[1,2,3], [2,4,5], [3,5,6]]
if kiem_tra_doi_xung(ma_tran):
    print("Ma trận là ma trận đối xứng")
else:
    print("Ma trận KHÔNG phải là ma trận đối xứng")
