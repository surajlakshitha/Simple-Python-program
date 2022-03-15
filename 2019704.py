from tabulate import tabulate
from random import choice as randInt

# ----------------Define Funtions----------------#

def instructions() :
    print("\n----------Hello User------------")
    print("Maximum Rows and Columns are '9'")
    print("Minimum Rows and Columns are '3'")
    print("\n")

def listToString(results):  
    str1 = " "  # Creating an Empty String  
    return (str1.join(results)) #Return String

# -------------------Validate Input-------------------#

instructions() #Display_Instructions

while True:
    try:
        row = int(input('Row:'))  # Getting input for Rows
    except ValueError:
        print("Plaese Enter an Integer")
        continue

    # Validate User Input in Range of 3 to 9
    if row < 10 and row > 2 and int:
        break
    else:
        print("Error !!! Please Try Again")

# -------------------Validate Input-------------------#

while True:
    try:
        col = int(input('Column:'))  # Getting input for Columns
    except ValueError:
        print("Please Enter an Integer")
        continue

    # Validate User Input in Range of 3 to 9
    if col < 10 and col > 2 and int:
        break
    else:
        print("Error !!! Please Try Again")

# -------------Creating Grid and Print Grid-----------#

listOfInt = list(range(10, 100))  # Creating List
listOfInt.extend(["  "] * 10)  # Extend the List with " "

grid = []
results =[]
for x in range(row):
    column = [randInt(listOfInt) for i in range(col)]
    grid.append(column)
    
# ---------------------Checking " "-------------------#

check=[]
for i in range(col):
    for y in grid:
        check.append(y[i])
    if "  " in check:
        results.append('NO')
    else:
        results.append('OK')
                   
    check.clear()#Clear List


# -------------Creating Grid and Print Grid-----------#

print(tabulate(grid, tablefmt='fancy_grid'))
print(*results, sep = "   ")


# -----------Getting File Name from the User----------#

userInput = input("Please Enter the File Name to Save as Text & HTML File : ")

# ------File Handling - Save Output to .txt File------#

f = open(userInput+".txt", "w")
f.write(tabulate(grid, tablefmt='plain'))
f.write("\n")
f.write(listToString(results))
f.close()

# -----File Handling - Save Output to .html File------#

f = open(userInput+".html", "w")
f.write(tabulate(grid, tablefmt='html'))
f.write("\n")
f.write(listToString(results))
f.close()

print("\nFile Saved Sucessfully !")
