import time
t1 = time.time()

with open("C:/Users/Halász Erik/Documents/Advent_of_code_2023/day_4/file1.txt") as f:
    text = f.read()
    text = text.split("\n")

lines = []

for i in range(len(text)):
    lines.append(text[i].replace(f"Card {i+1}: ", "").split("|"))

    x = 0

instances = {}

for i in range(len(text)):
    instances[f"{i+1}"] = 1


for m in range(len(lines)):
    line = lines[m]
    t = 0
    for k in range(len(line[0].split(" "))):
        kl = line[0].split(" ")[k]
        l = set(line[1].split(" "))
        if kl in l and kl != "":
            t += 1
    if t >= 1:
        for y in range(1, t+1):
            instances[f"{m + y + 1}"] += instances[f"{m+1}"]

x = 0


for key in instances:
    x += instances[key]

print(x)

t2 = time.time()
print(t2-t1)


import time

t1 = time.time()

with open("C:/Users/Halász Erik/Documents/Advent_of_code_2023/day_4/file1.txt") as f:
    text = f.read()
    text = text.split("\n")

cards = []

for i in range(len(text)):
    cards.append(list(map(int, text[i].replace(f"Card {i+1}: ", "").split("|")[0].split())))

instances = {}

for i in range(len(cards)):
    instances[f"{i+1}"] = 1

for m in range(len(cards)):
    card = cards[m]
    t = 0
    for k in range(len(card)):
        num = card[k]
        l = set(cards[m+1].split())
        if num in l:
            t += 1
    if t >= 1:
        for y in range(1, t+1):
            instances[f"{m + y + 1}"] += instances[f"{m+1}"]

x = 0

for key in instances:
    x += instances[key]

print(x)

t2 = time.time()
print(t2-t1)
