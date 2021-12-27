dic={"(":")","{":"}","[":"]"}

class Solution(object):
    def isValid(self, symbols):
        if len(symbols) % 2 != 0:
            return False
        new_stack = []
        for item in symbols:
            if item in dic.keys():
                new_stack.append(item)
            elif item in dic.values():
                if new_stack and dic[new_stack[-1]] == item:
                    new_stack.pop()
                else:
                    return False
        if new_stack == []:
            return True
        else:
            return False
