import sys
input = sys.stdin.readline

n = "{:02d}".format(int(input()))
operand = n
result = ""
cycle = 0
while n != operand or cycle == 0:
    cycle += 1
    result = str(int(operand[0]) + int(operand[1]))
    operand = operand[-1] + result[-1]
print(cycle)