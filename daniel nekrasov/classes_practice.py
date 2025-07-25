
#doing this for practice
# we forgot to add comments

class Dog:

    # constructor
    def __init__(self, hair_color, eye_color, breed, name, age):
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.breed = breed
        self.name = name
        self.age = age

    def what_breed(self):
        print(f"The dogs breed is {self.breed}")

    def what_age(self):
        print(f"The dogs age is {self.age}")

    def what_hair_color(self):
        print(f"the color is {self.hair_color}")

    def what_eye_color(self):
        print(f"the eye color is {self.eye_color}")

    def what_name(self):
        print(f"the name is {self.name}")

    

our_dog = Dog('white', 'black', 'White Lab', 'Daisy', 11)
our_dog.what_age()

class GameObject:

    # constructor
    def __init__(self):
        pass

    def update(self, dt):
        pass

    def draw(self):
        pass

#print(f"The dogs age is {our_dog.age}")
#print(f"The dogs breed is {our_dog.breed}")































class Whiteboard:
#                class for whiteboard
                #instantiate our charachteristics for whiteboard object
    def __init__(self, white, smooth, writing, two_sided):
        #member varibles
        self.white = white
        self.smooth = smooth
        self.writing = writing
        self.two_sided = two_sided

        def writing(self, has_writing):

            if has_writing == True:
                print("has writing on it")
            else:
                print("no writing")
                

    
        