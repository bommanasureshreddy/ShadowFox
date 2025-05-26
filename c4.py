#task 4.if condition(1)
height=float(input("enter height"))
weight=float(input("enter weight"))
bmi=weight/(height*2)
if bmi>=30 :
    print("Obisity")
elif 25<bmi<=29 :
    print("Overweight")    
elif 18.5<bmi<=25 :
    print("Normal")
elif 18.5<=bmi :
    print("Underweight")