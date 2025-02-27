class Solution:
    def removeDuplicates(self, nums) -> int:
        posicao = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[posicao] = nums[i]
                posicao += 1
        return posicao

result = Solution()
result.removeDuplicates([1,1,2,3,3,3,4,5])
print(result)