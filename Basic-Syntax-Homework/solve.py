
#1

with open("student_names.txt") as f :
	content = f.read()


#2
with open("student_names.txt","w") as f :
	f.write("Random but not so random")

#3
content = ""
with open("student_names.txt") as f :
	n = 10 
	for i in range(n):
		content += f.readline()


#4

content = ""
with open("student_names.txt") as f :
	n = 10 
	for line in (file.readlines()[-n:]):
		content += line


#5

with open("student_names.txt") as f :
	x = "word"
	print(x in f.read())


#6

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for char in chars:
	with open(char+".txt","w") as f :
		pass