####################################################################################################################
# Udemy Complete Python Bootcamp
# Final Capstone Project: Find Cost of Tile to Cover W*H Floor
# Completed on: 8/24/17
####################################################################################################################



w = input("Enter width of room: ")
h = input("Enter hight of the room: ")
w = float(w)
h = float(h)

squarefoot = w*h
print("Your total square footage is: %s" % squarefoot + " feet.")

cost = input("Enter the cost per tile: ")
cost = float(cost)

totalcost = squarefoot * cost
print("Your total cost is: $%s" % totalcost)

