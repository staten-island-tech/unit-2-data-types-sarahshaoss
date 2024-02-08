
# Function to find gcf of two numbers
def gcf(a, b):
 
    # Find minimum of a and b
    result = min(a, b)
 
    while result:
        if a % result == 0 and b % result == 0:
            break
        result -= 1
 
    # Return the gcd of a and b
    return result
 
 
# Driver Code
if __name__ == '__main__':
    a = 98
    b = 56
    print(f"GCF of {a} and {b} is {gcf(a, b)}")