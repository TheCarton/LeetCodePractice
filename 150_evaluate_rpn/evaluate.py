class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def minus(a, b):
            return a - b
        def plus(a, b):
            return a + b
        def div(a, b):
            return int(a / b)
        def mul(a, b):
            return a * b
        symbols = []
        operators = {"-" : minus , "+" : plus, "/" : div, "*" : mul}
        for token in tokens:
            if token in operators:
                operation = operators[token]
                b = symbols.pop()
                a = symbols.pop()
                symbols.append(operation(a, b))
            else:
                symbols.append(int(token))

        return symbols.pop()