'''Name   : Mohamed A. KAMARA
   Course : Design Patterns for Web Programming - Online
   File   : Week 4 - Reusable Code
   Date   :Sept. 23, 2016'''

#class to store processed data and apply for loyalty programs
import math
class Loyal(object):
    """Loyalty programme for customer"""
    def __init__(self):
        """Loyals is an array of customers to hold data"""
        #[name, image,price,color,length,texture,weight,quality,description]
        self.__loyalty = []

    # access modifier for the loyalty variable
    @property
    def loyalty(self):
        return self.__loyalty

    #setter for the loyalty array
    @loyalty.setter
    def loyalty(self, value):
        self.__loyalty = value


    # holds the loans application info into memory
    def add_Loyalty(self, name, image,price,color,length,texture,weight,quality,description):
        """apply 'name' : got a loan for x amount @ x rate for @ x term"""
        self.loyalty.append([name, image,price,color,length,texture,weight,quality,description])