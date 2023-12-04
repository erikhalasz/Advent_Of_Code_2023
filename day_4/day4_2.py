import time
t1 = time.time()

with open("C:/Users/Halász Erik/Documents/Advent_of_code_2023/day_4/file1.txt") as f:
    text = f.read()
    text = text.split("\n")

lines = []

for i in range(len(text)):
    lines.append(text[i].replace(f"Card {i+1}: ", "").split("|"))


instances = {f"{k}": 1 for k in range(1, len(text)+1)}


for l in range(len(lines)):
    line = lines[l]
    points_per_game = 0
    for k in range(len(line[0].split(" "))):
        numbers = line[0].split(" ")[k]
        w_numbers = set(line[1].split(" "))
        if numbers in w_numbers and numbers != "":
            points_per_game += 1
    if points_per_game >= 1:
        for y in range(1, points_per_game+1):
            instances[f"{l + y + 1}"] += instances[f"{l+1}"]

s = sum(instances.values())

print(s)

t2 = time.time()
print(t2-t1)
