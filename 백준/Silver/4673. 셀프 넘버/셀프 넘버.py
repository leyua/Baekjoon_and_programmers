def self_number(n):
    nums = list(range(1, n + 1))
    for i in range(1, n + 1):
        total = i + i // 1000 + i % 1000 // 100 + i % 100 // 10 + i % 10
        if total in nums:
            nums.remove(total)
    for num in nums:
        print(num)


self_number(10000)
