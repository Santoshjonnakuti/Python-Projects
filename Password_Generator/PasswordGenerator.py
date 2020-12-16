import random
list1 = ['!', '@', 1, '#', 8, '$', 6, '%', '&', 5, '*', '(', 9, ')', 7, '_', 3, '+', '=', 4, '.', ',', 0, ':', '/', '-', 2]
name = input("Enter a string that should be included in the password : ")
length = len(name)
number = random.randint(1, length//2)
new_name = ''
for i in range(number):
    position = random.randint(0, length-1)
    if i == 0:
        new_name = name[0:position] + name[position].upper() + name[position + 1:]
    else:
        new_name = new_name[0:position] + new_name[position].upper() + new_name[position + 1:]
required_length = 15 - length
password = ''
for i in range(required_length):
    p = random.choice(list1)
    password = password + str(p)
position = random.randint(0, required_length)
new_password = password[:position-1] + new_name + password[position-1:]
print(new_password)
