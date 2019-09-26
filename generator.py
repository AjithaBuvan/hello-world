input_number1 = input("Enter start of range ")
if input_number1.isdigit():
    input_number2 = input("Enter end of range ")
    if input_number2.isdigit():
        print(list(range(int(input_number1), int(input_number2))))
    else:
        print("Please enter valid input")
else:
    print("Please enter valid input")
