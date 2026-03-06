def addBinary(self, a: str, b: str) -> str:
        # Chuyển từ nhị phân sang số nguyên, cộng lại, rồi chuyển về nhị phân
        return bin(int(a, 2) + int(b, 2))[2:]