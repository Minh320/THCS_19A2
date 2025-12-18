a = [1, 4, 2, 3, 1, 4, 2]
ket_qua = []
for x in a:
    co = False
    for y in ket_qua:
        if x == y:
            co = True
            break
    if not co:
        ket_qua.append(x)
print(f"Danh sách ban đầu: {a}")
print(f"Danh sách sau khi loại trùng: {ket_qua}")
