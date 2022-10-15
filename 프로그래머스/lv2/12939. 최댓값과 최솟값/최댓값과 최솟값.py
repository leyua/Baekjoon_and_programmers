def solution(s):
    l = [int(i) for i in s.split()]
    return "{} {}".format(min(l),max(l))