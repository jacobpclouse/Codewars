#Help Suzuki rake his garden!
#Link: https://www.codewars.com/kata/571c1e847beb0a8f8900153d/train/python

#Helpful sources:
# https://stackoverflow.com/questions/2960772/how-do-i-put-a-variable-s-value-inside-a-string
# https://stackoverflow.com/questions/15478127/remove-final-character-from-string
# https://www.geeksforgeeks.org/how-to-replace-values-in-a-list-in-python/
# https://stackabuse.com/python-get-number-of-elements-in-a-list/
# https://www.tutorialspoint.com/python/string_split.htm

# Test cases
garden1 = 'slug spider rock gravel gravel gravel gravel gravel gravel gravel'
print(garden1)
print(garden1.count(" "))


# my solution
def rake_garden(garden):
    
    # spliting string
    splitGarden = garden.split(" ")
    print(f"new splitGarden: {splitGarden}")
    print(f"The number of items in garden: {len(splitGarden)}")

    #Creating output string - garden 2
    gardenNew = ''
    
    #Creating replacement for anything not 'rock' or 'gravel'
    replacement = 'gravel'
    
    #Creating a spacer to place between the answers 
    spacer = ' '
    
    ##count = 0
    #Iterating through the garden
    for items in splitGarden:
        ##count = count + 1
        ##print(count)

        #If statement to catch anything not 'rock' or 'gravel'
        if items == 'rock':
            gardenNew += items
            gardenNew += spacer
        elif items == 'gravel':
            gardenNew += items
            gardenNew += spacer
        else:
            #print(f"Number {count} fell down to else condition")
            gardenNew += replacement
            gardenNew += spacer
    
    # check to see if last character in the string is a space, remove it if so
    if gardenNew[-1] == ' ':
        gardenNew = gardenNew[:-1]


    # returning string gardenNew        
    return gardenNew



# main

exportString = rake_garden(garden1)
print(exportString)
print(exportString.count(" "))
