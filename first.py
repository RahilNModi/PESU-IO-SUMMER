# Program to accept comma seperated values and store them in list and tuple
# First we take it as string and then make them numbers and store them in list itself.
str=input("Enter numbers which are seperated with comma:")
count=0;c=0
a=[]
for i in str:
    if i==',':
        a.append(int(str[c:count]))
        c=count+1
    count=count+1
a.append(int(str[c:count]))
print(a)
print(tuple(a))
