nums = int(input())
letters = []

for i in range(1072, 1072 + nums):
    if i > 1103:
        break
    letters += [chr(i)]

print(letters)
