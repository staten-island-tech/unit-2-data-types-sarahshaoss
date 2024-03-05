def ispangram(y):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for x in alphabet:
        if x not in y.lower():
            return False
    return True
     
# Driver code
string = input("Enter")
if(ispangram(string) == True):
    print(string,", Is a pangram")
else:
    print(string,", Is not a pangram")
