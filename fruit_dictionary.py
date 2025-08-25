'''
1. Create a program that stores fruit prices in a dictionary and lets the user enter a fruit name. 


2. If the fruit exists in the dictionary, print its price. 


3. If the fruit doesn’t exist, print "Sorry, this fruit is
not available."

'''

fruit_prices = {
    "apple": 3,
    "banana": 1,
    "orange": 2,
    "mango": 3.5,
    "grape": 2.5
}

fruit = input("Enter a fruit name: ").lower() 

if fruit in fruit_prices:
    print(f"The price of {fruit} is {fruit_prices[fruit]}")
else:
    print("Sorry, this fruit is not available.")
