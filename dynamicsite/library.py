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
    def add_Loyalty(self, name,mydiscount, image,price,color,length,texture,weight,quality,description):
        """add_Loyalty 'x human hair' : got discount with sample, price, color, length, texture, weight, quality, description"""
        self.loyalty.append([name,mydiscount, image,price,color,length,texture,weight,quality,description])

    # determines loyalty discount for customers
    def loyal_Discout(self, hair):
        discount = "0%"
        # if hair is brazilian, 15% discount on total sales
        if hair == 'brazilian':
            discount = "15%"

        # if hair is indian, 10% discount on total sales
        elif hair == 'indian':
            discount = "10%"

        # if hair is peruvian, 20% discount on total sales
        elif hair == 'peruvian':
            discount = "20%"

        # if hair is malaysian, 5% discount on total sales
        elif hair == 'malaysian':
            discount = "5%"

        # if hair is africa , 15% discount on total sales
        elif hair == 'african':
            discount = "15%"
        return discount
