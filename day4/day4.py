from collections import Counter
test_input_ = """
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
""".split("\n")




def parse_boards(source):
    shots = None
    boards = []
    current_board = []
    for line  in source:
        line = line.strip()
        if not line:
            continue
        if "," in line:
            shots = [int(x) for x in line.split(',')]
        else:
            board_line = [int(x) for x in line.split()]
            current_board.append(board_line)
            if len(current_board) == 5:
                boards.append(current_board[:])
                current_board = []
    assert len(current_board) == 0
    assert all(len(b) == 5 for b in boards)
    return boards, shots


def check_shots_for_win(board_shots):
    for b_idx, shots in board_shots.items():
        xs = [x for x, y in shots]
        ys = [y for x, y in shots]
        for x in set(xs):
            if xs.count(x) >= 5:
                print("bingoo X", x, shots, b_idx)
                return b_idx
        for y in set(ys):
            if ys.count(y) >= 5:
                print("bingoo Y", y, shots, b_idx)
                return b_idx
    return None


from collections import defaultdict

def check_shots_for_win_last(board_shots):
    last_win = None
    for b_idx, shots in board_shots.items():
        xs = [x for x, y in shots]
        ys = [y for x, y in shots]
        for x in set(xs):
            if xs.count(x) >= 5:
                last_win = b_idx
        for y in set(ys):
            if ys.count(y) >= 5:
                last_win = b_idx
    return last_win


def play_bingo(source):
    boards, shots = parse_boards(source)
    board_shots = defaultdict(list)
    last_shot = None
    for shot in shots:
        last_shot = shot
        for b_idx, board in enumerate(boards):
            for y, bline in enumerate(board):
                if shot in bline:
                    x = bline.index(shot)
                    board_shots[b_idx].append((x, y))
        winner_idx = check_shots_for_win(board_shots)
        if winner_idx is not None:
            winboard = boards[winner_idx]
            shots = board_shots[winner_idx]
            print(winner_idx, winboard, shots)
            nonmarked_sum = 0
            for x in range(5):
                for y in range(5):
                    if (x,y) not in shots:
                        nonmarked_sum += winboard[y][x]
            print(nonmarked_sum, shot, nonmarked_sum*shot)
            return nonmarked_sum*shot
    assert False

def play_bingo_last_win(source):
    boards, shots = parse_boards(source)
    board_shots = defaultdict(list)
    last_shot = None
    winner_idx = None
    for shot in shots:
        print("sh", shot)
        for b_idx, board in enumerate(boards):
            for y, bline in enumerate(board):
                if shot in bline:
                    x = bline.index(shot)
                    board_shots[b_idx].append((x, y))
    winner_idx = check_shots_for_win_last(board_shots)
    if winner_idx:
        print("winner", winner_idx, shot)
        last_shot = shot

    board_shots = defaultdict(list) # reset
    for shot in shots:
        for b_idx, board in enumerate(boards):
            for y, bline in enumerate(board):
                if shot in bline:
                    x = bline.index(shot)
                    board_shots[b_idx].append((x, y))
        print("sh", shot)
        if shot == last_shot:
            break

    if winner_idx is not None:
        winboard = boards[winner_idx]
        shots = board_shots[winner_idx]
        print(winner_idx, winboard, shots)
        nonmarked_sum = 0
        for x in range(5):
            for y in range(5):
                if (x,y) not in shots:
                    nonmarked_sum += winboard[y][x]
        print(nonmarked_sum, last_shot, nonmarked_sum*last_shot)
        return nonmarked_sum*last_shot
    assert False


def main(filename):
    with open(filename) as fp:
        x = play_bingo(fp)
        print("simple: ", x)
    with open(filename) as fp:
        xx = play_bingo_last_win(fp)
        print("adv: ", xx)
    pass

if __name__ == "__main__":
    #assert play_bingo(test_input_) == 4512
    assert play_bingo_last_win(test_input_) == 1924
    main("input.txt")
