def factors(n, i):
 
    # Checking if the number is less than N
    if (i <= n):
        if (n % i == 0):
            print(i, end = " ");
         
        # Calling the function recursively
        # for the next number
        factors(n, i + 1);
     
# Driver code
if __name__ == '__main__':
    N = 12;
    factors(N, 1);