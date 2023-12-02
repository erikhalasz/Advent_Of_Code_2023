f = open("file1.txt", "r")
lines = []
for line in f.readlines():
    lines.append(line.strip('\n'))
    

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
num = []
for line in lines:
    num_line = []
    for i in range(len(line)):
        if line[i] in numbers:
            num_line.append(line[i])
    num.append(num_line)
    

n = 0
    

szamok = []    
for numbers in num:
    szam =  []
    szam.append(numbers[0])
    szam.append(numbers[-1])
    szamok.append(szam)
 
for l in szamok:
    seperator = ""
    k = seperator.join(l)
    n += int(k)
    
print(n)