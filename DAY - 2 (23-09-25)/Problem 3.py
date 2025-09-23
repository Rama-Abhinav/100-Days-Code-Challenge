# PROBLEM STATEMENT 
""" Count the Vowels in a given string """

Word = input("Enter Word: ").lower()
Vowel_Count = 0
vowel_set = {"a", "e", "i", "o", "u"}
for letter in Word:
    for vowel in vowel_set:
        if letter == vowel:
            Vowel_Count += 1

print(f"The Number of Vowels in the word {Word} is {Vowel_Count}\n")

# One line code for finding no.of vowels
print(sum(letter in "aeiou" for letter in Word))  # Generator Expressions

""" Counting Occurance of each vowel in a string using dictionary """

Vowel_Dict = {
    "a":0,
    "e":0,
    "i":0,
    "o":0,
    "u":0
}

for letter in Word:
    for vowel in vowel_set:
        if letter == vowel:
            Vowel_Dict[vowel] += 1

VL = Vowel_Dict.items()
for i in VL:
    print(i)