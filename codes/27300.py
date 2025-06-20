from collections import defaultdict
import re

models = defaultdict(list)
n = int(input())

for _ in range(n):
    s = input()
    match = re.match(r'^(.*)-(.*)$', s)
    if match:
        prefix, suffix = match.groups()
        models[prefix].append(suffix)

for name in sorted(models):
    sizes = sorted(models[name], key=lambda x: (x[-1], -float(x[:-1])), reverse=True)
    print(f"{name}: {', '.join(sizes)}")

    # gpt提供的代码看起来更简洁些！