ls = []

for word in input().split():
    if word[-1] == 's':
        ls.append(word)
# print(ls)
print('_'.join(ls))
