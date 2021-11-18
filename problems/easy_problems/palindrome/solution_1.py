def isPalindrome(self, x):
        if x < 0:
            return False
        forward = [number for number in str(x)]
        backward = [num for num in reversed(forward)]
        if forward == backward:
            return True
        return False
