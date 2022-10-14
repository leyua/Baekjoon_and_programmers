word = input().upper()
s = ""
n = 0
checked = []
for alphabet in word:
    if not alphabet in checked:
        checked.append(alphabet)
        if word.count(alphabet) > n:
            n = word.count(alphabet)
            s = alphabet
        elif word.count(alphabet) == n:
            s = "?"
print(s)