# import necessary libraries as well as functions from exponent.py file
from timeit import default_timer as timer
import exponent

####################################################
# timing function that takes base value, exponent value and number of iterations as arguments
def fast_exp_timer(a,b,iterations = 100):
    start = timer()

    for i in range(0,int(iterations)):
        exponent.pow(a,b)

    end = timer()

    return(end - start)

####################################################

# timing function that takes base value, exponent value and number of iterations as arguments
def slow_exp_timer(a,b,iterations = 100):
    start = timer()

    for i in range(0,int(iterations)):
        exponent.slow_pow(a,b)

    end = timer()

    return (end - start)

####################################################
# Interactive script with instructions via print statements
print("Let's compare some functions with O(n) time complexity vs O(log n) time complexity!")
a = input("Select your base value to compute: ")
b = input("Select your exponent value to compute: ")
iterations = input("Select the number of iterations you would like to run: ")

fast = fast_exp_timer(a,b,iterations)
print('Almost there..')
slow = slow_exp_timer(a,b,iterations)
print('Finished!\n')

print(f"Through {iterations} iterations - the results are as follows!: ")
print(f"O(log n): {fast} seconds")
print(f"O(n): {slow} seconds\n")
