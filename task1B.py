file1=set(line.strip() for line in open("Book1.txt")
file2=set(line.strip() for line in open("Book2.txt")
file3=set(line.strip() for line in open("Book3.txt")
fin1=set(line.split() for line in open("Book1.txt")
fin2=set(line.split() for line in open("Book2.txt")
fin3=set(line.split() for line in open("Book3.txt")
word={}
for line in file1 & file2 & file3:
	for line in fin1 & fin2 & fin3:
		line = line.replace(",","")
		line = line.replace(".","")
		line = line.replace("!","")
		line = line.replace("\"","")
		if line not in fin1 & fin2 & fin3:
			if line not in word:
				word[line] = 1
			else:
				word[line] += 1
print(word)

