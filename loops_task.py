list_of_items = []
item_name = ""

while True:
	item_name = input("Item or (write done if finished): ")
	#add the if statement of the True statement within to finish with a break.
	if item_name == "done":
		print("____________________")
		print("\t \t Reciept")
		print("____________________")
		break

	price = float(input("Price: "))
	quantity = int(input("Quantity: "))

	item = {
		"Name": item_name,
		"Price": price,
		"Quantity": quantity
	}

	list_of_items.append(item)


total = 0
for item in list_of_items:
	print("%s %s KD %.3f" % (item["Quantity"], item["Name"], item["Price"]*item["Quantity"]))
	total +=  item["Price"] * item["Quantity"]

print("Your total is %s" % total)