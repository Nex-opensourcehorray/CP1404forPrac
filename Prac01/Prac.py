age = int(input("Plz input the age: "))
total = 0
count = 0
while age >= 0:
    total += age
    count += 1
    age = int(input("Plz input the age: "))
print("Total: ", total)
print(total / count)

gift = int(input("Plz input the gift counting: "))
student = int(input("Plz input the student counting: "))
Avg_gift_count = gift // student
remain_gift = gift % student
print(Avg_gift_count)
print(remain_gift)

GST_RATE = 1.09
GST_NO_RATE = 1.00
gst_confirm = input("Does it have GST?")
gift_price = float(input("The item price: "))

if gst_confirm == 'y':
    gift_price *= GST_RATE

print(f"The Gift price is: {gift_price:.2f}")

number = int(input("Plz input the number: "))

for count in range(1, number, 2):
    print(count, end=' ')
print(end='\n')

SECRET_NUMBER = 7
get_number = int(input("Plz input your answer: "))

while get_number != SECRET_NUMBER:
    print("Wrong number! do it again!")
    get_number = int(input("Plz input your answer: "))

print("Congrats! You win!")

name = input("Plz input your name: ")
salary = int(input("Plz input your salary: "))

while name == "":
    print("Can not be blank!")
    name = input("Plz input your name: ")

while salary < 0:
    print("invalid income!")
    salary = input("Plz input your salary: ")
