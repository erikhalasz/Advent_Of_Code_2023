import time as t

t1 = t.time()
with open("C:/Users/Halász Erik/Documents/Advent_of_code_2023/day_4/file1.txt") as f:
    text = f.read()
    text = text.split("\n")

lines = []

for i in range(len(text)):
    lines.append(text[i].replace(f"Card {i+1}: ", "").split("|"))

    x = 0


for line in lines:
    i = 0
    for k in range(len(line[0].split(" "))):
        kl = line[0].split(" ")[k]
        l = set(line[1].split(" "))
        if kl in l and kl != "":
            i += 1
    if i >= 1:
        x += 2**(i-1)


print(x)
t2 = t.time()
print(t2-t1)
        
        
