


# Method that takes a binary string and converts the string into a decimal number.
def binToDec(binaryNumber):

    try:
        numOfBits = len(binaryNumber)
        index = 0
        num = 0

        # Iterate through the each index of the binary string
        for index in range(len(binaryNumber)):
            # If the bit is a 1, add the value to the current total and shift to the next index value.
            if binaryNumber[index] == "1":
                num += pow(2, numOfBits-1)
                numOfBits -= 1
            # If the bit is a 0, just shift to the next index value.
            else:
                numOfBits -= 1
    except Exception as ex:
        print("Unable to convert given binary number to decimal", ex)

    finally:
        return num
