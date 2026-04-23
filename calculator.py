num1= input("Enter the 1st number: ")
num2= input("Enter the 2nd number: ")
a=float(num1)
b=float(num2)
op=input("Enter the operation(+,-,*,/): ")
if op== '+':
    result= a+b
elif op=='-':
    result=a-b
elif op=='*':
    result=a*b
elif op=='/':
    if b!=0:
        result=a/b
    else:
        print("Cannot divide by zero")
        result = None
else:
    print("Invalid input")
    result= None

if result is not None:
    print("Result:" , result) 