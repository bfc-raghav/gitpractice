
# Python program to calculate the area of a rectangle

def calculate_area(length, width):
    area = length * width
    return area

try:
    length = int(input("Enter the length of the rectangle: "))
except:
    print("The value given is not a integer. A default value of 7 will be used")
    length = 7
try:
    width = int(input("Enter the width of the rectangle: "))
except: 
    print("The value given is not an integer. A default value of 12 will be used.")
    width = 12

print("The area of the rectangle is:", calculate_area(length, width))

    
