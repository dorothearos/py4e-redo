import re

fname = input('Enter file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()

reg_record = []
for line in fhand:
    line = line.rstrip()
    reg_exp = re.findall('^New Revision: ([0-9.]+)', line)
    if not reg_exp:
        continue
    for each in reg_exp:
        each = float(each)
        reg_record = reg_record + [each]

reg_sum = sum(reg_record)
count = len(reg_record)
reg_avg = reg_sum / count

print(reg_avg)
