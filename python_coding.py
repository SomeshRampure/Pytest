#1. print Hello world
print("Hello World")

#2. Take two numbers as input and print their sum.
a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
sum = a + b
print("Sum of a and b : ", sum)

#3. to check if a number is even or odd.
l = [1,2,3,4,5,6,7,8,9]
for i in l:
    if i % 2 == 0:
        print("Even number")
    else: 
        print("Odd number")

#4. to print numbers from 1 to 10 using a loop
for i in range(1, 11):
    print(i)

#5. to find the factorial of a number.
n = int(input("Enter a number : "))
fact = 1
for i in range (1, n+1):
    fact *= i
    print(fact)

6#. to check if a given string is a palindrome
s = input("Enter a string : ")
if s == s[::-1]:
    print("Palindrome")
else: 
    print("Not a palindrome")

#7. to find the largest number in a list.
l = [1,3,5,6,7]
largest = l[0]
for num in l:
    if num > largest:
        largest = num
        print(largest)

#8. to reverse a list.
l = [1,2,3,4]
s = l[::-1]
print(s)

#9. to find the sum of all elements in a list.
s = [1,2,3,4,5]
sum = 0
for i in s:
    sum += i
    print(sum)

#10. to check if a given list contains any duplicate elements.
l = [1,2,2,3,3,4,4]
s = set(l)
if len(l) != len(s): print("duplicates")
else : print("Not duplicate")

#11. to count the number of even numbers in a list.
l = [1,2,3,4,5,6,7,8]
count = 0
for i in l:
    if i % 2 == 0: count += 1
    print (count)

#12. to remove duplicates from a list and return a new list with unique elements.
l = [1,1,2,2,3,4,4,5]
s = list(set(l))
print(s)

#13. to sort a list in ascending order.
s = [1,2,3,4,5,6,7,8]
s.sort()
print(s)