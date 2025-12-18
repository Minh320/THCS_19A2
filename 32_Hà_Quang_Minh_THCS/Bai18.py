def dao_nguoc_dictionary(d):
    d_nguoc = {}
    for k in d:
        v = d[k]
        d_nguoc[v] = k
    return d_nguoc
ds = {1 : 10,
      2 : 20,
      3 : 30}
ket_qua = dao_nguoc_dictionary(ds)
print("Dictionary ban đầu:", ds)
print("Dictionary sau khi đảo:", ket_qua)
