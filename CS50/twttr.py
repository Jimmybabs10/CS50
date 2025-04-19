vowels = ['a', 'e', 'i', 'o', 'u']
text = input('INPUT:  ')

for letter in text:
    if letter in vowels:
        text = text.replace(letter,'')

print(text)
