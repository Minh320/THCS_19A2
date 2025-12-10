def giai_phuong_trinh_bac_nhat(a, b):
    if a == 0:
        if b == 0:
            return "Vô số nghiệm"
        else:
            return "Vô nghiệm"
    else:
        x = -b / a
        return ("Có nghiệm", x)
print(giai_phuong_trinh_bac_nhat(2, -4))  
print(giai_phuong_trinh_bac_nhat(0, 0))   
print(giai_phuong_trinh_bac_nhat(0, 3))  