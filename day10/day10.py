
import statistics
test_input_ = """
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]
""".split("\n")


# NESTING_MAP = {
#     ")" : "(",
#     "}" : "{",
#     "]" : "[",
#     ">" : "<",
# }

NESTING_MAP = {
    "(" : ")",
    "{" : "}",
    "[" : "]",
    "<" : ">",
}
#NESTING_OPENING = set(NESTING_MAP.keys())


CORRUPTED_LINE_POINTS={
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}


INCOMPLETE_LINE_POINTS = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def find_corrupted_lines(source):
    lines = (li.strip() for li in source if li.strip())
    corruption_points = 0
    completion_points = []
    for line in lines:
        stack = []
        line_compl_pts = 0
        is_corrupted=False
        for ch in line:
            if ch in NESTING_MAP.keys():
                stack.append(ch)
            else:
                last = stack.pop()
                expected_ch = NESTING_MAP[last]
                if expected_ch != ch:
                    corruption_points += CORRUPTED_LINE_POINTS[ch]
                    is_corrupted = True
                    break
        if not is_corrupted:
            print(line)
            for opened_nesting in stack[::-1]:
                closing_ch = NESTING_MAP[opened_nesting]
                print("INCOMPLETE_LINE_POINTS", closing_ch, INCOMPLETE_LINE_POINTS[closing_ch])
                line_compl_pts = (5*line_compl_pts) + INCOMPLETE_LINE_POINTS[closing_ch]
            print("compl pts", line_compl_pts)
            completion_points.append(line_compl_pts)
    print(statistics.median(completion_points))
    print(corruption_points, completion_points)
    return corruption_points, statistics.median(completion_points)





def main(filename):
    with open(filename) as fp:
        x , xx = find_corrupted_lines(fp)
        print("simple: ", x)
        print("adv: ", xx)
    

if __name__ == "__main__":
    assert find_corrupted_lines(test_input_) == (26397, 288957)
    main("input.txt")
