#Rectangle area calculation
#area of rectangle = length * breadth
length=int(input("Enter the length of the rectangle: "))
breadth=int(input("Enter the breadth of the rectangle: "))
area=length*breadth
print(f"The area of the rectangle is: {area}")

#Perimeter of rectangle calculation
#perimeter of rectangle = 2 * (length + breadth)
perimeter=2*(length+breadth)
print(f"The perimeter of the rectangle is: {perimeter}")

#Circle area calculation
#area of circle = π * radius * radius
import math
radius=float(input("Enter the radius of the circle: "))
area_circle=math.pi*radius*radius
print(f"The area of the circle is: {area_circle}")


#Circumference of circle calculation
#circumference of circle = 2 * π * radius
circumference=2*math.pi*radius
print(f"The circumference of the circle is: {circumference}")


#Simple interest calculation
#simple interest = (principal * rate * time) / 100
principal=float(input("Enter the principal amount: "))
rate=float(input("Enter the rate of interest: "))
time=float(input("Enter the time in years: "))
simple_interest=(principal*rate*time)/100
print(f"The simple interest is: {simple_interest}")

#compound interest calculation
#compound interest = principal * (1 + rate/100)^time - principal
compound_interest=principal*(1 + rate/100)**time - principal
print(f"The compound interest is: {compound_interest}")

#BMI(body mass index) calculation
#BMI = weight (kg) / (height (m) * height (m))
weight=float(input("Enter your weight in kg: "))
height=float(input("Enter your height in meters: "))
bmi=weight/(height*height)
print(f"Your BMI is: {bmi}")

#Temperature conversion
#Celsius to Fahrenheit: F = (C * 9/5) + 32
celsius=float(input("Enter temperature in Celsius: "))
fahrenheit=(celsius*9/5)+32
print(f"Temperature in Fahrenheit: {fahrenheit}")

#Fahrenheit to Celsius: C = (F - 32) * 5/9
fahrenheit_input=float(input("Enter temperature in Fahrenheit: "))
celsius_converted=(fahrenheit_input-32)*5/9
print(f"Temperature in Celsius: {celsius_converted}")

#Area of triangle calculation
#area of triangle = 0.5 * base * height
base=float(input("Enter the base of the triangle: "))
height_triangle=float(input("Enter the height of the triangle: "))
area_triangle=0.5*base*height_triangle
print(f"The area of the triangle is: {area_triangle}")

#Perimeter of triangle calculation
#perimeter of triangle = side1 + side2 + side3
side1=float(input("Enter length of side 1 of the triangle: "))
side2=float(input("Enter length of side 2 of the triangle: "))
side3=float(input("Enter length of side 3 of the triangle: "))
perimeter_triangle=side1+side2+side3
print(f"The perimeter of the triangle is: {perimeter_triangle}")

#Speed calculation
#speed = distance / time
distance=float(input("Enter distance traveled (in km): "))
time=float(input("Enter time taken (in hours): "))
speed=distance/time
print(f"The speed is: {speed} km/h")

#Distance calculation
#distance = speed * time
speed_input=float(input("Enter speed (in km/h): "))
time_input=float(input("Enter time (in hours): "))
distance_calculated=speed_input*time_input
print(f"The distance traveled is: {distance_calculated} km")

#Time calculation
#time = distance / speed
distance_time=float(input("Enter distance traveled (in km): "))
speed_time=float(input("Enter speed (in km/h): "))
time_calculated=distance_time/speed_time
print(f"The time taken is: {time_calculated} hours")

#Quadratic equation roots calculation
#roots = (-b ± √(b² - 4ac)) / 2a
a=float(input("Enter coefficient a: "))
b=float(input("Enter coefficient b: "))
c=float(input("Enter coefficient c: "))
discriminant=b**2 - 4*a*c
if discriminant > 0:
    root1=(-b + math.sqrt(discriminant)) / (2*a)
    root2=(-b - math.sqrt(discriminant)) / (2*a)
    print(f"The roots are real and different: {root1} and {root2}")
elif discriminant == 0:
    root=(-b) / (2*a)
    print(f"The roots are real and same: {root}")
else:
    real_part=-b / (2*a)
    imaginary_part=math.sqrt(-discriminant) / (2*a)
    print(f"The roots are complex: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i")

#Average of n numbers calculation
n=int(input("Enter the number of values to calculate average: "))
total=0
for i in range(n):
    num=float(input(f"Enter number {i+1}: "))
    total += num
average=total/n
print(f"The average is: {average}")

#c=sqrt(a^2 + b^2)(Pythagorean theorem)
import math
a=int(input("Enter side a: "))
b=int(input("Enter side b: "))
c=math.sqrt(a**2 + b**2)
print(f"The length of side c is: {c}")

#Area of parallelogram
#area = base * height
base=float(input("Enter the base of the parallelogram: "))
height=float(input("Enter the height of the parallelogram: "))
area=base*height
print(f"The area of the parallelogram is: {area}")

#Perimeter of parallelogram
#perimeter = 2 * (side1 + side2)
side1=float(input("Enter length of side 1 of the parallelogram: "))
side2=float(input("Enter length of side 2 of the parallelogram: "))
perimeter=2*(side1+side2)
print(f"The perimeter of the parallelogram is: {perimeter}")
