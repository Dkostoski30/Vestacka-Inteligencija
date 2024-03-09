birthdays = {
    "Daniel": "24/05/2003",
    "John": "22/02/2001",
    "Mary": "20/01/1999"
}
print("We know the birthdays of: ")
for key, value in birthdays.items():
    print(f"{key}")
x = input("Enter a name to get their birthday\n")
print(x + "'s birthday" + " is " + birthdays[x])
answer = input("Enter a name and a birthday to add to the collection\n")
answer = answer.split(' ')
birthdays.update({answer[0]: answer[1]})
print(birthdays)
