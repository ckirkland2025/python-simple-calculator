#--- Receive input from the user ---
calc_input = input("Enter a math expression (x OP y): ")

#--- Calculate the input by splitting the input and converting to integers ---
parts = calc_input.split()
num1 = float(parts[0])
num2 = float(parts[2])

# --- Output a quick check of the user input ---
print("Calculator input is: ", calc_input)
print("Calculator parts is: ", parts)
print("Number one is ", num1, " and Number two is:", num2)
print("The operator is:", parts[1], "Which is ", type(parts[1]))

#--- Calculator Logic ---
calc_output = 0

if parts[1] == "+" or parts[1] == "plus":
    calc_output = num1 + num2
elif parts[1] == "-" or parts[1] == "minus":
    calc_output = num1 - num2 
elif parts[1] == "*" or parts[1] == "times":
    calc_output = num1 * num2
elif parts[1] == "/":
    calc_output = num1 / num2
elif parts[1] == "^":
    calc_output = num2 ** num1
else:
    calc_output = "Invalid input! Calculation not possible"

#--- Print the answer ---
print("The answer is:", calc_output)