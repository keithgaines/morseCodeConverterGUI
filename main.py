import tkinter as tk

# alphabet and morse code values as separate lists
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', ' ']

# combines alphabet:morse lists into converter_dict dictionary. Alphabet is keys. Morse is values.
converter_dict = {alphabet[i]: morse[i] for i in range(0,26)}
converted_morse = []


def convert(): 
    letter = input_word.get() # gets input from input_word entry
    lowercase_word = letter.lower() # converts input to lowercase
    your_word.config(text=lowercase_word) # puts lowercase input on your word label
    for i in lowercase_word: # processes whitespace characters as whitespace
        if i == ' ':
            i == ' '
        else: # gets value from key, assigns it to letters variable, and appends letter variable to converted_morse
            letters = converter_dict[i] 
            converted_morse.append(letters) 
    morse_output = ' '.join([str(item) for item in converted_morse]) 
    translated_output.config(text=morse_output) 
    converted_morse.clear() 

# ---------- UI Setup ---------- # 
window = tk.Tk()
window.title("Morse Code Converter")
window.geometry("900x300")

title = tk.Label(padx=10)
title.config(text="Morse Code Converter", font=("Times new roman", 35, "bold"))
title.grid(row=0, column=0, columnspan=2, sticky=tk.E)

prompt = tk.Label()
prompt.config(text="Please enter a word or phrase: ", font=("Times new roman", 20))
prompt.grid(row=1, column=0, sticky=tk.W)

input_word = tk.Entry(font=("Times new roman", 20))
input_word.grid(row=1, column=1, columnspan=2, sticky=tk.W)

your_word = tk.Label(font=("Times new roman", 20))
your_word.grid(row=2, column=0)

imci = tk.Label()
imci.config(text="in morse code is ", font=("Times new roman", 20))
imci.grid(row=2, column=1, sticky=tk.W)

translated_output = tk.Label(font=("Times new roman", 20))
translated_output.config(text=" ")
translated_output.grid(row=2, column=2)

convert_button = tk.Button(text="Convert", font=("Times new roman", 20), command=convert)
convert_button.grid(row=3, column=0, sticky=tk.E)

window.mainloop()

