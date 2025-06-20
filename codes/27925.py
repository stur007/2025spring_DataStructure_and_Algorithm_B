from collections import deque

t = int(input())
group = {}
for i in range(t):
    members = list(input().split())
    for member in members:
        group[member] = i

mem_in_queue = {}
group_order = deque([])

while True:
    s = input()
    if 'ENQUEUE' in s:
        member = s[8:]
        if member in group:
            if group[member] in mem_in_queue:
                mem_in_queue[group[member]].append(member)
            else:
                mem_in_queue[group[member]] = deque([member])
                group_order.append(group[member])
        else:
            group_order.append(member)
    elif 'DEQUEUE' in s:
        if isinstance(group_order[0], str):
            print(group_order.popleft())
        else:
            num = group_order[0]
            print(mem_in_queue[num].popleft())
            if not mem_in_queue[num]:
                del mem_in_queue[num]
                group_order.popleft()
    else:
        break