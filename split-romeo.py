<!------*

fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
words=[]
for line in fhand:
    for word in line.split():
        if word not in words:
            words.append(word)

        words.sort()

print(sorted(words))
