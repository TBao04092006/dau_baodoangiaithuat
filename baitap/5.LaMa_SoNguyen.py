#Chuyển đổi số la mã sang số nguyên 
def chuyenDoiSo(nums: int)->str:
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    ki_hieu = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    result = ""
    for i in range(len(val)):
        while nums >= val[i]:
            result += ki_hieu[i]
            nums -= val[i]
    return result
print(chuyenDoiSo(4567))   
print(chuyenDoiSo(58))      
print(chuyenDoiSo(1994)) 