'''
Exercise

1. Create a list of your 5 favourite fruits and print it.

2. Print the first and last elements of the list.

3. Change the second item in the list to "Mango".

4. Insert: Add "Watermelon" at index 2.

5. Check existence: Write a program that asks the user for a fruit name and checks if it's in the list.

6. Sort the list alphabetically.

'''

lis=["corn","strawberry","apple","pineapple","carrot"]

print (lis[0])
print (lis[-1])

lis[1]="mango"
print (lis)

lis.insert (2,"watermelon")
print (lis)

fruit= input("Enter fruit name : ")

if lis.count(fruit) != 0:
    print("Yes, the fruit is in the list.")
else:
    print("No, the fruit is not in the list.")

lis.sort()
print (lis)
