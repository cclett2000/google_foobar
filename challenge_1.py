# Charles Lett Jr.
# 12/31/21
# Desc: python script containing code for 'Google FooBar' challenge

# import os
# import time

def solution(area):
    # clear powershell each run
    # os.system('cls' if os.name in ('nt', 'dos', 'window') else 'clear')

    # debug switch
    enable_debug = False
    show_roots = False

    roots = []                     # list to store sq_rt nums
    curr_rt = area                 # current num to test

    def sq_rt(num):
        return num*num

    # test roots
    while area > 0:
        # debug
        if enable_debug:
            db_sq_rt = sq_rt(curr_rt)
            print('Curr', curr_rt,
                  '\nsq_rt', db_sq_rt,
                  '\nArea', area,
                  '\n' + str(roots),
                  '\n' + '-'*33)

        if sq_rt(curr_rt) <= area:
            roots.append(sq_rt(curr_rt))
            area -= sq_rt(curr_rt)
            curr_rt = area

        if curr_rt > 1:
            curr_rt -= 1

        # time.sleep(0.5)     # slow debug display

    # debug
    if enable_debug:
        db_sq_rt = sq_rt(curr_rt)
        print('Curr', curr_rt,
              '\nsq_rt', db_sq_rt,
              '\nArea', area,
              '\n' + str(roots),
              '\n' + '-' * 33)

    if show_roots:
        print(str(roots))

    return roots

print(solution(15324))
