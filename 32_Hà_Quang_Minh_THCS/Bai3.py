s = input("Nhập chuỗi: ")
ket_qua = ""
da_gap_chu = False      # đã gặp ký tự chữ/số chưa
truoc_la_space = False # ký tự trước có phải dấu cách không
for ch in s:
    if ch != " ":                 # gặp chữ hoặc ký tự khác
        ket_qua += ch
        da_gap_chu = True
        truoc_la_space = False
    else:                          # gặp dấu cách
        if da_gap_chu and not truoc_la_space:
            ket_qua += ch          # chỉ thêm 1 dấu cách
            truoc_la_space = True
print(f"Chuỗi sau khi xử lý: {ket_qua}")