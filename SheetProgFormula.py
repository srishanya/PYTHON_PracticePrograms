# Q1 Sum of two numbers
a, b = 10, 5
print(a + b)

# Q2 Difference
print(a - b)

# Q3 Product
print(a * b)

# Q4 Quotient
print(a / b)

# Q5 Remainder
print(a % b)

# Q6 Swap using third variable
a, b = 10, 20
temp = a
a = b
b = temp
print(a, b)

# Q7 Swap without third variable
a, b = 10, 20
a, b = b, a
print(a, b)

# Q8 Last digit of N
a = int(input("Enter a number: "))
print(a % 10)

# Q9 All digits except last
print(N // 10)

# Q10 Sum of first and last digit of 3-digit number
N = 123
first = N // 100
last = N % 10
print(first + last)

# Q11 Middle digit of 3-digit number
print((N // 10) % 10)

# Q12 Absolute value
num = -42
print(abs(num))

# Q13 Square
num = 5
print(num ** 2)

# Q14 Cube
print(num ** 3)

# Q15 Average of three numbers
a, b, c = 10, 20, 30
print((a + b + c) / 3)

# Q16 Check equality
a, b = 10, 10
print(a == b)

# Q17 Check if number is power of 2
n = 16
print(n > 0 and (n & (n - 1)) == 0)

# Q18 Positive or Negative
num = -5
print("Positive" if num >= 0 else "Negative")

# Q19 Greatest of three numbers
a, b, c = 10, 20, 15
print(max(a, b, c))

# Q20 Pass/Fail
marks = 35
print("Pass" if marks >= 40 else "Fail")