from itertools import islice

test_input_ = """
199
200
208
210
200
207
240
269
260
263
""".split()


def count_increases_simple(source):
    increases = 0
    prev_depth = None
    for line in source:
        depth = int(line.strip())
        if prev_depth is not None:
            increases += 1 if prev_depth < depth else 0
        prev_depth = depth
    return increases


def window_maker(iterable, n=3):
    iterator = iter(iterable)
    current_window = tuple(islice(iterator, n))
    if len(current_window) == n:
        yield current_window
    for item in iterator:
        current_window = current_window[1:] + (item,)
        yield current_window
    

def count_increases_sliding(source, window_size = 3):
    prev_window = None
    increases = 0
    number_source = (int(x) for x in source)
    for window in window_maker(number_source, window_size):
        if prev_window is not None:
            increases += 1 if sum(window) > sum(prev_window) else 0
        prev_window = window
    return increases



    

def main(filename):
    with open(filename) as fp:
        increases1 = count_increases_simple(fp)
        print("simple: ", increases1)
    with open(filename) as fp:
        increases2 = count_increases_sliding(fp)
        print("sliding: ", increases2)


if __name__ == "__main__":
    assert count_increases_simple(test_input_) == 7
    assert count_increases_sliding(test_input_) == 5
    main("input.txt")
