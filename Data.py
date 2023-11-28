'''
Author: Chris Evans
Student Number: 041036829
Date: 11/17/23
Program name: Practical Project 3
'''

import csv
import RecordObject
import threading

recordList = []
'''defining recordList to hold data from the CSV file'''

def reloadData():
    recordList.clear()
    try:
        '''Opening Try-Catch to attempt to read CSV file, excepting FileNotFoundException'''  
        with open("C:\\Project2Submission\\travelq.csv", mode="r", newline="", encoding="utf-8") as file_in:
            '''Using python CSV API to read CSV file'''
            for i, row in enumerate(csv.DictReader(file_in)):
                '''For loop to iterate through CSV file using python CSV API reader'''
                if i >= 100:
                    break

                ref_number = row["ref_number"]
                title_en = row["title_en"]
                purpose_en = row["purpose_en"]
                start_date = row["start_date"]
                end_date = row["end_date"]
                airfare = row["airfare"]
                other_transport = row["other_transport"]
                lodging = row["lodging"]
                meals = row["meals"]
                other_expenses = row["other_expenses"]
                total = row["total"]
                '''Assigning variables in DTO to data read from CSV file, by column name as keys'''
                record = RecordObject.RecordObject(ref_number, title_en, purpose_en, start_date, end_date, airfare, other_transport, lodging, meals, other_expenses, total)
                recordList.append(record)
        print("Thread during data call: ", threading.current_thread())
        '''Printing to show which thread is active'''

    except FileNotFoundError:
        print(f"ERROR: FILE NOT FOUND")
        '''Catching FileNotFoundError, stopping the program from crashing if the file path for the CSV is null'''
def startReloadDataThread():
    '''Function to reload the data on a new thread'''
    dataThread = threading.Thread(target=reloadData)
    '''creating new thread'''
    dataThread.start()
    '''starting thread'''
    print("Thread started: ", threading.current_thread())
    '''printing to show which thread is active'''
    print("MultiThreading implemented by Chris Evans 041036829")



