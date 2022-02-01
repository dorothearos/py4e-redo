dictionary_addresses = dict()
maximum = 0
maximum_address = ''

fname = input('Enter file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        if words[1] not in dictionary_addresses:
            dictionary_addresses[words[1]] = 1
        else:
            dictionary_addresses[words[1]] += 1

for address in dictionary_addresses:
    if dictionary_addresses[address] > maximum:
        maximum = dictionary_addresses[address]
        maximum_address = address

print(maximum_address, maximum)
