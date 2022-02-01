fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
count = 0
total_float_str = 0
for line in fhand:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        count = count + 1
        split_str = line.split()
        line_str = split_str[1]
        float_str = float(line_str)
        total_float_str = total_float_str + float_str
if count:
    avg_spam = total_float_str / count
    print("Average spam confidence: ", avg_spam)
