fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()


dictionary_hours = dict()              
lst = list()
for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue

    col_pos = words[5].find(':')
    hour = words[5][:col_pos]
    if hour not in dictionary_hours:
        dictionary_hours[hour] = 1      
    else:
        dictionary_hours[hour] += 1     

for key, val in list(dictionary_hours.items()):
    lst.append((key, val))             
lst.sort()                              

for key, val in lst:
    print(key, val)
    