class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            match token:
                case _ if token.isnumeric():
                    stack.append(int(token))

                case "+":
                    stack.append(stack.pop() + stack.pop())

                case "-":
                    stack.append(stack.pop() - stack.pop())

                case "*":
                    stack.append(stack.pop() * stack.pop())

                case "/":
                    stack.append(stack.pop() // stack.pop())

                case _:
                    raise ValueError("Input must be valid.")

        return stack.pop()
