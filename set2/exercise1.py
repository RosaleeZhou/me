"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

some_words = ['what', 'does', 'this', 'line', 'do', '?']
# I think this will print "what does this line do" by calling the print function. 
for word in some_words:
    print(word)        # it printed "what","does","this","line","do","?"respectively.
# I think this will print a random word in the list.
for x in some_words:      
    print(x)           

print(some_words)      # it printed "what","does","this","line","do","?"respectively.
# I think this will print "some_words contains more than 3 words".
if len(some_words) > 3:
    print('some_words contains more than 3 words')      #It printed "some_words contains more than 3 words".
# I think this will print some details about my laptop system and settings.
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())    #It printed a namedtuple containing system, node, release, version, machine, and processor

usefulFunction()
