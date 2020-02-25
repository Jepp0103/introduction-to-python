# Set exercises.


# ![](https://www.linuxtopia.org/online_books/programming_books/python_programming/images/p2c6-union.png)



# 1. Write a Python program to create a set.
programmingLanguages = set(['Python', 'Java'])
objectOrientedLanguages = set(["Python", "C#", "Java", "C"])
# 2. Write a Python program to iteration over sets.

def iterateSet():
    for programmingLanguage in programmingLanguages:
        print(programmingLanguage)

# 3. Write a Python program to add member(s) in a set. 
def addLanguage(programmingLanguage):
    programmingLanguages.add(programmingLanguage)
    return programmingLanguages

# 4. Write a Python program to remove item(s) from set. 
def removeLanguage(programmingLanguage):
#remove method to remove specific element in set
    programmingLanguages.remove(programmingLanguage)
    return programmingLanguages


# 5. Write a Python program to remove an item from a set if it is present in the set. 
def removeLanguageIfExists(programmingLanguage):
    if programmingLanguage in programmingLanguages:
        programmingLanguages.remove(programmingLanguage)
        return programmingLanguages
    else:
        return "Language not found"

# 6. Write a Python program to create an intersection of sets.
def interSectSets(set1, set2):
    intersectionSet = set1.intersection(set2)
    return intersectionSet
# ![](https://www.linuxtopia.org/online_books/programming_books/python_programming/images/p2c6-intersection.png)

# 7. Write a Python program to create a union of sets.
def unifySets(set1, set2):
    unionSet = set1.union(set2)
    return unionSet
#  ![](https://www.linuxtopia.org/online_books/programming_books/python_programming/images/p2c6-union.png)

# 8. Write a Python program to create set difference.
def differSets1(set1, set2):
    differenceSet1 = list(set(set1) - set(set2))
    return differenceSet1

def differSets2(set1, set2):
    differenceSet2 = list(set(set2) - set(set1))
    return differenceSet2

#  ![](https://www.linuxtopia.org/online_books/programming_books/python_programming/images/p2c6-difference.png)

# 9. Write a Python program to create a symmetric difference.
def symmetricDifferSets(set1, set2):
    symdifferenceSet = set1.symmetric_difference(set2)
    return symdifferenceSet
#  ![](https://www.linuxtopia.org/online_books/programming_books/python_programming/images/p2c6-symmdiff.png)

# 10. Write a Python program to issubset and issuperset.
def isSubset(set1, set2):
    return set1.issubset(set2)

def isSuperset(set1, set2):
    return set1.issuperset(set2)

# 11. Write a Python program to create a shallow copy of sets.
def shallowCopySet(set):
    newSet = set.copy()
    return newSet

# Note : Shallow copy is a bit-wise copy of an object. A new object is created that has an exact copy of the values in the original object.

# 12. Write a Python program to clear a set.
def clearSet(set):
    set.clear()
    return set

# 13. Write a Python program to use of frozensets.
def freezeSet(set):
    freezeSet = frozenset(set)
    return freezeSet

# 14. Write a Python program to find maximum and the minimum value in a set.
def findMax(set):
    maxValue = max(set)
    return maxValue

def findMin(set):
    minValue = min(set)
    return minValue

# 15. Write a Python program to find the length of a set.
def findLength(set):
    length = len(set)
    return length

