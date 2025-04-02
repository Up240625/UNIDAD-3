import math

age = 18

height = 1.75

complex_num = 2 + 3j

base = float(input("Enter base: "))
height = float(input("Enter height: "))
area = 0.5 * base * height
print(f"The area of the triangle is {area}")

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
perimeter = a + b + c
print(f"The perimeter of the triangle is {perimeter}")

length = float(input("Enter length: "))
width = float(input("Enter width: "))
rectangle_area = length * width
rectangle_perimeter = 2 * (length + width)
print(f"The area of the rectangle is {rectangle_area}")
print(f"The perimeter of the rectangle is {rectangle_perimeter}")

radius = float(input("Enter radius: "))
pi = 3.14
circle_area = pi * radius ** 2
circumference = 2 * pi * radius
print(f"The area of the circle is {circle_area}")
print(f"The circumference of the circle is {circumference}")

m = 2
x_intercept = 2 / 2
y_intercept = -2
print(f"Slope: {m}, X-intercept: {x_intercept}, Y-intercept: {y_intercept}")

x1, y1, x2, y2 = 2, 2, 6, 10
slope = (y2 - y1) / (x2 - x1)
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"Slope: {slope}, Distance: {distance}")

print("Slopes are equal" if m == slope else "Slopes are different")

for x in range(-10, 10):
    if x**2 + 6*x + 9 == 0:
        print(f"y is 0 when x = {x}")

print(len("python") != len("dragon"))

print("on" in "python" and "on" in "dragon")

sentence = "I hope this course is not full of jargon"
print("jargon" in sentence)

print("on" not in "python" and "on" not in "dragon")

length_python = len("python")
length_float = float(length_python)
length_str = str(length_float)
print(length_str)

num = int(input("Enter a number: "))
print(f"{num} is even: {num % 2 == 0}")

print(7 // 3 == int(2.7))

print(type("10") == type(10))

try:
    print(int(float('9.8')) == 10)
except ValueError:
    print("Cannot convert '9.8' to int directly")

hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))
pay = hours * rate
print(f"Your weekly earning is {pay}")

years = int(input("Enter number of years you have lived: "))
seconds = years * 365 * 24 * 60 * 60
print(f"You have lived for {seconds} seconds.")

print("1 1 1 1 1")
for i in range(2, 6):
    print(f"{i} 1 {i} {i**2} {i**3}")