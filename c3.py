#task 3.test
justice_league = ["Superman","Batman","WonderWoman","Flash","Aquaman","Green Lantern"]
#1.to find number of words
num_words=len(justice_league)
print(justice_league)
print(num_words)
#2.insetr words
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print(justice_league)
#3.to move wonder women first
justice_league.remove("WonderWoman")
justice_league.insert(0,"WonderWoman")
print(justice_league)
#4.to insert between
justice_league.remove("Superman")
index=justice_league.index("Aquaman")
justice_league.insert(index,"Superman")
print(justice_league)
#5.to creat new list
justice_league=["Cyborg","Shazam","Hawkgirl","MartianManhunter","Green Arrow"]
#6.sorting the list
justice_league.sort()
print(justice_league)
#new leader
x=f"newleader is {justice_league[0]}"
print(x)



