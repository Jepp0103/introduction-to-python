
teils = dict()

def addTeil(tuple, cleanliness):
    if len(tuple) == 2:
        teils[tuple] = cleanliness
        return teils
    return "Teil cold not be added"

def isClean(tuple):
    if teils[tuple] == "clean":
        return True

    elif teils[tuple] == "not clean":
        return False
    
    else: 
        return "Cleanliness not defined."

def main():    
    print("-----------------------------------------------")
    print("-----------------------------------------------")
    print("DICTIONARY SOLUTION:")
    print("-----------------------------------------------")
    for i in range(1, 31):
        n = 1
        while n <= 24:
            if (n % 2) == 1:
                addTeil((i, n), "clean")
                n += 1
            else:
                addTeil((i, n), "not clean")
                n += 1

    addTeil((50,2),"ugly") #trying to specify another cleanliness which will return "not defined".
    print(teils)
    print("-----------------------------------------------")
    print("Number of teils:", len(teils))
    print("Is teil (29, 18) clean?", isClean((29,18)))
    print("Is teil (28, 9) clean?", isClean((28, 9)))
    print("Is teil (50,2) clean?", isClean((50,2)))
    print("-----------------------------------------------")
    print("-----------------------------------------------")

main()