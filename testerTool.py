
import unittest
from operations import tester, Powertester


print("================================================================")
print("#        Hello and welcome to automated operations tester!        #")
print("#                                                          #")
print("#                  Maths Functions                    #")
print("# 1- Convert Binary to Decimal.                            #")
print("# 2- Check if a number is Prime.                            #")
print("# 3- calculate the Power of given numbers                               #")
print("# 4- Find the power of Number                              #")
print("# q- Exit .                       #")
print("#                                                          #")
print("=================================================================\n\n")


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

