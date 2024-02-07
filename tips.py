bill = int(input("how much was your meal?"))


tip = input("How was the service?")

if tip == "bad":
    print("Your total is")
    print(bill)
elif tip == "okay":
    print("Your total is")
    print(bill * 1.15)
elif tip == "good":
    print("Your total is")
    print(bill * 1.2)
elif tip == "great":
    print("your total is")
    print(bill * 1.25)