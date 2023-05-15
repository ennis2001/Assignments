import requests


# The point of this assignment is not to use the functional elements that are part of your chosen language (JavScript/Python).
# But, rather, implement the functionality from scratch using pure functions and higher level functions.
# Do the implimentation in order as given. 
# We have linked to info at MDN, this is just to give a sence of how the reduce,forEach,map and filter functions should work.
#
# ðŸ› ï¸ Prerequisite:
# You must create an array persons that will contain the data from https:#raw.githubusercontent.com/MM-203/misc/main/data/data.json
# This must be done before the first task
#
# ----------------------------------------------------------------------------------------------------------------------------------
# Bonus challenge ðŸŽ‰ (a bit hard), the functions forEach, filter and map can all be created using the function reduce. 
# If you feel up for a challenge, try doing so. NB! The bonus challenge is optional. 
# ----------------------------------------------------------------------------------------------------------------------------------


# Fetching data from the URL and creating the 'persons' array
response = requests.get('https://raw.githubusercontent.com/MM-203/misc/main/data/data.json')
persons = response.json()

# 1
# Implement your own reduce function and count the number of people above the age of 50
# You can read about a reduce function https:#developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce 
print('Task 1')

# Implementation of the reduce function
def reduce(array, reducer, initial_value):
    result = initial_value
    for element in array:
        result = reducer(result, element)
    return result

# Function to count the number of people above the age of 50
def count_people_above_50(acc, person):
    if person['age'] > 50:
        return acc + 1
    else:
        return acc

# Using the reduce function to count the number of people above 50
count = reduce(persons, count_people_above_50, 0)
print(count)



# 2
# Implement your own forEach function and use it to greet all the people in the persons array (say Hi, persons name).
# Read about forEach https:#developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach
print('Task 2')

# Assuming you have already created the 'persons' array

# Implementation of the forEach function
def forEach(array, callback):
    for element in array:
        callback(element)

# Function to greet a person
def greet_person(person):
    print("Hi, " + person['name'])

# Using the forEach function to greet all the people
forEach(persons, greet_person)



# 3
# Implement your own map function and make everyone a year older.
# You can read about what the map function should do https:#developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map 
print('Task 3')

# Implementation of the map function
def map_array(array, callback):
    result = []
    for element in array:
        result.append(callback(element))
    return result

# Function to make a person a year older
def make_person_older(person):
    person['age'] += 1
    return person

# Using the map function to make everyone a year older
persons_older = map_array(persons, make_person_older)
print(persons_older)



# 4
# Implement your own filter function, and use it to find evryone under the drinking age.
# Read about filter https:#developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter
print('Task 4')

# Implementation of the filter function
def filter_array(array, callback):
    result = []
    for element in array:
        if callback(element):
            result.append(element)
    return result

# Function to check if a person is under the drinking age
def is_under_drinking_age(person):
    return person['age'] < 21

# Using the filter function to find everyone under the drinking age
under_drinking_age = filter_array(persons, is_under_drinking_age)
print(under_drinking_age)



# 5
# Now create a function sum, that takes a list of numbers and returns the sum
# Try to use your previously created functions to make this function 
# Sum the total age of persons using this new function 
# NB! Do not manually create the age listing
print('Task 5')

# Implementation of the sum function using reduce
def sum(numbers):
    return reduce(numbers, lambda acc, x: acc + x, 0)

# Using the sum function to find the total age of persons
total_age = sum(map_array(persons, lambda person: person['age']))
print(total_age)



# 6
# Now create a function average, that returns the average of a list of numbers
# Try to use your previously created functions to make this function 
# calculate the average age of the persons using this function
# NB! Do not manually create the age listing
print('Task 6')

# Implementation of the average function using reduce and sum
def average(numbers):
    return sum(numbers) / len(numbers)

# Using the average function to calculate the average age of persons
average_age = average(map_array(persons, lambda person: person['age']))
print(average_age)



# 7
# Finally, create a max and a min function that respectively returns the maximum value and the minimum value
# Only use previously created functions to achieve this.
# Then find the min and max age of the persons.
print('Task 7')

# Implementation of the max function using reduce
def max_value(numbers):
    return reduce(numbers, lambda x, y: x if x > y else y, float('-inf'))

# Implementation of the min function using reduce
def min_value(numbers):
    return reduce(numbers, lambda x, y: x if x < y else y, float('inf'))

# Using the max and min functions to find the min and max age of persons
ages = map_array(persons, lambda person: person['age'])
max_age = max_value(ages)
min_age = min_value(ages)

print("Maximum age:", max_age)
print("Minimum age:", min_age)



