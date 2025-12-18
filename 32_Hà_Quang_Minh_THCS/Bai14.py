def xu_ly_hai_set(A, B):
    A_khong_B = set()
    B_khong_A = set()
    giao = set()
    hop = set()
    # A nhưng không thuộc B
    for x in A:
        if x not in B:
            A_khong_B.add(x)
    # B nhưng không thuộc A
    for x in B:
        if x not in A:
            B_khong_A.add(x)
    # Giao của A và B
    for x in A:
        if x in B:
            giao.add(x)
    # Hợp của A và B
    for x in A:
        hop.add(x)
    for x in B:
        hop.add(x)
    return A_khong_B, B_khong_A, giao, hop
A = (1,2,3,4,5,6,7,8)
B = (1,2,3,4,6,7,9,10)
A_khong_B, B_khong_A, giao, hop = xu_ly_hai_set(A, B)
print("A nhưng không thuộc B:", A_khong_B)
print("B nhưng không thuộc A:", B_khong_A)
print("Giao của A và B:", giao)
print("Hợp của A và B:", hop)
