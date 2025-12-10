def tong_chu_so_de_quy(n):
    n = abs(int(n))
    if n < 10:
        return n
    return n % 10 + tong_chu_so_de_quy(n // 10)
print(tong_chu_so_de_quy(10))  
