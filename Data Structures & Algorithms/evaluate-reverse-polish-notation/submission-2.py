class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            match token:
                case token if token.isnumeric():
                    stack.append(int(token))

                case "+":
                    stack.append(stack.pop() + stack.pop())

                case "-":
                    stack.append(-stack.pop() + stack.pop())

                case "*":
                    stack.append(stack.pop() * stack.pop())

                case "/":
                    divisor, dividend = stack.pop(), stack.pop()
                    stack.append(dividend // divisor)

                case _:
                    raise ValueError("Input must be valid.")

            print(stack)

        return stack.pop()
