str_numbers = "456"
str_numbers_to_int = int(str_numbers)
print("Before casting :", str_numbers, ", the data type is", type(str_numbers))
print("After casting :", str_numbers_to_int, ", the data type is", type(str_numbers_to_int))

Integer = 12345
integer_to_str = str(Integer)
print("Before casting :", Integer, ", the data type is", type(Integer))
print("After casting :", integer_to_str, ", the data type is", type(integer_to_str))

num_int = 1
num_bool = bool(num_int)
print(num_bool, type(num_bool))

num_int = 0
num_bool = bool(num_int)
print(num_bool, type(num_bool))

# Equal to
8 == 8
# Not equal to
8 != 9
# Greater than
8 > 9
# Less than
8 < 9
# Less than
8 <= 9
# Less than
8 >= 9

a = True
b = True
print(a and b)
print(a or b)
print(not b)

#logic
5 > 6 and 6 < 7

e = 8
f = 2

# summation
sum = e + f
print(f"The sum of e with f is : {sum}\n")

# Reduction
red = e - f
print(f"The reduction of e with f is : {red}\n")

# Multiplication
mul = e * f
print(f"The multiplication of e with f is : {mul}\n")

# Division
divi = e / f
print(f"The division of e with f is : {divi}\n")

# Modulo
mod = e % f
print(f"The modulo of e with f is : {mod}\n")

# Power
pow = e ** f
print(f"The power of e with f is : {pow}\n")

# Input
name = str(input("Enter your name : "))
age = int(input("Enter your age : "))

print("Name: ", name)
print("Age: ", age)

# normal print
print('Hi all! am', name, 'age',age,'years old')
# format print
print(f'Hi all! am{name} age{age} years old')
# format print
print(f'Hi all! I am %s age %d years old'%(name, age))
# format output
print(30*"=")
print("Temperature Calculator Program")
print(30*"=")

#Using If-Else
try:
  your_GPA = float(input("Enter your GPA: "))
  if 4.0 >= your_GPA >= 0.0:
    if 4.0 >= your_GPA >= 3.80:
      print(f"Damn you've got a magna cumlaude with your {your_GPA} GPA")
    elif 3.50 <= your_GPA < 3.80:
        print(f"You've got a good cumlaude with your {your_GPA} GPA")
    elif 3.00 <= your_GPA < 3.50:
        print(f"You've got a stable GPA tho")
    elif your_GPA < 3.0:
        print(f"You need a stable GPA")
  else:
    print(f"sorry,your_GPA {your_GPA} is out of range and invalid")
except:
  print("Please enter a valid GPA")

#Using match case
try:
  status_code = int(input("Enter a status code: "))
  print("Your code means")
  match status_code:
    case 200:
      print("Succes")
    case 400:
      print("Bad Request")
    case 401:
      print("Unauthorized")
    case 402:
      print("Payment Required")
    case 403:
      print("Forbidden")
    case 404:
      print("Not Found")
    case 500:
      print("Internal Server Error")
    case 501:
      print("Not Implemented")
    case 502:
      print("Bad Gateway")
    case 503:
      print("Service Unavailable")
except :
         print("Please enter a valid status code")

         
#Ternary
a = 3
b = "Even Number" if a % 2 == 0 else "Odd Number"
print(b)

#Using Loops
for i in range(5):
  print(i)
0
1
2
3
4
# For loop with range
for i in range(5):
  print("Data science is easy")

print(50*"=")

for i in range(1, 5, 2):
  print("Data science is easy")

  word = "I want to master data science"
for letter in word:
  print(letter)

  # you can use it with enumerate function
for m, n in enumerate(word):
  print(f"Index {m}. {n}")

  # it can go backwards
for i in range(5,1,-1):
  print("I want big data's")

  #Keyword control
for i in range(5):
  if i == 2:
    continue # skip theis loop when i is equal to 2
  if i == 4:
    break # stops the loop when i is equal to 4
  print(i)

  # Using while loop
count = 0
while count < 0:
  print("Keep the spirits up interns!")
  count += 1