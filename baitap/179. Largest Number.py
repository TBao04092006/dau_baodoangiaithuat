from functools import cmp_to_key
def largestNumber(self, nums):
        # Chuyển các số thành chuỗi
        str_nums = list(map(str, nums))
        
        # Định nghĩa quy tắc so sánh tùy chỉnh
        def compare(x, y):
            if x + y > y + x:
                return -1
            else:
                return 1
                
        # Sắp xếp theo quy tắc trên
        str_nums.sort(key=cmp_to_key(compare))
        
        # Ghép lại thành kết quả
        res = "".join(str_nums)
        
        # Xử lý trường hợp mảng toàn số 0 (tránh kết quả "000")
        return "0" if res[0] == "0" else res