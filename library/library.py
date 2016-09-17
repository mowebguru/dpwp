'''Name   : Mohamed A. KAMARA
   Course : Design Patterns for Web Programming - Online
   File   : Week 3 - Reusable Code
   Date   :Sept. 15, 2016'''

#class to calculate loan interest, credit status, monthly payment
import math
class Loan(object):
    """Loan application for customer"""
    def __init__(self):
        """Loans is an array of application to hold data"""
        #[name, amount, rate, term]
        self.__loans = []
        self.__payments = []

    # access modifier for the loans variable
    @property
    def loans(self):
        return self.__loans

    #setter for the loans array
    @loans.setter
    def loans(self, value):
        self.__loans = value


    # holds the loans application info into memory
    def apply(self, name, amount, rate, term):
        """apply 'name' : got a loan for x amount @ x rate for @ x term"""
        self.loans.append([name, amount,rate,term])

    # holds the computed note and term in memory
    def accrue(self, note, term):
        """accrued payment 'note' :  @ x term"""
        self.payments.append([note, term])


    #determine the monthly payment
    def compute_Note(self):
        """What is the monthly payment on the loan?"""
        payment = 0
        for name, amount, rate, term in self.loans:
            #Converts the rate to decimal by dividing by 100
            p = float(amount)   # initiate p=principal and convert amount to float
            r = float(rate)/100/12  # converts the annual interest to a monthly apr
            t = float(term)  # initiate t=principal and convert amount to float
            #Calculates the numerator of the interest formula
            p1 = (p * r *((1 + r) ** t))
            p2 = (((1 + r) ** t)-1)
            payment += (p1/p2)
        return payment

    #Calculate the cumulative loan and interest
    def accrue_Principal(self, note, term):
        """accrued monthly payments during loan term"""
        totP = 0
        totP += float(note * term)
        return totP

    #Calculate the total interests
    def accrue_Interest(self, accrueP, amount):
        """accrued monthly payments during loan term"""
        totI = float(accrueP - amount)
        return totI



