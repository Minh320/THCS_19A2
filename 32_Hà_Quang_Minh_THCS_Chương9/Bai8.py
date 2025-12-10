def tim_so_le_lon_nhat(a, b, c):
    i = [a, b, c]
    j = [x for x in i if x % 2 != 0]
    return max(j) if  j else -1

print(tim_so_le_lon_nhat(2, 4, 6)) 
print(tim_so_le_lon_nhat(1, 5, 3))  
