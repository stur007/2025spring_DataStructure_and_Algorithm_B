t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    left = right = 0
    while True:
        if a != 1 and b!= 1:
            if a >b:
                left += a//b
                a = a%b
            elif b >a:
                right += b//a
                b = b%a
        else:
            if a == 1:
                right += b-1
                b =1
            else:
                left += a-1
                a= 1
        if a==b==1:
            print(f'Scenario #{i+1}:\n{left} {right}\n')
            break

# 不要被题目迷惑了，其实想想就可以发现，根本没有所谓的最短路径，都是单一的结果，直接逆向思维，模拟实现即可。