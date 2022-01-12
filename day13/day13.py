
test_input_ = """
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
""".split("\n")

# Then, there is a list of fold instructions.
# Each instruction indicates a line on the transparent paper
# and wants you to fold the paper up (for horizontal y=... lines) or left (for vertical x=... lines).

def fold(points, axis, fold_coord):
    for x,y in points:
        if axis == "y":
            assert y != fold_coord
            if y < fold_coord:
                yield x,y
            else:
                yield x, fold_coord - (y - fold_coord)
        elif axis == "x":
            assert x != fold_coord
            if x < fold_coord:
                yield x,y
            else:
                yield fold_coord - (x - fold_coord), y
        else:
            assert False, f"({x},{y}),{axis}={fold_coord}"


def parse_input(source):
    source = [li.strip() for li in source if li.strip()]
    commands = []
    dots = []
    for li in source:
        if li.startswith("fold along"):
            li = li.replace("fold along ", '')
            axis, coord = li.strip().split("=")
            commands.append((axis, int(coord)))
        else:
            x,y = map(int,li.split(","))
            dots.append((x,y))
    return dots, commands

def fold_transparent_paper(source, folds_n = 1):
    dots, commands = parse_input(source)
    for axis, coord in commands[:folds_n]:
        dots = set(fold(dots, axis, coord))
    print(len(dots))
    if folds_n == None:
        display_dots(dots)
    return len(dots)

def display_dots(dots):
    maxx = max(dots, key=lambda p:p[0])[0]
    maxy = max(dots, key=lambda p:p[1])[1]
    matrix = [[' ']*(maxx+1) for y in range(maxy+1)]
    for x,y in dots:
        matrix[y][x] = "#"
    rows = [''.join(r) for r in matrix]
    for row in rows:
        print(row)

def main(filename):
    with open(filename) as fp:
        x= fold_transparent_paper(fp)
        print("simple: ", x)
    with open(filename) as fp:
        y=fold_transparent_paper(fp, None)
        print("adv: ", y)
    

if __name__ == "__main__":
    assert fold_transparent_paper(test_input_) == 17
    #assert fold_transparent_paper(test_input_, None) == 17
    main("input.txt")
