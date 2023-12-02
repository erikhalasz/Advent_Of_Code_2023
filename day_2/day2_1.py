import time

t1 = time.time()

my_dict = {'red': 12, 'green': 13, 'blue': 14}
sorok = []

f = open("C:/Users/Halász Erik/Documents/Advent_of_code_2023/day_2/file1.txt", "r")
file = f.readlines()
f.close()


def maxing(inf):
    for rounds in inf:
        r = rounds.split(",")
        for num in r:
            n = num.strip((" ")).split(" ")
            if int(n[0]) > max_dict[n[1]]:
                max_dict[n[1]] = int(n[0])
    if max_dict["red"] <= my_dict["red"] and max_dict["green"] <= my_dict["green"] and max_dict["blue"] <= my_dict["blue"]:
        return True


for i in range(len(file)):
    sorok.append([file[i].replace(f"Game {i+1}:", "").strip("\n")])

x = 0
for i in range(len(sorok)):
    info = sorok[i][0].split(";")
    max_dict = {"red": 0, "green": 0, "blue": 0}
    if maxing(info):
        x += i+1

print(x)
t2 = time.time()

print(t2-t1)
