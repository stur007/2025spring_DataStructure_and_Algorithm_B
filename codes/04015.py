import re
pattern = r'^[^@.][^@]*[^@.]@[^@.][^@.]*\.[^@]*[^@.]$'
while True:
    try:
        s = (input())
    except EOFError:
        break
    if re.match(pattern, s):
        print('YES')
    else:
        print('NO')