from collections import deque

def isValid(string: str) -> bool:
    stack = deque()
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in string:
        if char in pairs.values():       # opening
            stack.append(char)
        elif char in pairs:              # closing
            if stack and stack[-1] == pairs[char]:
                stack.pop()
            else:
                return False
    return not stack

# Tests
assert isValid("{[()]}")  == True
assert isValid("()")      == True
assert isValid("{}")      == True
assert isValid("[]")      == True
assert isValid("[{}]")    == True
assert isValid("{[)]")    == False
assert isValid("[(])")    == False

print("All tests passed ✅")

def is_palindrome(string: str) -> bool:
    for i in range(len(string) // 2):
        if string[i] != string[-i-1]:
            return False
    return True

# Tests
assert is_palindrome("abba") == True
assert is_palindrome("abcba") == True
assert is_palindrome("abcd") == False

print("All tests passed ✅")