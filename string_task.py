time = input("Give me a number from 1 - 12: ")
items = input("Enter a noun(plural): ")
name = input ("What is your name? ")
# capitalized_name = name.capiatlize()
scream = input("Give me a stupid sentence. ")
action = input("Give me a verb, NOW: ")
print ("Number: " + time)
print ("Items: " + items)
print ("Name: " + name)
print ("Yelling: " + scream)
print ("Action: " + action)
print()
print()
print ("Mad Libs where libs get Mad")
print ("  Start Below:")
print()
print ("  It was %s o'clock when I hears a knock at the door." % (time))
print ("  I opened the door and there was a box full of %s with a note saying 'From Mr. %s'" % (items, name.capitalize()))
