from datetime import date

present = date.today()

#birthdate = (year, month, day)
def check_birthdate(year, month, day):
	if present > date(year, month, day):
		return(True)
	else:
		return(False)

def calculate_age(year, month, day):
	dob = present - date(year, month, day)

	year = present.year - year
	month = present.month - month
	day = present.day - day
	
	print ("You\'re %d years, %d months, and %d days" % (year, month, day))
	



	#print (present - birthdate)

year = int(input("Enter year of birth: "))
month = int(input("Enter month of birth: "))
day = int(input("Enter day of birth: "))

if check_birthdate(year, month, day) == True:
	calculate_age(year, month, day)
else:
	print ("The birthdate is invalid")