"""Opgave "Number pyramid"

Som altid skal du læse hele øpgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Se de første 93 sekunder af denne video: https://www.youtube.com/watch?v=NsjsLwYRW8o

Skriv en funktion "pyramid", der producerer de tal, der er vist i videoen.
Funktionen har en parameter, der definerer, hvor mange talrækker der skal produceres.
Funktionen udskriver tallene i hver række og også deres sum.

I hovedprogrammet kalder du funktionen med fx 7 som argument.

Tilføj en mere generel funktion pyramid2.
Denne funktion har som andet parameter en liste med tallene i
pyramidens øverste række.

I hovedprogrammet kalder du pyramid2 med 1, 2, 3, ..., 10 som det første argument
og en liste med tal efter eget valg som det andet argument.
Afprøv forskellige lister som andet argument.

Hvis du ikke aner, hvordan du skal begynde, kan du åbne S1620_pyramid_help.py og starte derfra

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""
def create_pyramid(lines):
    pyramid = []
    initial_numbers = [1,1]
    pyramid.append(initial_numbers)
    for new_line_index in range(1, lines): #index of
        pyramid.append([])
        for index in range(len(pyramid[-2]) - 1): #iterating over the index of each item in previous line
            pyramid[new_line_index].append(pyramid[new_line_index - 1][index])
            if pyramid[new_line_index - 1][index] + pyramid[new_line_index - 1][index + 1] == new_line_index + 1:
                pyramid[new_line_index].append(new_line_index + 1)
        pyramid[new_line_index].append(pyramid[new_line_index - 1][-1])
    return pyramid


pyramid1 = create_pyramid(6)
for i in pyramid1:
    print(i)
