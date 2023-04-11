class Human:
    name = "Aslıhan"
    def talk(self, sentence):
        name = "Ercan"
        print(f"{self.name}: {sentence}")
    def walk(self):
        print(f"{self.name} is walking")


human1 = Human
human1.name = "Enes"
human1.talk("Merhaba", "Samet")
human1.walk 
print(human1)

human2 = Human()
human2.name = "Cem"
human2.talk("Selam", "Mevlüt")
human2.walk()
print(human2)


