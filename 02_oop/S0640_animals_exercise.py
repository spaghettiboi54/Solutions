"""
Opgave "Animals"

Som altid skal du læse hele øpgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Alt, hvad du har brug for at vide for at løse denne opgave, finder du i cars_oop- og rpg1-filerne.

Definer en klasse ved navn Animal.
Hvert objekt i denne klasse skal have attributterne name (str), sound (str), height (float),
weight (float), legs (int), female (bool).
I parentes står data typerne, dette attributterne typisk har.

Tilføj til klassen meningsfulde metoder __init__ og __repr__.
Kald disse metoder for at oprette objekter af klassen Animal og for at udskrive dem i hovedprogrammet.

Skriv en klassemetode ved navn make_noise, som udskriver dyrets lyd i konsollen.
Kald denne metode i hovedprogrammet.

Definer en anden klasse Dog, som arver fra Animal.
Hvert objekt af denne klasse skal have attributterne tail_length (int eller float)
og hunts_sheep (typisk bool).

Tilføj til klassen meningsfulde metoder __init__ og __repr__.
Ved skrivning af konstruktoren for Dog skal du forsøge at genbruge kode fra klassen Animal.
Kald disse metoder for at oprette objekter af klassen Hund og for at udskrive dem i hovedprogrammet.

Kald metoden make_noise på Dog-objekter i hovedprogrammet.

Skriv en klassemetode ved navn wag_tail for Dog.
Denne metode udskriver i konsollen noget i stil med
"Hunden Snoopy vifter med sin 32 cm lange hale"
Kald denne metode i hovedprogrammet.

Skriv en funktion mate(mother, father). Begge parametre er af typen Dog.
Denne funktion skal returnere et nyt objekt af typen Dog.
I denne funktion skal du lave meningsfulde regler for den nye hunds attributter.
Sørg for, at denne funktion kun accepterer hunde med det korrekte køn som argumenter.

I hovedprogrammet kalder du denne metode og udskriver den nye hund.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""

class Animal:
    def __init__(self, name, weight, sound, height, legs, female):
        self._name = name
        self._weight = weight
        self._sound = sound
        self._height = height
        self._legs = legs
        self._female = female

    def __repr__(self):
        return f"this animal is a {self._name}, it weighs {self._weight} kg, calling it a female would be a {self._female} statement"

    def make_noise(self):
        print(self._sound)




class Dog(Animal):
    def __init__(self, name, weight, sound, height, tail_length, female, hunts_sheep):
        self._name = name
        self._weight = weight
        self._sound = sound
        self._height = height
        self._female = female
        self._tail_length = tail_length
        self._hunts_sheep = hunts_sheep

    def wag_tail(self):
        print(f"the dog wags its {self._tail_length} cm long tail")


    def mate(dog1, dog2,name):  #HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH spørg uli
        if (dog1._female == dog2._female):
            print("dogs must be opposite gender to mate")
            return
        return Dog(name, dog1._weight, dog2._sound, dog1._height, dog2._tail_length, dog1._female, dog2._hunts_sheep)






animal1 = Animal("cheetah", 200, "rawr", legs=4, female=True, height=22)


