'''Name   : Mohamed A. KAMARA
   Course : Design Patterns for Web Programming - Online
   File   : Week 4 - Dynamic Site
   Date   :Sept. 23, 2016'''
import webapp2
from data import HumanHair
from pages import ContentPage
from library import Loyal
class MainHandler(webapp2.RequestHandler):

    def get(self):

            myHair = HumanHair()
            myPage = ContentPage()
            l = Loyal()

            # populate content with brazilian human hair class
            if self.request.method == 'GET' and 'hair' in self.request.GET:
                hair = self.request.GET['hair']
                # calculate the loyal discount based on hair category
                mydiscount = l.loyal_Discout(hair)

                if hair == 'brazilian':
                        image = myHair.hair_Category[0].image #
                        name = myHair.hair_Category[0].name
                        price = myHair.hair_Category[0].price
                        color = myHair.hair_Category[0].color
                        length =myHair.hair_Category[0].length
                        texture = myHair.hair_Category[0].texture
                        weight =myHair.hair_Category[0].weight
                        quality = myHair.hair_Category[0].quality
                        description = myHair.hair_Category[0].description
                        myLoyalty = l.add_Loyalty(name,mydiscount, image,price,color,length,texture,weight,quality,description) # store data in cache
                        self.response.write(myPage.print_Content(name,mydiscount, image,price,color,length,texture,weight,quality,description))
                # populate content page with indian human hair data
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
                        myLoyalty = l.add_Loyalty(name,mydiscount, image,price,color,length,texture,weight,quality,description) # store data in cache
                        self.response.write(myPage.print_Content(name,mydiscount, image,price,color,length,texture,weight,quality,description))

                 # populate content page with indian human hair data
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
                        myLoyalty = l.add_Loyalty(name,mydiscount, image,price,color,length,texture,weight,quality,description) # store data in cache
                        self.response.write(myPage.print_Content(name,mydiscount, image,price,color,length,texture,weight,quality,description))

                # populate content page with malaysian human hair data
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
                        myLoyalty = l.add_Loyalty(name,mydiscount, image,price,color,length,texture,weight,quality,description) # store data in cache
                        self.response.write(myPage.print_Content(name,mydiscount, image,price,color,length,texture,weight,quality,description))

                 # populate content page with indian human hair data
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
                        myLoyalty = l.add_Loyalty(name,mydiscount, image,price,color,length,texture,weight,quality,description)
                        self.response.write(myPage.print_Content(name,mydiscount, image,price,color,length,texture,weight,quality,description))
                elif hair == 'home':
                    self.response.write(myPage.print_Page())
            else:
                self.response.write(myPage.print_Page())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
