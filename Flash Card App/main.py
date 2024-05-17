 #Flash Card App

import tkinter
import pandas
import random

#---------------------------------------------------------------------------------
#                                   User Interface
color = "#B1DDC6"
color2 = "#91C2AF"
color3 = "#FFFFFF"

window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=color)

#--Functions--

word_data = pandas.read_csv("100 Days of Code\\Day 31 Flash Card App\data\\french_words.csv")
current_card = 0
start = int()

#   Word Picker
def word_picker():
    global word_data
    global current_card

    canvas.itemconfig(card_background, image=flash_front)
    l_language.config(bg=color3, fg="black")
    l_word.config(bg=color3, fg="black")

    length_of_data = (len(word_data) - 1)
    random_index = random.randint(0, length_of_data)

    l_language.config(text="French", font=("Arial", 40, "italic"))

    current_card = random_index
    l_word.config(text=word_data["French"][random_index])


def flip_card():
    global word_data
    global current_card

    canvas.itemconfig(card_background, image=flash_back)
    l_language.config(bg=color2, fg=color3)
    l_word.config(bg=color2, fg=color3)

    l_language.config(text="English")
    l_word.config(text=word_data["English"][current_card])

canvas = tkinter.Canvas(width=800, height=526)

#--Images--
#   front card
flash_front = tkinter.PhotoImage(file="100 Days of Code/Day 31 Flash Card App/images/card_front.png")
flash_back = tkinter.PhotoImage(file="100 Days of Code\Day 31 Flash Card App\images\card_back.png")
card_background = canvas.create_image(400, 263, image=flash_front)
canvas.grid(column=0, row=0, columnspan=2, rowspan=3)
canvas.config(bg=color, highlightthickness=0)

#   Button Images
#       Right Button
i_right = tkinter.PhotoImage(file="100 Days of Code\\Day 31 Flash Card App\\images\\right.png")
#       Wrong Button
i_wrong = tkinter.PhotoImage(file="100 Days of Code\\Day 31 Flash Card App\\images\\wrong.png")

#--Buttons--
button_row = 3

b_wrong = tkinter.Button(image=i_wrong, command=flip_card)
b_wrong.config(highlightthickness=0)
b_wrong.grid(column=0, row=button_row)

b_right = tkinter.Button(image=i_right, command=word_picker)
b_right.config(highlightthickness=0)
b_right.grid(column=1, row=button_row)

#--Labels--
#   Language
l_language = tkinter.Label(text="French", font=("Arial", 40, "italic"))
l_language.config(bg=color3)
l_language.grid(column=0, row=1, columnspan=2)

#   Word
l_word = tkinter.Label(text="Word", font=("Arial", 60, "bold"))
l_word.config(bg=color3)
l_word.grid(column=0, row=2, columnspan=2)

window.mainloop()