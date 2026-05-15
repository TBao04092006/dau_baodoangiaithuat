def uniqueOccurrences(self, arr):
        # Bước 1: Đếm số lần xuất hiện của mỗi phần tử
        counts = Counter(arr)
        
        # Bước 2: Lấy danh sách các số lần xuất hiện (values)
        occurrence_list = counts.values()
        
        # So sánh số lượng tần suất với số lượng tần suất duy nhất
        return len(occurrence_list) == len(set(occurrence_list))