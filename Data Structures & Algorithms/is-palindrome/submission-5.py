import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        numbers = "0123456789"
        for char in s:
            if char in string.ascii_letters:
                lower = char.lower()
                new_s += lower
            elif char in numbers:
                new_s += char
        reversed_s = new_s[::-1]
        print(new_s)
        print(reversed_s)
        return new_s == reversed_s
        