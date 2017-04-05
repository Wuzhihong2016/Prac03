"""
lower = 10
upper = 100
print("Enter a number (" + str(lower) + "-" + str(upper) + "):")

value = 'VALUE'
character = 'CHAR'
print("{:^8s} {:^8s}\n".format(value,character))

for i in range (0,256,10):
    print("{:^8d} {:^8s}".format(i,chr(i)))

"""

def get_number(lower, upper):
    user_input = int(input("Enter a number (10-50):"))
    try:
        while upper < user_input or user_input < lower:
            print("Please enter a valid number!")
            user_input = int(input("Enter a number (10-50)"))
    except ValueError:
        print("Please enter a valid integer.")
        user_input = int(input("Enter a number (10-50)"))
    return user_input
def main():
    i = get_number(10, 50)
    value = 'VALUE'
    character = 'CHAR'
    print("{:^8s} {:^8s}\n".format(value,character))
    print("{:^8d} {:^8s}".format(i,chr(i)))


main()