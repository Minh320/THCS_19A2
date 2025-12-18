def tim_key_gia_tri_lon_nhat(d):
    max_key = None
    max_value = None
    for k in d:
        if max_value is None or d[k] > max_value:
            max_value = d[k]
            max_key = k
    return max_key

n = int(input("Nhập số cặp key-value: "))

d = {}
for i in range(n):
    key = int(input("Nhập key: "))
    value = int(input("Nhập value: "))
    d[key] = value

ket_qua = tim_key_gia_tri_lon_nhat(d)

print("Dictionary:", d)
print("Key có giá trị lớn nhất là:", ket_qua)
