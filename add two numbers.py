def add():
    a=10
    b=20
    c=a+b
    print(c)
add()
num = 5
square = num * num

print("Number:", num)
print("Square:", square)
num = 8

if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")
def print_hello():
    for i in range(5):
        print("Hello")

print_hello()
def find_max(a, b):
    if a > b:
        return a
    else:
        return b
num1 = 10
num2 = 25
result = find_max(num1, num2)
print("Maximum number is:", result)
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact
num = 5
result = factorial(num)
print("Factorial of", num, "is:", result)
def is_prime(n):
    if n <= 1:
        return "Not Prime"
    
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return "Not Prime"
    
    return "Prime"
num = 7
print(num, "is", is_prime(num))

def sum_n(n):
    return n * (n + 1) // 2 
num = 5
print("Sum of first", num, "natural numbers is", sum_n(num))
def reverse_number(n):
    rev = 0
    while n != 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
    return rev
num = 1234
result = reverse_number(num)

print("Reverse of", num, "is", result)
def count_digits(n):
    count = 0
    while n != 0:
        count += 1
        n //= 10
    return count

num = 12345
result = count_digits(num)

print("Number of digits in", num, "is", result)
def is_palindrome(n):
    return n == int(str(n)[::-1])

print("121 is palindrome:", is_palindrome(121))
def largest(a,b,c):
    return max(a,b,c)
print("Largest:", largest(10, 25, 15))
def simple_interest(p, t, r):
    return(p * t * r) / 100
print("SI:",simple_interest(1000, 2, 5))
def table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n*i)

table(9)
def is_armstrong(n):
    temp = n
    sum_val = 0
    while n != 0:
        digit = n % 10
        sum_val += digit ** 3
        n //= 10
    return sum_val == temp
print("153 is Armstrong:", is_armstrong(153))
def sum_digits(n):
    total = 0
    while n != 0:
        total += n % 10
        n //= 10
    return total
print("Sum of digits:", sum_digits(123))
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
print("GCD:", gcd(12, 18))
def is_string_palindrome(s):
    return s == s[::-1]
def swap(a, b):
    return b, a
x, y = swap(5, 10)
print("After swap:", x, y)
print("madam is palindrome:", is_string_palindrome("madam"))
def count_vowels(s):
    count = 0
    for ch in s.lower():
        if ch in "aeiou":
            count += 1
    return count
print("Vowels:", count_vowels("hello"))
