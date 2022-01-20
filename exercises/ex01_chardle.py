"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730507751"

Word: str = input("Enter a 5-character word: ")
Word = Word.lower()

if len(Word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

Character: str = input("Enter a single character: ")
Character = Character.lower()

if len(Character) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + Character + " in " + Word)

Count: int = 0

if Character == Word[0]:
    print(Character + " found at index 0")
    Count = Count + 1
if Character == Word[1]:
    print(Character + " found at index 1")
    Count = Count + 1
if Character == Word[2]:
    print(Character + " found at index 2")
    Count = Count + 1
if Character == Word[3]:
    print(Character + " found at index 3")
    Count = Count + 1
if Character == Word[4]:
    print(Character + " found at index 4")
    Count = Count + 1

if Count != 0:
    if Count == 1:
        str(Count)
        print(str(Count) + " instance of " + Character + " found in " + Word)
    else:
        str(Count)
        print(str(Count) + " instances of " + Character + " found in " + Word)
else:
    Count1: str = "No"
    print(str(Count1) + " instances of " + Character + " found in " + Word)