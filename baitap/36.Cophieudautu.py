def maxProfit(self, prices):
        # Giả định giá mua thấp nhất ban đầu là vô cực
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # Nếu tìm thấy giá thấp hơn giá mua hiện tại, hãy cập nhật nó
            if price < min_price:
                min_price = price
            # Ngược lại, tính thử lợi nhuận nếu bán vào ngày hôm nay
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit