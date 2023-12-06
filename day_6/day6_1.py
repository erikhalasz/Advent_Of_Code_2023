import time as t

t1 = t.time()

with open("C:/Users/Halász Erik/Documents/Advent_of_code_2023/day_6/file1.txt") as f:
    text = f.read().split("\n")

time = list(map(int, text[0].replace("Time:", "").split()))
distance = list(map(int, text[1].replace("Distance:", "").split()))


good = []


def speed():
    i = 0

    for k in range(len(time)):
        achievements = []
        for holding_button in range(time[k]):

            t = time[k]-holding_button
            if holding_button*t > distance[k]:
                achievements.append(holding_button*t)
        good.append(achievements)


n = 1


speed()
for el in good:
    n = n*len(el)

print(n)
t2 = t.time()
print(t2-t1)