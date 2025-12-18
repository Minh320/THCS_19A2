def nhom_sinh_vien_theo_diem(d):
    ket_qua = {}
    for ten in d:
        diem = d[ten]
        if diem in ket_qua:
            ket_qua[diem].append(ten)
        else:
            ket_qua[diem] = [ten]
    return ket_qua
ds = {"duc":9,
      "vinh":8,
      "hiep":8,
      "manh":7,
      "lam":7}
ket_qua = nhom_sinh_vien_theo_diem(ds)
print("Dictionary ban đầu:", ds)
print("Dictionary sau khi nhóm theo điểm:", ket_qua)
