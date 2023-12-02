import time as q

time1 = q.time()


f = open("C:/Users/Halász Erik/Documents/Advent_of_code_2023/day_1/file2.txt")
t = f.readlines()
text = []
for  string in t:
    text.append(string.strip("\n"))
my_dict = {
    "one": 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9
}

my_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

num_list = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


seperator = ""


s = []
for string in text:
    number = ""
    numbers = []
    for i in range(len(string)):
        number += string[i]
        for k in range(len(number)):
            for j in range(k+1):
                if (number[j:k+1]) in my_list:
                    szam = number[j:k+1]
                    numbers.append(szam)
                elif (number[j:k+1]) in num_list:
                    szo = number[j:k+1]

                    numbers.append(szo)
    s.append(numbers)

for number in s:
    if number[0] in num_list:
        number[0] = my_dict[number[0]]
    if number[-1] in num_list:
        number[-1] = my_dict[number[-1]]
    
l = []

for i in range(len(s)):
    k = []
    k.append(s[i][0])
    k.append(s[i][-1])
    l.append(k)
   
n = 0 
for m in l:
    t = f"{m[0]}{m[-1]}"
    n += eval(t)
    
print(n)

time2 = q.time()
print(time2 - time1)
    

    
