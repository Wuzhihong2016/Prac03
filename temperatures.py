

def celsiusTofarfenheit():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    result = "Result: {:.2f} F".format(fahrenheit)
    return result

def farenheitTocelsius():
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    result = "Result: {:.2f} C".format(celsius)
    return result

def main():
    MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ (for quit)"
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "C":
            result = celsiusTofarfenheit()
            print(result)
        elif choice == "F":
            result = farenheitTocelsius()
            print(result)
        else:
            print("Invalid option")

        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

main()
