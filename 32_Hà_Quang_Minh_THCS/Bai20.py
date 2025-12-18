def loc_dictionary(d):
    ket_qua = {}
    for k in d:
        if d[k] > 50:
            ket_qua[k] = d[k]
    return ket_qua

ds = {"A": 63,
      "B": 23,
      "C": 60,
      "D": 55,
      "E": 95}
ket_qua = loc_dictionary(ds)

print("Dictionary ban đầu:", ds)
print("Các cặp key-value có value > 50:", ket_qua)
