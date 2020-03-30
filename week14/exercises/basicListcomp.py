# Ex 1: Basic listcomp
# Create a list of capital letters from the english alphabet.
alphabetList = [chr(i) for i in range(65,91)]
print("Alphabetlist", alphabetList)

# Do the same, but exclude the 4 with the Unicode code point of 70, 75, 80 and 85.
alphabetListExclude = [chr(i) for i in range(65, 91) if i not in [70, 75, 80, 85] ]
print("alphabetListExclude", alphabetListExclude)


# Create a list of capital letters, but exclude every second between F & O
capFOsecond = [chr(i) for i in range(65, 91) if i not in range(70, 80, 2)]
print("capFOsecond", capFOsecond)

# Create something that prints

# From 2 lists, using a list comprehension, create a list containing:
# twoList = [('Black', 's'), ('Black', 'm'), ('Black', 'l'), 
#             ('Black', 'xl'), ('White', 's'), ('White', 'm'), 
#             ('White', 'l'), ('White', 'xl')]

colors = ['Black', 'White']
sizes = ['s', 'm', 'l', 'xl']

print("twoList", [(i,j) for i in colors for j in sizes])