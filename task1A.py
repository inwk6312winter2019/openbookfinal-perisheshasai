fin1=open("Book1.txt","r")
fin2=open("Book.txt","r")
fin3=open("Book.txt","r")
file1=fin1.readlines()
file2=fin2.readlines()
file3=fin3.readlines()
def unique_word():
	for line in fin1:
		for line1 in fin2:
			for line1 in fin3:
				if x is not in fin1:
					fin1.append(x)
					if y is not in fin2:
						fin2.append(y)
						if z ins not in fin3:
							fin3.append(z)

				print(x)
					print(y)
						print(z)
unique_word()
fin1.close()
fin2.close()
fin3.close()

list1=["a","the","at","run","to","and","or","for","an","this"]
count=0
def count_the_article()
	for fin1 in list:
		if  fin1 in count:
			count[fin1] += 1
		else:
			count[fin1] = 1
	for fin2 in list:
		if fn2 in count:
			count[fin2] +=1
		else:
			count[fin2] = 1
	for fin3 in list:
		if fn3 in count:
			count[fin3] += 1
		else:
			count[fin3] = 1
count_the _article()



def sortd_words()
word=fin1.split()
	word.sorted(reverse=True)
	print(word)
word1=fin2.split()
	word1.sorted(reverse=True)
	print(word1)
word2=fin3.split()
	word2.sorted(reverse=True)
	print(word3)

sorted_words()


def character_word_count()
	for key in fin1 & fin2 & fin3:
		x, y = fin1[key]
		print("{} : {}\n{} : {}".format(key,x,key,y))

		z,k = fin2[key]
		print("{} : {}\n{} : {}".format(key,z,ky,k))

		l,m = fin3[key]
		print("{} : {}\n{} : {}".format(key,l,key,m))





character_word_count()

vowels = ("a","e","i","o","u")

def starts_with_vow()
	for  vow in fin1 & fin2 & fin3:
		if  vow.lower() == "a":
			vow["a"] += 1
		elif vow.lower() == "e":
			vow["e"] += 1
		elif vow.lower() == "i":
			vow["i"] += 1
		elif vow.lower() == "o":
			vow["o"] += 1
		elif vow.lower() == "u"
			vow["u"] += 1
print(vow)
starts_with_vow()







