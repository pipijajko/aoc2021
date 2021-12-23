#Surely, each lanternfish creates a new lanternfish once every 7 days.
#So, you can model each fish as a single number that represents the number of days until it creates a new lanternfish.
#two more days for its first cycle.
#A lanternfish that creates a new fish resets its timer to 6, not 7 (because 0 is included as a valid timer value).
#The new lanternfish starts with an internal timer of 8 and does not start counting down until the next day.


from collections import Counter
test_input_ = """
3,4,3,1,2
"""



def lanternfish_repro_coalesce_timers(source, days=80):
    initial_timers = list(map(int, source.split(",")))
    timer_state = Counter(initial_timers)
    for _ in range(days):
        new_timer_state = Counter()
        for timer_state, timer_count in timer_state.items():
            timer_state -= 1
            if timer_state < 0:
                # reset internal clock of current fish = 6
                # create new lanternfish with initial clock of 8
                new_timer_state[6] += timer_count
                new_timer_state[8] += timer_count
            else:
                new_timer_state[timer_state] += timer_count
        timer_state = new_timer_state
    print(sum(timer_state.values()))
    return sum(timer_state.values())





def main(filename):
    with open(filename) as fp:
        x = lanternfish_repro_coalesce_timers(fp.read(), days=80)
        print("simple: ", x)
    with open(filename) as fp:
        xx = lanternfish_repro_coalesce_timers(fp.read(), days=256)
        print("adv: ", xx)


if __name__ == "__main__":
    assert lanternfish_repro_coalesce_timers(test_input_, 80) == 5934
    assert lanternfish_repro_coalesce_timers(test_input_, 256) == 26984457539
    main("input.txt")
