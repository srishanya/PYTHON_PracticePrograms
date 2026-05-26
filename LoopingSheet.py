# LOOP PROGRAMS SHEET PRACTICE PROGRAMS
#Q1. First digit of a number
n = int(input()) # 12345
first_digit = n // (10 ** (len(str(n)) - 1))
print(first_digit) # Output: 1

#Q2 First digit odd or even
n=int(input())
while n>=10:
    n//=10
print("Even" if n%2==0 else "Odd")

#Q3. Check digit occurrenc
n = int(input()) # 12345
digit = int(input()) # 3
count = 0
while n != 0:
    last = n % 10 # 5, 4, 3, 2, 1
    if last == digit: # when last is 3
        count += 1 # count is 1
    n //= 10 # 1234, 123, 12, 1, 0
print(count) # Output: 1

#Q4. Count digit occurrence
n = int(input())
digit = int(input())
count = 0
while n != 0:
    last = n % 10
    if last == digit:
        count += 1
    n //= 10
print(count)

#Q5 Digit ascending order
n=input()
print("Ascending" if all(n[i]<=n[i+1] for i in range(len(n)-1)) else "Not Ascending")

#Q6: Digits descending order
n=input()
print("Descending" if all(n[i]>=n[i+1] for i in range(len(n)-1)) else "Not Descending")

#Q7: Swap first and last digit
n=input()
if len(n)==1:
    print(n)
else:
    print(n[-1]+n[1:-1]+n[0])


#Q8:Frequency of each digit
n=input()
freq=[0]*10
for ch in n:
    freq[int(ch)]+=1
for i in range(10):
    if freq[i]>0:
        print(i,":",freq[i])

#Q9: Largest digit
n=input()
print(max(n))

#Q10: Smallest digit
n=input()
print(min(n))

#Q11. All digits even/odd/mixed
n=input()
if all(int(ch)%2==0 for ch in n):
    print("All Even")
elif all(int(ch)%2==1 for ch in n):
    print("All Odd")
else:
    print("Mixed")

#Q12 : Difference between sum of even and odd digits
n=input()
even=sum(int(ch) for ch in n if int(ch)%2==0)
odd=sum(int(ch) for ch in n if int(ch)%2==1)
print(abs(even-odd))

#Q13:Remove all zeroes
n=input()
print(n.replace("0",""))

#Q14. Sum of squares and cubes of digits
n=input()
sq=sum(int(ch)**2 for ch in n)
cu=sum(int(ch)**3 for ch in n)
print("Squares Sum:",sq)
print("Cubes Sum:",cu)

#Q15. Print digits in words

digit_words = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
n=input()
for ch in n:
    print(digit_words[int(ch)], end=" ")