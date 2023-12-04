with open("C:/Users/Halász Erik/Documents/Advent_of_code_2023/day_3/file1.txt") as f:
    lines = f.readlines()


def checking(list_):
    i_list = []
    for i in range(len(list_)):
        if list_[i] in numbers:
            i_list.append(i)
    return i_list
                
def getting_is(list_):
    maxes = []
    for i in range(len(list_), 3):
        print(min(list_[i:i+3]), max(list_[i:i+3]))
        maxes.append(*[(min(list_[i:i+3]), max(list_[i:i+3]))])
    return maxes
   
   
   
   
   
   
    
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# text = []
# for line in lines:
#     l = list(line)
#     if l[-1] == "\n":
#         text.append(l[0:len(l)-1])
#     else:
#         text.append(list(line))

# print(text)

print(getting_is(checking(['4', '6', '7', '.', '.', '1', '1', '4', '.', '.'])))