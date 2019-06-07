#Program to calculate sum of numbers in digit
ele=int(input("Enter an element:"))
sum=0
while ele:
    sum=sum+(ele%10)
    ele=ele//10
print("The sum of digits are:",sum)
