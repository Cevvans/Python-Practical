'''
Author: Chris Evans
Student Number: 041036829
Date: 11/17/23
Program name: Practical Project 3
'''
import unittest
import threading
from Data import startReloadDataThread


class MultiThreadingTest(unittest.TestCase):
    '''Class to test multithreading in data.py'''

    def testThreadingMethod(self):
        
        event = threading.Event()
        '''Creating threading event'''

        
        def threadWithCallback():
            '''Function to both call multithreading in data.py, and set event'''
            startReloadDataThread()
            event.set()

       
        dataThread = threading.Thread(target= threadWithCallback)
        '''starting new thread with event set'''
        dataThread.start()
        dataThread.join()
        '''joining the threads so that thread completes execution / task'''

        self.assertTrue(event.is_set())
        '''testing to see if event is set'''


if __name__ == '__main__':
    unittest.main()