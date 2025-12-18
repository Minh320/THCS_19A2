a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 8 #tổng 
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] + a[j] == k:
            print(f"Cặp số: {a[i], a[j]}")
