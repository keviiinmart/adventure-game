import soj

#function that get a input of the name of the user
def getNameOfUser():
	tav = input("What is your name?\n")
	return tav


def getStory(tav):
	story = input("What adventure did " + tav + " go on?\nOption 1: Shadows of Justice\n")
	if story == "Option 1":
		print("Shadows of Justice")
	else:
		getStory(tav)	
	return story

  
