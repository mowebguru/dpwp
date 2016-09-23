'''Name   : Mohamed A. KAMARA
   Course : Design Patterns for Web Programming - Online
   File   : Week 4 - Dynamic Site
   Date   :Sept. 23, 2016'''

class Hair(object): # the data class the will be used as template for all the hair categories
    def __init__(self):
        self.image = ''
        self.price = ''
        self.color = ''
        self.length = ''
        self.texture = ''
        self.weight = ''
        self.quality = ''
        self.description = ''

class HumanHair(object): # the HumanHair objects created from the Hair class
    def __init__(self):
        brazilian = Hair()
        brazilian.name = 'Virgin Brazalian Human Hair'
        brazilian.price = '$90.00'
        brazilian.image = 'images/brazilian.png'
        brazilian.color = 'Natural Black'
        brazilian.length = '8-30 INCH'
        brazilian.texture = 'Brazilian Body Wave'
        brazilian.weight = '95-100g/pc'
        brazilian.quality = '7A Grade High Quality  100% Virgin Hair,Tangle Free, No Shedding'
        brazilian.description = 'Brazilian Human Hair offers the most natural look and feel. It is remarkably soft with a ' \
                                'shine and movement that is not easily duplicated.'

        indian = Hair()
        indian.name = 'Virgin Indian Human Hair'
        indian.price = '$75.00'
        indian.image = 'images/indian.png'
        indian.color = 'Natural Black'
        indian.length = '8-30 INCH'
        indian.texture = 'Indian Body Wave'
        indian.weight = '95-100g/pc'
        indian.quality = '7A Grade High Quality  100% Virgin Hair,Tangle Free, No Shedding'
        indian.description = 'Indian human hair is regarded as the finest elite quality human hair. It is stronger' \
                             ', healthier and less likely to tangle than the ordinary human'

        peruvian = Hair()
        peruvian.name = 'Virgin Peruvian Human Hair'
        peruvian.price = '$65.00'
        peruvian.image = 'images/peruvian.png'
        peruvian.color = 'Natural Black'
        peruvian.length = '8-30 INCH'
        peruvian.texture = 'Straight Hair'
        peruvian.weight = '95-100g/pc'
        peruvian.quality = '7A Grade High Quality  100% Virgin Hair,Tangle Free, No Shedding'
        peruvian.description = 'Peruvian human hair is regarded as the finest elite quality human hair. It is stronger' \
                             ', healthier and less likely to tangle than the ordinary human'

        malaysian = Hair()
        malaysian.name = 'Virgin Malaysian Human Hair'
        malaysian.price = '$80.00'
        malaysian.image = 'images/malaysian.png'
        malaysian.color = 'T1B/4/27'
        malaysian.length = '16-26 INCH'
        malaysian.texture = 'Ombre Straight Hair'
        malaysian.weight = '95-100g/pc'
        malaysian.quality = '7A Grade High Quality  100% Virgin Hair,Tangle Free, No Shedding'
        malaysian.description = 'Malaysian human hair is regarded as the finest elite quality human hair. It is stronger' \
                             ', healthier and less likely to tangle than the ordinary human'

        african = Hair()
        african.name = 'Virgin Afrian Human Hair'
        african.price = '$88.00'
        african.image = 'images/african.png'
        african.color = 'Natural Black'
        african.length = '16-26 INCH'
        african.texture = 'Straight Hair'
        african.weight = '95-100g/pc'
        african.quality = '7A Grade High Quality  100% Virgin Hair,Tangle Free, No Shedding'
        african.description = 'African human hair is regarded as the finest elite quality human hair. It is stronger' \
                             ', healthier and less likely to tangle than the ordinary human'

        self.hair_data = [brazilian, indian, peruvian, malaysian, african] # this array holds all the human hair instances to be used in Mainhandler