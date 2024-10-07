

# Exercise 1
# Write Python code that prints your name , student number and email address
Name="Ayisha Mubashira"
Student_Number ="ST1001"
Email="ayishamubashira16@gmail.com"

print("Name:",Name)
print("Student_Number:",Student_Number)
print("Email:",Email)

# Exercise 2
# Write Python code that prints your name ,Student Number and Email address using escape sequence
Name="Ayisha Mubashira"
Student_Number="ST1001"
Email="ayishamubashira16@gmail.com"
print(f'{Name}\n{Student_Number}\n{Email}')

# Exercise 3
# Write Python code that add ,Substract ,multiply and divide the two numbers. You can use the two numbers 14 and 7

Num1=14
Num2=7

print(f"{Num1}+{Num2}={Num1+Num2}")
print(f"{Num1}-{Num2}={Num1-Num2}")
print(f"{Num1}*{Num2}={Num1*Num2}")
print(f"{Num1}/{Num2}={Num1/Num2}")

# Exercise 4
# Write Python code that displays the numbers from 1 to 5 as steps
print("1\n2\n3\n4\n5")

# Exercise 5
# Write Python code that outputs the following sentence(Including the quotation marks and line break)to the screen

Sentence="\"SDK\" Stands for \"software Development Kit\",whereas \n\"IDE\"Stands for \"Integrated Development Environment\"."
print(Sentence)


# Exercise 6
# Practice and check the output

print("python is an \"awesome\" language.")
print("python\n\t2023")
print('I\'m from Entri.\b')
print("\65")
print("\x65")
print("Entri", "2023", sep="\n")
print("Entri", "2023", sep="\b")
print("Entri", "2023", sep="*", end="\b\b\b\b")

# Exercise 7
# Define the variables below.Print the types of each variable.What is the sum of your Variables.What datatype is the sum?
Num =23
Textnum="57"
Decimal=98.3

print(type(Num))
print(type(Textnum))
print(type(Decimal))

Sum=Num+int(Textnum)+(Decimal)
print(Sum)
print(type(Sum))

# Exercise 8
# Calculate the number of minutes in a year using variables for each unit of time.Print a statement that describes what your code does
# also Create three variables to store no of days in a year,minutes in a hour,hours in a day . Then calculate the total minutes
# in a year and print the values

print("This code Calculate the total number of minutes in a year")

Days_in_year=365
Minutes_in_hour=60
Hours_in_day=24

Total_minutes_in_a_year = Days_in_year * Hours_in_day * Minutes_in_hour
print(Total_minutes_in_a_year)

# Exercise 9
# Write Python code that asks the user to enter his/her name and then output/prints his/her name with a greeting.

Name =input("Please enter your name:")
print("Hi",Name,"Welcome to the world of python.")
























