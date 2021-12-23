from collections import Counter
test_input_ = """
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
""".split("\n")




# def hydrotermal_vents(source):
#     source = (line.strip() for line in source if line.strip())
#     heatmap = Counter()
#     for line in source:
#         if not line:
#             continue
#         begin, end = line.split(" -> ")
#         x0,y0 = map(int, begin.split(","))
#         x1,y1 = map(int, end.split(","))

#         #straight lines only:
#         if x0 == x1 or y0 == y1:
#             for x in range(min(x0,x1), max(x0,x1)+1):
#                 for y in range(min(y0, y1), max(y0,y1)+1):
#                     heatmap[(x,y)] += 1
#     #print(heatmap)
#     overlap_n = sum(1 for count  in heatmap.values() if count > 1)
#     print(overlap_n)
#     return overlap_n


def hydrotermal_vents(source, enable_diagonals=False):
    source = (line.strip() for line in source if line.strip())
    heatmap = Counter()
    for line in source:
        if not line:
            continue
        begin, end = line.split(" -> ")
        x0,y0 = map(int, begin.split(","))
        x1,y1 = map(int, end.split(","))

        #straight lines only:
        if x0 == x1 or y0 == y1:
            for x in range(min(x0,x1), max(x0,x1)+1):
                for y in range(min(y0, y1), max(y0,y1)+1):
                    heatmap[(x,y)] += 1
        elif enable_diagonals:
            xd = 1 if x0 < x1 else -1
            yd = 1 if y0 < y1 else -1
            steps_n = max(x0,x1) - min(x0,x1) 
            for i in range(steps_n+1):
                x = x0 + xd * i
                y = y0 + yd * i
                heatmap[(x,y)] +=1
    overlap_n = sum(1 for count  in heatmap.values() if count > 1)
    print(overlap_n)
    return overlap_n


def main(filename):
    with open(filename) as fp:
        x = hydrotermal_vents(fp, False)
        print("simple: ", x)
    with open(filename) as fp:
        xx = hydrotermal_vents(fp, True)
        print("adv: ", xx)


if __name__ == "__main__":
    assert hydrotermal_vents(test_input_) == 5
    assert hydrotermal_vents(test_input_, True) == 12
    main("input.txt")
