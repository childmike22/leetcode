def isPalindrome(self, x):
        word = str(x)
        if word == word[::-1]:
            return True
        return False
