'''
Author: Chris Evans
Student Number: 041036829
Date: 11/17/23
Program name: Practical Project 3
'''

from tkinter import *
import Logic
import Data
import threading


root = Tk()
'''Initializing Tkinter variable as Root'''
Logic.reloadData()
'''Calling reloadData method to have data loaded in immediately on application launch'''



textWidget = Text(root, width=60, height = 30)
'''Creating a Text widget that will hold data from the CSV file'''
textWidget.pack()


def displayAllRecords():
    '''Method to display all records from CSV file'''
    textWidget.delete(1.0, END)
    for i, record, in enumerate(Logic.recordList):
        '''Looping through record list housed in Logic, adding calling addToText method to add data to text widget'''
        addToText(record, i)


def addToText(record, index):
    '''Method to add data from CSV file to textWidget'''
    textWidget.insert(END, f"Record {index + 1}\n")
    textWidget.insert(END, f"Ref Number: {record.ref_number}\n")
    textWidget.insert(END, f"Title: {record.title_en}\n")
    textWidget.insert(END, f"Purpose: {record.purpose_en}\n")
    textWidget.insert(END, f"Start Date: {record.start_date}\n")
    textWidget.insert(END, f"End Date: {record.end_date}\n")
    textWidget.insert(END, f"Airfare: {record.airfare}\n")
    textWidget.insert(END, f"Other Transport: {record.other_transport}\n")
    textWidget.insert(END, f"Lodging: {record.lodging}\n")
    textWidget.insert(END, f"Meals: {record.meals}\n")
    textWidget.insert(END, f"Other Expenses: {record.other_expenses}\n")
    textWidget.insert(END, f"Total: {record.total}\n")
    textWidget.insert(END, f"\n\n")


def displayOneRecord():
    '''Method to display one record, accepting userInput as index for which record to select'''
    textWidget.delete(1.0,END)
    record = Logic.recordList[int(readRecordEntry.get())-1]
    addToText(record, int(readRecordEntry.get())-1)

def viewAddRecord():
    '''Function to add a record to recordList, accepting user inpnut as parameters for Logic method, from Add window'''
    Logic.addRecord(addRefNumEntry.get(), addTitleEntry.get(), addPurposeEntry.get(), addStartEntry.get(), addEndEntry.get(), addAirFareEntry.get(), addOtherTranspoEntry.get(), addLodgingEntry.get(), addMealsEntry.get(), addOtherExpensesEntry.get(), addTotalEntry.get(),  )

def viewDeleteRecord():
    '''Function to delete a record from recordList, accepting user input as index for which record to delete.'''
    Logic.deleteRecord(int(deleteEntry.get())-1)

def viewEditRecord():
    '''Function to edit a record, accepting user input as both index for which record to edit, and accepting data to replace record with'''
    Logic.editRecord(int(editIndexEntry.get())-1, editRefNumEntry.get(), editTitleEntry.get(), editPurposeEntry.get(), editStartEntry.get(), editEndEntry.get(), editAirFareEntry.get(), editOtherTranspoEntry.get(), editLodgingEntry.get(), editMealsEntry.get(), editOtherExpensesEntry.get(), editTotalEntry.get(),)

def viewReloadData():
    '''Function to refresh data from CSV file'''
    Logic.reloadData()
    displayAllRecords()

def viewWriteToFile():
    '''Function to write data currently in recordList to a CSV file'''
    Logic.writeToFile()

displayAllRecords()
'''calling function which displays all records so they are visible on startup'''

