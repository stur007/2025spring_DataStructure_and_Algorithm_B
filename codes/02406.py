def compute_lps(s):
    m = len(s)
    lps = [0]*m
    for i in range(1, m):
        temp =  lps[i-1]
        while temp > 0 and s[i] != s[temp]:
            temp = lps[temp-1]
        if s[i] == s[temp]:
            temp += 1
        lps[i] = temp
    return m, lps

def max_t(s):
    m, lps = compute_lps(s)
    if lps[-1] == 0:
        return 1
    if m%(m-lps[-1])!= 0:
        return 1
    return m//(m-lps[-1])

while True:
    s = input()
    if s == '.':
        break
    print(max_t(s))