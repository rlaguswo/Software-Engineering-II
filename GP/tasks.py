def conv_endian(num, endian='big'):
    # Assign num to other variable.
    Num = num
    # Check if num is negative
    neg_flag = 0

    if num < 0:
        neg_flag = 1
    # Convert the num into absolute value
    # for the convenience of calculation
        Num = Num * (-1)

    if num == 0:
        return "00"

    # Initialize Hex list
    Hex_list = ['0', '1', '2', '3', '4', '5', '6',
                '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    Hex_string = list()

    # Convert Decimals into Hexadecimals
    while Num > 0:
        remainder = Num % 16
        hex = Hex_list[remainder]
        Hex_string.append(hex)
        Num = Num // 16

    # Make the hexadecimal in order to use big/little endian.
    if len(Hex_string) % 2 != 0:
        Hex_string.append('0')
    Hex_string = Hex_string[::-1]

    # Put Hex_string by a byte.
    Hexadecimal = list()
    for i in range(0, len(Hex_string), 2):
        Hex = Hex_string[i] + Hex_string[i+1]
        Hexadecimal.append(Hex)

    # Represent the Hexadecimal depending on Endians.
    hex = ""
    if endian == 'big':
        hex = concatenate(Hexadecimal, hex, neg_flag)

    elif endian == 'little':
        Hexadecimal = Hexadecimal[::-1]
        hex = concatenate(Hexadecimal, hex, neg_flag)

    else:
        hex = None

    return hex


# Function for Representing Hexadecimal numbers depending on Endians.
def concatenate(Hexadecimal, hex, neg_flag):
    # Make a string of bytes with spaces.
    for i in range(len(Hexadecimal)-1):
        hex = hex + Hexadecimal[i] + " "
    i = len(Hexadecimal) - 1
    hex = hex + Hexadecimal[i]

    # Check if the number is negative
    if neg_flag == 1:
        hex = "-" + hex

    return hex
