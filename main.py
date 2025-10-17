import tkinter
import pandas
import random
from tkinter import messagebox

BACKGROUND_COLOR = "#B1DDC6"
BACKGROUND_FOR_ENGLISH = "#91C2AF"

timer = None  #  keep track of the current after() timer

def right_clicked(french_word):

    global timer
    window.after_cancel(timer)  # stop the previous timer

    df = pandas.read_csv("data/french_words.csv")
    df_with_it = df[df["French"] == french_word]
    df = df[df["French"] != french_word]

    df.to_csv("data/french_words.csv", index=False)
    df_with_it.to_csv("data/french_words_known.csv",mode="a", header=False,index=False)

    shuffle()  #  show next card

def wrong_clicked():
    global timer
    window.after_cancel(timer)
    shuffle()

def restart():
    messagebox.showinfo("", "Game has restarted")
    global timer
    if timer:
        window.after_cancel(timer)

    try:
        known = pandas.read_csv("data/french_words_known.csv", header=None, names=["French", "English"])
    except FileNotFoundError:
        messagebox.showerror("Error", "No known words file found. Restarting empty game.")
        return

    # Load existing words
    try:
        words = pandas.read_csv("data/french_words.csv")
    except FileNotFoundError:
        words = pandas.DataFrame(columns=["French", "English"])

    # Merge known words back without duplicates
    all_words = pandas.concat([words, known]).drop_duplicates(subset="French", keep="first")

    # Save back to french_words.csv
    all_words.to_csv("data/french_words.csv", index=False)

    # Clear known words
    open("data/french_words_known.csv", "w").close()


def shuffle_to_english(english_word):
    title_label.config(text="English", bg=BACKGROUND_FOR_ENGLISH)
    word_label.config(text=english_word, bg=BACKGROUND_FOR_ENGLISH)


def shuffle():
    global timer  # we will reuse this variable
    df = pandas.read_csv("data/french_words.csv")
    french_words = df["French"]
    try:
        french_word = random.choice(french_words)
    except IndexError:
        messagebox.showinfo("🎉","Congregations words are finished ,You have to restart now")#emoji not showing
        return

    english_word = df[df["French"] == french_word]["English"].iloc[0]  # picks even if there are same world appeared twice

    title_label.config(text="French", bg="White")
    word_label.config(text=french_word, bg="White")
    canvas.itemconfig(canvas_img, image=card_front_img)

    def shuffle_to_eng():
        shuffle_to_english(english_word)
        card_back_img = tkinter.PhotoImage(file="images/card_back.png")
        canvas.itemconfig(canvas_img, image=card_back_img)
        canvas.image = card_back_img

        # schedule next shuffle (3 sec later)
        global timer
        timer = window.after(3000, shuffle)

    # cancel any previous timer before scheduling a new one
    if timer:
        window.after_cancel(timer)
    timer = window.after(3000, shuffle_to_eng)


window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = tkinter.PhotoImage(file="images/card_front.png")
canvas_img = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)

title_label = tkinter.Label(text="Title", font=("Ariel", 40, "italic"), fg="black", bg="white")
title_label.place(x=350, y=150)

word_label = tkinter.Label(text="Word", font=("Ariel", 60, "bold"), fg="black", bg="white")
word_label.place(x=310, y=263)

right_image = tkinter.PhotoImage(file="images/right.png")
right_button = tkinter.Button(image=right_image, highlightthickness=0, borderwidth=0, bg=BACKGROUND_COLOR,
                              command=lambda: right_clicked(word_label.cget("text")))
right_button.grid(row=1, column=1)

wrong_image = tkinter.PhotoImage(file="images/wrong.png")
wrong_button = tkinter.Button(image=wrong_image, highlightthickness=0, borderwidth=0, bg=BACKGROUND_COLOR,
                              command = wrong_clicked)
wrong_button.grid(row=1, column=0)

restart_image = tkinter.PhotoImage(file="images/restart.png")
restart_button = tkinter.Button(image=restart_image, highlightthickness=0,command=restart)
restart_button.place(x=380,y=550)


shuffle()
window.mainloop()
