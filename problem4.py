input_number=[1,2,8,9,12,46,76,82,15,20,30]
number=[1,2,3,4,5,6,7,8,9]
output={}
for x in number:
    count=0;
    for j in input_number:
        if j%x==0:
            count=count+1;
    output[x]=count;
print(output);
    

