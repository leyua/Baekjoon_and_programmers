fixed_cost, variable_cost, price = map(int, input().split())
if variable_cost >= price:
    n = -1
else:
    n = fixed_cost // (price - variable_cost) + 1
print(n)