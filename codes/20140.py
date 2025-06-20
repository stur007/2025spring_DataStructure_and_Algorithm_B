s = input()
num = ''
temp = ''
stack = []
for i in range(len(s)):
    if s[i].isalpha() or s[i] == '[':
        if num != '':
            stack.append(int(num))
            num = ''
        stack.append(s[i])
    elif s[i].isnumeric():
        num += s[i]
    elif s[i] == ']':
        temp = ''
        while not isinstance(stack[-1], int) and stack[-1] != '[':
            temp = stack.pop() + temp
        if stack[-1] != '[':
            temp = stack.pop() * temp
        stack.pop()
        stack.append(temp)
print(*stack, sep='')