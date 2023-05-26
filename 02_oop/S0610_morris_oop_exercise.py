"""
Opgave "Morris The Miner" (denne gang objekt orienteret)

Som altid skal du læse hele øpgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Omskriv din oprindelige Morris-kode til en objektorienteret version.

Definer en klasse Miner med attributter som sleepiness, thirst osv.
og metoder som sleep, drink osv.
Opret Morris og initialiser hans attributter ved at kalde konstruktoren for Miner:
morris = Miner()

Hvis du går i stå, så spørg google, de andre elever eller læreren (i denne rækkefølge).

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""


class Miner:
    def __init__(self):
        self._sleepiness = 0
        self._gold = 0
        self._hunger = 0
        self._vodka = 0
        self._thirst = 0
        self._turn = 0

    def __repr__(self):
        return f"sleepiness: {self._sleepiness} hunger: {self._hunger} vodka: {self._vodka} turn: {self._turn} thirst: {self._thirst} gold: {self._gold} "

    def mine(self):
        self._sleepiness += 5
        self._thirst += 5
        self._hunger += 5
        self._gold += 5
        self._turn += 1


    def sleep(self):
        self._sleepiness -= 10
        self._thirst += 1
        self._hunger += 1
        self._turn += 1

    def drink(self):
        if(self._vodka < 1):
            print("you don't have any vodka, turn wasted")
        else:
            self._thirst -= 15
            self._vodka -= 1
        self._hunger -= 1
        self._sleepiness += 5
        self._turn += 1

    def eat(self):
        self._hunger -= 20
        self._gold -= 2
        self._sleepiness += 5
        self._turn += 1
        self._thirst -= 5

    def buy_whisky(self):
        self._vodka += 1
        self._gold -= 1
        self._sleepiness += 5
        self._hunger += 1
        self._turn += 1


Morris = Miner()
print(repr(Morris))
Morris.mine()
print(repr(Morris))
