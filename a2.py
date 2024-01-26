


#taking in all the inputs from the user
adj1 = input("Input an adjective: ")
adj2 = input("Input a second adjective: ")
adj3 = input("Input a third adjective: ")
bodypart1 = input("Input a body part: ")
noun1 = input("Input a noun: ")
noun2 = input("Input a second noun: ")
noun3 = input("Input a third noun: ")
invention1 = input("Input an invetion: ")

#applying the given input from user to madlibs by using .format 
madlibstext = """I would like to say a few {} words about the
most important invention of the twentieth century. I am not
referring to {} or even the discovery of {}.
The most {} invention, in my opinion, is the sneaker.
If it were not for sneakers, our {} would be dirty, cold,
and {}. Sneakers keep me from skidding if the {} are slippery,
and when I run, they keep me from stubbing my {}.""".format(adj1, invention1, noun1, adj2, bodypart1, adj3, noun2, noun3)

#printing the madlibs
print(madlibstext)

#if this is still incoreect can you comment or give an hint at to what youre wanting? 