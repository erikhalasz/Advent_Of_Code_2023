import time

t1 = time.time()
sorok = []

f = open("file2.txt")
file = f.readlines()
f.close()


def maxing(inf):
    for rounds in inf:
        r = rounds.split(",")
        for num in r:
            n = num.strip((" ")).split(" ")
            if int(n[0]) > min_dict[n[1]] and min_dict[n[1]] != 0:
                min_dict[n[1]] = int(n[0])
            elif min_dict[n[1]] == 0:
                min_dict[n[1]] = int(n[0])
    return min_dict["blue"]*min_dict["green"]*min_dict["red"]


for i in range(len(file)):
    sorok.append([file[i].replace(f"Game {i+1}:", "").strip("\n")])

x = 0
for i in range(len(sorok)):
    info = sorok[i][0].split(";")
    min_dict = {"red": 0, "green": 0, "blue": 0}
    x += maxing(info)

print(x)
t2 = time.time()

print(t2-t1)
