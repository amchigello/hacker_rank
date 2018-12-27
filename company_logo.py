#!/bin/python3
from collections import Counter



if __name__ == '__main__':
    s = input()
    lits_s = list(s)
    s_counter = dict(Counter(list(s)))
    l1=[(y,x) for x,y in zip(s_counter.values(),s_counter.keys())]
    sorted_l1=sorted(l1,key=lambda x:(x[1]*-1,x[0]),reverse=False)
    for x in sorted_l1[:3]:
        print("{} {}".format(x[0],x[1]))
