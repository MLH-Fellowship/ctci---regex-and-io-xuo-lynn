# converts emails ending in @gmail.com to mlh.io

import csv

file = open('emails.csv', 'r')

with open('emails.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row[0].endswith('@gmail.com'):
            print(row[0][:-10] + '@mlh.io')
        else:
            print(row[0])
