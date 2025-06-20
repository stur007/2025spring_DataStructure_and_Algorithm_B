n, m, s, v = input().split()
n, m, s, v= int(n), int(m), int(s)-1, float(v)
bank = []
for _ in range(m):
    a, b, rab, cab, rba, cba = input().split()
    bank.append((int(a)-1, int(b)-1, float(rab), float(cab), float(rba), float(cba)))
money = [0]*n
money[s] = v
for _ in range(n-1):
    for a, b, rab, cab, rba, cba in bank:
        if money[b] < (money[a]-cab)*rab:
            money[b] = (money[a]-cab)*rab
        if money[a] < (money[b]-cba)*rba:
            money[a] = (money[b] - cba) * rba

for a, b, rab, cab, rba, cba in bank:
    if money[a] - cab >= 0 and money[b] < (money[a] - cab) * rab:
        print("YES")
        break
    if money[b] - cba >= 0 and money[a] < (money[b] - cba) * rba:
        print("YES")
        break
else:
    print("NO")