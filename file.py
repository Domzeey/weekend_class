file = open('fileio.txt', 'w')
file.write('hello world')
file.close


file = open('fileio.txt', 'r')
data = file.readlines()
for line in data:
    print(line)


file = open('fileio.txt', 'w')
file.write