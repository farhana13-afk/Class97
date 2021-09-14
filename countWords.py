words = input("Enter a quote")
characterCount = 0
wordCount = 1

for i in words:
    characterCount = characterCount + 1
    if(i == " ") : 
        wordCount = wordCount + 1

print("Number of Characters:")
print(characterCount)
print("Number of Words")
print(wordCount)