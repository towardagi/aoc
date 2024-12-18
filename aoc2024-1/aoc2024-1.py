left_list = []
right_list = []

with open('./aoc2024-1/input.txt', 'r') as file:
    for line in file:
        left_list.append(int(line.split()[0]))
        right_list.append(int(line.split()[1]))

left_list.sort()
right_list.sort()

distance = 0

for i in range(len(left_list)):
    distance += abs(left_list[i] - right_list[i])

print(distance)