class Solution:
    def checkValidString(self, s: str) -> bool:
        BRACKET_PAIR = {"(": ")"}

        stack = []
        stars = 0

        for char in s:
            print(stack, stars)

            if char == "*":
                stars += 1
                continue

            if char == "(":
                stack.append(BRACKET_PAIR["("])
                continue

            if char == ")":
                if not stack:
                    if stars > 0:
                        stars -= 1
                        continue

                    return False

                if stack[-1] == ")":
                    stack.pop()
                    continue

        while stack and stars > 0:
            stack.pop()
            stars -= 1

        return True if not stack else False
