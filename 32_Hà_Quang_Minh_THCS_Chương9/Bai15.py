def so_nguyen_to(n):
    if n < 2:
        return False
    limit = int(n**0.5) + 1
    for i in range(2, limit):
        if n % i == 0:
            return False
    return True
print(so_nguyen_to(7))
ds = [x for x in range(100, 501) if so_nguyen_to(x)]
print(ds)