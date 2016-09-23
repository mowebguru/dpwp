class Hair(object): # the data class the will be used as template for all the hair categories
    def __init__(self):
        self.image = ''
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
        brazilian.image = 'images/brazilian.png'
        brazilian.color = 'Natural Black'
        brazilian.length = '8-30 INCH'
        brazilian.texture = 'Brazilian Body Wave'
        brazilian.weight = '95-100g/pc'
        brazilian.quality = ''