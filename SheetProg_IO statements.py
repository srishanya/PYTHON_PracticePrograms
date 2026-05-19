# Q1 Print Welcome
print("Welcome")

# Q2 Print given word
word = input("Enter a word: ")
print(word)

# Q3 Print given message
message = input("Enter a message: ")
print(message)

# Q4 Print given integer number
num = int(input("Enter an integer: "))
print(num)

# Q5 Print given fractional number
fraction = float(input("Enter a fractional number: "))
print(fraction)

# Q6 Print fractional number in 2 digit decimal format
fraction = float(input("Enter a fractional number: "))
print(f"{fraction:.2f}")

# Q7 Print integer in Hexadecimal format
num = int(input("Enter an integer: "))
print(hex(num))

# Q8 Print integer in Octal format
num = int(input("Enter an integer: "))
print(oct(num))

# Q9 Print hexadecimal number in integer format
hex_num = input("Enter a hexadecimal number: ")
print(int(hex_num, 16))

# Q10 Print octal number in integer format
oct_num = input("Enter an octal number: ")
print(int(oct_num, 8))

# Q11 Print ASCII value of a character
ch = input("Enter a character: ")
print(ord(ch))

# Q12 Print character for given ASCII value
ascii_val = int(input("Enter an ASCII value: "))
print(chr(ascii_val))

# Q13 Print two numbers with space
print(10, 20)

# Q14 Print two numbers with tab space
print(10, "\t", 20)

# Q15 Print two numbers in two lines
print(10)
print(20)

# Q16 Print a character in single quotes
ch = input("Enter a character: ")
print(f"'{ch}'")

# Q17 Print two words in double quotes
print('"Hello World"')

# Q18 Print DOB in DD/MM/YYYY
print("19/05/2006")

# Q19 Print integer with plus sign
num = int(input("Enter an integer: "))
print(f"+{num}")

# Q20 Print size of datatypes
import sys
print("Size of char:", sys.getsizeof('a'))
print("Size of int:", sys.getsizeof(1))
print("Size of float:", sys.getsizeof(1.0))
print("Size of double:", sys.getsizeof(1.23456789))

# Q21 Print roll number and name
roll_no = int(input("Enter roll number: "))
name = input("Enter name: ")
print(f"Roll No: {roll_no}, Name: {name}")

# Q22 Print marks in 5 subjects
marks = [90, 85, 78, 92, 88]
for m in marks:
    print(m)

# Q23 Print blood group
print("Blood Group: O+")
print("Blood Group: A-")
print("Blood Group: B+")
print("Blood Group: AB-")
print("Blood Group: O-")
print("Blood Group: A+")
print("Blood Group: B-")
print("Blood Group: AB+")

# Q24 Print current time HH:MM:SS
import time
print(time.strftime("%H:%M:%S"))

# Q25 Print address in multiple lines
print("123 Street\nCity\nCountry")