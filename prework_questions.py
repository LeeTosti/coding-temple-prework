#Question 1
#Write a function tp print "hello_USERNAME!" USERNAME is the input of the function. 
def greeting(username):
    """Display a greeting to the user."""
    print(f'\n"Hello, {username.upper()}!"')

greeting('lee')

#Question 2
#Write a function that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    """Display all odd numbers from 1 to 100."""
    #Determin odd numbers by setting a range and stepping up by 2
    odd_numbers = range(1, 101, 2)
    #Create a for loop to move through all the the odd numbers in the range
    for odd in odd_numbers:
        #print all the odd numbers that moved through the for loop
        print(odd)
#call the function    
first_odds()

#Question 3
#Write a function to return the max number of a given list
def max_num_in_list():
    """Return the maximum number in the list."""
    #Create list of numbers
    numbers = [4, 8, 15, 16, 23, 42]
    #Find max number in list
    max_number = max(numbers)
    #Return max number in list
    return(max_number)
#Assign variable to function
highest_number = max_num_in_list()
#Print variable
print(highest_number)

#Question 4
#Write a function to return boolean if a given year is a leap year
def is_leap_year():
    """Return if a year is a leap year"""
    #Create an input prompt to obtain a year
    year = input(f"Please enter a year: ")
    #Change year from class str to class int
    year = int(year)
    #Determine if a year is divisible by 4 but not divisible by 100
    if year % 4 == 0 and year % 100 != 0:
        return True
    #Determine if a year is divisible by 400
    elif year % 400 == 0:
        return True
    #Determine if year does not meet parameters of previous conditional tests
    else:
        return False
#Assign variable to function    
leap_year = is_leap_year()
#Print varible
print(leap_year)

#Question 5
#Write a fucntion to check if all numbers in list are consecutive numbers and return a boolean
def is_consecutive(a_list):
    """Return if numbers in list are consecutive numbers."""
    #Create a loop that runs through the list one less time than range of the list
    for x in range(len(a_list)-1):
        #Print the index being used
        print(x)
        #Print the number being used plus 1 to get the next number in the list
        print(a_list[x+1])
        #Compare first number to second number
        if a_list[x] > a_list[x+1]:
            #Return False if a_list[x] is greater than a_list[x+1]
            return False
        #Verify if a_list[x+1] minus one is not equal to a_list[x] 
        elif a_list[x+1] - 1 != a_list[x]:
            #Return False if they are not equal
            return False
        #Close loop by returning True if it passed the other conditions
        else:
            return True
    #Return True if loop completes without returing False on any conditions
    return True
#Define list       
a_list = [22, 23, 24, 25, 26, 27]
#Assign variable to function call        
consectutive = is_consecutive(a_list)
#Print variable
print(consectutive)