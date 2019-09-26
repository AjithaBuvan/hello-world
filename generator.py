import sys

print('Argument List:', str(sys.argv))
input_number1 = sys.argv[1]
if input_number1.isdigit():
    input_number2 = sys.argv[2]
    if input_number2.isdigit():
        print(list(range(int(input_number1), int(input_number2))))
    else:
        print("Please enter valid input")
else:
    print("Please enter valid input")
