name = "I am Carl"
print(name)
do_not = "oh no that broke it"
print(do_not)
uhoh = name +"  " + do_not
print(uhoh)
first_num = 17
print(first_num)
first_num = 17 + 7
print(first_num)
sent_pt_one = "I am "
sent_pt_two = " years old!"
age = first_num
print(age + 1)
new_num = 14
print(age / new_num)

# not sure why these two refuse to work yet
subscribed = not False
prevent_logout = True
available = True
print(not available)
saved_pin = 1245
entered_pin = 1234
print(saved_pin == entered_pin)
print(saved_pin != entered_pin)
bad_pin = saved_pin != entered_pin
print(bad_pin)
# if entered_pin == saved_pen then print("Correct Pin")
pin_difference=saved_pin<entered_pin
print(pin_difference)
# this will return false below
print(10<1)
print(12 <= 43)
print(saved_pin >= entered_pin)
battery_level = 10
low = battery_level <= 20
print("Low battery:")
print(low)
pie = 3.14159
print(f"{2} new messages")
print(f"{entered_pin} is not the correct pin")
if True:
	print("Hello!")
if False:
	print("Goodbye!")
if True:
	print("This will print because the contition is True")
if False:
	print("This will not print because the condition is False")
#code blocks
if True:
	print("This is the first line of a code block")
	print("all lines with the same indentation will belong to the same block")
greet = True
if greet:
	print("Hello again!")
insult = False
if insult:
	print("Well thats not very nice")
answer = "Tacos"
if answer == "Tacos":
	print("Good good")
if answer != "Tacos":
	print("Hmm... Lets try Taco Bell instead")
score = 75
if score >= 85:
	print("Congrats you passed the test!")
available = True
if available:
	print("In stock")
unavailable = True
if not unavailable:
	print("In stock.")
else:
	print("Not in stock")
canadians = 5
if canadians ==13:
	print("Confirmed lock on 13 canadians")
else:
	print("Cannot lock on all thirteen canadians")
hour = 14
if hour < 12:
	print("Good Morning")
elif hour < 17:
	print("Good Afternoon")
elif hour < 23:
	print("Good Night")
else:
	print("Go to sleep you nocturnal opposum")
if hour < 17 and canadians == 5:
	print("Good luck decifering this")
usn = "toddswaen76"
psd = "fgah176"
eusn = "toddswaen76"
epsd = "fgah176"
if usn == eusn and psd == epsd:
	print("Welcome Back toddswaen76")
else:
	print("Password or Username incorrect")
	print("Please try again")
if usn == eusn or psd != epsd:
	print("That works almost")
potatoes = 37
tomatoes =95
if potatoes > 100 or tomatoes < 3:
	print("Do not order more Potato/Tomato combo packs")
else:
	print("Don't forget to order tomato/potato combo packs")
# or command only skips code if all statements are false
# or is good for linking alternative conditions
if potatoes == 37 or tomatoes < 3:
	new_order = True
else:
	new_order = False
print(new_order)
#
#▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎
#start of loops
print("------------------------------")
print("Start of loop usage")
wallet = 3
print(wallet)
wallet = wallet
print(wallet)
wallet = wallet + 1
print(wallet)
wallet = wallet + 2
wallet = wallet - 1
print(f"You have ${wallet}")
name = name + ", how are you?"
print(name)
wallet += 3
funds = f"You have ${wallet}"
print(funds)
wallet += 7
wallet-= 2
print(funds)
funds = f"You have ${wallet}"
print(funds)
keep_going = True
while keep_going == True:
	print("loop and ")
	keep_going = False
	print("one more time")
counter = 1
while counter <= 8:
	print(counter)
	counter += 1
print("Count Complete")
tacos = 23
while tacos >= 2:
	print(f"You have {tacos} tacos left")
	tacos -= 1
	if tacos == 1:
		print(f"You only have {tacos} taco(s) left")
#the variables counter and taco are called  counter variables
first_counter = 0
while first_counter < 5: 
  print("**********---------")
  first_counter += 1
second_counter = 0
while second_counter < 4:
  print("-------------------")
  second_counter += 1
for i in range(5):
	print(i)
	print("tacos")
# i is counter var
todo = ["Coffee", "Eat", "Code"]
print(todo)
temperatures = [37, 47, 50, 73, 74, 76]
print(temperatures[4])
print(todo[2])
print(temperatures[0])
print("changing temperature list")
print(temperatures)
temperatures[1] = 44
print(temperatures)
temperatures.append(78)
print(temperatures)
temperatures.insert(2, 49)
print(temperatures)
temperatures.pop()
print(temperatures)
temperatures.pop(2)
print(temperatures)
temperatures.append(78)
removed = temperatures.pop(3)
print(removed)
print(len(temperatures))
print(len(todo))
for temps in temperatures:
	print(temps)