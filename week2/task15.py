word = input("Type the first word: ")
word1 = input("Type the second word: ")
if word < word1:
    print(f"{word1} comes alphabetically last")
elif word > word1:
    print(f"{word} comes alphabetically last")
elif word == word1:
    print("These are same!")
