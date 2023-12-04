import time as t

t1 = t.time()
with open("C:/Users/Halász Erik/Documents/Advent_of_code_2023/day_4/file1.txt") as f:
    text = f.read()
    text = text.split("\n")

lines = []

for points_per_game in range(len(text)):
    lines.append(text[points_per_game].replace(f"Card {points_per_game+1}: ", "").split("|"))

    s = 0


for line in lines:
    points_per_game = 0
    for n in range(len(line[0].split(" "))):
        numbers = line[0].split(" ")[n]
        w_numbers = set(line[1].split(" "))
        if numbers in w_numbers and numbers != "":
            points_per_game += 1
    if points_per_game >= 1:
        s += 2**(points_per_game-1)


print(s)
t2 = t.time()
print(t2-t1)
        
        
