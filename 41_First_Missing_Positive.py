class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Filter positive numbers
        nums = [n for n in nums if n > 0]
        # Sort the list
        nums.sort()
        # Initialize target
        t = 1
       # Traverse the sorted list
        for n in nums:
            if n == t:
                t += 1
            elif n > t:
                return t
        # If no missing number is found, return t
        return t
