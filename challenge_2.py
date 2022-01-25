from itertools import permutations

def solution(num_list):
    best = []
    p_val = 0

    for i in range(len(num_list) + 1):
        for p in permutations(num_list, i):
            if len(p) > 0:
                p_val = int(''.join(map(str, p[:len(p)])))

            if len(num_list) == 0:
                break

            if p_val % 3 == 0:
                best.append(p_val)

    best.sort(reverse=True)

    return best[0]