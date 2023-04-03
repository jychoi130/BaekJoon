import sys

a = int(input())
for i in range(a):
    print(sum(map(int, sys.stdin.readline().split())))