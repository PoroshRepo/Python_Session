
class Human:
    name = ''
    skin_tone = ''
    height = 0
    weight = 0
    
    nationality = ''
    gender = ''
    def __init__(self, name, skin_tone, height, weight):
        self.name = name
        self.skin_tone = skin_tone
        self.height = height
        self.weight = weight
    
    def __init__(self, name, nationality, gender):
        self.name = name
        self.nationality = nationality
        self.gender = gender

    def show(self):
        print("The name of the person: "+self.name)
        print("Skin Tone: "+self.skin_tone)
        print("Height: "+str(self.height))
        print("Weight: "+str(self.weight))
    
    def ratio(self):
        name = self.name
        ratio = self.weight/self.height
        
        print("Name of the person: "+name)
        print("The ratio of height and weight: "+str(ratio))
    
    

#human_obj = Human("Porosh", "Brown", 178, 75)
human_ref_obj = Human("Porosh", "Bangladeshi", "Male")

human_obj.show()
human_obj.ratio()


