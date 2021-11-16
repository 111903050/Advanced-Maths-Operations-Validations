from math import sqrt

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

# checks whether given number is prime or not

def isPrime(n):

    try:
        m = int(n)
        prime_flag = True
        if(m > 1):
            uppnum = int(sqrt(m))+1
            print(uppnum)
            for i in range(2,uppnum):
                if(m%i== 0):
                    prime_flag = False
                    break
            
    except Exception as ex:
        print("Unable to check for prime number", ex)

    finally:
        return prime_flag




def power(N, P):
    try:
                
        if P == 0:
            return 1
        elif P == 1:
            return N
        else:
            return (N*power(N, P-1))
    except Exception as ex:
        print("unable to calculate power", ex)
