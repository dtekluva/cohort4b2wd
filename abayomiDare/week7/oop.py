from playsound import playsound
class Animal: 

    # INSTANCE ATTRIBUTE
    def __init__(self, name, type, furColor):
        self.name = name
        self.type = type
        self.furColor = furColor
    def describe(self):
        print(f"""
        I am {self.name}
        with a furcolor {self.furColor}
        belong to {self.type}
        """)
        playsound('cat_Meow.mp3')

cat = Animal('Smudge','Snowshoe','Tuxedo')
cat.describe()

