def kiem_tra_so_armstrong(n):
    s = str(n)
    total = sum(int(d)**3 for d in s)
    return total == n
print(kiem_tra_so_armstrong(153))  
print(kiem_tra_so_armstrong(3203)) 