n = int(input())
for _ in range(n):
    s = input()
    stack = []
    buffer = []
    num= ''

    for char in s:
        if char.isnumeric() or char == '.':
            num += char
        else:
            if num:
                buffer.append(num)
                num= ''
            if char in '*/':
                while stack and stack[-1] in '*/':
                    buffer.append(stack.pop())
                stack.append(char)
            elif char in '+-':
                while stack and stack[-1] in '+-*/':
                    buffer.append(stack.pop())
                stack.append(char)
            elif char in '(':
                stack.append(char)
            elif char in ')':
                while stack[-1] in '+-*/':
                    buffer.append(stack.pop())
                stack.pop()
    if num:
        buffer.append(num)
    while stack:
        buffer.append(stack.pop())

    print(*buffer, sep = ' ')
