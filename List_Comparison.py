import time
list1 = [23, 45, 68, 24]
list2 = [23, 75, 45, 17]
list3 = [23, 75, 45, 17]

if list2 == list3:
	print("List 2 and 3 are equal")
if list1 == list2:
	print("list 1 and 2 are equal")
else:
	print("list 1 and 2 are not equal")
	
if list1[0] == list2[0]:
	print("values are equal")

while True:
	if list1[3] != list3[3]:
		modifier = True
	elif list1[3] == list3[3]:
		modifier = False
	if modifier == True:
		list3[3] = 1 + list3[3]
		print(list3)
		time.sleep(0.25)
	if modifier == False:
		break
print("done")
