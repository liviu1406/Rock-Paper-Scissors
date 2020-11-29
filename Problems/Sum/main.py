# read sums.txt
file = open('sums.txt', 'r')

for line in file:
    sum = int(line.split()[0]) + int(line.split()[1])
    print(sum)

file.close()
