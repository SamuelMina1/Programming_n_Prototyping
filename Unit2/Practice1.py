'''
This program calculsted the perimeter of a rectangle using input from the user
'''
#getting the lengh from the user
length = int(input("What is the length of the rectangle?"))
width = int(input("What is the width of the rectangle?"))

perimeter = 2 * (length + width)

print("The perimeter is " + str(perimeter))