def addWindow():
    '''Defining a new window which will be used to accept user input to add a record'''
    global addRefNumEntry, addTitleEntry, addPurposeEntry, addStartEntry, addEndEntry, addAirFareEntry, addOtherTranspoEntry, addLodgingEntry, addMealsEntry, addOtherExpensesEntry, addTotalEntry
    '''Making entry fields global so they can be accessed by Logic methods (I'm aware this a security risk, just easiest solution given only me and prof are using this code)'''
    addWindow = Toplevel()
    '''Creating new window by invoking TopLevel method in Tkinter'''
    Label(master=addWindow, text="Add a record").pack()
    '''Header Label to specify which window is open'''
    
    addRefNumLabel = Label(addWindow, text="Enter a Reference Number").pack()
    addRefNumEntry = Entry(addWindow, width=50)
    addRefNumEntry.pack()
    '''Label and Entry to accept User Input '''
    addTitleLabel = Label(addWindow, text="Enter a title").pack()
    addTitleEntry = Entry(addWindow, width= 50)
    addTitleEntry.pack()
    '''Label and Entry to accept User Input '''
    addPurposeLabel = Label(addWindow, text="Enter a purpose").pack()
    addPurposeEntry = Entry(addWindow, width= 50)
    addPurposeEntry.pack()
    '''Label and Entry to accept User Input '''
    addStartLabel = Label(addWindow, text="Enter a Start Date").pack()
    addStartEntry = Entry(addWindow, width= 50)
    addStartEntry.pack()
    '''Label and Entry to accept User Input '''
    addEndLabel = Label(addWindow, text="Enter an End Date").pack()
    addEndEntry = Entry(addWindow, width= 50)
    addEndEntry.pack()
    '''Label and Entry to accept User Input '''
    addAirfareLabel = Label(addWindow, text="Enter Airfare").pack()
    addAirFareEntry = Entry(addWindow, width= 50)
    addAirFareEntry.pack()
    '''Label and Entry to accept User Input '''
    addOtherTranspoLabel = Label(addWindow, text="Enter Other Transportation").pack()
    addOtherTranspoEntry = Entry(addWindow, width= 50)
    addOtherTranspoEntry.pack()
    '''Label and Entry to accept User Input '''
    addLodgingLabel = Label(addWindow, text="Enter Lodging").pack()
    addLodgingEntry = Entry(addWindow, width= 50)
    addLodgingEntry.pack()
    '''Label and Entry to accept User Input '''
    addMealsLabel = Label(addWindow, text="Enter Meals").pack()
    addMealsEntry = Entry(addWindow, width= 50)
    addMealsEntry.pack()
    '''Label and Entry to accept User Input '''
    otherExpensesLabel = Label(addWindow, text="Enter Other Expenses").pack()
    addOtherExpensesEntry = Entry(addWindow, width= 50)
    addOtherExpensesEntry.pack()
    '''Label and Entry to accept User Input '''
    addTotalLabel = Label(addWindow, text="Enter Total").pack()
    addTotalEntry = Entry(addWindow, width= 50)
    addTotalEntry.pack()
    '''Label and Entry to accept User Input '''
    addRecordButton = Button(addWindow, text= "add record ", command= viewAddRecord).pack()
    '''Submit button which calls viewAddRecord, adding user input into recordList as a new record at the end of the list'''
def deleteWindow():
    '''Defining a new window which will accept user input to determine which record should be deleted'''
    global deleteEntry
    '''Making index input entry global so it can be accessed by Logic (again a security risk technically)'''
    deleteWindow = Toplevel()
    '''Invoking Tkinter Toplevel method to create a new window'''
    Label(master=deleteWindow, text="Delete a Record").pack()
    '''Header label'''
    deleteEntry = Entry(deleteWindow, width=50, text="delete INDEX")
    '''Entry accepting user input which will be used as an index to determine record for deletion'''
    deleteEntry.pack()
    deleteButton = Button(deleteWindow, text="delete selected Entry", command=viewDeleteRecord).pack()
    '''Submit button which invokes viewDeleteRecord, deleting selected record from recordList'''

