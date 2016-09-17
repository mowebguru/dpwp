'''Name   : Mohamed A. KAMARA
   Course : Design Patterns for Web Programming - Online
   File   : Week 3 - Reusable Code
   Date   :Sept. 15, 2016'''
import webapp2
import math
# import the FormPage and ResultPage classes from views
from views import FormPage, ResultPage
# import the Loan class from library
from library import Loan


class MainHandler(webapp2.RequestHandler):
    def get(self):

        #create an instance of the FormPage class
        myForm = FormPage()

        #create instance of the ResultPage class
        myResult = ResultPage()

        #create an instance of the Loan class
        myLoan = Loan()

        #if form submitted, collected data from URL and initiate variables
        if self.request.GET:
            name = self.request.GET['name']
            amount = self.request.GET['amount']
            email = self.request.GET['email']
            rate = self.request.GET['rate']
            term = self.request.GET['term']
            myemail = str(email)  # convert email to string
            myname = str(name)  # convert email to string
            t = float(term)  # duration of the loan converted to string
            p = float(amount)  # the amount borrowed converted to string
            length = float(t/12)  # length of the loan converted to year
            firstnote = myLoan.apply(name,amount,rate,t)  # call the module from the loan and load data in array
            firstnote = myLoan.compute_Note()  # calculates the monthly interest
            allnotes = myLoan.accrue_Principal(firstnote,t)  # calculates the payout amount
            myInterest = myLoan.accrue_Interest(allnotes,p)  # calculates the accrued interest on the loan
            monthlyLoan = format(firstnote, ',.2f')   #converts to currency notation with 2 decimal points
            payoutAmount = format(allnotes, ',.2f')   #converts to currency notation with 2 decimal points
            totInterest = format(myInterest, ',.2f')  #converts to currency notation with 2 decimal points
            loanperiod = format(length, '.1f')  # converts to 1 decimal notation
            self.response.write(myResult.print_result(myname, monthlyLoan, payoutAmount, totInterest, loanperiod,myemail))
        else:
            self.response.write(myForm.print_info())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
