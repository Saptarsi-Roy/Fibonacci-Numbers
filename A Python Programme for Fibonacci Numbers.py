# Write a Python Programme for Fibonacci Numbers.

                         ###Using For loop###

Fn=int(input("Enter no of Series:- "))
a=int(input("Enter the 1st Value:- "))
b=int(input("Enter the 2nd Value:- "))
print(a)
print(b)
for i in range (Fn):
        c=a+b
        a=b
        b=c
        print(c)
    

                        ### Using While Loop ###


a=0
b=1
print(a)
print(b)
while a>=0 and b>=1:
    c=a+b
    a=b
    b=c
    print(c)
