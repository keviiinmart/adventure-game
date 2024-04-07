#adventure game
#import of the story
import storyfunc

def story():
	tav = storyfunc.getNameOfUser()
	print(tav)
	storyfunc.getStory(tav)	
	
story()

