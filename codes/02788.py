import math
def cnt_nodes(root, end):
    RootFloor = int(math.log(root, 2))
    EndFloor = int(math.log(end, 2))
    if RootFloor == EndFloor:
        return 1
    floors = EndFloor - RootFloor
    ans = 2**floors-1
    begin_number = root * 2**floors
    end_number = (root+1)*2**floors-1
    if end >= begin_number:
        ans += min(end, end_number)-begin_number+1
    return ans
while True:
    a, b = map(int, input().split())
    if (a, b) == (0, 0):
        break
    print(cnt_nodes(a, b))