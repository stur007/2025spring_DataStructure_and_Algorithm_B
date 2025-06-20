from collections import defaultdict
import heapq
import math

xi, yi, xe, ye = map(int, input().split())
stops = defaultdict(list)

def distance(a, b):
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

while True:
    try:
        s = list(map(int, input().split()))[:-2]
    except EOFError:
        break
    xo = s[0]
    yo = s[1]
    for i in range(1, len(s)//2):
        xn = s[2*i]
        yn = s[2*i+1]
        stops[(xo, yo)].append(((xn, yn), 0.25))
        stops[(xn, yn)].append(((xo, yo), 0.25))
        xo = xn
        yo = yn

def dijkstra():
    times = {(xi, yi): 0, (xe, ye):float('inf')}
    q = [(0, (xi, yi))]
    stops[(xi, yi)].append(((xe, ye), 1))
    for stop in stops:
        if stop != (xi, yi):
            times[stop] = float('inf')
            stops[(xi, yi)].append((stop, 1))
            stops[stop].append(((xe, ye), 1))
        for other_stop in stops:
            stops[stop].append((other_stop, 1))
            stops[other_stop].append((other_stop, 1))
    while q:
        time_o, stop_o = heapq.heappop(q)
        if stop_o == (xe, ye):
            return round(time_o/10000*60)
        if time_o > times[stop_o]:
            continue
        for stop, scale in stops[stop_o]:
            time_n = time_o + math.sqrt((stop[0]-stop_o[0])**2+(stop[1]-stop_o[1])**2)*scale
            if time_n < times[stop]:
                times[stop] = time_n
                heapq.heappush(q, (time_n, stop))

print(dijkstra())