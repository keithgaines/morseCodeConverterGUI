import tkinter as tk


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
your_word.config(text="loremipsum")
your_word.grid(row=2, column=0)

imci = tk.Label()
imci.config(text="in morse code is ")
imci.grid(row=2, column=1)

translated_output = tk.Label()
translated_output.config(text="lorem")
translated_output.grid(row=2, column=2)

convert_button = tk.Button(text="Convert")
convert_button.grid(row=3, column=1)

window.mainloop()