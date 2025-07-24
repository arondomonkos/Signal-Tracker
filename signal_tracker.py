# Signal Tracker
# Author: Áron Domonkos
# Year: 2024

import math

#Function 1
signals = []
with open('signal.txt', 'r') as file:
    for line in file:
        line = line.strip().split()
        signals.append([
            int(line[0]),
            int(line[1]),
            int(line[2]),
            int(line[3]),
            int(line[4])
        ])

print('\nFunction 2')
index = int(input('Enter the signal index: '))
print(f'x={signals[index - 1][3]} y={signals[index - 1][4]}')

print('\nFunction 3')
def elapsed(signal1, signal2):
    return abs((signal2[0] - signal1[0]) * 3600 + (signal2[1] - signal1[1]) * 60 + (signal2[2] - signal1[2]))

print('\nFunction 4')
difference = elapsed(signals[0], signals[-1])
hours = difference // 3600
minutes = (difference % 3600) // 60
seconds = difference % 60
print(f'Duration: {hours}:{minutes}:{seconds}')

print('\nFunction 5')
min_x = 10000
max_x = -10000
min_y = 10000
max_y = -10000

for s in signals:
    if s[3] < min_x:
        min_x = s[3]
    if s[3] > max_x:
        max_x = s[3]
    if s[4] < min_y:
        min_y = s[4]
    if s[4] > max_y:
        max_y = s[4]

print(f'Bottom left: {min_x} {min_y}, top right: {max_x} {max_y}')

print('\nFunction 6')
def distance(signal1, signal2):
    return math.sqrt((signal2[3] - signal1[3]) ** 2 + (signal2[4] - signal1[4]) ** 2)

total = 0
for i in range(len(signals) - 1):
    total += distance(signals[i], signals[i + 1])

print(f'Movement: {round(total, 3)}')

#Function 7
with open('missed.txt', 'w') as output:
    for i in range(len(signals) - 1):
        missed_by_distance = 0
        missed_by_time = 0

        time_gap = elapsed(signals[i], signals[i + 1])
        if time_gap > 300:
            missed_by_time = (time_gap - 1) // 300

        max_shift = max(abs(signals[i + 1][3] - signals[i][3]), abs(signals[i + 1][4] - signals[i][4]))
        if max_shift > 10:
            missed_by_distance = (max_shift - 1) // 10

        if missed_by_distance > missed_by_time:
            print(signals[i + 1][0], signals[i + 1][1], signals[i + 1][2], 'coordinate-gap', missed_by_distance, file=output)

        if missed_by_distance <= missed_by_time != 0:
            print(signals[i + 1][0], signals[i + 1][1], signals[i + 1][2], 'time-gap', missed_by_time, file=output)