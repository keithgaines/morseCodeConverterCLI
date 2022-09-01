alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', ' ']


def convert(letter): 
    for i in letter:
        if i == ' ':
            i == ' '
        else:
            letters = converter_dict[i]
            converted_morse.append(letters)

converter_dict = {alphabet[i]: morse[i] for i in range(0,26)}
converted_morse = []

word = input("Please enter a word or phrase: ")
lowercase_word = word.lower()
letter = [i for i in lowercase_word]

convert(letter)
morse_output = ' '.join([str(item) for item in converted_morse])
print(f"'{word}' in morse code is {morse_output}")
