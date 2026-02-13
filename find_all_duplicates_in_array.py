class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        seen:dict[int,int] = {}
        final = []
        for num in nums:
            if seen.get(num) is not None:
                seen[num] = seen[num] + 1
                if seen[num] == 2:
                    final.append(num)
            else:
                seen[num] = 1
        return final
        

nums = [4,3,2,7,8,2,3,1]
print(Solution().findDuplicates(nums))