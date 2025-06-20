def compute_lps(s):
    lps = [0]*m
    for i in range(1, m):
        temp =  lps[i-1]
        while temp > 0 and s[i] != s[temp]:
            temp = lps[temp-1]
        if s[i] == s[temp]:
            temp += 1
        lps[i] = temp
    return lps

def max_t(s):
    lps = compute_lps(s)
    for i in range(m):
        if lps[i] != 0 and (i+1)%(i+1-lps[i]) == 0:
            k = (i+1)//(i+1-lps[i])
            print(i+1, k)
c = 0
while True:
    c += 1
    m = int(input())
    if m == 0:
        break
    print(f'Test case #{c}')
    max_t(input())
    print()