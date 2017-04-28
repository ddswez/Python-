
from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)

def print_a_line(line_count, f):
	print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Noe let's rewind, kind of like a tape"

rewind(current_file)

print "Let's print three lines:"

current_line = 3
print_a_line(current_line, current_file)

current_line = current_line - 1
print_a_line(current_line, current_file)

current_line = current_line - 1
print_a_line(current_line, current_file



# 打印结果为 :
# ➜  /Users/lpf/Documents/python python ex20.py test.txt
#First let's print the whole file:
#
#This is line 1 Ihaha
#This is line 2 hehe
#This is line 3 heihei
#
#Noe let's rewind, kind of like a tape
#Let's print three lines:
#3 This is line 1 Ihaha
#
#2 This is line 2 hehe
#
#1 This is line 3 heihei
#
#➜  /Users/lpf/Documents/python 	


# 每次运行f.seek(0)就回到了文件的开始  运行f.readLine()则会读取文件的一行  
# 空行是因为print在打印后会添加一个\n 解决办法是在print语句结尾加一个逗号, print就不会把自己的\n进行打印
# 如: print line_count, f.readline(), 














