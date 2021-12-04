from itertools import islice

test_input_ = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
""".split("\n")


def track_submarine(source):
    horizontal_position = 0
    depth = 0
    for cmd in source:
        cmd = cmd.strip()
        if not cmd:
            continue
        command, value = cmd.split()
        value = int(value)
        if command == "forward":
            horizontal_position += value
        elif command == "down":
            depth += value
        elif command == "up":
            depth -= value
            assert depth >= 0
    print(horizontal_position, depth)
    return horizontal_position * depth


def track_submarine_aim(source):
    horizontal_position = 0
    aim = 0
    depth = 0
    for cmd in source:
        cmd = cmd.strip()
        if not cmd:
            continue
        command, value = cmd.split()
        value = int(value)
        if command == "forward":
            horizontal_position += value
            depth += value * aim
        elif command == "down":
            aim += value
        elif command == "up":
            aim -= value
            assert aim >= 0
    print(horizontal_position, aim, depth)
    return horizontal_position * depth


def main(filename):
    with open(filename) as fp:
        position = track_submarine(fp)
        print("simple: ", position)
    with open(filename) as fp:
         position2 = track_submarine_aim(fp)
         print("aimed: ", position2)


if __name__ == "__main__":
    assert track_submarine(test_input_) == 150
    assert track_submarine_aim(test_input_) == 900
    main("input.txt")
