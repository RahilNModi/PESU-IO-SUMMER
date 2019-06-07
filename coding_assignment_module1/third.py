#Program to implement binary search
ele=[]
count=int(input("Enter the number of elements required:"))
key=int(input("Enter the key element:"))
i=0
while(i<count):
    c=int(input("Enter the  element:"))
    ele.append(c)
    i=i+1
print(ele)
low=0;high=count-1;flag=0
while(low<high):
    mid=int((low+high)/2)
    if(ele[mid]==key):
        flag=1
    elif ele[mid]<key:
        high=mid-1
    else:
        low=mid+1
if flag==0:
    print("Not present")
else:
    print("Index:",mid,"  Position:",mid+1)
