class Solution:
    def findPeakElement(self, Array: List[int]) -> int:
        left = 0
        right = len(Array) - 1

        while left < right:
            mid = (left + right) // 2

            if Array[mid] > Array[mid-1] and Array[mid] > Array[mid+1]:
                return mid
            if Array[mid] > Array[mid+1]:
                right = mid
            else:
                left = mid + 1
        return left
        
