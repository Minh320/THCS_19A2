def kiem_tra_so_doi_xung(n):
    s = str(n)
    return s == s[::-1]
print(kiem_tra_so_doi_xung(121))  
print(kiem_tra_so_doi_xung(353))  
print(kiem_tra_so_doi_xung(123))  
