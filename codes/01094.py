from collections import defaultdict, deque
from copy import deepcopy

while True:
    try:
        n, m = map(int, input().split())
    except EOFError:
        break
    in_degrees = dict()
    children = defaultdict(list)

    def topological_sort(in_degrees, children):
        temp = deque([])
        final = []
        flag = True
        temp_degrees =  deepcopy(in_degrees)
        for node in temp_degrees:
            if temp_degrees[node] == 0:
                temp.append(node)
        if len(temp) > 1:
            flag = False
        while temp:
            s = len(temp)
            for _ in range(s):
                node = temp.popleft()
                final.append(node)
                for child in children[node]:
                    temp_degrees[child] -= 1
                    if temp_degrees[child] == 0:
                        temp.append(child)
            if len(temp) > 1:
                flag = False
        if len(final) < len(temp_degrees):
            return -1
        if not flag:
            return 0
        return final

    for k in range(m):
        s = input()
        father = s[0]
        child = s[-1]
        in_degrees[child] = in_degrees.get(child, 0)+1
        in_degrees[father] = in_degrees.get(father, 0)
        children[father].append(child)
        ans = topological_sort(in_degrees, children)
        if ans == -1:
            print(f'Inconsistency found after {k+1} relations.')
            for _ in range(m-k-1):
                input()
            break
        elif ans == 0:
            if k == m-1:
                print(f'Sorted sequence cannot be determined.')
            else:
                continue
        else:
            if len(ans) < n:
                if k == m-1:
                    print(f'Sorted sequence cannot be determined.')
                    break
                else:
                    continue
            print(f'Sorted sequence determined after {k+1} relations: {"".join(ans)}.')
            for _ in range(m-k-1):
                input()
            break
