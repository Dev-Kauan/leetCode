class Solution:
    def isPalindrome(self, n):
        lista = list(str(n))
        i = len(lista) - 1
        novaLista = []
        while i>=0:
            novaLista.append(lista[i])
            i = i -1
        if lista == novaLista:
            return True
        else:
            return False   

result = Solution()
result.isPalindrome(121)