
from collections import Counter
test_input_ = """
2199943210
3987894921
9856789892
8767896789
9899965678
""".split("\n")

#Each number corresponds to the height of a particular location, where 9 is the highest and 0 is the lowest a location can be.
#Your first goal is to find the low points - the locations that are lower than any of its adjacent locations. Most locations have four adjacent locations (up, down, left, and right); 
# locations on the edge or corner of the map have three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)
def gas_heightmap(source):
    risks = []
    hmap = []
    lines = (li.strip() for li in source if li.strip())
    for line in lines:
        row = [int(x) for x in line]
        hmap.append(row)
    rows_n = len(hmap)
    cols_n = len(hmap[0])
    for y in range(rows_n):
        for x in range(cols_n):
            v = hmap[y][x]
            if y > 0 and hmap[y-1][x] <= v:
                continue
            if y < rows_n-1 and hmap[y+1][x] <= v:
                continue
            if x > 0 and hmap[y][x-1] <= v:
                continue
            if x < cols_n-1 and hmap[y][x+1] <= v:
                continue
            risk = v+1
            risks.append(risk)
    print(risks)
    print(sum(risks))
    return(sum(risks))

#Next, you need to find the largest basins so you know what areas are most important to avoid.
#A basin is all locations that eventually flow downward to a single low point. 
# Therefore, every low point has a basin, although some basins are very small. Locations of height 9 do not count as being in any basin, and all other locations will always be part of exactly one basin.
#The size of a basin is the number of locations within the basin, including the low point. The example above has four basins.




def gas_basins(source):
    basins = []
    hmap = []
    lines = (li.strip() for li in source if li.strip())
    for line in lines:
        row = [int(x) for x in line]
        hmap.append(row)
    rows_n = len(hmap)
    cols_n = len(hmap[0])

    def dfs(y, x, visited):
        visited.add((y,x))
        v = hmap[y][x]
        if v == 9:
            return 0
        bsize = 1
        if y > 0 and hmap[y-1][x] > v:
            if (y-1, x) not in visited:
                bsize += dfs(y-1, x,visited)
        if y < rows_n-1 and hmap[y+1][x] > v:
            if (y+1, x) not in visited:
                bsize += dfs(y+1, x, visited)
        if x > 0 and hmap[y][x-1] > v:
            if (y, x-1) not in visited:
                bsize += dfs(y, x-1, visited)
        if x < cols_n-1 and hmap[y][x+1] > v:
            if (y, x+1) not in visited:
                bsize += dfs(y, x+1, visited)
        return bsize

    for y in range(rows_n):
        for x in range(cols_n):
            visited = set()
            basinsize = dfs(y,x, visited)
            if basinsize > 1:
                basins.append(basinsize)

    sorted_basins = sorted(basins, reverse=True)
    print(sorted_basins)
    print(sorted_basins[:3])

    return sorted_basins[0] * sorted_basins[1] * sorted_basins[2]






def main(filename):
    with open(filename) as fp:
        x = gas_heightmap(fp)
        print("simple: ", x)
    with open(filename) as fp:
        xx = gas_basins(fp)
        print("adv: ", xx)


if __name__ == "__main__":
    assert gas_heightmap(test_input_) == 15
    assert gas_basins(test_input_) == 1134
    main("input.txt")
