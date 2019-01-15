import itertools

a=map(int,input().split(' '))
b=map(int,input().split(' '))

print(*sorted(list(itertools.product(a,b))))
