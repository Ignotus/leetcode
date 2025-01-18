def characterToInt(c: str) -> int:
    if c == "M":
        return 1000
    if c == "D":
        return 500
    if c == "C":
        return 100
    if c == "L":
        return 50
    if c == "X":
        return 10
    if c == "V":
        return 5
    return 1

def sign(s: str) -> int:
    if s == "IV" or s == "IX":
        return -1
    if s == "XL" or s == "XC":
        return -1
    if s == "CD" or s == "CM":
        return -1

    return 1

class Solution:
    def romanToInt(self, s: str) -> int:
        if len(s) == 1:
            return characterToInt(s)

        sv = sign(s[:2]) if len(s) > 1 else 0

        return sv * characterToInt(s[0]) + self.romanToInt(s[1:])

