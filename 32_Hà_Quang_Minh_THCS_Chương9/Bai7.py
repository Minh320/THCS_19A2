def so_hoan_hao(n):
    if n <= 1:
        return False
    s = 1
    r = int(n**0.5)
    for i in range(2, r+1):
        if n % i == 0:
            s += i
            j = n // i
            if j != i:
                s += j
    return s == n

def tinh_tong_so_hoan_hao(a, b):
    a, b = int(a), int(b)
    if a > b:
        a, b = b, a
    total = 0
    for x in range(max(1, a), b+1):
        if so_hoan_hao(x):
            total += x
    return total
print(so_hoan_hao(6))              
print(so_hoan_hao(28))            
print(tinh_tong_so_hoan_hao(1, 30)) 
