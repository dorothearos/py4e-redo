fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
for wstr in fhand:
    word = wstr.rstrip()
    print(word.upper())
