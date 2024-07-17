# Accept user input to create a list of integers
user_input = input("Enter list of integers separated by spaces: ")

# Split the input string into individual elements (substrings) and convert them to integers
integer_list = [int(x) for x in user_input.split()]

# Print the list of integers
print("List:", integer_list)

# Compute the sum of all the integers in the list
sum_of_integers = sum(integer_list)

# Print the sum of the integers
print("Sum of all integers:", sum_of_integers)

#Create a tuple containing the names of five of your favorite books. 
fav_books = ("Things Fall Apart", "Finding Chika", "Tales of an Economic Hitman",
             "A Slave Ship Called Jesus", "Kiss From a Rose")
print("My Favorite Books:", fav_books)

#Then, use a for loop to print each book name on a separate line.
for fav_book in fav_books:
    print(fav_book)    

# Initialize an empty dictionary to store the person's information
person_info = {}

# Ask the user for their name, age, and favorite color
name = input("Enter your name: ")
age = input("Enter your age: ")
favorite_color = input("Enter your favorite color: ")

# Store the information in the dictionary
person_info["Name"] = name
person_info["Age"] = age
person_info["Favorite Color"] = favorite_color

# Print the dictionary to the console
print("Person Information:", person_info)

# Function to create a set from user input
def create_set():
    # Prompt the user to enter integers separated by spaces
    user_input = input("Enter integers separated by spaces: ")
    # Split the input string into a list of strings
    input_list = user_input.split()
    # Convert the list of strings to a set of integers
    int_set = set(map(int, input_list))
    return int_set

# Create the first set
print("Enter the elements for the first set:")
set1 = create_set()

# Create the second set
print("Enter the elements for the second set:")
set2 = create_set()

# Create a new set containing only the elements common to both sets
common_elements_set = set1.intersection(set2)

# Print the common elements set
print("Common elements set:", common_elements_set)

# List of words
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

# Use list comprehension to create a new list with words that have an odd number of characters
odd_length_words = [word for word in words if len(word) % 2 != 0]

# Print the new list
print("Words with an odd number of characters:", odd_length_words)
