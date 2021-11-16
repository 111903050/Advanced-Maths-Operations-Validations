
import unittest
from operations import tester, Powertester


print("===================================================================")
print("#        Hello and welcome to automated operations tester!        #")
print("#                                                                 #")
print("#                  Maths Functions                                #")
print("# 1- Convert Binary to Decimal.                                   #")
print("# 2- Check if a number is Prime.                                  #")
print("# 3- calculate the Power of given numbers                         #")
print("# 4- Check if given number is perfect square                      #")
print("# q- Exit .                       #")
print("#                                                                 #")
print("===================================================================\n\n")


# test_01 for testing proper simple binary string input
class test_01(unittest.TestCase):
    def runTest(self):

        try:
            response = tester("1", "101")
            expected = 5
            msg = f"The answer returned is not as per the expectation, it is {response}"
            self.assertEqual(response, expected, msg)

            print("\nTEST-01 PASS : The returned answer is correct as expected", response)

            print(
                "\n========================================================================\n")

        except Exception as ex:
            print('\n\nTEST-01 FAIL', ex)
            print(
                "\n========================================================================\n")

        finally:
            return


# test_02 for testing proper long binary string input
class test_02(unittest.TestCase):
    def runTest(self):

        try:
            response = tester(
                "1", "10111111111111111111111000000000000000001111111111111111000000000011111111111111111")
            expected = 7253553764775066400325631
            msg = f"The answer returned is not as per the expectation, it is {response}"
            self.assertEqual(response, expected, msg)

            print("\nTEST-02 PASS : The returned answer is correct as expected", response)
            print(
                "\n========================================================================\n")
        except Exception as ex:
            print('\n\nTEST-02 FAIL', ex)
            print(
                "\n========================================================================\n")

        finally:
            return
            
            
# test_03 for testing invalid input of only characters
class test_03(unittest.TestCase):
    def runTest(self):

        try:
            response = tester("1", "abcdeghlloklmmsiml")
            expected = 2
            msg = f"The answer returned is not as per the expectation, it is {response}"
            self.assertEqual(response, expected, msg)

            print("\nTEST-03 PASS : The returned answer is correct as expected", response)
            print(
                "\n========================================================================\n")
        except Exception as ex:
            print('\n\nTEST-03 FAIL', ex)
            print(
                "\n========================================================================\n")

        finally:
            return
            
            
# test_04 for testing invalid input of constiting values other than 1 an 0
class test_04(unittest.TestCase):
    def runTest(self):

        try:
            response = tester("1", "11111111112223444444444555")
            expected = 2
            msg = f"The answer returned is not as per the expectation, it is {response}"
            self.assertEqual(response, expected, msg)

            print("\nTEST-04 PASS : The returned answer is correct as expected", response)
            print(
                "\n========================================================================\n")
        except Exception as ex:
            print('\n\nTEST-04 FAIL', ex)
            print(
                "\n========================================================================\n")

        finally:
            return

#testing prime function

# test_05 for testing a simple number to know if it is prime
class test_05(unittest.TestCase):
    def runTest(self):

        try:
            response = tester("2", "59")
            expected = True
            msg = f"The answer returned is not as per the expectation, it is {response}"
            self.assertEqual(response, expected, msg)

            print("\nTEST-05 PASS : The returned answer is correct as expected", response)
            print(
                "\n========================================================================\n")
        except Exception as ex:
            print('\n\nTEST-05 FAIL', ex)
            print(
                "\n========================================================================\n")

        finally:
            return


# test_06 for testing a bigger number to know if it is prime
class test_06(unittest.TestCase):
    def runTest(self):

        try:
            response = tester("2", "593456789921788945786383649834947123456789")
            expected = True
            msg = f"The answer returned is not as per the expectation, it is {response}"
            self.assertEqual(response, expected, msg)

            print("\nTEST-06 PASS : The returned answer is correct as expected", response)
            print(
                "\n========================================================================\n")
        except Exception as ex:
            print('\n\nTEST-06 FAIL', ex)
            print(
                "\n========================================================================\n")

        finally:
            return



# test_07 for testing a invalid input of characters to know if it is prime
class test_07(unittest.TestCase):
    def runTest(self):

        try:
            response = tester("2", "59345abjdskodjdoisddjdhdkusyddkjdjygddjhgujuth12345")
            expected = True
            msg = f"The answer returned is not as per the expectation, it is {response}"
            self.assertEqual(response, expected, msg)

            print("\nTEST-07 PASS : The returned answer is correct as expected", response)
            print(
                "\n========================================================================\n")
        except Exception as ex:
            print('\n\nTEST-07 FAIL', ex)
            print(
                "\n========================================================================\n")

        finally:
            return
# test_08 for testing a invalid input of negative number to know if it is prime
class test_08(unittest.TestCase):
    def runTest(self):

        try:
            response = tester("2", "-123489273")
            expected = False
            msg = f"The answer returned is not as per the expectation, it is {response}"
            self.assertEqual(response, expected, msg)

            print("\nTEST-08 PASS : The returned answer is correct as expected", response)
            print(
                "\n========================================================================\n")
        except Exception as ex:
            print('\n\nTEST-08 FAIL', ex)
            print(
                "\n========================================================================\n")

        finally:
            return


#testing power function

# test_09 for testing simple numbers power calculator
class test_09(unittest.TestCase):
    def runTest(self):

        try:
            response = Powertester("3", 12, 3)
            expected = 1728
            msg = f"The answer returned is not as per the expectation, it is {response}"
            self.assertEqual(response, expected, msg)

            print("\nTEST-09 PASS : The returned answer is correct as expected", response)
            print(
                "\n========================================================================\n")
        except Exception as ex:
            print('\n\nTEST-09 FAIL', ex)
            print(
                "\n========================================================================\n")

        finally:
            return



# test_10 for testing negative number power calculator
class test_10(unittest.TestCase):
    def runTest(self):

        try:
            response = Powertester("3", -123, 5)
            expected = -28153056843
            msg = f"The answer returned is not as per the expectation, it is {response}"
            self.assertEqual(response, expected, msg)

            print("\nTEST-10 PASS : The returned answer is correct as expected", response)
            print(
                "\n========================================================================\n")
        except Exception as ex:
            print('\n\nTEST-10 FAIL', ex)
            print(
                "\n========================================================================\n")

        finally:
            return

        
# test_11 for testing a invalid input of float number to know if it is prime
class test_11(unittest.TestCase):
    def runTest(self):

        try:
            response = tester("2", "1234.0806")
            expected = False
            msg = f"The answer returned is not as per the expectation, it is {response}"
            self.assertEqual(response, expected, msg)

            print("\nTEST-11 PASS : The returned answer is correct as expected", response)
            print(
                "\n========================================================================\n")
        except Exception as ex:
            print('\n\nTEST-11 FAIL', ex)
            print(
                "\n========================================================================\n")

        finally:
            return



# test_12 for testing character input for power calculator
class test_12(unittest.TestCase):
    def runTest(self):

        try:
            response = Powertester("3", "accdfkufkfnlfflk", 5)
            expected = -28153056843
            msg = f"The answer returned is not as per the expectation, it is {response}"
            self.assertEqual(response, expected, msg)

            print("\nTEST-12 PASS : The returned answer is correct as expected", response)
            print(
                "\n========================================================================\n")
        except Exception as ex:
            print('\n\nTEST-12 FAIL', ex)
            print(
                "\n========================================================================\n")

        finally:
            return


