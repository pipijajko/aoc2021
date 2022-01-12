test_input_ = """
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
""".split("\n")




import heapq

def parse_input(source):
    source = [li.strip() for li in source if li.strip()]
    risk_map = []
    for li in source:
        risk_map.append([int(i) for i in li])
    return risk_map


def print_riskmap(rmap, expand_n):
    maxy, maxx = len(rmap) * expand_n, len(rmap[-1]) * expand_n
    for y in range(maxy):
        for x in range(maxx):
            value = vcost(rmap, ((None), (y,x)))
            print(value, end='')
        print("")

def vcost(rmap, path):
    maxy, maxx = len(rmap), len(rmap[-1])
    sum_= 0
    for y,x in path[1:]:
        increment_x = x // maxx
        idx_x = x % maxx
        increment_y = y // maxy
        idx_y = y % maxy
        val = ((rmap[idx_y][idx_x] -1 + increment_x + increment_y) % 9) + 1
        sum_ += val
    return sum_

def dijkstra(rmap, expand_n=1):
    INFINITY = float('inf')
    assert expand_n > 0
    maxy, maxx = len(rmap) * expand_n, len(rmap[-1]) * expand_n
    target =(maxy-1, maxx-1)
    source=(0,0)
    dist, prev = {}, {}
    Q = set()
    for y in range(maxy):
        for x in range(maxx):
            v = (y,x)
            dist[v] = INFINITY
            prev[v] = None
            Q.add(v)
    dist[source] = 0
    while Q:
        u = min(Q, key=lambda x:dist[x])
        Q.remove(u)
        if u == target:
            break #terminate search
        uy, ux = u
        neighbors = [(uy+1, ux), (uy, ux+1), (uy, ux-1), (uy-1, ux)]
        neighbors = [(y,x) for y,x in neighbors if 0 <= x < maxx and 0 <= y < maxy and (y,x) in Q]
        for v in neighbors:
            alt = dist[u] + vcost(rmap, (u,v))
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
    
    shortest_path = []
    u = target
    if prev[u] is not None or u == source:
        while u is not None:
            shortest_path.insert(0, u)
            u = prev[u]

    print(shortest_path, vcost(rmap, shortest_path))
    return vcost(rmap, shortest_path)





def dijkstra_opt(rmap, expand_n=1):
    INFINITY = float('inf')
    assert expand_n > 0
    maxy, maxx = len(rmap) * expand_n, len(rmap[-1]) * expand_n
    target = (maxy-1, maxx-1)
    source = (0,0)
    dist, prev = {}, {} #dist is for quick lookup
    open_, closed_ = [], set()
    for y in range(maxy):
        for x in range(maxx):
            v = (y,x)
            #item = (0 if v == source else INFINITY, v)
            #heapq.heappush(open_, item)
            #dist[v] = INFINITY
            #prev[v] = None
    dist[source] = 0
    heapq.heappush(open_, (0, source))

    while open_:
        item = heapq.heappop(open_)
        dist_u, u = item
        assert dist_u != INFINITY
        closed_.add(u) #add to visited vertex lookup
        if u == target:
            break #terminate search
        uy, ux = u
        neighbors = [(uy+1, ux), (uy, ux+1), (uy, ux-1), (uy-1, ux)]
        neighbors = [(y,x) for y,x in neighbors if 0 <= x < maxx and 0 <= y < maxy and (y,x) not in closed_]
        for v in neighbors:
            dist_v =  INFINITY if v not in dist else dist[v]
            alt = dist_u + vcost(rmap, (u,v))
            if alt < dist_v:
                find = [it for it in open_ if it[1] == v]
                if find:
                    assert False
                    open_.remove((dist_v, v))
                    heapq.heapify(open_)
                heapq.heappush(open_, (alt, v))
                dist[v] = alt
                prev[v] = u
    shortest_path = []
    u = target
    if u in prev or u == source:
        while u is not None:
            shortest_path.insert(0, u)
            u = prev[u] if u in prev else None

    print(shortest_path, vcost(rmap, shortest_path))
    return vcost(rmap, shortest_path)
def cave_navigation_dijkstra(source, expand_n=1):
    rmap = parse_input(source)
    #print_riskmap(rmap, expand_n)
    return dijkstra_opt(rmap, expand_n)



def main(filename):
    with open(filename) as fp:
        x= cave_navigation_dijkstra(fp)
        print("simple: ", x)
    with open(filename) as fp:
        xx= cave_navigation_dijkstra(fp, 5)
        print("adv: ", xx)

if __name__ == "__main__":
    assert cave_navigation_dijkstra(test_input_) == 40
    assert cave_navigation_dijkstra(test_input_, 5 ) == 315
    main("input.txt")
