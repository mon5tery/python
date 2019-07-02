from datetime import date


#birthdate = (year, month, day)
def check_birthdate(year, month, day):
	present = date.today()
	birthdate = date(year, month, day)
	if present > birthdate:
		return(True)
	else:
		return(False)

def calculate_age(year, month, day):
	present = date.today()
	birthdate = date(year, month, day)
	#returns timedelta which can be used in age.days.
	age = present - birthdate
	age_days = age.days
	
	year = int(age_days / 365)
	age_days = int(age_days % 365)
	#age_days %= 365
	month = int(age_days / 30)
	age_days = int(age_days % 30)

	#year = present.year - year
	#month = present.month - month
	#day = present.day - day
	
	#int can be put in the last print and doesn't have to be as the top
	# I.E: print("You are %d years, %d months, and %d days" % (int(year),int(month), age_days)
	print ("You\'re %d years, %d months, and %d days" % (year, month, age_days))
	



	#print (present - birthdate)
#make sure that the primary variables (year, month, day) are integers from the root.
year = int(input("Enter year of birth: "))
month = int(input("Enter month of birth: "))
day = int(input("Enter day of birth: "))

if check_birthdate(year, month, day):
	calculate_age(year, month, day)
else:
	print ("The birthdate is invalid")