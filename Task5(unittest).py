import unittest #Importing unitest library
import task4 as t4 #Importing the program that we used before
class NamesTestCase(unittest.TestCase):

    def test_first_last_name(self):

        result = t4.main() #loading the main method in program (task 4)
        with open('untitestresult.txt', 'w+') as f: #Writing result to a text file
            f.write(str(result))
        self.assertTrue(result, True) #checking the value returned by the main function

unittest.main()