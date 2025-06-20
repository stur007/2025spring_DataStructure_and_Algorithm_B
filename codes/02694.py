s = input().split()

def f():
    op = s.pop(0)
    if op in '+-*/':
        return eval(str(f())+op+str(f()))
    return op
print(f'{f():.6f}')
