import os
import json
import markovify
import random

with open("transcripts copy 2.txt", 'r') as f:
    text = f.read()
    text=text.replace('Offscreen','offscreen')
    text=text.replace('Music','music')
    text=text.replace('Laughter','laughter')
    text=text.split('-')


reactions = []
reactionNum = []
characters = []
characterNum =[]
def makeCharacter(string, nums, characters):
	if string in characters:
		nums[characters.index(string)] = nums[characters.index(string)]+1
	else:
		characters.append(string)
		nums.append(1)
def makeReaction(string, nums, characters):
	if string in characters:
		nums[characters.index(string)] = nums[characters.index(string)]+1
	else:
		characters.append(string)
		nums.append(1)

def nonWords():
	reactions = []
	reactionNum = []
	characters = []
	characterNum =[]
	for line in text:
		if "[" in line or "(" in line:
			s=line[line.find("["):line.find("]")+1]
		# if "(" in line:
		# 	s=line[line.find("("):line.find(")")+1]
		# 	s=s.replace('(','[')
		# 	s=s.replace(')',']')

			#if len(s)>2 and s != "[bleep]" and s[1].isupper():
			if len(s)>2:
				if s[1].isupper():
					makeCharacter(s, characterNum, characters)
					# if " " in s:
					# 	q=s.split(" ")
						
					# 	if len(q)<1:
					# 		second=q[1]
					# 		if second.isupper()==False:
					# 			makeReaction(s, reactionNum, reactions)
					# 		else:
					# 			makeCharacter(s, characterNum, characters)
						# isReact= False
						# for x in range(len(q)-1):
						# 	cur=q[x]
						# 	if x==0 and cur[1].islower():
						# 		isReact=True
						# 	if cur[0].islower()and not x==0:
						# 		isReact=True
						# if isReact:
						# 	makeReaction(s, reactionNum, reactions)
						# else:
						# 	first = q[0]
						# 	first = first[1:]
						# 	for person in characters:
						# 		if first == person:
						# 			characternum[characters.index(first)] = characternum[characters.index(first)]+1
						# 			characters[characters.index(first)] = s
						# 		else:
						# 			makeCharacter(s, characterNum, characters)
						# first=s[0:s.find(" ")]
						# second=s[s.find(" "):]
						# if second[0].islower():
						# 	makeReaction(s, reactionNum, reactions)
						# else:
						# 	if first in characters:
						# 		characters[characters.index(first)]= s
						# 		characternum[characters.index(first)] = characternum[characters.index(first)]+1
						# 	else:
						# 		makeCharacter(s, characterNum, characters)
						# 		print(q)
				
					# else:
					# 	makeCharacter(s, characterNum, characters)
				else:
					makeReaction(s, reactionNum, reactions)
	return reactions, reactionNum, characters, characterNum
reactions = []
reactionNum = []
characters = []
characterNum =[]
reactions, reactionNum, characters, characterNum=nonWords()	
s=[]
for x in characters:
	for q in range(1, characterNum[characters.index(x)]):
		s.append(x)

text_model = markovify.Text(text)

charactersBad=True
while(charactersBad):
	sceneCharacters = []
	for x in range(1,9):
		curCharacter = random.choice(s)
		if x==1:
			sceneCharacters.append(curCharacter)
		if x>=1:
			while(curCharacter in sceneCharacters):
				curCharacter = random.choice(s)
			sceneCharacters.append(curCharacter)
	# print(random.choice(s))
	print(sceneCharacters)
	response=input("are characters bad? (y/n)")
	if response == 'n':
		charactersBad=False
#python3 rpdrtest.py 
 # Print five randomly-generated sentences

for i in range(60):
	myLine= str(random.choice(sceneCharacters))
	myLine= myLine[1:-1] +":"
	myLine = myLine+" "
	myLine = myLine+text_model.make_sentence()
	print(myLine)
	action=random.randrange(1,100)
	if action<=30:
		print(random.choice(reactions))
    #rint("-----------------------------------------")
f.close() 

