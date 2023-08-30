# Exercise 1
# Create three variables; x, y, z. Assign each a numeric value, then perform
# each of the operands you have learned
x <- 4
y <- 6
z <- 9

x + z
z - y
x * y
z / y
y %/% x
z %% x

# Exercise 2
# Create two strings with your first and last name
first_name = "Lisa"
last_name = "Tosti"

# Concatenate the strings 
full_name <- paste(first_name, last_name, sep=' ')
greeting <- paste("My name is ", full_name)
print(greeting)

#Exercise 3
#Create two numerical vectors of equal length
vec1 <- c(2,4,6,8,10)
vec2 <- c(3,5,7,9,11)

# Multiple the two vectors together
vec1 * vec2

# Save the resulting vector to the variable mult_vect
mult_vect = vec1 * vec2

# Exercise 4
# Using mult_vect, index the vector and return the last four values
mult_vect[2:5]

# Exercise 5
# Generate a sequence of numeric values
4:12

# Save sequence
my_first_sequence <- 4:12
