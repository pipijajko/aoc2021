
test_input_ = """
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
""".split("\n")


def parse_input(source):
    source = [li.strip() for li in source if li.strip()]
    rules = {}
    init = None
    for li in source:
        if "->" in li:
            pair,_, insertion = map(lambda x: x.strip(), li.partition("->"))
            assert pair not in rules
            rules[pair] = insertion
        else:
            assert init == None
            init = li
    assert init and rules
    return init, rules

from collections import Counter, defaultdict
def polymerize(init : str, rules : dict, steps = 10):
    polymer = init
    for i in range(steps):
        new_polymer = polymer
        inserts = 0
        for j in range(1, len(polymer)):
            pair = polymer[j-1:j+1]
            if pair in rules:
                new_polymer =f"{new_polymer[:j+inserts]}{rules[pair]}{new_polymer[j+inserts:]}"
                inserts +=1                #print(new_polymer)
        polymer = new_polymer
    return polymer

def pairwise(s):
    for i in range(1, len(s)):
        yield s[i-1:i+1]


def polymerization_step(cc, rules):
    ncc = defaultdict(int)
    for pair, insert in rules.items():
        cnt = cc[pair]
        if cnt > 0:
            newpair1, newpair2 = pair[0]+insert, insert+pair[1]
            ncc[newpair1] += cnt 
            ncc[newpair2] += cnt 
    return ncc


def wrap_polymeryzation(source, steps=10):
    init, rules = parse_input(source)
    cc = Counter(pairwise(init))
    print(cc)
    for _ in range(steps):
        cc = polymerization_step(cc, rules)
        print(cc)

    counts = defaultdict(int)
    for pair, count in cc.items():
        counts[pair[0]] += count
        counts[pair[1]] += count
    counts = {l:((c+1)// 2) if (c % 2) else (c // 2) for l,c in counts.items()}
    print(counts)
    max_v, min_v = max(counts.values()), min(counts.values())
    print(max_v - min_v, max_v, min_v, cc)
    return max_v - min_v



# def wrap_polymeryzation(source, steps=10):
#     init, rules = parse_input(source)
#     polymer =  polymerize(init, rules, steps)
#     cc = Counter(polymer)
#     max_v, min_v = max(cc.values()), min(cc.values())
#     print(max_v - min_v, max_v, min_v, cc)
#     return max_v - min_v


def main(filename):
    with open(filename) as fp:
        x= wrap_polymeryzation(fp, 10)
        print("simple: ", x)
    with open(filename) as fp:
        y=wrap_polymeryzation(fp, 40)
        print("adv: ", y)
    

if __name__ == "__main__":
    assert wrap_polymeryzation(test_input_, 10) == 1588
    assert wrap_polymeryzation(test_input_, 40) == 2188189693529
    main("input.txt")
