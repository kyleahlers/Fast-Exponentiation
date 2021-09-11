# Fast Exponentiation
# Ask the user to enter 2 integers a and b and output a^b (i.e. pow(a,b)) 
# in O(lg n) time complexity.


# Determine method to split number of iterations into smaller chunks, ie.
# if b is 8 in the above example, cut it in half to four calculations, etc

def is_even(num):
    if num%2 == 0:
        return True
    else:
        return False
###########################################################################

# basic method that uses a for loop
# this method has O(n) time complexity
# this method uses b iterations. so if b is 8, there are 8 steps
def slow_pow(a,b):
    
    base = int(a)
    exponent = int(b)

    result = 1
    
    for i in range(0,exponent):
        
        result = result*base

    return result
    
###########################################################################

def pow(a,b):
    
    base = int(a)
    exponent = int(b)

    
    finished = False
    extra_term = 1
    
    if exponent == 1:
        finished = True
    elif exponent == 0:
        base = 1
        finished = True
        
    while finished == False:

        #2^8 = 2*2 ^ 4 = 4*4 ^2 = 16*16 ^ 1
        # check if exponent is even
        if is_even(exponent) == True:

            base = (base*base)
            exponent = exponent / 2

        # check if exponent is odd
        elif is_even(exponent) == False:
            
            
            extra_term = extra_term * base
            
            #print(extra_term)
            base = base*base
            exponent = (exponent-1)/2
    
        ###
        
        if exponent == 1 and extra_term == 1:
            finished = True
            break
            
        elif exponent == 1 and extra_term !=1:
            base = base * extra_term
            finished = True
            break 
    
    # end of loop    
    
    return base

