import string

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

num_days = dict()

for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue

    if words[2] not in num_days:
        num_days[words[2]] = 1
    else:
        num_days[words[2]] += 1
print(num_days)
