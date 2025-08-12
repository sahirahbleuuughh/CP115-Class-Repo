# print("Starting program")
#     print("This line has spaces before it")
# print("Back to normal")

value = 3

if(value == 1):
     print("Value is 1")
else:
  print("Value is not 1")

value = 1

# if(value == 1):
#      print("Value is 1")
#        print("This is an additional print statement.")
# else:
#   print("Value is not 1")

#SNAKE_CASE (this is the convetion at least, or the standard)
student_name = "Ali"
total_price = 150.50
is_passed_exam = True
number_of_items = 5

#CAMELCASE (i much prefer using this one)
#honestly i dont really care about variable naming, as long as it work
#then it's good in my book
studentName = "Ali"
totalPrice = 150.50
isPassedExam = True
numberOfItems = 5

######################################################################

# Using single quotes
name1 = 'Ali'
print(name1)

# Using double quotes  
name2 = "Ali"
print(name2)

# Both produce the same result
print(name1 == name2)  # Output: True

######################################################################

# If your string contains single quotes, use double quotes
message1 = "I can't believe it's working!"
print(message1)

# If your string contains double quotes, use single quotes
message2 = 'He said "Hello there!"'
print(message2)

######################################################################

# Using triple double quotes
long_text = """This is a long text
that spans multiple lines.
You can write as many lines as you want."""
print(long_text)

# Using triple single quotes
poem = '''Roses are red,
Violets are blue,
Python is awesome,
And so are you!'''
print(poem)

a_text = """Please hurrry leave me i cant breathe
please dont say you love me
munegahachikiresode
one word form you and i would jump off of this ledge im on baby
tell me dont so i dcant wrbewhewuiejhjheie"""
print(a_text)

######################################################################

#print("\n") - CREATE A LINE BREAK
#print("\t") - CREATE A TAB SPACING

# Without \t - no spacing
print("Name Age Grade")
print("Ali 20 A")

# With \t - creates neat columns
print("Name\tAge\tGrade")
print("Ali\t20\tA")
print("Sarah\t19\tB+")

# Creating a formatted table
student_data = "Student Information:\n\nName\tAge\tGrade\nAli\t20\tA\nSarah\t19\tB+"
print(student_data)