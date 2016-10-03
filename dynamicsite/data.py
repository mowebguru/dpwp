'''Name   : Mohamed A. KAMARA
   Course : Design Patterns for Web Programming - Online
   File   : Week 4 - Dynamic Site
   Date   :Sept. 23, 2016'''

# the code below serves two functions: 1) create the Hair (DataObject) class that will be used to create instances of
# other hair categories and 2) populate the ContentPage with dynamic information as a user client on the associated options

# defines the Hair (DataObject) with all attributes
class Hair(object):
    def __init__(self):
        self.image = ''      # defines the sample picture of the hair
        self.name = ''       # defines the name of the hair
        self.price = ''      # defines the price of the hair
        self.color = ''      # defines the color of the hair
        self.length = ''     # defines the length of the hair
        self.texture = ''    # defines the texture of the hair
        self.weight = ''     # defines the weight of the hair
        self.quality = ''    # defines the quality of the hair
        self.description = '' # defines the description of the hair

# the HumanHair is an instance of the Hair class that serves as data store for the application
class HumanHair(object):
    def __init__(self):

         # creates the Brazilian human hair instance to be populated on contentpage
        brazilian = Hair()
        brazilian.image = 'images/brazilian.png'
        brazilian.name = 'Virgin Brazilian Human Hair'
        brazilian.price = '$90.00'
        brazilian.color = 'Natural Black'
        brazilian.length = '8-30 INCH'
        brazilian.texture = 'Brazilian Body Wave'
        brazilian.weight = '95-100g/pc'
        brazilian.quality = '7A Grade High Quality  100% Virgin Hair,Tangle Free, No Shedding'
        brazilian.description = 'Brazilian Human Hair offers the most natural look and feel. It is remarkably soft with a ' \
                                'shine and movement that is not easily duplicated.'

        # creates the Indian human hair instance to be populated on contentpage
        indian = Hair()
        indian.image = 'images/indian.png'
        indian.name = 'Virgin Indian Human Hair'
        indian.price = '$75.00'
        indian.color = 'Natural Black'
        indian.length = '8-30 INCH'
        indian.texture = 'Indian Body Wave'
        indian.weight = '95-100g/pc'
        indian.quality = '7A Grade High Quality  100% Virgin Hair,Tangle Free, No Shedding'
        indian.description = 'Indian human hair is regarded as the finest elite quality human hair. It is stronger' \
                             ', healthier and less likely to tangle than the ordinary human'

        # creates the Peruvian human hair instance to be populated on contentpage
        peruvian = Hair()
        peruvian.image = 'images/peruvian.png'
        peruvian.name = 'Virgin Peruvian Human Hair'
        peruvian.price = '$65.00'
        peruvian.color = 'Natural Black'
        peruvian.length = '8-30 INCH'
        peruvian.texture = 'Straight Hair'
        peruvian.weight = '95-100g/pc'
        peruvian.quality = '7A Grade High Quality  100% Virgin Hair,Tangle Free, No Shedding'
        peruvian.description = 'Peruvian human hair is regarded as the finest elite quality human hair. It is stronger' \
                             ', healthier and less likely to tangle than the ordinary human'

        # creates the Malaysian human hair instance to be populated on contentpage
        malaysian = Hair()
        malaysian.image = 'images/malaysian.png'
        malaysian.name = 'Virgin Malaysian Human Hair'
        malaysian.price = '$80.00'
        malaysian.color = 'T1B/4/27'
        malaysian.length = '16-26 INCH'
        malaysian.texture = 'Ombre Straight Hair'
        malaysian.weight = '95-100g/pc'
        malaysian.quality = '7A Grade High Quality  100% Virgin Hair,Tangle Free, No Shedding'
        malaysian.description = 'Malaysian human hair is regarded as the finest elite quality human hair. It is stronger' \
                             ', healthier and less likely to tangle than the ordinary human'

        # create the African human hair instance to be populated on contentpage
        african = Hair()
        african.image = 'images/african.png'
        african.name = 'Virgin Afrian Human Hair'
        african.price = '$88.00'
        african.color = 'Natural Black'
        african.length = '16-26 INCH'
        african.texture = 'Straight Hair'
        african.weight = '95-100g/pc'
        african.quality = '7A Grade High Quality  100% Virgin Hair,Tangle Free, No Shedding'
        african.description = 'African human hair is regarded as the finest elite quality human hair. It is stronger' \
                             ', healthier and less likely to tangle than the ordinary human'

        # this array holds all the human hair instances to be used in Mainhandler
        self.hair_Category = [brazilian, indian, peruvian, malaysian, african]
