'''
Author: Chris Evans
Student Number: 041036829
Date: 11/17/23
Program name: Practical Project 3
'''

import Data
import RecordObject
import csv
import unittest

Data.reloadData()
'''Calling data reloadData() method to populate recordList premptively'''
recordList = Data.recordList
'''naming recordList from data layer as a variable for simplicity'''

def reloadData():
    '''function to reload data from CSV file'''
    Data.startReloadDataThread()

def addRecord(ref_number, title_en, purpose_en, start_date, end_date, airfare, other_transport, lodging, meals, other_expenses, total):
    '''Function to add a record to recordList, using user input from presentation layer as parameters'''
    record = RecordObject.RecordObject(ref_number, title_en, purpose_en, start_date, end_date, airfare, other_transport, lodging, meals, other_expenses, total)
    recordList.append(record)

def deleteRecord(index):
    '''Function to delete a record from recordList using user input from presentation layer as index'''
    del recordList[index]

def editRecord(index, ref_number, title_en, purpose_en, start_date, end_date, airfare, other_transport, lodging, meals, other_expenses, total):
    '''Function to edit a record from recordList, using user input from presentation layer both as index, and desired input data.
    This function doesn't technically "edit/update" the data, but instead deletes the record at the index, and inserts a new record at the same index, giving the appearence of "editing"
    '''
    editedRecord = RecordObject.RecordObject(ref_number, title_en, purpose_en, start_date, end_date, airfare, other_transport, lodging, meals, other_expenses, total)
    del recordList[index]
    recordList.insert(index, editedRecord)

def writeToFile():
    '''Function utilizing CSV api to write to a file. This function works in tandem with another function in RecordObject (which primes the data into CSV format)'''
    try:
        with open("C:\\Practical3_Submission\\WriteFile.csv", mode="w", newline="", encoding="utf-8") as file_out:
            writer = csv.DictWriter(file_out, fieldnames=recordList[0].toWrite().keys())
            writer.writeheader()
            for record in recordList:
                writer.writerow(record.toWrite())
        print("Data has been written to WriteFile.txt")
    except Exception as e:
        print(f"Error writing to file: {e}")

