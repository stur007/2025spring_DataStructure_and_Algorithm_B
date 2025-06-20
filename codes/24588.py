n = int(input())
for _ in range(n):
    s = list(input().split())
    def cal():
        char = s.pop()
        if char in '+-*/':
            s1 = cal()
            s2 = cal()
            return str(eval(s2+char+s1))
        else:
            return char
    print('%.2f' % float(cal()))