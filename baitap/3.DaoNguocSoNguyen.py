def daoNguocSo(num):
    return int(str(num)[::-1])
print("Nhap so: ")
num = int(input())
print(daoNguocSo(num))
