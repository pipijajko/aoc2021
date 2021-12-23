
import statistics
test_input_ = """
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
""".split("\n")



test_micro_input_ = """11111
19991
19191
19991
11111
""".split("\n")
from collections import deque


from pprint import pprint

def model_octopus_flashes(source, steps):
    lines = [li.strip() for li in source if li.strip()]
    matrix = []
    for row in lines:
        r = [int(x) for x in row]
        matrix.append(r)
    rows_n = len(matrix)
    cols_n = len(matrix[0])
    inc = lambda x: (x+1) % 10
    flashed = deque()
    
    first_sync_flash = None
    number_of_flashes = 0
    def update(y,x):
        new_v = matrix[y][x] = inc(matrix[y][x])
        if new_v == 0:
            flashed.append((y,x))
            return True
        else:
            return False

    for step_n in range(steps):
        step_flashes = 0
        # Increase energy levels
        for y in range(rows_n):
            for x in range(cols_n):
                if update(y,x):
                    step_flashes += 1

        print(f"initial flashed: {flashed}, {number_of_flashes}")

        while len(flashed):
            y,x = flashed.popleft()
            
            can_move_up =(y > 0 and matrix[y-1][x] != 0)
            can_move_down =(y < rows_n-1 and matrix[y+1][x] != 0)
            can_move_left = (x > 0 and matrix[y][x-1] != 0)
            can_move_right = (x < cols_n-1 and matrix[y][x+1] != 0)

            can_move_up_left = (y > 0 and x > 0 and matrix[y-1][x-1] != 0)
            can_move_down_left = (y < rows_n-1  and x > 0 and matrix[y+1][x-1] != 0)
            can_move_up_right = (y > 0  and x < cols_n-1  and matrix[y-1][x+1] != 0)
            can_move_down_right = (y < rows_n-1 and x < cols_n-1 and matrix[y+1][x+1] != 0)

            if can_move_up and update(y-1, x):
                step_flashes +=1
            if can_move_down and update(y+1, x):
                step_flashes +=1
            if can_move_left and update(y, x-1):
                step_flashes +=1
            if can_move_right and update(y, x+1):
                step_flashes +=1

            if can_move_up_left and update(y-1, x-1):
                step_flashes+=1
            if can_move_down_left and update(y+1, x-1):
                step_flashes +=1
            if can_move_up_right and update(y-1, x+1):
                step_flashes +=1
            if can_move_down_right and update(y+1, x+1):
                step_flashes +=1
        
        print("step_n", step_n, step_flashes)
        number_of_flashes += step_flashes
        if step_flashes == cols_n * rows_n and first_sync_flash is None:
            first_sync_flash = step_n + 1
            break

    print(number_of_flashes, first_sync_flash)
    return number_of_flashes, first_sync_flash







def main(filename):
    with open(filename) as fp:
        x, y = model_octopus_flashes(fp, 100)
        print("simple: ", x)
    with open(filename) as fp:
        x, y = model_octopus_flashes(fp, 999999999999)
        print("adv: ", y)
    

if __name__ == "__main__":
    assert model_octopus_flashes(test_input_, 100)[0] == 1656
    assert model_octopus_flashes(test_input_, 200)[1] == 195
    main("input.txt")
