
#1
with open("student_names.txt","w") as f :
	content = f.read()
	f.write("Random but not so random")

#2
content = ""
with open("student_names.txt") as f :
	n = 10 
	for i in range(n):
		content += f.readline()


#3

content = ""
with open("student_names.txt") as f :
	n = 10 
	for line in (file.readlines()[-n:]):
		content += line


#4

with open("student_names.txt") as f :
	x = "word"
	print(x in f.read())


#5

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for char in chars:
	with open(char+".txt","w") as f :
		pass