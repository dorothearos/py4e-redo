"""
Write a simple program to simulate the operation of the grep command
on Unix. Ask the user to enter a regular expression and count
the number of lines that matched the regular expression
"""

import re

count=0
user_input = input('Enter a regular expression: ')
reg_exp = str(user_input)
fname = 'data/mbox-short.txt'
fhand = open(fname)
for line in fhand:
    line = line.rstrip()
    if re.findall(reg_exp, line) != []:
        count += 1
print(fname + ' had ' + str(count) + ' lines that matched ' + reg_exp)
