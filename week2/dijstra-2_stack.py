from stack_array import Stack

ops = Stack()
vals = Stack()

def calculate(exp):
    for char in exp:
        if char == "+" or char == "*":
            ops.push(char)
        elif char == ")":
            op = ops.pop()
            if op == "+":
                vals.push(vals.pop() + vals.pop())
            if op == "*":
                vals.push(vals.pop() * vals.pop())
        elif char == " " or char == "(":
            pass
        else:
            vals.push(int(char))
    print(vals.pop())


expression = input("Enter expression: ")
calculate(expression)