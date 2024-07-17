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