def main():
    print("-------------------------------------------------")
    print("Exercise 1 - create set")
    print(programmingLanguages)

    print("-------------------------------------------------")
    print("Exercise 2 - iterate")
    print(iterateSet())

    print("-------------------------------------------------")
    print("Exercise 3 - adding")
    addLanguage('Scala')
    addLanguage('SQL')
    addLanguage('JavaScript')
    addLanguage('HTML')
    print(programmingLanguages)

    print("-------------------------------------------------")
    print("Exercise 4 - remove items")
    removeLanguage('HTML')
    removeLanguage('JavaScript')
    print(programmingLanguages)

    print("-------------------------------------------------")
    print("Exercise 5 - remove items if present")
    removeLanguageIfExists('Python')
    print(removeLanguageIfExists('JavaScript'))
    print(programmingLanguages)

    print("-------------------------------------------------")
    print("Exercise 6 - intersection")
    print("Programminglanguages:", programmingLanguages)
    print("Object oriented languages", objectOrientedLanguages)
    intersectedSet = interSectSets(programmingLanguages, objectOrientedLanguages)
    print(intersectedSet)

    print("-------------------------------------------------")
    print("Exercise 7 - union")
    print("Programminglanguages:", programmingLanguages)
    print("Object oriented languages", objectOrientedLanguages)
    unionSet = unifySets(programmingLanguages, objectOrientedLanguages)
    print(unionSet)

    print("-------------------------------------------------")
    print("Exercise 8 - difference")
    print("Programminglanguages:", programmingLanguages)
    print("Object oriented languages", objectOrientedLanguages)
    differenceSet1 = differSets1(programmingLanguages, objectOrientedLanguages)
    differenceSet2 = differSets2(programmingLanguages, objectOrientedLanguages)
    print("Difference set 1:", differenceSet1)
    print("Difference set 2:", differenceSet2)

    print("-------------------------------------------------")
    print("Exercise 9 - symmetric difference")
    symmetricDifferenceSets = symmetricDifferSets(programmingLanguages, objectOrientedLanguages)
    print(symmetricDifferenceSets)

    print("-------------------------------------------------")
    print("Exercise 10 - isSubset and isSuperset")
    print("Programminglanguages:", programmingLanguages)
    print("Object oriented languages", objectOrientedLanguages)
    subset1 = isSubset(programmingLanguages, objectOrientedLanguages)
    subset2 = isSubset(objectOrientedLanguages, programmingLanguages)
    print("Is set1 subset of set2?:", subset1)
    print("Is set2 subset of set1?:", subset2)
    programmingLanguages.remove("SQL")
    programmingLanguages.remove("Scala")
    subset1 = isSubset(programmingLanguages, objectOrientedLanguages)
    print("Programminglanguages:", programmingLanguages)
    print("Is set1 subset of set2?:", subset1)

    print(" ")
    programmingLanguages.add('C#')
    print("Programminglanguages:", programmingLanguages)
    print("Object oriented languages", objectOrientedLanguages)
    superset = isSuperset(programmingLanguages, objectOrientedLanguages)
    print("Is set1 superset of set2?", superset)
    superset = isSuperset(objectOrientedLanguages, programmingLanguages) #swapping
    print("Is set2 superset of set1?", superset)


    print("-------------------------------------------------")
    print("Exercise 11 - shallow copy")
    wannabeProgrammingLanguages = shallowCopySet(programmingLanguages)
    print("Wannabe programminglanguages:", wannabeProgrammingLanguages)

    print("-------------------------------------------------")
    print("Exercise 12 - clear")
    cleared_wannabe = clearSet(wannabeProgrammingLanguages)
    print("Cleared wannabe programming languages:", cleared_wannabe)

    print("-------------------------------------------------")
    print("Exercise 13 - frozen set")
    print("Object oriented languages", objectOrientedLanguages)
    frozen_set = freezeSet(objectOrientedLanguages)
    print(frozen_set)
    

    print("-------------------------------------------------")
    print("Exercise 14 - find max and minimum value in set")
    print("Object oriented languages", objectOrientedLanguages)
    maximum = findMax(objectOrientedLanguages)
    minimum = findMin(objectOrientedLanguages)
    print("Max:", maximum)
    print("Minimum:", minimum)
    
    print("-------------------------------------------------")
    print("Exercise 15 - length")
    print("Object oriented languages", objectOrientedLanguages)
    length = findLength(objectOrientedLanguages)
    print("Length:", length)


main()

