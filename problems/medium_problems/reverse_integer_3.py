class Solution:
    def reverse(self, x: int) -> int:
        symbol = 1
        str_int = ''
        if x < 0: 
            symbol = -1
            str_int = str(x)[1:][::-1]
        else:
            str_int = str(x)[::-1]
            
        if int(str_int) > 2**31:
            return 0
        else: 
            return int(str_int) * symbol
