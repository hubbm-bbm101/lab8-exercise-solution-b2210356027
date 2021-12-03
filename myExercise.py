import sys
import os
student = open("student.txt", "r")
list0=[]
for line in student:
    line = line.strip("\n")
    list0.append(line.split(":"))
student.close()

dic={}
for i in list0:
    dic[i[0]] = i[1]
a=sys.argv[1].split(",")

try:
    for i in a:
       print("Name: " + i + ", University: " + dic[i])
except:
    print("No record of '" + i + "' was found!")