from collections import Counter
test_input_ = """
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
""".split("\n")


def track_bits(source):
    bit_lookup = Counter() #track '1' bits
    count = 0
    numbits = 0
    for binstr in source:
        binstr = binstr.strip()
        if not binstr:
            continue
        count +=1
        numbits = max(len(binstr), numbits)
        for i, bit in enumerate(binstr):
            if bit == "1":
                bit_lookup[i] += 1
    gamma = "" #most common bits
    epsilon = "" #least common bits
    for bit_n in range(numbits):
        ones =  bit_lookup[bit_n]
        if ones > count / 2:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    depsilon = int(epsilon,2)
    dgamma = int(gamma,2) 
    print(depsilon, dgamma, depsilon * dgamma)
    return depsilon * dgamma


def build_bit_lookup(binary_strings : list):
    set_bit_counter = Counter() #track '1' bits
    count = 0
    for binstr in binary_strings:
        binstr = binstr.strip()
        if not binstr:
            continue
        count +=1
        for i, bit in enumerate(binstr):
            set_bit_counter[i] +=1 if bit == "1" else 0
    def most_common(bit_position):
        ones =  bit_lookup[bit_position]
        return  '1'  if ones >= count / 2 else '0'
    return most_common


def track_bits_eliminate(source):
    source = [line.strip() for line in source if line.strip()]
    oxy_rating = source.copy()
    co2s_rating = source.copy()
    bit_n = 0
    while len(oxy_rating) > 1 or len(co2s_rating) > 1:
        oxy_common= build_bit_lookup(oxy_rating)
        co2_common= build_bit_lookup(co2s_rating)
        if len(oxy_rating) > 1:
            oxy_rating = [num for num in oxy_rating if num[bit_n] == oxy_common(bit_n)] #need to recalcualte lookup after each iter
        if len(co2s_rating) > 1:
            co2s_rating = [num for num in co2s_rating if num[bit_n] != co2_common(bit_n)]
        bit_n +=1
    assert len(oxy_rating) == 1, oxy_rating
    assert len(co2s_rating) == 1, co2s_rating
    doxy_rating = int(oxy_rating[0],2)
    dco2s_rating = int(co2s_rating[0],2) 
    return doxy_rating * dco2s_rating


def main(filename):
    with open(filename) as fp:
        x = track_bits(fp)
        print("simple: ", x)
    with open(filename) as fp:
        xx = track_bits_eliminate(fp)
        print("adv: ", xx)


if __name__ == "__main__":
    assert track_bits(test_input_) == 198
    assert track_bits_eliminate(test_input_) == 230
    main("input.txt")
