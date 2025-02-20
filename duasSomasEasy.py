class Solution:
    def twoSum(self, lista, target):
        for i in range(len(lista)):
            for j in range(i + 1,len(lista)):
                if lista[i] + lista[j] == target:
                    return [i,j]
result = Solution()
result.twoSum([2,5,5,15], 10)