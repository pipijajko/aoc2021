#There's one major catch - crab submarines can only move horizontally.
#Each change of 1 step in horizontal position of a single crab costs 1 fuel.

from collections import Counter
test_input_ = """
16,1,2,0,4,2,7,1,2,14
"""

import statistics
def fuel_for_target_pos1(hpos, initial_hpositions):
    return round(sum(abs(x - hpos) for x in initial_hpositions))

def fuel_for_target_pos2(hpos, initial_hpositions):
    distances = (abs(x - hpos) for x in initial_hpositions)
    return round(sum(d*(d+1) / 2 for d in distances))




def crab_submarines(source):
    initial_hpositions = list(map(int, source.split(",")))
    median = statistics.median(initial_hpositions)
    print(median)
    fuel = fuel_for_target_pos1(median, initial_hpositions)
    print(fuel)
    return fuel

def crab_submarines_triangle_number(source):
    initial_hpositions = list(map(int, source.split(",")))
    mean = round(statistics.mean(initial_hpositions))
    print(mean)
    fuel = fuel_for_target_pos2(mean, initial_hpositions)
    return fuel



# def crab_submarines_triangle_number(source):
#     "bruteforced :("
#     initial_hpositions = list(map(int, source.split(",")))
#     med = sorted(initial_hpositions)[(len(initial_hpositions) // 2)]
#     #fuel constumption is a triangle number
#     def fuel_for_target_pos(hpos):
#         distances = (abs(x - hpos) for x in initial_hpositions)
#         return sum(d*(d+1)*.5 for d in distances)
#     best_pos = med
#     visited = set()
#     increment = 1
#     go_left = best_pos +1
#     go_right = best_pos -1
#     no_imrpvement_epochs = 0
#     while True:
#         visited.add(best_pos)
#         current_fuel = fuel_for_target_pos(best_pos)
#         go_left = best_pos +1
#         go_right = best_pos -1
#         while go_left in visited:
#             go_left -= increment
#         while go_right  in visited:
#             go_right += increment
#         increment += 1
#         lfuel = fuel_for_target_pos(go_left)
#         rfuel = fuel_for_target_pos(go_right)
#         if lfuel < current_fuel:
#             best_pos = go_left
#             increment = 1
#             no_imrpvement_epochs = 0
#         if rfuel < current_fuel:
#             best_pos = go_right
#             increment = 1
#             no_imrpvement_epochs = 0
#         else:
#             no_imrpvement_epochs +=1

#         if no_imrpvement_epochs == 10:
#             break
#     print(fuel_for_target_pos(best_pos))
#     return fuel_for_target_pos(best_pos)



def main(filename):
    with open(filename) as fp:
        x = crab_submarines(fp.read())
        print("simple: ", x)
    with open(filename) as fp:
        xx = crab_submarines_triangle_number(fp.read())
        print("adv: ", xx)
    pass


if __name__ == "__main__":
    assert crab_submarines(test_input_) == 37
    assert crab_submarines_triangle_number(test_input_) == 168
    main("input.txt")
