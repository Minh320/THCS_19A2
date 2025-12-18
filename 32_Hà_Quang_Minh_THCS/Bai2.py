s = input("Nhập chuỗi: ")
n = int(input("Nhập n: "))
tu = ""
ket_qua = []
for i in s:
    if i != " ":
        tu += i
    else:
        if len(tu) > n:
            ket_qua.append(tu)
        tu = ""
if len(tu) > n:
    ket_qua.append(tu)
print(f"Các từ có độ dài > {n} là: {ket_qua}")