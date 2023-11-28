'''
Author: Chris Evans
Student Number: 041036829
Date: 10/13/23
Program name: Practical Project 2
'''

#Defining Data Transfer Object Class
class RecordObject:
    '''Data Transfer Object to store data from the CSV file'''
    #Defining INIT method, essentially a constructor
    def __init__(self,ref_number, title_en, purpose_en, start_date, end_date, airfare, other_transport, lodging, meals, other_expenses, total):
        '''Method initialized the data transfer object with parameters to accept al required columns.'''
        self.ref_number = ref_number
        self.title_en = title_en
        self.purpose_en = purpose_en
        self.start_date = start_date
        self.end_date = end_date
        self.airfare = airfare
        self.other_transport = other_transport
        self.lodging = lodging
        self.meals = meals
        self.other_expenses = other_expenses
        self.total = total

    
        #Defining STR method, essentially a toString in java
    def __str__(self):
        '''Method defines the format for what will print to console when this an instantiation of this record is printed'''
        return f"REF NUMBER: {self.ref_number} | TITLE: {self.title_en} | PURPOSE: {self.purpose_en} | START: {self.start_date} | END: {self.end_date} | AirFare: {self.airfare} | OTHER TRANSPORT: {self.other_transport} | LODGING: {self.lodging} | MEALS: {self.meals} | OTHER_EXPENSES: {self.other_expenses} | TOTAL: {self.total} \n\n"
    
    def toWrite(self):
        '''This function primes the data into CSV format, used by a function in Logic to write to a CSV file.'''
        return {
            'ref_number': self.ref_number,
            'title_en': self.title_en,
            'purpose_en': self.purpose_en,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'airfare': self.airfare,
            'other_transport': self.other_transport,
            'lodging': self.lodging,
            'meals': self.meals,
            'other_expenses': self.other_expenses,
            'total': self.total
        }
  