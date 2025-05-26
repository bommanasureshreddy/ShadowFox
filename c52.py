#task 5.forloop(2)
reply=0
out=0
out_1=0
for x in range(1,100) :
    if x%10==0 and x!=100:
        reply=input("are you tirde  ")
        if reply.lower()=="yes" or reply.lower()=="y" :
            reply_1=input("do you want to skip the remaining sets")
            if reply_1.lower()=="yes" or reply_1.lower()=="y":
                out=f"you completed a total of {x} events"
                print(out)
                break
            elif reply_1.lower()=="no" or reply_1.lower()=="n" :
                 out_1=f"{100-x} are remaining jumping jacks"    
                 print(out_1) 
        elif reply.lower()=="no" or reply.lower()=="n" :
            out_2=f"{100-x} are remaining jumping jacks"    
            print(out_2)  
    elif x==100 :
        print("congratulation! you completed the workout")