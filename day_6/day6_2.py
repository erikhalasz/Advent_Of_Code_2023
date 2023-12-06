import time

t1 = time.time()

with open("C:/Users/Halász Erik/Documents/Advent_of_code_2023/day_6/file1.txt") as f:
    text = f.read().split("\n")

time_1 = text[0].replace("Time:", "").split()
distance_1 = text[1].replace("Distance:", "").split()

time_string = ""
for el in time_1:
    time_string += el

distance_string = ""
for el in distance_1:
    distance_string += el

time_2 = int(time_string)
distance_2 = int(distance_string)


def speed():
    i = 0
    for holding_button in range(time_2):
        t = time_2-holding_button
        if holding_button*t > distance_2:
            i += 1
    return(i)



print(speed())
t2 = time.time()
print(t2-t1)

