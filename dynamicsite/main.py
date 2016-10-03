'''Name   : Mohamed A. KAMARA
   Course : Design Patterns for Web Programming - Online
   File   : Week 4 - Dynamic Site
   Date   :Sept. 23, 2016'''

import webapp2
from data import HumanHair
from pages import ContentPage
from library import Loyal

# the MainHandler class put all the pieces together to create a functional web app
# first the app check if url is not null and if not then it search for the "hair" keyword.
# and then load contentpage based on user's selection from the main main menu
# home takes user back; brazilian, indian, peruvian, malaysian and african

class MainHandler(webapp2.RequestHandler):

    def get(self):

            myHair = HumanHair() # creates an instance of the HumanHair class
            myPage = ContentPage() # creates an instance of the ContentPage class
            l = Loyal() # creates an instance of the loyal() class from library to hold data in memory

            # populate content with brazilian human hair class
            if self.request.method == 'GET' and 'hair' in self.request.GET:
                hair = self.request.GET['hair']

                # calculate the loyal discount based on hair category
                mydiscount = l.loyal_Discout(hair)

                #  checks if the hair category is brazilian, retrieves the various attributes associated.
                #  and then loads the contentpage

                if hair == 'brazilian':
                        image = myHair.hair_Category[0].image
                        name = myHair.hair_Category[0].name
                        price = myHair.hair_Category[0].price
                        color = myHair.hair_Category[0].color
                        length =myHair.hair_Category[0].length
                        texture = myHair.hair_Category[0].texture
                        weight =myHair.hair_Category[0].weight
                        quality = myHair.hair_Category[0].quality
                        description = myHair.hair_Category[0].description

                        # store data in memory for easy retrieval
                        myLoyalty = l.add_Loyalty(name,mydiscount, image,price,color,length,texture,weight,quality,description) # store data in cache

                        # loads the ContentPage with necessary data based on user's selection
                        self.response.write(myPage.print_Content(name,mydiscount, image,price,color,length,texture,weight,quality,description))


                #  checks if the hair category is indian, retrieves the various attributes associated
                #  and then loads the contentpage
                elif hair == 'indian':
                        image = myHair.hair_Category[1].image
                        name = myHair.hair_Category[1].name
                        price = myHair.hair_Category[1].price
                        color = myHair.hair_Category[1].color
                        length =myHair.hair_Category[1].length
                        texture = myHair.hair_Category[1].texture
                        weight =myHair.hair_Category[1].weight
                        quality = myHair.hair_Category[1].quality
                        description = myHair.hair_Category[1].description

                        # store data in memory for easy retrieval
                        myLoyalty = l.add_Loyalty(name,mydiscount, image,price,color,length,texture,weight,quality,description) # store data in cache

                        # loads the ContentPage with necessary data based on user's selection
                        self.response.write(myPage.print_Content(name,mydiscount, image,price,color,length,texture,weight,quality,description))

                #  checks if the hair category is indian, retrieves the various attributes associated
                #  and then loads the contentpage
                elif hair == 'peruvian':
                        image = myHair.hair_Category[2].image
                        name = myHair.hair_Category[2].name
                        price = myHair.hair_Category[2].price
                        color = myHair.hair_Category[2].color
                        length =myHair.hair_Category[2].length
                        texture = myHair.hair_Category[2].texture
                        weight =myHair.hair_Category[2].weight
                        quality = myHair.hair_Category[2].quality
                        description = myHair.hair_Category[2].description

                         # store data in memory for easy retrieval
                        myLoyalty = l.add_Loyalty(name,mydiscount, image,price,color,length,texture,weight,quality,description)

                        # loads the ContentPage with necessary data based on user's selection
                        self.response.write(myPage.print_Content(name,mydiscount, image,price,color,length,texture,weight,quality,description))

                #  checks if the hair category is malaysian, retrieves the various attributes associated
                #  and then loads the contentpage
                elif hair == 'malaysian':
                        image = myHair.hair_Category[3].image
                        name = myHair.hair_Category[3].name
                        price = myHair.hair_Category[3].price
                        color = myHair.hair_Category[3].color
                        length = myHair.hair_Category[3].length
                        texture = myHair.hair_Category[3].texture
                        weight = myHair.hair_Category[3].weight
                        quality = myHair.hair_Category[3].quality
                        description = myHair.hair_Category[3].description

                        # store data in memory for easy retrieval
                        myLoyalty = l.add_Loyalty(name,mydiscount, image,price,color,length,texture,weight,quality,description)

                        # loads the ContentPage with necessary data based on user's selection
                        self.response.write(myPage.print_Content(name,mydiscount, image,price,color,length,texture,weight,quality,description))

                #  checks if the hair category is african, retrieves the various attributes associated
                #  and then loads the contentpage
                elif hair == 'african':
                        image = myHair.hair_Category[4].image
                        name = myHair.hair_Category[4].name
                        price = myHair.hair_Category[4].price
                        color = myHair.hair_Category[4].color
                        length =myHair.hair_Category[4].length
                        texture = myHair.hair_Category[4].texture
                        weight =myHair.hair_Category[4].weight
                        quality = myHair.hair_Category[4].quality
                        description = myHair.hair_Category[4].description

                        # store data in memory for easy retrieval
                        myLoyalty = l.add_Loyalty(name,mydiscount, image,price,color,length,texture,weight,quality,description)

                        # loads the ContentPage with necessary data based on user's selection
                        self.response.write(myPage.print_Content(name,mydiscount, image,price,color,length,texture,weight,quality,description))

                #  if the user clicks on 'home', the page reload without the dynamic data
                elif hair == 'home':
                    self.response.write(myPage.print_Page())

            #  loads the default page without dynamic content
            else:
                self.response.write(myPage.print_Page())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
