def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    for i in range(1, m):
        length = lps[i-1]
        while length > 0 and pattern[length] != pattern[i]:
            length = lps[length-1]
        if pattern[i] == pattern[length]:
            length += 1
        lps[i] = length
    return lps

def kmp_search(text, pattern):
    lps = compute_lps(pattern)
    j = 0
    m = len(pattern)
    n = len(text)
    match = []
    for i in range(n):
        while j > 0 and pattern[j] != text[i]:
            j = lps[j-1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            match.append(i-j+1)
            j = lps[j-1]
    return match

text = "ABABABABCABABABABCABABABABC"
pattern = "ABABCABAB"
index = kmp_search(text, pattern)
print("pos matched：", index)