print ("Welcome to my humble company where dreams are crushed and people are grinded.")

skills = ["Python", "C++", "Javascript", "HTML", "CSS", "React"]
cv = {}


#you can use the below too:
	#cv["name"] = input("name: ")
name = input("Name: ")
cv["Name"] = name

age = int(input("Age: "))
cv["Age"] = age

experience = input("Years of experience: ")
cv["Experience"] = experience

cv["Skills"] = []

print("Skills: ")
print("1. %s" % skills[0])
print("2. %s" % skills[1])
print("3. %s" % skills[2])
print("4. %s" % skills[3])
print("5. %s" % skills[4])


skill1 = input("Choose a skill from the list above: ")
cv["Skills"].append(skills[int(skill1) - 1])
#cv["skills"].append(skills[int(skill1)-1])

skill2 = input("Choose another skill from the list above: ")
cv["Skills"].append(skills[int(skill2) - 1])

if (int(cv["Age"]) >= 17 and int(cv["Age"]) < 40) and (cv["Skills"][0] == skills[0] or cv["Skills"][1] == skills[1]):
	print("You're quialified, %s." % cv["Name"])
else:
	print("We regret to inform you that your're underqualified.")