def editWindow():
    '''Defining a new window which will be used to accept user input both as an index, and to replace data'''
    global editIndexEntry, editRefNumEntry, editTitleEntry, editPurposeEntry, editStartEntry, editEndEntry, editAirFareEntry, editOtherTranspoEntry, editLodgingEntry, editMealsEntry, editOtherExpensesEntry, editTotalEntry
    '''making entry fields global for Logic access'''
    editWindow = Toplevel()
    '''Invoking Tkinter Toplevel function to create a new window'''
    Label(master= editWindow, text= "Edit a Record" ).pack()
    '''Header label'''

    editIndexLabel = Label(editWindow, text="Index of record to edit").pack()
    editIndexEntry = Entry(editWindow, width=50)
    editIndexEntry.pack()
    '''Label and Entry to accept User Input for index '''
   

    editRefNumLabel = Label(editWindow, text="Enter a Reference Number").pack()
    editRefNumEntry = Entry(editWindow, width=50)
    editRefNumEntry.pack()
    '''Label and Entry to accept User Input '''
    editTitleLabel = Label(editWindow, text="Enter a title").pack()
    editTitleEntry = Entry(editWindow, width= 50)
    editTitleEntry.pack()
    '''Label and Entry to accept User Input '''
    editPurposeLabel = Label(editWindow, text="Enter a purpose").pack()
    editPurposeEntry = Entry(editWindow, width= 50)
    editPurposeEntry.pack()
    '''Label and Entry to accept User Input '''
    editStartLabel = Label(editWindow, text="Enter a Start Date").pack()
    editStartEntry = Entry(editWindow, width= 50)
    editStartEntry.pack()
    '''Label and Entry to accept User Input '''
    editEndLabel = Label(editWindow, text="Enter an End Date").pack()
    editEndEntry = Entry(editWindow, width= 50)
    editEndEntry.pack()
    '''Label and Entry to accept User Input '''
    editAirfareLabel = Label(editWindow, text="Enter Airfare").pack()
    editAirFareEntry = Entry(editWindow, width= 50)
    editAirFareEntry.pack()
    '''Label and Entry to accept User Input '''
    editOtherTranspoLabel = Label(editWindow, text="Enter Other Transportation").pack()
    editOtherTranspoEntry = Entry(editWindow, width= 50)
    editOtherTranspoEntry.pack()
    '''Label and Entry to accept User Input '''
    editLodgingLabel = Label(editWindow, text="Enter Lodging").pack()
    editLodgingEntry = Entry(editWindow, width= 50)
    editLodgingEntry.pack()
    '''Label and Entry to accept User Input '''    
    editMealsLabel = Label(editWindow, text="Enter Meals").pack()
    editMealsEntry = Entry(editWindow, width= 50)
    editMealsEntry.pack()
    '''Label and Entry to accept User Input '''
    editOtherExpensesLabel = Label(editWindow, text="Enter Other Expenses").pack()
    editOtherExpensesEntry = Entry(editWindow, width= 50)
    editOtherExpensesEntry.pack()
    '''Label and Entry to accept User Input '''
    editTotalLabel = Label(editWindow, text="Enter Total").pack()
    editTotalEntry = Entry(editWindow, width= 50)
    editTotalEntry.pack()
    '''Label and Entry to accept User Input '''
    editRecordButton = Button(editWindow, text="edit selected record", command=viewEditRecord).pack()
    '''Submit button to invoke viewEditRecord method'''

displayRecordButton = Button(root, text="Display All Records", command=displayAllRecords, pady=5, width=20).pack()
'''Button to display all records'''


readRecordLabel = Label(root, text="Index of record to read", width=20).pack()
'''label for index entry'''
readRecordEntry = Entry(root, width=3)
'''Accepting index of which record to read'''
readRecordEntry.pack()

displayOneRecordButton = Button(root, text="Read One record", command=displayOneRecord, pady=5, width=20).pack()
'''Button to display a single record based on index from entry above'''
addWindowButton= Button(master=root, text="Open Add Window", command=addWindow, pady=5, width=20).pack()
'''Button to direct to add window'''
editWindowButton = Button(master=root, text ="Open Edit Window", command=editWindow, pady=5, width=20).pack()
'''Button to direct to edit window'''
DeleteWindowButton = Button(master=root, text="Open Delete Window", command=deleteWindow, pady=5, width=20).pack()
'''Button to direct to delete window'''

reloadButton = Button(root, text="Reload Data", command=viewReloadData, pady=5, width=20).pack()
'''Button to reload data from csv file'''
writeToFileButton = Button(root, text="Write current data to a file", command=viewWriteToFile, pady=5, width=20).pack()
'''Button to write current recordList to a csv File'''
nameLabel = Label(root, text="Program made by Chris Evans, 041036829", pady=10).pack()
'''Programmer tag'''


root.mainloop()


