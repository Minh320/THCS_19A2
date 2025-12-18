a = [1, 7, 14, 9, 32, 18]
max1 = a[0]
max2 = None
for x in a:
    if x > max1:
        max2 = max1
        max1 = x
    elif x != max1 and x > max2:
        max2 = x
print(f"Giá trị lớn thứ hai là: {max2}")