def SoDoiXung(x:int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    dao_nguoc = 0
    while x > dao_nguoc:
        nums = x % 10
        dao_nguoc = dao_nguoc*10 + nums
        x //=10
    return x == dao_nguoc or x == dao_nguoc // 10
print(SoDoiXung(121))            
print(SoDoiXung(-121))     
print(SoDoiXung(10))     
print(SoDoiXung(0))     