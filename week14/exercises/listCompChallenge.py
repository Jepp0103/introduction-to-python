 
# deocorator from lesson-07
import time
# import resource


# def memory(func):

#     def wrapper(*args, **kwargs):
#         # meassure memory before
#         start_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        
#         # execute the script
#         value =  func(*args, **kwargs)
        
#         # meassure memory after
#         end_mem = (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss) - start_mem
        
#         print(f'Memory usage: {end_mem}')

#         return value
        
#     return wrapper    


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        value = func(*args, **kwargs)
        end = (time.time()) - start
        print(f'Time elapsed: {end}')
        return value

    return wrapper




# 1. Find all of the numbers from 1-1000 that are divisible by 7
# @timer
# @memory
def divisible_by_7_loop():
    l = []
    for i in range(1000):
        if(i % 7 == 0):
            l.append(i)
    return l

# @timer
# @memory
def divisible_by_7_comp():
    l = [i for i in range(1, 1000) if i % 7 ==  0]
    return l

# 2. Find all of the numbers from 1-1000 that have a 3 in them
def three_in_num(n):
    l = []                                                                                                                  
    for i in range(n):
        if i % 10 == 3:
            l.append(i)                                                                                                 
        elif i // 10 % 10 == 3:
            l.append(i)                                                                                                 
        elif i // 100 % 10 == 3:
            l.append(i)                                                                                                 
        elif i // 1000 % 10 == 3:
            l.append(i)  
    return l

def three_in_num_comp(n):
    l = [i for i in range(n) if i%10 == 3 or i // 10 %10 == 3 or i // 100 %10 == 3 or i//1000%10 == 3 ]
    return l

# 3. Count the number of spaces in a string
def number_of_spaces(string):
    count = 0
    for s in string:
        if s == ' ':
            count += 1
    return count

def number_of_spaces_comp(string):
    l = len([i for i in string if i == ' '])
    return l

# 4. Remove all of the vowels in a string
def remove_vowels(string):
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    l = []
    for s in string:
        if s not in vowels:
            l.append(s)
    return ''.join(l)

def remove_vowels_comp(string):
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    l = [i for i in string if i not in vowels]
    return ''.join(l)
    
# 5. In a string made up of randomly generated words, generate a list of all words that have less than 4 letters
# def generate_list_of_4_words(string):
#     strings = [string]
#     for s in strings:
#         if len(s) < 4:
#             strings.append(s)
#     return strings

# 6. Use a dictionary comprehension to count the length of each word in a sentence.
def length_word_comp(string):
    len_words = [len(word) for word in string.split()]
    return len_words

# 7. Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9)
def find_numbers_divisible_by_digit():
    # numbers_divisible = [[i for i in range(1, 1000)] if i % 2 == 0 or i % 3 == 0 or i % 4 == 0 or i % 5 == 0 or i % 6 == 0 or i % 7 == 0 or i % 8 == 0 or i % 9 == 0]
    numbers_divisible = [i for i in range(1, 1000) for j in range(2, 9) if i % j == 0]
    return numbers_divisible

# 8. For all the numbers 1-1000, use a nested list comprehension to find the highest single digit any of the numbers is divisible by


# 9. Multiples of 3 and 5: If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
def main():
    print("--------------------------")
    print("1. - Divisible by 7 - loop:")
    print(divisible_by_7_loop())

    print("Divisible by 7 comp:")
    print(divisible_by_7_comp())
    print("--------------------------")
    print("2. - Number contains 3")
    print(three_in_num(1000))
    print(three_in_num_comp(1000))

    print("--------------------------")
    print("3. - Number of spaces")
    print(number_of_spaces("Jeppe er så sej!"))
    print(number_of_spaces_comp("Jeppe er så sej!"))

    print("--------------------------")
    print("4. - Remove vowels")
    print(remove_vowels("Marry"))
    print(remove_vowels_comp("Marry"))

    print("--------------------------")
    print("6. - Word length")
    print(length_word_comp("Carla is a girl"))

    print("--------------------------")
    print("7. - Numbers divisible")
    print(find_numbers_divisible_by_digit())

main()
