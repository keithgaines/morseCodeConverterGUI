import tkinter as tk

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', ' ']

converter_dict = {alphabet[i]: morse[i] for i in range(0,26)}
converted_morse = []

def convert(): 
    letter = input_word.get()
    lowercase_word = letter.lower()
    your_word.config(text=lowercase_word)
    for i in lowercase_word:
        if i == ' ':
            i == ' '
        else:
            letters = converter_dict[i]
            converted_morse.append(letters)


window = tk.Tk()
window.title("Morse Code Converter")
window.geometry("500x300")

title = tk.Label()
title.config(text="Morse Code Converter")
title.grid(row=0, column=1, columnspan=2)

prompt = tk.Label()
prompt.config(text="Please enter a word or phrase: ")
prompt.grid(row=1, column=0)

input_word = tk.Entry()
input_word.grid(row=1, column=1, columnspan=2)

your_word = tk.Label()
your_word.grid(row=2, column=0)

imci = tk.Label()
imci.config(text="in morse code is ")
imci.grid(row=2, column=1)

translated_output = tk.Label()
translated_output.config(text=converted_morse)
translated_output.grid(row=2, column=2)

convert_button = tk.Button(text="Convert", command=convert)
convert_button.grid(row=3, column=1)

window.mainloop()
print(converted_morse)
