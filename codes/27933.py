n = int(input())
boxes = []
temp = 0
cnt = 0
for _ in range(2*n):
    s = list(input().split())
    if s[0] == 'add':
        boxes.append(int(s[1]))
    elif s[0] == 'remove':
        if boxes[-1] == temp+1:
            boxes.pop()
            temp += 1
        else:
            boxes.sort(reverse = True)
            boxes.pop()
            temp += 1
            cnt += 1
print(cnt)