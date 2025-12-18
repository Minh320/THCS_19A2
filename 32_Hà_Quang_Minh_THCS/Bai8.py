a = [1, 2, 3, 4, 5]
k = int(input("Nhập k: "))
n = len(a)
k = k % n
i = 0
while i < k:
    cuoi = a[n - 1]    
    j = n - 1
    while j > 0:
        a[j] = a[j - 1]
        j = j - 1
    a[0] = cuoi         
    i = i + 1
print(f"Danh sách sau khi dịch: {a}")
