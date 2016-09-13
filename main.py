'''Name: Mohamed A. Kamarag
Design Patterns for Web Programming - Online
Week 1 - Simple Form
Sept. 9, 2016'''
import webapp2
#import the Subscribe class from Form.py
from Form import Subscribe


class MainHandler(webapp2.RequestHandler):
    def get(self):
        #Initiate the myform variable to the Subscribe class containing form layout
        myform = Subscribe()

        if self.request.GET:
            firstname = self.request.GET['firstname']
            lastname = self.request.GET['lastname']
            phone = self.request.GET['phone']
            email = self.request.GET['email']
            profession= self.request.GET['profession']
            gender = self.request.GET['gender']
            package= self.request.GET['package']
            #Format to display submitted data.

            self.response.write(myform.print_data(firstname,lastname,phone,email,profession,package)) # if data exists in cache, load submitted data
        else:
            self.response.write(myform.print_info()) # otherwise displays form to fill for submission


routes = [('/', MainHandler)]
app = webapp2.WSGIApplication(routes, debug=True)
