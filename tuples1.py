fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

num_addresses = dict()
most_commits = list() #(email, count)

for lines in fhand:
    words = lines.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    
    if words[1] not in num_addresses:
        num_addresses[words[1]] = 1
    else:
        num_addresses[words[1]] += 1

for key, val in num_addresses.items():
    most_commits.append((key, val))

most_commits.sort(reverse=True)

for key, val in most_commits[:1]:
    print(key, val)