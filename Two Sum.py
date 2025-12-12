from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

# Test it
if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2,7,11,15], 9)) 
    print(solution.twoSum([3,2,4], 6))     
    print(solution.twoSum([3,3], 6))        