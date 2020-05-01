class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        Carry = 0
        if digits[-1] == 9:
            digits[-1] = 0
            Carry = 1
            for i in range(len(digits) - 2, -1, -1):
                if digits[i] + Carry == 10:
                    Carry = 1
                    digits[i] = 0
                else:
                    digits[i] += Carry
                    return digits
            if Carry:
                digits.insert(0, 1)
                return digits
            return digits
        else:
            digits[-1] += 1
            return digits
