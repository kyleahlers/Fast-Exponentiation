import exponent
from timeit import default_timer as timer

print("This program computes a ^ b in O(log n) time complexity")
a = input("Please select your base value: ")
b = input("Please select your exponent value: ")

start = timer()
answer = exponent.pow(a,b)
end = timer()

print(f"The result of {a}^{b} is {answer}")
print(f"This computation had O(log n) time complexity and took {end-start} seconds")
