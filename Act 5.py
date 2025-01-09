char = input("Enter a charcter:")
if len(char) == 1:
    ascii_value = ord(char)
    print(f"The ASCII value of the entered charcter is:",ascii_value)
else:
    print("Please enter a single character")