#Mad Libs Story Challenge

print ("We are going to play a game. I will ask you to type in some words. Then I will make a story out of them for you.")

adj1 = str(input("Type in an adjective:"))
adj2 = str(input("Type in a second adjective:"))
adj3 = str(input("Type in a third adjective:"))
adj4 = str(input("Type in a fourth adjective:"))
adj5 = str(input("Type in a fifth adjective:"))
pn1 = str(input("Type in a plural noun:"))
n1 = str(input("Type in a noun:"))
n1 = n1.capitalize()
n2 = str(input("Type in a second noun:"))
na1 = str(input("Type in a name:"))
na1 = na1.capitalize()
v1 = str(input("Type in a verb:"))

story = "The night was {0} and {1}. All around the howling {2} drove the dour folk of Scrunton-By-{3} under their {4} bedsheets. There was one brave {5} called {6} who decided to {7} back against the {8}. She was {9} and {10}. The {11} had no chance against her. Which is good for length of this story. The end.".format(adj1, adj2, pn1, n1, adj3, n2, na1, v1, pn1, adj4, adj5, pn1)

print (story)
