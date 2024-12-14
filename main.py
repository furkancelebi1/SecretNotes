from tkinter import *

FONT = ("verdana", 15 , "bold")
window = Tk()
window.title("Secret Notes")
window.config(padx=30, pady=30)

#uı
photo = PhotoImage(file="ımage.png")
photo_label = Label(image=photo)
photo_label.pack()

title_info_label = Label(text="Enter your title", font=FONT)
title_info_label.pack()

title_entry = Entry(width=30)
title_entry.pack()

input_info_label = Label(text="Enter your secret", font=FONT)
input_info_label.pack()

input_text = Text(width=30, height=25)
input_text.pack()

master_secret_label= Entry(width=30)
master_secret_label.pack()

save_button = Button(text="Save & Encrypt")
save_button.pack()

decrypt_button = Button(text="Encrypt")
decrypt_button.pack()

window.mainloop()