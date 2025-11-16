firstNum = input("Enter First number: ")
secNum = input("Enter Second Number: ")
operation = input(" 1. Sum \n 2. Subtraction \n 3. Multiplication \n 4. Divide \n Select Operation: ")

if operation.lower() == "sum" or operation == "1":
    ans = float(firstNum) + float(secNum)
elif operation.lower() == "subtraction" or operation == "2":
    ans = float(firstNum) - float(secNum) 
elif operation.lower() == "multiplication" or operation == "3":
    ans = float(firstNum) * float(secNum) 
elif operation.lower() == "divide" or operation == "4":
    ans = float(firstNum) / float(secNum) 
else:
    print("Wrong input. Enter either the operation nane or number associated with that operation")

print("answer: ", ans)

