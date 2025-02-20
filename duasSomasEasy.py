class Solution:
    def twoSum(self, lista, target):
        for i in range(len(lista)):
            for j in range(len(lista) - 1):
                if lista[i] + lista[j + 1] == target:
                    return [i,j+1]
result = Solution()
result.twoSum([2,7,11,15], 9)