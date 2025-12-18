def tach_chan_le_va_tinh_tong(t):
    chan = ()
    le = ()
    tong_chan = 0
    tong_le = 0
    for x in t:
        if x % 2 == 0:
            chan = chan + (x,)
            tong_chan = tong_chan + x
        else:
            le = le + (x,)
            tong_le = tong_le + x

    return chan, le, tong_chan, tong_le

a = [1,2,3,4,5,6]

chan, le, tong_chan, tong_le = tach_chan_le_va_tinh_tong(a)

print("Tuple ban đầu:", a)
print("Tuple chẵn:", chan)
print("Tổng các số chẵn:", tong_chan)
print("Tuple lẻ:", le)
print("Tổng các số lẻ:", tong_le)
