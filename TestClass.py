'''
Author: Chris Evans
Student Number: 041036829
Date: 11/17/23
Program name: Practical Project 3
'''

import unittest
import Logic
import Data
class TestRecordMethods(unittest.TestCase):
    '''Class to test a method in Logic (in seperate file for simplicity)'''

    def testaddRecord(self):
        '''function to test adding a record into recordList'''
        Logic.addRecord(1, "Test Title", "Test Purpose", "2023-01-01", "2023-01-05", 500, 100, 200, 150, 50, 900)
        '''adding a record '''
        self.assertEqual(len(Logic.recordList), 101)
        '''using unittest API to test if recordList length matches desired amount, (in this case one more than what's loaded from the CSV)'''
     

if __name__ == '__main__':
    '''Launching unittest class'''
    unittest.main()
