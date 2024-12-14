from tkinter import *
from tkinter import messagebox

FONT = ("verdana", 15 , "bold")
window = Tk()
window.title("Secret Notes")
window.config(padx=30, pady=30)

def save_and_encrypt_notes():
    title = title_entry.get()
    message = input_text.get("1.0" , END)
    master_secret = master_secret_input.get()
    if len(title) == 0 or len(message) == 0 or len(master_secret) == 0 :
        messagebox.showinfo(title="Error!", message="Please enter all info.")
    else:
        try:
            with open("mysecret.txt","a") as data_file:
                data_file.write(f"\n{title}\n{message}")
        except FileNotFoundError:
            with open("mysecret.txt","w") as data_file:
                data_file.write(f"\n{title}\n{message}")
        finally:
            title_entry.delete(0, END)
            master_secret_input.delete(0, END)
            input_text.delete("1.0", END)
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

master_secret_input= Entry(width=30)
master_secret_input.pack()

save_button = Button(text="Save & Encrypt",command=save_and_encrypt_notes)
save_button.pack()

decrypt_button = Button(text="Encrypt")
decrypt_button.pack()

window.mainloop()