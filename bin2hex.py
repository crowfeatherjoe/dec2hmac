conversion_table = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']


def decTohex(n):
    if (n <= 0):
        return ''
    remainder = n % 16
    return decTohex(n // 16) + conversion_table[remainder]


decimal = int(input("Enter a number: "))
print("Hexadecimal: ", decTohex(decimal))

