class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        if len(flowerbed) == 1 and flowerbed[0] == 0 and not n == 0:
            n -= 1
            flowerbed[0] = 1
        for j in range(1, len(flowerbed)):
            if n == 0:
                break
            if j - 1== 0 and flowerbed[j -1] == 0 and flowerbed[j] == 0:
                n -= 1
                flowerbed[j - 1] = 1
            if j != len(flowerbed) -1:
                if flowerbed[j] == 0 and flowerbed[j - 1] == 0 and flowerbed[j + 1] == 0:
                    n -= 1
                    flowerbed[j] = 1
            elif flowerbed[j] == 0 and flowerbed[j - 1] == 0:
                n -= 1
                flowerbed[j] = 1
        if n != 0:
            return False
        else:
            return True

result = Solution()
result.canPlaceFlowers([0], 0)