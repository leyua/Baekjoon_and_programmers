import sys

input = sys.stdin.readline

c = int(input())
for i in range(c):
    scores = [int(score) for score in input().split()]
    n = scores.pop(0)
    avg = sum(scores) / n
    percent = len([x for x in scores if x > avg]) / n * 100
    print("{:.3f}%".format(percent))