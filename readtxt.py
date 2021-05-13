import re
file = open("israel_cities.txt","r")
print("[",end="")

for line in file:

    flag = 0
    line = line.split()
    for character in line[2]:
        if character.isdigit():
            break
        else:
            flag = 1
    if flag == 1:
        print("\""+line[1]+" "+line[2]+"\""+',',end="")
    else:
        print("\""+line[1]+"\"" +",",end="")