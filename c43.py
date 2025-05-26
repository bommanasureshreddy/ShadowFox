#task 4.if condition(3)
Australia = ["Sydney","Melbourne","Brisbane","Perth"]
UAE = ["Dubai","Abu Dhabi","Sharjah","Ajman"]
India = ["Mumbai","Bangalore","Chennai","Delhi"]
city1=input("enter first city name")
city2=input("enter second city name")
if city1 in Australia and city2 in Australia :
    x=f"{city1},{city2} are in australia"
    print(x)
elif city1 in UAE and city2 in UAE :
    y=f"{city1},{city2} are in UAE"
    print(y)
elif city1 in India and city2 in India :
    z=f"{city1},{city2} are in india"
    print(z)
else :
    a=f"{city1},{city2} are in different countries"