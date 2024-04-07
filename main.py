#adventure game
#import of the story
import soj
import storyfunc

def story():
	tav = storyfunc.getNameOfUser()
	print(tav)
	storyO = storyfunc.getStory(tav)	
	if storyO == "Option 1":
		story = soj.sojbegin
		print(story)		

story()

