a=int(input("enter the  no:"))
b=1
p=0
if (a<=2):
    print(b);
elif(a>2):
    if(a%2==0):
        a=a-1;
    print(b,end=",");
    for x in range(1,a,1):
        b=b+2;
        print(b,end=",");
