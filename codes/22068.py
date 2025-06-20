x = input()
while True:
    try:
        s = input()
    except EOFError:
        break
    i = 0
    j = 0
    stack = []
    while i < len(x):
        stack.append(x[i])
        i += 1
        while stack and j < len(s) and stack[-1] == s[j]:
            stack.pop()
            j += 1
    if j == len(x):
        print('YES')
    else:
        print('NO')