import math
def la_so_nguyen_to(n):
    n = int(n)
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    r = int(math.sqrt(n))
    for i in range(3, r+1, 2):
        if n % i == 0:
            return False
    return True

def in_so_nguyen_to_trong_khoang(a, b):
    a, b = int(a), int(b)
    if a > b:
        a, b = b, a
    result = []
    for x in range(max(2, a), b+1):
        if la_so_nguyen_to(x):
            result.append(x)
    return result
print(la_so_nguyen_to(17))                
print(in_so_nguyen_to_trong_khoang(10, 30)) 
