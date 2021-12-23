#Surely, each lanternfish creates a new lanternfish once every 7 days.
#So, you can model each fish as a single number that represents the number of days until it creates a new lanternfish.
#two more days for its first cycle.
#A lanternfish that creates a new fish resets its timer to 6, not 7 (because 0 is included as a valid timer value).
#The new lanternfish starts with an internal timer of 8 and does not start counting down until the next day.


test_input_ = """
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb |fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec |fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef |cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega |efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga |gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf |gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf |cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd |ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg |gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc |fgae cfgab fg bagce
""".split("\n")

from collections import defaultdict, Counter
#                0          1   2       3           4       5       6           7           8       9
digit_lookup = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdfeg" , "acf", "abcdefg", "abcdfg"]

n_segment_lookup = defaultdict(list)
for digit, segments in enumerate(digit_lookup):
    n_segments = len(segments)
    n_segment_lookup[n_segments].append(digit)
print(n_segment_lookup)

def digital_display(source):
    digit_count = 0
    #cleanup_input = lambda x:list(map(sorted, x))
    cleanup_input = lambda x: x
    signal_pattern = []
    output_digits = []
    for line in source:
        line = line.strip()
        if not line:
            continue
        raw_signal,_, raw_digits = line.partition('|')
        signal_pattern = cleanup_input(raw_signal.split())
        output_digits = cleanup_input(raw_digits.split())

        easy_digits = {}
        for n_seg, digits in n_segment_lookup.items():
            #easy
            if len(digits) == 1:
                patterns = [x for x in signal_pattern if len(x) == n_seg]
                easy_digits[digits[0]] = patterns[0]
        print(easy_digits)
        for output in output_digits:
            for digit, pattern in easy_digits.items():
                if pattern == output:
                    digit_count += 1
    print(digit_count)
    return digit_count
            
            





def main(filename):
    with open(filename) as fp:
        x = digital_display(fp)
        print("simple: ", x)
    with open(filename) as fp:
        xx = digital_display(fp)
        print("adv: ", xx)


if __name__ == "__main__":
    assert digital_display(test_input_) == 26
    main("input.txt")
