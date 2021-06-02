from playsound import playsound
class Animal: 
    # INSTANCE ATTRIBUTE
    base_dir = "/home/abayomidare/Desktop/Univelcity/cohort4b2wd/abayomiDare/"
    
    def __init__(self, name, type, furColor, sound):
        self.name = name
        self.type = type
        self.furColor = furColor
        self.sound = sound

    def describe(self):
        print(f"""dog
        I am {self.name}
        with a furcolor {self.furColor}
        belong to {self.type}
        """)
        self.make_sound()

    def make_sound(self):

        playsound(f"{self.base_dir}{self.sound}")


        



cat = Animal('Smudge','Snowshoe','Tuxedo', "cat_Meow.mp3")
cat.describe()

dog = Animal('Billy','Terrier Mixed Breed', 'Brown',  "Terrier Mixed Breed Snarl .mp3")
dog.describe()

