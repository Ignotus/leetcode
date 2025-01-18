class Solution:
    def isValid(self, s: str) -> bool:
        def isValidImpl(openBrackets: list, s: str) -> bool:
            if not s:
                return not openBrackets

            if s[0] in "([{":
                return isValidImpl(openBrackets + [s[0]], s[1:])

            if not openBrackets:
                return False

            if (s[0] == ")" and openBrackets[-1] == "(") or\
                    (s[0] == ']' and openBrackets[-1] == "[") or\
                    (s[0] == '}' and openBrackets[-1] == "{"):
                return isValidImpl(openBrackets[:-1], s[1:])

            return False

        return isValidImpl([], s)
