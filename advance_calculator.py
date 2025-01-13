import math

def advanced_operations():
    print("\nAdvanced Operations:")
    print("5. Modulus (%)")
    print("6. Exponentiation (^)")
    print("7. Square Root (√)")
    print("8. Factorial (!)")
    print("9. Trigonometry (sin, cos, tan)")

    choice = input("Enter choice (5/6/7/8/9): ")
    if choice in ['5', '6', '7', '8', '9']:
        num = float(input("Enter a number: "))
        if choice == '5':
            mod = float(input("Enter second number for modulus: "))
            print(f"Result: {num} % {mod} = {num % mod}")
        elif choice == '6':
            exp = float(input("Enter exponent: "))
            print(f"Result: {num} ^ {exp} = {num ** exp}")
        elif choice == '7':
            if num >= 0:
                print(f"Result: √{num} = {math.sqrt(num)}")
            else:
                print("Error: Square root of a negative number is not defined!")
        elif choice == '8':
            if num >= 0 and num.is_integer():
                print(f"Result: {num}! = {math.factorial(int(num))}")
            else:
                print("Error: Factorial is only defined for non-negative integers.")
        elif choice == '9':
            print(f"sin({num}) = {math.sin(math.radians(num))}")
            print(f"cos({num}) = {math.cos(math.radians(num))}")
            print(f"tan({num}) = {math.tan(math.radians(num))}")
    else:
        print("Invalid choice!")

advanced_operations()
