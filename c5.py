#task 5.forloop (1)
count_6=0
count_1=0
count_6_6=0
y=[0]*20
for x in range(20) :
    y[x]=int(input("die roll"))
    if y[x]==6 :
        count_6=count_6+1
    elif y[x]==1 :
        count_1=count_1+1  
    elif y[x]==6 and y[x+1]==6 :
        count_6_6=count_6_6+1
x=f"6 rolled ,{count_6} times"
y=f"1 rolled ,{count_1} times"
z=f"two 6s rolled ,{count_6_6} times"
print(x)
print(y) 
print(z)      

