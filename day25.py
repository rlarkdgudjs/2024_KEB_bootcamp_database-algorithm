import webbrowser
import time


# def is_stack_full():
#     global size, stack, top
#     return top >= size - 1
#
#
# def is_stack_empty():
#     global size, stack, top
#     return top == -1
#
#
# def push(data):
#     global size, stack, top
#     if is_stack_full():
#         print("Stack is Full")
#         return
#     top += 1
#     stack[top] = data
#
#
# def pop():
#     global size, stack, top
#     if is_stack_empty():
#         print("Stack is Empty")
#         return None
#     data = stack[top]
#     stack[top] = None
#     top -= 1
#     return data
#
#
# def peek():
#     global size, stack, top
#     if is_stack_empty():
#         print("Stack is Empty")
#         return None
#     data = stack[top]
#     return data


# def check_bracket(expr):
#     for ch in expr:
#         if ch in '([{<':
#             push(ch)
#         elif ch in ')]}>':
#             out = pop()
#             if ch == ')' and out == '(':
#                 pass
#             elif ch == ']' and out == '[':
#                 pass
#             elif ch == '}' and out == '{':
#                 pass
#             elif ch == '>' and out == '<':
#                 pass
#             else:
#                 return False
#         else:
#             pass
#     return is_stack_empty()
def check_bracket(expr):
    stack = list()
    table = {')': '(', ']': '[', '}': '{', '>': '<'}
    for char in expr:
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False
        else:
            pass
    return len(stack) == 0

# size = 20
# stack = [None for _ in range(size)]
# top = -1

if __name__ == "__main__":
    expression = input()
    print(check_bracket(expression))