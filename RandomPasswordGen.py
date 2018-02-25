import random

upper   = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lower   = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = ["0","1","2","3","4","5","6","7","8","9","0","1","2","3","4","5","6","7","8","9"]
special = ["+","=","#","&","$","@","%","!","£"]
choice_list = []

#def   [length, charcters, [seperator,block], number of pws]
data = [0, 'uln', ['',0], 1]

print('''\n------------------------------PASSWORD GENERATOR------------------------------\n
Usage: length [optional: /characters /seperator, block /number] or type 'help'\n''')

userin = input('\nEnter password length: ')

if 'help' in userin:
	print('''\n   length	determines the length of the password(s)
   characters	deternimes the characters used
   		[default is upper, lower and numbers]\n
   		or choose from:\n
   		  a for all
   		  u for upper
   		  l for lower
   		  n for numbers
   		  s for speial characters\n
   seperator 	determines a charcater to create groups
   block	determines the number of characters in a group
   		***note: sperator and block can only be used together***\n
   number 	determines the number of generated passwords
   		[default is 1]\n
   Examples: 8            -->  Oga4Vo02
             12 /un /-,3  -->  JMU-013-YJ9-PE6''')
	L = (input('\nEnter password length: ')).split('/')
else:
	L = userin.split('/')

#changes the type of the user input
for i in range(len(L)):
	L[i] = L[i].rstrip()
	if L[i].isdigit():
		L[i] = int(L[i])
	if type(L[i]) is str and ',' in L[i]:
		L[i] = list(L[i])
		L[i].pop(1)
		L[i][1] = int(L[i][1])

#overwrites the default values with user input
while len(L) > 0:
	data[0], data[2][1] = L[0], L.pop(0)
	
	if len(L) > 0:
		if type(L[0]) is str:
			data[1] = L.pop(0)
			if len(L) == 0:
				break
		if type(L[0]) is list:
			data[2] = L.pop(0)
			if len(L) == 0:
				break
		if type(L[0]) is int:
			data[3] = L.pop(0)
			if len(L) == 0:
				break

length = data[0]
seperator = data[2][0]
block = data[2][1]
number = data[3]
chars = data[1]

#creates custom set of characters
if 'a' in chars:
	choice_list = upper + lower + numbers + special #add skip when a
if 'u' in chars:
	choice_list += upper
if 'l' in chars:
	choice_list += lower
if 'n' in chars:	
	choice_list += numbers
if 's' in chars:
	choice_list += special
#	if 'c' in chars:
#		choice_list += custom

if seperator in choice_list:
	choice_list.pop(choice_list.index(seperator))

def password_generator(length, number):
	'''chooses 'length characters from the choosen set and prints
	number passwords of length 'length', creating group of 'block' 
	seize, adding the seperator inbetween
	'''
	if number == 1:
		print('\nYour password is:\n\t')
	else:
		print('\nYour passwords are:\n\t')

	for num in range(number):
		password_list, password_list_final = [], []
		for i in range(length):
				c = random.choice(choice_list)
				password_list.append(c)

		b1 = length / block
		while b1 >= 1:
			for x in range(block):
				password_list_final.append(password_list.pop()) 
			password_list_final.append(seperator)
			b1 -= 1

		if 0 < b1 < 1:
			b2 = b1 * block
			for y in range(round(b2)):
				password_list_final.append(password_list.pop())

		if password_list_final[-1] == seperator:
			password_list_final.pop()


		print('\t', ''.join(password_list_final), '\n')

password_generator(length, number)

input()
