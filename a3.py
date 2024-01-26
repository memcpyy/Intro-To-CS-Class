

#asking the users to give me cords
print("---Calculate the slope of a line passing through 2 points!---")
x1 = float(input("Enter the x coordinate of the first point: "))
y1 = float(input("Enter the y coordinate of the first point: "))
x2 = float(input("Enter the x coordinate of the second point: "))
y2 = float(input("Enter the y coordinate of the second point: "))

result  = (y2 - y1) / (x2 - x1) #the math to calculate the slope of 2 lines passing through 

print("The slope of the line passing through ({}, {}) and ({}, {}) is: {:.2f}".format(x1,y1, x2,y2, result))
#printing it back to the user using .format