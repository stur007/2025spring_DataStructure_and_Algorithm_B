def f(x):
    return x**3-5*x**2+10*x-80
def df(x):
    return 3*x**2-10*x+10
x_in = 5
x_out = 0
while abs(x_in-x_out)>10**(-9):
    x_in = x_out
    x_out = x_in -f(x_in)/df(x_in)
print(f'{x_out:.9f}')