# Mad Lib Generator

def main():
    authorName = getAuthorName()
    askUserForInput(authorName)

def askUserForInput(authorName):
    print("\nOkay we need some words\n")
    place = str(input("Name a place: "))
    country = str(input("Name a country: "))
    music = str(input("Name a music genre: "))
    sport = str(input("Name a sport: "))
    fictionCharacter = str(input("Name a fictional character: "))
    print("\nOkay we have everything we need\n")
    putTogetherMadlib(place, country, music, sport, fictionCharacter, authorName)

def getAuthorName():
    authorName = str(input("Hello, what is your name? "))
    return authorName

def putTogetherMadlib(place, country, music, sport, fictionCharacter, authorName):
    print(f"Long ago, maybe a couple days ago.\n{authorName.title()} and {fictionCharacter.title()} went to {country.title()} where they played {sport}.\nDuring the tournament they were playing {music}. \nAfterwards they went to the {place}")
    print(f"\nA madlib by, {authorName}")
main()